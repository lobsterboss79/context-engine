# VE-P4-2.10-R1 — derived comparison/review stop record

**Overall R1 classification:** **FAIL**

| Review field | Preserved result |
| --- | --- |
| Completed run identities | `R1-01` only. `R1-02` and `R1-03` were not executed because the frozen stop rule activated after R1-01 FAIL. |
| Input equality | R1-01's six F3 file hashes and both-part provenance preflight passed. Cross-run input equality is not assessable because no peer run was allowed. |
| Isolation | R1-01 isolation passed: separate process, workspace, and SQLite state with no inherited output, audit, or prior-run state. |
| ER-F3 / R1 ER / SC result | R1-01 preserved all tested F3 identities, qualifications, Conflict, Uncertainty, sufficiency, coherence, Source Manifest order, and rendering boundary, but fails the frozen Candidate and logical-package order. |
| Expected semantic order | `RI-F3-SEALED`, `RI-F3-TOTE`, `RI-F3-CANVAS-HISTORY`, `RI-F3-DEPOT-UNVERIFIED`. |
| Observed Candidate/package order | `RI-F3-CANVAS-HISTORY`, `RI-F3-DEPOT-UNVERIFIED`, `RI-F3-SEALED`, `RI-F3-TOTE`. |
| Renderer comparison | Each renderer presented Required `SEALED`, `TOTE` then Supporting `CANVAS-HISTORY`, `DEPOT-UNVERIFIED`; its individual material order passed. This does not normalize or cure the distinct package-order mismatch. |
| Permitted non-semantic differences | None relied on. The mismatch is governed semantic order and is outside the narrow allowlist. |
| Cross-run comparison | Not performed: a peer comparison was prohibited by the R1-01 FAIL stop rule. |
| Finding / H3 | [`F-P4-2.10-R1-001`](VE-P4-2.10-R1-001/finding-record.md), MATERIAL; H3 triggered. |
| Coverage review | Not performed. The bounded 2.10-A/B/I review is authorized only after overall R1 PASS. C–H are not dispositioned. |
| Boundaries | R2 was not executed. Item 2.10 remains incomplete; Gate 4B is not approved; proving is not authorized; TD-14 remains closed; production readiness is not established. |

This review derives only from [R1-01 raw and derived evidence](VE-P4-2.10-R1-001/)
and adds no interpretation that changes the frozen controls or expected results.
