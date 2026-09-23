"""Application orchestration for non-governed runtime prerequisite checks."""

from __future__ import annotations

from dataclasses import dataclass

from context_engine.ports.environment import PrerequisiteCheck, PrerequisiteProbe


@dataclass(frozen=True)
class ReadinessReport:
    """A diagnostic report that establishes no governed semantic state."""

    checks: tuple[PrerequisiteCheck, ...]

    @property
    def ready(self) -> bool:
        return all(check.available for check in self.checks)


def assess_readiness(probe: PrerequisiteProbe) -> ReadinessReport:
    """Collect physical-environment checks through the port."""
    return ReadinessReport(checks=probe.checks())
