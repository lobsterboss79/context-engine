# Lane A Expected Results — `ER-P4-4A-001 v1`

**Status:** Frozen for authorized execution. **Fixture:** `FX-P4-4A-001 v1`.

| Field | Frozen record |
| --- | --- |
| Governing basis | Checklist 4.1/4.6; Phase 2 G ST-06, CI-02, FR-01, FR-03--FR-07, OM-02--OM-04; Phase 3 WS3/WS6/WS8/WS9/WS10; WS1 §§1.3--1.9. |
| Controlled input | Malformed TOML; valid Bootstrap plus mismatched configuration; lane-private Source construction in the runner. |
| Environment | Windows, local/network-free CPython execution from the recorded Git baseline. |
| Scenario states | CLI cases: `APPLICATION-LEVEL FAILURE` (exit 2). Source cases: bounded `ABSENCE`, `UNAVAILABLE`, `PARTIAL EVIDENCE`, `SUCCESSFUL COMPLETION`. |
| PASS criteria | Both failures return 2 with attributable generic diagnostics; no output contains `lane-a-secret-canary`; neither claims validated; all four Source classifications and expected candidate/limitation patterns are distinct; no SQLite/audit artifact or recovery claim; output is preserved. |
| Validation FAIL criteria | Rejection succeeds/validates; states collapse; unavailable becomes absence/inaccessible; partial loses limitation; failure becomes success; diagnostic leaks canary; diagnostics become audit/recovery; or output is missing/contradictory. |
| Qualifications | `ABSENT` is limited to frozen ASU. `UNAVAILABLE` is not `INACCESSIBLE`; DVL-P4-001 remains active. No Windows filesystem/path/permission/Git/process behavior or Linux claim is made. CLI diagnostic is not durable audit. |
| Reviewer basis | Frozen runner assertions and this ER; no post-result revision. |
| Affected evidence | `VE-P4-4A-001`. |

Expected negative application outcomes satisfying this ER yield validation
**PASS**. Validation **FAIL** is only an ER violation.
