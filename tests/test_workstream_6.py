"""Controlled deterministic-discovery tests for Workstream 6 only."""
from __future__ import annotations

from pathlib import Path
import shutil
import tempfile

import pytest

from context_engine.adapters.sqlite_state import (
    PersistedArtifactEvidence, PersistedRepresentation, SQLiteStateStore,
)
from context_engine.application.discovery import DiscoveryEvidence, ExpansionRequest, discover
from context_engine.application.lifecycle import ApplicableSourceUniverse, Availability, BoundaryAdequacy, RegisteredSource, ScopeInputs
from context_engine.core.model import (
    Authority, AuthorityScope, Classification, Conflict, ContextRequest,
    Currentness, CurrentnessAssessment, EpistemicState, GovernanceAssessment,
    GovernanceState, Provenance, Relationship, RepresentedInformation, Requester,
    Consumer, SemanticIdentity, TaskIntent, TaskScope, Uncertainty,
)


def ident(kind: str, value: str) -> SemanticIdentity:
    return SemanticIdentity(kind, value)


@pytest.fixture
def controlled_dir() -> Path:
    directory = Path(tempfile.mkdtemp(dir=Path.home() / "temp", prefix="context-engine-ws6-"))
    try:
        yield directory
    finally:
        shutil.rmtree(directory)


@pytest.fixture
def context_request() -> ContextRequest:
    return ContextRequest(ident("request", "request-6"), ident("project", "project-a"), Requester(ident("requester", "r")), Consumer(ident("consumer", "c")), TaskIntent("review"), TaskScope("bounded docs"))


def evidence(source: RegisteredSource, value: str, *, text: str = "", metadata: tuple[tuple[str, str], ...] = (), classifications: tuple[str, ...] = (), relationships: tuple[Relationship, ...] = (), history: tuple[str, ...] = (), expansion_only: bool = False) -> DiscoveryEvidence:
    provenance = Provenance(ident("provenance", f"p-{value}"), source=ident("source", source.identity), location_reference=f"{value}.md")
    represented = RepresentedInformation(ident("represented_information", value), ident("artifact", f"artifact-{value}"), provenance, tuple(Classification(name) for name in classifications))
    return DiscoveryEvidence(represented, source, text, ("heading",), metadata, relationships, local_history=history, expansion_only=expansion_only)


def universe(context_request: ContextRequest, *sources: RegisteredSource) -> ApplicableSourceUniverse:
    return ApplicableSourceUniverse(context_request.identity.value, sources, BoundaryAdequacy.INDETERMINATE, "governed controlled ASU")


def test_deterministic_mechanisms_and_stable_semantic_ordering(context_request: ContextRequest) -> None:
    source = RegisteredSource("source-a", "project-a", "git", "docs", Availability.AVAILABLE)
    relation = Relationship(ident("relationship", "rel-a"), "governs", ident("represented_information", "literal"), ident("source", "source-a"))
    items = (
        evidence(source, "literal", text="Alpha literal", relationships=(relation,)),
        evidence(source, "metadata", metadata=(("status", "beta"),)),
        evidence(source, "classification", classifications=("gamma",)),
        evidence(source, "identity", history=("commit-delta",)),
    )
    first = discover(context_request, universe(context_request, source), items, query_terms=("alpha", "beta", "gamma", "identity", "heading", "commit-delta", "governs"))
    second = discover(context_request, universe(context_request, source), tuple(reversed(items)), query_terms=("governs", "commit-delta", "heading", "identity", "gamma", "beta", "alpha"))
    assert tuple(item.represented.identity.value for item in first.candidates) == ("identity", "metadata", "classification", "literal")
    assert first == second
    assert "deterministic:identity" in first.candidates[0].discovery_basis
    assert "markdown_structure" in first.candidates[3].discovery_basis


def test_candidate_preserves_governed_evidence_without_elevation(context_request: ContextRequest) -> None:
    source = RegisteredSource("source-a", "project-a", "git", "limited-docs", Availability.PARTIAL)
    base = evidence(source, "x", text="needle")
    authority = Authority(ident("authority", "a"), "recorded basis", AuthorityScope(project=context_request.project), base.represented.provenance)
    governance = GovernanceAssessment(base.represented.subject, GovernanceState.PROPOSED, base.represented.provenance)
    currentness = CurrentnessAssessment(base.represented.subject, Currentness.HISTORICAL)
    conflict = Conflict(ident("conflict", "x"), (ident("claim", "one"), ident("claim", "two")), "same subject", base.represented.provenance)
    item = DiscoveryEvidence(base.represented, source, "needle", authorities=(authority,), governance=(governance,), currentness=(currentness,), conflicts=(conflict,), limitations=(Uncertainty(EpistemicState.UNKNOWN, detail="partial source"),))
    candidate = discover(context_request, universe(context_request, source), (item,), query_terms=("needle",)).candidates[0]
    assert candidate.source_scope == "limited-docs" and candidate.authorities == (authority,)
    assert candidate.governance == (governance,) and candidate.currentness == (currentness,) and candidate.conflicts == (conflict,)
    for forbidden in ("applicable", "selected", "role", "sufficient"):
        assert not hasattr(candidate, forbidden)


@pytest.mark.parametrize("availability", (Availability.UNAVAILABLE, Availability.INACCESSIBLE, Availability.UNAUTHORIZED, Availability.UNSUPPORTED, Availability.PARTIAL))
def test_failure_states_and_negative_results_are_qualified_not_absent(context_request: ContextRequest, availability: Availability) -> None:
    source = RegisteredSource("source-a", "project-a", "git", "docs", availability)
    result = discover(context_request, universe(context_request, source), (evidence(source, "x", text="needle"),), query_terms=("needle",))
    if availability is Availability.PARTIAL:
        assert result.candidates
    else:
        assert not result.candidates
    assert "ASU=request-6" in result.negative_result_scope
    assert result.termination_basis.startswith("bounded deterministic")
    assert not hasattr(result, "universal_absence")


def test_project_isolation_source_scope_and_cross_project_prerequisites(context_request: ContextRequest) -> None:
    local = RegisteredSource("local", "project-a", "git", "docs")
    external = RegisteredSource("external", "project-b", "git", "external-docs")
    records = (evidence(local, "local", text="needle"), evidence(external, "external", text="needle"))
    isolated = discover(context_request, universe(context_request, local, external), records, query_terms=("needle",))
    assert [item.represented.identity.value for item in isolated.candidates] == ["local"]
    allowed = discover(context_request, universe(context_request, local, external), records, query_terms=("needle",), scope_inputs=ScopeInputs(True, True, True, True))
    assert [item.represented.identity.value for item in allowed.candidates] == ["external", "local"]
    assert {item.source_scope for item in allowed.candidates} == {"docs", "external-docs"}


def test_bounded_authorized_relationship_expansion_and_termination(context_request: ContextRequest) -> None:
    source_a = RegisteredSource("source-a", "project-a", "git", "docs")
    source_b = RegisteredSource("source-b", "project-a", "git", "linked-docs")
    origin = evidence(source_a, "origin", text="needle")
    relation = Relationship(ident("relationship", "r"), "bounded-link", origin.represented.identity, ident("source", "source-b"))
    origin = DiscoveryEvidence(origin.represented, source_a, "needle", relationships=(relation,))
    linked = evidence(source_b, "linked", text="needle", expansion_only=True)
    expanded = discover(context_request, universe(context_request, source_a, source_b), (origin, linked), query_terms=("needle",), expansions=(ExpansionRequest(origin.represented.identity, relation.identity, "source-b", True, True, "represented bounded link"),))
    assert [item.represented.identity.value for item in expanded.candidates] == ["linked", "origin"]
    assert expanded.initial_inspected_sources == ("source-a",) and expanded.expanded_inspected_sources == ("source-b",)
    denied = discover(context_request, universe(context_request, source_a, source_b), (origin, linked), query_terms=("needle",), expansions=(ExpansionRequest(origin.represented.identity, relation.identity, "source-b", True, False, "represented bounded link"),))
    assert [item.represented.identity.value for item in denied.candidates] == ["origin"]


def test_persisted_evidence_order_is_semantic_not_sqlite_row_order(controlled_dir: Path) -> None:
    store = SQLiteStateStore(controlled_dir / "state.sqlite")
    store.initialize()
    # This test verifies reload ordering at the evidence boundary; reload does
    # not itself make historical evidence current or a Candidate Context.
    for identity in ("z", "a"):
        store.save_artifact_evidence(PersistedArtifactEvidence("project-a", f"artifact-{identity}", f"version-{identity}", "source", f"{identity}.md", "text", "observation"))
        store.save_representation(PersistedRepresentation("project-a", f"representation-{identity}", f"version-{identity}", f"provenance-{identity}", "line", "{}"))
    assert [item.artifact_version_identity for item in store.artifact_evidence_for_project("project-a")] == ["version-a", "version-z"]
    assert [item.representation_identity for item in store.representations_for_project("project-a")] == ["representation-a", "representation-z"]


def test_negative_semantic_collapse_guards(context_request: ContextRequest) -> None:
    source = RegisteredSource("source-a", "project-a", "git", "docs")
    result = discover(context_request, universe(context_request, source), (evidence(source, "x", text="approved latest needle"),), query_terms=("needle",))
    candidate = result.candidates[0]
    assert "literal" in candidate.discovery_basis
    # Parser/literal ranking/recency-like words are retained evidence only.
    assert not candidate.authorities and not candidate.governance and not candidate.currentness
    assert candidate.represented.provenance.transformation.value == "direct"
    assert not hasattr(result, "sufficiency") and not hasattr(result, "selection")
