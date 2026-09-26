"""Execution-only orchestration of frozen FX-F4-A through existing v0.1 APIs."""
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
FIXTURE = ROOT / "docs/phase-4/ws2-item-2.1-fixtures/F4-A"
OUT = Path("/tmp/context-engine-ve-f4-a-001")

def ident(kind, value): return SemanticIdentity(kind, value)
def normalize(value):
    if isinstance(value, Enum): return value.value
    if isinstance(value, Path): return str(value)
    if is_dataclass(value): return {key: normalize(item) for key, item in asdict(value).items()}
    if isinstance(value, tuple): return [normalize(item) for item in value]
    if isinstance(value, list): return [normalize(item) for item in value]
    if isinstance(value, dict): return {str(key): normalize(item) for key, item in value.items()}
    return value

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    request = ContextRequest(ident("request", "REQ-F4-RELEASE-CHECKLIST"), ident("project", "fixture-atlas-f4"), Requester(RequesterId(ident("requester", "fixture-requester"))), Consumer(ConsumerId(ident("consumer", "fixture-human"))), TaskIntent("prepare the controlled field-kit release checklist"), TaskScope("field-kit-release"))
    source = RegisteredSource("SRC-F4A-DECISION", "fixture-atlas-f4", "git", "field-kit-release", Availability.AVAILABLE, str(ROOT))
    git_observation = LocalGitSourceAdapter().observe(source, inspection_authorized=True)
    markdown_observation = observe_markdown_artifact(FIXTURE, "sources/release-decision.md")
    if markdown_observation.outcome != "observed" or markdown_observation.original_markdown is None: raise RuntimeError("F4-A Markdown observation failed")
    direct = Provenance(ident("provenance", "PROV-OBS-F4A-DECISION"), origin_projects=(request.project,), source=ident("source", "SRC-F4A-DECISION"), observation=ident("observation", "OBS-F4A-DECISION"), transformation=TransformationKind.DIRECT, location_reference="sources/release-decision.md")
    transformed = transform_markdown(source_identity=ident("source", "SRC-F4A-DECISION"), artifact_identity=ident("artifact", "ART-F4A-DECISION"), artifact_version_identity=ident("artifact_version", "ARTV-F4A-DECISION"), source_locator="sources/release-decision.md", native_state_reference=git_observation.head, original_markdown=markdown_observation.original_markdown, observation_provenance=direct)
    provenance = Provenance(ident("provenance", "PROV-F4A-DECISION"), origin_projects=(request.project,), source=ident("source", "SRC-F4A-DECISION"), artifact=transformed.artifact.identity, artifact_version=transformed.version.identity, observation=ident("observation", "OBS-F4A-DECISION"), upstream=(direct.identity,), transformation=TransformationKind.NORMALIZED, location_reference="sources/release-decision.md", transformation_reference=f"{transformed.parser_configuration}; version={transformed.parser_version}")
    item = RepresentedInformation(ident("represented_information", "RI-F4-REQUIRED-DECISION"), ident("claim", "RI-F4-REQUIRED-DECISION"), provenance)
    evidence = DiscoveryEvidence(item, source, text=markdown_observation.original_markdown, markdown_kinds=("heading", "paragraph"), governance=(GovernanceAssessment(item.subject, GovernanceState.APPROVED, item.provenance),), currentness=(CurrentnessAssessment(item.subject, Currentness.CURRENT),))
    universe = ApplicableSourceUniverse(request.identity.value, (source,), BoundaryAdequacy.ADEQUATE, "FX-F4-A frozen adequate ASU: available required decision is the controlled applicable Source")
    enforcement = EnforcementInputs(True, request.project, request.project, True, True)
    applicability = ApplicabilityInputs(RelevanceOutcome.RELEVANT, "FX-F4-A frozen task mapping establishes applicable required release decision", True, enforcement)
    role = RoleInputs(True, False, False, "FX-F4-A omission basis: omitting the required release decision would make the checklist materially incorrect")
    store = SQLiteStateStore(OUT / "f4-a-state.sqlite"); store.initialize()
    inputs = GovernedRenderInputs(FIXTURE / "bootstrap.toml", FIXTURE / "project.toml", True, request, universe, (evidence,), ("field-kit", "release", "checklist", "sealed", "case"), ((item.identity.value, applicability),), ((item.identity.value, role),), "FX-F4-A frozen governed selection of the available required decision", (), False, False, False, ident("package", "PKG-F4-A-001"), ident("record", "PCR-F4-A-001"), "FX-F4-A adequate ASU fully inspected; no conflict or material uncertainty", ConsumerContract(ConsumerKind.HUMAN, request.consumer, True), coherence_inputs=CoherenceInputs())
    outcome = run_governed_render(inputs, store=store)
    if outcome.construction.package is None: raise RuntimeError("F4-A logical package was not constructed")
    decision = evaluate_applicability(outcome.discovery.candidates[0], applicability)
    selection = select_candidate(decision, role, selection_basis=inputs.selection_basis)
    renderings = {"human": outcome.rendering}
    for kind, name in ((ConsumerKind.CHATGPT, "fixture-chatgpt"), (ConsumerKind.CODEX, "fixture-codex")):
        renderings[kind.value] = render_package(outcome.construction.package, ConsumerContract(kind, Consumer(ConsumerId(ident("consumer", name))), True))
    for kind, rendering in renderings.items(): (OUT / f"rendering-{kind}.md").write_text(rendering.content or "", encoding="utf-8")
    result = {"evidence_id":"VE-F4-A-001", "fixture":"FX-F4-A v1", "expected_result":"ER-F4-A v1", "execution_utc":datetime.now(UTC).isoformat(), "environment":{"python":sys.version,"platform":platform.platform(),"markdown_it":markdown_it.__version__}, "bootstrap":outcome.bootstrap, "configuration":outcome.configuration, "source_observations":[{"source":source.identity,"git":git_observation,"markdown":markdown_observation,"transformation":transformed}], "represented_information":[item], "discovery":outcome.discovery, "applicability_and_selection":[{"represented_information":item.identity.value,"applicability":decision,"selection":selection}], "construction":outcome.construction, "renderings":{kind:{"status":value.status,"reason_codes":value.reason_codes,"reference":value.rendering.representation_reference if value.rendering else None} for kind,value in renderings.items()}, "audit":store.audit_for_project("fixture-atlas-f4", authorized=True)}
    (OUT / "raw-result.json").write_text(json.dumps(normalize(result), indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(json.dumps({"evidence_id":"VE-F4-A-001","output":str(OUT),"represented":[item.identity.value],"candidates":[x.represented.identity.value for x in outcome.discovery.candidates],"selected":[{"represented":x.represented.identity.value,"role":x.role.value} for x in outcome.construction.package.items],"sufficiency":outcome.construction.package.sufficiency.value,"coherence":outcome.construction.package.coherence.outcome,"rendering_statuses":{key:value.status for key,value in renderings.items()}}, sort_keys=True))
if __name__ == "__main__": main()
