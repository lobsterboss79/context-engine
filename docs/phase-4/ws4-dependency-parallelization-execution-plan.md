# Phase 4 WS4 — Dependency, Parallelization, and Execution-Topology Plan

**Status:** **ANALYSIS COMPLETE — PROJECT OWNER WS4 EXECUTION-TOPOLOGY / PLATFORM DECISION REQUIRED**

## 1. Baseline, authority, and non-execution attestation

This analysis was performed on Windows at `Z:\projects\context-engine` (the
corresponding required repository root is `/z/projects/context-engine`).  The
exact observed baseline was:

| Check | Observed value |
| --- | --- |
| Working tree | clean (`git status --short` produced no output) |
| Branch | `main` |
| Remote | `origin` fetch/push: `git@github.com:lobsterboss79/context-engine.git` |
| HEAD | `05e8d91 Close Phase 4 security governance isolation validation` |

The baseline satisfies the requested precondition. WS1, WS2, and WS3 are
complete; `DVL-P4-001` remains **ACTIVE — ACCEPTED / DEFERRED V0.1 VALIDATION
LIMITATION**; TD-14 remains **TRIGGER NOT MET — CLOSED / NOT REOPENED**; Gate
4B is **NOT APPROVED**; fresh-Consumer preflight/proving are **NOT
AUTHORIZED**; and production readiness is **NOT ESTABLISHED**.

This is a planning record only. It creates no WS4 control, fixture, expected
result, evidence, Finding, branch, worktree, execution, status change, Gate
activity, proving, remediation, commit, or push.

## 2. Exact WS4 scope and gate boundary

The controlling checklist states:

> **Objective:** After Gate 4A PASS and explicit execution authorization,
> validate approved failure, persistence, manual-backup, controlled-restore,
> recovery, and diagnostic behavior without expanding operational scope.

> **Dependencies:** Gate 4A PASS; authorized execution; WS1 controls;
> controlled non-production failure/recovery procedures.

| Item | Exact committed wording |
| --- | --- |
| 4.1 | “Validate malformed input, invalid configuration, and missing/unavailable Sources where applicable. Confirm that failure, absence, partial evidence, and successful completion remain distinct.” |
| 4.2 | “Validate interrupted operations, persistence integrity, transaction/partial-state behavior, and migration behavior where applicable using controlled procedures and preserved evidence.” |
| 4.3 | “Validate the existing manual backup capability and controlled restore only within the approved local/manual boundary.” |
| 4.4 | “Validate restored Project/Source state, Provenance, governance state, history, audit/construction evidence, and Project isolation as historical evidence where applicable.” |
| 4.5 | “Validate that restore does not manufacture currentness, Authority, Governance State, present authorization, or sufficiency; historical state remains historical until independently re-established.” |
| 4.6 | “Validate recovery after controlled failure and useful diagnostic/error behavior without treating diagnostics as durable audit or a recovery claim.” |
| 4.7 | “If evidence demonstrates a material need for backup scheduling, retention duration, deletion workflow, RPO/RTO, HA, daemon/service deployment, containers, cloud infrastructure, or an additional integration environment, stop and raise it through governance. Do not add it to Phase 4.” |

Completion evidence is exactly: “Failure/recovery matrix, backup/restore and
historical-state evidence, diagnostic results, operational limitations, and
findings register.” Item 4.7 is the WS4-specific H3 condition. Universal WS1
H3, expected-result, preservation, result-state, Finding, and remediation
rules also control every item.

Gate 4B entry is preserved WS2–WS4 evidence assessed under WS1 controls. Its
Owner review includes evidence completeness, Findings/unresolved
BLOCKER/MATERIAL Findings, semantic invariants, security/governance/isolation,
failure/recovery, technology boundaries, unauthorized expansion, TD-14, and
the justification for a fresh Consumer. A later Gate 4B PASS is required
before fresh-Consumer preflight/proving; it neither authorizes remediation nor
establishes readiness.

## 3. Governing-record map and recovery invariants

| Subject | Governing records and applicable rule |
| --- | --- |
| Evidence, expected results, result/Finding/H3 treatment | WS1 §§1.3–1.10; validation-governance package and templates. Preserve original FAIL/INDETERMINATE evidence; do not alter an ER to make execution pass. |
| Failure distinction and recovery | Phase 2 Domain G: ST-06; G6 CI-01–CI-05; G8 FR-01–FR-07; G10 OM-01–OM-04; G12 TV-03–TV-04. |
| Backup/restore boundary | Domain G G9 BR-01–BR-07; WS10 closure “Backup and controlled restore.” |
| Implemented v0.1 behavior | Phase 3 WS10: SQLite transaction rollback; no automatic retry; caller receives original failure; backup validates, stages, revalidates, then uses `os.replace`; restoration has historical-only qualification. |
| Runtime/technology boundary | Phase 2 Domain H: direct local Linux x86-64/Ubuntu non-root deployment; CPython/stdlib `sqlite3`, shell-free native Git; no new infrastructure. |
| WS2/WS3 inputs | WS2 closure; WS3 closure and Item 3.9 review; these are evidence inputs, not automatic WS4 closure. |
| DVL / TD-14 | Deferred-validation register DVL-P4-001; Phase 2 I15 / WS1 TD-14 template. |

The actual approved recovery invariants are: preserve distinct failure states;
do not make failed work appear successful (FR-01); distinguish last durable
from intended state (FR-02); do not strengthen Unknown/evidence (FR-03);
preserve isolation, authorization, sensitivity, secret exclusion, audit
protection, and governance (FR-04); prevent partial state from normal-complete
treatment (FR-05); make material recovery explainable (FR-06); and never
relax governance/security for availability (FR-07). WS10 additionally requires
restored state to remain historical-only until independent re-establishment;
backup is not Source truth, Authority, Governance State, currentness, receipt,
or use. Repeated observations remain distinct evidence and do not multiply
Authority. Diagnostics never substitute for durable audit.

## 4. Obligation decomposition

These labels are analytical aids, not new requirements.

| Obligation | Exact parent / semantic meaning | Evidence and likely method | Mode / reuse / control |
| --- | --- | --- | --- |
| 4.1-A | 4.1 malformed input | Frozen malformed input at CLI/configuration seam; preserved classified result. | Negative; deliberate; new lane control. |
| 4.1-B | 4.1 invalid configuration | Frozen invalid Bootstrap/configuration with no false readiness/success. | Negative; deliberate; new control. |
| 4.1-C | 4.1 missing/unavailable Sources | Controlled Source absence/unavailability; distinguish absence, unavailable, partial evidence and completion. | Negative/positive; existing evidence supporting only; new control if direct gap remains. |
| 4.1-D | 4.1 distinction requirement | Cross-case classification comparison; no collapse of failure, absence, partial evidence, success. | Static plus execution; new reconciliation control. |
| 4.2-A | 4.2 interrupted operations | Predetermined interruption at an approved seam, state inspection, preserved raw evidence. | Controlled failure/recovery; new control. |
| 4.2-B | 4.2 persistence integrity | SQLite/database integrity and semantic link checks after controlled failure. | Failure/static; new control. |
| 4.2-C | 4.2 transaction/partial state | Confirm no partial operation appears complete; explicit rollback/incomplete/isolation outcome. | Controlled failure/recovery; new control. |
| 4.2-D | 4.2 migration where applicable | Exercise supported migration path or freeze a static applicability determination if no migration is executable. | Conditional execution/static; new control. |
| 4.3-A | 4.3 existing manual backup | Create and validate a local/manual backup with explicit destination, purpose and retention basis. | Positive; deliberate; new control. |
| 4.3-B | 4.3 controlled restore | Validated, staged, authorized restore; no scheduler/remote/HA scope. | Positive/recovery; deliberate; new control. |
| 4.4-A | 4.4 restored Project/Source/Provenance/governance/history | Compare source and restore for retained historical evidence, Project association and isolation. | Positive/static; direct existing WS3 evidence is supporting only; new control. |
| 4.4-B | 4.4 audit/construction evidence | Confirm durable construction/audit evidence is preserved and access remains authorization-bound. | Positive/negative; new control. |
| 4.5-A | 4.5 no currentness/Authority/governance/present-authorization manufacture | Assert recovery qualification and denied/non-elevated state after restore. | Negative/recovery; WS3 B evidence is mechanism evidence only; new WS4 control. |
| 4.5-B | 4.5 no sufficiency manufacture | Assert historical restoration does not make a package sufficient/current without independent basis. | Negative/recovery; new control. |
| 4.6-A | 4.6 recovery after controlled failure | Frozen predecessor failure -> preserved evidence -> only pre-authorized successor/recovery. | Controlled failure/recovery; new control. |
| 4.6-B | 4.6 diagnostics/errors | Useful, secret-safe, correctly classified diagnostic/error output; no claim it is durable audit/recovery. | Failure/static; new control. |
| 4.7-A | 4.7 H3 boundary | Review all observed evidence for the enumerated operational/infrastructure need. | Post-lane static integration; no execution; shared integration control. |

## 5. Dependency graph

```text
WS1 controls + Gate 4A execution authority + frozen shared index
                              |
        +---------------------+---------------------+
        |                     |                     |
  A: 4.1-A..D          B: 4.2-A..D / 4.6-B     C: 4.3-A/B, 4.4-A/B,
  failure taxonomy       interruption/integrity       4.5-A/B, 4.6-A
        |                     |                     |
        +---------------------+---------------------+
                              v
           main-only failure/recovery inventory + 4.7 H3 review
                              v
                     WS4 evidence/closure review
                              v
                         later Gate 4B review
```

| Dependency | Classification | Why / boundary |
| --- | --- | --- |
| Every execution -> WS1 control, provenance and expected-result freeze | HARD / SHARED-GOVERNANCE | No result can be classified without it. |
| 4.1-A/B/C -> 4.1-D | HARD | The distinction comparison needs all applicable observed classes. |
| 4.2-A -> 4.2-B/C | SOFT / SEQUENCING | An interruption gives the strongest persistence/partial-state evidence, but static integrity control can be prepared independently. |
| 4.2-D | NO DEPENDENCY except applicability | Migration is conditional and must not be invented because numbered beside interruption. |
| 4.3-A -> 4.3-B -> 4.4/4.5 | HARD | There must be a validated backup before restore, and restore before restored-state claims. |
| 4.2-C -> 4.6-A | SOFT | Controlled failure can supply a recovery predecessor, but restore recovery is independently valid when frozen. |
| A/B/C outputs -> 4.7 and closure inventory | POST-LANE INTEGRATION | The H3/limitation decision and complete matrix require all observed results. |
| Path/replacement/interruption controls -> platform assignment | PLATFORM | Windows and Linux may differ materially. |
| Earlier evidence -> any direct WS4 conclusion | NO DEPENDENCY | It is candidate/supporting/mechanism evidence unless a frozen WS4 assessment declares a specific reuse. |

## 6. Existing-evidence reuse assessment

| Candidate | Classification | WS4 use / non-use |
| --- | --- | --- |
| F4-E-001 FAIL -> Finding -> authorized remediation -> F4-E-002 PASS | MECHANISM EVIDENCE | Strong immutable failure/remediation/retest lineage example; not WS4 operational closure evidence. WS4 must not assume remediation authority for an unexpected failure. |
| F6-D-001 INDETERMINATE -> corrected procedure -> F6-D-002 PASS | MECHANISM EVIDENCE | Shows preserved procedure-deficient predecessor and fresh successor; no direct recovery/backup claim. |
| R1 v1/v2 FAIL -> H3/Finding/investigation/control correction -> PASS | MECHANISM EVIDENCE | Demonstrates governed lineage, not an operational scenario substitute. |
| WS3 Lane B VE-P4-3B-001 -> Owner-approved successor VE-P4-3B-002 | MECHANISM EVIDENCE | Directly controls the predecessor/successor discipline; its restore assertions are SUPPORTING ONLY for WS4. |
| WS3 Lane B restore/persistence assertions | SUPPORTING ONLY | Relevant preservation/non-elevation mechanism but executed for WS3 trust-state scope, not WS4’s complete operational matrix. |
| Phase 3 WS10 tests/closure | SUPPORTING ONLY | Implementation-test input for backup, restore, migration, transaction and diagnostics; not Phase 4 integrated validation. |
| DVL-P4-001 | NOT APPLICABLE to closure, active qualification | It remains visible. It is neither a WS4 failure nor evidence that WS4 may relabel inaccessible/unavailable outcomes. |

## 7. Failure, recovery, and expected-result model

Supported WS4 domains are malformed input, invalid configuration,
missing/unavailable Sources, interruption, persistence integrity, partial
state, migration where applicable, manual backup, controlled restore,
historical restoration, diagnostic/error behavior, and the item-4.7 scope
boundary. Renderer, Consumer, unsupported capability, generic retry,
stale/corrupt state, and adapter domains are not independently added: they may
be evidence only where needed to faithfully exercise one listed obligation.

The safe injection layers are lane-private disposable fixture/input for 4.1;
application/SQLite persistence seam for 4.2; and disposable backup/target
directories for 4.3–4.6. Do not inject host-wide disk, permission, kill, or
environment failures; do not touch user/system data. The frozen procedure must
state its exact interruption boundary and cleanup/preservation behavior.

A control may expect a semantic state such as `DENIED`, `UNAVAILABLE`,
`INCOMPLETE`, `RECOVERY REQUIRED`, or an application-level failure. That is a
**scenario-expected failure state**. The **validation control FAIL** state is
reserved for preserved evidence not satisfying its frozen acceptance/negative
criteria. Every ER must state both separately before execution.

Only a pre-frozen sequence may run vertically:

```text
controlled failure attempt -> immutable predecessor evidence
-> predetermined, non-semantic recovery/successor procedure
-> independent successor evidence and classification
```

An unexpected product failure, unexpected INDETERMINATE, missing preservation,
or need to change source/test/ER is not a successor path: it is **STOP AND
PRESERVE** pending Project Owner disposition.

## 8. Platform matrix and required Owner decision

The approved v0.1 deployment target is direct local Linux x86-64/Ubuntu
non-root. Windows therefore may provide valuable preparation/static evidence,
but it cannot silently stand in for Linux runtime evidence where behavior turns
on OS filesystem, process, SQLite, shell, or atomic-replacement semantics.

| Obligation | Sensitivity | Windows execution valid? | Linux required? | Cross-platform useful? | Reason |
| --- | --- | ---:| ---:| ---:| --- |
| 4.1-A malformed input | PLATFORM-NEUTRAL | Yes | No | No | Controlled parser/input classification can be environment-recorded. |
| 4.1-B invalid configuration | WINDOWS-VALIDATABLE | Yes | No | Yes | Paths/environment and invocation syntax differ, but configuration semantics can be tested locally. |
| 4.1-C/D Source outcome distinction | CROSS-PLATFORM EVIDENCE DESIRABLE | Yes, for semantic cases | No | Yes | Path separators, case sensitivity, environment and native Git process behavior can affect a real Source error. |
| 4.2-A interruption | PLATFORM DECISION REQUIRED | Not sufficient alone | Yes for runtime claim | Yes | Signal/process termination and cleanup differ; approved runtime is Linux. |
| 4.2-B/C integrity and partial state | LINUX-SPECIFIC | Static/preparation only | Yes | Yes | SQLite locking/filesystem durability and process interruption matter to the claimed operational execution. |
| 4.2-D migration | LINUX-SPECIFIC if executed | Static applicability only | Yes if execution required | Yes | Schema/file replacement and runtime target govern fidelity. |
| 4.3-A/B backup/restore | LINUX-SPECIFIC | Static/control review only | Yes | Yes | Uses SQLite backup, staging in target directory and `os.replace`; Windows replacement/handle behavior differs. |
| 4.4-A/B restored evidence | LINUX-SPECIFIC | Static evidence comparison only | Yes | Useful | Depends on faithful restore execution. |
| 4.5-A/B non-manufacture | LINUX-SPECIFIC | Supporting semantic check only | Yes | Useful | Must follow a faithful restore in the approved runtime. |
| 4.6-A recovery | PLATFORM DECISION REQUIRED | Not sufficient alone | Yes for interrupted/replacement recovery | Yes | Predecessor/successor capture, process and temp cleanup are platform-sensitive. |
| 4.6-B diagnostics | WINDOWS-VALIDATABLE | Yes | No | Yes | Semantic diagnostic category/secret safety can be inspected, while paths/process text is platform-specific. |
| 4.7-A | PLATFORM-NEUTRAL | Yes | No | No | Governed review, not runtime validation. |

**Recommendation requiring Project Owner decision:** assign the execution parts
of Lanes B and C to **LNX-01**. Lane A can execute its platform-neutral and
Windows-validatable controls on this machine, with its Source case explicitly
recording Windows. The Owner must decide whether cross-platform corroboration
is desired for A/4.1-C and whether the Linux runtime evidence is required as
recommended. This is material platform fidelity, not a convenience choice.

## 9. Recommended topology, lanes, and vertical authority

**Maximum safe useful parallelism: three lanes, after one shared foundation.**
This matches three genuine domains; a separate 4.7 lane is not useful because
it is an integrated review, and splitting backup from restore creates a hard
handoff with little concurrency benefit.

| Lane | Ownership / purpose / platform / burden | Vertical authority after one explicit Owner authorization | Stops / output |
| --- | --- | --- | --- |
| A — Input, configuration & diagnostic distinctions | 4.1-A–D, 4.6-B. Windows; `MEDIUM`. Classify input/config/Source outcomes and diagnostic boundary. | Lane-private analysis -> ER/control/fixture -> freeze -> provenance preflight -> execute -> preserve -> classify -> bounded review. It may not recover an unexpected outcome. | Stops on unexpected result/ambiguity/Source classification conflict. Output: `VE-P4-4A-*` and lane matrix. |
| B — Interruption, persistence & partial state | 4.2-A–D. LNX-01; `HIGH`. Exercise controlled interruption and state integrity. | Same vertical path only for pre-frozen disposable injection/recovery sequence. Migration may execute only if frozen applicability says it exists. | Stops on host-level need, source/test change, unclear atomicity, unexpected failure/INDETERMINATE. Output: `VE-P4-4B-*`. |
| C — Manual backup, restore & historical recovery | 4.3-A/B, 4.4-A/B, 4.5-A/B, 4.6-A. LNX-01; `HIGH`. Validate manual/local restore and non-elevation. | Same vertical path; C may run its predetermined controlled-failure/recovery successor only if fully frozen before the first attempt. | Stops on invalid restore, unexpected replacement behavior, governed-state ambiguity, any need for scheduling/retention/deletion/RPO/RTO/HA/infrastructure. Output: `VE-P4-4C-*`. |
| Main-only integration | 4.7-A, WS4 matrix/inventory. Platform-neutral; `MEDIUM`. | No lane execution authority; reconciliation only after all parked lane products are integrated. | Stops on contradiction, scope/H3, unresolved result/Finding/platform insufficiency. Output: integration review and proposed disposition only. |

Each lane has Finding authority only to create a governed record when evidence
meets WS1 criteria; it has no material Finding disposition or remediation
authority. Failure-injection authority is only within its frozen disposable
boundary. Recovery authority is limited to the explicitly frozen sequence.

## 10. Shared controls, ownership, and worktrees

Recommend **Option C — hybrid**. First, main-only shared materialization
should freeze the one WS4 control index: exact baseline(s), lane/ER/fixture/VE
IDs, provenance fields, expected-state vocabulary, predecessor/successor
rules, platform assignments, common evidence contract, and main-only 4.7
integration contract. It produces no validation result. Each lane then owns
only its private fixtures, ERs, procedures, raw/derived evidence, and bounded
review.

| Namespace / file family | Owner / access |
| --- | --- |
| `docs/phase-4/ws4-validation-controls/` and this plan | main-only shared preparation/integration; lane read-only after freeze |
| `docs/phase-4/ws4-lane-a-input-diagnostics/`, `...ws4-lane-b-persistence/`, `...ws4-lane-c-backup-restore/` | respective lane only |
| `docs/phase-4/validation-evidence/VE-P4-4A-*`, `...4B-*`, `...4C-*` | respective lane only |
| Checklist, README, roadmap, WS1 package, WS2/WS3 closure/evidence, DVL, TD-14, shared Finding/register surfaces, source, tests, `pyproject.toml` | frozen/read-only to lanes |

No lane updates shared status or shared registers. No lane changes another
lane’s namespace. A successful lane parks as a self-contained product.

Suggested branches/worktrees, not created by this analysis:

| Platform | Branch | Worktree |
| --- | --- | --- |
| Windows | `phase4-ws4-input-diagnostics-win` | `/z/projects/context-engine-worktrees/ws4-input-diagnostics-win` |
| LNX-01 | `phase4-ws4-persistence-linux` | Linux-local `context-engine-worktrees/ws4-persistence-linux` |
| LNX-01 | `phase4-ws4-backup-restore-linux` | Linux-local `context-engine-worktrees/ws4-backup-restore-linux` |

All must originate from one named, clean, committed shared-foundation baseline.
Use distinct branch names across machines; no machine may assume another’s
unpushed work. A lane product is transferred only by an identified commit
whose parent traces to that baseline, then reviewed and integrated on main in
dependency order. No remote operation is authorized by this plan.

## 11. Context minimization and integration

Every lane needs only AGENTS.md; WS4 checklist; WS1 preservation/result/
Finding/H3 rules; Gate 4A boundary; WS2/WS3 closures; DVL/TD-14 state; its
frozen shared index; and its governing Domain G/WS10 excerpts. Lane A also
needs source/Bootstrap failure architecture. Lane B needs G6–G8 and SQLite
runtime seams. Lane C needs G8–G11, WS10 backup/restore, and WS3 historical
non-elevation evidence. Main integration needs lane outputs, not all raw Phase
1–3 records. This applies the **SMALLEST SUFFICIENT TRUSTWORTHY CONTEXT**
principle and avoids duplicated historical ingestion.

Recommended integration order is A, then B, then C (A has no hard predecessor;
B/C can be reviewed in parallel; C’s own internal backup->restore sequence is
hard). Main then performs one reconciliation: every obligation exactly once;
scenario-expected state vs validation result; failure/recovery and
predecessor/successor inventories; Finding/H3/DVL/TD-14 inventory; platform
coverage; cross-lane contradictions; and common operational invariants. Use
reviewed cherry-picks or reviewed merges only after each parked lane is
self-contained and based on the same foundation. Update shared status files
only after Project Owner disposition.

## 12. Universal stop conditions and closure/Gate prerequisites

**STOP AND PRESERVE** for unexpected FAIL or INDETERMINATE; H3; material
Finding; semantic/governance conflict; unexpected failure outside the frozen
injection boundary; recovery not pre-authorized; evidence preservation loss;
need for remediation/source/test/ER/shared-file change; cross-lane unresolved
dependency; platform mismatch; prior-evidence invalidation; a DVL decision;
TD-14 threshold; or any Gate/proving/readiness question. A lane may continue
automatically only after a faithful preserved result satisfies its frozen ER,
creates no stop condition, and remains inside its lane-private boundary.

WS4 can later be presented for closure only when every obligation is accounted
for; expected scenario states and validation results are correctly separated;
required immutable predecessor/recovery evidence is preserved; no failure
history is overwritten; Findings and INDETERMINATE lineages are dispositioned
or honestly preserved; no unresolved H3; DVL-P4-001 remains visible; TD-14 is
evaluated under its trigger; platform coverage matches the Owner decision;
applicable regression evidence and operational limitations are preserved; and
the main-only reconciliation finds no unresolved contradiction. This plan does
not close WS4.

If WS4 later closes, only the WS4 portion of Gate 4B’s WS2–WS4 evidence entry
condition becomes eligible. Gate 4B may then be one vertical main-only review
task after a separate Owner authorization, reviewing WS2, WS3, WS4, DVL,
Findings/H3, TD-14, technology boundaries, and fresh-Consumer justification.
The dependency remains:

```text
WS4 closure -> separate Gate 4B review/Owner decision -> possible later proving authorization
```

Neither arrow authorizes proving, preflight, remediation, or production
readiness.

## 13. Project Owner decisions requested

1. Approve, modify, or reject the recommended three-lane topology and hybrid
   shared-materialization strategy.
2. Make the material platform-fidelity decision: LNX-01 for Lanes B/C as
   recommended, and whether Windows/LNX cross-platform corroboration is needed
   for Lane A Source behavior.
3. Approve the lane ownership/freeze/worktree/cross-machine model and whether
   authorization covers shared preparation alone or preparation plus bounded
   lane execution under the stated stop conditions.
4. Confirm main-only post-lane reconciliation and a separate Owner disposition
   before WS4 closure consideration. Gate 4B, preflight/proving, and readiness
   remain outside this decision.
