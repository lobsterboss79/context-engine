# Lane A Procedure — `PROC-P4-4A-004 v1`

**Status:** Frozen for authorized execution. Reuses immutable v1 fixture files
only; no application, source, test, or predecessor artifact is modified.

Before execution, preserve a portable preflight under `VE-P4-4A-004` using
literal full SHA `rev-parse --verify --quiet` and `merge-base --is-ancestor`
checks for `636afcf72cbd63dc2cfb5f8a0cc5388eb4e9f6f6`,
`1fdef6ee07c5a6f5e6663f34b85b6e339845bd03`,
`f55d2541b7c650e28cdfa70dc0ff3648ff11fa51`,
`85d0adfcf0dd8aa5122f452fb654f0a7c6338c82`,
`0af099b62de675ad01daf01aa17a3e077cee74a9`,
`8a2894e10ad840e130c2e9119e3ad401f480b507`, and
`7843afaf41ce581a040f4458fda028f5b901a56d`. Do not use braced revision
syntax. Verify hashes of this procedure, ER, runner, fixture files, and
Windows environment provenance; source/tests/shared/Lane B/C integrity;
fresh namespace; and venv CPython 3.14.7, pytest 9.1.1, and prior 60-test
collection capability. Hash the durable preflight record before execution.

Execute once, exactly:

```powershell
$env:PYTHONPATH = 'src'
$env:PYTHONDONTWRITEBYTECODE = '1'
& 'Z:\temp\context-engine-phase4-validation\Scripts\python.exe' docs/phase-4/ws4-lane-a-input-diagnostics/fixtures/run_lane_a_004.py --output docs/phase-4/validation-evidence/VE-P4-4A-004/raw/result.json
```

If PASS, run once with that same venv:

```powershell
& 'Z:\temp\context-engine-phase4-validation\Scripts\python.exe' -m pytest -p no:cacheprovider -q tests/test_workstream_3.py tests/test_workstream_4.py tests/test_workstream_6.py tests/test_workstream_8.py tests/test_workstream_9.py
```

Unexpected FAIL/INDETERMINATE, qualification loss, or evidence deficiency
stops and preserves; no further successor or revision is authorized.
