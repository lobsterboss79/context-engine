"""Execution-only procedure for frozen FX-F6-EF v1 / ER-F6-EF v1."""
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
from context_engine.application.discovery import DiscoveryEvidence, ExpansionRequest, discover
from context_engine.application.lifecycle import ApplicableSourceUniverse, Availability, BoundaryAdequacy, RegisteredSource
from context_engine.application.package_construction import CoherenceInputs, construct_logical_package, evaluate_coherence
from context_engine.application.rendering import ConsumerContract, ConsumerKind, render_package
from context_engine.application.representation import observe_markdown_artifact, transform_markdown
from context_engine.application.sufficiency import DiscoveryDeficiency, SufficiencyInputs, evaluate_sufficiency, plan_bounded_iteration
from context_engine.core.model import Consumer, ConsumerId, ContextRequest, Provenance, Relationship, RepresentedInformation, Requester, RequesterId, SemanticIdentity, TaskIntent, TaskScope, TransformationKind, Uncertainty, EpistemicState


ROOT = Path.cwd()
FIXTURE = ROOT / "docs/phase-4/ws2-item-2.6-fixtures/F6-EF"
OUT = ROOT / "docs/phase-4/validation-evidence/VE-F6-EF-001/raw"
QUERY = "CE-F6EF-ABSENT-IDENTIFIER-7Q3M"


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


def observe(source: RegisteredSource, relative_path: str, request: ContextRequest, represented_identity: str, *, relationship: Relationship | None = None, expansion_only: bool = False):
    git = LocalGitSourceAdapter().observe(source, inspection_authorized=True)
    markdown = observe_markdown_artifact(FIXTURE, relative_path)
    if markdown.outcome != "observed" or markdown.original_markdown is None:
        raise RuntimeError(f"normal local Markdown observation failed for {source.identity}")
    direct = Provenance(ident("provenance", f"PROV-OBS-{source.identity}"), origin_projects=(request.project,), source=ident("source", source.identity), observation=ident("observation", f"OBS-{source.identity}"), transformation=TransformationKind.DIRECT, location_reference=relative_path)
    transformed = transform_markdown(source_identity=ident("source", source.identity), artifact_identity=ident("artifact", f"ART-{source.identity}"), artifact_version_identity=ident("artifact_version", f"ARTV-{source.identity}"), source_locator=relative_path, native_state_reference=git.head, original_markdown=markdown.original_markdown, observation_provenance=direct)
    provenance = Provenance(ident("provenance", f"PROV-{source.identity}"), origin_projects=(request.project,), source=ident("source", source.identity), artifact=transformed.artifact.identity, artifact_version=transformed.version.identity, observation=ident("observation", f"OBS-{source.identity}"), upstream=(direct.identity,), transformation=TransformationKind.NORMALIZED, location_reference=relative_path, transformation_reference=f"{transformed.parser_configuration}; version={transformed.parser_version}")
    represented = RepresentedInformation(ident("represented_information", represented_identity), ident("claim", represented_identity), provenance)
    evidence = DiscoveryEvidence(represented=represented, source=source, text=markdown.original_markdown, markdown_kinds=("heading", "paragraph", "list"), relationships=(() if relationship is None else (relationship,)), expansion_only=expansion_only)
    return evidence, {"source": source.identity, "git": git, "markdown": markdown, "transformation": transformed, "represented_information": represented}


def main() -> None:
    request = ContextRequest(ident("request", "REQ-F6EF-HARBOR-SCOPED-IDENTIFIER-REPORT"), ident("project", "fixture-harbor-f6ef"), Requester(RequesterId(ident("requester", "fixture-requester"))), Consumer(ConsumerId(ident("consumer", "fixture-human"))), TaskIntent("report whether the exact controlled identifier is present within the governed inspected ASU after the authorized bounded expansion"), TaskScope("bounded reporting only; governed inspected ASU"))
    origin = RegisteredSource("SRC-F6EF-HARBOR-ORIGIN", "fixture-harbor-f6ef", "git", "harbor/controlled-register/origin", Availability.AVAILABLE, str(ROOT))
    target = RegisteredSource("SRC-F6EF-HARBOR-EXPANSION-TARGET", "fixture-harbor-f6ef", "git", "harbor/controlled-register/annex", Availability.AVAILABLE, str(ROOT))
    asu_basis = "For REQ-F6EF-HARBOR-SCOPED-IDENTIFIER-REPORT, the governed Source universe is complete and consists exactly of SRC-F6EF-HARBOR-ORIGIN and SRC-F6EF-HARBOR-EXPANSION-TARGET. Both are local, available, accessible, authorized, supported, and governed in scope. The task is only to report the exact-literal result within this governed inspected ASU after its pre-authorized one-hop inspection path; no Source outside these two belongs to that bounded reporting task."
    universe = ApplicableSourceUniverse(request.identity.value, (origin, target), BoundaryAdequacy.ADEQUATE, asu_basis)
    relationship = Relationship(ident("relationship", "REL-F6EF-HARBOR-ORIGIN-TO-ANNEX"), "governed-controlled-annex", ident("represented_information", "RI-F6EF-HARBOR-ORIGIN-REGISTER"), ident("source", target.identity))
    deficiency = DiscoveryDeficiency(ident("deficiency", "DEF-F6EF-INITIAL-EXACT-QUERY-ABSENCE"), "Initial inspection of SRC-F6EF-HARBOR-ORIGIN found no exact literal match for the controlled query. For the bounded reporting task, this is material and potentially resolvable because the one represented governed relationship identifies one already-governed, available expansion-only Source for inspection.", material=True, resolvable_by_discovery=True, authorized=True, in_scope=True, source_ids=(target.identity,))
    expansion = ExpansionRequest(origin=ident("represented_information", "RI-F6EF-HARBOR-ORIGIN-REGISTER"), relationship=relationship.identity, target_source=target.identity, material_resolvable_deficiency=True, inspection_authorized=True, basis="DEF-F6EF-INITIAL-EXACT-QUERY-ABSENCE; authorized one-hop inspection of the sole represented governed annex target.")
    origin_evidence, origin_observation = observe(origin, "sources/origin-register.md", request, "RI-F6EF-HARBOR-ORIGIN-REGISTER", relationship=relationship)
    initial_discovery = discover(request, universe, (origin_evidence,), query_terms=(QUERY,))
    if initial_discovery.candidates:
        raise RuntimeError("initial exact-query inspection unexpectedly found a Candidate")
    iteration_plan = plan_bounded_iteration(universe, deficiency)
    if not iteration_plan.authorized_to_discover or iteration_plan.additional_sources != (target.identity,):
        raise RuntimeError("frozen bounded iteration plan was not authorized as expected")
    target_evidence, target_observation = observe(target, "sources/expansion-target-annex.md", request, "RI-F6EF-HARBOR-EXPANSION-TARGET-ANNEX", expansion_only=True)
    discovery = discover(request, universe, (origin_evidence, target_evidence), query_terms=(QUERY,), expansions=(expansion,))
    if discovery.candidates:
        raise RuntimeError("final exact-query inspection unexpectedly found a Candidate")
    sufficiency = evaluate_sufficiency(SufficiencyInputs(selected=(), universe=universe, required_deficiencies=(), material_conflict=False, material_uncertainty=False, bounded_task_safe=True))
    qualifications = (
        Uncertainty(EpistemicState.UNKNOWN, evidence_boundary=asu_basis, detail="FX-F6-EF bounded reporting task: exact query CE-F6EF-ABSENT-IDENTIFIER-7Q3M; ASU-F6EF-HARBOR-SCOPED-REPORT is adequate and contains exactly the two governed Sources."),
        Uncertainty(EpistemicState.UNKNOWN, evidence_boundary=asu_basis, detail="Initial inspected Sources: SRC-F6EF-HARBOR-ORIGIN only. Its normalized represented information is RI-F6EF-HARBOR-ORIGIN-REGISTER and preserves relationship REL-F6EF-HARBOR-ORIGIN-TO-ANNEX."),
        Uncertainty(EpistemicState.UNKNOWN, evidence_boundary=asu_basis, detail="Initial deficiency DEF-F6EF-INITIAL-EXACT-QUERY-ABSENCE was material and potentially resolvable. Pre-frozen EXP-F6EF-HARBOR-ONE-HOP authorized one governed one-hop expansion to SRC-F6EF-HARBOR-EXPANSION-TARGET."),
        Uncertainty(EpistemicState.UNKNOWN, evidence_boundary=asu_basis, detail="Expanded inspected Sources: SRC-F6EF-HARBOR-EXPANSION-TARGET only; effective inspected Sources: SRC-F6EF-HARBOR-ORIGIN, SRC-F6EF-HARBOR-EXPANSION-TARGET."),
        Uncertainty(EpistemicState.UNKNOWN, evidence_boundary=asu_basis, detail="Zero exact matching Candidates were found. This is no-result evidence, not Candidate inapplicability or exclusion."),
        Uncertainty(EpistemicState.UNKNOWN, evidence_boundary=asu_basis, detail="Not found within the governed inspected ASU. This is not a universal-absence assertion and does not decide whether information exists outside that boundary."),
        Uncertainty(EpistemicState.UNKNOWN, evidence_boundary=asu_basis, detail="Termination: origin inspected; sole authorized one-hop target inspected; no exact match in either; sole approved path exhausted; no second hop or crawl authorized. Sufficient only for this bounded reporting task."),
    )
    termination = "Initial inspection of SRC-F6EF-HARBOR-ORIGIN completed; one authorized governed expansion inspected SRC-F6EF-HARBOR-EXPANSION-TARGET; no exact literal match in either Source; no second hop is authorized; the sole approved expansion path is exhausted."
    construction = construct_logical_package(package_identity=ident("package", "PKG-F6EF-HARBOR-SCOPED-IDENTIFIER-REPORT"), request=request.identity, selected=(), candidates=discovery.candidates, universe=universe, sufficiency=sufficiency, coherence=evaluate_coherence(CoherenceInputs(basis="The bounded reporting task, adequate ASU, initial-only origin inspection, authorized one-hop expansion, final two-Source inspected set, zero exact matches, scoped negative result, Sufficient reporting outcome, and termination basis are retained without contradiction.")), record_identity=ident("record", "PCR-F6EF-HARBOR-SCOPED-IDENTIFIER-REPORT"), termination_basis=termination, construction_qualifications=qualifications)
    if construction.package is None:
        raise RuntimeError("logical package construction was denied")
    renderings = {}
    for kind, consumer in ((ConsumerKind.HUMAN, "fixture-human"), (ConsumerKind.CHATGPT, "fixture-chatgpt"), (ConsumerKind.CODEX, "fixture-codex")):
        rendering = render_package(construction.package, ConsumerContract(kind=kind, consumer=Consumer(ConsumerId(ident("consumer", consumer))), disclosure_authorized=True))
        renderings[kind.value] = rendering
        (OUT / f"rendering-{kind.value}.md").write_text(rendering.content or "", encoding="utf-8")
    result = {"evidence_id": "VE-F6-EF-001", "fixture": "FX-F6-EF v1", "expected_result": "ER-F6-EF v1", "execution_utc": datetime.now(UTC).isoformat(), "environment": {"python": sys.version, "platform": platform.platform(), "markdown_it": markdown_it.__version__}, "request": request, "asu": {"identity": "ASU-F6EF-HARBOR-SCOPED-REPORT", "adequacy": universe.adequacy, "basis": universe.basis}, "source_observations": [origin_observation, target_observation], "represented_relationship": relationship, "initial_discovery": initial_discovery, "deficiency": deficiency, "expansion_request": expansion, "bounded_iteration_plan": iteration_plan, "discovery": discovery, "sufficiency": sufficiency, "construction": construction, "renderings": {key: {"status": value.status, "reason_codes": value.reason_codes, "reference": value.rendering.representation_reference if value.rendering else None} for key, value in renderings.items()}}
    (OUT / "raw-result.json").write_text(json.dumps(normalize(result), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(normalize({"evidence_id": "VE-F6-EF-001", "initial_inspected": initial_discovery.initial_inspected_sources, "expanded_inspected": discovery.expanded_inspected_sources, "candidates": len(discovery.candidates), "sufficiency": construction.package.sufficiency, "coherence": construction.package.coherence.outcome, "renderings": {key: value.status for key, value in renderings.items()}}), sort_keys=True))


if __name__ == "__main__":
    main()
