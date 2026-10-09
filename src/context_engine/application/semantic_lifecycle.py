"""Append-only validation rules for governed semantic-record succession."""
from __future__ import annotations

from enum import StrEnum

from context_engine.application.semantic_ingestion import SemanticRecord


class SemanticRecordLifecycleError(ValueError):
    """Raised when an asserted record lifecycle cannot safely be established."""


class SemanticRecordLifecycleKind(StrEnum):
    PROVENANCE_CORRECTION = "provenance_correction"
    SEMANTIC_REVISION = "semantic_revision"
    SOURCE_REVISION_TRANSITION = "source_revision_transition"


def validate_semantic_record_successor(
    predecessor: SemanticRecord,
    successor: SemanticRecord,
    kind: SemanticRecordLifecycleKind,
) -> None:
    """Validate the record-content invariants of one explicit successor edge.

    This does not infer a relation from versions, identities, or timestamps.
    Persistence validates the immutable instance keys and complete graph.
    """
    if predecessor.project_identity != successor.project_identity:
        raise SemanticRecordLifecycleError("semantic-record lifecycle Project mismatch")
    if (predecessor.identity, predecessor.version) == (successor.identity, successor.version):
        raise SemanticRecordLifecycleError("semantic-record lifecycle cannot self-supersede")
    if kind is SemanticRecordLifecycleKind.PROVENANCE_CORRECTION:
        if predecessor.claim_identity != successor.claim_identity:
            raise SemanticRecordLifecycleError("provenance correction Claim identity mismatch")
        if predecessor.assertion_reference != successor.assertion_reference:
            raise SemanticRecordLifecycleError("provenance correction assertion mismatch")
        if predecessor.assertion_content != successor.assertion_content:
            raise SemanticRecordLifecycleError("provenance correction assertion content mismatch")
        if (
            predecessor.source_identity,
            predecessor.artifact_locator,
            predecessor.source_revision,
            predecessor.source_sha256,
        ) != (
            successor.source_identity,
            successor.artifact_locator,
            successor.source_revision,
            successor.source_sha256,
        ):
            raise SemanticRecordLifecycleError("provenance correction Source binding mismatch")
    elif kind is SemanticRecordLifecycleKind.SEMANTIC_REVISION:
        if predecessor.claim_identity == successor.claim_identity:
            raise SemanticRecordLifecycleError("semantic revision requires a new Claim identity")
    elif kind is SemanticRecordLifecycleKind.SOURCE_REVISION_TRANSITION:
        if (
            predecessor.source_identity,
            predecessor.source_revision,
            predecessor.source_sha256,
        ) == (
            successor.source_identity,
            successor.source_revision,
            successor.source_sha256,
        ):
            raise SemanticRecordLifecycleError("source revision transition requires changed Source revision/hash")
    else:  # pragma: no cover - enum construction protects normal callers.
        raise SemanticRecordLifecycleError("semantic-record lifecycle kind is invalid")
