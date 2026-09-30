"""Frozen executor for ER-P4-4C-001 v1; lane-private disposable state only."""
from __future__ import annotations

from dataclasses import asdict
from hashlib import sha256
import json
from pathlib import Path
import shutil
import sqlite3
import sys

from context_engine.adapters import sqlite_state
from context_engine.adapters.sqlite_state import (
    PersistedArtifactEvidence,
    PersistedEvidence,
    PersistedObservation,
    PersistedPackageConstruction,
    PersistedRepresentation,
    PersistedSourceRegistration,
    PersistedTransformation,
    RestoreError,
    SQLiteStateStore,
)


ROOT = Path(__file__).resolve().parent
STATE = ROOT / "state"
SOURCE = STATE / "source-alpha.sqlite"
BACKUP = STATE / "backup-alpha.sqlite"
TARGET = STATE / "target.sqlite"
FAILED_TARGET = STATE / "predecessor-failed-target-beta.sqlite"
RESULT = STATE / "result.json"
PURPOSE = "Phase 4 WS4 Lane C controlled local recovery validation"
RETENTION = "retain only in this VE-P4-4C-001 record; no scheduler, duration, or deletion policy selected"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def projection(store: SQLiteStateStore, project: str) -> dict[str, object]:
    return {
        "evidence": [asdict(value) for value in (store.restore_evidence(project, "claim-alpha"),) if value],
        "sources": [asdict(value) for value in store.source_registrations_for_project(project)],
        "observations": [asdict(value) for value in store.observations_for_project(project)],
        "artifacts": [asdict(value) for value in store.artifact_evidence_for_project(project)],
        "transformations": [asdict(value) for value in store.transformations_for_project(project)],
        "representations": [asdict(value) for value in store.representations_for_project(project)],
        "constructions": [asdict(value) for value in store.package_constructions_for_project(project)],
        "audit_authorized": list(store.audit_for_project(project, authorized=True)),
    }


def populate_alpha(path: Path) -> SQLiteStateStore:
    store = SQLiteStateStore(path)
    store.initialize()
    store.save_evidence(PersistedEvidence("project-alpha", "claim-alpha", "historical Alpha evidence"))
    store.save_source_registration(PersistedSourceRegistration(
        "project-alpha", "source-alpha", "markdown", "controlled-fixture", "available", "fixtures/alpha.md"))
    store.save_observation(PersistedObservation(
        "project-alpha", "observation-alpha", "source-alpha", "2026-09-30T00:00:00+00:00", "observed", "historical observation"))
    store.save_artifact_evidence(PersistedArtifactEvidence(
        "project-alpha", "artifact-alpha", "artifact-alpha-v1", "source-alpha", "fixtures/alpha.md", "historical alpha artifact", "observation-alpha"))
    store.save_transformation(PersistedTransformation(
        "project-alpha", "transformation-alpha", "artifact-alpha-v1", "markdown-it", "controlled-fixture", "represented", "historical transformation"))
    store.save_representation(PersistedRepresentation(
        "project-alpha", "representation-alpha", "artifact-alpha-v1", "provenance-alpha", "line 1", "historical provenance-bearing representation"))
    store.save_package_construction(PersistedPackageConstruction(
        "project-alpha", "construction-alpha", "request-alpha", "package-alpha", "completed", "insufficient", "coherent_with_qualification", "historical construction evidence"))
    store.write_audit("project-alpha", "controlled-construction", "historical Alpha audit")
    return store


def populate_beta(path: Path) -> SQLiteStateStore:
    store = SQLiteStateStore(path)
    store.initialize()
    store.save_evidence(PersistedEvidence("project-beta", "claim-beta", "pre-existing valid target"))
    store.save_source_registration(PersistedSourceRegistration(
        "project-beta", "source-beta", "markdown", "controlled-fixture", "available", "fixtures/beta.md"))
    store.write_audit("project-beta", "controlled-target", "pre-existing Beta audit")
    return store


def integrity(path: Path) -> str:
    with sqlite3.connect(path) as connection:
        return connection.execute("PRAGMA integrity_check").fetchone()[0]


def main() -> None:
    if STATE.exists():
        raise RuntimeError("frozen procedure refuses an existing raw state directory")
    STATE.mkdir(parents=True)
    source = populate_alpha(SOURCE)
    source_projection = projection(source, "project-alpha")
    metadata = source.create_backup(BACKUP, operator_authorized=True, purpose=PURPOSE, retention_basis=RETENTION, backup_identity="backup-p4-4c-001-alpha")
    validated_metadata = SQLiteStateStore.validate_backup(BACKUP)

    target = populate_beta(TARGET)
    beta_before_projection = projection(target, "project-beta")
    target_before_hash = digest(TARGET)
    original_replace = sqlite_state.os.replace
    def interrupted_replace(_source: Path | str, _target: Path | str) -> None:
        raise OSError("controlled replace interruption")
    sqlite_state.os.replace = interrupted_replace
    try:
        try:
            target.restore_backup(BACKUP, operator_authorized=True)
        except RestoreError as error:
            predecessor = {"scenario_state": "RECOVERY REQUIRED", "exception_type": type(error).__name__, "message": str(error)}
        else:
            raise AssertionError("controlled replacement failure did not occur")
    finally:
        sqlite_state.os.replace = original_replace

    target_after_failure_hash = digest(TARGET)
    beta_after_projection = projection(target, "project-beta")
    failed_staging = sorted(path.name for path in STATE.glob(".context-engine-restore-*.sqlite"))
    shutil.copy2(TARGET, FAILED_TARGET)

    qualification = target.restore_backup(BACKUP, operator_authorized=True)
    restored_projection = projection(target, "project-alpha")
    beta_after_restore_projection = projection(target, "project-beta")
    try:
        target.audit_for_project("project-alpha", authorized=False)
    except PermissionError as error:
        unauthorized_audit = {"denied": True, "exception_type": type(error).__name__, "message": str(error)}
    else:
        raise AssertionError("unauthorized audit read was not denied")

    assertion_map = {
        "backup_metadata_matches_validation": asdict(metadata) == asdict(validated_metadata),
        "backup_integrity_ok": integrity(BACKUP) == "ok",
        "failure_preserved_target_bytes": target_before_hash == target_after_failure_hash,
        "failure_preserved_beta_semantics": beta_before_projection == beta_after_projection,
        "failure_left_no_staging_file": not failed_staging,
        "source_restored_semantic_projection_matches": source_projection == restored_projection,
        "restored_integrity_ok": integrity(TARGET) == "ok",
        "project_beta_absent_after_restore": beta_after_restore_projection == {"evidence": [], "sources": [], "observations": [], "artifacts": [], "transformations": [], "representations": [], "constructions": [], "audit_authorized": []},
        "unauthorized_audit_denied": unauthorized_audit["denied"],
        "historical_currentness_unknown": target.restore_evidence("project-alpha", "claim-alpha").currentness == "unknown",  # type: ignore[union-attr]
        "no_authority_basis": target.restore_evidence("project-alpha", "claim-alpha").authority_basis is None,  # type: ignore[union-attr]
        "construction_remains_insufficient": target.package_constructions_for_project("project-alpha")[0].sufficiency == "insufficient",
        "qualification_is_historical_only": "historical-only" in qualification.qualification and "independent re-establishment" in qualification.qualification,
        "qualification_matches_backup": qualification.backup_identity == metadata.backup_identity,
        "successor_left_no_staging_file": not list(STATE.glob(".context-engine-restore-*.sqlite")),
    }
    if not all(assertion_map.values()):
        raise AssertionError("one or more frozen acceptance assertions failed")
    payload = {
        "control": "ER-P4-4C-001 v1",
        "scenario": {"predecessor": predecessor, "successor": "RESTORED HISTORICAL-ONLY STATE"},
        "backup_metadata": asdict(metadata),
        "recovery_qualification": asdict(qualification),
        "hashes": {str(path.name): digest(path) for path in (SOURCE, BACKUP, FAILED_TARGET, TARGET)},
        "integrity": {str(path.name): integrity(path) for path in (SOURCE, BACKUP, FAILED_TARGET, TARGET)},
        "projections": {"source_alpha": source_projection, "predecessor_beta": beta_after_projection, "restored_alpha": restored_projection, "restored_beta": beta_after_restore_projection},
        "unauthorized_audit": unauthorized_audit,
        "assertions": assertion_map,
        "validation_result": "PASS",
    }
    RESULT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"validation_result": payload["validation_result"], "assertions": assertion_map, "predecessor": predecessor}, sort_keys=True))


if __name__ == "__main__":
    main()
