"""Controlled governed-decision tests for Workstream 7."""
from __future__ import annotations

from context_engine.application.decision_pipeline import (
    ApplicabilityInputs, ApplicabilityOutcome, EnforcementInputs, RelevanceOutcome,
    RoleInputs, evaluate_applicability, select_candidate,
)
from context_engine.core.model import (
    Authority, AuthorityScope, CandidateContext, Classification, Conflict,
    ContextRequest, ContextRole, Currentness, CurrentnessAssessment,
    GovernanceAssessment, GovernanceState, Provenance, RepresentedInformation,
    Requester, Consumer, SemanticIdentity, TaskIntent, TaskScope, Uncertainty,
    EpistemicState,
)


def ident(kind: str, value: str) -> SemanticIdentity:
    return SemanticIdentity(kind, value)


def request() -> ContextRequest:
    return ContextRequest(ident("request", "request-7"), ident("project", "project-a"), Requester(ident("requester", "r")), Consumer(ident("consumer", "c")), TaskIntent("review"), TaskScope("component"))


def candidate(*, authority: bool = True, governance: GovernanceState = GovernanceState.APPROVED, currentness: Currentness = Currentness.CURRENT, conflict: bool = False, limitations: tuple[Uncertainty, ...] = ()) -> CandidateContext:
    provenance = Provenance(ident("provenance", "p"), origin_projects=(ident("project", "project-a"),), source=ident("source", "source-a"))
    represented = RepresentedInformation(ident("represented_information", "item"), ident("claim", "claim-a"), provenance, (Classification("Decision"),), limitations)
    authorities = (Authority(ident("authority", "owner"), "governed owner basis", AuthorityScope(project=ident("project", "project-a"), domains=("architecture",), phases=("phase-3",), actions=("review",)), provenance),) if authority else ()
    conflicts = (Conflict(ident("conflict", "c"), (ident("claim", "claim-a"), ident("claim", "claim-b")), "component", provenance),) if conflict else ()
    return CandidateContext(request().identity, represented, "deterministic:literal", "docs", authorities=authorities, governance=(GovernanceAssessment(represented.subject, governance, provenance),), currentness=(CurrentnessAssessment(represented.subject, currentness),), conflicts=conflicts, limitations=limitations)


def enforcement(**changes: object) -> EnforcementInputs:
    values: dict[str, object] = dict(
        bootstrap_valid=True, request_project=ident("project", "project-a"), candidate_project=ident("project", "project-a"),
        requester_authorized=True, consumer_disclosure_authorized=True,
        task_domain="architecture", task_phase="phase-3", task_action="review",
    )
    values.update(changes)
    return EnforcementInputs(**values)  # type: ignore[arg-type]


def applicable_inputs(**changes: object) -> ApplicabilityInputs:
    values: dict[str, object] = dict(relevance=RelevanceOutcome.RELEVANT, relevance_basis="explicit task/component mapping", scope_matches_task=True, enforcement=enforcement())
    values.update(changes)
    return ApplicabilityInputs(**values)  # type: ignore[arg-type]


def required_inputs(**changes: object) -> RoleInputs:
    values: dict[str, object] = dict(omission_risks_incorrect_performance=True, omission_risks_improper_performance=False, materially_improves_understanding_or_validation=True, basis="explicit omission analysis")
    values.update(changes)
    return RoleInputs(**values)  # type: ignore[arg-type]


def test_discovery_is_not_applicability_and_explicit_relevance_is_required() -> None:
    found = candidate()
    unknown = evaluate_applicability(found, applicable_inputs(relevance=RelevanceOutcome.UNKNOWN, relevance_basis=""))
    ranked = evaluate_applicability(found, applicable_inputs(relevance=RelevanceOutcome.NOT_RELEVANT))
    assert unknown.outcome is ApplicabilityOutcome.UNRESOLVED
    assert ranked.outcome is ApplicabilityOutcome.INAPPLICABLE
    assert "ranking" not in " ".join(unknown.reason_codes)


def test_scoped_authority_and_governance_state_are_independent() -> None:
    no_authority = evaluate_applicability(candidate(authority=False), applicable_inputs(enforcement=enforcement(requires_governing_authority=True)))
    proposal = evaluate_applicability(candidate(governance=GovernanceState.PROPOSED), applicable_inputs(enforcement=enforcement(requires_governing_authority=True)))
    ordinary_proposal = evaluate_applicability(candidate(governance=GovernanceState.PROPOSED), applicable_inputs())
    assert no_authority.outcome is ApplicabilityOutcome.UNRESOLVED
    assert proposal.outcome is ApplicabilityOutcome.UNRESOLVED
    assert ordinary_proposal.outcome is ApplicabilityOutcome.APPLICABLE


def test_currentness_and_history_are_task_qualified_not_recency() -> None:
    current = evaluate_applicability(candidate(currentness=Currentness.CURRENT), applicable_inputs(enforcement=enforcement(task_requires_current=True)))
    historical = evaluate_applicability(candidate(currentness=Currentness.HISTORICAL), applicable_inputs(enforcement=enforcement(task_requires_current=True)))
    unknown = evaluate_applicability(candidate(currentness=Currentness.UNKNOWN), applicable_inputs(enforcement=enforcement(task_requires_current=True)))
    history_task = evaluate_applicability(candidate(currentness=Currentness.HISTORICAL), applicable_inputs(enforcement=enforcement(task_is_historical=True)))
    assert current.outcome is ApplicabilityOutcome.APPLICABLE
    assert historical.outcome is ApplicabilityOutcome.INAPPLICABLE
    assert unknown.outcome is ApplicabilityOutcome.UNRESOLVED
    assert history_task.outcome is ApplicabilityOutcome.APPLICABLE


def test_authorization_and_protected_metadata_fail_closed_separately() -> None:
    item = candidate()
    for change, code in (({"bootstrap_valid": False}, "bootstrap-invalid-or-unavailable"), ({"requester_authorized": None}, "requester-authorization-not-established"), ({"consumer_disclosure_authorized": False}, "consumer-disclosure-authorization-not-established"), ({"protected_metadata_authorized": False}, "protected-metadata-authorization-not-established")):
        result = evaluate_applicability(item, applicable_inputs(enforcement=enforcement(**change)))
        assert result.outcome is ApplicabilityOutcome.DENIED and result.reason_codes == (code,)


def test_unknown_governance_and_unavailable_protected_required_context_do_not_be_selected() -> None:
    governance_unknown = evaluate_applicability(candidate(governance=GovernanceState.UNKNOWN), applicable_inputs(enforcement=enforcement(requires_governing_authority=True)))
    protected_unavailable = evaluate_applicability(candidate(limitations=(Uncertainty(EpistemicState.UNAVAILABLE, detail="protected required evidence unavailable"),)), applicable_inputs(enforcement=enforcement(protected_metadata_authorized=None)))
    assert governance_unknown.outcome is ApplicabilityOutcome.UNRESOLVED
    assert protected_unavailable.outcome is ApplicabilityOutcome.DENIED
    assert select_candidate(protected_unavailable, required_inputs(), selection_basis="selection").selected is None


def test_project_isolation_and_cross_project_prerequisites_are_enforced() -> None:
    external = enforcement(candidate_project=ident("project", "project-b"))
    denied = evaluate_applicability(candidate(), applicable_inputs(enforcement=external))
    allowed = evaluate_applicability(candidate(), applicable_inputs(enforcement=enforcement(candidate_project=ident("project", "project-b"), cross_project_prerequisites=True)))
    assert denied.outcome is ApplicabilityOutcome.DENIED
    assert allowed.outcome is ApplicabilityOutcome.APPLICABLE


def test_source_derived_instruction_is_inert_without_governed_instructional_basis() -> None:
    item = candidate()
    denied = evaluate_applicability(item, applicable_inputs(enforcement=enforcement(instructional_use_requested=True)))
    allowed = evaluate_applicability(item, applicable_inputs(enforcement=enforcement(instructional_use_requested=True, instructional_authority_established=True, requires_governing_authority=True)))
    assert denied.outcome is ApplicabilityOutcome.DENIED
    assert allowed.outcome is ApplicabilityOutcome.APPLICABLE


def test_selection_requires_applicability_and_explicit_counterfactual_basis() -> None:
    unresolved = evaluate_applicability(candidate(), applicable_inputs(relevance=RelevanceOutcome.UNKNOWN, relevance_basis=""))
    assert select_candidate(unresolved, required_inputs(), selection_basis="selection").selected is None
    decision = evaluate_applicability(candidate(), applicable_inputs())
    no_role = select_candidate(decision, required_inputs(omission_risks_incorrect_performance=False, materially_improves_understanding_or_validation=False), selection_basis="selection")
    assert no_role.selected is None
    selected = select_candidate(decision, required_inputs(), selection_basis="governed explicit selection")
    assert selected.selected is not None and selected.selected.role is ContextRole.REQUIRED
    assert selected.selected.represented.provenance.identity.value == "p"


def test_required_and_supporting_do_not_depend_on_capacity_rendering_or_repetition() -> None:
    decision = evaluate_applicability(candidate(), applicable_inputs())
    required = select_candidate(decision, required_inputs(consumer_capacity_limited=True, rendering_limited=True), selection_basis="selection")
    supporting = select_candidate(decision, required_inputs(omission_risks_incorrect_performance=False, materially_improves_understanding_or_validation=True), selection_basis="selection")
    assert required.role is ContextRole.REQUIRED
    assert "consumer-capacity-does-not-waive-required" in required.reason_codes
    assert "rendering-limitation-does-not-waive-required" in required.reason_codes
    assert supporting.role is ContextRole.SUPPORTING


def test_conflict_uncertainty_and_selection_sufficiency_boundary_are_preserved() -> None:
    limitation = Uncertainty(EpistemicState.UNKNOWN, detail="local history bounded")
    decision = evaluate_applicability(candidate(conflict=True, limitations=(limitation,)), applicable_inputs())
    selected = select_candidate(decision, required_inputs(), selection_basis="selection")
    assert "conflict-preserved" in selected.reason_codes
    assert selected.qualifications == (limitation,)
    assert selected.selected is not None
    assert not hasattr(selected, "sufficiency") and not hasattr(selected.selected, "sufficiency")


def test_parser_ranking_recency_and_repetition_cannot_select_or_create_authority() -> None:
    item = candidate(authority=False, governance=GovernanceState.PROPOSED, currentness=Currentness.HISTORICAL)
    denied_governing = evaluate_applicability(item, applicable_inputs(enforcement=enforcement(requires_governing_authority=True, task_requires_current=True)))
    assert denied_governing.outcome is ApplicabilityOutcome.INAPPLICABLE
    ordinary = evaluate_applicability(item, applicable_inputs())
    selected = select_candidate(ordinary, required_inputs(), selection_basis="selection")
    assert selected.selected is not None
    assert not item.authorities and not selected.selected.represented.provenance.upstream


def test_repeated_authority_evidence_does_not_multiply_authority_or_selection_role() -> None:
    item = candidate()
    repeated = CandidateContext(item.request, item.represented, item.discovery_basis, item.source_scope, authorities=item.authorities * 2, governance=item.governance)
    decision = evaluate_applicability(repeated, applicable_inputs(enforcement=enforcement(requires_governing_authority=True)))
    selected = select_candidate(decision, required_inputs(), selection_basis="selection")
    assert decision.outcome is ApplicabilityOutcome.APPLICABLE
    assert selected.role is ContextRole.REQUIRED
    assert selected.selected is not None and selected.selected.represented is repeated.represented
