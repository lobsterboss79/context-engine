"""Deterministic ingestion of governed source-owner semantic records.

Semantic records are explicit evidence inputs.  This module never extracts or
infers assertions from Markdown, Authority, currentness, or supersession.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path

from context_engine.application.lifecycle import RegisteredSource
from context_engine.application.representation import MarkdownTransformation
from context_engine.core.model import (
    Claim, Classification, EpistemicState, Provenance, RepresentedInformation,
    SemanticIdentity, TransformationKind, Uncertainty,
)


class SemanticRecordError(ValueError):
    """Raised when an explicit semantic record cannot be safely ingested."""


@dataclass(frozen=True)
class SemanticRecord:
    identity: str
    version: str
    claim_identity: str
    assertion_reference: str
    source_identity: str
    project_identity: str
    artifact_locator: str
    source_revision: str
    source_sha256: str
    observation_identity: str
    block_ordinal: int
    line_start: int | None
    line_end: int | None
    authoring_process: str
    classifications: tuple[str, ...] = ()
    limitations: tuple[str, ...] = ()
    authority_basis: str | None = None
    currentness_basis: str | None = None
    governance_basis: str | None = None


@dataclass(frozen=True)
class IngestedSemanticRecord:
    record: SemanticRecord
    record_sha256: str
    claim: Claim
    represented: RepresentedInformation


def load_semantic_record(path: Path) -> tuple[SemanticRecord, str]:
    """Load JSON only; JSON is data, never controller instruction."""
    try:
        payload = path.read_bytes()
        data = json.loads(payload.decode("utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise SemanticRecordError("semantic record is unavailable or invalid JSON") from error
    return _record_from_mapping(data), hashlib.sha256(payload).hexdigest()


def ingest_semantic_record(
    record: SemanticRecord, *, record_sha256: str, source: RegisteredSource,
    transformation: MarkdownTransformation, project_identity: str,
    observation_identity: str, source_revision: str, source_sha256: str,
) -> IngestedSemanticRecord:
    """Validate explicit bindings and emit existing Claim/representation types."""
    if source.project != project_identity or record.project_identity != project_identity:
        raise SemanticRecordError("semantic record project binding mismatch")
    if record.source_identity != source.identity or transformation.artifact.source.value != source.identity:
        raise SemanticRecordError("semantic record Source binding mismatch")
    if record.artifact_locator != transformation.artifact.locators[0]:
        raise SemanticRecordError("semantic record Artifact binding mismatch")
    if record.source_revision != source_revision or record.source_sha256 != source_sha256:
        raise SemanticRecordError("semantic record revision/hash binding mismatch")
    if record.observation_identity != observation_identity:
        raise SemanticRecordError("semantic record observation binding mismatch")
    if not record_sha256 or len(record_sha256) != 64:
        raise SemanticRecordError("semantic record hash is required")
    if record.block_ordinal < 0 or record.block_ordinal >= len(transformation.blocks):
        raise SemanticRecordError("semantic record block is outside Artifact")
    block = transformation.blocks[record.block_ordinal]
    if (record.line_start, record.line_end) != (block.line_start, block.line_end):
        raise SemanticRecordError("semantic record line binding mismatch")
    location = f"{record.artifact_locator};block:{block.ordinal};lines:{block.line_start}-{block.line_end}"
    upstream = (transformation.version.provenance.identity,) if transformation.version.provenance else ()
    provenance = Provenance(
        SemanticIdentity("provenance", f"semantic-record:{record.identity}:{record.version}"),
        source=transformation.artifact.source, artifact=transformation.artifact.identity,
        artifact_version=transformation.version.identity, upstream=upstream,
        transformation=TransformationKind.DIRECT, location_reference=location,
        transformation_reference=f"semantic-record={record.identity};version={record.version};sha256={record_sha256}",
        limitations=tuple(Uncertainty(EpistemicState.UNKNOWN, detail=value) for value in record.limitations),
    )
    claim = Claim(SemanticIdentity("claim", record.claim_identity), record.assertion_reference, provenance)
    represented = RepresentedInformation(
        SemanticIdentity("represented_information", f"semantic-record:{record.identity}:{record.version}"),
        claim.identity, provenance, tuple(Classification(value) for value in record.classifications),
        tuple(Uncertainty(EpistemicState.UNKNOWN, detail=value) for value in record.limitations),
    )
    return IngestedSemanticRecord(record, record_sha256, claim, represented)


def _record_from_mapping(data: object) -> SemanticRecord:
    if not isinstance(data, dict):
        raise SemanticRecordError("semantic record must be an object")
    required = ("identity", "version", "claim_identity", "assertion_reference", "source_identity", "project_identity", "artifact_locator", "source_revision", "source_sha256", "observation_identity", "block_ordinal", "authoring_process")
    if any(not isinstance(data.get(key), str) or not data[key] for key in required if key != "block_ordinal") or not isinstance(data.get("block_ordinal"), int):
        raise SemanticRecordError("semantic record required fields are missing")
    def strings(name: str) -> tuple[str, ...]:
        value = data.get(name, [])
        if not isinstance(value, list) or any(not isinstance(item, str) or not item for item in value):
            raise SemanticRecordError(f"semantic record {name} must be strings")
        return tuple(value)
    for name in ("line_start", "line_end"):
        if data.get(name) is not None and not isinstance(data.get(name), int):
            raise SemanticRecordError(f"semantic record {name} must be integer or null")
    return SemanticRecord(
        **{key: data[key] for key in required}, line_start=data.get("line_start"), line_end=data.get("line_end"),
        classifications=strings("classifications"), limitations=strings("limitations"),
        authority_basis=data.get("authority_basis"), currentness_basis=data.get("currentness_basis"), governance_basis=data.get("governance_basis"),
    )
