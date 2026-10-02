# Phase 4 Gate 4B — Dependency, Parallelization, and Execution-Topology Plan

**Status:** **PLANNING COMPLETE — PROJECT OWNER EXECUTION-TOPOLOGY AUTHORIZATION REQUIRED**

## 1. Purpose, baseline, and non-execution attestation

This is a planning-only analysis of the next Phase 4 boundary, **Gate 4B —
Controlled Validation Acceptance & Proving Readiness**.  It neither performs a
Gate 4B obligation nor makes a Gate decision.  In particular, it creates no
Gate evidence, Finding, H3 record, DVL/TD state change, branch, worktree,
validation/proving activity, source/test change, WS5 activity, commit, or push.

The requested read-only baseline check returned no paths from `git status
--short`; the checked-out branch was `main`; and `git log -1 --oneline` was:

```
18b978f Close Phase 4 operational resilience validation
```

Thus the exact clean main baseline for any later authorized topology is
`18b978f`.  This record is a new, uncommitted planning artifact and must not be
treated as changing that recorded baseline or any governed status.

Controlling records read for this analysis were `AGENTS.md`; the Phase 4
checklist; roadmap/README Phase 4 status; WS1, WS2, WS3, and WS4 closures; the
WS1 validation-governance package; the Phase 2 validation/proving architecture;
`DVL-P4-001`; WS4 Item 4.7-A; the WS2/WS3/WS4 Finding/H3 dispositions; and the
WS4 post-integration corroboration successor.  Those records, rather than this
plan, remain the sources of authority.

## 2. Exact Gate 4B scope and obligation register

Gate 4B is a Project Owner acceptance/review gate, not a new validation
workstream.  The following **15** obligations enumerate the checklist language
once, including entry, review, conditional stop, and decision/consequence
controls.  `Assessment` means a bounded analytical review; it is not an
approval.

| ID | Checklist basis and purpose | Required inputs / evidence / output | Source of truth and dependencies | Nature and ownership boundary |
| --- | --- | --- | --- | --- |
| G4B-01 | Entry: establish that WS2–WS4 evidence was preserved and assessed under WS1 controls. | WS2–WS4 closures, their traceability, WS1 preservation/result rules; an evidence-completeness matrix. | Checklist Gate 4B entry; WS1; all three closures. Shared-foundation then both lanes. | Assessment; may reveal a Finding/H3. No DVL/TD change or proving/readiness authorization. Main-only final register. |
| G4B-02 | Entry protection: do not consume a fresh Consumer before PASS. | Current status and protected proving architecture; a retained prohibition statement. | Checklist Gate 4B/WS5; WS1 proving controls; Phase 2 I10–I12. No lane result is needed. | Control verification; no Finding normally. Main-only proving-boundary record. |
| G4B-03 | Owner review: assess evidence completeness. | G4B-01 matrix, closure records, targeted provenance/raw evidence only for gaps; proposed completeness assessment. | Checklist; WS1 §§1.3–1.5. Depends on G4B-01. | Assessment; provenance gap can create a Finding/H3. Lane A proposes; main reconciles. |
| G4B-04 | Owner review: assess the complete Finding inventory and disposition. | WS2–WS4 closure inventories; relevant closed finding records and remediation/retest lineage; proposed inventory. | Checklist; WS1 §§1.6–1.10; closures. | Assessment; can discover an open/new Finding. Lane B proposes; main owns final register. |
| G4B-05 | Owner review: determine whether any BLOCKER or MATERIAL Finding is unresolved. | G4B-04 inventory and governing closure/disposition evidence; proposed stop/no-stop assessment. | Checklist; WS1 finding lifecycle. Depends on G4B-04. | Assessment; an unresolved material condition is a stop, not a lane disposition. Main-only conclusion. |
| G4B-06 | Owner review: assess preservation of semantic invariants. | WS2 integrated-behavior closure; WS3/WS4 corroborating closure material; governing Phase 0–2 semantics; targeted original evidence if contradiction is alleged. | Checklist; WS1; Phase 2 architecture. | Assessment; contradiction can create Finding/H3. Lane A proposes; main reconciles. |
| G4B-07 | Owner review: assess security, governance, and isolation results. | WS3 closure, Item 3.9 review, relevant WS2/WS4 evidence and WS1 controls; proposed assessment. | Checklist; WS3 closure. | Assessment; a discrepancy can create Finding/H3. Lane A proposes; main reconciles. |
| G4B-08 | Owner review: assess failure and recovery results. | WS4 closure, Item 4.7-A, preserved Lane A/B non-PASS lineage, Lane C PASS, and post-integration successor; proposed assessment. | Checklist; WS4 closure. | Assessment; operational contradiction can create Finding/H3. Lane A proposes; main reconciles. |
| G4B-09 | Owner review: assess technology boundaries. | Phase 2 technology/proving architecture; WS2–WS4 closures; Item 4.7-A; proposed non-expansion assessment. | Checklist; Phase 2; Item 4.7-A. | Assessment; technology need is H3/Owner-decision territory. Lane B proposes; main-only conclusion. |
| G4B-10 | Owner review: assess unauthorized scope expansion. | Approved Phase 4 exclusions, WS2–WS4 closures, DVL and Item 4.7-A; proposed scope-integrity assessment. | Checklist; WS1 §1.16; Item 4.7-A. | Assessment; suspected expansion stops for H3. Lane B proposes; main-only conclusion. |
| G4B-11 | Owner review: assess TD-14 status. | TD-14 control/reopening rules, closures, DVL, and any deterministic-discovery evidence; proposed trigger assessment. | Checklist TD-14 control; WS1 §1.15; Phase 2 I15. | Assessment. A qualifying trigger stops the gate and requires governed reopening; lane may not change TD-14. Lane B proposes; main-only record. |
| G4B-12 | Owner review: assess justification for consuming a fresh-Consumer proving opportunity. | G4B-03 through G4B-11 proposed results; Phase 2 I10–I12 and WS1 proving architecture; a bounded rationale/limitations statement. | Checklist; Phase 2 I10–I12; WS1 §§1.12–1.14. Hard post-lane integration dependency. | Assessment only; does not reserve/expose/preflight a Consumer. Main-only. |
| G4B-13 | Conditional TD-14 control: if the material deterministic-discovery-deficiency threshold is met, stop, preserve, and reopen through governance. | Relevant authorized in-scope evidence showing material/repeated undiscoverability and material consequence; TD-14 Reopening Evidence Record if triggered. | Checklist; WS1 §1.15; Phase 2 I15. Conditional on G4B-11. | Executable stop/governance procedure, not normal lane work. Can create MATERIAL-or-higher Finding/H3; Owner review required; TD state cannot be changed by a lane. |
| G4B-14 | Required decision: Project Owner disposition of Gate 4B as PASS, HOLD, or FAIL. | Main-only reconciled Gate package, unresolved-condition register, and proving-readiness conclusion. | Checklist Gate outcomes/required decision. Depends on G4B-01–G4B-12 and no unresolved G4B-13 stop. | Project Owner only. It may affect whether preflight/proving can later be considered, but does not itself authorize them or establish readiness. |
| G4B-15 | Consequence control: even a PASS is required before actual preflight/proving and does not authorize remediation, technology change, or production readiness. | Gate decision record and a separate authorization decision if PASS. | Checklist Gate 4B and WS5/WS6 dependencies. Depends on G4B-14. | Main-only boundary control. No Gate lane may perform WS5/WS6 or claim production readiness. |

No Gate obligation independently changes `DVL-P4-001` or TD-14.  None grants
proving authorization or establishes production readiness.  Gate artifacts
should be owned only by future authorized Gate 4B lanes/main namespaces; no
existing closure, DVL, TD, source, or test file is an output target.

## 3. Current evidence base: available is not satisfied

| Evidence area | Evidence available now | What it supports for a later Gate assessment | It does **not** satisfy by itself |
| --- | --- | --- | --- |
| WS1 | Complete governance/evidence model and approved Gate 4A execution controls; preservation, PASS/FAIL/INDETERMINATE, Finding/H3, TD-14, and proving-protocol rules. | The criteria and lineage method by which Gate evidence is assessed. | Any Gate 4B review or decision. |
| WS2 | Owner-approved complete integrated behavior closure; preserved F4-E FAIL/remediation/PASS, F6-D INDETERMINATE/successor PASS, R1 FAIL/H3/superseding control/PASS; no required Finding open; active DVL. | Deterministic integration evidence and non-PASS lineage for G4B-01/03/04/06. | A universal direct-validation claim, DVL closure, Gate acceptance, or proving authorization. |
| WS3 | Owner-approved complete security/governance/isolation closure; PASS A/B successor/C; immutable `VE-P4-3B-001` INDETERMINATE retained; no open required Finding/H3. | G4B-01/03/04/07 and coherent qualified security evidence. | Conversion of the predecessor to PASS, Gate acceptance, or proving authorization. |
| WS4 | Owner-approved closed complete resilience closure; Lane A/B non-PASS lineages retained; Lane C PASS; `F-P4-4A-001` closed; successor corroboration PASS 12/12. | G4B-01/03/04/08, plus post-remediation corroboration. | An uninterrupted-PASS narrative, operational-policy need, Gate acceptance, or readiness claim. |
| PASS evidence | WS2/WS3/WS4 closure-listed PASS results, including WS4 successor 12/12. | Positive coverage, subject to lineage/completeness review. | Automatic satisfaction of Gate evidence-completeness or proving justification. |
| Preserved FAIL / INDETERMINATE | WS2 F4-E and R1 historical FAILs, F6-D INDETERMINATE; WS3 B-001 INDETERMINATE; WS4 Lane A/B and first corroboration non-PASS lineage. | Honest historical lineage, remediation/successor and procedure assessments. | Erasure, normalization, or automatic gate failure absent a current unresolved condition. |
| Findings / H3 | Expected current state verified in WS2/WS3/WS4 closures: no open required Finding, no open H3; closed records include `F-F4-E-001`, `F-P4-2.10-R1-001`, and `F-P4-4A-001`. | Starting inventory for G4B-04/05. | A substitute for a fresh cross-workstream audit. |
| DVL-P4-001 | **ACTIVE / ACCEPTED / DEFERRED** inaccessible-Source direct-validation limitation; supporting evidence only; visible downstream qualification. | G4B-03/10/12 limitation visibility. | Direct inaccessible-Source validation, DVL closure, a Finding/H3, TD-14 trigger, or proving/readiness acceptance. |
| TD-14 | **TRIGGER NOT MET / CLOSED / NOT REOPENED** across the closures and Item 4.7-A. | Starting state for G4B-11. | Immunity from re-evaluation if qualifying new evidence appears. |
| Remediation / corroboration | Closed WS2 finding remediations/retests; WS4 deterministic SQLite lifecycle remediation and successor corroboration PASS. | Closure lineage and evidence integrity review. | Alteration of predecessor outcomes or proof of any new operational policy. |
| Item 4.7-A | Owner-approved Result A: no material deferred operational need demonstrated. | G4B-08/09/10 evidence that WS4 did not demonstrate the named expansion need. | A production-readiness or future-infrastructure decision. |

## 4. Dependency DAG and critical path

```text
current clean main + frozen Gate foundation
                 |
      +----------+----------+
      |                     |
 Lane A: evidence/coherence  Lane B: limitations/Finding/boundaries
 G4B-01,03,06,07,08          G4B-02,04,05,09,10,11
      |                     |
      +----------+----------+
                 v
 main-only reconciliation: final evidence and condition register
                 v
 main-only G4B-12 fresh-Consumer justification
                 v
 conditional G4B-13 stop/reopen TD-14 if threshold is met
                 v
 Project Owner G4B-14 disposition
                 v
 G4B-15: separate authorization decision before any WS5/WS6 activity
```

| Dependency classification | Obligations |
| --- | --- |
| **NO DEPENDENCY** | G4B-02 can be drafted from current controls, but must be reconciled on main. |
| **SHARED-FOUNDATION DEPENDENCY** | G4B-01 and the evidence references used by G4B-03–G4B-11 require a frozen common obligation/evidence/limitation index. |
| **LANE DEPENDENCY** | G4B-03 depends on G4B-01; G4B-05 on G4B-04; G4B-13 conditionally on G4B-11. |
| **POST-LANE INTEGRATION DEPENDENCY** | G4B-12, the final form of G4B-03–G4B-11, and the unified discrepancy/Finding/H3 inventory require both lanes integrated. |
| **PROJECT OWNER DECISION DEPENDENCY** | G4B-13 if triggered, G4B-14, and any proving authorization following G4B-15. |

The critical path is foundation -> both bounded lane assessments -> main
reconciliation -> fresh-Consumer justification -> no-TD-stop determination ->
Project Owner Gate decision -> separate proving authorization.  The two lanes
are the only meaningful independent subgraphs.  All decision, status, and
proving-boundary work converges on main.

## 5. Recommended future topology: two bounded LNX-01 lanes

Two parallel analytical lanes are recommended after a centrally frozen
foundation.  One sequential lane would repeat the same evidence discovery but
avoid little material coordination; three lanes would split tightly coupled
cross-workstream acceptance judgments and create an extra reconciliation.
Windows is not needed: Gate review is documentary/analytical, and WS4 already
preserves the applicable Windows evidence.

| Lane | Owned obligations | Proposed branch / worktree | Future file and evidence ownership | Read-only dependencies / forbidden shared files | Stop conditions | Context |
| --- | --- | --- | --- | --- | --- | --- |
| **LNX-01-A — Evidence & Coherence** | G4B-01, G4B-03, G4B-06, G4B-07, G4B-08; bounded proposed assessments only. | `phase4-gate4b-evidence-coherence` / `~/Projects/context-engine-worktrees/phase4-gate4b-evidence-coherence` | Only `docs/phase-4/gate-4b-lane-a-evidence-coherence/` and its lane-local evidence index/review. | Common foundation; WS1–WS4 closures; targeted evidence named by closures. Forbidden: lane B, all common/main registers, checklist/README/roadmap, closures, DVL/TD, existing evidence, source/tests/`pyproject.toml`. | Evidence provenance gap, contradiction, unexpected FAIL/INDETERMINATE not already governed, new Finding/H3, remediation need, or boundary question. | **MEDIUM** — three closures plus selected lineages; raw evidence only on a specific discrepancy. |
| **LNX-01-B — Findings, Limitations & Boundaries** | G4B-02, G4B-04, G4B-05, G4B-09, G4B-10, G4B-11; bounded proposed assessments only. | `phase4-gate4b-findings-boundaries` / `~/Projects/context-engine-worktrees/phase4-gate4b-findings-boundaries` | Only `docs/phase-4/gate-4b-lane-b-findings-boundaries/` and lane-local inventories/reviews. | Common foundation; closures; DVL; TD-14 control; Item 4.7-A; Phase 2 I10–I12/I15. Same forbidden files as Lane A, including Lane A. | Apparent open BLOCKER/MATERIAL, H3, DVL reconsideration trigger, TD-14 threshold, scope/technology question, acceptance ambiguity, or need to amend a shared register. | **MEDIUM** — narrow closure/disposition and architecture passages; no routine raw-result review. |

Each lane should work vertically in one short-lived fresh Codex session:
analysis -> evidence inventory -> bounded review -> proposed disposition.  A
fresh session is preferable because neither needs the prior execution history;
the foundation and closure-first package prevent long-session context accretion.
Lane outputs must not assert Gate PASS/HOLD/FAIL, update shared status, close a
Finding, alter DVL/TD, or authorize proving.

## 6. Required shared foundation and file freeze

Before branching, main must pre-materialize and freeze a minimal common package
(this task does **not** create it):

1. `docs/phase-4/gate-4b-controls/obligation-register.md` — the 15-item
   register, source links, expected assessment outputs, and no-decision rule.
2. `docs/phase-4/gate-4b-controls/evidence-and-lineage-index.md` — closure-first
   map of WS2–WS4, PASS/FAIL/INDETERMINATE lineage, evidence IDs, and drill-down
   pointers; it must distinguish available evidence from satisfied obligations.
3. `docs/phase-4/gate-4b-controls/limitation-finding-h3-index.md` — DVL-P4-001,
   TD-14, closed/open Findings, H3 inventory, Item 4.7-A, and stop criteria.
4. `docs/phase-4/gate-4b-controls/lane-integration-contract.md` — ownership,
   freeze, evidence-lineage, stop, self-contained-commit, and integration rules.

These common files are main-only after materialization.  Every lane must treat
as read-only: `AGENTS.md`, `README.md`, `docs/roadmap.md`, the Phase 4
checklist, WS1–WS4 closures and their existing evidence/directories, the
validation-governance package, `DVL-P4-001`, TD-14 control, existing Findings,
Item 4.7-A, source, tests, and `pyproject.toml`.  Any required modification to
one is an immediate stop and integration/Owner dependency.

Main-only files, created only in a future authorized execution, should be
`docs/phase-4/gate-4b-controls/` and
`docs/phase-4/gate-4b-main-reconciliation/` (final inventory, discrepancy
register, readiness assessment, and Owner decision record).  This avoids shared
write ownership altogether.

## 7. DVL, TD-14, Finding/H3 treatment

`DVL-P4-001` is analyzed in Lane B as an active downstream qualification and
reconciled main-only.  It remains **ACTIVE / ACCEPTED / DEFERRED** unless either
its stated future trigger (a real approved distinct inaccessible-observation
capability) occurs or a Project Owner-approved governance/design decision meets
its closure criteria.  Neither Gate passage, proving consideration, nor nearby
PASS closes it.  Discovery of such a trigger stops the lane for Owner review.

TD-14 is analyzed in Lane B and recorded main-only.  Its current state is
**TRIGGER NOT MET / CLOSED / NOT REOPENED**.  Only evidence that relevant,
authorized, in-scope information necessary to Required Context or an approved
success criterion is materially or repeatedly undiscoverable through approved
deterministic mechanisms, with incorrect/insufficient context or material harm,
can trigger reconsideration.  Such evidence invokes G4B-13: stop, preserve,
create the required material Finding/reopening package, and obtain Project
Owner review.  No lane may reopen it or add AI/vector technology.

Lane B owns the cross-workstream Finding/H3 audit proposal.  Its minimum
package is the three closures, WS2 Item 2.11 final disposition, WS3 Item 3.9
review, WS4 Item 4.7-A and successor corroboration, relevant finding records,
and WS1 lifecycle rules.  Current expected state is verified by those closure
records: no open required Finding, no open H3, and `F-P4-4A-001` closed
Project-Owner approved (with the listed WS2 closed lineages retained).  A newly
discovered Finding/H3 stops its lane; main alone reconciles a cross-lane
condition and prepares any Owner decision material.

## 8. Proving-readiness and main-only boundary

Gate 4B may establish only **READY FOR PROJECT OWNER
PROVING-AUTHORIZATION DECISION**: a complete, coherent, lineage-preserved
validation package; no unresolved blocking/material condition; active limits
explicitly qualified; no ungoverned TD-14/scope/technology issue; and an
evidence-based justification that consuming a fresh Consumer is warranted.

That state is not **PROVING AUTHORIZED**.  Actual reservation, contamination
preflight, package delivery, or either WS6 exercise additionally require Gate
4B PASS and the applicable explicit Project Owner authorization.  It is also
not production readiness, which remains a separate Gate 4D Owner disposition.

The following stay main-only: cross-lane reconciliation; final Gate evidence
inventory and completeness conclusion; contradiction resolution; final
Finding/H3/DVL/TD register; final limitation acceptance; technology/scope and
TD-14 conclusions; fresh-Consumer justification; any Gate checklist/README/
roadmap update; Project Owner Gate disposition; and all authorization/readiness
statements.  No parallel lane can approve Gate 4B.

## 9. Future integration order and checks

1. Authorize/materialize the common foundation on clean `main`, then branch both
   lanes from that exact commit.
2. Each lane creates one self-contained, lane-private commit after its vertical
   bounded review.  No status files are changed.
3. Integrate Lane B first, then Lane A.  The order is not semantically material
   because ownership is disjoint; B first makes the condition/stop inventory
   available before the broader evidence-coherence review is reconciled.
4. On main only, perform the dedicated reconciliation.  Check all 15
   obligations exactly once; closure-to-evidence lineage; preserved non-PASS
   evidence; Finding/H3 counts; DVL/TD state; cross-workstream contradiction;
   technology/scope integrity; Item 4.7-A; and the proving-readiness boundary.
5. Prepare an Owner review package.  Do not alter status or begin proving until
   the Owner separately makes the required decision(s).

## 10. Context efficiency, drill-down rules, and stops

The pre-materialized closure-first index avoids making each lane reread Phase 4
history.  Both lanes need `AGENTS.md`, Gate 4B checklist language, their
foundation register, WS1 result/Finding/H3 controls, all three short closures,
and only their domain-specific records.  Lane A adds WS3 Item 3.9, WS4 Item
4.7-A/successor, and targeted evidence IDs.  Lane B adds DVL, TD-14 control,
WS2 Item 2.11, Phase 2 I10–I12/I15, and the named finding records.  Closure
records are sufficient for ordinary review.  Drill into raw evidence only for
an untraceable closure claim, a provenance/lineage gap, a claimed contradiction,
an uncertain PASS/FAIL/INDETERMINATE state, or a suspected Finding/H3/TD trigger.
This permits short, vertically focused fresh sessions without sacrificing
evidentiary sufficiency.

Universal future stop-and-preserve conditions are: unexpected FAIL; unresolved
INDETERMINATE; open material Finding; H3; contradiction across WS evidence;
DVL reconsideration trigger; TD-14 trigger; evidence-provenance gap; acceptance
ambiguity; source/test remediation need; unauthorized scope or technology
expansion; a material architecture/security/governance/policy decision; frozen
shared-file change; proving-authorization question; or production-readiness
question.  The concrete DVL, TD-14, H3, and evidence rules above refine those
conditions; none is waived for efficiency.

## 11. Exact Project Owner decisions and recommended next action

Before Gate work begins, the Project Owner must decide whether to authorize:

1. the two-lane topology, named LNX-01 worktrees, common foundation, freeze, and
   main-only integration contract;
2. the scope of bounded analytical Gate 4B execution under that contract;
3. any stop-triggered Finding/H3, DVL, TD-14, scope, technology, remediation, or
   policy decision if evidence requires one; and
4. after main-only reconciliation, the distinct Gate 4B PASS/HOLD/FAIL decision
   and, only after a PASS, any separate proving authorization.

**Recommended next action:** obtain Project Owner authorization for the stated
two-lane execution topology and its central foundation/freeze.  Only then
materialize the foundation on main and create the two worktrees.  Do not perform
proving, begin WS5, or make a production-readiness claim.
