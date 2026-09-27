# Item 2.10 Superseding Expected Results and Semantic Contract v2

**Status:** PROJECT OWNER APPROVED PRE-RESULTS CONTROL CORRECTION — FUTURE
EXECUTION REQUIRES SEPARATE AUTHORIZATION. This record supersedes only the
erroneous unified Candidate/package ordering assertion in v1. It preserves v1,
the immutable R1-01 FAIL, and every other controlled input, provenance,
isolation, comparison, and stop requirement.

## Lineage and correction boundary

| Field | Value |
| --- | --- |
| Superseded records | SC-P4-2.10 v1; ER-P4-2.10-R1 v1; ER-P4-2.10-R2 v1; RC-P4-2.10-R1 v1; RC-P4-2.10-R2 v1. |
| Superseding records | SC-P4-2.10 v2; ER-P4-2.10-R1 v2; ER-P4-2.10-R2 v2; RC-P4-2.10-R1 v2; RC-P4-2.10-R2 v2. |
| Authority | Project Owner disposition in ws2-item-2.10-r1-ordering-failure-disposition.md. |
| Reason | v1 incorrectly made renderer role-grouped/input-list order the Candidate and package order. Phase 3 WS6 and historical VE-F3-001 govern those domains differently. |
| Preserved history | VE-P4-2.10-R1-001 remains FAIL against executed v1. It is not a v2 run and cannot count toward v2 repeatability. |
| Unchanged controls | FX-F3 v1, ER-F3 v1, controlled F3 files/hashes, historical and current provenance checks, isolation, semantic fields other than corrected order taxonomy, three-run R1 design, R2 matrix, allowlist, and stop rules. |

## SC-P4-2.10 v2 — independent order domains

Equality requires every governed semantic field inherited from v1 to be equal,
including request/task/scope; Sources/states; artifacts; observations;
represented information; Provenance; discovery basis; applicability reasons;
roles; selected identities; exclusions; Conflict; Uncertainty; qualification;
ASU; deficiencies; sufficiency; coherence; package membership; limitations; and
the package/rendering/delivery/receipt/use boundary. The following order domains
are independent and each is material:

| Domain | Frozen F3 order / rule |
| --- | --- |
| Candidate order | RI-F3-CANVAS-HISTORY, RI-F3-DEPOT-UNVERIFIED, RI-F3-SEALED, RI-F3-TOTE. Phase 3 WS6: mechanism, represented-information identity, Provenance identity. |
| Applicability/selection traversal | RI-F3-CANVAS-HISTORY, RI-F3-DEPOT-UNVERIFIED, RI-F3-SEALED, RI-F3-TOTE. It follows Candidate traversal. |
| Selected Context / logical-package items | RI-F3-CANVAS-HISTORY Supporting; RI-F3-DEPOT-UNVERIFIED Supporting; RI-F3-SEALED Required; RI-F3-TOTE Required. It preserves selected traversal. |
| Source Manifest | SRC-F3-COMPETING, SRC-F3-CURRENT, SRC-F3-HISTORY, SRC-F3-QUALIFICATION, ordered by Source identity. |
| Renderer material presentation | Required: RI-F3-SEALED, RI-F3-TOTE. Supporting: RI-F3-CANVAS-HISTORY, RI-F3-DEPOT-UNVERIFIED. Renderer stable-filters roles and preserves relative order within each role. |

A difference in one domain cannot be normalized by agreement in another.
Renderer role grouping must not be required at Candidate/package level, and
Candidate/package traversal must not be required at renderer-presentation level.
The v1 narrow non-semantic allowlist remains unchanged and does not waive any
of these orders.

## ER-P4-2.10-R1 v2

| Field | Frozen value |
| --- | --- |
| Control / relationship | RC-P4-2.10-R1 v2; supersedes v1 only because v1 had an erroneous unified ordering expectation. |
| Governed expectation | Three new independent isolated executions using unchanged F3 inventory/hashes, Bootstrap/configuration semantics, request, Sources, artifacts, Consumer contracts, approved application baseline, ER-F3 v1, and SC-P4-2.10 v2. |
| Acceptance | Each run satisfies ER-F3 v1 and SC-P4-2.10 v2; all three projections are mutually equal in every independently governed order domain and all other governed semantic fields. |
| Required preservation | Both current Required Conflict participants remain unresolved; historical Supporting and unverified Supporting Context remain qualified; Insufficient and coherent_with_qualification remain; every renderer remains faithful and makes no delivery/receipt/use assertion. |
| Failure | Input/provenance failure, contamination, F3 failure, a mismatch in any governed field or any independent order domain, lost qualification, or fewer than three mutually equal runs is not PASS. |
| Future evidence | Three new v2-specific run identities and a derived comparison record. R1-01 v1 is immutable historical FAIL, not a run in this matrix. |

## ER-P4-2.10-R2 v2

| Field | Frozen value |
| --- | --- |
| Control / relationship | RC-P4-2.10-R2 v2; supersedes unexecuted v1 to use SC-P4-2.10 v2. |
| Reference / matrix | Retains the v1 predesignated R2-REF and R2-H, R2-P, R2-M bounded matrix, fresh isolation, input inventory, and no-product-change rule. |
| Governed expectation | Every future supported perturbation satisfies ER-F3 v1 and equals R2-REF in every independent SC-P4-2.10 v2 order domain and all other governed semantic fields. |
| Negative criteria | No incidental mechanism may select, omit, reorder within its governed domain, or resolve Context. Currentness, Conflict, Uncertainty, ASU, role, Authority, and input semantics remain unchanged. |
| Execution status | Not executed; not authorized. |

## Future execution boundary

This correction creates no validation result and authorizes no run. Corrected R1
requires three new isolated v2 runs; the historical v1 R1-01 FAIL is not a
PASS-equivalent observation. R2 remains not authorized. Item 2.10 remains
incomplete; Gate 4B is not approved; proving is not authorized; TD-14 remains
closed; and production readiness is not established.

