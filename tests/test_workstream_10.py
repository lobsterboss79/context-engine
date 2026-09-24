"""Operational-hardening and controlled recovery tests for Workstream 10.

Every filesystem fixture is isolated under ~/temp via the shared test
convention; no developer state, registered Source, or future proving Consumer
is used here.
"""
from __future__ import annotations

from pathlib import Path
import shutil
import sqlite3
import tempfile

import pytest

from context_engine.adapters import sqlite_state
from context_engine.adapters.sqlite_state import (
    BackupValidationError, PersistedEvidence, PersistedObservation,
    PersistedPackageConstruction, PersistedSourceRegistration, RestoreError,
    SQLiteStateStore,
)


@pytest.fixture
def controlled_dir() -> Path:
    directory = Path(tempfile.mkdtemp(dir=Path.home() / "temp", prefix="context-engine-ws10-"))
    try:
        yield directory
    finally:
        shutil.rmtree(directory)


def populated_store(path: Path) -> SQLiteStateStore:
    store = SQLiteStateStore(path)
    store.initialize()
    store.save_evidence(PersistedEvidence("project-a", "claim-a", "historic evidence"))
    store.save_source_registration(PersistedSourceRegistration(
        "project-a", "source-a", "markdown", "docs", "available", "docs/a.md"))
    store.save_observation(PersistedObservation(
        "project-a", "observation-a", "source-a", "2026-01-01T00:00:00+00:00", "observed", "local-only"))
    store.save_package_construction(PersistedPackageConstruction(
        "project-a", "record-a", "request-a", "package-a", "completed", "sufficient", "coherent", "historic construction"))
    store.write_audit("project-a", "rendering-rendered", "controlled render outcome")
    return store


def test_sqlite_backup_and_restore_preserve_durable_history_but_qualify_present_state(controlled_dir: Path) -> None:
    source = populated_store(controlled_dir / "source.sqlite")
    backup = controlled_dir / "controlled-backup.sqlite"
    metadata = source.create_backup(
        backup, operator_authorized=True, purpose="controlled recovery validation", retention_basis="test-only retention")
    assert SQLiteStateStore.validate_backup(backup) == metadata

    target = SQLiteStateStore(controlled_dir / "target.sqlite")
    target.initialize()
    target.save_evidence(PersistedEvidence("project-b", "claim-b", "must be replaced only on success"))
    qualification = target.restore_backup(backup, operator_authorized=True)

    assert qualification.backup_identity == metadata.backup_identity
    assert target.restore_evidence("project-a", "claim-a").historical_reference == "historic evidence"  # type: ignore[union-attr]
    restored = target.restore_evidence("project-a", "claim-a")
    assert restored is not None and restored.currentness == "unknown" and restored.authority_basis is None
    assert target.restore_evidence("project-b", "claim-b") is None
    assert target.source_registrations_for_project("project-a")[0].source_identity == "source-a"
    assert target.observations_for_project("project-a")[0].observation_identity == "observation-a"
    assert target.package_constructions_for_project("project-a")[0].record_identity == "record-a"
    assert target.audit_for_project("project-a", authorized=True) == (("rendering-rendered", "controlled render outcome"),)
    assert target.audit_for_project("project-b", authorized=True) == ()
    assert target.recovery_qualification() == qualification
    assert "historical-only" in qualification.qualification


def test_backup_and_restore_fail_closed_for_authorization_secrets_and_invalid_files(controlled_dir: Path) -> None:
    store = populated_store(controlled_dir / "state.sqlite")
    with pytest.raises(PermissionError):
        store.create_backup(controlled_dir / "unauthorized.sqlite", operator_authorized=False, purpose="test", retention_basis="test")
    with pytest.raises(ValueError):
        store.create_backup(controlled_dir / "missing-purpose.sqlite", operator_authorized=True, purpose="", retention_basis="test")
    with pytest.raises(ValueError):
        store.create_backup(controlled_dir / "secret.sqlite", operator_authorized=True, purpose="token=never", retention_basis="test")
    invalid = controlled_dir / "invalid.sqlite"
    invalid.write_text("not a sqlite backup", encoding="utf-8")
    with pytest.raises(BackupValidationError):
        SQLiteStateStore.validate_backup(invalid)
    with pytest.raises(PermissionError):
        store.restore_backup(invalid, operator_authorized=False)


def test_incompatible_backup_and_interrupted_restore_do_not_replace_valid_operational_state(controlled_dir: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    source = populated_store(controlled_dir / "source.sqlite")
    backup = controlled_dir / "backup.sqlite"
    source.create_backup(backup, operator_authorized=True, purpose="test", retention_basis="test")
    with sqlite3.connect(backup) as connection:
        connection.execute("UPDATE schema_version SET version = 999")
    target = populated_store(controlled_dir / "target.sqlite")
    with pytest.raises(BackupValidationError):
        target.restore_backup(backup, operator_authorized=True)
    assert target.restore_evidence("project-a", "claim-a") is not None

    valid_backup = controlled_dir / "valid.sqlite"
    source.create_backup(valid_backup, operator_authorized=True, purpose="test", retention_basis="test")
    monkeypatch.setattr(sqlite_state.os, "replace", lambda _source, _target: (_ for _ in ()).throw(OSError("interrupted")))
    with pytest.raises(RestoreError):
        target.restore_backup(valid_backup, operator_authorized=True)
    assert target.restore_evidence("project-a", "claim-a") is not None
    assert not list(controlled_dir.glob(".context-engine-restore-*.sqlite"))


def test_backup_metadata_cannot_substitute_for_authority_or_currentness(controlled_dir: Path) -> None:
    store = populated_store(controlled_dir / "state.sqlite")
    backup = controlled_dir / "backup.sqlite"
    store.create_backup(backup, operator_authorized=True, purpose="test", retention_basis="test")
    metadata = SQLiteStateStore.validate_backup(backup)
    assert metadata.schema_version == 5
    assert not hasattr(metadata, "authority") and not hasattr(metadata, "currentness")
