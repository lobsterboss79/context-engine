from __future__ import annotations

import hashlib

import pytest

from context_engine.application.lifecycle import RegisteredSource
from context_engine.application.representation import transform_markdown
from context_engine.application.semantic_ingestion import SemanticRecord, SemanticRecordError, ingest_semantic_record
from context_engine.core.model import Provenance, SemanticIdentity


def ident(kind: str, value: str) -> SemanticIdentity:
    return SemanticIdentity(kind, value)


def prepared():
    source = RegisteredSource("source", "project", "git", "scope", locator="/unused")
    provenance = Provenance(ident("provenance", "observed"), source=ident("source", "source"))
    transformation = transform_markdown(
        source_identity=ident("source", "source"), artifact_identity=ident("artifact", "artifact"),
        artifact_version_identity=ident("artifact_version", "version"), source_locator="docs/a.md",
        native_state_reference="head", original_markdown="# Heading\n\nA governed statement.\n",
        observation_provenance=provenance,
    )
    record = SemanticRecord("record", "v1", "claim", "assertion:record:v1", "source", "project", "docs/a.md", "head", "a" * 64, "observation", 1, 3, 3, "source-owner", ("Decision",), ("local-only",))
    return source, transformation, record


def test_ingests_explicit_source_bound_claim() -> None:
    source, transformation, record = prepared()
    result = ingest_semantic_record(record, record_sha256="b" * 64, source=source, transformation=transformation, project_identity="project", observation_identity="observation", source_revision="head", source_sha256="a" * 64)
    assert result.claim.identity.value == "claim"
    assert result.represented.subject == result.claim.identity
    assert "block:1;lines:3-3" in result.claim.provenance.location_reference


@pytest.mark.parametrize("field,value", [("source_revision", "wrong"), ("block_ordinal", 99), ("line_start", 2)])
def test_rejects_invalid_source_binding(field: str, value: object) -> None:
    source, transformation, record = prepared()
    changed = record.__dict__ | {field: value}
    with pytest.raises(SemanticRecordError):
        ingest_semantic_record(SemanticRecord(**changed), record_sha256="b" * 64, source=source, transformation=transformation, project_identity="project", observation_identity="observation", source_revision="head", source_sha256="a" * 64)
