"""Frozen runner for ER-P4-3B-001 v1; uses existing public v0.1 interfaces."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

from context_engine.adapters.sqlite_state import (
    PersistedArtifactEvidence,
    PersistedEvidence,
    PersistedObservation,
    PersistedRepresentation,
    PersistedTransformation,
    SQLiteStateStore,
)
from context_engine.application.decision_pipeline import (
    ApplicabilityInputs,
    ApplicabilityOutcome,
    EnforcementInputs,
    RelevanceOutcome,
    evaluate_applicability,
)
from context_engine.core.model import (
    Authority,
    AuthorityScope,
    CandidateContext,
    Classification,
    Consumer,
    ContextRequest,
    Currentness,
    CurrentnessAssessment,
    GovernanceAssessment,
    GovernanceState,
    Provenance,
    RepresentedInformation,
    Requester,
    SemanticIdentity,
    TaskIntent,
    TaskScope,
)


def ident(kind: str, value: str) -> SemanticIdentity:
    return SemanticIdentity(kind, value)


PROJECT_A = ident("project", "ws3b-alpha")
PROJECT_B = ident("project", "ws3b-beta")
SUBJECT = ident("claim", "ws3b-governed-subject")
PROVENANCE = Provenance(
    ident("provenance", "ws3b-provenance"), origin_projects=(PROJECT_A,),
    source=ident("source", "ws3b-source"),
)


def candidate(*, authority: str = "matching", governance: GovernanceState = GovernanceState.APPROVED,
              currentness: Currentness = Currentness.CURRENT) -> CandidateContext:
    scope_project = PROJECT_A if authority == "matching" else PROJECT_B
    authorities = () if authority == "absent" else (
        Authority(ident("authority", "ws3b-authority"), "controlled governed basis",
                  AuthorityScope(project=scope_project, domains=("governance",),
                                 phases=("phase-4",), actions=("audit",)), PROVENANCE),
    )
    request = ContextRequest(ident("request", "ws3b-request"), PROJECT_A,
                             Requester(ident("requester", "ws3b-requester")),
                             Consumer(ident("consumer", "ws3b-consumer")),
                             TaskIntent("audit"), TaskScope("governance"))
    represented = RepresentedInformation(ident("represented_information", "ws3b-representation"),
                                          SUBJECT, PROVENANCE, (Classification("Decision"),))
    return CandidateContext(request.identity, represented, "controlled-explicit-relevance", "governance",
                            authorities=authorities,
                            governance=(GovernanceAssessment(SUBJECT, governance, PROVENANCE),),
                            currentness=(CurrentnessAssessment(SUBJECT, currentness),))


def applicability(item: CandidateContext, **changes: object):
    fields: dict[str, object] = dict(
        bootstrap_valid=True, request_project=PROJECT_A, candidate_project=PROJECT_A,
        requester_authorized=True, consumer_disclosure_authorized=True,
        task_requires_current=True, task_domain="governance", task_phase="phase-4",
        task_action="audit", requires_governing_authority=True,
    )
    fields.update(changes)
    return evaluate_applicability(item, ApplicabilityInputs(
        relevance=RelevanceOutcome.RELEVANT, relevance_basis="controlled explicit task mapping",
        scope_matches_task=True, enforcement=EnforcementInputs(**fields),  # type: ignore[arg-type]
    ))


def expect(label: str, actual: object, expected: object, results: dict[str, object]) -> None:
    if actual != expected:
        raise AssertionError(f"{label}: expected {expected!r}, observed {actual!r}")
    results[label] = actual.value if hasattr(actual, "value") else actual


def main(output: Path) -> None:
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)
    results: dict[str, object] = {}

    expect("B1_matching", applicability(candidate()).outcome, ApplicabilityOutcome.APPLICABLE, results)
    expect("B1_scope_mismatch", applicability(candidate(authority="mismatch")).outcome,
           ApplicabilityOutcome.UNRESOLVED, results)
    expect("B1_unapproved_state", applicability(candidate(governance=GovernanceState.PROPOSED)).outcome,
           ApplicabilityOutcome.UNRESOLVED, results)
    expect("B1_absent_authority", applicability(candidate(authority="absent")).outcome,
           ApplicabilityOutcome.UNRESOLVED, results)
    expect("B1_historical_current_task", applicability(candidate(currentness=Currentness.HISTORICAL)).outcome,
           ApplicabilityOutcome.INAPPLICABLE, results)
    expect("B1_historical_task", applicability(candidate(currentness=Currentness.HISTORICAL),
           task_requires_current=False, task_is_historical=True).outcome, ApplicabilityOutcome.APPLICABLE, results)

    source = SQLiteStateStore(output / "source.sqlite")
    source.initialize()
    source.save_evidence(PersistedEvidence("ws3b-alpha", "historical-claim", "historical-only reference",
                                           currentness="current", authority_basis="claimed authority"))
    source.save_observation(PersistedObservation("ws3b-alpha", "observation-1", "source-1",
                            "2026-09-27T00:00:00+00:00", "observed", "historical observation"))
    source.save_artifact_evidence(PersistedArtifactEvidence("ws3b-alpha", "artifact-1", "artifact-version-1",
                                  "source-1", "docs/governance.md", "controlled historical evidence", "observation-1"))
    source.save_transformation(PersistedTransformation("ws3b-alpha", "transformation-1", "artifact-version-1",
                               "controlled-parser", "controlled-config", "succeeded", "inert transformation"))
    source.save_representation(PersistedRepresentation("ws3b-alpha", "representation-1", "artifact-version-1",
                                "ws3b-provenance", "lines:1-1", "represented historical information"))
    source.write_audit("ws3b-alpha", "governance-evaluated", "controlled minimized outcome")

    reloaded = SQLiteStateStore(output / "source.sqlite").restore_evidence("ws3b-alpha", "historical-claim")
    assert reloaded is not None
    expect("B2_reload_currentness", reloaded.currentness, "unknown", results)
    expect("B2_reload_authority", reloaded.authority_basis, None, results)
    expect("B2_project_scope_before_restore", source.restore_evidence("ws3b-beta", "historical-claim"), None, results)

    backup = output / "backup.sqlite"
    source.create_backup(backup, operator_authorized=True, purpose="ws3 lane b controlled validation",
                         retention_basis="ER-P4-3B-001")
    target = SQLiteStateStore(output / "restored.sqlite")
    target.initialize()
    qualification = target.restore_backup(backup, operator_authorized=True)
    restored = target.restore_evidence("ws3b-alpha", "historical-claim")
    assert restored is not None
    expect("B2_restored_currentness", restored.currentness, "unknown", results)
    expect("B2_restored_authority", restored.authority_basis, None, results)
    if "historical-only" not in qualification.qualification or "independent re-establishment" not in qualification.qualification:
        raise AssertionError("B2 recovery qualification did not preserve historical-only non-elevation")
    results["B2_recovery_qualification"] = "historical-only independent re-establishment"
    expect("B2_project_scope_after_restore", target.restore_evidence("ws3b-beta", "historical-claim"), None, results)

    reps = target.representations_for_project("ws3b-alpha")
    expect("B3_provenance_identity", tuple(item.provenance_identity for item in reps), ("ws3b-provenance",), results)
    expect("B3_other_project_representations", target.representations_for_project("ws3b-beta"), (), results)
    expect("B3_historical_governed_use", applicability(candidate(currentness=Currentness.HISTORICAL)).outcome,
           ApplicabilityOutcome.INAPPLICABLE, results)

    expect("B4_authorized_audit", target.audit_for_project("ws3b-alpha", authorized=True),
           (("governance-evaluated", "controlled minimized outcome"),), results)
    expect("B4_other_project_audit", target.audit_for_project("ws3b-beta", authorized=True), (), results)
    try:
        target.audit_for_project("ws3b-alpha", authorized=False)
    except PermissionError:
        results["B4_unauthorized_audit"] = "PermissionError"
    else:
        raise AssertionError("B4 unauthorized audit read unexpectedly succeeded")
    if hasattr(target.audit_for_project("ws3b-alpha", authorized=True), "authority"):
        raise AssertionError("B4 audit result unexpectedly contains Authority")
    results["result"] = "PASS"
    (output / "result.json").write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(results, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: control-runner.py OUTPUT_DIRECTORY")
    main(Path(sys.argv[1]))
