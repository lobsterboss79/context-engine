"""Local, non-pipeline input verification for FX-F6-EF v1."""
from __future__ import annotations

import json
from pathlib import Path
import tomllib


ROOT = Path.cwd()
FIXTURE = ROOT / "docs/phase-4/ws2-item-2.6-fixtures/F6-EF"
OUTPUT = ROOT / "docs/phase-4/validation-evidence/VE-F6-EF-001/raw/procedure-preflight.json"
QUERY = "CE-F6EF-ABSENT-IDENTIFIER-7Q3M"


def main() -> None:
    with (FIXTURE / "controlled-request.toml").open("rb") as handle:
        request = tomllib.load(handle)
    sources = {entry["identity"]: entry for entry in request["sources"]}
    expansion = request["expansion_request"]
    plan = request["bounded_iteration_plan"]
    checks = {
        "asu_contains_origin_and_target": request["asu"]["sources"] == ["SRC-F6EF-HARBOR-ORIGIN", "SRC-F6EF-HARBOR-EXPANSION-TARGET"],
        "initial_inspection_is_origin_only": [entry["identity"] for entry in request["sources"] if entry["initially_inspected"]] == ["SRC-F6EF-HARBOR-ORIGIN"],
        "target_is_expansion_only_and_not_initial": sources["SRC-F6EF-HARBOR-EXPANSION-TARGET"]["expansion_only"] is True and sources["SRC-F6EF-HARBOR-EXPANSION-TARGET"]["initially_inspected"] is False,
        "expansion_request_origin": expansion["origin_represented_information"] == "RI-F6EF-HARBOR-ORIGIN-REGISTER",
        "expansion_request_relationship": expansion["relationship"] == "REL-F6EF-HARBOR-ORIGIN-TO-ANNEX",
        "expansion_request_target": expansion["target_source"] == "SRC-F6EF-HARBOR-EXPANSION-TARGET",
        "expansion_request_booleans_and_basis": expansion["material_resolvable_deficiency"] is True and expansion["inspection_authorized"] is True and bool(expansion["basis"]),
        "bounded_iteration": plan["initial_boundary"] == "SRC-F6EF-HARBOR-ORIGIN" and plan["additional_sources"] == ["SRC-F6EF-HARBOR-EXPANSION-TARGET"] and plan["authorized_to_discover"] is True,
        "exact_literal_only": request["query"]["exact_literal"] == QUERY and request["query"]["matching_mode"] == "exact_literal_only",
        "no_runtime_generated_second_target": len(plan["additional_sources"]) == 1 and plan["additional_sources"][0] == expansion["target_source"],
        "no_result_injection": "expected_sufficiency" not in request["bounded_iteration_plan"] and "expected_coherence" not in request["bounded_iteration_plan"] and "expected_sufficiency" not in request["expansion_request"],
    }
    result = {"fixture": "FX-F6-EF v1", "pipeline_executed": False, "checks": checks, "result": "PASS" if all(checks.values()) else "FAIL"}
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))
    if result["result"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
