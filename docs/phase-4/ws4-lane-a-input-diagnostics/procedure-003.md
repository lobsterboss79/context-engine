# Lane A Portable Successor Procedure — `PROC-P4-4A-003 v1`

**Status:** Frozen for authorized execution. This procedure reuses unchanged
`CTL-P4-4A-002 v1`, `ER-P4-4A-002 v1`, and `FX-P4-4A-001 v1`; it does not
modify or rerun `VE-P4-4A-001` or `VE-P4-4A-002`.

## Frozen portable preflight

The preflight uses these literal full commit IDs and no peel/braced revision
syntax. For each literal SHA, execute `git rev-parse --verify --quiet <SHA>`
and `git merge-base --is-ancestor <SHA> HEAD`, requiring exit status zero:

- `636afcf72cbd63dc2cfb5f8a0cc5388eb4e9f6f6` — shared baseline;
- `1fdef6ee07c5a6f5e6663f34b85b6e339845bd03` — VE-001;
- `f55d2541b7c650e28cdfa70dc0ff3648ff11fa51` — VE-001 investigation;
- `85d0adfcf0dd8aa5122f452fb654f0a7c6338c82` — VE-002;
- `0af099b62de675ad01daf01aa17a3e077cee74a9` — VE-002 investigation.

Require unchanged hashes for the referenced ER, all v1 fixtures, and v2 runner;
unchanged source/tests/shared files and Lane B/C namespaces; a clean
pre-execution worktree apart from the new Lane A 003 artifacts; and the
canonical external venv collection-only PASS documented in
`windows-validation-environment.md`. Preserve and hash `VE-P4-4A-003`
preflight evidence before execution.

## Frozen semantic invocation and regression

```powershell
$env:PYTHONPATH = 'src'
$env:PYTHONDONTWRITEBYTECODE = '1'
& 'Z:\temp\context-engine-phase4-validation\Scripts\python.exe' docs/phase-4/ws4-lane-a-input-diagnostics/fixtures/run_lane_a_002.py --output docs/phase-4/validation-evidence/VE-P4-4A-003/raw/result.json
```

Expected scenario states and validation criteria are unchanged from
`ER-P4-4A-002 v1`: two expected `APPLICATION-LEVEL FAILURE` CLI outcomes;
bounded `ABSENCE`, `UNAVAILABLE`, `PARTIAL EVIDENCE`, and `SUCCESSFUL
COMPLETION`; distinct states; attributable and canary-safe diagnostic; no
audit/recovery/success conversion. An expected negative scenario may yield
validation PASS; only an ER violation is validation FAIL.

If semantic execution PASSes, run exactly once with the same venv:

```powershell
& 'Z:\temp\context-engine-phase4-validation\Scripts\python.exe' -m pytest -p no:cacheprovider -q tests/test_workstream_3.py tests/test_workstream_4.py tests/test_workstream_6.py tests/test_workstream_8.py tests/test_workstream_9.py
```

Any unexpected FAIL or INDETERMINATE stops and preserves evidence. No further
successor, remediation, or artifact revision is authorized.
