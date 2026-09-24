"""Controlled sufficiency, logical-package, coherence, and persistence tests."""
from __future__ import annotations

from pathlib import Path
import shutil
import sqlite3
import tempfile

import pytest

from context_engine.adapters.sqlite_state import SQLiteStateStore
from context_engine.application.lifecycle import ApplicableSourceUniverse, Availability, BoundaryAdequacy, RegisteredSource
from context_engine.application.package_construction import CoherenceInputs, construct_logical_package, evaluate_coherence, persist_construction
from context_engine.application.sufficiency import DiscoveryDeficiency, RequiredDeficiency, SufficiencyInputs, evaluate_sufficiency, plan_bounded_iteration
from context_engine.core.model import CandidateContext, ContextItem, ContextRole, EpistemicState, Provenance, RepresentedInformation, SemanticIdentity, SufficiencyOutcome, Uncertainty


def ident(kind: str, value: str) -> SemanticIdentity:
    return SemanticIdentity(kind, value)


@pytest.fixture
def controlled_dir() -> Path:
    directory = Path(tempfile.mkdtemp(dir=Path.home() / "temp", prefix="context-engine-ws8-"))
    try:
        yield directory
    finally:
        shutil.rmtree(directory)


def item(role: ContextRole = ContextRole.REQUIRED) -> ContextItem:
    provenance = Provenance(ident("provenance", "p"), source=ident("source", "source-a"), observation=ident("observation", "o"))
    represented = RepresentedInformation(ident("represented_information", "r"), ident("claim", "c"), provenance)
    candidate = CandidateContext(ident("request", "request-8"), represented, "deterministic:literal")
    return ContextItem.select(candidate, basis="governed selection", role=role)


def universe(adequacy: BoundaryAdequacy = BoundaryAdequacy.ADEQUATE, availability: Availability = Availability.AVAILABLE) -> ApplicableSourceUniverse:
    return ApplicableSourceUniverse("request-8", (RegisteredSource("source-a", "project-a", "git", "docs", availability),), adequacy, "governed ASU fixture")


def construct(sufficiency, coherence=None):
    selected = (item(),)
    candidate = CandidateContext(selected[0].request, selected[0].represented, "d")
    return construct_logical_package(package_identity=ident("package", "package-8"), request=selected[0].request, selected=selected, candidates=(candidate,), universe=universe(), sufficiency=sufficiency, coherence=coherence or evaluate_coherence(CoherenceInputs()), record_identity=ident("record", "record-8"), termination_basis="bounded governed termination")


def test_adequate_asu_and_required_coverage_can_be_sufficient() -> None:
    decision = evaluate_sufficiency(SufficiencyInputs((item(),), universe()))
    assert decision.outcome is SufficiencyOutcome.SUFFICIENT
    package = construct(decision)
    assert package.package is not None and package.package.sufficiency is SufficiencyOutcome.SUFFICIENT


@pytest.mark.parametrize("adequacy", (BoundaryAdequacy.KNOWN_INCOMPLETE, BoundaryAdequacy.INDETERMINATE))
def test_asu_inadequacy_and_negative_search_do_not_become_sufficient(adequacy: BoundaryAdequacy) -> None:
    insufficient = evaluate_sufficiency(SufficiencyInputs((item(),), universe(adequacy)))
    conditional = evaluate_sufficiency(SufficiencyInputs((item(),), universe(adequacy), bounded_task_safe=True))
    assert insufficient.outcome is SufficiencyOutcome.INSUFFICIENT
    assert conditional.outcome is SufficiencyOutcome.CONDITIONALLY_SUFFICIENT
    assert "asu" in conditional.reason_codes[0]


def test_required_anti_waiver_conditional_and_denied_outcomes() -> None:
    missing = RequiredDeficiency(ident("represented_information", "missing"), "known required decision", limitation=Uncertainty(EpistemicState.UNAVAILABLE, detail="Source unavailable"))
    insufficient = evaluate_sufficiency(SufficiencyInputs((item(),), universe(), (missing,), bounded_task_safe=True))
    bounded = RequiredDeficiency(ident("represented_information", "missing"), "bounded task", can_proceed_bounded_without=True)
    conditional = evaluate_sufficiency(SufficiencyInputs((item(),), universe(), (bounded,), bounded_task_safe=True))
    denied = RequiredDeficiency(ident("represented_information", "protected"), "protected required decision", disclosure_denied=True)
    denial = evaluate_sufficiency(SufficiencyInputs((item(),), universe(), (denied,), bounded_task_safe=True))
    assert insufficient.outcome is SufficiencyOutcome.INSUFFICIENT
    assert conditional.outcome is SufficiencyOutcome.CONDITIONALLY_SUFFICIENT and conditional.required_deficiencies == (bounded,)
    assert denial.outcome is SufficiencyOutcome.DENIED


@pytest.mark.parametrize("availability", (Availability.UNAVAILABLE, Availability.INACCESSIBLE, Availability.UNAUTHORIZED, Availability.UNSUPPORTED, Availability.PARTIAL))
def test_source_failure_qualifications_are_preserved(availability: Availability) -> None:
    decision = evaluate_sufficiency(SufficiencyInputs((item(),), universe(BoundaryAdequacy.KNOWN_INCOMPLETE, availability), bounded_task_safe=True))
    assert decision.outcome is SufficiencyOutcome.CONDITIONALLY_SUFFICIENT
    assert decision.limitations and availability.value in " ".join(entry.detail or "" for entry in decision.limitations)


def test_conflict_uncertainty_and_package_existence_do_not_establish_sufficiency() -> None:
    conflict = evaluate_sufficiency(SufficiencyInputs((item(),), universe(), material_conflict=True))
    uncertainty = evaluate_sufficiency(SufficiencyInputs((item(),), universe(), material_uncertainty=True))
    assert conflict.outcome is SufficiencyOutcome.INSUFFICIENT
    assert uncertainty.outcome is SufficiencyOutcome.INSUFFICIENT
    package = construct(conflict)
    assert package.package is not None and package.package.sufficiency is SufficiencyOutcome.INSUFFICIENT


def test_bounded_iteration_is_explicit_authorized_and_scope_limited() -> None:
    allowed = plan_bounded_iteration(universe(), DiscoveryDeficiency(ident("deficiency", "d"), "known gap", True, True, True, True, ("source-a", "outside")))
    denied = plan_bounded_iteration(universe(), DiscoveryDeficiency(ident("deficiency", "d"), "known gap", True, True, False, True, ("source-a",)))
    assert allowed.authorized_to_discover and allowed.additional_sources == ("source-a",)
    assert not denied.authorized_to_discover and denied.termination_reason == "authorization-or-scope-boundary"


def test_coherence_downgrades_but_never_upgrades_sufficiency() -> None:
    sufficient = evaluate_sufficiency(SufficiencyInputs((item(),), universe()))
    qualified = construct(sufficient, evaluate_coherence(CoherenceInputs(understood_qualified_state=True)))
    incoherent = construct(sufficient, evaluate_coherence(CoherenceInputs(material_governance_changed=True)))
    assert qualified.package is not None and qualified.package.sufficiency is SufficiencyOutcome.CONDITIONALLY_SUFFICIENT
    assert incoherent.package is not None and incoherent.package.sufficiency is SufficiencyOutcome.INSUFFICIENT
    assert evaluate_coherence(CoherenceInputs(compatibility_uncertain=True)).outcome == "uncertain"


def test_denied_construction_is_not_fake_empty_package_and_persistence_is_historical(controlled_dir: Path) -> None:
    denied = evaluate_sufficiency(SufficiencyInputs((item(),), universe(), (RequiredDeficiency(ident("represented_information", "protected"), "protected", disclosure_denied=True),)))
    construction = construct(denied)
    assert construction.package is None and construction.record.status == "denied"
    store = SQLiteStateStore(controlled_dir / "state.sqlite")
    store.initialize()
    persist_construction(store, project_identity="project-a", construction=construction)
    restored = SQLiteStateStore(controlled_dir / "state.sqlite").package_constructions_for_project("project-a")
    assert restored[0].record_identity == "record-8" and restored[0].sufficiency == "denied"
    assert not hasattr(restored[0], "authority") and not hasattr(restored[0], "currentness")


def test_manifest_provenance_and_row_identity_boundary() -> None:
    decision = evaluate_sufficiency(SufficiencyInputs((item(),), universe()))
    construction = construct(decision)
    assert construction.package is not None
    assert construction.package.manifest.entries[0].source.value == "source-a"
    assert construction.record.package == ident("package", "package-8")
    assert not hasattr(construction.package, "rendering") and not hasattr(construction.package, "receipt")


def test_package_construction_schema_migration_and_duplicate_retry_are_explicit(controlled_dir: Path) -> None:
    database = controlled_dir / "version-three.sqlite"
    with sqlite3.connect(database) as connection:
        connection.execute("CREATE TABLE schema_version (version INTEGER NOT NULL)")
        connection.execute("INSERT INTO schema_version VALUES (3)")
    store = SQLiteStateStore(database)
    store.initialize()
    decision = evaluate_sufficiency(SufficiencyInputs((item(),), universe()))
    construction = construct(decision)
    persist_construction(store, project_identity="project-a", construction=construction)
    with pytest.raises(sqlite3.IntegrityError):
        persist_construction(store, project_identity="project-a", construction=construction)
    assert len(store.package_constructions_for_project("project-a")) == 1
