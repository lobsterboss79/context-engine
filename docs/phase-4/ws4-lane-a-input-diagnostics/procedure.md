# Lane A Procedure — `PROC-P4-4A-001 v1`

**Status:** Frozen for authorized execution. Do not edit this procedure,
fixture, ER, or runner after execution.

1. Confirm required branch, clean tree, and baseline ancestry. Record Windows,
   Python, Git, and commit identity.
2. Preserve a pre-execution SHA-256 manifest for this procedure, ER, fixture,
   valid configuration, and runner.
3. From repository root, run:

   ```powershell
   $env:PYTHONPATH = 'src'
   python docs/phase-4/ws4-lane-a-input-diagnostics/fixtures/run_lane_a.py --output docs/phase-4/validation-evidence/VE-P4-4A-001/raw/result.json 1> docs/phase-4/validation-evidence/VE-P4-4A-001/raw/stdout.txt 2> docs/phase-4/validation-evidence/VE-P4-4A-001/raw/stderr.txt
   ```

4. Preserve raw output and post-execution manifest. Compare only with
   `ER-P4-4A-001 v1`. The runner has no recovery or successor step.
5. Run `python -m pytest tests/test_workstream_3.py tests/test_workstream_4.py tests/test_workstream_6.py tests/test_workstream_8.py tests/test_workstream_9.py -q` with `PYTHONPATH=src`.
6. Absent/contradictory output is **INDETERMINATE** or **FAIL**, preserved, and
   stopped. Do not revise any frozen item.

Injection is restricted to lane-private malformed TOML, configuration mismatch,
and in-memory Source inputs. No host permission, process, filesystem, network,
database, audit, recovery, or external injection is permitted.
