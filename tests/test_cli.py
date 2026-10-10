"""Tests for framework-free CLI parsing and safe output."""

from __future__ import annotations

import json
from pathlib import Path

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


def _identity(kind: str, value: str) -> dict[str, str]:
    return {"kind": kind, "value": value}


def _render_input(directory: Path, *, operator_authorized: bool = True, disclosure_authorized: bool = True) -> dict[str, object]:
    bootstrap = directory / "bootstrap.toml"
    project = directory / "project.toml"
    bootstrap.write_text(
        'version = 1\n[bootstrap]\nproject = "project-cli"\nscope = "controlled"\ngovernance_basis = "fixture"\nproject_configuration = "project.toml"\n',
        encoding="utf-8",
    )
    project.write_text('version = 1\n[project]\nidentity = "project-cli"\ngovernance_reference = "fixture"\n', encoding="utf-8")
    request = _identity("request", "request-cli")
    project_id = _identity("project", "project-cli")
    represented = _identity("represented_information", "represented-cli")
    subject = _identity("claim", "claim-cli")
    source = _identity("source", "source-cli")
    provenance = {
        "identity": _identity("provenance", "provenance-cli"), "origin_projects": [], "source": source,
        "artifact": _identity("artifact", "artifact-cli"), "artifact_version": _identity("artifact_version", "artifact-version-cli"),
        "observation": _identity("observation", "observation-cli"), "upstream": [], "transformation": "direct",
        "missing_material_basis": False, "location_reference": "fixture.md:1", "transformation_reference": None, "limitations": [],
    }
    enforcement = {
        "bootstrap_valid": True, "request_project": project_id, "candidate_project": project_id,
        "requester_authorized": True, "consumer_disclosure_authorized": disclosure_authorized,
        "protected_metadata_authorized": True, "task_requires_current": False, "task_is_historical": False,
        "task_domain": None, "task_phase": None, "task_action": None, "requires_governing_authority": False,
        "instructional_use_requested": False, "instructional_authority_established": False, "cross_project_prerequisites": False,
    }
    return {
        "version": 1, "bootstrap_reference": "bootstrap.toml", "project_configuration_reference": "project.toml",
        "operator_authorized": operator_authorized,
        "request": {
            "identity": request, "project": project_id, "requester": _identity("requester", "owner-cli"),
            "consumer": _identity("consumer", "consumer-cli"),
            "intent": {"purpose": "controlled CLI rendering", "inferred": False, "uncertainty": None},
            "scope": {"description": "controlled scope"}, "constraints": ["preserve governed boundaries"],
        },
        "universe": {
            "request_reference": "request-cli", "sources": [{"identity": "source-cli", "project": "project-cli", "source_type": "markdown", "scope": "fixture", "availability": "available", "locator": None}],
            "adequacy": "adequate", "basis": "controlled fixture",
        },
        "evidence": [{
            "represented": {"identity": represented, "subject": subject, "provenance": provenance, "classifications": [{"name": "controlled", "provenance": None}], "uncertainty": [],
                            "assertion_content": "Fixture assertion remains evidence.", "authority_basis": "fixture", "currentness_basis": "fixture", "governance_basis": "fixture"},
            "source_identity": "source-cli", "text": "controlled CLI rendering", "markdown_kinds": [], "metadata": [], "relationships": [], "authorities": [], "governance": [], "currentness": [], "conflicts": [], "local_history": [], "limitations": [], "expansion_only": False,
        }],
        "query_terms": ["controlled"],
        "applicability": [{"represented_identity": "represented-cli", "relevance": "relevant", "relevance_basis": "controlled explicit relevance", "scope_matches_task": True, "enforcement": enforcement}],
        "role_inputs": [{"represented_identity": "represented-cli", "omission_risks_incorrect_performance": True, "omission_risks_improper_performance": False, "materially_improves_understanding_or_validation": True, "basis": "controlled counterfactual", "consumer_capacity_limited": False, "rendering_limited": False}],
        "selection_basis": "controlled governed selection", "sufficiency_deficiencies": [], "material_conflict": False, "material_uncertainty": False, "bounded_task_safe": False,
        "package_identity": _identity("package", "package-cli"), "record_identity": _identity("record", "record-cli"), "termination_basis": "controlled termination",
        "contract": {"kind": "chatgpt", "consumer": _identity("consumer", "consumer-cli"), "disclosure_authorized": disclosure_authorized, "capacity_characters": None},
        "scope_inputs": {"task_requires_external": False, "governed_relationship": False, "requester_authorized": False, "consumer_disclosure_authorized": False},
        "expansions": [],
        "coherence_inputs": {"material_source_changed": False, "material_governance_changed": False, "material_authorization_changed": False, "material_scope_changed": False, "material_boundary_changed": False, "compatibility_uncertain": False, "understood_qualified_state": False, "basis": "controlled coherence"},
        "construction_qualifications": [],
    }


def _write_input(directory: Path, **kwargs) -> Path:
    path = directory / "render-input.json"
    path.write_text(json.dumps(_render_input(directory, **kwargs), sort_keys=True), encoding="utf-8")
    return path


def test_render_accepts_explicit_validated_input_and_is_deterministic(tmp_path: Path, capsys) -> None:
    input_path = _write_input(tmp_path)
    first = tmp_path / "first.txt"
    second = tmp_path / "second.txt"

    assert cli.main(["render", "--input", str(input_path), "--output", str(first)]) == 0
    first_summary = json.loads(capsys.readouterr().out)
    assert first_summary["status"] == "rendered"
    assert first_summary["selected_context_items"] == 1
    assert cli.main(["render", "--input", str(input_path), "--output", str(second)]) == 0
    assert first.read_bytes() == second.read_bytes()
    assert "Fixture assertion remains evidence." in first.read_text(encoding="utf-8")


def test_render_fails_closed_for_missing_role_and_leaves_no_output(tmp_path: Path, capsys) -> None:
    input_path = _write_input(tmp_path)
    data = json.loads(input_path.read_text(encoding="utf-8"))
    data["role_inputs"] = []
    input_path.write_text(json.dumps(data), encoding="utf-8")
    output = tmp_path / "not-created.txt"

    assert cli.main(["render", "--input", str(input_path), "--output", str(output)]) == 2
    assert "role_inputs must cover exactly" in capsys.readouterr().err
    assert not output.exists()


def test_render_rejects_unexpected_input_fields_without_output(tmp_path: Path, capsys) -> None:
    input_path = _write_input(tmp_path)
    data = json.loads(input_path.read_text(encoding="utf-8"))
    data["unexpected"] = True
    input_path.write_text(json.dumps(data), encoding="utf-8")
    output = tmp_path / "not-created.txt"

    assert cli.main(["render", "--input", str(input_path), "--output", str(output)]) == 2
    assert "root keys invalid" in capsys.readouterr().err
    assert not output.exists()


def test_render_enforces_bootstrap_and_consumer_disclosure_without_partial_output(tmp_path: Path, capsys) -> None:
    output = tmp_path / "not-created.txt"
    unauthorized_bootstrap = _write_input(tmp_path, operator_authorized=False)
    assert cli.main(["render", "--input", str(unauthorized_bootstrap), "--output", str(output)]) == 2
    assert "operator is not authorized" in capsys.readouterr().err
    assert not output.exists()

    unauthorized_disclosure = _write_input(tmp_path, disclosure_authorized=False)
    assert cli.main(["render", "--input", str(unauthorized_disclosure), "--output", str(output)]) == 2
    assert "consumer-disclosure-authorization-not-established" in capsys.readouterr().err
    assert not output.exists()


def test_render_never_overwrites_an_existing_output(tmp_path: Path, capsys) -> None:
    input_path = _write_input(tmp_path)
    output = tmp_path / "existing.txt"
    output.write_text("preserve", encoding="utf-8")

    assert cli.main(["render", "--input", str(input_path), "--output", str(output)]) == 2
    assert "already exists" in capsys.readouterr().err
    assert output.read_text(encoding="utf-8") == "preserve"


def test_bootstrap_validate_remains_available(tmp_path: Path, capsys) -> None:
    _render_input(tmp_path)

    assert cli.main([
        "bootstrap-validate", "--bootstrap", str(tmp_path / "bootstrap.toml"),
        "--project-configuration", str(tmp_path / "project.toml"),
    ]) == 0
    assert json.loads(capsys.readouterr().out)["status"] == "validated"
