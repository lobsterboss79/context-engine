"""Deterministic fixtures for Workstream 1 tests only."""

from __future__ import annotations

import pytest

from context_engine.ports.environment import PrerequisiteCheck


@pytest.fixture
def ready_checks() -> tuple[PrerequisiteCheck, ...]:
    """Return a stable prerequisite result without inspecting the test host."""
    return (
        PrerequisiteCheck("cpython-3.14", True, "CPython"),
        PrerequisiteCheck("linux-x86-64", True, "Linux"),
        PrerequisiteCheck("ordinary-non-root", True, "process privilege check"),
        PrerequisiteCheck("git-cli", True, "git executable check"),
    )
