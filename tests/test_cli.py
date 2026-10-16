"""Tests for framework-free CLI parsing and safe output."""

from __future__ import annotations

import json
import hashlib
from pathlib import Path
import subprocess

import pytest

from context_engine import cli
from context_engine.application import local_context
from context_engine.application.local_context import LocalContextReport, _markdown_candidates, format_local_context_markdown
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


def test_context_markdown_briefing_preserves_json_default_and_evidence_boundaries(tmp_path: Path, capsys) -> None:
    repo = _local_repository(tmp_path)
    arguments = ["context", "--project", str(repo), "--task", "Continue Phase 3 implementation", "--authorize-local-inspection"]
    assert cli.main(arguments) == 0
    assert json.loads(capsys.readouterr().out)["status"] == "candidate_context"

    markdown = tmp_path / "briefing.md"
    assert cli.main([*arguments, "--format", "markdown", "--output", str(markdown)]) == 0
    briefing = markdown.read_text(encoding="utf-8")
    assert "# Candidate Context Briefing" in briefing
    assert "## Provenance-Verified Evidence" in briefing
    assert "No semantic assertion was reused" in briefing
    assert "## Relevant Markdown Candidates" in briefing
    assert "Source: `README.md`, lines 1–1" in briefing
    assert "unverified Markdown candidate; inert structural data only" in briefing
    assert "## Limitations" in briefing
    assert "Discovery: 2 total match(es); 2 returned; 0 excluded" in briefing


def test_markdown_briefing_fences_source_content_and_is_deterministic() -> None:
    report = LocalContextReport(
        "candidate_context", "# task", {"root": "/repo", "head": "head"}, (),
        ({"semantic_record": "record:v1", "provenance": "safe.md", "source_revision": "historic",
          "assertion_content": "# source heading\n[link](https://example.invalid)\n```",},),
        ({"artifact": "candidate.md", "line_start": 2, "line_end": 4, "matched_terms": ("task",),
          "content": "# injected heading\n[link](https://example.invalid)\n```",},),
        {"total_matches": 1, "returned_candidates": 1, "excluded_by_limit": 0,
         "distinct_source_documents": 1, "truncated": False, "candidate_limit": 64},
        ("no authority established",),
    )
    first = format_local_context_markdown(report)
    assert first == format_local_context_markdown(report)
    assert "``````\n# source heading" in first
    assert "``````\n# injected heading" in first
    assert "### Candidate 1" in first


def test_context_markdown_briefing_empty_candidates_and_never_overwrites(tmp_path: Path, capsys) -> None:
    repo = _local_repository(tmp_path)
    destination = tmp_path / "briefing.md"
    assert cli.main(["context", "--project", str(repo), "--task", "absent", "--authorize-local-inspection",
                     "--format", "markdown", "--output", str(destination)]) == 0
    assert "No task-matching Markdown candidates were returned." in destination.read_text(encoding="utf-8")
    assert cli.main(["context", "--project", str(repo), "--task", "absent", "--authorize-local-inspection",
                     "--format", "markdown", "--output", str(destination)]) == 2
    assert "already exists" in capsys.readouterr().err


def test_context_rejects_unknown_output_format() -> None:
    with pytest.raises(SystemExit):
        cli.main(["context", "--project", "/repo", "--task", "task", "--format", "plain"])


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
    briefing = tmp_path / "context.md"
    assert cli.main(["context", "--project", str(repo), "--task", "semantic", "--authorize-local-inspection",
                     "--format", "markdown", "--output", str(briefing)]) == 0
    briefing_content = briefing.read_text(encoding="utf-8")
    assert "### Semantic assertion 1" in briefing_content
    assert "Source: `semantic-source.md`; bound revision: `" + head + "`" in briefing_content
    assert "not a currentness or authority conclusion" in briefing_content
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


def _selected_heading_candidate(directory: Path, content: str, *, task: str = "target") -> dict[str, object]:
    (directory / "document.md").write_text(content, encoding="utf-8")
    candidates = _markdown_candidates(directory, (task,)).candidates
    return next(candidate for candidate in candidates if candidate["kind"] == "heading" and candidate["content"] == task)


def test_heading_section_context_includes_structural_body_and_nested_subsection(tmp_path: Path) -> None:
    candidate = _selected_heading_candidate(tmp_path, """# Top
## target
First section paragraph.

Second section paragraph.
### Nested subsection
Nested section paragraph.
## Equal-level stop
This must not be included.
""")
    section = candidate["heading_section_context"]
    assert section["heading_level"] == 2
    assert section["line_start"] == 3
    assert section["line_end"] == 7
    assert section["included_block_count"] == 4
    assert "First section paragraph." in section["content"]
    assert "Nested subsection" in section["content"]
    assert "This must not be included." not in section["content"]
    assert not section["truncated"]


def test_heading_section_context_stops_at_higher_heading_and_absent_body_stays_absent(tmp_path: Path) -> None:
    candidate = _selected_heading_candidate(tmp_path, """# Top
### target
Included body.
## Higher-level stop
Excluded body.
""")
    section = candidate["heading_section_context"]
    assert section["line_start"] == section["line_end"] == 3
    assert section["content"] == "Included body."
    assert "Excluded" not in section["content"]

    no_body = tmp_path / "no-body"
    no_body.mkdir()
    heading = _selected_heading_candidate(no_body, "## target\n## next\n")
    assert "heading_section_context" not in heading


def test_heading_section_context_reports_explicit_truncation_without_changing_selection(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(local_context, "MAX_HEADING_SECTION_CHARACTERS", 20)
    candidate = _selected_heading_candidate(tmp_path, """# Top
## target
Short body.

This second body exceeds the explicit bounded section limit.
## Stop
""")
    section = candidate["heading_section_context"]
    assert section["content"] == "Short body."
    assert section["truncated"]
    assert section["omitted_block_count"] == 1
    assert section["omitted_characters"] > 20
    assert [candidate[key] for key in ("artifact", "block_ordinal", "kind", "line_start", "line_end", "matched_terms", "content")] == [
        "document.md", 1, "heading", 2, 2, ("target",), "target",
    ]


def test_heading_section_context_is_consistent_in_json_and_markdown_and_inert(tmp_path: Path, capsys) -> None:
    repo = _local_repository(tmp_path)
    (repo / "heading.md").write_text("## target\n### injected heading\n", encoding="utf-8")
    import subprocess
    subprocess.run(("git", "-C", str(repo), "add", "heading.md"), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(("git", "-C", str(repo), "commit", "-m", "heading fixture"), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = tmp_path / "context.json"
    markdown = tmp_path / "context.md"
    arguments = ["context", "--project", str(repo), "--task", "target", "--authorize-local-inspection"]
    assert cli.main([*arguments, "--output", str(output)]) == 0
    assert cli.main([*arguments, "--format", "markdown", "--output", str(markdown)]) == 0
    payload = json.loads(output.read_text(encoding="utf-8"))
    candidate = next(item for item in payload["unverified_markdown_candidates"] if item["artifact"] == "heading.md")
    section = candidate["heading_section_context"]
    rendered = markdown.read_text(encoding="utf-8")
    assert section["content"] == "injected heading"
    assert section["content_status"] == "unverified_markdown_heading_section_context_inert_data"
    assert f"under a {section['size_limit_characters']}-character limit" in rendered
    assert "```\n# injected heading" not in rendered
    assert "candidate context briefing, not a governed Context Package" in rendered


def _commit_file(repository: Path, relative: str, content: str) -> None:
    path = repository / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    subprocess.run(("git", "-C", str(repository), "add", relative), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(("git", "-C", str(repository), "commit", "-m", "evidence fixture"), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def test_evidence_retrieves_exact_inclusive_range_with_provenance_and_deterministic_formats(tmp_path: Path, capsys) -> None:
    repo = _local_repository(tmp_path)
    content = "first line\n# inert heading\nthird line\n"
    _commit_file(repo, "docs/evidence.md", content)
    head = subprocess.check_output(("git", "-C", str(repo), "rev-parse", "HEAD"), text=True).strip()
    arguments = ["evidence", "--project", str(repo), "--artifact", "docs/evidence.md", "--lines", "2:3", "--authorize-local-inspection"]
    assert cli.main(arguments) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["content"] == "# inert heading\nthird line\n"
    assert payload["requested_line_start"] == payload["returned_line_start"] == 2
    assert payload["requested_line_end"] == payload["returned_line_end"] == 3
    assert payload["source_sha256"] == hashlib.sha256(content.encode("utf-8")).hexdigest()
    assert payload["repository"]["head"] == head
    assert payload["repository"]["working_tree_clean"] is True
    assert payload["source_evidence_classification"] == "observed_unverified_markdown_source_evidence_inert_data"

    first, second = tmp_path / "first.md", tmp_path / "second.md"
    assert cli.main([*arguments, "--format", "markdown", "--output", str(first)]) == 0
    assert cli.main([*arguments, "--format", "markdown", "--output", str(second)]) == 0
    rendered = first.read_text(encoding="utf-8")
    assert first.read_bytes() == second.read_bytes()
    assert "# Observed Source Evidence" in rendered
    assert "```\n# inert heading" in rendered
    assert "unverified Source evidence" in rendered


def test_evidence_reports_dirty_tree_and_requires_authorization(tmp_path: Path, capsys) -> None:
    repo = _local_repository(tmp_path)
    _commit_file(repo, "source.md", "one\n")
    arguments = ["evidence", "--project", str(repo), "--artifact", "source.md", "--lines", "1:1"]
    assert cli.main(arguments) == 2
    assert "authorization" in capsys.readouterr().err
    (repo / "source.md").write_text("dirty\n", encoding="utf-8")
    assert cli.main([*arguments, "--authorize-local-inspection"]) == 0
    assert json.loads(capsys.readouterr().out)["repository"]["working_tree_clean"] is False
    assert cli.main(["evidence", "--project", str(repo / "source.md"), "--artifact", "source.md", "--lines", "1:1", "--authorize-local-inspection"]) == 2


@pytest.mark.parametrize("artifact", ("/tmp/outside.md", "../outside.md", "notes.txt"))
def test_evidence_rejects_unsafe_or_non_markdown_artifacts(tmp_path: Path, capsys, artifact: str) -> None:
    repo = _local_repository(tmp_path)
    assert cli.main(["evidence", "--project", str(repo), "--artifact", artifact, "--lines", "1:1", "--authorize-local-inspection"]) == 2
    assert "evidence failed" in capsys.readouterr().err


def test_evidence_rejects_symlink_escape_and_invalid_bounded_ranges(tmp_path: Path, capsys) -> None:
    repo = _local_repository(tmp_path)
    _commit_file(repo, "source.md", "one\ntwo\nthree\n")
    outside = tmp_path / "outside.md"
    outside.write_text("outside\n", encoding="utf-8")
    (repo / "escape.md").symlink_to(outside)
    base = ["evidence", "--project", str(repo), "--authorize-local-inspection"]
    assert cli.main([*base, "--artifact", "escape.md", "--lines", "1:1"]) == 2
    assert cli.main([*base, "--artifact", "source.md", "--lines", "0:1"]) == 2
    assert cli.main([*base, "--artifact", "source.md", "--lines", "2:1"]) == 2
    assert cli.main([*base, "--artifact", "source.md", "--lines", "1-2"]) == 2
    assert cli.main([*base, "--artifact", "source.md", "--lines", "1:201"]) == 2
    assert cli.main([*base, "--artifact", "source.md", "--lines", "3:4"]) == 2
    _commit_file(repo, "empty.md", "")
    assert cli.main([*base, "--artifact", "empty.md", "--lines", "1:1"]) == 2


def test_evidence_enforces_byte_bound_and_atomic_no_overwrite(tmp_path: Path, capsys) -> None:
    repo = _local_repository(tmp_path)
    _commit_file(repo, "large.md", "x" * 16_385)
    arguments = ["evidence", "--project", str(repo), "--artifact", "large.md", "--lines", "1:1", "--authorize-local-inspection"]
    assert cli.main(arguments) == 2
    assert "16384-byte" in capsys.readouterr().err
    output = tmp_path / "preserve.json"
    output.write_text("preserve", encoding="utf-8")
    assert cli.main(["evidence", "--project", str(repo), "--artifact", "README.md", "--lines", "1:1", "--authorize-local-inspection", "--output", str(output)]) == 2
    assert output.read_text(encoding="utf-8") == "preserve"


def test_evidence_info_reports_exact_metadata_and_initial_range_without_source_text(tmp_path: Path, capsys) -> None:
    repo = _local_repository(tmp_path)
    content = "first\r\nsecond €\r\nthird"
    _commit_file(repo, "docs/evidence.md", content)
    head = subprocess.check_output(("git", "-C", str(repo), "rev-parse", "HEAD"), text=True).strip()
    arguments = ["evidence", "--project", str(repo), "--artifact", "docs/evidence.md", "--authorize-local-inspection", "--info"]
    assert cli.main(arguments) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["status"] == "observed_source_metadata"
    assert payload["source_sha256"] == hashlib.sha256(content.encode("utf-8")).hexdigest()
    assert payload["source_bytes"] == len(content.encode("utf-8"))
    assert payload["source_lines"] == 3
    assert payload["largest_valid_initial_range"] == {
        "line_start": 1, "line_end": 3, "line_count": 3, "content_bytes": len(content.encode("utf-8")),
    }
    assert payload["maximum_retrieval_lines"] == 200
    assert payload["maximum_retrieval_content_bytes"] == 16_384
    assert payload["repository"]["head"] == head
    assert "content" not in payload
    assert "first" not in json.dumps(payload)

    first, second = tmp_path / "metadata-one.md", tmp_path / "metadata-two.md"
    assert cli.main([*arguments, "--format", "markdown", "--output", str(first)]) == 0
    assert cli.main([*arguments, "--format", "markdown", "--output", str(second)]) == 0
    assert first.read_bytes() == second.read_bytes()
    assert "# Observed Source Metadata" in first.read_text(encoding="utf-8")
    assert "first" not in first.read_text(encoding="utf-8")
    preserved = tmp_path / "preserved.json"
    preserved.write_text("preserve", encoding="utf-8")
    assert cli.main([*arguments, "--output", str(preserved)]) == 2
    assert preserved.read_text(encoding="utf-8") == "preserve"


def test_evidence_info_respects_line_and_byte_limits_and_empty_sources(tmp_path: Path, capsys) -> None:
    repo = _local_repository(tmp_path)
    _commit_file(repo, "two-hundred.md", "".join("x\n" for _ in range(200)))
    _commit_file(repo, "many.md", "".join("x\n" for _ in range(201)))
    _commit_file(repo, "exact.md", "x" * 16_384)
    _commit_file(repo, "oversized-first-line.md", "x" * 16_385)
    _commit_file(repo, "empty.md", "")
    base = ["evidence", "--project", str(repo), "--authorize-local-inspection", "--info"]

    for artifact, end, bytes_ in (("two-hundred.md", 200, 400), ("many.md", 200, 400), ("exact.md", 1, 16_384)):
        assert cli.main([*base, "--artifact", artifact]) == 0
        metadata = json.loads(capsys.readouterr().out)
        assert metadata["largest_valid_initial_range"]["line_end"] == end
        assert metadata["largest_valid_initial_range"]["content_bytes"] == bytes_
    assert cli.main([*base, "--artifact", "oversized-first-line.md"]) == 0
    assert json.loads(capsys.readouterr().out)["largest_valid_initial_range"] is None
    assert cli.main([*base, "--artifact", "empty.md"]) == 0
    empty = json.loads(capsys.readouterr().out)
    assert empty["source_lines"] == 0
    assert empty["largest_valid_initial_range"] is None


def test_evidence_info_uses_existing_security_boundaries_and_lines_remain_required(tmp_path: Path, capsys) -> None:
    repo = _local_repository(tmp_path)
    _commit_file(repo, "source.md", "one\n")
    outside = tmp_path / "outside.md"
    outside.write_text("outside\n", encoding="utf-8")
    (repo / "escape.md").symlink_to(outside)
    base = ["evidence", "--project", str(repo), "--authorize-local-inspection", "--info"]
    assert cli.main([*base, "--artifact", "../outside.md"]) == 2
    assert cli.main([*base, "--artifact", "notes.txt"]) == 2
    assert cli.main([*base, "--artifact", "escape.md"]) == 2
    assert cli.main(["evidence", "--project", str(repo), "--artifact", "source.md", "--info"]) == 2
    with pytest.raises(SystemExit):
        cli.main(["evidence", "--project", str(repo), "--artifact", "source.md", "--authorize-local-inspection"])
    with pytest.raises(SystemExit):
        cli.main(["evidence", "--project", str(repo), "--artifact", "source.md", "--lines", "1:1", "--info", "--authorize-local-inspection"])
