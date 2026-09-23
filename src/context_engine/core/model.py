"""Technology-independent governed semantic representations for Workstream 2.

These types record semantic assertions and their governed qualifications.  They
perform no observation, parsing, identity resolution, discovery, applicability,
selection policy, sufficiency evaluation, rendering, or persistence.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import NewType


class SemanticInvariantError(ValueError):
    """Raised when construction would collapse governed semantic distinctions."""


@dataclass(frozen=True)
class SemanticIdentity:
    """An explicitly supplied logical identity, never derived from a locator."""

    kind: str
    value: str

    def __post_init__(self) -> None:
        if not self.kind or not self.value:
            raise SemanticInvariantError("semantic identities require kind and value")


@dataclass(frozen=True)
class Project:
    identity: SemanticIdentity
    registration_reference: str | None = None
    governance_reference: str | None = None
    provenance: "Provenance | None" = None

    def __post_init__(self) -> None:
        if self.identity.kind != "project":
            raise SemanticInvariantError("Project requires a project semantic identity")


@dataclass(frozen=True)
class SourceScope:
    identity: SemanticIdentity
    source: SemanticIdentity
    governed_meaning: str
    provenance: "Provenance | None" = None


@dataclass(frozen=True)
class Source:
    identity: SemanticIdentity
    project: SemanticIdentity
    source_type: str
    locators: tuple[str, ...] = ()
    scopes: tuple[SourceScope, ...] = ()
    provenance: "Provenance | None" = None

    def __post_init__(self) -> None:
        if self.identity.kind != "source" or self.project.kind != "project":
            raise SemanticInvariantError("Source must identify a Source and Project")
        if any(scope.source != self.identity for scope in self.scopes):
            raise SemanticInvariantError("Source Scope must belong to its Source")


@dataclass(frozen=True)
class Artifact:
    identity: SemanticIdentity
    source: SemanticIdentity
    locators: tuple[str, ...] = ()


@dataclass(frozen=True)
class ArtifactVersion:
    identity: SemanticIdentity
    artifact: SemanticIdentity
    native_state_reference: str | None = None
    provenance: "Provenance | None" = None


@dataclass(frozen=True)
class ObservedState:
    """An observation record; it is neither a version nor a currentness claim."""

    identity: SemanticIdentity
    source: SemanticIdentity
    observed_reference: str | None = None
    observed_versions: tuple[SemanticIdentity, ...] = ()
    observation_time: str | None = None


class TransformationKind(str, Enum):
    DIRECT = "direct"
    NORMALIZED = "normalized"
    SUMMARIZED = "summarized"
    INFERRED = "inferred"
    PROPOSED = "proposed"


@dataclass(frozen=True)
class Provenance:
    identity: SemanticIdentity
    origin_projects: tuple[SemanticIdentity, ...] = ()
    source: SemanticIdentity | None = None
    artifact: SemanticIdentity | None = None
    artifact_version: SemanticIdentity | None = None
    observation: SemanticIdentity | None = None
    upstream: tuple[SemanticIdentity, ...] = ()
    transformation: TransformationKind = TransformationKind.DIRECT
    missing_material_basis: bool = False


@dataclass(frozen=True)
class Claim:
    """A semantic assertion; its identity excludes locator and governed status."""

    identity: SemanticIdentity
    assertion_reference: str
    provenance: Provenance


@dataclass(frozen=True)
class Classification:
    name: str
    provenance: Provenance | None = None


@dataclass(frozen=True)
class Relationship:
    identity: SemanticIdentity
    kind: str
    source: SemanticIdentity
    target: SemanticIdentity
    scope: str | None = None
    provenance: Provenance | None = None
    inferred: bool = False


@dataclass(frozen=True)
class AuthorityScope:
    project: SemanticIdentity | None = None
    domains: tuple[str, ...] = ()
    phases: tuple[str, ...] = ()
    actions: tuple[str, ...] = ()
    subject: str | None = None
    temporal_scope: str | None = None
    unknown: bool = False

    def __post_init__(self) -> None:
        if self.unknown and any((self.project, self.domains, self.phases, self.actions, self.subject, self.temporal_scope)):
            raise SemanticInvariantError("unknown Authority Scope is not unrestricted scope")


@dataclass(frozen=True)
class Authority:
    identity: SemanticIdentity
    basis: str
    scope: AuthorityScope
    provenance: Provenance
    delegation_basis: tuple[SemanticIdentity, ...] = ()


class GovernanceState(str, Enum):
    PROPOSED = "proposed"
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    WITHDRAWN = "withdrawn"
    SUPERSEDED = "superseded"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class GovernanceAssessment:
    subject: SemanticIdentity
    state: GovernanceState
    provenance: Provenance | None = None


@dataclass(frozen=True)
class CandidateProposal:
    identity: SemanticIdentity
    represented: SemanticIdentity
    provenance: Provenance


class Currentness(str, Enum):
    CURRENT = "current"
    HISTORICAL = "historical"
    SUPERSEDED = "superseded"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class TemporalContext:
    event_time: str | None = None
    effective_time: str | None = None
    version_time: str | None = None
    observation_time: str | None = None
    construction_time: str | None = None


@dataclass(frozen=True)
class CurrentnessAssessment:
    subject: SemanticIdentity
    currentness: Currentness = Currentness.UNKNOWN
    basis: tuple[SemanticIdentity, ...] = ()
    temporal: TemporalContext = field(default_factory=TemporalContext)


@dataclass(frozen=True)
class Supersession:
    prior: SemanticIdentity
    replacement: SemanticIdentity
    scope: str
    provenance: Provenance
    established: bool = False


@dataclass(frozen=True)
class Conflict:
    identity: SemanticIdentity
    participants: tuple[SemanticIdentity, ...]
    scope: str
    provenance: Provenance
    resolved_by: SemanticIdentity | None = None

    def __post_init__(self) -> None:
        if len(self.participants) < 2:
            raise SemanticInvariantError("Conflict requires materially incompatible participants")


class EpistemicState(str, Enum):
    UNKNOWN = "unknown"
    MISSING = "missing"
    UNAVAILABLE = "unavailable"
    UNAUTHORIZED = "unauthorized"
    AMBIGUOUS = "ambiguous"
    UNRESOLVED_CONFLICT = "unresolved_conflict"
    UNVERIFIED = "unverified"
    INFERRED = "inferred"
    PROPOSED = "proposed"


@dataclass(frozen=True)
class Uncertainty:
    state: EpistemicState
    evidence_boundary: str | None = None
    detail: str | None = None

    def __post_init__(self) -> None:
        if self.state is EpistemicState.MISSING and not self.evidence_boundary:
            raise SemanticInvariantError("Missingness requires an evidence boundary")


RequesterId = NewType("RequesterId", SemanticIdentity)
ConsumerId = NewType("ConsumerId", SemanticIdentity)


@dataclass(frozen=True)
class Requester:
    identity: RequesterId


@dataclass(frozen=True)
class Consumer:
    identity: ConsumerId


@dataclass(frozen=True)
class TaskIntent:
    purpose: str
    inferred: bool = False
    uncertainty: Uncertainty | None = None


@dataclass(frozen=True)
class TaskScope:
    description: str


@dataclass(frozen=True)
class ContextRequest:
    identity: SemanticIdentity
    project: SemanticIdentity
    requester: Requester
    consumer: Consumer
    intent: TaskIntent
    scope: TaskScope
    constraints: tuple[str, ...] = ()


@dataclass(frozen=True)
class RepresentedInformation:
    """Information represented in the core, before task-relative discovery."""

    identity: SemanticIdentity
    subject: SemanticIdentity
    provenance: Provenance
    classifications: tuple[Classification, ...] = ()
    uncertainty: tuple[Uncertainty, ...] = ()


@dataclass(frozen=True)
class CandidateContext:
    request: SemanticIdentity
    represented: RepresentedInformation
    discovery_basis: str


class ContextRole(str, Enum):
    REQUIRED = "required"
    SUPPORTING = "supporting"


@dataclass(frozen=True)
class _SelectionSeal:
    candidate: CandidateContext
    basis: str


@dataclass(frozen=True, init=False)
class ContextItem:
    request: SemanticIdentity
    represented: RepresentedInformation
    selection_basis: str
    role: ContextRole

    def __init__(self, seal: _SelectionSeal, role: ContextRole) -> None:
        if not isinstance(seal, _SelectionSeal):
            raise SemanticInvariantError("Context Item requires the selection construction path")
        object.__setattr__(self, "request", seal.candidate.request)
        object.__setattr__(self, "represented", seal.candidate.represented)
        object.__setattr__(self, "selection_basis", seal.basis)
        object.__setattr__(self, "role", role)

    @classmethod
    def select(cls, candidate: CandidateContext, *, basis: str, role: ContextRole) -> "ContextItem":
        if not basis:
            raise SemanticInvariantError("selection requires an explicit governed basis")
        return cls(_SelectionSeal(candidate, basis), role)


class SufficiencyOutcome(str, Enum):
    SUFFICIENT = "sufficient"
    CONDITIONALLY_SUFFICIENT = "conditionally_sufficient"
    INSUFFICIENT = "insufficient"


@dataclass(frozen=True)
class ApplicableSourceUniverse:
    sources: tuple[SemanticIdentity, ...]
    adequacy: Uncertainty | None = None


@dataclass(frozen=True)
class SourceManifestEntry:
    source: SemanticIdentity
    scope: SemanticIdentity | None = None
    observation: SemanticIdentity | None = None
    contributed: bool = False
    limitations: tuple[Uncertainty, ...] = ()


@dataclass(frozen=True)
class SourceManifest:
    entries: tuple[SourceManifestEntry, ...]


@dataclass(frozen=True)
class ConstructionState:
    outcome: str
    basis: str


@dataclass(frozen=True)
class ContextPackage:
    identity: SemanticIdentity
    request: SemanticIdentity
    items: tuple[ContextItem, ...]
    manifest: SourceManifest
    sufficiency: SufficiencyOutcome
    coherence: ConstructionState
    limitations: tuple[Uncertainty, ...] = ()

    def __post_init__(self) -> None:
        if any(item.request != self.request for item in self.items):
            raise SemanticInvariantError("Context Package items must belong to its Context Request")
        if self.sufficiency is SufficiencyOutcome.SUFFICIENT and self.coherence.outcome in {"incoherent", "uncertain"}:
            raise SemanticInvariantError("material incoherence precludes unqualified sufficiency")


@dataclass(frozen=True)
class PackageConstructionRecord:
    identity: SemanticIdentity
    request: SemanticIdentity
    package: SemanticIdentity | None
    source_universe: ApplicableSourceUniverse
    candidates: tuple[CandidateContext, ...]
    outcome: SufficiencyOutcome | None
    coherence: ConstructionState | None
    limitations: tuple[Uncertainty, ...] = ()


@dataclass(frozen=True)
class ConsumerRendering:
    package: SemanticIdentity
    consumer: Consumer
    representation_reference: str


@dataclass(frozen=True)
class DeliveryAttempt:
    rendering: ConsumerRendering
    destination_reference: str


@dataclass(frozen=True)
class ConsumerReceipt:
    delivery: DeliveryAttempt
    received_reference: str


@dataclass(frozen=True)
class ConsumerUse:
    receipt: ConsumerReceipt
    use_reference: str
