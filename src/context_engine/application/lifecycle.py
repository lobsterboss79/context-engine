"""Governed Project and Source lifecycle representations for Workstream 4.

This module has no observation, discovery, selection, or sufficiency behavior.
It retains the preconditions and evidence distinctions those later workstreams
must consume without treating registration or access as a semantic elevation.
"""
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


class Availability(str, Enum):
    """Bounded lifecycle/inspection conditions; none implies universal absence."""

    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    INACCESSIBLE = "inaccessible"
    UNAUTHORIZED = "unauthorized"
    UNSUPPORTED = "unsupported"
    PARTIAL = "partial"
    ABSENT = "absent"
    NOT_INSPECTED = "not_inspected"


class BoundaryAdequacy(str, Enum):
    """Evidence boundary for an ASU determination, not a discovery outcome."""

    ADEQUATE = "adequate"
    KNOWN_INCOMPLETE = "known_incomplete"
    INDETERMINATE = "indeterminate"


@dataclass(frozen=True)
class RegisteredSource:
    """A Project-scoped registration with semantic, not physical, identity.

    Registration deliberately contains no Authority, Governance State,
    currentness, applicability, selection, or disclosure assertion.
    """

    identity: str
    project: str
    source_type: str
    scope: str
    availability: Availability = Availability.NOT_INSPECTED
    locator: str | None = None

    def __post_init__(self) -> None:
        if not all((self.identity, self.project, self.source_type, self.scope)):
            raise ValueError("a registered Source requires identity, Project, type, and scope")


@dataclass(frozen=True)
class ScopeInputs:
    """Explicit prerequisites for a bounded external Project scope expansion."""

    task_requires_external: bool = False
    governed_relationship: bool = False
    requester_authorized: bool = False
    consumer_disclosure_authorized: bool = False

    @property
    def permits_cross_project(self) -> bool:
        """Return only an explicitly governed, task-relevant, dual-authorized path."""

        return (
            self.task_requires_external
            and self.governed_relationship
            and self.requester_authorized
            and self.consumer_disclosure_authorized
        )


def effective_sources(
    primary_project: str,
    sources: tuple[RegisteredSource, ...],
    inputs: ScopeInputs,
) -> tuple[RegisteredSource, ...]:
    """Calculate bounded lifecycle scope without discovering or selecting.

    Relationships themselves do not transfer Authority, Governance State, or
    currentness. The local Project remains the default.
    """

    local = tuple(source for source in sources if source.project == primary_project)
    if not inputs.permits_cross_project:
        return local
    return sources


@dataclass(frozen=True)
class ApplicableSourceUniverse:
    """A request-scoped Source boundary plus its establishment evidence."""

    request_reference: str
    sources: tuple[RegisteredSource, ...]
    adequacy: BoundaryAdequacy
    basis: str

    def __post_init__(self) -> None:
        if not self.request_reference or not self.basis:
            raise ValueError("ASU requires a request reference and establishment basis")
