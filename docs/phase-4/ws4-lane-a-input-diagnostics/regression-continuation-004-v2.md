# VE-P4-4A-004 focused regression continuation v2

Status: **FROZEN BEFORE EXECUTION**

This separately identified continuation follows the Owner's disposition of the
first continuation as INDETERMINATE due solely to sandbox write capability.
It is neither a semantic rerun nor a new VE identity.

| Item | Frozen value |
| --- | --- |
| Branch / HEAD | `phase4-ws4-input-diagnostics-win` / `3bfb9c6180ed1a98d64d83f8106677c2b5aea0ee` |
| Semantic basis | VE-P4-4A-004 semantic PASS, preserved at `9b8481f54b7817a74e7d8dd7bd3818bdad4ebee3` |
| Prior lineage | temp-path investigation `21814f59d888503b971a7d2fe20025dca173c8f2`; first continuation preserved at `3bfb9c6180ed1a98d64d83f8106677c2b5aea0ee` |
| Interpreter | `Z:\temp\context-engine-phase4-validation\Scripts\python.exe` |
| Runtime | CPython 3.14.7; pytest 9.1.1 |
| Package inventory | colorama 0.4.6; iniconfig 2.3.0; packaging 26.3; pluggy 1.6.0; Pygments 2.21.0; pytest 9.1.1 |
| External writable tree | `Z:\temp\context-engine-phase4-regression-home\temp` only |
| Process-scoped environment | `USERPROFILE=Z:\temp\context-engine-phase4-regression-home` only for the probe, pytest process, and its test children |
| Test integrity | WS3 `74ebf438b5288f21bb608f8203ef7a7ca2f0314e`; WS4 `c7dcf0e1eee6290348e03a0b9c912e929c1d6b48`; WS6 `df180f94f53df355b03cc5d10825bd039cbd1ea3`; WS8 `914e6e0b5438b443de1a7e89c11c61c3ed98bc44`; WS9 `fa719e5d808b7a6a524fec93b1cc5fe715b64348` |

The same effective approved external-write permission context must first run a
child-process infrastructure probe that creates a unique directory beneath the
approved `temp` path, writes and reads one small probe file, deletes it, and
removes the directory.  Probe failure stops without pytest.

Only after probe PASS, invoke exactly once from the repository root:

```powershell
$env:PYTHONPATH = 'src'
$env:PYTHONDONTWRITEBYTECODE = '1'
$env:USERPROFILE = 'Z:\temp\context-engine-phase4-regression-home'
& 'Z:\temp\context-engine-phase4-validation\Scripts\python.exe' -m pytest -p no:cacheprovider -q tests/test_workstream_3.py tests/test_workstream_4.py tests/test_workstream_6.py tests/test_workstream_8.py tests/test_workstream_9.py
```

Expected PASS criterion: zero exit status; the frozen slice collects and has
zero failures and errors.  A test assertion failure, fixture/setup error,
external-write preflight failure, integrity change, or evidence loss is a stop
condition.  No rerun is authorized.
