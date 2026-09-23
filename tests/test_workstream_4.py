"""Project/Source lifecycle and anti-elevation tests for Workstream 4."""

from __future__ import annotations

from pathlib import Path
import shutil
import sqlite3
import tempfile

import pytest

from context_engine.adapters.sqlite_state import (
    CURRENT_SCHEMA_VERSION,
    PersistedSourceRegistration,
    SQLiteStateStore,
    StateCompatibilityError,
)
from context_engine.application.lifecycle import (
    ApplicableSourceUniverse,
    Availability,
    BoundaryAdequacy,
    RegisteredSource,
    ScopeInputs,
    effective_sources,
)


@pytest.fixture
def controlled_dir() -> Path:
    directory = Path(tempfile.mkdtemp(dir=Path.home() / "temp", prefix="context-engine-ws4-"))
    try:
        yield directory
    finally:
        shutil.rmtree(directory)


def source(identity: str, project: str, locator: str = "same") -> RegisteredSource:
    return RegisteredSource(identity, project, "registered-type", "docs", locator=locator)


def test_project_source_identity_and_default_isolation_ignore_shared_locator() -> None:
    local, external = source("source-a", "project-a"), source("source-b", "project-b")
    assert effective_sources("project-a", (local, external), ScopeInputs()) == (local,)
    assert local.identity != external.identity
    assert local.locator == external.locator


def test_cross_project_requires_task_relationship_and_distinct_authorizations() -> None:
    local, external = source("source-a", "project-a"), source("source-b", "project-b")
    prerequisites = (
        ScopeInputs(governed_relationship=True, requester_authorized=True, consumer_disclosure_authorized=True),
        ScopeInputs(task_requires_external=True, requester_authorized=True, consumer_disclosure_authorized=True),
        ScopeInputs(task_requires_external=True, governed_relationship=True, requester_authorized=True),
        ScopeInputs(task_requires_external=True, governed_relationship=True, consumer_disclosure_authorized=True),
    )
    for inputs in prerequisites:
        assert effective_sources("project-a", (local, external), inputs) == (local,)
    allowed = ScopeInputs(True, True, True, True)
    assert effective_sources("project-a", (local, external), allowed) == (local, external)


def test_registration_and_relationship_do_not_create_semantic_elevation() -> None:
    registered = source("source-a", "project-a")
    for elevated_field in ("authority", "governance_state", "currentness", "selected", "consumer_disclosure_authorized"):
        assert not hasattr(registered, elevated_field)


def test_source_scope_is_not_project_wide_and_requires_lifecycle_fields() -> None:
    narrowed = RegisteredSource("source-a", "project-a", "registered-type", "limited-docs")
    assert narrowed.scope == "limited-docs"
    with pytest.raises(ValueError):
        RegisteredSource("", "project-a", "registered-type", "docs")


def test_asu_preserves_basis_and_is_not_registered_set_adequacy() -> None:
    unavailable = RegisteredSource("source-a", "project-a", "registered-type", "docs", Availability.UNAVAILABLE)
    asu = ApplicableSourceUniverse("request-a", (unavailable,), BoundaryAdequacy.KNOWN_INCOMPLETE, "governed scoped inventory")
    same_registered_set = ApplicableSourceUniverse("request-b", (unavailable,), BoundaryAdequacy.INDETERMINATE, "inspection unavailable")
    assert asu.adequacy is BoundaryAdequacy.KNOWN_INCOMPLETE
    assert same_registered_set.adequacy is BoundaryAdequacy.INDETERMINATE
    assert unavailable.availability is not Availability.ABSENT
    with pytest.raises(ValueError):
        ApplicableSourceUniverse("request-c", (), BoundaryAdequacy.ADEQUATE, "")


@pytest.mark.parametrize("availability", (Availability.UNAVAILABLE, Availability.INACCESSIBLE, Availability.UNAUTHORIZED, Availability.UNSUPPORTED, Availability.PARTIAL, Availability.NOT_INSPECTED))
def test_bounded_failure_states_are_not_silently_absent(availability: Availability) -> None:
    registered = RegisteredSource("source-a", "project-a", "registered-type", "docs", availability)
    assert registered.availability is availability
    assert registered.availability is not Availability.ABSENT


def test_lifecycle_persists_and_restarts_with_project_isolation(controlled_dir: Path) -> None:
    database = controlled_dir / "state.sqlite"
    store = SQLiteStateStore(database)
    store.initialize()
    first = PersistedSourceRegistration("project-a", "source-semantic-a", "registered-type", "docs", Availability.PARTIAL.value, "same")
    second = PersistedSourceRegistration("project-b", "source-semantic-b", "registered-type", "docs", Availability.AVAILABLE.value, "same")
    store.save_source_registration(first)
    store.save_source_registration(second)
    restarted = SQLiteStateStore(database)
    assert restarted.source_registrations_for_project("project-a") == (first,)
    assert restarted.source_registrations_for_project("project-b") == (second,)
    assert restarted.source_registrations_for_project("project-c") == ()


def test_source_registration_row_id_is_not_semantic_identity_or_cross_project_key(controlled_dir: Path) -> None:
    store = SQLiteStateStore(controlled_dir / "state.sqlite")
    store.initialize()
    identity = "source-semantic"
    one = PersistedSourceRegistration("project-a", identity, "registered-type", "docs", Availability.AVAILABLE.value)
    two = PersistedSourceRegistration("project-b", identity, "registered-type", "docs", Availability.AVAILABLE.value)
    store.save_source_registration(one)
    store.save_source_registration(two)
    assert store.source_registrations_for_project("project-a") == (one,)
    assert store.source_registrations_for_project("project-b") == (two,)


def test_lifecycle_schema_migrates_deterministically_from_version_one(controlled_dir: Path) -> None:
    database = controlled_dir / "version-one.sqlite"
    with sqlite3.connect(database) as connection:
        connection.execute("CREATE TABLE schema_version (version INTEGER NOT NULL)")
        connection.execute("INSERT INTO schema_version VALUES (1)")
        connection.execute("CREATE TABLE evidence (row_id INTEGER PRIMARY KEY, project_identity TEXT NOT NULL, semantic_identity TEXT NOT NULL, historical_reference TEXT NOT NULL, UNIQUE(project_identity, semantic_identity))")
        connection.execute("CREATE TABLE audit (row_id INTEGER PRIMARY KEY, project_identity TEXT NOT NULL, outcome TEXT NOT NULL, detail TEXT NOT NULL)")
    SQLiteStateStore(database).initialize()
    with sqlite3.connect(database) as connection:
        version = connection.execute("SELECT version FROM schema_version").fetchone()
        table = connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='source_registration'").fetchone()
    assert version == (CURRENT_SCHEMA_VERSION,)
    assert table == ("source_registration",)


def test_duplicate_lifecycle_write_rolls_back_without_partial_state(controlled_dir: Path) -> None:
    store = SQLiteStateStore(controlled_dir / "state.sqlite")
    store.initialize()
    original = PersistedSourceRegistration("project-a", "source-semantic", "registered-type", "docs", Availability.AVAILABLE.value)
    store.save_source_registration(original)
    with pytest.raises(sqlite3.IntegrityError):
        store.save_source_registration(original)
    assert store.source_registrations_for_project("project-a") == (original,)


def test_incompatible_lifecycle_schema_fails_closed(controlled_dir: Path) -> None:
    database = controlled_dir / "incompatible.sqlite"
    with sqlite3.connect(database) as connection:
        connection.execute("CREATE TABLE schema_version (version INTEGER NOT NULL)")
        connection.execute("INSERT INTO schema_version VALUES (99)")
    with pytest.raises(StateCompatibilityError):
        SQLiteStateStore(database).initialize()
