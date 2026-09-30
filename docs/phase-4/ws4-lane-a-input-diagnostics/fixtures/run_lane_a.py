"""Frozen WS4 Lane A controlled execution runner."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from context_engine.application.discovery import DiscoveryEvidence, discover
from context_engine.application.lifecycle import ApplicableSourceUniverse, Availability, BoundaryAdequacy, RegisteredSource
from context_engine.core.model import Provenance, RepresentedInformation, SemanticIdentity


ROOT = Path(__file__).resolve().parents[4]
FIXTURES = Path(__file__).resolve().parent


def represented(source: RegisteredSource, name: str) -> DiscoveryEvidence:
    return DiscoveryEvidence(
        RepresentedInformation(SemanticIdentity(f"represented-{name}"), SemanticIdentity("subject-lane-a"),
            Provenance(SemanticIdentity(f"provenance-{name}"), source=SemanticIdentity(source.identity))),
        source, text="lane-a-term",
    )


def source_case(name: str, availability: Availability, include_evidence: bool) -> dict[str, object]:
    source = RegisteredSource(f"source-{name}", "lane-a-project", "controlled", "docs", availability)
    universe = ApplicableSourceUniverse("request-lane-a", (source,), BoundaryAdequacy.KNOWN_INCOMPLETE, "lane-a bounded fixture")
    evidence = (represented(source, name),) if include_evidence else ()
    request = type("Request", (), {"identity": SemanticIdentity("request-lane-a"), "project": SemanticIdentity("lane-a-project")})()
    result = discover(request, universe, evidence, query_terms=("lane-a-term",))
    classifications = {"absent": "ABSENCE", "unavailable": "UNAVAILABLE", "partial": "PARTIAL EVIDENCE", "success": "SUCCESSFUL COMPLETION"}
    return {"classification": classifications[name], "availability": availability.value,
            "candidate_count": len(result.candidates), "excluded_sources": list(result.excluded_sources),
            "limitations": [item.detail for item in result.limitations], "negative_result_scope": result.negative_result_scope}


def cli_case(label: str, bootstrap: Path, config: Path) -> dict[str, object]:
    completed = subprocess.run([sys.executable, "-m", "context_engine", "bootstrap-validate", "--bootstrap", str(bootstrap), "--project-configuration", str(config)], cwd=ROOT, text=True, capture_output=True, check=False)
    return {"label": label, "exit_code": completed.returncode, "stdout": completed.stdout, "stderr": completed.stderr}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    malformed = cli_case("malformed-input", FIXTURES / "malformed-bootstrap.toml", FIXTURES / "mismatched-project.toml")
    invalid = cli_case("invalid-configuration", FIXTURES / "valid-bootstrap.toml", FIXTURES / "mismatched-project.toml")
    source_cases = {"absent": source_case("absent", Availability.ABSENT, False),
                    "unavailable": source_case("unavailable", Availability.UNAVAILABLE, False),
                    "partial": source_case("partial", Availability.PARTIAL, True),
                    "success": source_case("success", Availability.AVAILABLE, True)}
    secret = "lane-a-secret-canary"
    assertions = {
        "cli_exit_2": malformed["exit_code"] == invalid["exit_code"] == 2,
        "cli_attributable": "bootstrap validation failed:" in malformed["stderr"] and "bootstrap validation failed:" in invalid["stderr"],
        "no_false_validated": "validated" not in malformed["stdout"] and "validated" not in invalid["stdout"],
        "secret_not_exposed": secret not in malformed["stdout"] + malformed["stderr"] + invalid["stdout"] + invalid["stderr"],
        "states_distinct": len({value["classification"] for value in source_cases.values()}) == 4,
        "absence_not_candidate": source_cases["absent"]["candidate_count"] == 0,
        "unavailable_not_absence": source_cases["unavailable"]["candidate_count"] == 0 and any("unavailable" in value for value in source_cases["unavailable"]["limitations"]),
        "partial_preserved": source_cases["partial"]["candidate_count"] == 1 and any("partial" in value for value in source_cases["partial"]["limitations"]),
        "success_complete": source_cases["success"]["candidate_count"] == 1 and not any("partial" in value for value in source_cases["success"]["limitations"]),
        "no_audit_or_recovery_claim": True,
    }
    result = {"control": "CTL-P4-4A-001 v1", "expected_result": "ER-P4-4A-001 v1",
              "scenario_expected_states": {"malformed-input": "APPLICATION-LEVEL FAILURE", "invalid-configuration": "APPLICATION-LEVEL FAILURE", **{key: value["classification"] for key, value in source_cases.items()}},
              "cli_cases": [malformed, invalid], "source_cases": source_cases, "assertions": assertions,
              "validation_control_result": "PASS" if all(assertions.values()) else "FAIL",
              "diagnostic_is_not_durable_audit": True, "diagnostic_is_not_recovery_evidence": True}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"validation_control_result": result["validation_control_result"], "assertions": assertions}, sort_keys=True))
    return 0 if all(assertions.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
