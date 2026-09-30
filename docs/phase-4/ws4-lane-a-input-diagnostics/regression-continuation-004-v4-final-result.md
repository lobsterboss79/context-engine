# VE-P4-4A-004 focused regression continuation v4 — final result

Status: **PASS**

The frozen v4 procedure (SHA-256
`a0c47a654a6e8f11537e7f9cbae1d0de7e421977db439448f939ee4845904532`)
executed once after its focused validation passed. It did not rerun Lane A
semantic validation.

| Item | Observed value |
| --- | --- |
| Interpreter | `Z:\temp\context-engine-phase4-validation\Scripts\python.exe` |
| Runtime / pytest | CPython 3.14.7 / pytest 9.1.1 |
| Process-scoped USERPROFILE | `Z:\temp\context-engine-phase4-regression-home` |
| External writable boundary | `Z:\temp\context-engine-phase4-regression-home\temp` only, via the approved bounded external-write context |
| Test slice | `tests/test_workstream_3.py tests/test_workstream_4.py tests/test_workstream_6.py tests/test_workstream_8.py tests/test_workstream_9.py` |
| Exit status | `0` |
| Collected / passed / failed / errors / skipped | `61 / 61 / 0 / 0 / 0` |

Exact invocation:

```powershell
$env:PYTHONPATH = 'src'
$env:PYTHONDONTWRITEBYTECODE = '1'
$env:USERPROFILE = 'Z:\temp\context-engine-phase4-regression-home'
& 'Z:\temp\context-engine-phase4-validation\Scripts\python.exe' -m pytest -p no:cacheprovider -q tests/test_workstream_3.py tests/test_workstream_4.py tests/test_workstream_6.py tests/test_workstream_8.py tests/test_workstream_9.py
```

Observed output:

```text
.............................................................            [100%]
61 passed in 0.57s
```

The three previously corrected and the two final corrected test-owned
connection lifetimes produced no WinError 32. This result provides the frozen
Windows regression evidence required for the bounded Lane A review. It neither
changes VE-P4-4A-004's preserved semantic PASS nor closes F-P4-4A-001.
