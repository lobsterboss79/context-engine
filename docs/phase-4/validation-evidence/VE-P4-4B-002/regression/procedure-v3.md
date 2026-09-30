# VE-P4-4B-002 Focused Regression Procedure v3

**Status:** FROZEN BEFORE EXECUTION — Project Owner-authorized bounded external-temp regression.

The prior v2 result (29 passed, 18 setup errors, exit 1) remains immutable historical evidence. This v3 procedure is a separately identified regression execution after the Project Owner authorized only the test-required `/home/lobsterboss79/temp` write boundary and the Codex write probe succeeds.

Exact interpreter and invocation:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src /home/lobsterboss79/temp/context-engine-ws2-validation.qNq9B4/bin/python -m pytest -p no:cacheprovider tests/test_workstream_3.py tests/test_workstream_4.py tests/test_workstream_8.py tests/test_workstream_10.py
```

The v3 preflight must preserve the successful create/verify/delete probe, branch/HEAD/baseline, interpreter/Python/pytest identity, source/test/shared state, semantic-artifact hashes, test hashes, exact invocation, expected result, and stop criteria before this invocation. Preserve stdout/stderr, exit status, and result in `stdout-v3.txt`, `stderr-v3.txt`, and `result-v3.md`. Any nonzero exit, setup/environment error, assertion failure, missing evidence, protected-state change, or outside-boundary condition is STOP AND PRESERVE with no retry or workaround.
