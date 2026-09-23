"""Narrow orchestration for durable Workstream 5 evidence only."""
from __future__ import annotations

import json

from context_engine.adapters.git_source import GitObservation
from context_engine.adapters.sqlite_state import (
    PersistedArtifactEvidence, PersistedObservation, PersistedRepresentation,
    PersistedTransformation, SQLiteStateStore,
)
from context_engine.application.representation import MarkdownTransformation
from context_engine.core.model import RepresentedInformation, SemanticIdentity


def persist_evidence_pipeline(
    store: SQLiteStateStore, *, project_identity: str,
    observation_identity: SemanticIdentity, observation: GitObservation,
    transformation_identity: SemanticIdentity, transformation: MarkdownTransformation,
    represented: tuple[RepresentedInformation, ...],
) -> None:
    """Persist one already-observed/transformed evidence path atomically by row.

    This records historical evidence.  It intentionally has no currentness,
    Claim, Candidate Context, applicability, selection, or package behavior.
    """
    if observation_identity.kind != "observation" or transformation_identity.kind != "transformation":
        raise ValueError("observation and transformation require explicit semantic identities")
    store.save_observation(PersistedObservation(
        project_identity, observation_identity.value, observation.source_identity,
        observation.observation_time, observation.outcome,
        json.dumps({"head": observation.head, "branch": observation.branch, "unborn": observation.unborn,
                    "limitations": [item.code for item in observation.limitations]}, sort_keys=True),
    ))
    store.save_artifact_evidence(PersistedArtifactEvidence(
        project_identity, transformation.artifact.identity.value, transformation.version.identity.value,
        transformation.artifact.source.value, transformation.artifact.locators[0], transformation.original_markdown,
        observation_identity.value,
    ))
    store.save_transformation(PersistedTransformation(
        project_identity, transformation_identity.value, transformation.version.identity.value,
        transformation.parser_version, transformation.parser_configuration, "succeeded",
        json.dumps({"blocks": [{"kind": block.kind, "line_start": block.line_start, "line_end": block.line_end} for block in transformation.blocks],
                    "limitations": [item.state.value for item in transformation.limitations]}, sort_keys=True),
    ))
    for item in represented:
        store.save_representation(PersistedRepresentation(
            project_identity, item.identity.value, transformation.version.identity.value,
            item.provenance.identity.value, item.provenance.location_reference or "unknown",
            json.dumps({"subject": item.subject.value, "transformation": item.provenance.transformation.value,
                        "limitations": [limit.state.value for limit in item.uncertainty]}, sort_keys=True),
        ))
