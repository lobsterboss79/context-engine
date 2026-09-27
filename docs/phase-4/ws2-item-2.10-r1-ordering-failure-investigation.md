# WS2 Item 2.10 — R1 Ordering-Failure Investigation

**Status:** **H3 / ROOT-CAUSE INVESTIGATION COMPLETE — PROJECT OWNER DISPOSITION REQUIRED**

## 1. Baseline, scope, and preserved failure

This is the Project Owner-authorized bounded root-cause investigation of
F-P4-2.10-R1-001. It is read-only as to preserved R1 evidence, the finding,
application, tests, fixtures, expected results, and controls. This record is
the sole investigation output.

| Field | Value |
| --- | --- |
| Committed investigation baseline | aeb2d59801370e660356a27e5407f2cead149798 — Correct Phase 4 F3 provenance verification. |
| Worktree at start | Only the uncommitted, preserved R1-01 evidence directory and R1 comparison-stop review. They are not altered. |
| F3 / implementation lineage | c7d17714a3983335f8564aa9360739d9ec785410 / IVB-P4-ORIGIN 9862497. |
| Repeatability-control materialization | 67bfeb74ef47ca050e12befe74707377e41e9340. |
| Execution boundary | No R1 rerun, R1-02/R1-03, or R2 activity occurred. |

VE-P4-2.10-R1-001 faithfully preserves Candidate/package order
CANVAS-HISTORY, DEPOT-UNVERIFIED, SEALED, TOTE. It failed the later R1
control's stated order SEALED, TOTE, CANVAS-HISTORY, DEPOT-UNVERIFIED. All
other stated R1-01 checks passed.

The authority hierarchy applied is: approved Phase 0–1 requirements and
semantics; Phase 2 architecture; Phase 3 design/closure; original FX-F3 v1
and ER-F3 v1; historical VE-F3-001; Item 2.10 analysis/control; then current
behavior. A later validation control cannot redefine an earlier semantic
requirement.

## 2. Ordering-semantic taxonomy

| Boundary | Governing record / rule | Result |
| --- | --- | --- |
| Represented-information input sequence | FX-F3 lists the four identities; historical procedure supplied SEALED, TOTE, CANVAS-HISTORY, DEPOT-UNVERIFIED. Neither calls that listing a Candidate/package canonical order. | It is a procedure/input sequence. |
| Candidate discovery | Phase 3 WS6: fixed mechanism order, then represented-information semantic identity, then Provenance semantic identity. | Every F3 Candidate is deterministic:literal, so identity gives CANVAS-HISTORY, DEPOT-UNVERIFIED, SEALED, TOTE. Provenance is the unused tie-break. |
| Applicability output | Phase 2 E8 and Phase 3 WS7 govern evaluation/outcomes, not an independent sort. Orchestration evaluates Candidate order. | Follows Candidate order. |
| Selected Context | Phase 2 E9/E10 and Phase 3 WS7 govern task-relative role; they do not require Required before Supporting in a selected tuple. Orchestration appends selected Candidates in traversal order. | Follows Candidate order; roles are Supporting, Supporting, Required, Required. |
| Logical package | Phase 1 requires Required/Supporting items and manifest; Phase 3 WS8 says package preserves selected items. No Phase 0–3 role-grouped package sort was found. Construction retains selected tuple. | CANVAS-HISTORY, DEPOT-UNVERIFIED, SEALED, TOTE. |
| Source Manifest | Phase 3 WS8 derives it from selected Provenance. Current construction sorts Source identity keys. | COMPETING, CURRENT, HISTORY, QUALIFICATION. This passed. |
| Renderer presentation | Phase 3 WS9 requires a deterministic package view retaining Required/Supporting items. Renderer stable-filters package items into Required and Supporting arrays. | It groups roles; it does not sort within a role. Required SEALED, TOTE; Supporting CANVAS-HISTORY, DEPOT-UNVERIFIED. |

Phase 0 permits Consumer packaging variation without changing meaning,
Provenance, Authority, or Uncertainty. Phase 1 distinguishes representation,
Candidate, selected Context, package, and rendering but provides no disputed
four-item sorting key. Phase 2 prohibits resolution of material Conflict by
order/model preference and defines roles as task-relative, but provides no
role-grouped Candidate/package order. Phase 3 WS6 is the controlling exact
Candidate order rule.

## 3. Original ER-F3 and historical raw-order reconstruction

ER-F3 v1 requires two current Approved decisions as unresolved Conflict, one
historical Supporting claim, unverified availability, distinct lineage,
Insufficient, and coherent_with_qualification. Its acceptance criterion says
“No newer-wins/order/model resolution” and requires Conflict participants,
currentness, historical role, Uncertainty, and Provenance to remain explicit in
logical package and renderings. It does not explicitly freeze SEALED, TOTE,
CANVAS-HISTORY, DEPOT-UNVERIFIED as Candidate or package-item order.

Historical VE-F3-001 raw raw-result.json preserves:

| Layer | Actual preserved order |
| --- | --- |
| Represented information | SEALED, TOTE, CANVAS-HISTORY, DEPOT-UNVERIFIED |
| Candidates | CANVAS-HISTORY, DEPOT-UNVERIFIED, SEALED, TOTE |
| Applicability / selection decisions | CANVAS-HISTORY, DEPOT-UNVERIFIED, SEALED, TOTE |
| Logical-package items | CANVAS-HISTORY, DEPOT-UNVERIFIED, SEALED, TOTE |
| Source Manifest | SRC-F3-COMPETING, SRC-F3-CURRENT, SRC-F3-HISTORY, SRC-F3-QUALIFICATION |
| Human / ChatGPT / Codex | Required SEALED, TOTE; Supporting CANVAS-HISTORY, DEPOT-UNVERIFIED |

The existing historical manifest records raw-result.json SHA-256
053648501a6536944d326dab40b471e77ac3dc9687b3ff244aa2e5ef95128db6.
All three historical renderer artifacts preserve the same role-grouped
presentation as R1-01. Historical VE-F3-001 therefore used the same observed
Candidate/package order as R1-01, not the later R1 expected order.

## 4. Item 2.10 expected-order origin

The Item 2.10 analysis was first committed at 25a25dd. It proposed semantic
comparison of Candidate, selection, package, and renderer order, but did not
state the disputed exact F3 sequence. The exact statement first appears in
the prepared-control commit 67bfeb74, repeatability-expected-results.md
lines 92–97: “The expected F3 order is the established canonical semantic
order from the result,” followed by SEALED, TOTE, CANVAS-HISTORY,
DEPOT-UNVERIFIED and separate Required/Supporting sequences.

Before that control, the same sequence appeared only as the FX-F3
represented-information listing and as the historical renderer's role-grouped
presentation. Historical raw Candidate/package evidence contains the different
mechanism/identity order. No Phase 1–3 record was found that promotes the
fixture listing or renderer grouping into Candidate/package canonical order.

The evidence therefore supports that the control conflated renderer
role-grouped order (and/or fixture input listing) with Candidate/package
canonical order. It does not support inheritance of that sequence from ER-F3
v1 semantics.

## 5. Current implementation and test trace

application.discovery.discover creates a key of first discovery-mechanism
ordinal, represented-information identity, and Provenance identity, and sorts
Candidate hits by that key. In F3 all mechanisms are literal, so the identity
key produces the observed alphabetical sequence.

application.orchestration.run_governed_render evaluates in Candidate order and
appends selected items in that order. application.package_construction.
construct_logical_package retains the selected tuple; its _manifest separately
sorts Source identities. application.rendering._package_payload stable-filters
package items into Required and Supporting arrays, grouping by role without
sorting inside roles.

This behavior is deterministic, explicit, and conforms to Phase 3 WS6. The
investigation found no evidence of filesystem enumeration, hash iteration,
SQLite row ID, frequency, recency, or score as the ordering mechanism.

tests/test_workstream_6.py asserts stable Candidate order by mechanism and
semantic identity, including equality with reversed inputs. This is supporting
implementation-intent evidence only. test_workstream_8.py checks Manifest
identity behavior but no general package-item ordering. test_workstream_9.py
checks shared renderer payload and role arrays with only one Required and one
Supporting item; it does not specify F3 Candidate/package order. No test
encodes the later Item 2.10 four-item expected order.

## 6. Materiality, classification, and finding review

Candidate order is semantically governed and material under Phase 3 WS6:
mechanism, represented-information identity, then Provenance identity.
Package order is materially distinguishable because implementation preserves
selected Candidate order. Renderer presentation is separately role-grouped;
Source Manifest order is separately Source-identity governed. These are not
one generic order.

The frozen R1 comparison correctly did not normalize a stated
Candidate/package-order mismatch. But the higher-authority trace establishes
that the frozen expected Candidate/package order was not the approved
governing order.

The root-cause classification is **D — MULTIPLE / COMPOUND ISSUE**:

1. **B — pre-results expectation/control-design error:** R1 asserted a
   Candidate/package sequence not required by ER-F3 v1 or Phase 0–3 ordering
   semantics.
2. **C — historical-evidence inconsistency requiring reconciliation:**
   VE-F3-001 preserves the same Candidate/package order as R1-01 while the
   later control called a different renderer/input-list sequence “established.”

**A — implementation/integration defect is not supported** by this evidence.

The finding assessment is **FINDING RECLASSIFICATION RECOMMENDED**. The
MATERIAL/H3 stop remains appropriate pending Owner review because a frozen
validation control conflicts with higher-authority records. The finding's
current primary INTEGRATION type is not supported by this trace and must not
be changed without disposition.

## 7. Prior-evidence impact and TD-14

| Prior item/evidence family | Impact | Basis |
| --- | --- | --- |
| Item 2.3 deterministic discovery | NO IMPACT | It relies on F2, not a claim that F3 uses renderer role order. |
| Item 2.4 Conflict/Uncertainty and VE-F3-001 | QUALIFICATION REQUIRED | Historical raw evidence is the reconciliation source. Its original criteria did not require the later exact package sequence; no invalidation follows. |
| Item 2.5 selection/sufficiency | NO IMPACT | Membership, roles, Conflict, Uncertainty, ASU basis, Insufficient, and coherence are unchanged. |
| Item 2.7 preservation | NO IMPACT | No material field was lost or changed. |
| Item 2.8 renderer fidelity | NO IMPACT | All renderers preserve role-grouped material presentation and the boundary. |
| Phase 3 WS6 ordering evidence | REVIEW REQUIRED | It is the governing ordering authority needing reconciliation with the R1 control. |

No prior evidence is automatically invalidated. TD-14 is **TRIGGER NOT MET**:
all relevant F3 information was discovered and preserved; this is an
expectation/order-taxonomy conflict, not material/repeated undiscoverability.

## 8. Consequences, non-selected options, and decisions required

R1 cannot continue under the conflicting frozen expectation. R2 remains not
authorized. Before future R1 activity, the Project Owner must decide how Phase
3 Candidate/package ordering, historical F3 evidence, and the Item 2.10
comparison contract are reconciled.

Non-selected possible paths are: preserve Phase 3 order and create a newly
governed pre-results control/ER correction; determine a higher-authority
requirement mandates another package order and separately authorize bounded
implementation remediation/retest; or require another narrow
record-authority investigation. None is selected or authorized here.

Required Owner decisions are: (1) finding disposition/reclassification;
(2) authoritative taxonomy for Candidate, selected/package, Manifest, and
renderer order; (3) whether a pre-results correction/reconciliation is
permitted; and (4) any later R1/R2 authorization. Item 2.10 remains
incomplete; Gate 4B is not approved; proving is not authorized; TD-14 remains
closed; production readiness is not established.

## 9. Non-change and non-execution attestation

This investigation did not modify preserved R1 evidence or the finding; alter
source, tests, fixtures, expected results, controls, checklist, or DVL-P4-001;
rerun R1; execute R2; remediate; invalidate evidence; approve a gate; authorize
proving; reopen TD-14; establish production readiness; commit; or push.

