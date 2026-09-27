"""Execution-only orchestration of frozen FX-F6-D through existing v0.1 APIs."""
from __future__ import annotations

from dataclasses import asdict, is_dataclass
from datetime import UTC, datetime
from enum import Enum
import json
from pathlib import Path
import platform
import sys

import markdown_it

from context_engine.adapters.git_source import LocalGitSourceAdapter
from context_engine.adapters.sqlite_state import SQLiteStateStore
from context_engine.application.decision_pipeline import ApplicabilityInputs, EnforcementInputs, RelevanceOutcome, RoleInputs, evaluate_applicability, select_candidate
from context_engine.application.discovery import DiscoveryEvidence
from context_engine.application.lifecycle import ApplicableSourceUniverse, Availability, BoundaryAdequacy, RegisteredSource
from context_engine.application.orchestration import GovernedRenderInputs, run_governed_render
from context_engine.application.package_construction import CoherenceInputs
from context_engine.application.rendering import ConsumerContract, ConsumerKind, render_package
from context_engine.application.representation import observe_markdown_artifact, transform_markdown
from context_engine.core.model import Consumer, ConsumerId, ContextRequest, Currentness, CurrentnessAssessment, GovernanceAssessment, GovernanceState, Provenance, RepresentedInformation, Requester, RequesterId, SemanticIdentity, TaskIntent, TaskScope, TransformationKind

ROOT = Path.cwd()
FIXTURE = ROOT / "docs/phase-4/ws2-item-2.6-fixtures/F6-D"
OUT = Path("/tmp/context-engine-ve-f6-d-001")


def ident(kind: str, value: str) -> SemanticIdentity:
    return SemanticIdentity(kind, value)


def normalize(value):
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Path):
        return str(value)
    if is_dataclass(value):
        return {key: normalize(item) for key, item in asdict(value).items()}
    if isinstance(value, tuple):
        return [normalize(item) for item in value]
    if isinstance(value, list):
        return [normalize(item) for item in value]
    if isinstance(value, dict):
        return {str(key): normalize(item) for key, item in value.items()}
    return value


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    request = ContextRequest(
        ident("request", "REQ-F6D-ATLAS-DEPLOYMENT-RECOMMENDATION"),
        ident("project", "fixture-atlas-f6d"),
        Requester(RequesterId(ident("requester", "fixture-requester"))),
        Consumer(ConsumerId(ident("consumer", "fixture-human"))),
        TaskIntent("prepare an unqualified deployment recommendation for the complete unbounded Atlas field-operations plan"),
        TaskScope("atlas/field-operations/current-plan"),
    )
    source = RegisteredSource(
        "SRC-F6D-FIELD-OPERATIONS-NOTE", "fixture-atlas-f6d", "git",
        "atlas/field-operations/current-plan", Availability.AVAILABLE, str(ROOT),
    )
    git_observation = LocalGitSourceAdapter().observe(source, inspection_authorized=True)
    markdown_observation = observe_markdown_artifact(FIXTURE, "sources/field-operations-note.md")
    if markdown_observation.outcome != "observed" or markdown_observation.original_markdown is None:
        raise RuntimeError("F6-D normal local Markdown observation failed")

    direct = Provenance(
        ident("provenance", "PROV-OBS-F6D-FIELD-OPERATIONS-NOTE"),
        origin_projects=(request.project,), source=ident("source", source.identity),
        observation=ident("observation", "OBS-F6D-FIELD-OPERATIONS-NOTE"),
        transformation=TransformationKind.DIRECT,
        location_reference="sources/field-operations-note.md",
    )
    transformed = transform_markdown(
        source_identity=ident("source", source.identity),
        artifact_identity=ident("artifact", "ART-F6D-FIELD-OPERATIONS-NOTE"),
        artifact_version_identity=ident("artifact_version", "ARTV-F6D-FIELD-OPERATIONS-NOTE"),
        source_locator="sources/field-operations-note.md", native_state_reference=git_observation.head,
        original_markdown=markdown_observation.original_markdown, observation_provenance=direct,
    )
    provenance = Provenance(
        ident("provenance", "PROV-F6D-FIELD-OPERATIONS-NOTE"),
        origin_projects=(request.project,), source=ident("source", source.identity),
        artifact=transformed.artifact.identity, artifact_version=transformed.version.identity,
        observation=ident("observation", "OBS-F6D-FIELD-OPERATIONS-NOTE"),
        upstream=(direct.identity,), transformation=TransformationKind.NORMALIZED,
        location_reference="sources/field-operations-note.md",
        transformation_reference=f"{transformed.parser_configuration}; version={transformed.parser_version}",
    )
    item = RepresentedInformation(
        ident("represented_information", "RI-F6D-ATLAS-STAGING-SAFETY-REVIEW"),
        ident("claim", "RI-F6D-ATLAS-STAGING-SAFETY-REVIEW"), provenance,
    )
    evidence = DiscoveryEvidence(
        item, source, text=markdown_observation.original_markdown,
        markdown_kinds=("heading", "paragraph", "list"),
        governance=(GovernanceAssessment(item.subject, GovernanceState.APPROVED, item.provenance),),
        currentness=(CurrentnessAssessment(item.subject, Currentness.CURRENT),),
    )
    basis = (
        "The governed inspection boundary identifies and permits normal inspection of the known local Source "
        "SRC-F6D-FIELD-OPERATIONS-NOTE in scope 'atlas/field-operations/current-plan'. The available governed "
        "boundary and inventory evidence establishes this known local boundary, but does not reliably establish "
        "whether an additional Source or Source scope could be applicable to the complete unbounded deployment-"
        "recommendation task. No particular omitted material Source, Source scope, or governed relationship is known or asserted."
    )
    universe = ApplicableSourceUniverse(
        request.identity.value, (source,), BoundaryAdequacy.INDETERMINATE, basis,
    )
    enforcement = EnforcementInputs(True, request.project, request.project, True, True)
    applicability = ApplicabilityInputs(
        RelevanceOutcome.RELEVANT,
        "FX-F6-D frozen task mapping establishes the represented current field-operations staging and safety-review information as applicable Supporting Context.",
        True, enforcement,
    )
    role = RoleInputs(
        False, True, False,
        "FX-F6-D frozen task mapping establishes the known staging and safety-review information as useful Supporting Context, without treating it as proof of ASU adequacy.",
    )
    store = SQLiteStateStore(OUT / "f6-d-state.sqlite")
    store.initialize()
    inputs = GovernedRenderInputs(
        FIXTURE / "bootstrap.toml", FIXTURE / "project.toml", True, request, universe,
        (evidence,), ("atlas", "field", "operations", "staging", "safety", "deployment"),
        ((item.identity.value, applicability),), ((item.identity.value, role),),
        "FX-F6-D frozen governed selection of known applicable Supporting Context; selection does not establish ASU adequacy.",
        (), False, False, False, ident("package", "PKG-F6D-ATLAS-DEPLOYMENT"),
        ident("record", "PCR-F6D-ATLAS-DEPLOYMENT"),
        "FX-F6-D known local Source inspected normally; ASU evidence boundary remains indeterminate for the complete unbounded task.",
        ConsumerContract(ConsumerKind.HUMAN, request.consumer, True),
        coherence_inputs=CoherenceInputs(
            understood_qualified_state=True,
            basis="The known selected Context, Provenance, nonempty ASU basis, indeterminate adequacy, Insufficient sufficiency, and evidence-boundary limitation are retained without contradiction.",
        ),
    )
    outcome = run_governed_render(inputs, store=store)
    if outcome.construction.package is None:
        raise RuntimeError("F6-D qualified logical package was not constructed")
    decision = evaluate_applicability(outcome.discovery.candidates[0], applicability)
    selection = select_candidate(decision, role, selection_basis=inputs.selection_basis)
    renderings = {"human": outcome.rendering}
    for kind, name in ((ConsumerKind.CHATGPT, "fixture-chatgpt"), (ConsumerKind.CODEX, "fixture-codex")):
        renderings[kind.value] = render_package(
            outcome.construction.package,
            ConsumerContract(kind, Consumer(ConsumerId(ident("consumer", name))), True),
        )
    for kind, rendering in renderings.items():
        (OUT / f"rendering-{kind}.md").write_text(rendering.content or "", encoding="utf-8")

    package = outcome.construction.package
    if package.sufficiency.value != "insufficient" or package.coherence.outcome != "coherent_with_qualification":
        raise RuntimeError("F6-D frozen qualified sufficiency/coherence result was not preserved")
    if selection.selected is None or selection.selected.role.value != "supporting":
        raise RuntimeError("F6-D applicable Supporting selection was not preserved")
    if not any(value.state.value == "unknown" and "ASU adequacy=indeterminate" in (value.detail or "") for value in package.limitations):
        raise RuntimeError("F6-D evidence-boundary limitation was not retained")
    for kind, rendering in renderings.items():
        if rendering.status != "rendered" or rendering.content is None:
            raise RuntimeError(f"F6-D {kind} rendering was not produced")

    result = {
        "evidence_id": "VE-F6-D-001", "fixture": "FX-F6-D v1", "expected_result": "ER-F6-D v1",
        "execution_utc": datetime.now(UTC).isoformat(),
        "environment": {"python": sys.version, "platform": platform.platform(), "markdown_it": markdown_it.__version__},
        "bootstrap": outcome.bootstrap, "configuration": outcome.configuration,
        "source_observations": [{"source": source.identity, "git": git_observation, "markdown": markdown_observation, "transformation": transformed}],
        "represented_information": [item], "discovery": outcome.discovery,
        "applicability_and_selection": [{"represented_information": item.identity.value, "applicability": decision, "selection": selection}],
        "asu": {"identity": "ASU-F6D-ATLAS-DEPLOYMENT", "adequacy": universe.adequacy, "basis": universe.basis},
        "construction": outcome.construction,
        "renderings": {kind: {"status": value.status, "reason_codes": value.reason_codes, "reference": value.rendering.representation_reference if value.rendering else None} for kind, value in renderings.items()},
        "audit": store.audit_for_project("fixture-atlas-f6d", authorized=True),
    }
    (OUT / "raw-result.json").write_text(json.dumps(normalize(result), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "evidence_id": "VE-F6-D-001", "output": str(OUT), "represented": [item.identity.value],
        "candidates": [candidate.represented.identity.value for candidate in outcome.discovery.candidates],
        "selected": [{"represented": selected.represented.identity.value, "role": selected.role.value} for selected in package.items],
        "asu_adequacy": universe.adequacy.value, "sufficiency": package.sufficiency.value,
        "coherence": package.coherence.outcome, "rendering_statuses": {key: value.status for key, value in renderings.items()},
    }, sort_keys=True))


if __name__ == "__main__":
    main()
