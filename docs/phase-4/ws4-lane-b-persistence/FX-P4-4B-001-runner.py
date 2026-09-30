#!/usr/bin/env python3
"""Lane-private, deterministic WS4 4.2 fixture; output is preserved evidence."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import sqlite3

from context_engine.adapters import sqlite_state
from context_engine.adapters.sqlite_state import (
    CURRENT_SCHEMA_VERSION,
    PersistedEvidence,
    PersistedObservation,
    PersistedPackageConstruction,
    PersistedSourceRegistration,
    RestoreError,
    SQLiteStateStore,
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def integrity(path: Path) -> str:
    with sqlite3.connect(path) as connection:
        return connection.execute("PRAGMA integrity_check").fetchone()[0]


def version(path: Path) -> int:
    with sqlite3.connect(path) as connection:
        return connection.execute("SELECT version FROM schema_version").fetchone()[0]


def tables(path: Path) -> list[str]:
    with sqlite3.connect(path) as connection:
        return sorted(row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'"))


def populated(path: Path, project: str, claim: str) -> SQLiteStateStore:
    store = SQLiteStateStore(path)
    store.initialize()
    store.save_evidence(PersistedEvidence(project, claim, f"historical {claim}"))
    if project == "project-a":
        store.save_source_registration(PersistedSourceRegistration(project, "source-a", "markdown", "docs", "available", "docs/a.md"))
        store.save_observation(PersistedObservation(project, "observation-a", "source-a", "2026-01-01T00:00:00+00:00", "observed", "local-only"))
        store.save_package_construction(PersistedPackageConstruction(project, "record-a", "request-a", "package-a", "completed", "sufficient", "coherent", "historic construction"))
        store.write_audit(project, "rendering-rendered", "controlled render outcome")
    return store


def write_result(out: Path, result: dict[str, object]) -> None:
    (out / "result.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def predecessor(out: Path) -> dict[str, object]:
    source = populated(out / "source.sqlite", "project-a", "claim-a")
    target = populated(out / "target.sqlite", "project-b", "claim-b")
    backup = out / "valid.sqlite"
    source.create_backup(backup, operator_authorized=True, purpose="ws4 lane-b interruption", retention_basis="lane-private evidence")
    before = digest(out / "target.sqlite")
    original_replace = sqlite_state.os.replace
    sqlite_state.os.replace = lambda _source, _target: (_ for _ in ()).throw(OSError("controlled replacement interruption"))
    caught = None
    try:
        target.restore_backup(backup, operator_authorized=True)
    except RestoreError as error:
        caught = str(error)
    finally:
        sqlite_state.os.replace = original_replace
    after = digest(out / "target.sqlite")
    return {
        "scenario_state": "APPLICATION-LEVEL FAILURE / RECOVERY REQUIRED",
        "caught_restore_error": caught,
        "target_hash_before": before,
        "target_hash_after": after,
        "target_integrity": integrity(out / "target.sqlite"),
        "target_version": version(out / "target.sqlite"),
        "target_project_b_claim": target.restore_evidence("project-b", "claim-b").historical_reference if target.restore_evidence("project-b", "claim-b") else None,
        "target_project_a_claim": target.restore_evidence("project-a", "claim-a").historical_reference if target.restore_evidence("project-a", "claim-a") else None,
        "recovery_qualification": target.recovery_qualification() is not None,
        "staging_files": sorted(path.name for path in out.glob(".context-engine-restore-*.sqlite")),
        "backup_integrity": integrity(backup),
    }


def successor(out: Path, predecessor_state: Path) -> dict[str, object]:
    copied_target = out / "target.sqlite"
    copied_backup = out / "valid.sqlite"
    shutil.copy2(predecessor_state / "target.sqlite", copied_target)
    shutil.copy2(predecessor_state / "valid.sqlite", copied_backup)
    predecessor_hash = digest(predecessor_state / "target.sqlite")
    copied_pre_hash = digest(copied_target)
    target = SQLiteStateStore(copied_target)
    qualification = target.restore_backup(copied_backup, operator_authorized=True)
    restored = target.restore_evidence("project-a", "claim-a")
    return {
        "scenario_state": "SUCCESSFUL PREDETERMINED RECOVERY SUCCESSOR",
        "predecessor_target_hash": predecessor_hash,
        "copied_pre_recovery_target_hash": copied_pre_hash,
        "target_integrity": integrity(copied_target),
        "target_version": version(copied_target),
        "target_project_a_claim": restored.historical_reference if restored else None,
        "target_project_b_claim": target.restore_evidence("project-b", "claim-b") is not None,
        "source_registration": target.source_registrations_for_project("project-a")[0].source_identity,
        "observation": target.observations_for_project("project-a")[0].observation_identity,
        "construction": target.package_constructions_for_project("project-a")[0].record_identity,
        "audit": list(target.audit_for_project("project-a", authorized=True)),
        "qualification": qualification.qualification,
        "restored_currentness": restored.currentness if restored else None,
        "restored_authority_basis": restored.authority_basis if restored else "unexpected-none",
        "staging_files": sorted(path.name for path in out.glob(".context-engine-restore-*.sqlite")),
    }


def migration(out: Path) -> dict[str, object]:
    database = out / "version-one.sqlite"
    with sqlite3.connect(database) as connection:
        connection.execute("CREATE TABLE schema_version (version INTEGER NOT NULL)")
        connection.execute("INSERT INTO schema_version VALUES (1)")
        connection.execute("CREATE TABLE evidence (row_id INTEGER PRIMARY KEY, project_identity TEXT NOT NULL, semantic_identity TEXT NOT NULL, historical_reference TEXT NOT NULL, UNIQUE(project_identity, semantic_identity))")
        connection.execute("CREATE TABLE audit (row_id INTEGER PRIMARY KEY, project_identity TEXT NOT NULL, outcome TEXT NOT NULL, detail TEXT NOT NULL)")
        connection.execute("INSERT INTO evidence(project_identity, semantic_identity, historical_reference) VALUES ('project-m', 'claim-m', 'v1 historical evidence')")
    SQLiteStateStore(database).initialize()
    restored = SQLiteStateStore(database).restore_evidence("project-m", "claim-m")
    return {"scenario_state": "SUPPORTED MIGRATION COMPLETED", "schema_version": version(database), "expected_schema_version": CURRENT_SCHEMA_VERSION, "integrity": integrity(database), "tables": tables(database), "retained_v1_evidence": restored.historical_reference if restored else None}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("scenario", choices=("predecessor", "successor", "migration"))
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--predecessor-state", type=Path)
    args = parser.parse_args()
    if args.out.exists():
        raise SystemExit("output directory must be new")
    args.out.mkdir(parents=True)
    if args.scenario == "predecessor":
        result = predecessor(args.out)
    elif args.scenario == "successor":
        if args.predecessor_state is None:
            raise SystemExit("successor requires --predecessor-state")
        result = successor(args.out, args.predecessor_state)
    else:
        result = migration(args.out)
    write_result(args.out, result)


if __name__ == "__main__":
    main()
