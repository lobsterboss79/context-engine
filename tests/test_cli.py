"""Tests for framework-free CLI parsing and safe output."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from context_engine import cli
from context_engine.application.local_context import _markdown_candidates
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


def _local_repository(directory: Path) -> Path:
    repo = directory / "candidate-repository"
    repo.mkdir()
    import subprocess
    for arguments in (("init",), ("config", "user.email", "test@example.invalid"), ("config", "user.name", "Test")):
        subprocess.run(("git", "-C", str(repo), *arguments), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (repo / "README.md").write_text("# Phase 3\n\nContinue implementation safely.\n", encoding="utf-8")
    (repo / "notes.md").write_text("# Other\n\nUnrelated text.\n", encoding="utf-8")
    subprocess.run(("git", "-C", str(repo), "add", "."), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(("git", "-C", str(repo), "commit", "-m", "fixture"), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return repo


def test_context_requires_explicit_local_authorization(tmp_path: Path, capsys) -> None:
    repo = _local_repository(tmp_path)
    assert cli.main(["context", "--project", str(repo), "--task", "continue phase 3"]) == 2
    assert "authorization is required" in capsys.readouterr().err


def test_context_writes_deterministic_qualified_markdown_candidates(tmp_path: Path, capsys) -> None:
    repo = _local_repository(tmp_path)
    first, second = tmp_path / "first.json", tmp_path / "second.json"
    arguments = ["context", "--project", str(repo), "--task", "Continue Phase 3 implementation", "--authorize-local-inspection"]
    assert cli.main([*arguments, "--output", str(first)]) == 0
    assert cli.main([*arguments, "--output", str(second)]) == 0
    one, two = json.loads(first.read_text()), json.loads(second.read_text())
    assert one["status"] == "candidate_context"
    assert one["unverified_markdown_candidates"] == two["unverified_markdown_candidates"]
    assert one["verified_semantic_evidence"] == []
    assert one["discovery_diagnostics"] == two["discovery_diagnostics"]
    assert one["discovery_diagnostics"] == {
        "total_matches": 2, "returned_candidates": 2, "excluded_by_limit": 0,
        "distinct_source_documents": 1, "truncated": False, "candidate_limit": 64,
    }
    candidate = one["unverified_markdown_candidates"][0]
    assert candidate["content_status"] == "unverified_markdown_structure_inert_data"
    assert "applicability" in " ".join(one["limitations"])


def test_context_rejects_non_root_and_never_overwrites_output(tmp_path: Path, capsys) -> None:
    repo = _local_repository(tmp_path)
    assert cli.main(["context", "--project", str(repo / "README.md"), "--task", "phase", "--authorize-local-inspection"]) == 2
    assert "repository" in capsys.readouterr().err
    output = tmp_path / "existing.json"
    output.write_text("preserve", encoding="utf-8")
    assert cli.main(["context", "--project", str(repo), "--task", "phase", "--authorize-local-inspection", "--output", str(output)]) == 2
    assert output.read_text(encoding="utf-8") == "preserve"


def test_context_reuses_only_current_validated_semantic_record_with_provenance(tmp_path: Path, capsys) -> None:
    repo = _local_repository(tmp_path)
    import hashlib
    import subprocess
    artifact = repo / "semantic-source.md"
    artifact.write_text("Semantic context.\n", encoding="utf-8")
    subprocess.run(("git", "-C", str(repo), "add", "semantic-source.md"), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(("git", "-C", str(repo), "commit", "-m", "semantic source"), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    head = subprocess.run(("git", "-C", str(repo), "rev-parse", "HEAD"), check=True, stdout=subprocess.PIPE).stdout.decode().strip()
    records = repo / "docs" / "project" / "semantic-records"
    records.mkdir(parents=True)
    record = {
        "identity": "record-cli", "version": "v1", "claim_identity": "claim-cli", "assertion_reference": "assertion-cli",
        "assertion": "Validated semantic assertion.", "source_identity": "source-cli", "project_identity": "candidate-repository",
        "artifact_locator": "semantic-source.md", "source_revision": head,
        "source_sha256": hashlib.sha256(artifact.read_bytes()).hexdigest(), "observation_identity": "observation-cli",
        "block_ordinal": 0, "line_start": 1, "line_end": 1, "authoring_process": "fixture",
    }
    v1 = records / "record-v1.json"
    v2 = records / "record-v2.json"
    v1.write_text(json.dumps(record), encoding="utf-8")
    v2_record = record | {"version": "v2", "line_start": 1, "line_end": 1}
    v2.write_text(json.dumps(v2_record), encoding="utf-8")
    from context_engine.adapters.sqlite_state import PersistedSemanticRecordSupersession, semantic_record_supersession_sha256
    v1_hash = hashlib.sha256(v1.read_bytes()).hexdigest()
    v2_hash = hashlib.sha256(v2.read_bytes()).hexdigest()
    relation = PersistedSemanticRecordSupersession("candidate-repository", "record-v1-to-v2", "v1", "pending", "record-cli", "v1", v1_hash, "record-cli", "v2", v2_hash,
                                                   "provenance_correction", "fixture", "fixture")
    relation = PersistedSemanticRecordSupersession(**(relation.__dict__ | {"relation_sha256": semantic_record_supersession_sha256(relation)}))
    lifecycle = records / "lifecycle"
    lifecycle.mkdir()
    (lifecycle / "v1-to-v2.json").write_text(json.dumps(relation.__dict__, sort_keys=True, separators=(",", ":")), encoding="utf-8")
    (repo / "notes.md").write_text("# Other\n\nLater unrelated change.\n", encoding="utf-8")
    subprocess.run(("git", "-C", str(repo), "add", "notes.md"), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(("git", "-C", str(repo), "commit", "-m", "later unrelated change"), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = tmp_path / "context.json"
    assert cli.main(["context", "--project", str(repo), "--task", "semantic", "--authorize-local-inspection", "--output", str(output)]) == 0
    evidence = json.loads(output.read_text())["verified_semantic_evidence"]
    assert evidence[0]["assertion_content"] == "Validated semantic assertion."
    assert evidence[0]["content_status"] == "validated_semantic_record_evidence_bound_to_recorded_revision_not_currentness_or_authority"
    assert evidence[0]["provenance"] == "semantic-source.md"
    assert evidence[0]["source_revision"] == head
    assert evidence[0]["source_sha256"] == hashlib.sha256(artifact.read_bytes()).hexdigest()
    assert evidence[0]["semantic_record"] == "record-cli:v2"
    invalid_relation = json.loads((lifecycle / "v1-to-v2.json").read_text()) | {"relation_sha256": "0" * 64}
    (lifecycle / "v1-to-v2.json").write_text(json.dumps(invalid_relation), encoding="utf-8")
    invalid_output = tmp_path / "invalid-lifecycle.json"
    assert cli.main(["context", "--project", str(repo), "--task", "semantic", "--authorize-local-inspection", "--output", str(invalid_output)]) == 0
    invalid_payload = json.loads(invalid_output.read_text())
    assert invalid_payload["verified_semantic_evidence"] == []
    assert any("lifecycle relation" in value for value in invalid_payload["limitations"])


def test_context_rejects_semantic_record_when_bound_source_bytes_change(tmp_path: Path) -> None:
    repo = _local_repository(tmp_path)
    import hashlib
    import subprocess
    artifact = repo / "semantic-source.md"
    artifact.write_text("Original semantic context.\n", encoding="utf-8")
    subprocess.run(("git", "-C", str(repo), "add", "semantic-source.md"), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(("git", "-C", str(repo), "commit", "-m", "semantic source"), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    head = subprocess.check_output(("git", "-C", str(repo), "rev-parse", "HEAD"), text=True).strip()
    records = repo / "docs" / "project" / "semantic-records"
    records.mkdir(parents=True)
    (records / "record.json").write_text(json.dumps({"identity": "record", "version": "v1", "claim_identity": "claim", "assertion_reference": "assertion",
        "assertion": "Bound assertion.", "source_identity": "source", "project_identity": "candidate-repository", "artifact_locator": "semantic-source.md",
        "source_revision": head, "source_sha256": hashlib.sha256(artifact.read_bytes()).hexdigest(), "observation_identity": "observation", "block_ordinal": 0,
        "line_start": 1, "line_end": 1, "authoring_process": "fixture"}), encoding="utf-8")
    artifact.write_text("Changed semantic context.\n", encoding="utf-8")
    output = tmp_path / "context.json"
    assert cli.main(["context", "--project", str(repo), "--task", "semantic", "--authorize-local-inspection", "--output", str(output)]) == 0
    payload = json.loads(output.read_text())
    assert payload["verified_semantic_evidence"] == []
    assert any("bound Source hash" in value for value in payload["limitations"])


@pytest.mark.parametrize(
    ("count", "returned", "excluded", "truncated"),
    ((3, 3, 0, False), (64, 64, 0, False), (66, 64, 2, True)),
)
def test_markdown_candidate_diagnostics_preserve_order_and_limit(
    tmp_path: Path, count: int, returned: int, excluded: int, truncated: bool,
) -> None:
    for index in range(count):
        (tmp_path / f"document-{index:03}.md").write_text("# Document\n\nneedle\n", encoding="utf-8")
    discovery = _markdown_candidates(tmp_path, ("needle",))
    assert discovery.diagnostics() == {
        "total_matches": count, "returned_candidates": returned, "excluded_by_limit": excluded,
        "distinct_source_documents": returned, "truncated": truncated, "candidate_limit": 64,
    }
    assert [item["artifact"] for item in discovery.candidates] == [f"document-{index:03}.md" for index in range(returned)]
