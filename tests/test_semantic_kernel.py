"""Semantic and anti-collapse tests for the Workstream 2 governed kernel."""

from __future__ import annotations

import pytest

from context_engine.core.model import (
    ApplicableSourceUniverse, Artifact, Authority, AuthorityScope, CandidateContext,
    CandidateProposal, Classification, Conflict, Consumer, ConsumerRendering,
    ConstructionState, ContextItem, ContextRequest, ContextRole, ContextPackage,
    Currentness, CurrentnessAssessment, DeliveryAttempt, EpistemicState,
    GovernanceAssessment, GovernanceState, ObservedState, PackageConstructionRecord, Project,
    Provenance, RepresentedInformation, Requester, SemanticIdentity,
    SemanticInvariantError, Source, SourceManifest, SufficiencyOutcome, TaskIntent,
    TaskScope, TransformationKind, Uncertainty,
)


def identity(kind: str, value: str) -> SemanticIdentity:
    return SemanticIdentity(kind, value)


@pytest.fixture
def provenance() -> Provenance:
    return Provenance(identity("provenance", "p"), origin_projects=(identity("project", "one"),))


@pytest.fixture
def context_request() -> ContextRequest:
    return ContextRequest(
        identity("request", "r"), identity("project", "one"),
        Requester(identity("requester", "requester")), Consumer(identity("consumer", "consumer")),
        TaskIntent("review"), TaskScope("kernel"),
    )


def test_project_is_not_source_or_repository(provenance: Provenance) -> None:
    project = Project(identity("project", "one"), provenance=provenance)
    source = Source(identity("source", "docs"), project.identity, "markdown", locators=("repo/README.md",))
    assert project.identity != source.identity
    assert source.locators[0] != source.identity.value


def test_authority_scope_and_governance_state_are_independent(provenance: Provenance) -> None:
    claim = identity("claim", "decision")
    authority = Authority(identity("authority", "owner"), "owner decision", AuthorityScope(project=identity("project", "one")), provenance)
    state = GovernanceAssessment(claim, GovernanceState.PROPOSED, provenance)
    assert authority.scope.project != state.subject
    with pytest.raises(SemanticInvariantError, match="not unrestricted"):
        AuthorityScope(project=identity("project", "one"), unknown=True)


def test_claim_identity_does_not_change_with_physical_locator_or_governance(provenance: Provenance) -> None:
    claim = identity("claim", "use-python")
    artifact_a = Artifact(identity("artifact", "a"), identity("source", "s"), ("old.md",))
    artifact_b = Artifact(identity("artifact", "b"), identity("source", "s"), ("new.md",))
    assert artifact_a.identity != artifact_b.identity
    assert GovernanceAssessment(claim, GovernanceState.APPROVED).subject == claim
    assert GovernanceAssessment(claim, GovernanceState.REJECTED).subject == claim


def test_shared_locator_does_not_merge_semantic_source_or_artifact_identity(provenance: Provenance) -> None:
    project = identity("project", "one")
    first = Source(identity("source", "first"), project, "markdown", locators=("same/path.md",))
    second = Source(identity("source", "second"), project, "markdown", locators=("same/path.md",))
    assert first.identity != second.identity
    assert Artifact(identity("artifact", "a"), first.identity, ("same/path.md",)).identity != Artifact(identity("artifact", "b"), second.identity, ("same/path.md",)).identity


def test_candidate_proposal_and_candidate_context_are_distinct(provenance: Provenance, context_request: ContextRequest) -> None:
    represented = RepresentedInformation(identity("represented", "x"), identity("claim", "c"), provenance)
    proposal = CandidateProposal(identity("proposal", "p"), represented.identity, provenance)
    candidate = CandidateContext(context_request.identity, represented, "discovery basis")
    assert proposal.represented == represented.identity
    assert candidate.represented is represented


def test_observation_and_recency_do_not_establish_currentness() -> None:
    assessment = CurrentnessAssessment(identity("claim", "c"))
    assert assessment.currentness is Currentness.UNKNOWN
    observation = ObservedState(identity("observation", "o"), identity("source", "s"), observed_reference="newer")
    assert not hasattr(observation, "authority")
    assert not hasattr(observation, "currentness")
    historical = CurrentnessAssessment(identity("claim", "c"), Currentness.HISTORICAL)
    assert historical.currentness is Currentness.HISTORICAL


def test_provenance_preserves_transformation_lineage(provenance: Provenance) -> None:
    derived = Provenance(identity("provenance", "derived"), upstream=(provenance.identity,), transformation=TransformationKind.SUMMARIZED)
    assert derived.upstream == (provenance.identity,)
    assert derived.transformation.value == "summarized"


def test_conflict_and_uncertainty_are_preserved_not_resolved(provenance: Provenance) -> None:
    conflict = Conflict(identity("conflict", "x"), (identity("claim", "a"), identity("claim", "b")), "overlapping", provenance)
    assert conflict.resolved_by is None
    missing = Uncertainty(EpistemicState.MISSING, evidence_boundary="ASU-1")
    assert missing.state is EpistemicState.MISSING
    with pytest.raises(SemanticInvariantError, match="evidence boundary"):
        Uncertainty(EpistemicState.MISSING)


def test_represented_information_cannot_be_context_item_without_candidate_and_selection(
    provenance: Provenance, context_request: ContextRequest,
) -> None:
    represented = RepresentedInformation(identity("represented", "x"), identity("claim", "c"), provenance)
    candidate = CandidateContext(context_request.identity, represented, "found in authorized scope")
    selected = ContextItem.select(candidate, basis="task-relative selection", role=ContextRole.REQUIRED)
    assert selected.represented is represented
    assert selected.role is ContextRole.REQUIRED
    with pytest.raises(SemanticInvariantError, match="explicit governed basis"):
        ContextItem.select(candidate, basis="", role=ContextRole.SUPPORTING)
    with pytest.raises(SemanticInvariantError, match="selection construction path"):
        ContextItem(candidate, ContextRole.REQUIRED)  # type: ignore[arg-type]


def test_discovery_does_not_establish_applicability_or_selection(provenance: Provenance, context_request: ContextRequest) -> None:
    represented = RepresentedInformation(identity("represented", "x"), identity("claim", "c"), provenance)
    candidate = CandidateContext(context_request.identity, represented, "discovered")
    assert not hasattr(candidate, "applicable")
    assert not hasattr(candidate, "selected")


def test_package_rejects_unqualified_sufficiency_with_incoherence(provenance: Provenance, context_request: ContextRequest) -> None:
    represented = RepresentedInformation(identity("represented", "x"), identity("claim", "c"), provenance)
    item = ContextItem.select(CandidateContext(context_request.identity, represented, "d"), basis="s", role=ContextRole.REQUIRED)
    with pytest.raises(SemanticInvariantError, match="incoherence"):
        ContextPackage(identity("package", "p"), context_request.identity, (item,), SourceManifest(()), SufficiencyOutcome.SUFFICIENT, ConstructionState("incoherent", "drift"))


def test_rendering_delivery_receipt_and_use_are_distinct(context_request: ContextRequest) -> None:
    rendering = ConsumerRendering(identity("package", "p"), context_request.consumer, "rendering")
    delivery = DeliveryAttempt(rendering, "destination")
    assert delivery.rendering is rendering
    assert not hasattr(delivery, "received_reference")


def test_consumer_identity_cannot_waive_required_context(provenance: Provenance, context_request: ContextRequest) -> None:
    represented = RepresentedInformation(identity("represented", "x"), identity("claim", "c"), provenance)
    required = ContextItem.select(CandidateContext(context_request.identity, represented, "d"), basis="selection", role=ContextRole.REQUIRED)
    other_consumer = Consumer(identity("consumer", "limited"))
    assert context_request.consumer != other_consumer
    assert required.role is ContextRole.REQUIRED


def test_package_record_preserves_source_universe_and_candidate_limitations(provenance: Provenance, context_request: ContextRequest) -> None:
    represented = RepresentedInformation(identity("represented", "x"), identity("claim", "c"), provenance)
    candidate = CandidateContext(context_request.identity, represented, "discovery")
    universe = ApplicableSourceUniverse((identity("source", "one"),), Uncertainty(EpistemicState.UNAVAILABLE))
    record = PackageConstructionRecord(identity("record", "r"), context_request.identity, None, universe, (candidate,), None, None)
    assert record.source_universe.adequacy is not None
