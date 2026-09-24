"""Controlled Consumer-rendering and application-composition tests."""
from __future__ import annotations

from pathlib import Path
import json
import shutil
import tempfile

import pytest

from context_engine.adapters.sqlite_state import SQLiteStateStore
from context_engine.application.decision_pipeline import ApplicabilityInputs, EnforcementInputs, RelevanceOutcome, RoleInputs
from context_engine.application.discovery import DiscoveryEvidence
from context_engine.application.lifecycle import ApplicableSourceUniverse, Availability, BoundaryAdequacy, RegisteredSource
from context_engine.application.orchestration import GovernedRenderInputs, run_governed_render
from context_engine.application.package_construction import CoherenceInputs
from context_engine.application.rendering import ConsumerContract, ConsumerKind, render_package
from context_engine.application.sufficiency import RequiredDeficiency
from context_engine.core.model import (
    CandidateContext, Conflict, Consumer, ConsumerId, ContextItem, ContextPackage, ContextRequest,
    ContextRole, ConstructionState, Currentness, CurrentnessAssessment, EpistemicState,
    GovernanceAssessment, GovernanceState, Provenance, RepresentedInformation, Requester,
    RequesterId, SemanticIdentity, SourceManifest, SourceManifestEntry, SufficiencyOutcome,
    TaskIntent, TaskScope, Uncertainty,
)


def ident(kind: str, value: str) -> SemanticIdentity:
    return SemanticIdentity(kind, value)


@pytest.fixture
def controlled_dir() -> Path:
    directory = Path(tempfile.mkdtemp(dir=Path.home() / "temp", prefix="context-engine-ws9-"))
    try:
        yield directory
    finally:
        shutil.rmtree(directory)


@pytest.fixture
def governed_request() -> ContextRequest:
    return ContextRequest(ident("request", "request-9"), ident("project", "project-9"),
        Requester(RequesterId(ident("requester", "requester-9"))),
        Consumer(ConsumerId(ident("consumer", "consumer-9"))), TaskIntent("controlled task"), TaskScope("controlled scope"))


def package(request: ContextRequest) -> ContextPackage:
    provenance = Provenance(ident("provenance", "p9"), source=ident("source", "source-9"), observation=ident("observation", "o9"), location_reference="doc.md:1")
    represented = RepresentedInformation(ident("represented_information", "r9"), ident("claim", "c9"), provenance,
        uncertainty=(Uncertainty(EpistemicState.UNAVAILABLE, detail="partial Source"),))
    conflict = Conflict(ident("conflict", "conflict-9"), (ident("claim", "c9"), ident("claim", "c10")), "controlled", provenance)
    candidate = CandidateContext(request.identity, represented, "deterministic:literal",
        governance=(GovernanceAssessment(represented.subject, GovernanceState.APPROVED),),
        currentness=(CurrentnessAssessment(represented.subject, Currentness.HISTORICAL),), conflicts=(conflict,),
        limitations=(Uncertainty(EpistemicState.UNKNOWN, detail="explicit limitation"),))
    required = ContextItem.select(candidate, basis="counterfactual omission", role=ContextRole.REQUIRED)
    supporting = ContextItem.select(candidate, basis="validation benefit", role=ContextRole.SUPPORTING)
    return ContextPackage(ident("package", "package-9"), request.identity, (required, supporting),
        SourceManifest((SourceManifestEntry(ident("source", "source-9"), observation=ident("observation", "o9"), contributed=True),)),
        SufficiencyOutcome.CONDITIONALLY_SUFFICIENT, ConstructionState("coherent_with_qualification", "controlled qualification"),
        (Uncertainty(EpistemicState.UNKNOWN, detail="ASU qualification"),))


def contract(request: ContextRequest, kind: ConsumerKind, **values) -> ConsumerContract:
    return ConsumerContract(kind, request.consumer, values.get("disclosure_authorized", True), values.get("capacity_characters"))


def payload(result) -> dict[str, object]:
    assert result.content is not None
    return json.loads(result.content.split("```json\n", 1)[1].rsplit("\n```", 1)[0])


def test_all_renderers_share_one_complete_semantic_view(governed_request: ContextRequest) -> None:
    logical = package(governed_request)
    results = [render_package(logical, contract(governed_request, kind)) for kind in ConsumerKind]
    assert all(result.status == "rendered" for result in results)
    assert payload(results[0]) == payload(results[1]) == payload(results[2])
    view = payload(results[0])
    assert len(view["required_context"]) == 1 and len(view["supporting_context"]) == 1
    assert view["sufficiency"] == "conditionally_sufficient"
    assert "evidence, not Context Engine instructions" in view["source_content_boundary"]
    assert not hasattr(results[0].rendering, "delivery")


def test_disclosure_and_capacity_fail_closed_without_package_leak(governed_request: ContextRequest) -> None:
    logical = package(governed_request)
    denied = render_package(logical, contract(governed_request, ConsumerKind.HUMAN, disclosure_authorized=None))
    constrained = render_package(logical, contract(governed_request, ConsumerKind.HUMAN, capacity_characters=20))
    assert denied.status == "denied" and denied.content is None
    assert constrained.status == "failed" and constrained.content is None
    assert "package-9" not in " ".join(denied.reason_codes + constrained.reason_codes)
    assert logical.items[0].role is ContextRole.REQUIRED


def test_rendering_does_not_create_authority_or_currentness(governed_request: ContextRequest) -> None:
    logical = package(governed_request)
    before = logical
    result = render_package(logical, contract(governed_request, ConsumerKind.CODEX))
    assert result.status == "rendered" and logical == before
    rendered = payload(result)["required_context"][0]
    assert rendered["governance_state"][0]["state"] == "approved"
    assert rendered["currentness"][0]["state"] == "historical"
    assert rendered["authority"] == []


def _bootstrap_files(directory: Path) -> tuple[Path, Path]:
    bootstrap = directory / "bootstrap.toml"
    configuration = directory / "project.toml"
    bootstrap.write_text('version = 1\n[bootstrap]\nproject = "project-9"\nscope = "controlled"\ngovernance_basis = "approved-fixture"\nproject_configuration = "project.toml"\n')
    configuration.write_text('version = 1\n[project]\nidentity = "project-9"\ngovernance_reference = "approved-fixture"\n')
    return bootstrap, configuration


def test_controlled_full_application_composition_and_durable_audit(controlled_dir: Path, governed_request: ContextRequest) -> None:
    bootstrap, configuration = _bootstrap_files(controlled_dir)
    logical = package(governed_request)
    item = logical.items[0]
    source = RegisteredSource("source-9", "project-9", "markdown", "docs", Availability.AVAILABLE)
    universe = ApplicableSourceUniverse(governed_request.identity.value, (source,), BoundaryAdequacy.ADEQUATE, "controlled ASU")
    evidence = DiscoveryEvidence(item.represented, source, text="controlled task", governance=item.governance, currentness=item.currentness, conflicts=item.conflicts)
    enforcement = EnforcementInputs(True, governed_request.project, governed_request.project, True, True)
    applicability = ApplicabilityInputs(RelevanceOutcome.RELEVANT, "controlled deterministic relevance", True, enforcement)
    role = RoleInputs(True, False, False, "controlled counterfactual omission", consumer_capacity_limited=True, rendering_limited=True)
    inputs = GovernedRenderInputs(bootstrap, configuration, True, governed_request, universe, (evidence,), ("controlled",),
        ((item.represented.identity.value, applicability),), ((item.represented.identity.value, role),), "explicit governed selection",
        (), False, False, False, ident("package", "pipeline-package-9"), ident("record", "pipeline-record-9"), "controlled termination",
        contract(governed_request, ConsumerKind.CHATGPT), coherence_inputs=CoherenceInputs())
    store = SQLiteStateStore(controlled_dir / "state.sqlite")
    store.initialize()
    outcome = run_governed_render(inputs, store=store)
    assert outcome.discovery.candidates and outcome.construction.package is not None
    assert outcome.construction.package.sufficiency is SufficiencyOutcome.SUFFICIENT
    assert outcome.rendering.status == "rendered"
    assert store.audit_for_project("project-9", authorized=True)[0][0] == "rendering-rendered"
    assert not hasattr(outcome.rendering.rendering, "receipt") and not hasattr(outcome.rendering.rendering, "use")


def test_controlled_denied_and_insufficient_outcomes_do_not_fake_rendering(controlled_dir: Path, governed_request: ContextRequest) -> None:
    bootstrap, configuration = _bootstrap_files(controlled_dir)
    logical = package(governed_request)
    source = RegisteredSource("source-9", "project-9", "markdown", "docs", Availability.PARTIAL)
    universe = ApplicableSourceUniverse(governed_request.identity.value, (source,), BoundaryAdequacy.KNOWN_INCOMPLETE, "bounded ASU")
    evidence = DiscoveryEvidence(logical.items[0].represented, source, text="controlled")
    enforcement = EnforcementInputs(True, governed_request.project, governed_request.project, True, True)
    inputs = GovernedRenderInputs(bootstrap, configuration, True, governed_request, universe, (evidence,), ("controlled",),
        (("r9", ApplicabilityInputs(RelevanceOutcome.RELEVANT, "basis", True, enforcement)),), (), "selection",
        (RequiredDeficiency(ident("represented_information", "protected"), "protected", disclosure_denied=True),), False, False, False,
        ident("package", "denied-package-9"), ident("record", "denied-record-9"), "bounded termination", contract(governed_request, ConsumerKind.HUMAN))
    outcome = run_governed_render(inputs)
    assert outcome.construction.package is None and outcome.construction.record.status == "denied"
    assert outcome.rendering.status == "denied" and outcome.rendering.content is None
