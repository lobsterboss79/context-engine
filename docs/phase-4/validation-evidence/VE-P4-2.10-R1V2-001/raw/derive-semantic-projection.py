"""Derive and assess an R1 v2 semantic projection from preserved run originals."""
from __future__ import annotations

import json
from pathlib import Path
import sys


CANDIDATES = ["RI-F3-CANVAS-HISTORY", "RI-F3-DEPOT-UNVERIFIED", "RI-F3-SEALED", "RI-F3-TOTE"]
MANIFEST = ["SRC-F3-COMPETING", "SRC-F3-CURRENT", "SRC-F3-HISTORY", "SRC-F3-QUALIFICATION"]
REQUIRED = ["RI-F3-SEALED", "RI-F3-TOTE"]
SUPPORTING = ["RI-F3-CANVAS-HISTORY", "RI-F3-DEPOT-UNVERIFIED"]


def payload(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    fence = chr(96) * 3
    return json.loads(text.split(fence + "json" + chr(10), 1)[1].split(chr(10) + fence, 1)[0])


def main() -> None:
    raw_dir = Path(sys.argv[1])
    raw = json.loads((raw_dir / "raw-result.json").read_text(encoding="utf-8"))
    renderings = {kind: payload(raw_dir / f"rendering-{kind}.md") for kind in ("human", "chatgpt", "codex")}
    projection = {
        "fixture": raw["fixture"],
        "expected_result": raw["expected_result"],
        "repeatability_expected_result": raw["repeatability_expected_result"],
        "semantic_contract": raw["semantic_contract"],
        "bootstrap": raw["bootstrap"],
        "configuration": raw["configuration"],
        "represented_information": raw["represented_information"],
        "candidates": raw["discovery"]["candidates"],
        "applicability_and_selection": raw["applicability_and_selection"],
        "construction": raw["construction"],
        "rendering_statuses": raw["renderings"],
        "renderer_payloads": renderings,
    }
    candidate_ids = [entry["represented"]["identity"]["value"] for entry in projection["candidates"]]
    selected = projection["construction"]["package"]["items"]
    selected_ids = [entry["represented"]["identity"]["value"] for entry in selected]
    selected_roles = [entry["role"] for entry in selected]
    manifest_ids = [entry["source"]["value"] for entry in projection["construction"]["package"]["manifest"]["entries"]]
    assessments = {
        "candidate_order": candidate_ids == CANDIDATES,
        "selection_package_order": selected_ids == CANDIDATES and selected_roles == ["supporting", "supporting", "required", "required"],
        "manifest_order": manifest_ids == MANIFEST,
        "renderers": {},
        "represented_information": [entry["identity"]["value"] for entry in projection["represented_information"]] == ["RI-F3-SEALED", "RI-F3-TOTE", "RI-F3-CANVAS-HISTORY", "RI-F3-DEPOT-UNVERIFIED"],
        "sufficiency": projection["construction"]["package"]["sufficiency"] == "insufficient",
        "coherence": projection["construction"]["package"]["coherence"]["outcome"] == "coherent_with_qualification",
    }
    for kind, rendered in renderings.items():
        assessments["renderers"][kind] = {
            "status": raw["renderings"][kind]["status"] == "rendered",
            "required_order": [item["represented_information"] for item in rendered["required_context"]] == REQUIRED,
            "supporting_order": [item["represented_information"] for item in rendered["supporting_context"]] == SUPPORTING,
            "manifest_order": [item["source"] for item in rendered["source_manifest"]] == MANIFEST,
            "boundary": "rendering-is-not-delivery-receipt-or-use" in raw["renderings"][kind]["reason_codes"],
        }
    conflict_items = [item for item in selected if item["represented"]["identity"]["value"] in REQUIRED]
    assessments["conflict_unresolved"] = all(
        item["conflicts"][0]["identity"]["value"] == "CON-F3-CASE-CHOICE"
        and item["conflicts"][0]["resolved_by"] is None
        for item in conflict_items
    )
    assessments["uncertainty"] = any(
        lim["evidence_boundary"] == "UNC-F3-DEPOT"
        for item in selected for lim in item["limitations"]
    )
    assessments["pass"] = all(
        [assessments["candidate_order"], assessments["selection_package_order"], assessments["manifest_order"],
         assessments["represented_information"], assessments["sufficiency"], assessments["coherence"],
         assessments["conflict_unresolved"], assessments["uncertainty"]]
        + [all(check.values()) for check in assessments["renderers"].values()]
    )
    derived = raw_dir.parent / "derived"
    (derived / "semantic-projection.json").write_text(json.dumps(projection, indent=2, sort_keys=True) + chr(10), encoding="utf-8")
    (derived / "semantic-assessment.json").write_text(json.dumps(assessments, indent=2, sort_keys=True) + chr(10), encoding="utf-8")
    print(json.dumps(assessments, sort_keys=True))


if __name__ == "__main__":
    main()
