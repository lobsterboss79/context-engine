"""Local application composition for the already-governed decision pipeline."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from context_engine.adapters.sqlite_state import SQLiteStateStore
from context_engine.application.bootstrap import Bootstrap, ProjectConfiguration, establish_bootstrap, load_project_configuration
from context_engine.application.decision_pipeline import ApplicabilityInputs, RoleInputs, evaluate_applicability, select_candidate
from context_engine.application.discovery import DiscoveryEvidence, DiscoveryResult, ExpansionRequest, discover
from context_engine.application.lifecycle import ApplicableSourceUniverse, ScopeInputs
from context_engine.application.package_construction import CoherenceInputs, PackageConstruction, construct_logical_package, evaluate_coherence, persist_construction
from context_engine.application.rendering import ConsumerContract, RenderingResult, render_package
from context_engine.application.sufficiency import RequiredDeficiency, SufficiencyDecision, SufficiencyInputs, evaluate_sufficiency
from context_engine.core.model import CandidateContext, ContextRequest, SemanticIdentity


@dataclass(frozen=True)
class GovernedRenderInputs:
    """Already-governed inputs for one on-demand local composition.

    Observation, Markdown transformation, and representation must occur before
    this boundary; their represented evidence is consumed here.  This type is
    intentionally an application API, not a Context Package import format.
    """
    bootstrap_reference: Path
    project_configuration_reference: Path
    operator_authorized: bool
    request: ContextRequest
    universe: ApplicableSourceUniverse
    evidence: tuple[DiscoveryEvidence, ...]
    query_terms: tuple[str, ...]
    applicability: tuple[tuple[str, ApplicabilityInputs], ...]
    role_inputs: tuple[tuple[str, RoleInputs], ...]
    selection_basis: str
    sufficiency_deficiencies: tuple[RequiredDeficiency, ...]
    material_conflict: bool
    material_uncertainty: bool
    bounded_task_safe: bool
    package_identity: SemanticIdentity
    record_identity: SemanticIdentity
    termination_basis: str
    contract: ConsumerContract
    scope_inputs: ScopeInputs = ScopeInputs()
    expansions: tuple[ExpansionRequest, ...] = ()
    coherence_inputs: CoherenceInputs = CoherenceInputs()


@dataclass(frozen=True)
class GovernedRenderOutcome:
    bootstrap: Bootstrap
    configuration: ProjectConfiguration
    discovery: DiscoveryResult
    construction: PackageConstruction
    rendering: RenderingResult


def run_governed_render(inputs: GovernedRenderInputs, *, store: SQLiteStateStore | None = None) -> GovernedRenderOutcome:
    """Compose approved stages without reimplementing their semantic logic."""
    bootstrap = establish_bootstrap(inputs.bootstrap_reference, operator_authorized=inputs.operator_authorized)
    configuration = load_project_configuration(bootstrap, inputs.project_configuration_reference)
    if configuration.project_identity != inputs.request.project.value:
        raise ValueError("Context Request Project is outside Bootstrap-established Project configuration")
    discovery = discover(inputs.request, inputs.universe, inputs.evidence, query_terms=inputs.query_terms,
                         scope_inputs=inputs.scope_inputs, expansions=inputs.expansions)
    applicability = dict(inputs.applicability)
    roles = dict(inputs.role_inputs)
    selected = []
    for candidate in discovery.candidates:
        evaluated = evaluate_applicability(candidate, applicability.get(candidate.represented.identity.value, _missing_applicability(inputs, candidate)))
        role = roles.get(candidate.represented.identity.value)
        if role is None:
            continue
        result = select_candidate(evaluated, role, selection_basis=inputs.selection_basis)
        if result.selected is not None:
            selected.append(result.selected)
    sufficiency = evaluate_sufficiency(SufficiencyInputs(tuple(selected), inputs.universe, inputs.sufficiency_deficiencies,
                                                           inputs.material_conflict, inputs.material_uncertainty, inputs.bounded_task_safe))
    construction = construct_logical_package(package_identity=inputs.package_identity, request=inputs.request.identity,
        selected=tuple(selected), candidates=discovery.candidates, universe=inputs.universe, sufficiency=sufficiency,
        coherence=evaluate_coherence(inputs.coherence_inputs), record_identity=inputs.record_identity,
        termination_basis=inputs.termination_basis)
    if store is not None:
        persist_construction(store, project_identity=inputs.request.project.value, construction=construction)
    rendering = (render_package(construction.package, inputs.contract) if construction.package is not None else
                 RenderingResult("denied", None, None, ("logical-package-construction-denied",)))
    if store is not None:
        store.write_audit(inputs.request.project.value, "rendering-" + rendering.status,
                          "package=" + inputs.package_identity.value + "; reasons=" + ",".join(rendering.reason_codes))
    return GovernedRenderOutcome(bootstrap, configuration, discovery, construction, rendering)


def _missing_applicability(inputs: GovernedRenderInputs, candidate: CandidateContext) -> ApplicabilityInputs:
    """A missing deterministic applicability input fails closed through W7."""
    from context_engine.application.decision_pipeline import EnforcementInputs, RelevanceOutcome
    return ApplicabilityInputs(RelevanceOutcome.UNKNOWN, "", None,
        EnforcementInputs(True, inputs.request.project, inputs.request.project, True, True))
