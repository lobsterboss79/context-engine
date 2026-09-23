"""Bootstrap, configuration, SQLite, and anti-elevation tests for Workstream 3."""

from __future__ import annotations

from pathlib import Path
import shutil
import sqlite3
import tempfile

import pytest

from context_engine.adapters.sqlite_state import PersistedEvidence, SQLiteStateStore, SecretValueError, StateCompatibilityError
from context_engine.application.bootstrap import GovernanceEstablishmentError, establish_bootstrap, load_project_configuration


@pytest.fixture
def controlled_dir() -> Path:
    directory = Path(tempfile.mkdtemp(dir=Path.home() / "temp", prefix="context-engine-ws3-"))
    try:
        yield directory
    finally:
        shutil.rmtree(directory)


def write_bootstrap(directory: Path, *, version: int = 1, project: str = "project-a", config: str = "project.toml") -> Path:
    reference = directory / "bootstrap.toml"
    reference.write_text(f"version = {version}\n[bootstrap]\nproject = {project!r}\nscope = 'project'\ngovernance_basis = 'owner-established'\nproject_configuration = {config!r}\n", encoding="utf-8")
    return reference


def write_config(directory: Path, *, project: str = "project-a") -> Path:
    reference = directory / "project.toml"
    reference.write_text(f"version = 1\n[project]\nidentity = {project!r}\ngovernance_reference = 'governance-record'\n", encoding="utf-8")
    return reference


def test_explicit_authorized_bootstrap_and_separate_configuration(controlled_dir: Path) -> None:
    bootstrap = establish_bootstrap(write_bootstrap(controlled_dir), operator_authorized=True)
    configuration = load_project_configuration(bootstrap, write_config(controlled_dir))
    assert configuration.project_identity == bootstrap.project_identity


@pytest.mark.parametrize("reference,authorized", [(None, True), (Path("missing.toml"), True), (None, False)])
def test_bootstrap_fails_closed_without_explicit_valid_authorized_reference(reference: Path | None, authorized: bool) -> None:
    with pytest.raises(GovernanceEstablishmentError):
        establish_bootstrap(reference, operator_authorized=authorized)


def test_bootstrap_rejects_malformed_unsupported_and_configuration_substitution(controlled_dir: Path) -> None:
    malformed = controlled_dir / "malformed.toml"
    malformed.write_text("[bootstrap\n", encoding="utf-8")
    with pytest.raises(GovernanceEstablishmentError):
        establish_bootstrap(malformed, operator_authorized=True)
    with pytest.raises(GovernanceEstablishmentError):
        establish_bootstrap(write_bootstrap(controlled_dir, version=2), operator_authorized=True)
    bootstrap = establish_bootstrap(write_bootstrap(controlled_dir), operator_authorized=True)
    with pytest.raises(GovernanceEstablishmentError):
        load_project_configuration(bootstrap, controlled_dir / "ordinary-source.toml")


def test_configuration_cannot_acquire_bootstrap_legitimacy(controlled_dir: Path) -> None:
    bootstrap = establish_bootstrap(write_bootstrap(controlled_dir), operator_authorized=True)
    with pytest.raises(GovernanceEstablishmentError):
        load_project_configuration(bootstrap, write_config(controlled_dir, project="other-project"))


def test_sqlite_initializes_and_restores_historical_evidence_without_elevation(controlled_dir: Path) -> None:
    store = SQLiteStateStore(controlled_dir / "state.sqlite")
    store.initialize()
    store.save_evidence(PersistedEvidence("project-a", "claim-a", "historical observation"))
    restored = store.restore_evidence("project-a", "claim-a")
    assert restored is not None
    assert restored.currentness == "unknown"
    assert restored.authority_basis is None


def test_sqlite_rejects_incompatible_schema_and_preserves_project_isolation(controlled_dir: Path) -> None:
    database = controlled_dir / "state.sqlite"
    with sqlite3.connect(database) as connection:
        connection.execute("CREATE TABLE schema_version (version INTEGER NOT NULL)")
        connection.execute("INSERT INTO schema_version VALUES (99)")
    with pytest.raises(StateCompatibilityError):
        SQLiteStateStore(database).initialize()
    database.unlink()
    store = SQLiteStateStore(database)
    store.initialize()
    store.save_evidence(PersistedEvidence("project-a", "claim-a", "history"))
    assert store.restore_evidence("project-b", "claim-a") is None


def test_sqlite_transaction_rolls_back_duplicate_partial_state(controlled_dir: Path) -> None:
    store = SQLiteStateStore(controlled_dir / "state.sqlite")
    store.initialize()
    store.save_evidence(PersistedEvidence("project-a", "claim-a", "history"))
    with pytest.raises(sqlite3.IntegrityError):
        store.save_evidence(PersistedEvidence("project-a", "claim-a", "different history"))
    assert store.restore_evidence("project-a", "claim-a").historical_reference == "history"  # type: ignore[union-attr]


def test_audit_is_durable_authorization_bound_and_secret_safe(controlled_dir: Path) -> None:
    store = SQLiteStateStore(controlled_dir / "state.sqlite")
    store.initialize()
    store.write_audit("project-a", "failed", "configuration unavailable")
    assert store.audit_for_project("project-a", authorized=True) == (("failed", "configuration unavailable"),)
    with pytest.raises(PermissionError):
        store.audit_for_project("project-a", authorized=False)
    with pytest.raises(SecretValueError):
        store.write_audit("project-a", "failed", "token=do-not-store")
