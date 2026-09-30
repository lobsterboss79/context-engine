# VE-P4-4A-004 focused regression continuation

Status: **FROZEN BEFORE EXECUTION**

## Authorization and lineage

This is the one Project Owner-authorized continuation of the required focused
regression after the recorded external temporary-path prerequisite is supplied.
It is not a semantic rerun, a new semantic control, or a new VE identity.

| Item | Frozen value |
| --- | --- |
| Branch | `phase4-ws4-input-diagnostics-win` |
| HEAD | `21814f59d888503b971a7d2fe20025dca173c8f2` |
| VE-P4-4A-004 committed evidence | `9b8481f54b7817a74e7d8dd7bd3818bdad4ebee3` |
| Regression-path investigation | `21814f59d888503b971a7d2fe20025dca173c8f2` |
| Semantic state preserved, not rerun | VE-P4-4A-004 semantic control PASS |

## Environment and integrity freeze

| Item | Frozen value |
| --- | --- |
| Validation interpreter | `Z:\temp\context-engine-phase4-validation\Scripts\python.exe` |
| Python / pytest | CPython 3.14.7 / pytest 9.1.1 |
| Package inventory | colorama 0.4.6; iniconfig 2.3.0; packaging 26.3; pluggy 1.6.0; Pygments 2.21.0; pytest 9.1.1 |
| External regression home | `Z:\temp\context-engine-phase4-regression-home` |
| Required existing child | `Z:\temp\context-engine-phase4-regression-home\temp` |
| Process-scoped environment | `USERPROFILE=Z:\temp\context-engine-phase4-regression-home` only for the regression process and children |
| Source/tests | unchanged from HEAD before execution |
| Frozen test-file Git object hashes | WS3 `74ebf438b5288f21bb608f8203ef7a7ca2f0314e`; WS4 `c7dcf0e1eee6290348e03a0b9c912e929c1d6b48`; WS6 `df180f94f53df355b03cc5d10825bd039cbd1ea3`; WS8 `914e6e0b5438b443de1a7e89c11c61c3ed98bc44`; WS9 `fa719e5d808b7a6a524fec93b1cc5fe715b64348` |

`HOME`, `TEMP`, `TMP`, and `TMPDIR` remain unchanged.  No global Windows
environment setting is changed.

## Exact single invocation

From the repository root, execute exactly once:

```powershell
$env:PYTHONPATH = 'src'
$env:PYTHONDONTWRITEBYTECODE = '1'
$env:USERPROFILE = 'Z:\temp\context-engine-phase4-regression-home'
& 'Z:\temp\context-engine-phase4-validation\Scripts\python.exe' -m pytest -p no:cacheprovider -q tests/test_workstream_3.py tests/test_workstream_4.py tests/test_workstream_6.py tests/test_workstream_8.py tests/test_workstream_9.py
```

The environment assignments are scoped to the PowerShell process executing this
single command and its child.  The frozen expected result is a zero-exit focused
regression with the selected tests collected and no failures or errors.

On non-zero exit, indeterminate execution, source/test change, or evidence
preservation loss: stop and preserve; do not rerun.  Only a PASS permits the
already-authorized bounded Lane A post-results review.
