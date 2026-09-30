# Lane A Successor Expected Results — `ER-P4-4A-002 v1`

**Status:** Frozen for the authorized successor execution. **Control:**
`CTL-P4-4A-002 v1`; **procedure:** `PROC-P4-4A-002 v1`; **fixture:** immutable
`FX-P4-4A-001 v1` at `fixtures/`.

## Lineage and unchanged semantics

`VE-P4-4A-001` remains permanently INDETERMINATE because of its runner
construction error. The approved investigation classified it A — Lane Control /
Runner Design Error, with no Finding, no H3, and Windows not material. This
successor neither modifies nor reclassifies the predecessor.

This ER preserves the v1 semantic expectations unchanged: malformed input and
invalid configuration are `APPLICATION-LEVEL FAILURE` (CLI exit 2); bounded
Source outcomes are `ABSENCE`, `UNAVAILABLE`, `PARTIAL EVIDENCE`, and
`SUCCESSFUL COMPLETION`; a matching expected negative outcome can produce
validation PASS; and diagnostics must be attributable, useful, canary-safe,
not durable audit, not recovery evidence, and not success.

## Frozen criteria

| Field | Frozen successor requirement |
| --- | --- |
| Governing basis | Checklist 4.1/4.6; Phase 2 Domain G ST-06, CI-02, FR-01, FR-03--FR-07, OM-02--OM-04; Phase 3 WS3/WS6/WS8/WS9/WS10; WS1 preservation/result/Finding/H3 rules; approved v1 investigation. |
| Controlled inputs | Unchanged v1 malformed Bootstrap TOML; unchanged valid Bootstrap plus mismatched project configuration; v2 runner's lane-private in-memory Source construction. |
| PASS criteria | Both CLI cases: exit 2, attributable `bootstrap validation failed:` diagnostic, no `validated`, no canary; four named Source states are distinct; absent/unavailable have zero candidates, unavailable has limitation, partial has a candidate and partial limitation, success has a candidate without partial limitation; no audit/recovery claim; raw output and preflight are preserved. |
| Validation FAIL criteria | Any v1 negative criterion occurs, four required states collapse, required artifacts are contradictory, source/tests/shared files change, or execution differs from frozen successor procedure. |
| INDETERMINATE criteria | Required evidence/preflight is absent or insufficient, or a procedure/evidence deficiency prevents assessment. |
| Qualifications | `ABSENT` is bounded ASU absence, not universal nonexistence. `UNAVAILABLE` is not inaccessible; DVL-P4-001 remains active. The Source exercise makes no Windows filesystem/path/permission/Git/process or Linux claim. |

No semantic ER revision is made from v1: this record only identifies the
separately versioned successor evidence/control lineage.
