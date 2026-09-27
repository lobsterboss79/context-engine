"""Local, TOML-only preflight for frozen FX-F6-J v1; no pipeline invocation."""
from __future__ import annotations

import json
from pathlib import Path
import tomllib


ROOT = Path.cwd()
FIXTURE = ROOT / "docs/phase-4/ws2-item-2.6-fixtures/F6-J"


def load(name: str) -> dict:
    with (FIXTURE / name).open("rb") as handle:
        return tomllib.load(handle)


def main() -> None:
    bootstrap = load("bootstrap.toml")
    project = load("project.toml")
    request = load("controlled-request.toml")
    source = request["sources"][0]
    artifact = request["artifacts"][0]
    forbidden_product_outcomes = {
        "unsupported-artifact-type", "Insufficient", "insufficient",
        "coherent_with_qualification", "PASS", "required deficiency",
        "renderer output",
    }
    constructed_values = (
        *bootstrap["bootstrap"].values(), *project["project"].values(),
        *request["fixture"].values(), *request["task"].values(),
        *request["asu"].values(), *source.values(), *artifact.values(),
    )
    checks = {
        "bootstrap_project": bootstrap["bootstrap"]["project"] == "fixture-lantern-f6j",
        "project_identity": project["project"]["identity"] == "fixture-lantern-f6j",
        "fixture_identity": request["fixture"]["identity"] == "FX-F6-J" and request["fixture"]["version"] == 1,
        "task_identity": request["task"]["identity"] == "REQ-F6J-LANTERN-REVIEW-STATUS",
        "asu_frozen_adequate": request["asu"]["identity"] == "ASU-F6J-LANTERN-REVIEW-STATUS" and request["asu"]["adequacy"] == "adequate" and bool(request["asu"]["basis"]),
        "sole_source_preserved": source["identity"] == "SRC-F6J-LANTERN-REVIEW-REPOSITORY" and all(source[key] is True for key in ("available", "accessible", "authorized", "supported", "governed_in_scope")),
        "required_pdf_artifact_preserved": artifact["identity"] == "ART-F6J-LANTERN-REVIEW-STATUS-PDF" and artifact["source"] == source["identity"] and artifact["locator"] == "sources/lantern-review-status.pdf" and artifact["format"] == "pdf" and artifact["relevant_to_task"] is True and artifact["role"] == "required" and artifact["contains_required_material"] is True,
        "sole_artifact_location_exists": (FIXTURE / artifact["locator"]).is_file(),
        "no_preclassified_source_failure": not any(value in {"unavailable", "inaccessible", "unauthorized", "unsupported", "absent"} for value in source.values() if isinstance(value, str)),
        "no_runtime_outcome_injected": not any(value in forbidden_product_outcomes for value in constructed_values if isinstance(value, str)),
        "pipeline_executed": False,
        "artifact_observation_executed": False,
    }
    passed = all(value for key, value in checks.items() if key not in {"pipeline_executed", "artifact_observation_executed"}) and not checks["pipeline_executed"] and not checks["artifact_observation_executed"]
    result = {"fixture": "FX-F6-J v1", "expected_result": "ER-F6-J v1", "checks": checks, "result": "PASS" if passed else "FAIL"}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
