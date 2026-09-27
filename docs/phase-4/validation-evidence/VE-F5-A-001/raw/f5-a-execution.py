"""Execution-only orchestration of frozen FX-F5-A through existing v0.1 APIs."""
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
from context_engine.application.decision_pipeline import (
    ApplicabilityInputs,
    EnforcementInputs,
    RelevanceOutcome,
    RoleInputs,
    evaluate_applicability,
    select_candidate,
)
from context_engine.application.discovery import DiscoveryEvidence
from context_engine.application.lifecycle import (
    ApplicableSourceUniverse,
    Availability,
    BoundaryAdequacy,
    RegisteredSource,
)
from context_engine.application.orchestration import GovernedRenderInputs, run_governed_render
from context_engine.application.package_construction import CoherenceInputs
from context_engine.application.rendering import ConsumerContract, ConsumerKind, render_package
from context_engine.application.representation import observe_markdown_artifact, transform_markdown
from context_engine.core.model import (
    Consumer,
    ConsumerId,
    ContextRequest,
    Currentness,
    CurrentnessAssessment,
    GovernanceAssessment,
    GovernanceState,
    Provenance,
    RepresentedInformation,
    Requester,
    RequesterId,
    SemanticIdentity,
    TaskIntent,
    TaskScope,
    TransformationKind,
)

ROOT = Path.cwd()
FIXTURE = ROOT / "docs/phase-4/ws2-item-2.1-fixtures/F5-A"
OUT = Path("/tmp/context-engine-ve-f5-a-001-final")
ATLAS_SOURCE = "SRC-F5A-ATLAS"
BEACON_SOURCE = "SRC-F5A-BEACON"


def ident(kind, value):
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


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    request = ContextRequest(
        ident("request", "REQ-F5A-ATLAS-RELEASE-CHECKLIST"),
        ident("project", "fixture-atlas-f5"),
        Requester(RequesterId(ident("requester", "fixture-requester"))),
        Consumer(ConsumerId(ident("consumer", "fixture-human"))),
        TaskIntent("prepare the Atlas field-kit release checklist"),
        TaskScope("atlas-field-kit-release"),
    )
    atlas = RegisteredSource(
        ATLAS_SOURCE,
        "fixture-atlas-f5",
        "git",
        "atlas-field-kit-release",
        Availability.AVAILABLE,
        str(ROOT),
    )
    # The Beacon controlled identity is deliberately not instantiated, observed,
    # transformed, or supplied to discovery: the frozen authorization/governance
    # boundary stops traversal before inspection and representation.
    git_observation = LocalGitSourceAdapter().observe(atlas, inspection_authorized=True)
    markdown_observation = observe_markdown_artifact(FIXTURE, "sources/atlas-task.md")
    if markdown_observation.outcome != "observed" or markdown_observation.original_markdown is None:
        raise RuntimeError("F5-A Atlas Markdown observation failed")
    direct = Provenance(
        ident("provenance", "PROV-OBS-F5A-ATLAS"),
        origin_projects=(request.project,),
        source=ident("source", ATLAS_SOURCE),
        observation=ident("observation", "OBS-F5A-ATLAS"),
        transformation=TransformationKind.DIRECT,
        location_reference="sources/atlas-task.md",
    )
    transformed = transform_markdown(
        source_identity=ident("source", ATLAS_SOURCE),
        artifact_identity=ident("artifact", "ART-F5A-ATLAS-TASK"),
        artifact_version_identity=ident("artifact_version", "ARTV-F5A-ATLAS-TASK"),
        source_locator="sources/atlas-task.md",
        native_state_reference=git_observation.head,
        original_markdown=markdown_observation.original_markdown,
        observation_provenance=direct,
    )
    provenance = Provenance(
        ident("provenance", "PROV-F5A-ATLAS"),
        origin_projects=(request.project,),
        source=ident("source", ATLAS_SOURCE),
        artifact=transformed.artifact.identity,
        artifact_version=transformed.version.identity,
        observation=ident("observation", "OBS-F5A-ATLAS"),
        upstream=(direct.identity,),
        transformation=TransformationKind.NORMALIZED,
        location_reference="sources/atlas-task.md",
        transformation_reference=f"{transformed.parser_configuration}; version={transformed.parser_version}",
    )
    item = RepresentedInformation(
        ident("represented_information", "RI-F5A-ATLAS-TASK"),
        ident("claim", "RI-F5A-ATLAS-TASK"),
        provenance,
    )
    evidence = DiscoveryEvidence(
        item,
        atlas,
        text=markdown_observation.original_markdown,
        markdown_kinds=("heading", "paragraph"),
        governance=(GovernanceAssessment(item.subject, GovernanceState.APPROVED, item.provenance),),
        currentness=(CurrentnessAssessment(item.subject, Currentness.CURRENT),),
    )
    universe = ApplicableSourceUniverse(
        request.identity.value,
        (atlas,),
        BoundaryAdequacy.ADEQUATE,
        "FX-F5-A frozen adequate Atlas-only ASU: absent governed relationship and denied cross-Project requester authorization exclude Beacon before inspection/discovery.",
    )
    enforcement = EnforcementInputs(True, request.project, request.project, True, True)
    applicability = ApplicabilityInputs(
        RelevanceOutcome.RELEVANT,
        "FX-F5-A frozen Atlas task mapping establishes applicable Required Atlas task information.",
        True,
        enforcement,
    )
    role = RoleInputs(
        True,
        False,
        False,
        "FX-F5-A omission basis: omitting Atlas task information would make the Atlas release checklist materially incorrect.",
    )
    store = SQLiteStateStore(OUT / "f5-a-state.sqlite")
    store.initialize()
    inputs = GovernedRenderInputs(
        FIXTURE / "bootstrap.toml",
        FIXTURE / "project.toml",
        True,
        request,
        universe,
        (evidence,),
        ("atlas", "field-kit", "release", "checklist"),
        ((item.identity.value, applicability),),
        ((item.identity.value, role),),
        "FX-F5-A frozen governed selection of the Atlas Required task information.",
        (),
        False,
        False,
        False,
        ident("package", "PKG-F5-A-001"),
        ident("record", "PCR-F5-A-001"),
        "FX-F5-A adequate Atlas-only ASU fully inspected; Beacon is an authorization/governance boundary outside the effective discovery boundary, not unavailable or inaccessible.",
        ConsumerContract(ConsumerKind.HUMAN, request.consumer, True),
        coherence_inputs=CoherenceInputs(),
    )
    outcome = run_governed_render(inputs, store=store)
    if outcome.construction.package is None:
        raise RuntimeError("F5-A logical package was not constructed")
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
    if outcome.discovery.initial_inspected_sources != (ATLAS_SOURCE,) or outcome.discovery.expanded_inspected_sources:
        raise RuntimeError("F5-A inspected source boundary is not Atlas-only")
    if len(outcome.discovery.candidates) != 1 or outcome.discovery.candidates[0].represented.identity.value != item.identity.value:
        raise RuntimeError("F5-A discovery produced a non-Atlas Candidate")
    if selection.selected is None or selection.selected.role.value != "required":
        raise RuntimeError("F5-A Atlas Required selection was not preserved")
    if outcome.construction.package.sufficiency.value != "sufficient" or outcome.construction.package.coherence.outcome != "coherent":
        raise RuntimeError("F5-A Atlas-only package is not sufficient and coherent")
    result = {
        "evidence_id": "VE-F5-A-001",
        "fixture": "FX-F5-A v1",
        "expected_result": "ER-F5-A v1",
        "execution_utc": datetime.now(UTC).isoformat(),
        "environment": {"python": sys.version, "platform": platform.platform(), "markdown_it": markdown_it.__version__},
        "authorization_governance_boundary": {
            "atlas_project": "fixture-atlas-f5",
            "beacon_project": "fixture-beacon-f5",
            "governed_atlas_beacon_relationship": "absent",
            "cross_project_requester_authorization": "denied",
            "beacon_consumer_disclosure": "not_established",
            "atlas_authorization": "allowed",
            "effective_asu_discovery_boundary": "Atlas-only; Beacon excluded before inspection/discovery/representation",
            "uninspected_unauthorized_source_identity": BEACON_SOURCE,
        },
        "bootstrap": outcome.bootstrap,
        "configuration": outcome.configuration,
        "source_observations": [{"source": atlas.identity, "git": git_observation, "markdown": markdown_observation, "transformation": transformed}],
        "represented_information": [item],
        "discovery": outcome.discovery,
        "applicability_and_selection": [{"represented_information": item.identity.value, "applicability": decision, "selection": selection}],
        "construction": outcome.construction,
        "renderings": {kind: {"status": value.status, "reason_codes": value.reason_codes, "reference": value.rendering.representation_reference if value.rendering else None} for kind, value in renderings.items()},
        "audit": store.audit_for_project("fixture-atlas-f5", authorized=True),
    }
    (OUT / "raw-result.json").write_text(json.dumps(normalize(result), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"evidence_id": "VE-F5-A-001", "output": str(OUT), "inspected_sources": [atlas.identity], "represented": [item.identity.value], "candidates": [candidate.represented.identity.value for candidate in outcome.discovery.candidates], "selected": [{"represented": selected.represented.identity.value, "role": selected.role.value} for selected in outcome.construction.package.items], "sufficiency": outcome.construction.package.sufficiency.value, "coherence": outcome.construction.package.coherence.outcome, "rendering_statuses": {key: value.status for key, value in renderings.items()}}, sort_keys=True))


if __name__ == "__main__":
    main()
