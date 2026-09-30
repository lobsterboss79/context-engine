# Lane A Successor Procedure — `PROC-P4-4A-002 v1`

**Status:** Frozen for authorized execution. This is a separately versioned
successor after immutable `VE-P4-4A-001` INDETERMINATE.

1. Preserve `preflight.md` before execution, verifying branch/baseline,
   committed predecessor/investigation, v1 immutability, fresh evidence
   namespace, frozen successor hashes, two-field identity calls, unchanged
   fixture/ER semantics, source/test/shared-file and Lane B/C integrity, and
   Windows environment.
2. From repository root execute exactly:

   ```powershell
   $env:PYTHONPATH = 'src'
   python docs/phase-4/ws4-lane-a-input-diagnostics/fixtures/run_lane_a_002.py --output docs/phase-4/validation-evidence/VE-P4-4A-002/raw/result.json 1> docs/phase-4/validation-evidence/VE-P4-4A-002/raw/stdout.txt 2> docs/phase-4/validation-evidence/VE-P4-4A-002/raw/stderr.txt
   ```

3. Preserve raw artifacts and SHA-256 manifest. Compare only against
   `ER-P4-4A-002 v1`. Do not edit this procedure, runner, ER, or v1 fixtures.
4. If and only if the control result is PASS, run the frozen relevant regression
   slice: `tests/test_workstream_3.py`, `test_workstream_4.py`,
   `test_workstream_6.py`, `test_workstream_8.py`, and `test_workstream_9.py`.
5. Any unexpected FAIL or INDETERMINATE stops and preserves evidence. No
   additional successor, remediation, source/test change, or ER revision is
   authorized by this procedure.

Injection remains only the existing disposable fixtures and in-memory Source
inputs. The procedure has no recovery step.
