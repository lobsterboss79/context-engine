"""Execution-only orchestration of frozen FX-F2 through existing v0.1 APIs."""
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
    ApplicabilityInputs, EnforcementInputs, RelevanceOutcome, RoleInputs,
    evaluate_applicability, select_candidate,
)
from context_engine.application.discovery import DiscoveryEvidence
from context_engine.application.lifecycle import ApplicableSourceUniverse, Availability, BoundaryAdequacy, RegisteredSource
from context_engine.application.orchestration import GovernedRenderInputs, run_governed_render
from context_engine.application.package_construction import CoherenceInputs
from context_engine.application.rendering import ConsumerContract, ConsumerKind, render_package
from context_engine.application.representation import observe_markdown_artifact, transform_markdown
from context_engine.core.model import (
    Consumer, ConsumerId, ContextRequest, Provenance, RepresentedInformation,
    Requester, RequesterId, SemanticIdentity, TaskIntent, TaskScope,
    TransformationKind,
)


ROOT = Path.cwd()
FIXTURE = ROOT / "docs/phase-4/ws2-item-2.1-fixtures/F2"
OUT = Path("/tmp/context-engine-ve-f2-001")


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


def source_section(markdown: str, heading: str) -> str:
    marker = "## " + heading
    start = markdown.index(marker)
    end = markdown.find("\n## ", start + len(marker))
    return markdown[start:] if end == -1 else markdown[start:end]


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    source_id = "SRC-F2-BOUNDARIES"
    locator = "sources/atlas-boundaries.md"
    items = (
        ("RI-F2-CONSTRAINT", "PROV-F2-CONSTRAINT", "OBS-F2-BOUNDARIES", "Release constraint"),
        ("RI-F2-SUPPORT", "PROV-F2-SUPPORT", "OBS-F2-BOUNDARIES", "Supporting note"),
        ("RI-F2-HISTORY", "PROV-F2-HISTORY", "OBS-F2-BOUNDARIES", "Discoverable but non-applicable history"),
        ("RI-F2-IRRELEVANT", "PROV-F2-IRRELEVANT", "OBS-F2-BOUNDARIES", "Irrelevant material"),
    )
    request = ContextRequest(
        ident("request", "REQ-F2-RELEASE-CHECKLIST"), ident("project", "fixture-atlas-f2"),
        Requester(RequesterId(ident("requester", "fixture-requester"))),
        Consumer(ConsumerId(ident("consumer", "fixture-human"))),
        TaskIntent("prepare the field-kit release checklist"), TaskScope("controlled-boundaries"),
    )
    source = RegisteredSource(source_id, "fixture-atlas-f2", "git", "controlled-boundaries", Availability.AVAILABLE, str(ROOT))
    universe = ApplicableSourceUniverse(request.identity.value, (source,), BoundaryAdequacy.ADEQUATE,
        "FX-F2 explicit synthetic single-Source ASU; adequacy is established by frozen fixture governance, not Source count")
    git_observation = LocalGitSourceAdapter().observe(source, inspection_authorized=True)
    markdown_observation = observe_markdown_artifact(FIXTURE, locator)
    if markdown_observation.outcome != "observed" or markdown_observation.original_markdown is None:
        raise RuntimeError("F2 Markdown observation failed")
    original = markdown_observation.original_markdown
    observation_provenance = Provenance(
        ident("provenance", "PROV-OBS-F2-BOUNDARIES"), origin_projects=(request.project,), source=ident("source", source_id),
        observation=ident("observation", "OBS-F2-BOUNDARIES"), transformation=TransformationKind.DIRECT, location_reference=locator,
    )
    transformation = transform_markdown(
        source_identity=ident("source", source_id), artifact_identity=ident("artifact", "ART-F2-BOUNDARIES"),
        artifact_version_identity=ident("artifact_version", "ARTV-F2-BOUNDARIES"), source_locator=locator,
        native_state_reference=git_observation.head, original_markdown=original, observation_provenance=observation_provenance,
    )
    represented, evidence = [], []
    for ri_id, prov_id, obs_id, heading in items:
        provenance = Provenance(
            ident("provenance", prov_id), origin_projects=(request.project,), source=ident("source", source_id),
            artifact=transformation.artifact.identity, artifact_version=transformation.version.identity,
            observation=ident("observation", obs_id), upstream=(observation_provenance.identity,),
            transformation=TransformationKind.NORMALIZED, location_reference=locator,
            transformation_reference=f"{transformation.parser_configuration}; version={transformation.parser_version}",
        )
        item = RepresentedInformation(ident("represented_information", ri_id), ident("artifact", "ART-F2-BOUNDARIES"), provenance)
        represented.append(item)
        evidence.append(DiscoveryEvidence(item, source, text=source_section(original, heading), markdown_kinds=("heading", "paragraph")))
    enforcement = EnforcementInputs(True, request.project, request.project, True, True)
    applicability = (
        ("RI-F2-CONSTRAINT", ApplicabilityInputs(RelevanceOutcome.RELEVANT, "FX-F2 governed mapping: sealed-case constraint applies to current release checklist", True, enforcement)),
        ("RI-F2-SUPPORT", ApplicabilityInputs(RelevanceOutcome.RELEVANT, "FX-F2 governed mapping: blue label supports current release checklist", True, enforcement)),
        ("RI-F2-HISTORY", ApplicabilityInputs(RelevanceOutcome.RELEVANT, "FX-F2 history is discoverable, but its scope is expressly outside current release task", False, enforcement)),
    )
    roles = (
        ("RI-F2-CONSTRAINT", RoleInputs(True, False, False, "FX-F2 omission basis: omission risks incorrect release checklist")),
        ("RI-F2-SUPPORT", RoleInputs(False, False, True, "FX-F2 supporting basis: blue label materially improves preparation without changing constraint")),
    )
    store = SQLiteStateStore(OUT / "f2-state.sqlite")
    store.initialize()
    inputs = GovernedRenderInputs(
        FIXTURE / "bootstrap.toml", FIXTURE / "project.toml", True, request, universe, tuple(evidence),
        ("sealed case", "blue", "canvas bag"), applicability, roles, "FX-F2 explicit governed selection basis", (),
        False, False, False, ident("package", "PKG-F2-001"), ident("record", "PCR-F2-001"),
        "FX-F2 adequate ASU fully inspected; bounded deterministic discovery complete", ConsumerContract(ConsumerKind.HUMAN, request.consumer, True),
        coherence_inputs=CoherenceInputs(basis="FX-F2 no material source/governance/authorization/scope/boundary change; compatibility established"),
    )
    outcome = run_governed_render(inputs, store=store)
    if outcome.construction.package is None:
        raise RuntimeError("F2 logical package was not constructed")
    decisions = []
    role_by_id = dict(roles)
    applicability_by_id = dict(applicability)
    for candidate in outcome.discovery.candidates:
        decision = evaluate_applicability(candidate, applicability_by_id[candidate.represented.identity.value])
        selection = select_candidate(decision, role_by_id[candidate.represented.identity.value], selection_basis=inputs.selection_basis) if candidate.represented.identity.value in role_by_id else None
        decisions.append({"represented_information": candidate.represented.identity.value, "applicability": decision, "selection": selection})
    renderings = {"human": outcome.rendering}
    for kind, consumer_name in ((ConsumerKind.CHATGPT, "fixture-chatgpt"), (ConsumerKind.CODEX, "fixture-codex")):
        renderings[kind.value] = render_package(outcome.construction.package, ConsumerContract(kind, Consumer(ConsumerId(ident("consumer", consumer_name))), True))
    for kind, rendering in renderings.items():
        (OUT / f"rendering-{kind}.md").write_text(rendering.content or "", encoding="utf-8")
    result = {
        "evidence_id": "VE-F2-001", "fixture": "FX-F2 v1", "expected_result": "ER-F2 v1", "execution_utc": datetime.now(UTC).isoformat(),
        "environment": {"python": sys.version, "platform": platform.platform(), "markdown_it": markdown_it.__version__},
        "bootstrap": outcome.bootstrap, "configuration": outcome.configuration, "source_observation": {"git": git_observation, "markdown": markdown_observation, "transformation": transformation},
        "represented_information": represented, "discovery": outcome.discovery, "applicability_and_selection": decisions,
        "construction": outcome.construction, "renderings": {kind: {"status": item.status, "reason_codes": item.reason_codes, "reference": item.rendering.representation_reference if item.rendering else None} for kind, item in renderings.items()},
        "audit": store.audit_for_project("fixture-atlas-f2", authorized=True),
    }
    (OUT / "raw-result.json").write_text(json.dumps(normalize(result), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"evidence_id": "VE-F2-001", "output": str(OUT), "represented": [x.identity.value for x in represented], "candidates": [x.represented.identity.value for x in outcome.discovery.candidates], "selected": [{"represented": x.represented.identity.value, "role": x.role.value} for x in outcome.construction.package.items], "sufficiency": outcome.construction.package.sufficiency.value, "coherence": outcome.construction.package.coherence.outcome, "rendering_statuses": {key: value.status for key, value in renderings.items()}}, sort_keys=True))


if __name__ == "__main__":
    main()
