# VE-P4-4A-004 focused regression continuation result

Status: **INDETERMINATE — EXTERNAL TEMPORARY-ROOT EXECUTION PERMISSION DENIED; STOPPED AND PRESERVED**

The frozen continuation procedure in
`regression-continuation-004.md` (SHA-256
`46547959CD7CD8D4CECEE0E09DCE6C75EFB5478E24A7118F05F3E57AA6BE1B48`) was
invoked once with the established external interpreter, unchanged frozen test
slice, `PYTHONPATH=src`, `PYTHONDONTWRITEBYTECODE=1`, and process-scoped:

```text
USERPROFILE=Z:\temp\context-engine-phase4-regression-home
```

The requested redirected parent existed and the process resolved the fixture
path correctly as:

```text
Z:\temp\context-engine-phase4-regression-home\temp
```

The fixture `tempfile.mkdtemp` attempts nevertheless failed with
`PermissionError: [WinError 5] Access is denied` while creating its unique
child beneath that external parent.  This was the same sandboxed execution
context in which the invocation was made.  The Owner-authorized external setup
command had verified write access to the parent and child using its approved
external-write permission, but that permission was not available to the
separate sandboxed regression process.

Observed stdout summary: `43 passed, 17 errors in 0.48s`; stderr was empty.
Every error was fixture setup before a test body, in the five frozen test
modules (WS3, WS4, WS6, WS8, and WS9).  The first error, representative of all
17, was:

```text
PermissionError: [WinError 5] Access is denied:
'Z:\\temp\\context-engine-phase4-regression-home\\temp\\context-engine-ws3-dwch4p82'
```

This does establish that the `USERPROFILE` redirection was effective; it does
not establish a test, application, or Lane A semantic failure.  It is an
indeterminate regression-execution result because the frozen regression could
not write to its required external temporary root in the actual process that
ran it.  No additional regression attempt, semantic rerun, source/test change,
or post-results review was performed.

VE-P4-4A-004's already-preserved semantic control PASS is unchanged.  No
Finding or H3 is created by this result.  Source, tests, shared WS4 materials,
and Lane B/C remain unchanged.

Project Owner disposition is required before any further regression attempt:
whether to authorize a fresh, separately frozen regression continuation whose
single test process has the approved external-write capability required for its
already-authorized `Z:\temp` fixture workspace.
