"""Strict local JSON adapter for the governed render application boundary.

The JSON document is intentionally an input adapter, not a Context Package
format and not a semantic extraction mechanism.  Callers must provide the
already-governed evidence and every applicability, role, and authorization
decision consumed by :class:`GovernedRenderInputs`.
"""
from __future__ import annotations

import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

from context_engine.application.decision_pipeline import (
    ApplicabilityInputs,
    EnforcementInputs,
    RelevanceOutcome,
    RoleInputs,
)
from context_engine.application.discovery import DiscoveryEvidence, ExpansionRequest
from context_engine.application.lifecycle import (
    ApplicableSourceUniverse,
    Availability,
    BoundaryAdequacy,
    RegisteredSource,
    ScopeInputs,
)
from context_engine.application.orchestration import GovernedRenderInputs
from context_engine.application.package_construction import CoherenceInputs
from context_engine.application.rendering import ConsumerContract, ConsumerKind
from context_engine.application.sufficiency import RequiredDeficiency
from context_engine.core.model import (
    Authority,
    AuthorityScope,
    Classification,
    Conflict,
    Consumer,
    ConsumerId,
    ContextRequest,
    Currentness,
    CurrentnessAssessment,
    EpistemicState,
    GovernanceAssessment,
    GovernanceState,
    Provenance,
    Relationship,
    RepresentedInformation,
    Requester,
    RequesterId,
    SemanticIdentity,
    TaskIntent,
    TaskScope,
    TemporalContext,
    TransformationKind,
    Uncertainty,
)


class CliRenderInputError(ValueError):
    """A local CLI document is missing, malformed, or not explicit enough."""


def load_governed_render_inputs(reference: Path) -> GovernedRenderInputs:
    """Load one explicit v1 local input document without deriving governance."""
    try:
        data = json.loads(reference.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise CliRenderInputError("render input is unavailable or invalid JSON") from error
    root = _mapping(data, "root")
    _exact_keys(root, _ROOT_KEYS, "root")
    if root["version"] != 1:
        raise CliRenderInputError("unsupported render input version")
    base = reference.parent
    request = _request(_mapping(root["request"], "request"))
    universe = _universe(_mapping(root["universe"], "universe"))
    sources = {source.identity: source for source in universe.sources}
    evidence = tuple(_evidence(_mapping(item, "evidence entry"), sources) for item in _list(root["evidence"], "evidence"))
    applicability = _applicability(_list(root["applicability"], "applicability"), request.project)
    roles = _roles(_list(root["role_inputs"], "role_inputs"))
    _complete_decisions(evidence, applicability, roles)
    contract = _contract(_mapping(root["contract"], "contract"))
    if contract.consumer != request.consumer:
        raise CliRenderInputError("ConsumerContract consumer must match Context Request consumer")
    return GovernedRenderInputs(
        _path(base, root["bootstrap_reference"], "bootstrap_reference"),
        _path(base, root["project_configuration_reference"], "project_configuration_reference"),
        _bool(root["operator_authorized"], "operator_authorized"),
        request,
        universe,
        evidence,
        _strings(root["query_terms"], "query_terms", nonempty=True),
        applicability,
        roles,
        _string(root["selection_basis"], "selection_basis"),
        tuple(_deficiency(_mapping(item, "sufficiency deficiency")) for item in _list(root["sufficiency_deficiencies"], "sufficiency_deficiencies")),
        _bool(root["material_conflict"], "material_conflict"),
        _bool(root["material_uncertainty"], "material_uncertainty"),
        _bool(root["bounded_task_safe"], "bounded_task_safe"),
        _identity(_mapping(root["package_identity"], "package_identity")),
        _identity(_mapping(root["record_identity"], "record_identity")),
        _string(root["termination_basis"], "termination_basis"),
        contract,
        _scope(_mapping(root["scope_inputs"], "scope_inputs")),
        tuple(_expansion(_mapping(item, "expansion")) for item in _list(root["expansions"], "expansions")),
        _coherence(_mapping(root["coherence_inputs"], "coherence_inputs")),
        tuple(_uncertainty(_mapping(item, "construction qualification")) for item in _list(root["construction_qualifications"], "construction_qualifications")),
    )


def _complete_decisions(
    evidence: tuple[DiscoveryEvidence, ...],
    applicability: tuple[tuple[str, ApplicabilityInputs], ...],
    roles: tuple[tuple[str, RoleInputs], ...],
) -> None:
    """Require an explicit applicability and role record for every evidence item.

    The orchestration API permits callers to omit a role for deliberately
    unselected material.  A CLI document has no separate exclusion record, so
    accepting omission here would silently turn it into an exclusion.
    """
    represented = {item.represented.identity.value for item in evidence}
    applicability_ids = {identity for identity, _ in applicability}
    role_ids = {identity for identity, _ in roles}
    if represented != applicability_ids:
        raise CliRenderInputError("applicability must cover exactly the supplied represented information identities")
    if represented != role_ids:
        raise CliRenderInputError("role_inputs must cover exactly the supplied represented information identities")


_ROOT_KEYS = frozenset({
    "version", "bootstrap_reference", "project_configuration_reference", "operator_authorized", "request", "universe",
    "evidence", "query_terms", "applicability", "role_inputs", "selection_basis", "sufficiency_deficiencies",
    "material_conflict", "material_uncertainty", "bounded_task_safe", "package_identity", "record_identity",
    "termination_basis", "contract", "scope_inputs", "expansions", "coherence_inputs", "construction_qualifications",
})


def _request(data: Mapping[str, Any]) -> ContextRequest:
    _exact_keys(data, {"identity", "project", "requester", "consumer", "intent", "scope", "constraints"}, "request")
    requester = _identity(_mapping(data["requester"], "requester"))
    consumer = _identity(_mapping(data["consumer"], "consumer"))
    intent = _mapping(data["intent"], "intent")
    _exact_keys(intent, {"purpose", "inferred", "uncertainty"}, "request intent")
    scope = _mapping(data["scope"], "scope")
    _exact_keys(scope, {"description"}, "request scope")
    return ContextRequest(
        _identity(_mapping(data["identity"], "request identity")),
        _identity(_mapping(data["project"], "request project")),
        Requester(RequesterId(requester)), Consumer(ConsumerId(consumer)),
        TaskIntent(_string(intent["purpose"], "intent purpose"), _bool(intent["inferred"], "intent inferred"), _nullable_uncertainty(intent["uncertainty"], "intent uncertainty")),
        TaskScope(_string(scope["description"], "scope description")),
        _strings(data["constraints"], "constraints"),
    )


def _universe(data: Mapping[str, Any]) -> ApplicableSourceUniverse:
    _exact_keys(data, {"request_reference", "sources", "adequacy", "basis"}, "universe")
    sources = tuple(_source(_mapping(item, "registered source")) for item in _list(data["sources"], "sources"))
    if len({source.identity for source in sources}) != len(sources):
        raise CliRenderInputError("registered Source identities must be unique")
    return ApplicableSourceUniverse(_string(data["request_reference"], "universe request_reference"), sources,
                                    _enum(BoundaryAdequacy, data["adequacy"], "universe adequacy"), _string(data["basis"], "universe basis"))


def _source(data: Mapping[str, Any]) -> RegisteredSource:
    _exact_keys(data, {"identity", "project", "source_type", "scope", "availability", "locator"}, "registered source")
    locator = data["locator"]
    if locator is not None and not isinstance(locator, str):
        raise CliRenderInputError("registered source locator must be a string or null")
    return RegisteredSource(_string(data["identity"], "source identity"), _string(data["project"], "source project"),
                            _string(data["source_type"], "source type"), _string(data["scope"], "source scope"),
                            _enum(Availability, data["availability"], "source availability"), locator)


def _evidence(data: Mapping[str, Any], sources: Mapping[str, RegisteredSource]) -> DiscoveryEvidence:
    _exact_keys(data, {"represented", "source_identity", "text", "markdown_kinds", "metadata", "relationships", "authorities", "governance", "currentness", "conflicts", "local_history", "limitations", "expansion_only"}, "evidence entry")
    source_id = _string(data["source_identity"], "evidence source_identity")
    source = sources.get(source_id)
    if source is None:
        raise CliRenderInputError("evidence Source is not registered in the supplied ASU")
    metadata = tuple(_pair(_mapping(item, "metadata entry"), "metadata entry") for item in _list(data["metadata"], "metadata"))
    return DiscoveryEvidence(
        _represented(_mapping(data["represented"], "represented information")), source, _string(data["text"], "evidence text", allow_empty=True),
        _strings(data["markdown_kinds"], "markdown_kinds"), metadata,
        tuple(_relationship(_mapping(item, "relationship")) for item in _list(data["relationships"], "relationships")),
        tuple(_authority(_mapping(item, "authority")) for item in _list(data["authorities"], "authorities")),
        tuple(_governance(_mapping(item, "governance assessment")) for item in _list(data["governance"], "governance")),
        tuple(_currentness(_mapping(item, "currentness assessment")) for item in _list(data["currentness"], "currentness")),
        tuple(_conflict(_mapping(item, "conflict")) for item in _list(data["conflicts"], "conflicts")),
        _strings(data["local_history"], "local_history"),
        tuple(_uncertainty(_mapping(item, "evidence limitation")) for item in _list(data["limitations"], "limitations")),
        _bool(data["expansion_only"], "expansion_only"),
    )


def _represented(data: Mapping[str, Any]) -> RepresentedInformation:
    _exact_keys(data, {"identity", "subject", "provenance", "classifications", "uncertainty", "assertion_content", "authority_basis", "currentness_basis", "governance_basis"}, "represented information")
    optional_strings = tuple(_nullable_string(data[name], name) for name in ("assertion_content", "authority_basis", "currentness_basis", "governance_basis"))
    return RepresentedInformation(
        _identity(_mapping(data["identity"], "represented identity")), _identity(_mapping(data["subject"], "represented subject")),
        _provenance(_mapping(data["provenance"], "represented provenance")),
        tuple(_classification(_mapping(item, "classification")) for item in _list(data["classifications"], "classifications")),
        tuple(_uncertainty(_mapping(item, "represented uncertainty")) for item in _list(data["uncertainty"], "represented uncertainty")),
        *optional_strings,
    )


def _classification(data: Mapping[str, Any]) -> Classification:
    _exact_keys(data, {"name", "provenance"}, "classification")
    return Classification(_string(data["name"], "classification name"), _nullable_provenance(data["provenance"], "classification provenance"))


def _provenance(data: Mapping[str, Any]) -> Provenance:
    _exact_keys(data, {"identity", "origin_projects", "source", "artifact", "artifact_version", "observation", "upstream", "transformation", "missing_material_basis", "location_reference", "transformation_reference", "limitations"}, "provenance")
    return Provenance(
        _identity(_mapping(data["identity"], "provenance identity")),
        tuple(_identity(_mapping(item, "origin project")) for item in _list(data["origin_projects"], "origin_projects")),
        _nullable_identity(data["source"], "provenance source"), _nullable_identity(data["artifact"], "provenance artifact"),
        _nullable_identity(data["artifact_version"], "provenance artifact_version"), _nullable_identity(data["observation"], "provenance observation"),
        tuple(_identity(_mapping(item, "upstream identity")) for item in _list(data["upstream"], "upstream")),
        _enum(TransformationKind, data["transformation"], "provenance transformation"), _bool(data["missing_material_basis"], "missing_material_basis"),
        _nullable_string(data["location_reference"], "location_reference"), _nullable_string(data["transformation_reference"], "transformation_reference"),
        tuple(_uncertainty(_mapping(item, "provenance limitation")) for item in _list(data["limitations"], "provenance limitations")),
    )


def _applicability(entries: Sequence[Any], project: SemanticIdentity) -> tuple[tuple[str, ApplicabilityInputs], ...]:
    result: list[tuple[str, ApplicabilityInputs]] = []
    for entry in entries:
        data = _mapping(entry, "applicability entry")
        _exact_keys(data, {"represented_identity", "relevance", "relevance_basis", "scope_matches_task", "enforcement"}, "applicability entry")
        enforcement = _enforcement(_mapping(data["enforcement"], "enforcement"), project)
        result.append((_string(data["represented_identity"], "represented_identity"), ApplicabilityInputs(
            _enum(RelevanceOutcome, data["relevance"], "relevance"), _string(data["relevance_basis"], "relevance_basis", allow_empty=True),
            _nullable_bool(data["scope_matches_task"], "scope_matches_task"), enforcement)))
    return _unique_pairs(result, "applicability represented identities")


def _enforcement(data: Mapping[str, Any], project: SemanticIdentity) -> EnforcementInputs:
    keys = {"bootstrap_valid", "request_project", "candidate_project", "requester_authorized", "consumer_disclosure_authorized", "protected_metadata_authorized", "task_requires_current", "task_is_historical", "task_domain", "task_phase", "task_action", "requires_governing_authority", "instructional_use_requested", "instructional_authority_established", "cross_project_prerequisites"}
    _exact_keys(data, keys, "enforcement")
    request_project = _identity(_mapping(data["request_project"], "enforcement request_project"))
    candidate_project = _identity(_mapping(data["candidate_project"], "enforcement candidate_project"))
    if request_project != project:
        raise CliRenderInputError("enforcement request_project must match Context Request Project")
    return EnforcementInputs(
        _bool(data["bootstrap_valid"], "bootstrap_valid"), request_project, candidate_project,
        _nullable_bool(data["requester_authorized"], "requester_authorized"), _nullable_bool(data["consumer_disclosure_authorized"], "consumer_disclosure_authorized"),
        _nullable_bool(data["protected_metadata_authorized"], "protected_metadata_authorized"),
        _bool(data["task_requires_current"], "task_requires_current"), _bool(data["task_is_historical"], "task_is_historical"),
        _nullable_string(data["task_domain"], "task_domain"), _nullable_string(data["task_phase"], "task_phase"), _nullable_string(data["task_action"], "task_action"),
        _bool(data["requires_governing_authority"], "requires_governing_authority"), _bool(data["instructional_use_requested"], "instructional_use_requested"),
        _bool(data["instructional_authority_established"], "instructional_authority_established"), _bool(data["cross_project_prerequisites"], "cross_project_prerequisites"),
    )


def _roles(entries: Sequence[Any]) -> tuple[tuple[str, RoleInputs], ...]:
    result: list[tuple[str, RoleInputs]] = []
    keys = {"represented_identity", "omission_risks_incorrect_performance", "omission_risks_improper_performance", "materially_improves_understanding_or_validation", "basis", "consumer_capacity_limited", "rendering_limited"}
    for entry in entries:
        data = _mapping(entry, "role input entry")
        _exact_keys(data, keys, "role input entry")
        result.append((_string(data["represented_identity"], "role represented_identity"), RoleInputs(
            _bool(data["omission_risks_incorrect_performance"], "omission_risks_incorrect_performance"),
            _bool(data["omission_risks_improper_performance"], "omission_risks_improper_performance"),
            _bool(data["materially_improves_understanding_or_validation"], "materially_improves_understanding_or_validation"),
            _string(data["basis"], "role basis"), _bool(data["consumer_capacity_limited"], "consumer_capacity_limited"),
            _bool(data["rendering_limited"], "rendering_limited"),
        )))
    return _unique_pairs(result, "role represented identities")


def _deficiency(data: Mapping[str, Any]) -> RequiredDeficiency:
    _exact_keys(data, {"identity", "basis", "disclosure_denied", "can_proceed_bounded_without", "limitation"}, "sufficiency deficiency")
    return RequiredDeficiency(_identity(_mapping(data["identity"], "deficiency identity")), _string(data["basis"], "deficiency basis"),
                              _bool(data["disclosure_denied"], "disclosure_denied"), _bool(data["can_proceed_bounded_without"], "can_proceed_bounded_without"),
                              _nullable_uncertainty(data["limitation"], "deficiency limitation"))


def _contract(data: Mapping[str, Any]) -> ConsumerContract:
    _exact_keys(data, {"kind", "consumer", "disclosure_authorized", "capacity_characters"}, "ConsumerContract")
    capacity = data["capacity_characters"]
    if capacity is not None and (not isinstance(capacity, int) or isinstance(capacity, bool) or capacity < 0):
        raise CliRenderInputError("capacity_characters must be a non-negative integer or null")
    return ConsumerContract(_enum(ConsumerKind, data["kind"], "consumer kind"), Consumer(ConsumerId(_identity(_mapping(data["consumer"], "contract consumer")))),
                            _nullable_bool(data["disclosure_authorized"], "contract disclosure_authorized"), capacity)


def _scope(data: Mapping[str, Any]) -> ScopeInputs:
    _exact_keys(data, {"task_requires_external", "governed_relationship", "requester_authorized", "consumer_disclosure_authorized"}, "scope_inputs")
    return ScopeInputs(*(_bool(data[key], key) for key in ("task_requires_external", "governed_relationship", "requester_authorized", "consumer_disclosure_authorized")))


def _expansion(data: Mapping[str, Any]) -> ExpansionRequest:
    _exact_keys(data, {"origin", "relationship", "target_source", "material_resolvable_deficiency", "inspection_authorized", "basis"}, "expansion")
    return ExpansionRequest(_identity(_mapping(data["origin"], "expansion origin")), _identity(_mapping(data["relationship"], "expansion relationship")),
                            _string(data["target_source"], "expansion target_source"), _bool(data["material_resolvable_deficiency"], "material_resolvable_deficiency"),
                            _bool(data["inspection_authorized"], "inspection_authorized"), _string(data["basis"], "expansion basis"))


def _coherence(data: Mapping[str, Any]) -> CoherenceInputs:
    keys = {"material_source_changed", "material_governance_changed", "material_authorization_changed", "material_scope_changed", "material_boundary_changed", "compatibility_uncertain", "understood_qualified_state", "basis"}
    _exact_keys(data, keys, "coherence_inputs")
    boolean_fields = (
        "material_source_changed", "material_governance_changed", "material_authorization_changed",
        "material_scope_changed", "material_boundary_changed", "compatibility_uncertain",
        "understood_qualified_state",
    )
    return CoherenceInputs(*(_bool(data[key], key) for key in boolean_fields), _string(data["basis"], "coherence basis"))


def _relationship(data: Mapping[str, Any]) -> Relationship:
    _exact_keys(data, {"identity", "kind", "source", "target", "scope", "provenance", "inferred"}, "relationship")
    return Relationship(_identity(_mapping(data["identity"], "relationship identity")), _string(data["kind"], "relationship kind"),
                        _identity(_mapping(data["source"], "relationship source")), _identity(_mapping(data["target"], "relationship target")),
                        _nullable_string(data["scope"], "relationship scope"), _nullable_provenance(data["provenance"], "relationship provenance"), _bool(data["inferred"], "relationship inferred"))


def _authority(data: Mapping[str, Any]) -> Authority:
    _exact_keys(data, {"identity", "basis", "scope", "provenance", "delegation_basis"}, "authority")
    scope = _mapping(data["scope"], "authority scope")
    _exact_keys(scope, {"project", "domains", "phases", "actions", "subject", "temporal_scope", "unknown"}, "authority scope")
    return Authority(_identity(_mapping(data["identity"], "authority identity")), _string(data["basis"], "authority basis"), AuthorityScope(
        _nullable_identity(scope["project"], "authority scope project"), _strings(scope["domains"], "authority domains"), _strings(scope["phases"], "authority phases"),
        _strings(scope["actions"], "authority actions"), _nullable_string(scope["subject"], "authority subject"), _nullable_string(scope["temporal_scope"], "authority temporal_scope"), _bool(scope["unknown"], "authority unknown")),
        _provenance(_mapping(data["provenance"], "authority provenance")), tuple(_identity(_mapping(item, "delegation identity")) for item in _list(data["delegation_basis"], "delegation_basis")))


def _governance(data: Mapping[str, Any]) -> GovernanceAssessment:
    _exact_keys(data, {"subject", "state", "provenance"}, "governance assessment")
    return GovernanceAssessment(_identity(_mapping(data["subject"], "governance subject")), _enum(GovernanceState, data["state"], "governance state"), _nullable_provenance(data["provenance"], "governance provenance"))


def _currentness(data: Mapping[str, Any]) -> CurrentnessAssessment:
    _exact_keys(data, {"subject", "currentness", "basis", "temporal"}, "currentness assessment")
    temporal = _mapping(data["temporal"], "temporal context")
    temporal_keys = {"event_time", "effective_time", "version_time", "observation_time", "construction_time"}
    _exact_keys(temporal, temporal_keys, "temporal context")
    return CurrentnessAssessment(_identity(_mapping(data["subject"], "currentness subject")), _enum(Currentness, data["currentness"], "currentness"),
                                 tuple(_identity(_mapping(item, "currentness basis")) for item in _list(data["basis"], "currentness basis")),
                                 TemporalContext(*(_nullable_string(temporal[key], key) for key in ("event_time", "effective_time", "version_time", "observation_time", "construction_time"))))


def _conflict(data: Mapping[str, Any]) -> Conflict:
    _exact_keys(data, {"identity", "participants", "scope", "provenance", "resolved_by"}, "conflict")
    return Conflict(_identity(_mapping(data["identity"], "conflict identity")), tuple(_identity(_mapping(item, "conflict participant")) for item in _list(data["participants"], "conflict participants")),
                    _string(data["scope"], "conflict scope"), _provenance(_mapping(data["provenance"], "conflict provenance")), _nullable_identity(data["resolved_by"], "conflict resolved_by"))


def _uncertainty(data: Mapping[str, Any]) -> Uncertainty:
    _exact_keys(data, {"state", "evidence_boundary", "detail"}, "uncertainty")
    return Uncertainty(_enum(EpistemicState, data["state"], "uncertainty state"), _nullable_string(data["evidence_boundary"], "uncertainty evidence_boundary"), _nullable_string(data["detail"], "uncertainty detail"))


def _identity(data: Mapping[str, Any]) -> SemanticIdentity:
    _exact_keys(data, {"kind", "value"}, "semantic identity")
    return SemanticIdentity(_string(data["kind"], "identity kind"), _string(data["value"], "identity value"))


def _nullable_identity(value: Any, name: str) -> SemanticIdentity | None:
    return None if value is None else _identity(_mapping(value, name))


def _nullable_provenance(value: Any, name: str) -> Provenance | None:
    return None if value is None else _provenance(_mapping(value, name))


def _nullable_uncertainty(value: Any, name: str) -> Uncertainty | None:
    return None if value is None else _uncertainty(_mapping(value, name))


def _path(base: Path, value: Any, name: str) -> Path:
    raw = Path(_string(value, name))
    return raw if raw.is_absolute() else base / raw


def _pair(data: Mapping[str, Any], name: str) -> tuple[str, str]:
    _exact_keys(data, {"key", "value"}, name)
    return _string(data["key"], name + " key"), _string(data["value"], name + " value")


def _unique_pairs(values: list[tuple[str, Any]], name: str) -> tuple[tuple[str, Any], ...]:
    if len({key for key, _ in values}) != len(values):
        raise CliRenderInputError(name + " must be unique")
    return tuple(values)


def _mapping(value: Any, name: str) -> Mapping[str, Any]:
    if not isinstance(value, dict):
        raise CliRenderInputError(name + " must be an object")
    return value


def _list(value: Any, name: str) -> list[Any]:
    if not isinstance(value, list):
        raise CliRenderInputError(name + " must be an array")
    return value


def _strings(value: Any, name: str, *, nonempty: bool = False) -> tuple[str, ...]:
    values = _list(value, name)
    result = tuple(_string(item, name + " entry") for item in values)
    if nonempty and not result:
        raise CliRenderInputError(name + " must not be empty")
    return result


def _string(value: Any, name: str, *, allow_empty: bool = False) -> str:
    if not isinstance(value, str) or (not allow_empty and not value):
        raise CliRenderInputError(name + " must be a " + ("string" if allow_empty else "non-empty string"))
    return value


def _nullable_string(value: Any, name: str) -> str | None:
    if value is None:
        return None
    return _string(value, name)


def _bool(value: Any, name: str) -> bool:
    if not isinstance(value, bool):
        raise CliRenderInputError(name + " must be a boolean")
    return value


def _nullable_bool(value: Any, name: str) -> bool | None:
    return None if value is None else _bool(value, name)


def _enum(enum_type, value: Any, name: str):
    try:
        return enum_type(_string(value, name))
    except ValueError as error:
        raise CliRenderInputError(name + " has an unsupported value") from error


def _exact_keys(data: Mapping[str, Any], keys: set[str] | frozenset[str], name: str) -> None:
    missing = set(keys) - set(data)
    unknown = set(data) - set(keys)
    if missing or unknown:
        detail = []
        if missing:
            detail.append("missing=" + ",".join(sorted(missing)))
        if unknown:
            detail.append("unknown=" + ",".join(sorted(unknown)))
        raise CliRenderInputError(name + " keys invalid (" + "; ".join(detail) + ")")
