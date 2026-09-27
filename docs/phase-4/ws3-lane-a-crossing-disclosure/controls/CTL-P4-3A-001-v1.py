"""Frozen Lane A crossing/disclosure control; execute once with a fresh output directory."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from context_engine.application.decision_pipeline import ApplicabilityInputs, EnforcementInputs, RelevanceOutcome, evaluate_applicability
from context_engine.application.lifecycle import RegisteredSource, ScopeInputs, effective_sources
from context_engine.application.rendering import ConsumerContract, ConsumerKind, render_package
from context_engine.core.model import (CandidateContext, Consumer, ConsumerId, ContextItem, ContextPackage, ContextRequest, ContextRole, ConstructionState, GovernanceAssessment, GovernanceState, Provenance, RepresentedInformation, Requester, RequesterId, SemanticIdentity, SourceManifest, SourceManifestEntry, SufficiencyOutcome, TaskIntent, TaskScope)


def ident(kind: str, value: str) -> SemanticIdentity:
    return SemanticIdentity(kind, value)


ATLAS = ident("project", "project-lane-a-atlas")
BEACON = ident("project", "project-lane-a-beacon")
REQUEST = ContextRequest(ident("request", "REQ-3A"), ATLAS, Requester(RequesterId(ident("requester", "REQ-3A-REQUESTER"))), Consumer(ConsumerId(ident("consumer", "REQ-3A-CONSUMER"))), TaskIntent("bounded external compatibility"), TaskScope("one governed external relationship"))
LOCAL = RegisteredSource("SRC-3A-ATLAS", ATLAS.value, "synthetic", "controlled")
EXTERNAL = RegisteredSource("SRC-3A-BEACON", BEACON.value, "synthetic", "controlled")


def external_candidate() -> CandidateContext:
    provenance = Provenance(ident("provenance", "PROV-3A-BEACON"), origin_projects=(BEACON,), source=ident("source", "SRC-3A-BEACON"))
    represented = RepresentedInformation(ident("represented_information", "RI-3A-BEACON"), ident("claim", "CLM-3A-BEACON"), provenance)
    return CandidateContext(REQUEST.identity, represented, "controlled:relationship-hop", "controlled", governance=(GovernanceAssessment(represented.subject, GovernanceState.APPROVED, provenance),))


def applicability(*, requester: bool = True, disclosure: bool = True, crossing: bool = False) -> dict[str, object]:
    result = evaluate_applicability(external_candidate(), ApplicabilityInputs(RelevanceOutcome.RELEVANT, "pre-established controlled task relationship", True, EnforcementInputs(True, ATLAS, BEACON, requester, disclosure, cross_project_prerequisites=crossing)))
    return {"outcome": result.outcome.value, "reasons": list(result.reason_codes), "origin_projects": [value.value for value in result.candidate.represented.provenance.origin_projects]}


def denied_render() -> dict[str, object]:
    candidate = external_candidate()
    item = ContextItem.select(candidate, basis="controlled required compatibility basis", role=ContextRole.REQUIRED)
    package = ContextPackage(ident("package", "PKG-3A-PROTECTED"), REQUEST.identity, (item,), SourceManifest((SourceManifestEntry(ident("source", "SRC-3A-BEACON"), contributed=True),)), SufficiencyOutcome.SUFFICIENT, ConstructionState("coherent", "controlled"))
    result = render_package(package, ConsumerContract(ConsumerKind.HUMAN, REQUEST.consumer, False))
    return {"status": result.status, "content_is_none": result.content is None, "rendering_is_none": result.rendering is None, "reasons": list(result.reason_codes)}


def main(output: Path) -> None:
    cases = {
        "default": ScopeInputs(),
        "missing_task": ScopeInputs(governed_relationship=True, requester_authorized=True, consumer_disclosure_authorized=True),
        "missing_relationship": ScopeInputs(task_requires_external=True, requester_authorized=True, consumer_disclosure_authorized=True),
        "missing_requester": ScopeInputs(task_requires_external=True, governed_relationship=True, consumer_disclosure_authorized=True),
        "missing_disclosure": ScopeInputs(task_requires_external=True, governed_relationship=True, requester_authorized=True),
        "all_prerequisites": ScopeInputs(True, True, True, True),
    }
    scopes = {name: [source.identity for source in effective_sources(ATLAS.value, (LOCAL, EXTERNAL), inputs)] for name, inputs in cases.items()}
    result = {"scope_cases": scopes, "crossing_denied": applicability(), "crossing_allowed": applicability(crossing=True), "requester_denied": applicability(requester=False, crossing=True), "consumer_denied": applicability(disclosure=False, crossing=True), "disclosure_denied_render": denied_render()}
    assert all(value == ["SRC-3A-ATLAS"] for name, value in scopes.items() if name != "all_prerequisites")
    assert scopes["all_prerequisites"] == ["SRC-3A-ATLAS", "SRC-3A-BEACON"]
    assert result["crossing_denied"]["outcome"] == "denied" and result["crossing_denied"]["reasons"] == ["cross-project-prerequisites-not-established"]
    assert result["crossing_allowed"]["outcome"] == "applicable" and result["crossing_allowed"]["origin_projects"] == ["project-lane-a-beacon"]
    assert result["requester_denied"]["reasons"] == ["requester-authorization-not-established"]
    assert result["consumer_denied"]["reasons"] == ["consumer-disclosure-authorization-not-established"]
    render = result["disclosure_denied_render"]
    assert render["status"] == "denied" and render["content_is_none"] and render["rendering_is_none"]
    assert "PKG-3A-PROTECTED" not in " ".join(render["reasons"])
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
