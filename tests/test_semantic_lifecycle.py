from __future__ import annotations

import sqlite3
from dataclasses import replace

import pytest

from context_engine.adapters.sqlite_state import (
    CURRENT_SCHEMA_VERSION,
    PersistedSemanticRecord,
    PersistedSemanticRecordSupersession,
    SQLiteStateStore,
    semantic_record_supersession_sha256,
)
from context_engine.application.semantic_lifecycle import (
    SemanticRecordLifecycleError,
    SemanticRecordLifecycleKind,
    validate_semantic_record_successor,
)
from context_engine.application.semantic_ingestion import SemanticRecord


def digest(character: str) -> str:
    return character * 64


def record(
    identity: str = "record",
    version: str = "v1",
    claim: str = "claim",
    *,
    project: str = "project",
    revision: str = "rev-1",
    source_hash: str = "a",
) -> PersistedSemanticRecord:
    return PersistedSemanticRecord(
        project, identity, version, digest("b" if version == "v1" else "c"),
        claim, "source", "docs/source.md", revision, digest(source_hash),
        "observation", "docs/source.md;block:1;lines:3-3", "evidence",
    )


def relation(
    predecessor: PersistedSemanticRecord,
    successor: PersistedSemanticRecord,
    *,
    kind: str = "provenance_correction",
    identity: str = "relation-v1-v2",
) -> PersistedSemanticRecordSupersession:
    value = PersistedSemanticRecordSupersession(
        predecessor.project_identity, identity, "v1", digest("d"),
        predecessor.record_identity, predecessor.version, predecessor.record_sha256,
        successor.record_identity, successor.version, successor.record_sha256,
        kind, "source-owner correction", "lifecycle evidence",
    )
    return replace(value, relation_sha256=semantic_record_supersession_sha256(value))


def store(tmp_path) -> SQLiteStateStore:
    value = SQLiteStateStore(tmp_path / "state.sqlite")
    value.initialize()
    return value


def test_initial_record_is_active_and_historical_query_is_available(tmp_path) -> None:
    state = store(tmp_path)
    first = record()
    state.save_semantic_record(first)

    assert state.semantic_records_for_project("project") == (first,)
    assert state.active_semantic_records_for_project("project") == (first,)
    assert state.semantic_record_supersessions_for_project("project") == ()


def test_provenance_correction_preserves_predecessor_and_selects_successor(tmp_path) -> None:
    state = store(tmp_path)
    first = record()
    second = record(version="v2")
    state.save_semantic_record(first)
    state.save_semantic_record_successor(second, relation(first, second))

    assert state.semantic_records_for_project("project") == (first, second)
    assert state.active_semantic_records_for_project("project") == (second,)
    assert state.semantic_record_supersessions_for_project("project")[0].kind == "provenance_correction"


def test_three_version_chain_selects_only_terminal_record(tmp_path) -> None:
    state = store(tmp_path)
    first = record()
    second = record(version="v2")
    third = record(version="v3")
    state.save_semantic_record(first)
    state.save_semantic_record_successor(second, relation(first, second))
    state.save_semantic_record_successor(
        third, relation(second, third, identity="relation-v2-v3")
    )

    assert state.active_semantic_records_for_project("project") == (third,)


def test_competing_successor_and_missing_predecessor_fail_closed(tmp_path) -> None:
    state = store(tmp_path)
    first = record()
    second = record(version="v2")
    competing = record(version="v2b")
    state.save_semantic_record(first)
    state.save_semantic_record_successor(second, relation(first, second))
    with pytest.raises(ValueError, match="conflicts"):
        state.save_semantic_record_successor(
            competing, relation(first, competing, identity="relation-v1-v2b")
        )
    missing = record(identity="missing")
    with pytest.raises(ValueError, match="missing"):
        state.save_semantic_record_successor(competing, relation(missing, competing))

    assert state.active_semantic_records_for_project("project") == (second,)


def test_unlinked_versions_of_one_record_identity_fail_closed(tmp_path) -> None:
    state = store(tmp_path)
    state.save_semantic_record(record())
    state.save_semantic_record(record(version="v2"))

    with pytest.raises(ValueError, match="ambiguous active versions"):
        state.active_semantic_records_for_project("project")


def test_cross_project_claim_kind_and_hash_failures_are_rejected(tmp_path) -> None:
    state = store(tmp_path)
    first = record()
    state.save_semantic_record(first)
    wrong_claim = record(version="v2", claim="other")
    with pytest.raises(ValueError, match="Claim"):
        state.save_semantic_record_successor(wrong_claim, relation(first, wrong_claim))
    semantic_same_claim = record(version="v2")
    with pytest.raises(ValueError, match="new Claim"):
        state.save_semantic_record_successor(
            semantic_same_claim, relation(first, semantic_same_claim, kind="semantic_revision")
        )
    other_project = record(version="v2", project="other")
    with pytest.raises(ValueError, match="does not name"):
        state.save_semantic_record_successor(other_project, relation(first, other_project))
    invalid = record(identity="invalid")
    invalid = replace(invalid, record_sha256="not-a-hash")
    with pytest.raises(ValueError, match="SHA-256"):
        state.save_semantic_record(invalid)
    bad_relation = replace(relation(first, semantic_same_claim), relation_sha256=digest("f"))
    with pytest.raises(ValueError, match="hash mismatch"):
        state.save_semantic_record_successor(semantic_same_claim, bad_relation)
    unsupported = replace(relation(first, semantic_same_claim), kind="unsupported_kind")
    unsupported = replace(unsupported, relation_sha256=semantic_record_supersession_sha256(unsupported))
    with pytest.raises(ValueError, match="kind is invalid"):
        state.save_semantic_record_successor(
            semantic_same_claim,
            unsupported,
        )


def test_semantic_and_source_revision_transitions(tmp_path) -> None:
    state = store(tmp_path)
    first = record()
    semantic = record(version="v2", claim="claim-v2")
    source = record(version="v3", claim="claim-v2", revision="rev-2", source_hash="e")
    state.save_semantic_record(first)
    state.save_semantic_record_successor(
        semantic, relation(first, semantic, kind="semantic_revision")
    )
    state.save_semantic_record_successor(
        source, relation(semantic, source, kind="source_revision_transition", identity="relation-v2-v3")
    )

    assert state.active_semantic_records_for_project("project") == (source,)


def test_replay_is_idempotent_and_cycle_is_detected(tmp_path) -> None:
    state = store(tmp_path)
    first = record()
    second = record(version="v2")
    edge = relation(first, second)
    state.save_semantic_record(first)
    state.save_semantic_record_successor(second, edge)
    state.save_semantic_record_successor(second, edge)
    assert len(state.semantic_record_supersessions_for_project("project")) == 1

    with sqlite3.connect(tmp_path / "state.sqlite") as connection:
        connection.execute("PRAGMA foreign_keys = OFF")
        cycle = relation(second, first, identity="cycle")
        connection.execute(
            "INSERT INTO semantic_record_supersession VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            tuple(cycle.__dict__.values()),
        )
    with pytest.raises(ValueError, match="ambiguous|cycle"):
        state.active_semantic_records_for_project("project")


def test_v6_migrates_without_rewriting_semantic_evidence(tmp_path) -> None:
    database = tmp_path / "v6.sqlite"
    first = record()
    with sqlite3.connect(database) as connection:
        connection.execute("CREATE TABLE schema_version (version INTEGER NOT NULL)")
        connection.execute("INSERT INTO schema_version VALUES (6)")
        connection.execute(
            "CREATE TABLE semantic_record_evidence (row_id INTEGER PRIMARY KEY, "
            "project_identity TEXT NOT NULL, record_identity TEXT NOT NULL, version TEXT NOT NULL, "
            "record_sha256 TEXT NOT NULL, claim_identity TEXT NOT NULL, source_identity TEXT NOT NULL, "
            "artifact_locator TEXT NOT NULL, source_revision TEXT NOT NULL, source_sha256 TEXT NOT NULL, "
            "observation_identity TEXT NOT NULL, location_reference TEXT NOT NULL, evidence TEXT NOT NULL, "
            "UNIQUE(project_identity, record_identity, version, record_sha256))"
        )
        connection.execute(
            "INSERT INTO semantic_record_evidence "
            "(project_identity, record_identity, version, record_sha256, claim_identity, source_identity, artifact_locator, source_revision, source_sha256, observation_identity, location_reference, evidence) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            tuple(first.__dict__.values()),
        )
    state = SQLiteStateStore(database)
    state.initialize()

    assert CURRENT_SCHEMA_VERSION == 7
    assert state.semantic_records_for_project("project") == (first,)
    assert state.active_semantic_records_for_project("project") == (first,)


def test_backup_restore_preserves_lifecycle_and_active_resolution(tmp_path) -> None:
    source = store(tmp_path)
    first = record()
    second = record(version="v2")
    source.save_semantic_record(first)
    source.save_semantic_record_successor(second, relation(first, second))
    backup = tmp_path / "backup.sqlite"
    source.create_backup(backup, operator_authorized=True, purpose="test", retention_basis="test")

    restored = SQLiteStateStore(tmp_path / "restored.sqlite")
    restored.restore_backup(backup, operator_authorized=True)

    assert restored.semantic_records_for_project("project") == (first, second)
    assert len(restored.semantic_record_supersessions_for_project("project")) == 1
    assert restored.active_semantic_records_for_project("project") == (second,)


def semantic_record(identity: str, version: str, claim: str, *, revision: str = "rev-1") -> SemanticRecord:
    return SemanticRecord(
        identity, version, claim, "assertion", "source", "project", "docs/source.md",
        revision, digest("a"), "observation", 1, 3, 3, "source-owner", assertion_content="assertion content",
    )


def test_content_lifecycle_validation_preserves_assertion_rules() -> None:
    first = semantic_record("record", "v1", "claim")
    corrected = semantic_record("record", "v2", "claim")
    validate_semantic_record_successor(first, corrected, SemanticRecordLifecycleKind.PROVENANCE_CORRECTION)

    wrong = semantic_record("record", "v2", "other")
    with pytest.raises(SemanticRecordLifecycleError, match="Claim"):
        validate_semantic_record_successor(first, wrong, SemanticRecordLifecycleKind.PROVENANCE_CORRECTION)
    changed_content = SemanticRecord(**(first.__dict__ | {"version": "v2-content", "assertion_content": "changed"}))
    with pytest.raises(SemanticRecordLifecycleError, match="assertion content"):
        validate_semantic_record_successor(first, changed_content, SemanticRecordLifecycleKind.PROVENANCE_CORRECTION)
    validate_semantic_record_successor(first, wrong, SemanticRecordLifecycleKind.SEMANTIC_REVISION)
    changed_source = semantic_record("record", "v3", "other", revision="rev-2")
    validate_semantic_record_successor(first, changed_source, SemanticRecordLifecycleKind.SOURCE_REVISION_TRANSITION)
