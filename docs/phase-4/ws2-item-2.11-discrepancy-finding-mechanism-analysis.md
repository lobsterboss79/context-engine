# WS2 Item 2.11 — Discrepancy and Finding Mechanism Analysis

**Status:** **INDEPENDENT MECHANISM ANALYSIS COMPLETE — FINAL ITEM 2.11
COMPLETENESS DEFERRED PENDING R2 v2 AND CROSS-LANE RECONCILIATION.**

## 1. Scope, authority, and boundary

This Lane B record analyzes already committed evidence only.  It does not
execute Item 2.11, create a new validation-evidence directory, alter a
fixture, expected result, finding, remediation, control, application, test,
or shared register, or make a final Item 2.11 completion claim.

The applicable scope is checklist Item 2.11:

> Preserve all discrepancy evidence and create findings for differences from
> predetermined expected results, unexpected instability, missing
> qualification, or evidence gaps. Do not normalize fixture data or revise
> expected results solely to obtain PASS.

The [parallelization analysis](ws2-items-2.10-2.11-parallelization-analysis.md)
permits this mechanism/inventory analysis, but makes complete evidence
inventory and final Item 2.11 disposition post-2.10 integration work.  R2 v2
is not an input to this record and remains exclusively in Lane A.

The governing preservation, expected-result, result-state, finding-lifecycle,
H3, and remediation/retest rules are WS1 sections 1.3–1.11 in the
[validation-governance/evidence model](workstream-1-validation-governance-evidence-model.md)
and its [governance package](validation-governance-package/README.md).  The
Phase 1–3 foundations applied here preserve evidence boundaries and
qualifications rather than converting them to absence or success; the
[Phase 1 material-findings audit](../phase-1/item-59-material-findings-disposition-audit.md),
[Phase 2 discovery/sufficiency architecture](../phase-2/discovery-selection-sufficiency-architecture.md),
and Phase 3 [WS6](../phase-3/workstream-6-deterministic-discovery.md),
[WS8](../phase-3/workstream-8-sufficiency-package-construction.md), and
[WS9](../phase-3/workstream-9-consumer-rendering-orchestration.md) are the
read-only foundations applied.  In particular, Phase 2 treats negative results
as evidence-boundary-relative; WS6 requires preservation of
fixture/request/evidence/scope/result evidence at the TD-14 threshold; and
WS8/WS9 require material package and rendering qualifications to remain
explicit.

## 2. Method and evidence-integrity basis

The complete committed lineages below were inspected, including their evidence
records, finding/remediation/disposition records where present, frozen-control
records, raw execution procedures, streams, raw results or preserved absence
of a raw result, renderings, state artifacts, and hash manifests.  The raw
evidence directories themselves remain read-only.  This record does not
reclassify a historical result, finding severity/type, or disposition.

| Lineage | Original result | Subsequent governed state | Item 2.11 relevance |
| --- | --- | --- | --- |
| F4-E | `VE-F4-E-001` **FAIL** against frozen `ER-F4-E v1` | MATERIAL / INTEGRATION finding; Owner-authorized correction; `VE-F4-E-002` **PASS** retest; finding closed | Direct preserved product/integration discrepancy and missing-qualification example |
| F6-D | `VE-F6-D-001` **INDETERMINATE** because procedure inputs did not faithfully materialize frozen Supporting role | Corrected disposable procedure; unchanged fixture/ER; `VE-F6-D-002` **PASS**; no product finding | Direct procedure/evidence-gap preservation example, not a product discrepancy |
| R1 v1/v2 | `VE-P4-2.10-R1-001` **FAIL** against its v1 control | MATERIAL/H3 finding; root-cause investigation and MATERIAL / DESIGN reclassification; Owner-approved v2 control; three v2 **PASS** runs; finding closed | Direct control-discrepancy/supersession and anti-normalization example; no observed instability finding |

## 3. Reconstructed F4-E lineage

`FX-F4-E v1` and `ER-F4-E v1` were frozen before `VE-F4-E-001`.  The original
raw evidence, streams, state, renderings, controlled-input hashes, and raw
hash manifest remain under `VE-F4-E-001/raw` and `derived`.  The original
record reports a faithful **FAIL**: the package/renderings omitted the broad
known-incomplete ASU limitation, broad Insufficient state, and no-release
qualification even though the bounded task result remained conditionally
sufficient.  The raw stdout retains both bounded and broad sufficiency values;
the original result was not replaced or made PASS.

`F-F4-E-001` preserved that failure as **MATERIAL / INTEGRATION**, identified
the missing two-scope qualification, and retained the original classification
after closure.  The Project Owner authorized only preservation of the
already-established construction qualification through the existing package
and rendering path.  `R-F4-E-001` records the bounded change and retest
requirements.  The independent `VE-F4-E-002` retest used unchanged frozen
fixture/ER hashes, passed all criteria, and explicitly states that the original
FAIL remains immutable.  The finding is closed on the resulting retest and
regression evidence, not erased.

This deliberately demonstrates:

| Obligation | Determination |
| --- | --- |
| 2.11-A | **Direct.** Original discrepancy evidence, including raw artifacts and hashes, is retained after correction/retest. |
| 2.11-B | **Direct.** A frozen-ER difference produced and governed `F-F4-E-001`. |
| 2.11-D | **Direct.** The finding is specifically a missing material qualification; its absence was neither treated as harmless nor concealed by bounded PASS-like facts. |
| 2.11-F | **Direct.** Neither `FX-F4-E v1` nor `ER-F4-E v1` was changed to obtain PASS; correction and separate retest followed Owner authorization. |

F4-E is not evidence of unexpected instability (2.11-C) or an evidence-gap
finding (2.11-E); it must not be reclassified to manufacture either example.

## 4. Reconstructed F6-D lineage

`VE-F6-D-001` preserves the frozen `FX-F6-D v1` / `ER-F6-D v1` identity,
controlled hashes, raw procedure, state, renderings, zero-byte stdout, and
terminating stderr.  Its procedure used positional `RoleInputs(False, True,
False, ...)`; the second input triggered Required rather than the frozen
Supporting mapping.  The resulting absence of a completed faithful
`raw-result.json` and the non-frozen role input made a criterion-level PASS or
fixture/product FAIL invalid.  The record therefore classified the attempt
**INDETERMINATE**, expressly preserved it, and stopped.

The successor `VE-F6-D-002` preserved the original INDETERMINATE and used a
new disposable procedure with named inputs plus a role-input preflight.  It
used unchanged F6-D fixture, request, ASU basis, Source, and ER hashes, then
produced separate raw evidence and a faithful **PASS**.  No Finding Record was
created: the record explicitly limits the issue to contained execution
procedure/evidence deficiency and does not attribute a frozen-control or
product violation to the Context Engine.

This deliberately demonstrates:

| Obligation | Determination |
| --- | --- |
| 2.11-A | **Direct.** The INDETERMINATE attempt and all available raw evidence remain preserved after the later PASS. |
| 2.11-E | **Mechanism-supporting, not direct finding-instance validation.** It identifies and governs a specific evidence/procedure gap—the missing faithful Supporting-role execution—without falsely converting it into a product discrepancy. It has no Finding Record, so it cannot itself demonstrate creation of an evidence-gap finding. |
| 2.11-F | **Direct anti-normalization example.** Fixture and ER stayed frozen; the procedure was corrected and executed anew rather than revising expected results or calling the predecessor PASS. |

The F6-D lineage does not demonstrate 2.11-B, 2.11-C, or 2.11-D.  In
particular, an execution-procedure defect is not automatically a product
finding, and treating it as one would contradict its preserved disposition.

## 5. Reconstructed R1 v1/v2 lineage

The frozen v1 R1 control and expected result were executed faithfully in
`VE-P4-2.10-R1-001`.  Its controlled F3 hashes, isolated execution procedure,
raw result, state, renderings, streams, derived semantic projection, and hash
manifest are preserved.  The result was **FAIL** because Candidate and
logical-package order followed the governing deterministic discovery order
but differed from the v1 control's erroneous unified order.  The finding was
recorded **MATERIAL / INTEGRATION**, H3 stopped further runs, and neither the
control nor expected result was changed in the original result.

The bounded investigation traced the higher-authority ordering taxonomy and
historical F3 raw evidence.  The Project Owner disposition preserved the
historical classification while reclassifying the primary type to **DESIGN**:
a validation-control/governance discrepancy, not a supported product defect.
It authorized a new, pre-results superseding v2 control only.  The v2 control
separated Candidate/traversal/package, Source Manifest, and renderer order
domains; it did not rewrite v1 or treat its FAIL as v2 success.

Three fresh isolated v2 executions (`R1V2-01` through `-03`) each preserve
their raw procedure, streams, raw result, state, renderings, semantic
projection/assessment, and manifests.  Each passed the v2 control and their
governed semantic projections were equal.  The Owner then closed the finding
additively.  The final disposition explicitly retains v1 as an immutable FAIL
against the erroneous executed v1 control.

This deliberately demonstrates:

| Obligation | Determination |
| --- | --- |
| 2.11-A | **Direct.** The original v1 discrepancy, its raw evidence, H3 history, and classification history remain after supersession and closure. |
| 2.11-B | **Direct.** The frozen expected-result/control difference created a MATERIAL finding and Owner-governed disposition. |
| 2.11-C | **Not directly demonstrated.** The three v2 runs demonstrate expected identical-input semantic stability; the v1 failure was a control-design mismatch, not an observed unexpected instability. No unexpected-instability finding exists in this lineage. |
| 2.11-E | **Mechanism-supporting, not direct finding-instance validation.** Investigation established a validation-control/governance evidence reconciliation need and governed a superseding control. It is not an evidence-gap Finding Record and must not be relabelled as one. |
| 2.11-F | **Direct.** The expected result was not silently rewritten to make R1 v1 pass. A separately Owner-approved v2 control was frozen before three new executions; v1 remains FAIL. |

## 6. Mechanism-validation conclusion and remaining boundary

Existing committed evidence directly validates that the approved mechanism can
preserve original discrepancy evidence, govern a finding for a frozen expected
result difference, govern missing qualification, and prevent normalization of
fixtures/expected results merely to obtain PASS.  It also directly shows the
correct treatment of a contained procedure/evidence deficiency as
INDETERMINATE rather than a fabricated PASS or product finding.

It does **not** directly validate a governed finding for an actual unexpected
instability (2.11-C), nor does the inspected evidence contain a direct
evidence-gap Finding Record for 2.11-E.  Those are coverage facts, not a
license to create synthetic discrepancies, alter controls, or execute a new
validation.  No new finding is warranted from this read-only analysis.

Final Item 2.11 completeness cannot yet be determined.  The required
integration input is Lane A's future R2 v2 result and any R2-specific
FAIL/INDETERMINATE/finding/disposition.  After R2 and final Item 2.10
reconciliation, an authorized cross-lane review must inventory every WS2
discrepancy and decide whether the remaining 2.11-C and 2.11-E coverage is
direct, supporting, deferred, or requires a Project Owner decision.  That
review may require shared-file updates and is outside Lane B authority.

## 7. Non-change attestation

No Item 2.11 validation executed.  No fixture, expected result, shared
register, governance-package artifact, existing evidence/finding directory,
application/source, test, gate, proving, TD-14, DVL, readiness, or Lane A
Item 2.10 file was changed.  This is a new Lane B Item 2.11 analysis record
only.
