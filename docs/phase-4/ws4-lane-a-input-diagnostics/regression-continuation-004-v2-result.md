# VE-P4-4A-004 focused regression continuation v2 result

Status: **STOPPED — UNEXPECTED WINDOWS SQLITE FILE-LOCK REGRESSION RESULT; PROJECT OWNER DISPOSITION REQUIRED**

## Execution boundary

The frozen v2 procedure (SHA-256
`7C27ECE826A56F9B260A40928477E645AB151EE3E8823042A2A5951D941E4C68`) ran
once after the Owner-approved bounded external-write escalation.  The only
external writable tree authorized to the probe and regression process was:

```text
Z:\temp\context-engine-phase4-regression-home\temp
```

The process-scoped setting was:

```text
USERPROFILE=Z:\temp\context-engine-phase4-regression-home
```

The interpreter was
`Z:\temp\context-engine-phase4-validation\Scripts\python.exe` (CPython
3.14.7 / pytest 9.1.1).  The unchanged frozen WS3, WS4, WS6, WS8, and WS9
slice was invoked with `PYTHONPATH=src`, `PYTHONDONTWRITEBYTECODE=1`, and
`-p no:cacheprovider`.

## External-write preflight

**PASS.**  A child process created a unique directory beneath the approved
`temp` root, wrote and read a probe file, deleted it, and removed the probe
directory.  This proves the first continuation's sandbox write denial was
removed for this invocation.

## Regression result

Pytest completed its one authorized invocation with:

```text
1 failed, 59 passed, 13 errors in 1.16s
```

The unexpected failures are Windows `PermissionError: [WinError 32]` file-lock
conditions while deleting SQLite files from fixture directories.  Thirteen
errors are fixture teardown errors in WS3, WS4, WS6, WS8, and WS9.  The sole
reported failure is `test_sqlite_rejects_incompatible_schema_and_preserves_project_isolation` at its direct `database.unlink()` call, also because
`state.sqlite` remained in use.  Representative observed path:

```text
Z:\temp\context-engine-phase4-regression-home\temp\context-engine-ws3-ff86q55g\state.sqlite
```

This differs from the preceding missing-directory and sandbox-write conditions:
the fixture directories were created and the relevant test paths executed.
The result is an unexpected regression failure/teardown condition.  It is not
automatically classified as a product defect, and no semantic conclusion is
drawn from it pending Owner disposition.

No semantic control was rerun.  VE-P4-4A-004's preserved semantic PASS remains
unchanged.  No post-results coverage review, proposed Lane A disposition,
Finding, H3, Lane B/C change, or Item 4.7 activity was performed.  No cleanup
of residual fixture directories was attempted after the stop condition.
