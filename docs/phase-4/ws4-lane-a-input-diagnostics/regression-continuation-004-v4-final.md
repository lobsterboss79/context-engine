# VE-P4-4A-004 focused regression continuation v4 — final

Status: **FROZEN BEFORE EXECUTION**

This is the one final continuation of the unchanged five-module Windows
regression slice. It follows the focused PASS for the two final test-owned
connection boundaries. It does not rerun VE-P4-4A-004 semantic validation and
does not create another VE identity.

| Item | Frozen value |
| --- | --- |
| Branch / committed HEAD | `phase4-ws4-input-diagnostics-win` / `e95421b27ac01894c60abcdab5a54366c2e144c9` |
| Semantic basis | VE-P4-4A-004 semantic PASS |
| Finding | F-P4-4A-001 OPEN — application-owned SQLite lifecycle remediation evidence required for closure candidacy |
| Application remediation lineage | `36b73316c9ca736e4d25298eb5a066747519bb2b` |
| Prior test-close lineage | Three approved test-owned closes, committed in `28ea004559ffcbd581b60be172c9f66652a4a99b` |
| Final two-close basis | `final-incompatible-schema-test-close-correction-record.md`; focused validation: 3 passed, no WinError 32 |
| Adapter blob | `2e948c02a2d2fea96c93e46ea5a38657dd7e468c` |
| WS3 blob | `6769ace529a777fbfec4186c64d35c2e8e0e8fb2` |
| WS4 blob | `f847ad6cda8afc0c789d5fc0d5fe9684b294de7f` |
| WS6 / WS8 / WS9 blobs | `df180f94f53df355b03cc5d10825bd039cbd1ea3`; `534e6ee7b8a1f7e77d703ce893138094b38c00f5`; `fa719e5d808b7a6a524fec93b1cc5fe715b64348` |
| Interpreter | `Z:\temp\context-engine-phase4-validation\Scripts\python.exe` |
| Runtime / inventory | CPython 3.14.7; pytest 9.1.1; colorama 0.4.6; iniconfig 2.3.0; packaging 26.3; pip 26.2.1; pluggy 1.6.0; Pygments 2.21.0 |
| External writable boundary | `Z:\temp\context-engine-phase4-regression-home\temp` only, through the approved bounded external-write context |
| Process-scoped environment | `USERPROFILE=Z:\temp\context-engine-phase4-regression-home`; `PYTHONPATH=src`; `PYTHONDONTWRITEBYTECODE=1` |
| Frozen test slice | `tests/test_workstream_3.py tests/test_workstream_4.py tests/test_workstream_6.py tests/test_workstream_8.py tests/test_workstream_9.py` |
| Expected result | Zero exit status; no failed, errored, or skipped tests. |

Run exactly once from repository root:

```powershell
$env:PYTHONPATH = 'src'
$env:PYTHONDONTWRITEBYTECODE = '1'
$env:USERPROFILE = 'Z:\temp\context-engine-phase4-regression-home'
& 'Z:\temp\context-engine-phase4-validation\Scripts\python.exe' -m pytest -p no:cacheprovider -q tests/test_workstream_3.py tests/test_workstream_4.py tests/test_workstream_6.py tests/test_workstream_8.py tests/test_workstream_9.py
```

Any assertion failure, setup/teardown error, integrity discrepancy, or
evidence-preservation loss stops without a rerun or further correction. A PASS
permits only bounded Lane A post-results review and an F-P4-4A-001
closure-candidate assessment; it does not close the Finding.
