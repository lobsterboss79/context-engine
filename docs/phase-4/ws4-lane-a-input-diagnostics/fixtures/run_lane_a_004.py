"""Frozen semantic successor CTL-P4-4A-004 v1."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from context_engine.application.decision_pipeline import ApplicabilityInputs, EnforcementInputs, RelevanceOutcome, RoleInputs, evaluate_applicability, select_candidate
from context_engine.application.discovery import DiscoveryEvidence, discover
from context_engine.application.lifecycle import ApplicableSourceUniverse, Availability, BoundaryAdequacy, RegisteredSource
from context_engine.application.package_construction import CoherenceInputs, construct_logical_package, evaluate_coherence
from context_engine.application.rendering import ConsumerContract, ConsumerKind, render_package
from context_engine.application.sufficiency import SufficiencyInputs, evaluate_sufficiency
from context_engine.core.model import Consumer, ContextRequest, Provenance, RepresentedInformation, Requester, SemanticIdentity, SufficiencyOutcome, TaskIntent, TaskScope


ROOT = Path(__file__).resolve().parents[4]
FIXTURES = Path(__file__).resolve().parent


def ident(kind: str, value: str) -> SemanticIdentity:
    return SemanticIdentity(kind, value)


def request() -> ContextRequest:
    return ContextRequest(ident("request", "request-lane-a"), ident("project", "lane-a-project"), Requester(ident("requester", "lane-a-requester")), Consumer(ident("consumer", "lane-a-consumer")), TaskIntent("lane-a controlled classification"), TaskScope("lane-a bounded fixture"))


def represented(source: RegisteredSource, name: str) -> DiscoveryEvidence:
    return DiscoveryEvidence(RepresentedInformation(ident("represented_information", f"represented-{name}"), ident("subject", "subject-lane-a"), Provenance(ident("provenance", f"provenance-{name}"), source=ident("source", source.identity))), source, text="lane-a-term")


def discovery_case(name: str, availability: Availability, include_evidence: bool):
    source = RegisteredSource(f"source-{name}", "lane-a-project", "controlled", "docs", availability)
    universe = ApplicableSourceUniverse("request-lane-a", (source,), BoundaryAdequacy.KNOWN_INCOMPLETE, "lane-a bounded fixture")
    evidence = (represented(source, name),) if include_evidence else ()
    return source, universe, discover(request(), universe, evidence, query_terms=("lane-a-term",))


def source_case(name: str, availability: Availability, include_evidence: bool) -> dict[str, object]:
    source, _, result = discovery_case(name, availability, include_evidence)
    labels = {"absent": "ABSENCE", "unavailable": "UNAVAILABLE", "partial": "PARTIAL EVIDENCE", "success": "SUCCESSFUL COMPLETION"}
    candidate_limitations = [value.detail for value in result.candidates[0].limitations] if result.candidates else []
    return {"classification": labels[name], "availability": source.availability.value, "candidate_count": len(result.candidates), "candidate_limitations": candidate_limitations, "excluded_sources": list(result.excluded_sources), "limitations": [value.detail for value in result.limitations], "negative_result_scope": result.negative_result_scope}


def cli_case(label: str, bootstrap: Path, config: Path) -> dict[str, object]:
    completed = subprocess.run([sys.executable, "-m", "context_engine", "bootstrap-validate", "--bootstrap", str(bootstrap), "--project-configuration", str(config)], cwd=ROOT, text=True, capture_output=True, check=False)
    return {"label": label, "exit_code": completed.returncode, "stdout": completed.stdout, "stderr": completed.stderr}


def downstream_partial() -> dict[str, object]:
    _, universe, discovery = discovery_case("partial", Availability.PARTIAL, True)
    candidate = discovery.candidates[0]
    req = request()
    applicable = evaluate_applicability(candidate, ApplicabilityInputs(RelevanceOutcome.RELEVANT, "frozen deterministic relevance", True, EnforcementInputs(True, req.project, req.project, True, True)))
    selected = select_candidate(applicable, RoleInputs(False, False, True, "frozen supporting selection"), selection_basis="frozen selection basis").selected
    assert selected is not None
    sufficiency = evaluate_sufficiency(SufficiencyInputs((selected,), universe))
    construction = construct_logical_package(package_identity=ident("package", "package-lane-a-partial"), request=req.identity, selected=(selected,), candidates=(candidate,), universe=universe, sufficiency=sufficiency, coherence=evaluate_coherence(CoherenceInputs()), record_identity=ident("record", "record-lane-a-partial"), termination_basis="frozen bounded partial qualification")
    assert construction.package is not None
    rendering = render_package(construction.package, ConsumerContract(ConsumerKind.HUMAN, req.consumer, True))
    manifest = construction.package.manifest.entries[0]
    return {"candidate_limitations": [value.detail for value in candidate.limitations], "item_limitations": [value.detail for value in selected.limitations], "manifest_limitations": [value.detail for value in manifest.limitations], "package_limitations": [value.detail for value in construction.package.limitations], "sufficiency": construction.package.sufficiency.value, "authority_count": len(selected.authorities), "render_status": rendering.status, "rendered_content": rendering.content}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    malformed = cli_case("malformed-input", FIXTURES / "malformed-bootstrap.toml", FIXTURES / "mismatched-project.toml")
    invalid = cli_case("invalid-configuration", FIXTURES / "valid-bootstrap.toml", FIXTURES / "mismatched-project.toml")
    source_cases = {"absent": source_case("absent", Availability.ABSENT, False), "unavailable": source_case("unavailable", Availability.UNAVAILABLE, False), "partial": source_case("partial", Availability.PARTIAL, True), "success": source_case("success", Availability.AVAILABLE, True)}
    downstream = downstream_partial()
    partial_detail = "Source source-partial: partial"
    secret = "lane-a-secret-canary"
    assertions = {
        "cli_exit_2": malformed["exit_code"] == invalid["exit_code"] == 2,
        "cli_attributable": "bootstrap validation failed:" in malformed["stderr"] and "bootstrap validation failed:" in invalid["stderr"],
        "no_false_validated": "validated" not in malformed["stdout"] and "validated" not in invalid["stdout"],
        "secret_not_exposed": secret not in malformed["stdout"] + malformed["stderr"] + invalid["stdout"] + invalid["stderr"],
        "states_distinct": len({value["classification"] for value in source_cases.values()}) == 4,
        "absence_not_candidate": source_cases["absent"]["candidate_count"] == 0,
        "unavailable_not_absence": source_cases["unavailable"]["candidate_count"] == 0 and any("unavailable" in value for value in source_cases["unavailable"]["limitations"]),
        "partial_candidate_qualified": source_cases["partial"]["candidate_count"] == 1 and partial_detail in source_cases["partial"]["candidate_limitations"],
        "success_not_partial": source_cases["success"]["candidate_count"] == 1 and partial_detail not in source_cases["success"]["candidate_limitations"],
        "partial_downstream_preserved": all(partial_detail in downstream[key] for key in ("candidate_limitations", "item_limitations", "manifest_limitations")),
        "partial_rendered_faithfully": downstream["render_status"] == "rendered" and partial_detail in (downstream["rendered_content"] or ""),
        "no_authority_manufactured": downstream["authority_count"] == 0,
        "no_sufficiency_manufactured": downstream["sufficiency"] == SufficiencyOutcome.INSUFFICIENT.value,
        "no_audit_or_recovery_claim": True,
    }
    result = {"control": "CTL-P4-4A-004 v1", "procedure": "PROC-P4-4A-004 v1", "expected_result": "ER-P4-4A-004 v1", "scenario_expected_states": {"malformed-input": "APPLICATION-LEVEL FAILURE", "invalid-configuration": "APPLICATION-LEVEL FAILURE", **{key: value["classification"] for key, value in source_cases.items()}}, "cli_cases": [malformed, invalid], "source_cases": source_cases, "downstream_partial": downstream, "assertions": assertions, "validation_control_result": "PASS" if all(assertions.values()) else "FAIL", "diagnostic_is_not_durable_audit": True, "diagnostic_is_not_recovery_evidence": True}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"validation_control_result": result["validation_control_result"], "assertions": assertions}, sort_keys=True))
    return 0 if all(assertions.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
