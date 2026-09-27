# Phase 4 WS3 — Dependency, Parallelization, and Execution-Boundary Plan

**Status:** **ANALYSIS COMPLETE — PROJECT OWNER WS3 EXECUTION-TOPOLOGY DECISION REQUIRED**

## 1. Baseline and exact WS3 scope

This analysis began clean on main at eb80a1d1cf52f9d1cf52f80a8771a8158b8b39ee — Close Phase 4 integrated behavior validation. WS2 is complete; DVL-P4-001 is active; TD-14 is closed/not reopened; Gate 4B and proving are not authorized.

WS3 objective: “After Gate 4A PASS and explicit execution authorization, validate integrated enforcement of approved security, governance, provenance, disclosure, and isolation semantics.”

Dependencies: Gate 4A PASS, authorized execution, WS1 controls, and controlled security/governance fixtures. Completion evidence: controlled positive/negative security and isolation evidence, enforcement-path explanation, disclosure results, and governed Finding disposition.

## 2. Exact checklist items

| Item | Controlling wording |
| --- | --- |
| 3.1 | Validate default Project isolation and fail-closed unauthorized cross-Project access. |
| 3.2 | Validate bounded cross-Project traversal only when the established task requirement, governed relationship, Requester authorization, and Consumer disclosure authorization prerequisites are present; validate denial when any prerequisite is absent. |
| 3.3 | Validate Requester authorization separately from Consumer disclosure authorization, including cases where Requester access does not permit disclosure to the Consumer. |
| 3.4 | Validate scoped Authority; Authority distinct from Governance State; current versus historical state; and denial of unsupported elevation. |
| 3.5 | Validate that restoration/persistence does not create currentness, Authority, Governance State, or present authorization. |
| 3.6 | Validate Provenance and governance-state enforcement, disclosure restrictions, and authorization-bound material metadata/audit handling within approved scope. |
| 3.7 | Validate Source-derived imperative/instruction-like content, including hostile/malicious instruction-like Source content within approved scope, remains evidence/content and does not establish governing instruction, Authority, or unauthorized action. |
| 3.8 | Validate preservation—not suppression—of Required Context, Conflict, Uncertainty, and material limitations under security/governance constraints; undisclosable or unavailable Required Context must affect qualification/sufficiency according to approved semantics. |
| 3.9 | Record unauthorized Consumer exposure attempts, denied paths, and any discrepancy/finding evidence without treating a denial as proof that all other paths are secure. |

There is no WS3-specific checklist H3 item. Universal H3 and WS1 result/Finding rules control every item. WS3 has no explicit dependency on WS4; Gate 4B entry requires WS2–WS4 evidence preserved and assessed.

## 3. Analytical obligation decomposition

These labels are planning aids, not additional requirements.

| Obligations | Governing Phase 1–3 record set | Required evidence / likely method |
| --- | --- | --- |
| 3.1-A default isolation; 3.1-B fail-closed unauthorized crossing | Phase 2 B7–B8; Phase 3 WS7 | Negative integrated denial. |
| 3.2-A task requirement; B governed relationship; C Requester authorization; D Consumer disclosure; E bounded traversal; F denial when any prerequisite absent | Phase 2 B7–B8; Phase 3 WS4/WS7 | One positive all-prerequisite case and controlled negative prerequisite cases. |
| 3.3-A Requester independent; B Consumer independent; C Requester allowance does not imply disclosure | Phase 2 B7; Phase 3 WS7 | Comparative authorization/disclosure denial. |
| 3.4-A scoped Authority; B Authority distinct from Governance State; C temporal state; D unsupported-elevation denial | Phase 2 B6/B12; Phase 3 WS2/WS7 | Mixed positive/negative enforcement. |
| 3.5-A persistence non-elevation; B restoration non-elevation; C Project-scoped historical state | Phase 2 B6 and Domain G; Phase 3 WS5/WS10 | Controlled semantic persistence/restore validation. |
| 3.6-A Provenance enforcement; B Governance-State enforcement; C disclosure restrictions; D authorization-bound metadata/audit; E approved scope | Phase 2 B9/B13–B14, Domain G; Phase 3 WS5/WS7/WS10 | Enforcement, denial, rendering/package and audit evidence. |
| 3.7-A imperative Source content remains content; B hostile content inert; C no instruction/Authority/action elevation | Phase 2 B11–B12; Phase 3 WS5/WS7 | Positive preservation and negative non-elevation. |
| 3.8-A Required; B Conflict; C Uncertainty; D limitations preserved; E undisclosable/unavailable Required Context affects qualification/sufficiency | Phase 2 B7–B14/E/F; Phase 3 WS7–WS9 | Security-boundary denial plus package/rendering qualification. |
| 3.9-A exposure attempts; B denied paths; C discrepancy/Finding evidence; D denial is not universal proof | WS1 §§1.3–1.11; all WS3 evidence | Integration inventory/documentation. |

All obligations require a frozen expected-result control before execution. Existing evidence may support a later coverage review but does not itself close a WS3 obligation absent a specific approved direct-evidence determination.

## 4. Dependency graph

    WS1 controls + Gate 4A authority + WS2 baseline
                         |
          +--------------+--------------+
          |              |              |
    A crossing       B trust/state    C inert content/
    3.1–3.3,3.6-C    3.4–3.6(A,B,D,E) preservation 3.7–3.8
          |              |              |
          +--------------+--------------+
                         v
             3.9 inventory and reconciliation
                         v
                   WS3 closure review
                         v
                 WS4 and Gate 4B review

3.1–3.3 have a soft sequencing dependency: the shared crossing family should establish default denial before permitted traversal and independent authorization cases. 3.4–3.6 also have soft sequencing: Authority/state facts inform enforcement/audit assertions, but separate controls can be frozen and executed independently. 3.7 and 3.8 have no hard dependency. Every lane has a hard dependency on the future shared control index/provenance convention, and 3.9 has a hard dependency on all lane results for completion. No item is dependent merely because it has a later checklist number.

## 5. WS2 dependency and reuse matrix

| WS3 area | WS2 use | Candidate / classification |
| --- | --- | --- |
| 3.1 | Direct baseline input | F5-A Atlas/Beacon exclusion is a direct candidate for bounded isolation, not automatic closure. |
| 3.2–3.3 | Supporting input | F5-A has absent relationship, denied Requester, and no disclosure; supporting only because it lacks all-prerequisite traversal and independent disclosure cases. |
| 3.4 | Supporting input | F3/R1/R2 currentness and governed pipeline; supporting only. |
| 3.5 | Supporting input | WS2 private state is not restoration semantic evidence; not applicable as direct closure evidence. |
| 3.6 | Supporting input | F1/F3/F5-A Provenance/package/rendering; supporting only. |
| 3.7 | No material WS2 dependency | No deliberate hostile-content evidence; not applicable. |
| 3.8 | Direct semantic input | F3 Conflict/Uncertainty, F4-B limitations, F5-A exclusion, Items 2.7/2.8; supporting only for security-constrained cases. |
| 3.9 | Direct mechanism input | F4-E, F6-D, R1, and Item 2.11 govern record preservation; direct candidate for mechanism only. |

R1/R2 repeatability is supporting only; it is not security evidence. DVL-P4-001 remains a carried qualification, not a WS3 control or a WS3 limitation. WS2 must not be rerun.

## 6. Recommended lanes and authority

**Recommend three execution lanes.** A separate 3.9 lane is not useful because its final inventory depends on all other lanes.

| Lane | Ownership | Purpose / context burden | Vertical authority after explicit execution approval |
| --- | --- | --- | --- |
| A — Crossing & Disclosure | 3.1, 3.2, 3.3, 3.6-C | Project isolation, bounded crossing, independent disclosure. **HIGH** | Analyze, prepare its controls, preflight, execute, preserve PASS evidence, and write bounded review. |
| B — Trust, State & Audit | 3.4, 3.5, 3.6-A/B/D/E | Authority/state/currentness, persistence/restore non-elevation, Provenance/governance/audit. **HIGH** | Same vertical path within lane-owned controls/evidence. |
| C — Inert Content & Qualified Preservation | 3.7, 3.8 | Inert hostile instructions and qualified preservation under denial. **MEDIUM** | Same vertical path within lane-owned controls/evidence. |
| Main integration | 3.9 | Complete inventory, reconciliation, shared status updates only after Owner review. **MEDIUM** | Analysis only until all lane outcomes and an Owner disposition exist. |

Every lane may create only lane-specific planning/control records under docs/phase-4/ws3-<lane>-* and evidence under docs/phase-4/validation-evidence/VE-P4-3-<lane>-*. It may create a Finding only if the existing WS1 governed threshold is met. It must not touch another lane or shared status/register files.

## 7. Control materialization, files, and worktrees

**Recommend Option C, hybrid.** First perform a main-only, Owner-authorized pre-materialization: one compact WS3 control index freezes the common baseline, stable lane/evidence IDs, provenance fields, and lane directory ownership. It creates no validation result. Then each lane owns and freezes its own fixture/ER/control family in its disjoint directory before executing. This preserves expected-result immutability without concurrent edits to shared WS2 fixture/ER registers.

Freeze: AGENTS.md; README; roadmap; checklist; WS1 governance package/templates/traceability; shared fixture/ER registers; DVL; shared Finding surfaces; source; tests; pyproject.toml; all WS1/WS2 evidence/findings; and all other lane directories. No lane needs a shared-register write during execution.

After shared pre-materialization, all worktrees must originate from one named clean main commit:

    main @ approved WS3 preparation baseline
    ├── phase4-ws3-crossing-disclosure
    ├── phase4-ws3-trust-state-audit
    └── phase4-ws3-inert-preservation

Suggested worktree paths: ~/Projects/context-engine-worktrees/ws3-crossing-disclosure, ws3-trust-state-audit, and ws3-inert-preservation. Existing WS2 worktrees must not be removed without a separate inspection and authorization.

## 8. Context minimization and stop conditions

Every lane needs AGENTS.md; the checklist WS3 section; WS1 preservation/result/Finding/H3 rules; Gate 4A boundary; WS2 closure; DVL/TD-14 state; and its governing Phase 2/3 records. Lane A additionally needs B7–B8, WS4/WS7, and F5-A. Lane B needs B6/B9/B13–B14/Domain G and WS5/WS7/WS10. Lane C needs B11–B12/E/F and WS5/WS7–WS9. Integration needs lane outputs and WS1 inventory rules, not all raw implementation context.

Universal stop-and-preserve conditions: FAIL; INDETERMINATE; MATERIAL/BLOCKER Finding or H3; semantic ambiguity; governance conflict; need for an unintegrated lane result; frozen shared-file modification; source/test remediation; architecture/technology/security-policy decision; prior-evidence invalidation; accepted limitation decision; TD-14 candidate; or Gate/proving/readiness question.

Lane A additionally stops if crossing prerequisites or Requester/Consumer separation are unclear. Lane B stops on restore/currentness/Authority/audit ambiguity or a need to alter persistence behavior. Lane C stops if preservation requires unsupported disclosure behavior or instruction-like content could invoke action. A faithful PASS under unchanged controls may continue automatically.

## 9. Synchronization, WS3 closure, WS4, and Gate 4B

Completed lane commits may remain parked. Review each self-contained commit, rebase on the approved preparation baseline if needed, then integrate reviewed commits in a non-conflicting order, preferably A, B, C. Cherry-pick or reviewed rebase/merge is acceptable; do not interleave unreviewed shared-file changes.

After all lanes are on main, perform one Item 3.9/cross-lane review: inventory every denial, exposure attempt, FAIL/INDETERMINATE, Finding, and disposition; confirm no denial is represented as universal security; reconcile common invariants; then make Owner-approved shared checklist/roadmap/register updates.

WS3 closure needs: all 3.1–3.9 obligations assessed; frozen-control traceability; preserved positive/negative evidence; closed/dispositioned Findings; honest INDETERMINATE treatment; no unresolved H3; TD-14 status; DVL carried forward; applicable regression evidence; and cross-lane reconciliation. It does not close DVL or approve Gate 4B.

WS4 is **INDEPENDENT PREPARATION POSSIBLE** only. Its failure/recovery planning may later run alongside late WS3 execution, but this plan grants no WS4 control, execution, or closure authority. Gate 4B remains **NOT APPROVED** and requires preserved/assessed WS2–WS4 evidence plus separate Project Owner review.

## 10. Risks, Owner decisions, and non-change attestation

Primary risks are shared-control conflict, overclaiming F5-A reuse, confusing WS3 persistence semantics with WS4 operational recovery, and treating a denial as universal security. The hybrid control strategy, freeze, and post-lane reconciliation mitigate them.

Project Owner decisions requested:

1. Approve three lanes and reserve Item 3.9 for post-lane integration.
2. Approve hybrid main-only pre-materialization plus lane-owned controls/evidence.
3. Approve lane names, ownership, freeze, worktree model, and vertical PASS authority.
4. Decide whether the next authorization covers shared preparation only or preparation plus execution under the stated stops.
5. Require cross-lane reconciliation and Owner disposition before WS3 closure; do not authorize WS4 or Gate 4B.

This document is planning only. No WS3/WS4 control, fixture, ER, validation, test, Finding, branch, worktree, source/test/checklist/register/DVL change, TD-14 action, Gate action, proving, or readiness action occurred.

