# VE-P4-4A-004 focused regression continuation v3 result

Status: **STOPPED — REMAINING UNFROZEN TEST-OWNED SQLITE HANDLE CASES; PROJECT OWNER DISPOSITION REQUIRED**

The frozen v3 procedure (SHA-256
`51D5C8E04301708BF0612084A1ABDA38EE78FCB654B280FA0977647B07829BA0`) ran
once using the established Windows environment, the approved bounded
external-write context, and process-scoped
`USERPROFILE=Z:\temp\context-engine-phase4-regression-home`.

Result:

```text
1 failed, 60 passed, 2 errors in 0.75s
```

The three authorized test-owned close corrections passed their focused
validation, including both migration tests. No WinError 32 occurred in those
three corrected boundaries.

The full slice nevertheless exposed two separate, previously uncorrected
direct test-owned connection paths:

1. WS3 `test_sqlite_rejects_incompatible_schema_and_preserves_project_isolation`:
   its setup `with sqlite3.connect(database)` remains non-closing. The expected
   `StateCompatibilityError` assertion passed; its subsequent direct
   `database.unlink()` raised `WinError 32`, and fixture teardown also errored
   on the same `state.sqlite`.
2. WS4 `test_incompatible_lifecycle_schema_fails_closed`:
   its setup `with sqlite3.connect(database)` remains non-closing. Its semantic
   expected-error assertion completed, but fixture teardown raised `WinError
   32` on `incompatible.sqlite`.

This is an unexpected remaining test-lifecycle inventory beyond the exact
three correction sites frozen for this continuation. Per stop conditions, no
additional test correction, source change, regression rerun, semantic rerun,
Finding closure, or Lane A post-results review was performed.

VE-P4-4A-004 semantic PASS and the scoped application-owned connection
remediation remain unchanged. This result does not establish an application
semantic failure or automatically expand F-P4-4A-001; it requires a new Owner
disposition for the newly identified test-owned paths.
