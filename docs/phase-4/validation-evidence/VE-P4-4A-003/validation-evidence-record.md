# Validation Evidence Record — `VE-P4-4A-003`

**Status/disposition:** **FAIL — STOP AND PRESERVE.**

## Lineage and scope

This independent portable-preflight and semantic execution references unchanged
`CTL-P4-4A-002 v1`, `ER-P4-4A-002 v1`, and `FX-P4-4A-001 v1` under
`PROC-P4-4A-003 v1`. It does not modify or reinterpret immutable predecessors
`VE-P4-4A-001` (INDETERMINATE) or `VE-P4-4A-002` (INDETERMINATE).

Portable preflight PASS is preserved in `preflight.md` and `raw/` before this
execution. The control then ran once through the approved external Windows
venv and returned exit 1 with `validation_control_result: FAIL`.

## Observed frozen-control comparison

The malformed-input and invalid-configuration CLI cases both returned expected
exit 2 and attributable generic diagnostics, without validation success or the
canary. The observed Source classifications remain named and distinct:
ABSENCE (zero candidates), UNAVAILABLE (zero candidates and unavailable
limitation), PARTIAL EVIDENCE (one candidate), and SUCCESSFUL COMPLETION (one
candidate). No audit or recovery claim was produced.

However, frozen assertion `partial_preserved` is false. The runner requires a
top-level `DiscoveryResult.limitations` detail containing `partial`; observed
partial state instead appears in the partial candidate's preserved uncertainty,
while the top-level result contains only `ASU adequacy=known_incomplete`.
Therefore the preserved output does not satisfy the frozen ER/control PASS
criterion. This is a validation **FAIL**, not an expected application-level
negative scenario and not a converted PASS.

## Stop boundary

No regression was run. No coverage/disposition conclusion, Finding, H3,
remediation, successor, source/test/shared-file change, Lane B/C change,
Item 4.7 review, Gate/proving/readiness action, or post-result artifact
revision occurred. Raw result, stdout/stderr, exit status, and artifact hashes
are preserved in `raw/`. Cause classification and any later action require
Project Owner direction.
