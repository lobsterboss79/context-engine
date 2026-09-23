"""Technology-independent contracts required by the Workstream 2 kernel."""

from __future__ import annotations

from typing import Protocol

from context_engine.core.model import (
    ApplicableSourceUniverse, Authority, CandidateContext, Consumer, ContextPackage,
    ContextRequest, ConsumerRendering, PackageConstructionRecord, Project,
    Provenance, Source, SourceManifest, SemanticIdentity,
)


class GovernancePort(Protocol):
    def applicable_authority(self, subject: SemanticIdentity, request: ContextRequest) -> tuple[Authority, ...]: ...


class PersistencePort(Protocol):
    def store_package_record(self, record: PackageConstructionRecord) -> None: ...


class SourceObservationPort(Protocol):
    """Read-oriented observation boundary.

    Implementations receive an already registered, scoped, and authorized
    Source.  They return evidence only; they do not establish governance,
    currentness, relevance, or selection.
    """

    def observe(self, source: Source, request: ContextRequest) -> tuple[Provenance, ...]: ...


class RepresentationPort(Protocol):
    def represent(self, provenance: Provenance) -> tuple[SemanticIdentity, ...]: ...


class DiscoveryPort(Protocol):
    def discover(self, request: ContextRequest, universe: ApplicableSourceUniverse) -> tuple[CandidateContext, ...]: ...


class AuthorizationPort(Protocol):
    def may_disclose(self, subject: SemanticIdentity, consumer: Consumer, request: ContextRequest) -> bool: ...


class PackageConstructionPort(Protocol):
    def construct(self, request: ContextRequest) -> ContextPackage: ...


class RenderingPort(Protocol):
    def render(self, package: ContextPackage, consumer: Consumer) -> ConsumerRendering: ...


class DiagnosticsPort(Protocol):
    def record_limitation(self, request: ContextRequest, detail: str) -> None: ...


class BackupRecoveryPort(Protocol):
    def recover(self, project: Project) -> None: ...


class ClockPort(Protocol):
    def now_reference(self) -> str: ...


class IdentityPort(Protocol):
    def resolve(self, reference: str) -> SemanticIdentity | None: ...
