"""Logical package construction and deterministic coherence for Workstream 8."""
from __future__ import annotations

from dataclasses import dataclass
import json

from context_engine.application.lifecycle import ApplicableSourceUniverse
from context_engine.application.sufficiency import SufficiencyDecision
from context_engine.core.model import (
    ApplicableSourceUniverse as CoreApplicableSourceUniverse, CandidateContext, ConstructionState, ContextItem, ContextPackage,
    PackageConstructionRecord, SemanticIdentity, SourceManifest, SourceManifestEntry,
    SufficiencyOutcome, Uncertainty,
)
from context_engine.adapters.sqlite_state import PersistedPackageConstruction, SQLiteStateStore


@dataclass(frozen=True)
class CoherenceInputs:
    material_source_changed: bool = False
    material_governance_changed: bool = False
    material_authorization_changed: bool = False
    material_scope_changed: bool = False
    material_boundary_changed: bool = False
    compatibility_uncertain: bool = False
    understood_qualified_state: bool = False
    basis: str = "explicit construction-state comparison"


def evaluate_coherence(inputs: CoherenceInputs) -> ConstructionState:
    if any((inputs.material_source_changed, inputs.material_governance_changed, inputs.material_authorization_changed, inputs.material_scope_changed, inputs.material_boundary_changed)):
        return ConstructionState("incoherent", inputs.basis)
    if inputs.compatibility_uncertain:
        return ConstructionState("uncertain", inputs.basis)
    if inputs.understood_qualified_state:
        return ConstructionState("coherent_with_qualification", inputs.basis)
    return ConstructionState("coherent", inputs.basis)


@dataclass(frozen=True)
class PackageConstruction:
    package: ContextPackage | None
    record: PackageConstructionRecord


def construct_logical_package(
    *, package_identity: SemanticIdentity, request: SemanticIdentity,
    selected: tuple[ContextItem, ...], candidates: tuple[CandidateContext, ...],
    universe: ApplicableSourceUniverse, sufficiency: SufficiencyDecision,
    coherence: ConstructionState, record_identity: SemanticIdentity,
    termination_basis: str,
) -> PackageConstruction:
    """Construct an authorized logical package, never a rendering/delivery.

    Denied construction returns a durable denied attempt with no manufactured
    empty package.  Incoherence can downgrade, never upgrade, sufficiency.
    """
    outcome = _coherent_outcome(sufficiency.outcome, coherence)
    limitations = sufficiency.limitations
    core_universe = CoreApplicableSourceUniverse(
        tuple(SemanticIdentity("source", source.identity) for source in universe.sources),
        limitations[0] if limitations else None,
    )
    if outcome is SufficiencyOutcome.DENIED:
        record = PackageConstructionRecord(record_identity, request, None, core_universe, candidates, outcome, coherence, limitations, "denied", termination_basis)
        return PackageConstruction(None, record)
    manifest = _manifest(selected)
    package = ContextPackage(package_identity, request, selected, manifest, outcome, coherence, limitations)
    status = "completed" if coherence.outcome in {"coherent", "coherent_with_qualification"} else "partial"
    record = PackageConstructionRecord(record_identity, request, package.identity, core_universe, candidates, outcome, coherence, limitations, status, termination_basis)
    return PackageConstruction(package, record)


def _coherent_outcome(outcome: SufficiencyOutcome, coherence: ConstructionState) -> SufficiencyOutcome:
    if outcome is SufficiencyOutcome.SUFFICIENT and coherence.outcome in {"incoherent", "uncertain", "coherent_with_qualification"}:
        return SufficiencyOutcome.CONDITIONALLY_SUFFICIENT if coherence.outcome == "coherent_with_qualification" else SufficiencyOutcome.INSUFFICIENT
    return outcome


def _manifest(items: tuple[ContextItem, ...]) -> SourceManifest:
    entries: dict[str, SourceManifestEntry] = {}
    for item in items:
        provenance = item.represented.provenance
        if provenance.source is None:
            continue
        entries[provenance.source.value] = SourceManifestEntry(provenance.source, observation=provenance.observation, contributed=True, limitations=item.represented.uncertainty + provenance.limitations + item.limitations)
    return SourceManifest(tuple(entries[key] for key in sorted(entries)))


def persist_construction(store: SQLiteStateStore, *, project_identity: str, construction: PackageConstruction) -> None:
    """Persist a completed/partial/denied construction atomically as history."""
    record = construction.record
    store.save_package_construction(PersistedPackageConstruction(
        project_identity, record.identity.value, record.request.value,
        record.package.value if record.package else None, record.status,
        record.outcome.value if record.outcome else None,
        record.coherence.outcome if record.coherence else None,
        json.dumps({"limitations": [item.state.value for item in record.limitations],
                    "sources": [item.value for item in record.source_universe.sources],
                    "candidates": [item.represented.identity.value for item in record.candidates],
                    "termination_basis": record.termination_basis}, sort_keys=True),
    ))
