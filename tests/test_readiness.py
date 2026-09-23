"""Tests for the non-governed Workstream 1 readiness path."""

from __future__ import annotations

from context_engine.application.readiness import assess_readiness
from context_engine.ports.environment import PrerequisiteCheck


class StaticProbe:
    def __init__(self, checks: tuple[PrerequisiteCheck, ...]) -> None:
        self._checks = checks

    def checks(self) -> tuple[PrerequisiteCheck, ...]:
        return self._checks


def test_readiness_is_ready_when_all_prerequisites_are_available(ready_checks: tuple[PrerequisiteCheck, ...]) -> None:
    assert assess_readiness(StaticProbe(ready_checks)).ready


def test_readiness_reports_unavailable_prerequisite(ready_checks: tuple[PrerequisiteCheck, ...]) -> None:
    unavailable = (*ready_checks[:-1], PrerequisiteCheck("git-cli", False, "git executable check"))
    assert not assess_readiness(StaticProbe(unavailable)).ready
