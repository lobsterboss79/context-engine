"""Execution-only procedure for frozen FX-P4-3C-001 v1."""
from __future__ import annotations

from dataclasses import asdict, is_dataclass
from datetime import UTC, datetime
from enum import Enum
import json
from pathlib import Path
import platform
import sys

import markdown_it

from context_engine.application.decision_pipeline import (
    ApplicabilityInputs, ApplicabilityOutcome, EnforcementInputs,
    RelevanceOutcome, RoleInputs, evaluate_applicability,
)
from context_engine.application.discovery import DiscoveryEvidence
from context_engine.application.lifecycle import (
    ApplicableSourceUniverse, Availability, BoundaryAdequacy, RegisteredSource,
)
from context_engine.application.orchestration import GovernedRenderInputs, run_governed_render
from context_engine.application.package_construction import CoherenceInputs
from context_engine.application.rendering import ConsumerContract, ConsumerKind, render_package
from context_engine.application.representation import observe_markdown_artifact, transform_markdown
from context_engine.application.sufficiency import RequiredDeficiency
from context_engine.core.model import (
    Conflict, Consumer, ConsumerId, ContextRequest, Currentness,
    CurrentnessAssessment, EpistemicState, GovernanceAssessment, GovernanceState,
    Provenance, RepresentedInformation, Requester, RequesterId, SemanticIdentity,
    TaskIntent, TaskScope, TransformationKind, Uncertainty,
)


ROOT = Path.cwd()
LANE = ROOT / "docs/phase-4/ws3-lane-c-inert-preservation"
FIXTURE = LANE / "fixtures"
OUT = Path("/tmp/context-engine-ve-p4-3c-001")


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


def represented(request, source_id, filename, ri_id, currentness, governance, uncertainty=()):
    observed = observe_markdown_artifact(FIXTURE, filename)
    if observed.outcome != "observed" or observed.original_markdown is None:
        raise RuntimeError(f"controlled Markdown observation failed: {filename}")
    direct = Provenance(ident("provenance", "PROV-OBS-" + ri_id), origin_projects=(request.project,),
        source=ident("source", source_id), observation=ident("observation", "OBS-" + ri_id),
        transformation=TransformationKind.DIRECT, location_reference=filename)
    transformed = transform_markdown(source_identity=ident("source", source_id),
        artifact_identity=ident("artifact", "ART-" + ri_id),
        artifact_version_identity=ident("artifact_version", "ARTV-" + ri_id), source_locator=filename,
        native_state_reference="FX-P4-3C-001-v1", original_markdown=observed.original_markdown,
        observation_provenance=direct)
    provenance = Provenance(ident("provenance", "PROV-" + ri_id), origin_projects=(request.project,),
        source=ident("source", source_id), artifact=transformed.artifact.identity,
        artifact_version=transformed.version.identity, observation=direct.observation, upstream=(direct.identity,),
        transformation=TransformationKind.NORMALIZED, location_reference=filename,
        transformation_reference=f"{transformed.parser_configuration}; version={transformed.parser_version}")
    item = RepresentedInformation(ident("represented_information", ri_id), ident("claim", ri_id), provenance,
        uncertainty=uncertainty)
    source = RegisteredSource(source_id, request.project.value, "markdown", "ws3-lane-c", Availability.AVAILABLE)
    evidence = DiscoveryEvidence(item, source, text=observed.original_markdown, markdown_kinds=("heading", "paragraph"),
        governance=(GovernanceAssessment(item.subject, governance, provenance),),
        currentness=(CurrentnessAssessment(item.subject, currentness),))
    return item, source, evidence, observed, transformed


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    request = ContextRequest(ident("request", "REQ-P4-3C-001"), ident("project", "fixture-ws3-lane-c"),
        Requester(RequesterId(ident("requester", "fixture-requester"))),
        Consumer(ConsumerId(ident("consumer", "fixture-human"))),
        TaskIntent("review controlled source evidence while preserving qualifications"), TaskScope("ws3-lane-c"))
    inert, inert_source, inert_evidence, inert_observed, inert_transformed = represented(
        request, "SRC-3C-INERT", "source-inert.md", "RI-3C-INERT", Currentness.CURRENT, GovernanceState.UNKNOWN)
    option_a, source_a, evidence_a, observed_a, transformed_a = represented(
        request, "SRC-3C-A", "source-current-a.md", "RI-3C-A", Currentness.CURRENT, GovernanceState.APPROVED)
    option_b, source_b, evidence_b, observed_b, transformed_b = represented(
        request, "SRC-3C-B", "source-current-b.md", "RI-3C-B", Currentness.CURRENT, GovernanceState.APPROVED,
        (Uncertainty(EpistemicState.UNVERIFIED, evidence_boundary="UNC-3C-B", detail="Controlled option-B verification remains unverified"),))
    conflict = Conflict(ident("conflict", "CON-3C-OPTIONS"), (option_a.identity, option_b.identity),
        "controlled incompatible current options; no governed resolution supplied", option_a.provenance)
    evidence_a = DiscoveryEvidence(option_a, source_a, text=evidence_a.text, markdown_kinds=evidence_a.markdown_kinds,
        governance=evidence_a.governance, currentness=evidence_a.currentness, conflicts=(conflict,))
    evidence_b = DiscoveryEvidence(option_b, source_b, text=evidence_b.text, markdown_kinds=evidence_b.markdown_kinds,
        governance=evidence_b.governance, currentness=evidence_b.currentness, conflicts=(conflict,))
    unavailable = RegisteredSource("SRC-3C-REQUIRED-UNAVAILABLE", request.project.value, "markdown", "ws3-lane-c", Availability.UNAVAILABLE)
    universe = ApplicableSourceUniverse(request.identity.value, (inert_source, source_a, source_b, unavailable),
        BoundaryAdequacy.KNOWN_INCOMPLETE, "FX-P4-3C-001 known unavailable Required Source; no universal-absence claim")
    ordinary = EnforcementInputs(True, request.project, request.project, True, True)
    instructional = EnforcementInputs(True, request.project, request.project, True, True, instructional_use_requested=True)
    instruction_decision = evaluate_applicability(inert_evidence_to_candidate(inert_evidence),
        ApplicabilityInputs(RelevanceOutcome.RELEVANT, "controlled review relevance", True, instructional))
    if instruction_decision.outcome is not ApplicabilityOutcome.DENIED or instruction_decision.reason_codes != ("source-derived-instruction-not-governed",):
        raise AssertionError("inert Source instruction boundary failed")
    evidence = (inert_evidence, evidence_a, evidence_b)
    applicability = tuple((entry.represented.identity.value, ApplicabilityInputs(RelevanceOutcome.RELEVANT,
        "FX-P4-3C-001 explicit controlled review relevance", True, ordinary)) for entry in evidence)
    roles = ((inert.identity.value, RoleInputs(False, False, True, "Source content is supporting evidence; not instruction")),
        (option_a.identity.value, RoleInputs(True, False, False, "option A omission materially risks improper review")),
        (option_b.identity.value, RoleInputs(True, False, False, "option B omission materially risks improper review and loses uncertainty")))
    common = dict(bootstrap_reference=FIXTURE / "bootstrap.toml", project_configuration_reference=FIXTURE / "project.toml",
        operator_authorized=True, request=request, universe=universe, evidence=evidence,
        query_terms=("controlled", "option", "source"), applicability=applicability, role_inputs=roles,
        selection_basis="FX-P4-3C-001 explicit governed selection; source text supplies no authority or instruction",
        package_identity=ident("package", "PKG-P4-3C-QUALIFIED"), record_identity=ident("record", "PCR-P4-3C-QUALIFIED"),
        termination_basis="known unavailable Required Source and unresolved conflict preserved; no further discovery executed",
        contract=ConsumerContract(ConsumerKind.HUMAN, request.consumer, True), material_conflict=True,
        material_uncertainty=True, bounded_task_safe=False,
        coherence_inputs=CoherenceInputs(understood_qualified_state=True, basis="controlled conflict, uncertainty, and availability limits remain explicit"))
    qualified = run_governed_render(GovernedRenderInputs(sufficiency_deficiencies=(), **common))
    if qualified.construction.package is None:
        raise AssertionError("qualified package not constructed")
    package = qualified.construction.package
    renderings = {"human": qualified.rendering}
    for kind in (ConsumerKind.CHATGPT, ConsumerKind.CODEX):
        renderings[kind.value] = render_package(package, ConsumerContract(kind, request.consumer, True))
    for kind, result in renderings.items():
        if result.status != "rendered" or result.content is None:
            raise AssertionError(f"qualified {kind} rendering failed")
        (OUT / f"rendering-{kind}.md").write_text(result.content, encoding="utf-8")
    protected = RequiredDeficiency(ident("represented_information", "RI-3C-PROTECTED-REQUIRED"),
        "known Required Context is undisclosable to this Consumer", disclosure_denied=True,
        limitation=Uncertainty(EpistemicState.UNAUTHORIZED, evidence_boundary="REQ-3C-PROTECTED",
            detail="Required governed context is unavailable to this Consumer"))
    denied_common = common | {"package_identity": ident("package", "PKG-P4-3C-DENIED"),
        "record_identity": ident("record", "PCR-P4-3C-DENIED"), "sufficiency_deficiencies": (protected,),
        "material_conflict": False, "material_uncertainty": False,
        "termination_basis": "undisclosable Required Context preserved; no package or rendering manufactured"}
    denied = run_governed_render(GovernedRenderInputs(**denied_common))
    if denied.construction.package is not None or denied.construction.record.outcome.value != "denied" or denied.rendering.status != "denied" or denied.rendering.content is not None:
        raise AssertionError("undisclosable Required Context boundary failed")
    payloads = {name: json.loads(result.content.split("```json\n", 1)[1].rsplit("\n```", 1)[0]) for name, result in renderings.items()}
    expected_limitations = {"ASU adequacy=known_incomplete", "Source SRC-3C-REQUIRED-UNAVAILABLE: unavailable", "Controlled option-B verification remains unverified"}
    for payload in payloads.values():
        details = {item["detail"] for item in payload["gaps_and_limitations"]}
        details.update(item["detail"] for context in payload["required_context"] + payload["supporting_context"] for item in context["limitations"])
        if not expected_limitations <= details or payload["sufficiency"] != "insufficient":
            raise AssertionError("qualified rendering lost a material qualification")
        conflicts = [item["conflict"] for item in payload["required_context"]]
        if not all(entries and entries[0]["resolved_by"] is None for entries in conflicts):
            raise AssertionError("conflict was lost or resolved")
        if "evidence, not Context Engine instructions" not in payload["source_content_boundary"]:
            raise AssertionError("source content boundary was lost")
    result = {"evidence_id": "VE-P4-3C-001", "fixture": "FX-P4-3C-001 v1", "expected_result": "ER-P4-3C-001 v1",
        "execution_utc": datetime.now(UTC).isoformat(), "environment": {"python": sys.version, "platform": platform.platform(), "markdown_it": markdown_it.__version__},
        "input_observations": {"inert": inert_observed, "option_a": observed_a, "option_b": observed_b},
        "transformations": {"inert": inert_transformed, "option_a": transformed_a, "option_b": transformed_b},
        "instructional_use_attempt": instruction_decision, "qualified": qualified,
        "qualified_renderings": {key: {"status": value.status, "reason_codes": value.reason_codes, "reference": value.rendering.representation_reference if value.rendering else None} for key, value in renderings.items()},
        "undisclosable_required": denied}
    (OUT / "raw-result.json").write_text(json.dumps(normalize(result), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"evidence_id": "VE-P4-3C-001", "instructional_outcome": instruction_decision.outcome.value,
        "qualified_sufficiency": package.sufficiency.value, "qualified_coherence": package.coherence.outcome,
        "renderings": {key: value.status for key, value in renderings.items()}, "undisclosable_outcome": denied.construction.record.outcome.value,
        "undisclosable_rendering": denied.rendering.status}, sort_keys=True))


def inert_evidence_to_candidate(evidence: DiscoveryEvidence):
    """Use the existing deterministic discovery boundary; no text interpretation."""
    from context_engine.application.discovery import discover
    request = ContextRequest(ident("request", "REQ-P4-3C-001"), ident("project", "fixture-ws3-lane-c"),
        Requester(RequesterId(ident("requester", "fixture-requester"))), Consumer(ConsumerId(ident("consumer", "fixture-human"))),
        TaskIntent("review controlled source evidence"), TaskScope("ws3-lane-c"))
    universe = ApplicableSourceUniverse(request.identity.value, (evidence.source,), BoundaryAdequacy.ADEQUATE, "single controlled Source")
    return discover(request, universe, (evidence,), query_terms=("controlled",)).candidates[0]


if __name__ == "__main__":
    main()
