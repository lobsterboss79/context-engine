"""Deterministic Workstream 7 applicability, enforcement, and selection.

Inputs are already-established governed facts.  This module does not discover
evidence, infer governance or authorization, assess sufficiency, construct a
package, render, or persist hidden reasoning.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from context_engine.core.model import (
    Authority, CandidateContext, ContextItem, ContextRole, Currentness,
    GovernanceState, SemanticIdentity, Uncertainty,
)


class ApplicabilityOutcome(str, Enum):
    APPLICABLE = "applicable"
    INAPPLICABLE = "inapplicable"
    UNRESOLVED = "unresolved"
    DENIED = "denied"


class RelevanceOutcome(str, Enum):
    RELEVANT = "relevant"
    NOT_RELEVANT = "not_relevant"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class EnforcementInputs:
    """Explicit deterministic governance/security facts for one operation."""

    bootstrap_valid: bool
    request_project: SemanticIdentity
    candidate_project: SemanticIdentity
    requester_authorized: bool | None
    consumer_disclosure_authorized: bool | None
    protected_metadata_authorized: bool | None = True
    task_requires_current: bool = False
    task_is_historical: bool = False
    task_domain: str | None = None
    task_phase: str | None = None
    task_action: str | None = None
    requires_governing_authority: bool = False
    instructional_use_requested: bool = False
    instructional_authority_established: bool = False
    cross_project_prerequisites: bool = False


@dataclass(frozen=True)
class ApplicabilityInputs:
    """Pre-established task-relative relevance and scope evidence.

    The application never derives these facts from discovery rank, parser
    tokens, repetition, recency, or untrusted source wording.
    """

    relevance: RelevanceOutcome
    relevance_basis: str
    scope_matches_task: bool | None
    enforcement: EnforcementInputs


@dataclass(frozen=True)
class ApplicabilityDecision:
    candidate: CandidateContext
    outcome: ApplicabilityOutcome
    reason_codes: tuple[str, ...]
    qualifications: tuple[Uncertainty, ...] = ()


@dataclass(frozen=True)
class RoleInputs:
    """Observable counterfactual omission evidence, not a sufficiency result."""

    omission_risks_incorrect_performance: bool
    omission_risks_improper_performance: bool
    materially_improves_understanding_or_validation: bool
    basis: str
    consumer_capacity_limited: bool = False
    rendering_limited: bool = False


@dataclass(frozen=True)
class SelectionDecision:
    applicability: ApplicabilityDecision
    selected: ContextItem | None
    role: ContextRole | None
    reason_codes: tuple[str, ...]
    qualifications: tuple[Uncertainty, ...] = ()


def evaluate_applicability(candidate: CandidateContext, inputs: ApplicabilityInputs) -> ApplicabilityDecision:
    """Evaluate one Candidate with explicit governed facts and fail closed.

    The returned decision is explainable via concise reason codes only.  It
    deliberately contains no score, Authority creation, selection, or
    sufficiency outcome.
    """
    enforcement = inputs.enforcement
    reasons: list[str] = []
    qualifications = candidate.limitations
    if not enforcement.bootstrap_valid:
        return _decision(candidate, ApplicabilityOutcome.DENIED, ("bootstrap-invalid-or-unavailable",), qualifications)
    if enforcement.requester_authorized is not True:
        return _decision(candidate, ApplicabilityOutcome.DENIED, ("requester-authorization-not-established",), qualifications)
    if enforcement.consumer_disclosure_authorized is not True:
        return _decision(candidate, ApplicabilityOutcome.DENIED, ("consumer-disclosure-authorization-not-established",), qualifications)
    if enforcement.protected_metadata_authorized is not True:
        return _decision(candidate, ApplicabilityOutcome.DENIED, ("protected-metadata-authorization-not-established",), qualifications)
    if enforcement.candidate_project != enforcement.request_project and not enforcement.cross_project_prerequisites:
        return _decision(candidate, ApplicabilityOutcome.DENIED, ("cross-project-prerequisites-not-established",), qualifications)
    if inputs.scope_matches_task is not True:
        outcome = ApplicabilityOutcome.INAPPLICABLE if inputs.scope_matches_task is False else ApplicabilityOutcome.UNRESOLVED
        return _decision(candidate, outcome, ("task-or-source-scope-not-established",), qualifications)
    if inputs.relevance is RelevanceOutcome.NOT_RELEVANT:
        return _decision(candidate, ApplicabilityOutcome.INAPPLICABLE, ("deterministic-task-relevance-not-established",), qualifications)
    if inputs.relevance is RelevanceOutcome.UNKNOWN or not inputs.relevance_basis:
        return _decision(candidate, ApplicabilityOutcome.UNRESOLVED, ("deterministic-task-relevance-unknown",), qualifications)
    temporal = _temporal_reason(candidate, enforcement)
    if temporal is not None:
        return _decision(candidate, temporal[0], (temporal[1],), qualifications)
    if enforcement.requires_governing_authority and not _has_governing_authority(candidate, enforcement):
        return _decision(candidate, ApplicabilityOutcome.UNRESOLVED, ("scoped-governing-authority-not-established",), qualifications)
    if enforcement.instructional_use_requested and not _instructional_applicability(candidate, enforcement):
        return _decision(candidate, ApplicabilityOutcome.DENIED, ("source-derived-instruction-not-governed",), qualifications)
    reasons.append("deterministic-task-relevance-established")
    if candidate.conflicts:
        reasons.append("conflict-preserved")
    if qualifications:
        reasons.append("limitations-preserved")
    return _decision(candidate, ApplicabilityOutcome.APPLICABLE, tuple(reasons), qualifications)


def select_candidate(
    decision: ApplicabilityDecision, role_inputs: RoleInputs, *, selection_basis: str,
    include: bool = True,
) -> SelectionDecision:
    """Create a selected ContextItem only from an applicable Candidate.

    This consumes explicit counterfactual-omission evidence; it does not decide
    whether the resulting selection is sufficient.
    """
    if decision.outcome is not ApplicabilityOutcome.APPLICABLE:
        return SelectionDecision(decision, None, None, ("not-selected-applicability-" + decision.outcome.value,), decision.qualifications)
    if not include:
        return SelectionDecision(decision, None, None, ("not-selected-explicit-governed-basis",), decision.qualifications)
    if not selection_basis or not role_inputs.basis:
        return SelectionDecision(decision, None, None, ("not-selected-material-basis-missing",), decision.qualifications)
    if role_inputs.omission_risks_incorrect_performance or role_inputs.omission_risks_improper_performance:
        role = ContextRole.REQUIRED
        role_reason = "counterfactual-omission-material-risk"
    elif role_inputs.materially_improves_understanding_or_validation:
        role = ContextRole.SUPPORTING
        role_reason = "counterfactual-supporting-material-benefit"
    else:
        return SelectionDecision(decision, None, None, ("not-selected-no-required-or-supporting-basis",), decision.qualifications)
    item = ContextItem.select(decision.candidate, basis=selection_basis, role=role)
    reasons = ["selected-explicit-material-basis", role_reason]
    if role is ContextRole.REQUIRED and role_inputs.consumer_capacity_limited:
        reasons.append("consumer-capacity-does-not-waive-required")
    if role is ContextRole.REQUIRED and role_inputs.rendering_limited:
        reasons.append("rendering-limitation-does-not-waive-required")
    if decision.candidate.conflicts:
        reasons.append("conflict-preserved")
    if decision.qualifications:
        reasons.append("limitations-preserved")
    return SelectionDecision(decision, item, role, tuple(reasons), decision.qualifications)


def _temporal_reason(candidate: CandidateContext, enforcement: EnforcementInputs) -> tuple[ApplicabilityOutcome, str] | None:
    values = {assessment.currentness for assessment in candidate.currentness}
    if enforcement.task_is_historical:
        return None
    if enforcement.task_requires_current:
        if Currentness.CURRENT in values:
            return None
        if Currentness.UNKNOWN in values or not values:
            return ApplicabilityOutcome.UNRESOLVED, "currentness-not-established"
        return ApplicabilityOutcome.INAPPLICABLE, "historical-or-superseded-for-current-task"
    return None


def _has_governing_authority(candidate: CandidateContext, inputs: EnforcementInputs) -> bool:
    approved_subjects = {entry.subject for entry in candidate.governance if entry.state is GovernanceState.APPROVED}
    for authority in candidate.authorities:
        scope = authority.scope
        if scope.unknown or (scope.project is not None and scope.project != inputs.candidate_project):
            continue
        if scope.domains and inputs.task_domain not in scope.domains:
            continue
        if scope.phases and inputs.task_phase not in scope.phases:
            continue
        if scope.actions and inputs.task_action not in scope.actions:
            continue
        if scope.subject and scope.subject != candidate.represented.subject.value:
            continue
        if candidate.represented.subject in approved_subjects:
            return True
    return False


def _instructional_applicability(candidate: CandidateContext, inputs: EnforcementInputs) -> bool:
    return inputs.instructional_authority_established and _has_governing_authority(candidate, inputs)


def _decision(candidate: CandidateContext, outcome: ApplicabilityOutcome, reasons: tuple[str, ...], qualifications: tuple[Uncertainty, ...]) -> ApplicabilityDecision:
    return ApplicabilityDecision(candidate, outcome, reasons, qualifications)
