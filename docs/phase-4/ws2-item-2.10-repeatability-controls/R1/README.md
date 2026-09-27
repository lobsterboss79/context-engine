# `RC-P4-2.10-R1 v1` — Identical-Input Repeatability

**Pre-results only; not executed.** This is the frozen procedure control for
`ER-P4-2.10-R1 v1` and shared `SC-P4-2.10 v1`.

## Future matrix

| Future run | Fixed inputs | Isolation requirement |
| --- | --- | --- |
| `R1-001` | Exact F3 inventory/hashes and unmodified F3 semantic inputs | Fresh SQLite, output/evidence workspace, audit, cache/state, and generated artifacts. |
| `R1-002` | Same | Same; no prior-run artifact or database may be read. |
| `R1-003` | Same | Same; no prior-run artifact or database may be read. |

Before each run, verify the eight frozen hashes in the shared expected-result
record, the approved application baseline, and Bootstrap/configuration
semantics. The execution procedure may use a separately preserved
execution-only control script that invokes existing v0.1 interfaces; it may
not alter application source, tests, F3 inputs, `ER-F3 v1`, or historical F3
evidence. Preserve each run's originals before deriving its semantic
projection.

R1 PASS requires three, not merely two, individually F3-faithful runs and
pairwise semantic equality (`001=002`, `001=003`, `002=003`) under the shared
contract. Any stateful component discovered to influence results must be
isolated before execution; inability to do so is H3.
