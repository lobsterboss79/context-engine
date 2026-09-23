"""Tests for framework-free CLI parsing and safe output."""

from __future__ import annotations

import json

from context_engine import cli
from context_engine.application.readiness import ReadinessReport
from context_engine.ports.environment import PrerequisiteCheck


def test_readiness_json_is_deterministic(monkeypatch) -> None:
    report = ReadinessReport((PrerequisiteCheck("git-cli", True, "git executable check"),))
    monkeypatch.setattr(cli, "assess_readiness", lambda probe: report)

    assert cli.main(["readiness", "--format", "json"]) == 0


def test_readiness_json_output_contains_no_host_path(monkeypatch, capsys) -> None:
    report = ReadinessReport((PrerequisiteCheck("git-cli", False, "git executable check"),))
    monkeypatch.setattr(cli, "assess_readiness", lambda probe: report)

    assert cli.main(["readiness", "--format", "json"]) == 2
    payload = json.loads(capsys.readouterr().out)
    assert payload == {
        "checks": [{"available": False, "detail": "git executable check", "name": "git-cli"}],
        "status": "not_ready",
    }
