# F-P4-2.10-R1-001 — Frozen F3 semantic-order mismatch

| Field | Record value |
| --- | --- |
| Finding ID | `F-P4-2.10-R1-001` |
| Linked evidence/result | `VE-P4-2.10-R1-001` — **FAIL** |
| Concise finding | The faithful R1-01 result orders Candidates and logical-package items as `RI-F3-CANVAS-HISTORY`, `RI-F3-DEPOT-UNVERIFIED`, `RI-F3-SEALED`, `RI-F3-TOTE`, not the frozen canonical semantic order. |
| Severity | **MATERIAL** — the mismatch is in governed Candidate/package semantic order and prevents the R1 acceptance condition. |
| Primary finding type | **INTEGRATION** |
| Owner/investigator | Project Owner / Codex evidence preservation |
| Cause analysis | Not determined. The preserved output establishes the mismatch only; it does not establish a root cause or authorize a change. |
| Status/lifecycle | **OPEN — PROJECT OWNER REVIEW REQUIRED** |
| Governed disposition | Pending Project Owner review. No remediation, control change, rerun, or expected-result revision is authorized. |
| Disposition authority | Pending |
| Remediation authorization | None |
| Remediation/retest evidence | None |
| Residual limitation | R1 cannot establish Item 2.10-A, 2.10-B, or 2.10-I while this failure remains. |
| Closure evidence | Pending governed disposition and any separately authorized work. |
| Lineage/related findings | R1 sequence stopped after R1-01; R1-02 and R1-03 were not executed; R2 was not executed. |

## H3 and Item 2.11 implication

H3 is triggered by the MATERIAL governed semantic-order mismatch. The required
Item 2.11 implication is preservation of this discrepancy and finding for
review; Item 2.11 work, remediation, and a rerun are not authorized here.
TD-14 is not implicated: this is not evidence that required information is
materially undiscoverable. `DVL-P4-001` remains active and unchanged.

## Project Owner disposition and reclassification

**Original classification preserved:** MATERIAL / INTEGRATION; H3 stop; OPEN
pending review. The Project Owner approved root-cause classification D:
pre-results validation-control design error plus historical-evidence
reconciliation requirement; implementation/integration defect is not
supported. Under the finding-register rule that severity, type, and disposition
are independent, severity remains **MATERIAL** pending a future closure
decision, while primary type is reclassified to **DESIGN** (validation control /
governance discrepancy). Status is **DISPOSITIONED — CONTROL CORRECTION
REQUIRED**. No product/application remediation is authorized.

The authoritative disposition is recorded in
[ws2-item-2.10-r1-ordering-failure-disposition.md](../../ws2-item-2.10-r1-ordering-failure-disposition.md).
The original R1-01 FAIL remains historically true against v1 and is not
retroactively changed.

## Project Owner-approved final lifecycle closure

**Historical lifecycle preserved:** original MATERIAL / INTEGRATION
classification, H3 stop, v1 FAIL, investigation, root-cause disposition, and
later MATERIAL / DESIGN reclassification remain intact.

**Final lifecycle state:** **CLOSED — PROJECT OWNER APPROVED.** The closure is
additive and does not alter the original evidence or classifications. Its basis
is the governed v2 control supersession; faithful R1 v2 execution with three
new independent PASS runs; mutually equal governed semantic projections; no
new semantic discrepancy; no required application remediation; and
established intended corrected-control behavior. See the
[post-R1 v2 results disposition](../../ws2-item-2.10-r1v2-post-results-disposition.md).

R1 v1 remains FAIL against its erroneous executed v1 control. R1 v2 PASS does
not retroactively convert that historical result to PASS. R2 v2 remains
unexecuted and separately authorized only by a future Project Owner decision.
