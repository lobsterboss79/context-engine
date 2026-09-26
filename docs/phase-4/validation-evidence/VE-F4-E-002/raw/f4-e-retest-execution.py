"""Authorized retest of frozen FX-F4-E through the corrected general API."""
from __future__ import annotations

from dataclasses import asdict, is_dataclass
from datetime import UTC, datetime
from enum import Enum
import json
from pathlib import Path
import platform
import sys
import tomllib

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
from context_engine.application.sufficiency import RequiredDeficiency, SufficiencyInputs, evaluate_sufficiency
from context_engine.core.model import Consumer, ConsumerId, ContextRequest, Currentness, CurrentnessAssessment, EpistemicState, GovernanceAssessment, GovernanceState, Provenance, RepresentedInformation, Requester, RequesterId, SemanticIdentity, TaskIntent, TaskScope, TransformationKind, Uncertainty

ROOT = Path.cwd()
FIXTURE = ROOT / "docs/phase-4/ws2-item-2.1-fixtures/F4-E"
OUT = ROOT / "docs/phase-4/validation-evidence/VE-F4-E-002/raw"


def ident(kind, value): return SemanticIdentity(kind, value)


def normalize(value):
    if isinstance(value, Enum): return value.value
    if isinstance(value, Path): return str(value)
    if is_dataclass(value): return {key: normalize(item) for key, item in asdict(value).items()}
    if isinstance(value, tuple): return [normalize(item) for item in value]
    if isinstance(value, list): return [normalize(item) for item in value]
    if isinstance(value, dict): return {str(key): normalize(item) for key, item in value.items()}
    return value


def load_controlled_request():
    with (FIXTURE / "controlled-request.toml").open("rb") as stream:
        controlled = tomllib.load(stream)
    assert controlled["fixture"]["identity"] == "FX-F4-E"
    assert controlled["fixture"]["pre_execution_established"] is True
    assert controlled["fixture"]["engine_may_invent_or_modify_task_boundary"] is False
    assert controlled["broad_task"]["identity"] == "REQ-F4E-BROAD-RELEASE-RECOMMENDATION"
    assert controlled["bounded_subtask"]["identity"] == "REQ-F4E-INVENTORY-READINESS"
    assert controlled["bounded_subtask"]["explicitly_established_before_execution"] is True
    assert controlled["bounded_subtask"]["materially_bounded"] is True
    assert controlled["bounded_subtask"]["safe_without_broad_required_decision"] is True
    return controlled


def observed_item(request, source, relative_path, ri, label):
    git_observation = LocalGitSourceAdapter().observe(source, inspection_authorized=True)
    markdown_observation = observe_markdown_artifact(FIXTURE, relative_path)
    if markdown_observation.outcome != "observed" or markdown_observation.original_markdown is None:
        raise RuntimeError(f"F4-E Markdown observation failed for {source.identity}")
    direct = Provenance(ident("provenance", f"PROV-OBS-F4E-{label}"), origin_projects=(request.project,), source=ident("source", source.identity), observation=ident("observation", f"OBS-F4E-{label}"), transformation=TransformationKind.DIRECT, location_reference=relative_path)
    transformed = transform_markdown(source_identity=ident("source", source.identity), artifact_identity=ident("artifact", f"ART-F4E-{label}"), artifact_version_identity=ident("artifact_version", f"ARTV-F4E-{label}"), source_locator=relative_path, native_state_reference=git_observation.head, original_markdown=markdown_observation.original_markdown, observation_provenance=direct)
    provenance = Provenance(ident("provenance", f"PROV-F4E-{label}"), origin_projects=(request.project,), source=ident("source", source.identity), artifact=transformed.artifact.identity, artifact_version=transformed.version.identity, observation=ident("observation", f"OBS-F4E-{label}"), upstream=(direct.identity,), transformation=TransformationKind.NORMALIZED, location_reference=relative_path, transformation_reference=f"{transformed.parser_configuration}; version={transformed.parser_version}")
    item = RepresentedInformation(ident("represented_information", ri), ident("claim", ri), provenance)
    evidence = DiscoveryEvidence(item, source, text=markdown_observation.original_markdown, markdown_kinds=("heading", "paragraph", "list_item"), governance=(GovernanceAssessment(item.subject, GovernanceState.APPROVED, item.provenance),), currentness=(CurrentnessAssessment(item.subject, Currentness.CURRENT),))
    return item, evidence, {"source": source.identity, "git": git_observation, "markdown": markdown_observation, "transformation": transformed}


def main():
    controlled = load_controlled_request()
    OUT.mkdir(parents=True, exist_ok=True)
    requester = Requester(RequesterId(ident("requester", controlled["authorization"]["requester_identity"])))
    request = ContextRequest(ident("request", controlled["bounded_subtask"]["identity"]), ident("project", controlled["fixture"]["project"]), requester, Consumer(ConsumerId(ident("consumer", "fixture-human"))), TaskIntent(controlled["bounded_subtask"]["purpose"]), TaskScope(controlled["bounded_subtask"]["scope"]))
    inventory = RegisteredSource("SRC-F4E-INVENTORY-REGISTER", request.project.value, "git", request.scope.description, Availability.AVAILABLE, str(ROOT))
    packing = RegisteredSource("SRC-F4E-PACKING-CHECKLIST", request.project.value, "git", request.scope.description, Availability.AVAILABLE, str(ROOT))
    missing = RegisteredSource("SRC-F4E-FINAL-RELEASE-DECISION", request.project.value, "git", controlled["broad_task"]["scope"], Availability.UNAVAILABLE, None)
    inventory_item, inventory_evidence, inventory_observation = observed_item(request, inventory, "sources/inventory-register.md", "RI-F4E-INVENTORY-READINESS", "INVENTORY")
    packing_item, packing_evidence, packing_observation = observed_item(request, packing, "sources/packing-checklist.md", "RI-F4E-PACKING-READINESS", "PACKING")
    bounded_universe = ApplicableSourceUniverse(request.identity.value, (inventory, packing), BoundaryAdequacy.ADEQUATE, controlled["bounded_asu"]["basis"])
    broad_universe = ApplicableSourceUniverse(controlled["broad_task"]["identity"], (missing, inventory, packing), BoundaryAdequacy.KNOWN_INCOMPLETE, controlled["broad_asu"]["basis"])
    deficiency = RequiredDeficiency(ident("represented_information", controlled["required_deficiency"]["represented_identity"]), controlled["required_deficiency"]["basis"], can_proceed_bounded_without=controlled["required_deficiency"]["can_proceed_bounded_without"], limitation=Uncertainty(EpistemicState.UNAVAILABLE, evidence_boundary=controlled["required_deficiency"]["source_identity"], detail="Required broad final-release decision is unavailable; its content was not observed, represented as content, or fabricated."))
    broad_qualification = Uncertainty(EpistemicState.UNKNOWN,
        evidence_boundary=f"{controlled['broad_asu']['identity']}; {controlled['required_deficiency']['source_identity']}",
        detail=(f"Broad task {controlled['broad_task']['identity']} is {controlled['broad_task']['expected_sufficiency']}; "
                f"broad ASU {controlled['broad_asu']['identity']} is {controlled['broad_asu']['adequacy']}; "
                f"Required {controlled['required_deficiency']['represented_identity']} remains unavailable. "
                f"This package is conditionally sufficient only for bounded task {controlled['bounded_subtask']['identity']}; "
                "it does not recommend, approve, or authorize release."))
    enforcement = EnforcementInputs(True, request.project, request.project, controlled["authorization"]["requester_authorized"], True)
    applicability = ApplicabilityInputs(RelevanceOutcome.RELEVANT, "FX-F4-E frozen bounded-task mapping: this Source supplies a necessary inventory-readiness fact only.", True, enforcement)
    inventory_role = RoleInputs(True, True, False, "FX-F4-E bounded omission basis: without the inventory register, verified inventory count and staged case readiness cannot be established.")
    packing_role = RoleInputs(True, True, False, "FX-F4-E bounded omission basis: without the packing checklist, packing-material availability and checklist-preparation readiness cannot be established.")
    store = SQLiteStateStore(OUT / "f4-e-state.sqlite"); store.initialize()
    inputs = GovernedRenderInputs(FIXTURE / "bootstrap.toml", FIXTURE / "project.toml", True, request, bounded_universe, (inventory_evidence, packing_evidence), ("inventory", "packing", "checklist", "readiness"), ((inventory_item.identity.value, applicability), (packing_item.identity.value, applicability)), ((inventory_item.identity.value, inventory_role), (packing_item.identity.value, packing_role)), "FX-F4-E frozen bounded governed selection: both available readiness items are Required only for REQ-F4E-INVENTORY-READINESS; neither substitutes for the broad final-release decision.", (deficiency,), False, False, True, ident("package", controlled["construction"]["bounded_package_identity"]), ident("record", controlled["construction"]["bounded_construction_record_identity"]), "FX-F4-E bounded package: supports only REQ-F4E-INVENTORY-READINESS; broad REQ-F4E-BROAD-RELEASE-RECOMMENDATION remains Insufficient because SRC-F4E-FINAL-RELEASE-DECISION is unavailable and Required.", ConsumerContract(ConsumerKind.HUMAN, request.consumer, True), coherence_inputs=CoherenceInputs(understood_qualified_state=True, basis=controlled["construction"]["coherence_basis"]), construction_qualifications=(broad_qualification,))
    outcome = run_governed_render(inputs, store=store)
    if outcome.construction.package is None: raise RuntimeError("F4-E bounded logical package was not constructed")
    decisions = []
    for item, role in ((inventory_item, inventory_role), (packing_item, packing_role)):
        decision = evaluate_applicability(next(candidate for candidate in outcome.discovery.candidates if candidate.represented.identity == item.identity), applicability)
        decisions.append({"represented_information": item.identity.value, "applicability": decision, "selection": select_candidate(decision, role, selection_basis=inputs.selection_basis)})
    broad_sufficiency = evaluate_sufficiency(SufficiencyInputs(tuple(), broad_universe, (deficiency,), False, False, False))
    renderings = {"human": outcome.rendering}
    for kind, name in ((ConsumerKind.CHATGPT, "fixture-chatgpt"), (ConsumerKind.CODEX, "fixture-codex")):
        renderings[kind.value] = render_package(outcome.construction.package, ConsumerContract(kind, Consumer(ConsumerId(ident("consumer", name))), True))
    for kind, rendering in renderings.items():
        (OUT / f"rendering-{kind}.md").write_text(rendering.content or "", encoding="utf-8")
    assert broad_sufficiency.outcome.value == controlled["broad_task"]["expected_sufficiency"]
    assert outcome.construction.package.sufficiency.value == controlled["bounded_subtask"]["expected_sufficiency"]
    assert broad_qualification in outcome.construction.package.limitations
    assert outcome.construction.package.limitations == outcome.construction.record.limitations
    for rendering in renderings.values():
        assert rendering.content is not None and broad_qualification.detail in rendering.content
    result = {"evidence_id":"VE-F4-E-002", "original_evidence":"VE-F4-E-001", "fixture":"FX-F4-E v1", "expected_result":"ER-F4-E v1", "execution_utc":datetime.now(UTC).isoformat(), "environment":{"python":sys.version, "platform":platform.platform(), "markdown_it":markdown_it.__version__}, "controlled_request":controlled, "bootstrap":outcome.bootstrap, "configuration":outcome.configuration, "source_observations":[inventory_observation, packing_observation, {"source":missing.identity, "availability":missing.availability.value, "observation":"not attempted: frozen unavailable broad Required Source; no Source content artifact exists"}], "represented_information":[inventory_item, packing_item], "known_required_deficiency":deficiency, "broad_package_qualification":broad_qualification, "bounded_discovery":outcome.discovery, "applicability_and_selection":decisions, "broad_asu":broad_universe, "bounded_asu":bounded_universe, "broad_sufficiency":broad_sufficiency, "bounded_construction":outcome.construction, "renderings":{kind:{"status":value.status, "reason_codes":value.reason_codes, "reference":value.rendering.representation_reference if value.rendering else None} for kind, value in renderings.items()}, "audit":store.audit_for_project(request.project.value, authorized=True)}
    (OUT / "raw-result.json").write_text(json.dumps(normalize(result), indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(json.dumps({"evidence_id":"VE-F4-E-002", "original_evidence":"VE-F4-E-001", "output":str(OUT), "represented":[inventory_item.identity.value, packing_item.identity.value], "candidates":[x.represented.identity.value for x in outcome.discovery.candidates], "selected":[{"represented":x.represented.identity.value, "role":x.role.value} for x in outcome.construction.package.items], "broad_sufficiency":broad_sufficiency.outcome.value, "bounded_sufficiency":outcome.construction.package.sufficiency.value, "coherence":outcome.construction.package.coherence.outcome, "required_deficiencies":[deficiency.identity.value], "rendering_statuses":{key:value.status for key,value in renderings.items()}}, sort_keys=True))


if __name__ == "__main__": main()
