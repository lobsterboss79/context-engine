"""Bounded deterministic Candidate Context discovery for Workstream 6.

This module consumes already represented evidence and already established
scope/authorization inputs.  It does not observe Sources, interpret task
applicability, select Context Items, or assess sufficiency.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import re

from context_engine.application.lifecycle import (
    ApplicableSourceUniverse, Availability, RegisteredSource, ScopeInputs,
    effective_sources,
)
from context_engine.core.model import (
    Authority, CandidateContext, Conflict, ContextRequest, CurrentnessAssessment,
    GovernanceAssessment, Relationship, RepresentedInformation, SemanticIdentity,
    Uncertainty, EpistemicState,
)


class DiscoveryMechanism(str, Enum):
    IDENTITY = "identity"
    METADATA = "metadata"
    CLASSIFICATION = "classification"
    RELATIONSHIP = "relationship"
    LITERAL = "literal"
    MARKDOWN_STRUCTURE = "markdown_structure"
    LOCAL_GIT_HISTORY = "local_git_history"


_MECHANISM_ORDER = {mechanism: index for index, mechanism in enumerate(DiscoveryMechanism)}


@dataclass(frozen=True)
class DiscoveryEvidence:
    """An explicit, already represented, source-scoped discovery record."""

    represented: RepresentedInformation
    source: RegisteredSource
    text: str = ""
    markdown_kinds: tuple[str, ...] = ()
    metadata: tuple[tuple[str, str], ...] = ()
    relationships: tuple[Relationship, ...] = ()
    authorities: tuple[Authority, ...] = ()
    governance: tuple[GovernanceAssessment, ...] = ()
    currentness: tuple[CurrentnessAssessment, ...] = ()
    conflicts: tuple[Conflict, ...] = ()
    local_history: tuple[str, ...] = ()
    limitations: tuple[Uncertainty, ...] = ()
    expansion_only: bool = False

    def __post_init__(self) -> None:
        if self.represented.provenance.source and self.represented.provenance.source.value != self.source.identity:
            raise ValueError("discovery evidence Source must match represented Provenance")


@dataclass(frozen=True)
class ExpansionRequest:
    """A pre-established, bounded request for one relationship expansion.

    ``material_resolvable_deficiency`` is supplied by an authorized upstream
    process/record.  Discovery does not decide that a deficiency is material.
    """

    origin: SemanticIdentity
    relationship: SemanticIdentity
    target_source: str
    material_resolvable_deficiency: bool
    inspection_authorized: bool
    basis: str


@dataclass(frozen=True)
class DiscoveryResult:
    candidates: tuple[CandidateContext, ...]
    initial_inspected_sources: tuple[str, ...]
    expanded_inspected_sources: tuple[str, ...]
    excluded_sources: tuple[tuple[str, str], ...]
    negative_result_scope: str
    expansion_basis: tuple[str, ...]
    termination_basis: str
    limitations: tuple[Uncertainty, ...]


def discover(
    request: ContextRequest,
    universe: ApplicableSourceUniverse,
    evidence: tuple[DiscoveryEvidence, ...],
    *,
    query_terms: tuple[str, ...],
    scope_inputs: ScopeInputs = ScopeInputs(),
    expansions: tuple[ExpansionRequest, ...] = (),
) -> DiscoveryResult:
    """Return deterministic Candidate Context only from permitted evidence.

    Query terms are explicit established literal/structured request inputs;
    this function intentionally does not infer them from natural language.
    """
    if universe.request_reference != request.identity.value:
        raise ValueError("ASU must belong to the Context Request")
    permitted = effective_sources(request.project.value, universe.sources, scope_inputs)
    permitted_by_id = {source.identity: source for source in permitted}
    universe_by_id = {source.identity: source for source in universe.sources}
    normalized_terms = tuple(sorted({term.casefold() for term in query_terms if term.strip()}))
    excluded: list[tuple[str, str]] = []
    searchable: list[DiscoveryEvidence] = []
    for item in evidence:
        source = universe_by_id.get(item.source.identity)
        if source is None:
            excluded.append((item.source.identity, "outside-applicable-source-universe"))
        elif source.identity not in permitted_by_id:
            excluded.append((source.identity, "project-or-authorization-scope-excluded"))
        elif source.availability in {Availability.UNAVAILABLE, Availability.INACCESSIBLE, Availability.UNAUTHORIZED, Availability.UNSUPPORTED}:
            excluded.append((source.identity, source.availability.value))
        elif item.expansion_only:
            # It is eligible only through a separately justified bounded
            # relationship expansion below, never by incidental availability.
            continue
        else:
            searchable.append(item)
    # ASU Sources without represented evidence remain explicit limitations.
    represented_source_ids = {item.source.identity for item in evidence}
    for source in universe.sources:
        if source.identity not in represented_source_ids:
            excluded.append((source.identity, source.availability.value if source.availability is not Availability.AVAILABLE else "not-inspected"))

    initial_ids = tuple(sorted({item.source.identity for item in searchable}))
    allowed_evidence = list(searchable)
    expansion_basis: list[str] = []
    expanded_ids: set[str] = set()
    for expansion in sorted(expansions, key=lambda value: (value.origin.value, value.relationship.value, value.target_source)):
        if not (expansion.material_resolvable_deficiency and expansion.inspection_authorized and expansion.basis):
            continue
        target = permitted_by_id.get(expansion.target_source)
        if target is None:
            excluded.append((expansion.target_source, "expansion-outside-governed-effective-scope"))
            continue
        if target.availability in {Availability.UNAVAILABLE, Availability.INACCESSIBLE, Availability.UNAUTHORIZED, Availability.UNSUPPORTED}:
            excluded.append((target.identity, f"expansion-{target.availability.value}"))
            continue
        related = any(
            relation.identity == expansion.relationship
            and relation.source == expansion.origin
            and relation.target.value == expansion.target_source
            for item in searchable for relation in item.relationships
        )
        if not related:
            excluded.append((expansion.target_source, "expansion-relationship-not-represented"))
            continue
        additions = [item for item in evidence if item.source.identity == target.identity and item not in allowed_evidence]
        allowed_evidence.extend(additions)
        expanded_ids.add(target.identity)
        expansion_basis.append(expansion.basis)

    hits: list[tuple[tuple[int, str, str], CandidateContext]] = []
    for item in allowed_evidence:
        mechanisms = _match_mechanisms(item, normalized_terms)
        if not mechanisms:
            continue
        ordered = tuple(sorted(mechanisms, key=_MECHANISM_ORDER.__getitem__))
        basis = "deterministic:" + ",".join(value.value for value in ordered)
        source_limitations = () if item.source.availability is not Availability.PARTIAL else (
            Uncertainty(EpistemicState.UNKNOWN, detail=f"Source {item.source.identity}: partial"),
        )
        candidate = CandidateContext(
            request.identity, item.represented, basis, item.source.scope,
            item.relationships, item.authorities, item.governance, item.currentness,
            item.conflicts, item.represented.uncertainty + item.limitations + source_limitations,
        )
        hits.append(((_MECHANISM_ORDER[ordered[0]], item.represented.identity.value, item.represented.provenance.identity.value), candidate))
    hits.sort(key=lambda item: item[0])
    limitations = _boundary_limitations(universe, tuple(sorted(set(excluded))))
    scope = f"ASU={universe.request_reference}; adequacy={universe.adequacy.value}; inspected={','.join(initial_ids + tuple(sorted(expanded_ids)))}"
    return DiscoveryResult(tuple(candidate for _, candidate in hits), initial_ids, tuple(sorted(expanded_ids)), tuple(sorted(set(excluded))), scope, tuple(expansion_basis), "bounded deterministic inspection completed; no applicability, selection, or sufficiency evaluation", limitations)


def _match_mechanisms(item: DiscoveryEvidence, terms: tuple[str, ...]) -> set[DiscoveryMechanism]:
    if not terms:
        return set()
    matches: set[DiscoveryMechanism] = set()
    identities = (item.represented.identity.value, item.represented.subject.value, item.source.identity)
    metadata = tuple(value for _, value in item.metadata)
    classifications = tuple(value.name for value in item.represented.classifications)
    relationships = tuple(value.kind for value in item.relationships) + tuple(value.target.value for value in item.relationships)
    text = item.text.casefold()
    for term in terms:
        if term in tuple(value.casefold() for value in identities): matches.add(DiscoveryMechanism.IDENTITY)
        if term in tuple(value.casefold() for value in metadata): matches.add(DiscoveryMechanism.METADATA)
        if term in tuple(value.casefold() for value in classifications): matches.add(DiscoveryMechanism.CLASSIFICATION)
        if term in tuple(value.casefold() for value in relationships): matches.add(DiscoveryMechanism.RELATIONSHIP)
        if term in text: matches.add(DiscoveryMechanism.LITERAL)
        if term in tuple(value.casefold() for value in item.markdown_kinds): matches.add(DiscoveryMechanism.MARKDOWN_STRUCTURE)
        if term in tuple(value.casefold() for value in item.local_history): matches.add(DiscoveryMechanism.LOCAL_GIT_HISTORY)
    return matches


def _boundary_limitations(universe: ApplicableSourceUniverse, excluded: tuple[tuple[str, str], ...]) -> tuple[Uncertainty, ...]:
    limitations = [Uncertainty(EpistemicState.UNKNOWN, evidence_boundary=universe.basis, detail=f"ASU adequacy={universe.adequacy.value}")]
    for source, reason in excluded:
        if reason in {Availability.UNAVAILABLE.value, Availability.INACCESSIBLE.value, Availability.UNAUTHORIZED.value, Availability.UNSUPPORTED.value, Availability.PARTIAL.value, "not-inspected"}:
            state = EpistemicState.UNAUTHORIZED if reason == Availability.UNAUTHORIZED.value else EpistemicState.UNAVAILABLE
            limitations.append(Uncertainty(state, evidence_boundary=universe.basis, detail=f"Source {source}: {reason}"))
    return tuple(limitations)
