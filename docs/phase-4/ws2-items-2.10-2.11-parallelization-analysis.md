# WS2 Items 2.10 / 2.11 — dependency and parallelization analysis

**Status:** **ANALYSIS COMPLETE — PROJECT OWNER PARALLELIZATION DECISION REQUIRED**

## 1. Baseline and current state

This analysis begins at clean committed `HEAD` `37ae192ed900e2e1f372988befbd64c94acde5fd`.
Phase 4 is in progress; WS1 and WS2 Items 2.1–2.9 are complete; Item 2.10 is
in progress; and Item 2.11 is incomplete. R1 v2 is PASS and its disposition
records A/B as directly validated and I as directly validated for
identical-input stability only. R2 v2 is frozen/not executed. Gate 4B is not
approved; proving is not authorized; TD-14 is closed/not reopened;
`DVL-P4-001` is active/unchanged; readiness is not established.

This is dependency analysis only, not R2, Item 2.11, remediation, branch, or
worktree authorization.

## 2. Exact Item 2.11 wording and stable decomposition

The committed checklist says:

> **2.11 [VAL][DOC] Preserve all discrepancy evidence and create findings for
> differences from predetermined expected results, unexpected instability,
> missing qualification, or evidence gaps. Do not normalize fixture data or
> revise expected results solely to obtain PASS.**

The following labels organize that wording only:

| Obligation | Stable analysis-only meaning |
| --- | --- |
| 2.11-A | Preserve original evidence for every discrepancy. |
| 2.11-B | Create/govern a finding for a difference from a predetermined expected result. |
| 2.11-C | Create/govern a finding for unexpected instability. |
| 2.11-D | Create/govern a finding for missing qualification. |
| 2.11-E | Create/govern a finding for an evidence gap. |
| 2.11-F | Do not normalize fixture data or revise expected results merely to obtain PASS. |

WS1 supplies the evidence-preservation, expected-result, result-state, finding
lifecycle, H3, and remediation/retest mechanism. Relevant Phase 1–3
foundations preserve the distinctions among source, representation, Candidate,
selection, package, rendering, delivery/receipt/use, qualification, Provenance,
audit, failure history, and governed correction lineage. Item 2.11 does not
create remediation authority.

## 3. Obligation-level dependency matrix

| Obligation | Dependency on final 2.10 | Why / permitted boundary |
| --- | --- | --- |
| 2.11-A | **POST-2.10 INTEGRATION DEPENDENCY** | Mechanism/inventory analysis can proceed now; complete WS2 inventory must include future R2 evidence. |
| 2.11-B | **SOFT / SEQUENCING DEPENDENCY** | F4-E and R1 v1 support mechanism analysis now; any R2 expected-result discrepancy is a later input. |
| 2.11-C | **HARD DEPENDENCY for an R2-specific instance; NO DEPENDENCY for mechanism analysis** | R2's actual instability outcome is unknowable until executed. |
| 2.11-D | **NO DEPENDENCY** | Existing F3/F4 qualification evidence and F4-E's historical omission/retest lineage support analysis now. |
| 2.11-E | **POST-2.10 INTEGRATION DEPENDENCY** | Existing gaps can be inventoried now; final completeness must consume the R2 outcome. |
| 2.11-F | **NO DEPENDENCY** | WS1 plus F4-E and R1 v1/v2 already govern/provide examples of anti-normalization. |

This distinguishes validating the Item 2.11 mechanism from final Item 2.11
completeness across all WS2 findings. Only the latter waits for R2.

## 4. Existing evidence candidates

| Lineage | Legitimate Item 2.11 relevance | Candidate strength |
| --- | --- | --- |
| F4-E: FAIL → MATERIAL / INTEGRATION finding → approved remediation → PASS retest → closure | Original-evidence preservation, finding lifecycle, authorized remediation/retest, and no rewrite of the FAIL. | Direct candidate for A/B/F process; supporting for final completeness. |
| F6-D: INDETERMINATE procedure issue → correction → PASS | Preserved indeterminate result and correction/retest without treating the predecessor as PASS. | Direct candidate for A/F process; supporting for gap/procedure analysis. |
| R1 v1: FAIL → MATERIAL/H3 → investigation → DESIGN reclassification → v2 supersession → three-run PASS → closure | Preserves an erroneous control, prohibits normalization, distinguishes design from implementation defect, and closes only after corrected evidence. | Direct candidate for A/B/C/E/F mechanism; supporting for final completeness. |

No lineage is reclassified by this analysis.

## 5. Parallel work-category matrix

| Item 2.11 activity | May begin now? | Boundary |
| --- | --- | --- |
| Evidence-coverage analysis | **YES** | Inventory committed evidence and explicitly defer R2. |
| Governing-semantics analysis | **YES** | Trace approved WS1 and Phase 1–3 records without changing them. |
| Existing-finding inventory | **YES** | Read-only; do not reclassify or close records. |
| Fixture/control design | **CONDITIONAL** | Only after a governed gap and separate Project Owner authorization. |
| Expected-result preparation | **CONDITIONAL** | Same condition; never derive it from desired results. |
| Validation execution | **NO** | Requires a frozen, authorized control and applicable execution authorization. |
| Post-results classification | **CONDITIONAL** | Existing evidence needs a bounded Owner disposition; R2-specific classification waits. |
| Final Item 2.11 closure | **NO** | Must reconcile final R2/2.10 evidence and all WS2 discrepancies. |

## 6. Recommended parallel lanes and ownership

| Lane | Permitted independent scope | Create/modify ownership |
| --- | --- | --- |
| A — Item 2.10/R2 v2 | Separately authorized R2 execution, R2 evidence, R2-specific comparison/finding records, and post-R2 Item 2.10 review. | `docs/phase-4/validation-evidence/VE-P4-2.10-*`; `docs/phase-4/ws2-item-2.10-*`; authorized Item 2.10-specific finding records only. |
| B — Item 2.11 | Existing-lineage inventory, governing/coverage/dependency analysis, and only if separately authorized Item 2.11 preparation. No final-completeness claim. | `docs/phase-4/validation-evidence/VE-P4-2.11-*`; `docs/phase-4/ws2-item-2.11-*`. |

**Shared-file freeze:** neither lane changes `AGENTS.md`, `README.md`,
`docs/roadmap.md`, the Phase 4 checklist, governance-package templates or
traceability, shared fixture/expected-result registers, deferred-limitations
register, application/source, tests, `pyproject.toml`, or existing
evidence/finding directories (including F4-E, F6-D, and R1 v1/v2). Shared
status/register/checklist updates are later integration work only.

## 7. Git worktree model and integration

```text
main @ one clean committed baseline
├── phase4-item-2.10-r2
└── phase4-item-2.11
```

Two worktrees from one exact clean committed baseline are viable. Lane B needs
only already committed WS1, Items 2.1–2.9, F4-E/F6-D/R1 lineages, and R1 v2
disposition; it needs no uncommitted or future R2 state if it defers final
completeness and R2-specific classification.

Recommended integration: review self-contained changes, rebase each branch on
current main, and merge in dependency order—Lane B independent analysis/
preparation if accepted, Lane A R2 evidence/results, then one dedicated
cross-lane reconciliation and any authorized shared-file updates. A reviewed,
self-contained commit may instead be cherry-picked; do not interleave
unreviewed shared-file changes.

## 8. Mandatory stop conditions

Either lane stops and preserves work for Project Owner review on FAIL,
INDETERMINATE, H3, new finding, semantic ambiguity, governance/control
conflict, need for other-lane information, shared-file modification, possible
prior-evidence invalidation, source/test remediation, architecture/technology/
security/scope decision, TD-14 threshold, or Gate/proving/readiness decision.
It may continue only through already-governed PASS transitions within its
authorization and ownership boundary.

## 9. Integration boundary and recommendation

After independent work, review R2 results and R2-specific discrepancy evidence;
Item 2.11 mechanism/coverage analysis; every WS2 finding lineage; and
shared-file impact. Integrate Lane B analysis before final Item 2.11
completeness review; integrate Lane A R2 result before Item 2.10 final
disposition; then conduct one cross-lane reconciliation and obtain required
Project Owner dispositions.

Final WS2 closure still requires final Item 2.10 disposition, complete Item
2.11 evidence/finding coverage, and all other WS2 completion evidence. Gate 4B
preparation may begin only after that evidence exists and separate Owner review
is authorized.

**Recommended Project Owner decision:** authorize two worktrees from one named
clean baseline only with Lane B initially limited to analysis, existing-finding
inventory, and coverage/preparation documentation; retain R2 and every
R2-derived finding exclusively in Lane A; freeze shared files; and require the
integration review before Item 2.11 final disposition or gate action.

## 10. Non-change attestation

No R1, R2, or Item 2.11 validation executed; no fixture, control, expected
result, source, test, checklist, README, roadmap, branch, worktree, finding,
DVL, TD-14, gate, proving, or readiness state changed by this analysis.
