# VE-P4-4B-002 Focused Regression Procedure v2

**Status:** FROZEN BEFORE EXECUTION — Project Owner-authorized existing-environment regression.

The exact interpreter is `/home/lobsterboss79/temp/context-engine-ws2-validation.qNq9B4/bin/python`. The exact invocation is:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src /home/lobsterboss79/temp/context-engine-ws2-validation.qNq9B4/bin/python -m pytest -p no:cacheprovider tests/test_workstream_3.py tests/test_workstream_4.py tests/test_workstream_8.py tests/test_workstream_10.py
```

The preflight must preserve branch/HEAD/baseline ancestry, interpreter/Python/pytest identity, test hashes, unchanged source/tests/shared state, and semantic-evidence hashes before invocation. Raw stdout, stderr, exit status, and a result record are preserved in this directory. Expected result: pytest collects and passes the four established persistence/migration/recovery slices. Any nonzero exit, failed test, unavailable interpreter/package, changed source/test/shared/semantic artifact, or missing preservation is STOP AND PRESERVE; no retry, substitute interpreter, install, or semantic rerun is authorized.
