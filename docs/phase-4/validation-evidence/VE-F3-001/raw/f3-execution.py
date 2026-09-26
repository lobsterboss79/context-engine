"""Execution-only orchestration of frozen FX-F3 through existing v0.1 APIs."""
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
    Conflict, Consumer, ConsumerId, ContextRequest, Currentness,
    CurrentnessAssessment, EpistemicState, GovernanceAssessment,
    GovernanceState, Provenance, RepresentedInformation, Requester,
    RequesterId, SemanticIdentity, TaskIntent, TaskScope, TransformationKind,
    Uncertainty,
)


ROOT = Path.cwd()
FIXTURE = ROOT / "docs/phase-4/ws2-item-2.1-fixtures/F3"
OUT = Path("/tmp/context-engine-ve-f3-001")


def ident(kind: str, value: str) -> SemanticIdentity:
    return SemanticIdentity(kind, value)


def normalize(value):
    if isinstance(value, Enum): return value.value
    if isinstance(value, Path): return str(value)
    if is_dataclass(value): return {key: normalize(item) for key, item in asdict(value).items()}
    if isinstance(value, tuple): return [normalize(item) for item in value]
    if isinstance(value, list): return [normalize(item) for item in value]
    if isinstance(value, dict): return {str(key): normalize(item) for key, item in value.items()}
    return value


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    request = ContextRequest(
        ident("request", "REQ-F3-RELEASE-RECOMMENDATION"), ident("project", "fixture-atlas-f3"),
        Requester(RequesterId(ident("requester", "fixture-requester"))),
        Consumer(ConsumerId(ident("consumer", "fixture-human"))),
        TaskIntent("prepare a current release recommendation while preserving controlled qualifications"),
        TaskScope("field-kit-release"),
    )
    definitions = (
        ("RI-F3-SEALED", "SRC-F3-CURRENT", "current-decision.md", "ART-F3-SEALED", "ARTV-F3-SEALED", "OBS-F3-SEALED", "PROV-F3-SEALED", Currentness.CURRENT, GovernanceState.APPROVED, ()),
        ("RI-F3-TOTE", "SRC-F3-COMPETING", "competing-decision.md", "ART-F3-TOTE", "ARTV-F3-TOTE", "OBS-F3-TOTE", "PROV-F3-TOTE", Currentness.CURRENT, GovernanceState.APPROVED, ()),
        ("RI-F3-CANVAS-HISTORY", "SRC-F3-HISTORY", "historical-note.md", "ART-F3-CANVAS-HISTORY", "ARTV-F3-CANVAS-HISTORY", "OBS-F3-CANVAS-HISTORY", "PROV-F3-CANVAS-HISTORY", Currentness.HISTORICAL, GovernanceState.APPROVED, ()),
        ("RI-F3-DEPOT-UNVERIFIED", "SRC-F3-QUALIFICATION", "qualification.md", "ART-F3-DEPOT-UNVERIFIED", "ARTV-F3-DEPOT-UNVERIFIED", "OBS-F3-DEPOT-UNVERIFIED", "PROV-F3-DEPOT-UNVERIFIED", Currentness.UNKNOWN, GovernanceState.UNKNOWN, (Uncertainty(EpistemicState.UNVERIFIED, evidence_boundary="UNC-F3-DEPOT", detail="FX-F3 governed depot availability remains unverified"),)),
    )
    sources, represented, evidence, observations = [], [], [], []
    provisional = {}
    adapter = LocalGitSourceAdapter()
    for ri_id, source_id, filename, artifact_id, version_id, observation_id, provenance_id, currentness, governance_state, uncertainty in definitions:
        source = RegisteredSource(source_id, "fixture-atlas-f3", "git", "field-kit-release", Availability.AVAILABLE, str(ROOT))
        sources.append(source)
        git_observation = adapter.observe(source, inspection_authorized=True)
        markdown_observation = observe_markdown_artifact(FIXTURE, "sources/" + filename)
        if markdown_observation.outcome != "observed" or markdown_observation.original_markdown is None:
            raise RuntimeError("F3 Markdown observation failed: " + filename)
        direct = Provenance(ident("provenance", "PROV-OBS-F3-" + source_id.removeprefix("SRC-F3-")), origin_projects=(request.project,), source=ident("source", source_id), observation=ident("observation", observation_id), transformation=TransformationKind.DIRECT, location_reference="sources/" + filename)
        transformed = transform_markdown(source_identity=ident("source", source_id), artifact_identity=ident("artifact", artifact_id), artifact_version_identity=ident("artifact_version", version_id), source_locator="sources/" + filename, native_state_reference=git_observation.head, original_markdown=markdown_observation.original_markdown, observation_provenance=direct)
        provenance = Provenance(ident("provenance", provenance_id), origin_projects=(request.project,), source=ident("source", source_id), artifact=transformed.artifact.identity, artifact_version=transformed.version.identity, observation=ident("observation", observation_id), upstream=(direct.identity,), transformation=TransformationKind.NORMALIZED, location_reference="sources/" + filename, transformation_reference=f"{transformed.parser_configuration}; version={transformed.parser_version}")
        item = RepresentedInformation(ident("represented_information", ri_id), ident("claim", ri_id), provenance, uncertainty=uncertainty)
        provisional[ri_id] = (source, item, markdown_observation, git_observation, currentness, governance_state)
        represented.append(item)
        observations.append({"source": source_id, "git": git_observation, "markdown": markdown_observation, "transformation": transformed})
    conflict = Conflict(ident("conflict", "CON-F3-CASE-CHOICE"), (ident("represented_information", "RI-F3-SEALED"), ident("represented_information", "RI-F3-TOTE")), "current field-kit case choice; no governed supersession supplied", provisional["RI-F3-SEALED"][1].provenance)
    for ri_id, source, item, markdown_observation, git_observation, currentness, governance_state in ((key, *value) for key, value in provisional.items()):
        governance = (GovernanceAssessment(item.subject, governance_state, item.provenance),)
        temporal = (CurrentnessAssessment(item.subject, currentness),)
        conflicts = (conflict,) if ri_id in {"RI-F3-SEALED", "RI-F3-TOTE"} else ()
        evidence.append(DiscoveryEvidence(item, source, text=markdown_observation.original_markdown or "", markdown_kinds=("heading", "paragraph"), governance=governance, currentness=temporal, conflicts=conflicts))
    universe = ApplicableSourceUniverse(request.identity.value, tuple(sources), BoundaryAdequacy.ADEQUATE, "FX-F3 explicit synthetic four-Source ASU; adequacy is established by frozen fixture governance")
    enforcement = EnforcementInputs(True, request.project, request.project, True, True)
    applicability = tuple((item.identity.value, ApplicabilityInputs(RelevanceOutcome.RELEVANT, "FX-F3 frozen governed task mapping establishes applicable qualified release context", True, enforcement)) for item in represented)
    roles = (
        ("RI-F3-SEALED", RoleInputs(True, False, False, "FX-F3 omission basis: omission conceals material current sealed-case guidance")),
        ("RI-F3-TOTE", RoleInputs(True, False, False, "FX-F3 omission basis: omission conceals material incompatible current tote guidance")),
        ("RI-F3-CANVAS-HISTORY", RoleInputs(False, False, True, "FX-F3 supporting basis: historical state materially qualifies current recommendation without becoming current")),
        ("RI-F3-DEPOT-UNVERIFIED", RoleInputs(False, False, True, "FX-F3 supporting basis: unverified depot availability materially qualifies the task without establishing availability")),
    )
    store = SQLiteStateStore(OUT / "f3-state.sqlite")
    store.initialize()
    inputs = GovernedRenderInputs(FIXTURE / "bootstrap.toml", FIXTURE / "project.toml", True, request, universe, tuple(evidence), ("field-kit", "release", "case", "tote", "canvas", "depot"), applicability, roles, "FX-F3 explicit governed selection preserves all applicable qualified context; no precedence or resolution is supplied", (), True, True, False, ident("package", "PKG-F3-001"), ident("record", "PCR-F3-001"), "FX-F3 adequate ASU fully inspected; unresolved current conflict and depot uncertainty preserved", ConsumerContract(ConsumerKind.HUMAN, request.consumer, True), coherence_inputs=CoherenceInputs(understood_qualified_state=True, basis="FX-F3 intentional unresolved current conflict, historical state, and uncertainty are explicitly preserved; construction is coherent with qualification"))
    outcome = run_governed_render(inputs, store=store)
    if outcome.construction.package is None: raise RuntimeError("F3 logical package was not constructed")
    role_by_id, applicability_by_id = dict(roles), dict(applicability)
    decisions = []
    for candidate in outcome.discovery.candidates:
        decision = evaluate_applicability(candidate, applicability_by_id[candidate.represented.identity.value])
        selection = select_candidate(decision, role_by_id[candidate.represented.identity.value], selection_basis=inputs.selection_basis)
        decisions.append({"represented_information": candidate.represented.identity.value, "applicability": decision, "selection": selection})
    renderings = {"human": outcome.rendering}
    for kind, name in ((ConsumerKind.CHATGPT, "fixture-chatgpt"), (ConsumerKind.CODEX, "fixture-codex")):
        renderings[kind.value] = render_package(outcome.construction.package, ConsumerContract(kind, Consumer(ConsumerId(ident("consumer", name))), True))
    for kind, rendering in renderings.items(): (OUT / f"rendering-{kind}.md").write_text(rendering.content or "", encoding="utf-8")
    result = {"evidence_id": "VE-F3-001", "fixture": "FX-F3 v1", "expected_result": "ER-F3 v1", "execution_utc": datetime.now(UTC).isoformat(), "environment": {"python": sys.version, "platform": platform.platform(), "markdown_it": markdown_it.__version__}, "bootstrap": outcome.bootstrap, "configuration": outcome.configuration, "source_observations": observations, "represented_information": represented, "discovery": outcome.discovery, "applicability_and_selection": decisions, "construction": outcome.construction, "renderings": {kind: {"status": value.status, "reason_codes": value.reason_codes, "reference": value.rendering.representation_reference if value.rendering else None} for kind, value in renderings.items()}, "audit": store.audit_for_project("fixture-atlas-f3", authorized=True)}
    (OUT / "raw-result.json").write_text(json.dumps(normalize(result), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"evidence_id": "VE-F3-001", "output": str(OUT), "represented": [item.identity.value for item in represented], "candidates": [item.represented.identity.value for item in outcome.discovery.candidates], "selected": [{"represented": item.represented.identity.value, "role": item.role.value} for item in outcome.construction.package.items], "sufficiency": outcome.construction.package.sufficiency.value, "coherence": outcome.construction.package.coherence.outcome, "rendering_statuses": {key: value.status for key, value in renderings.items()}}, sort_keys=True))


if __name__ == "__main__": main()
