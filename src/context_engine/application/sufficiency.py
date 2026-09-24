"""Evidence-boundary-aware Workstream 8 sufficiency and iteration planning."""
from __future__ import annotations

from dataclasses import dataclass

from context_engine.application.lifecycle import ApplicableSourceUniverse, Availability
from context_engine.core.model import ContextItem, EpistemicState, SemanticIdentity, SufficiencyOutcome, Uncertainty


@dataclass(frozen=True)
class RequiredDeficiency:
    """Known Required Context not covered by the selected body."""

    identity: SemanticIdentity
    basis: str
    disclosure_denied: bool = False
    can_proceed_bounded_without: bool = False
    limitation: Uncertainty | None = None


@dataclass(frozen=True)
class SufficiencyInputs:
    selected: tuple[ContextItem, ...]
    universe: ApplicableSourceUniverse
    required_deficiencies: tuple[RequiredDeficiency, ...] = ()
    material_conflict: bool = False
    material_uncertainty: bool = False
    bounded_task_safe: bool = False


@dataclass(frozen=True)
class SufficiencyDecision:
    outcome: SufficiencyOutcome
    reason_codes: tuple[str, ...]
    limitations: tuple[Uncertainty, ...]
    required_deficiencies: tuple[RequiredDeficiency, ...]


@dataclass(frozen=True)
class DiscoveryDeficiency:
    identity: SemanticIdentity
    basis: str
    material: bool
    resolvable_by_discovery: bool
    authorized: bool
    in_scope: bool
    source_ids: tuple[str, ...] = ()


@dataclass(frozen=True)
class IterationPlan:
    deficiency: DiscoveryDeficiency
    initial_boundary: str
    additional_sources: tuple[str, ...]
    termination_reason: str
    authorized_to_discover: bool


def evaluate_sufficiency(inputs: SufficiencyInputs) -> SufficiencyDecision:
    """Evaluate selected coverage and ASU evidence without creating a package.

    Conditional Sufficiency retains every missing Required item.  It is allowed
    only for an explicitly safe bounded task that does not depend on the
    unavailable Required information; it never changes that item's role.
    """
    limitations = list(_universe_limitations(inputs.universe))
    limitations.extend(deficiency.limitation for deficiency in inputs.required_deficiencies if deficiency.limitation is not None)
    denied = tuple(item for item in inputs.required_deficiencies if item.disclosure_denied)
    if denied:
        return SufficiencyDecision(SufficiencyOutcome.DENIED, ("required-context-disclosure-denied",), tuple(limitations), inputs.required_deficiencies)
    if inputs.required_deficiencies:
        if inputs.bounded_task_safe and all(item.can_proceed_bounded_without for item in inputs.required_deficiencies):
            return SufficiencyDecision(SufficiencyOutcome.CONDITIONALLY_SUFFICIENT, ("required-context-remains-missing-bounded-task-only",), tuple(limitations), inputs.required_deficiencies)
        return SufficiencyDecision(SufficiencyOutcome.INSUFFICIENT, ("required-context-missing-or-omitted",), tuple(limitations), inputs.required_deficiencies)
    if inputs.material_conflict:
        return SufficiencyDecision(SufficiencyOutcome.INSUFFICIENT, ("material-conflict-unresolved",), tuple(limitations), ())
    if inputs.material_uncertainty:
        return SufficiencyDecision(SufficiencyOutcome.INSUFFICIENT, ("material-uncertainty-unresolved",), tuple(limitations), ())
    if inputs.universe.adequacy.value != "adequate":
        if inputs.bounded_task_safe:
            return SufficiencyDecision(SufficiencyOutcome.CONDITIONALLY_SUFFICIENT, ("asu-evidence-boundary-qualified",), tuple(limitations), ())
        return SufficiencyDecision(SufficiencyOutcome.INSUFFICIENT, ("asu-evidence-boundary-inadequate",), tuple(limitations), ())
    return SufficiencyDecision(SufficiencyOutcome.SUFFICIENT, ("selected-required-coverage-and-adequate-asu",), tuple(limitations), ())


def plan_bounded_iteration(universe: ApplicableSourceUniverse, deficiency: DiscoveryDeficiency) -> IterationPlan:
    """Plan, but do not execute, one deterministic authorized discovery step."""
    boundary = f"ASU={universe.request_reference}; adequacy={universe.adequacy.value}; basis={universe.basis}"
    allowed = {source.identity for source in universe.sources}
    additional = tuple(sorted(source for source in deficiency.source_ids if source in allowed))
    if not deficiency.material:
        return IterationPlan(deficiency, boundary, (), "deficiency-not-material", False)
    if not deficiency.resolvable_by_discovery:
        return IterationPlan(deficiency, boundary, (), "no-justified-useful-discovery", False)
    if not deficiency.authorized or not deficiency.in_scope:
        return IterationPlan(deficiency, boundary, (), "authorization-or-scope-boundary", False)
    if not additional:
        return IterationPlan(deficiency, boundary, (), "no-governed-additional-source", False)
    return IterationPlan(deficiency, boundary, additional, "one-bounded-authorized-discovery-step-requested", True)


def _universe_limitations(universe: ApplicableSourceUniverse) -> tuple[Uncertainty, ...]:
    items = [Uncertainty(EpistemicState.UNKNOWN, evidence_boundary=universe.basis, detail=f"ASU adequacy={universe.adequacy.value}")]
    for source in universe.sources:
        if source.availability is not Availability.AVAILABLE:
            state = EpistemicState.UNAUTHORIZED if source.availability is Availability.UNAUTHORIZED else EpistemicState.UNAVAILABLE
            items.append(Uncertainty(state, evidence_boundary=universe.basis, detail=f"Source {source.identity}: {source.availability.value}"))
    return tuple(items)
