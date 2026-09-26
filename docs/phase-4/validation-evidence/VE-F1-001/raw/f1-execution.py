"""Execution-only orchestration of frozen FX-F1 through existing v0.1 APIs."""
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
from context_engine.application.decision_pipeline import ApplicabilityInputs, EnforcementInputs, RelevanceOutcome, RoleInputs
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


ROOT = Path(__file__).resolve().parents[1] / "home" / "lobsterboss79" / "Projects" / "context-engine"
if not ROOT.exists():
    ROOT = Path.cwd()
FIXTURE = ROOT / "docs/phase-4/ws2-item-2.1-fixtures/F1"
OUT = Path("/tmp/context-engine-ve-f1-001")


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
    sources = (
        ("SRC-F1-CHARTER", "sources/atlas-charter.md", "RI-F1-RELEASE-CONSTRAINT", "PROV-F1-RELEASE-CONSTRAINT", "OBS-F1-CHARTER"),
        ("SRC-F1-DELIVERY", "sources/atlas-delivery.md", "RI-F1-AVAILABILITY", "PROV-F1-AVAILABILITY", "OBS-F1-DELIVERY"),
    )
    request = ContextRequest(
        ident("request", "REQ-F1-RELEASE-CHECKLIST"), ident("project", "fixture-atlas-f1"),
        Requester(RequesterId(ident("requester", "fixture-requester"))),
        Consumer(ConsumerId(ident("consumer", "fixture-human"))),
        TaskIntent("prepare the field-kit release checklist"), TaskScope("field-kit-release"),
    )
    registered = tuple(
        RegisteredSource(source_id, "fixture-atlas-f1", "git", "field-kit-release", Availability.AVAILABLE, str(ROOT))
        for source_id, *_ in sources
    )
    universe = ApplicableSourceUniverse(request.identity.value, registered, BoundaryAdequacy.ADEQUATE,
        "FX-F1 explicit synthetic Project registration and task mapping; both named Sources available and inspected")

    git = LocalGitSourceAdapter()
    observations = []
    represented = []
    evidence = []
    for source, (source_id, locator, ri_id, prov_id, obs_id) in zip(registered, sources, strict=True):
        git_observation = git.observe(source, inspection_authorized=True)
        markdown_observation = observe_markdown_artifact(FIXTURE, locator)
        if markdown_observation.outcome != "observed" or markdown_observation.original_markdown is None:
            raise RuntimeError(f"F1 Markdown observation failed for {locator}")
        observation_provenance = Provenance(
            ident("provenance", f"PROV-{obs_id}"), origin_projects=(request.project,), source=ident("source", source_id),
            observation=ident("observation", obs_id), transformation=TransformationKind.DIRECT,
            location_reference=locator,
        )
        transformation = transform_markdown(
            source_identity=ident("source", source_id), artifact_identity=ident("artifact", f"ART-F1-{source_id}"),
            artifact_version_identity=ident("artifact_version", f"ARTV-F1-{source_id}"), source_locator=locator,
            native_state_reference=git_observation.head, original_markdown=markdown_observation.original_markdown,
            observation_provenance=observation_provenance,
        )
        semantic_provenance = Provenance(
            ident("provenance", prov_id), origin_projects=(request.project,), source=ident("source", source_id),
            artifact=transformation.artifact.identity, artifact_version=transformation.version.identity,
            observation=ident("observation", obs_id), upstream=(observation_provenance.identity,),
            transformation=TransformationKind.NORMALIZED, location_reference=locator,
            transformation_reference=f"{transformation.parser_configuration}; version={transformation.parser_version}",
        )
        item = RepresentedInformation(ident("represented_information", ri_id), ident("artifact", f"ART-F1-{source_id}"), semantic_provenance)
        represented.append(item)
        evidence.append(__import__("context_engine.application.discovery", fromlist=["DiscoveryEvidence"]).DiscoveryEvidence(
            item, source, text=markdown_observation.original_markdown, markdown_kinds=tuple(block.kind for block in transformation.blocks),
        ))
        observations.append({"source_id": source_id, "git": git_observation, "markdown": markdown_observation, "transformation": transformation, "represented": item})

    enforcement = EnforcementInputs(True, request.project, request.project, True, True)
    applicability = (
        ("RI-F1-RELEASE-CONSTRAINT", ApplicabilityInputs(RelevanceOutcome.RELEVANT,
            "FX-F1 explicit task mapping: sealed-case constraint applies to the release checklist", True, enforcement)),
        ("RI-F1-AVAILABILITY", ApplicabilityInputs(RelevanceOutcome.RELEVANT,
            "FX-F1 explicit task mapping: availability supports preparation/validation of the release checklist", True, enforcement)),
    )
    roles = (
        ("RI-F1-RELEASE-CONSTRAINT", RoleInputs(True, False, False,
            "FX-F1 omission basis: omission risks an incorrect release checklist")),
        ("RI-F1-AVAILABILITY", RoleInputs(False, False, True,
            "FX-F1 supporting basis: availability materially improves preparation/validation without changing the constraint")),
    )
    bootstrap, project = FIXTURE / "bootstrap.toml", FIXTURE / "project.toml"
    store = SQLiteStateStore(OUT / "f1-state.sqlite")
    store.initialize()
    human_contract = ConsumerContract(ConsumerKind.HUMAN, request.consumer, True)
    inputs = GovernedRenderInputs(
        bootstrap, project, True, request, universe, tuple(evidence), ("sealed case", "available", "field-kit release"),
        applicability, roles, "FX-F1 explicit governed selection basis", (), False, False, False,
        ident("package", "PKG-F1-001"), ident("record", "PCR-F1-001"),
        "FX-F1 adequate ASU fully inspected; bounded deterministic discovery complete", human_contract,
        coherence_inputs=CoherenceInputs(basis="FX-F1 no material source/governance/authorization/scope/boundary change; compatibility established"),
    )
    outcome = run_governed_render(inputs, store=store)
    if outcome.construction.package is None:
        raise RuntimeError("F1 logical package was not constructed")
    renderings = {"human": outcome.rendering}
    for kind, consumer_name in ((ConsumerKind.CHATGPT, "fixture-chatgpt"), (ConsumerKind.CODEX, "fixture-codex")):
        contract = ConsumerContract(kind, Consumer(ConsumerId(ident("consumer", consumer_name))), True)
        renderings[kind.value] = render_package(outcome.construction.package, contract)
    for kind, rendering in renderings.items():
        (OUT / f"rendering-{kind}.md").write_text(rendering.content or "", encoding="utf-8")
    result = {
        "evidence_id": "VE-F1-001", "fixture": "FX-F1 v1", "expected_result": "ER-F1 v1",
        "execution_utc": datetime.now(UTC).isoformat(),
        "environment": {"python": sys.version, "platform": platform.platform(), "markdown_it": markdown_it.__version__},
        "bootstrap": outcome.bootstrap, "configuration": outcome.configuration,
        "source_observation_representation": observations,
        "discovery": outcome.discovery,
        "applicability_inputs": applicability, "role_inputs": roles,
        "construction": outcome.construction,
        "renderings": {kind: {"status": item.status, "reason_codes": item.reason_codes, "reference": item.rendering.representation_reference if item.rendering else None} for kind, item in renderings.items()},
        "audit": store.audit_for_project("fixture-atlas-f1", authorized=True),
    }
    (OUT / "raw-result.json").write_text(json.dumps(normalize(result), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"evidence_id": "VE-F1-001", "output": str(OUT), "rendering_statuses": {key: value.status for key, value in renderings.items()}, "sufficiency": outcome.construction.package.sufficiency.value, "coherence": outcome.construction.package.coherence.outcome, "candidates": [item.represented.identity.value for item in outcome.discovery.candidates], "selected": [{"represented": item.represented.identity.value, "role": item.role.value} for item in outcome.construction.package.items], "manifest": [item.source.value for item in outcome.construction.package.manifest.entries]}, sort_keys=True))


if __name__ == "__main__":
    main()
