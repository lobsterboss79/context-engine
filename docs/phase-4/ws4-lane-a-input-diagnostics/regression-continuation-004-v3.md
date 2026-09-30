# VE-P4-4A-004 focused regression continuation v3

Status: **FROZEN BEFORE EXECUTION**

This continuation follows the committed application-lifecycle remediation and
the approved three test-owned close corrections. It does not rerun semantic
validation or create a new VE identity.

| Item | Frozen value |
| --- | --- |
| Branch / committed HEAD | `phase4-ws4-input-diagnostics-win` / `d33b244b0c6107a5d482d31145bcbdd67ee0a576` |
| Semantic basis | VE-P4-4A-004 semantic PASS |
| Application remediation lineage | `36b73316c9ca736e4d25298eb5a066747519bb2b` |
| Test-close correction basis | `test-owned-sqlite-close-correction-record.md` |
| Interpreter | `Z:\temp\context-engine-phase4-validation\Scripts\python.exe` |
| Runtime / inventory | CPython 3.14.7; pytest 9.1.1; colorama 0.4.6; iniconfig 2.3.0; packaging 26.3; pluggy 1.6.0; Pygments 2.21.0 |
| External writable path | `Z:\temp\context-engine-phase4-regression-home\temp` only, through the approved bounded external-write context |
| Process-scoped environment | `USERPROFILE=Z:\temp\context-engine-phase4-regression-home`; `PYTHONPATH=src`; `PYTHONDONTWRITEBYTECODE=1` |
| Current source/test blobs | adapter `2e948c02a2d2fea96c93e46ea5a38657dd7e468c`; WS3 `231e1ac53c3e1b05a37547e70ca836229aba1907`; WS4 `36c77ef2d88bb4054b3efaa00b14a808b7a269b1`; WS6 `df180f94f53df355b03cc5d10825bd039cbd1ea3`; WS8 `534e6ee7b8a1f7e77d703ce893138094b38c00f5`; WS9 `fa719e5d808b7a6a524fec93b1cc5fe715b64348` |
| Shared files | unchanged |

Run exactly once from repository root:

```powershell
$env:PYTHONPATH = 'src'
$env:PYTHONDONTWRITEBYTECODE = '1'
$env:USERPROFILE = 'Z:\temp\context-engine-phase4-regression-home'
& 'Z:\temp\context-engine-phase4-validation\Scripts\python.exe' -m pytest -p no:cacheprovider -q tests/test_workstream_3.py tests/test_workstream_4.py tests/test_workstream_6.py tests/test_workstream_8.py tests/test_workstream_9.py
```

Expected PASS: zero exit status, no failed tests, no errors, and no skipped
tests. Any assertion failure, setup/teardown error, integrity change, or
evidence loss stops without rerun. A PASS alone permits bounded Lane A
post-results review; it does not close F-P4-4A-001.
