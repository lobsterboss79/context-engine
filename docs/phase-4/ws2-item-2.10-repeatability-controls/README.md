# WS2 Item 2.10 — Repeatability Controls

**Status:** **PRE-RESULTS CONTROL PREPARATION ONLY.** `RC-P4-2.10-R1 v1` and
`RC-P4-2.10-R2 v1` are additive controls governed for a later, separately
authorized execution. They are not evidence, a validation result, a finding,
or an Item 2.10 completion disposition. R1 and R2 have not been executed.

## Governing baseline and preservation

Both controls reference, without replacing or revising, `FX-F3 v1`, unchanged
`ER-F3 v1`, and immutable historical `VE-F3-001`. The original F3 execution
is not part of either run matrix and must not be rerun under `ER-F3 v1`.

The F3 fixture/ER materialization baseline is
`c7d17714a3983335f8564aa9360739d9ec785410`; its implementation origin is
`IVB-P4-ORIGIN` / `9862497`. This package's preparation baseline is the clean
committed design baseline `25a25dd5f5c5b547278f58ae7609f57bb8acf7a7`.
The separate repeatability-control materialization baseline is the first
commit that contains this package; it must be recorded in future execution
evidence and is not a revision of either F3 baseline.

The frozen F3 input inventory and SHA-256 values are copied in
[repeatability expected results](repeatability-expected-results.md#f3-input-inventory-and-hash-control).
The authoritative historical copy remains the F3 manifest; this copy is a
control reference only.

## Control family

| Control | Expected result | Purpose | Future run count |
| --- | --- | --- | --- |
| `RC-P4-2.10-R1 v1` | `ER-P4-2.10-R1 v1` | Three isolated identical-input executions. | 3 |
| `RC-P4-2.10-R2 v1` | `ER-P4-2.10-R2 v1` | Predesignated reference plus supported incidental-order perturbations. | 4 |

R1 tests repeatability. R2 separately tests whether the supported incidental
mechanisms can affect the established F3 semantic result or semantic order.
No result from one control substitutes for the other.

## Shared comparison and execution constraints

Both controls use the one governed contract in
[repeatability expected results](repeatability-expected-results.md#shared-semantic-comparison-contract-sc-p4-210-v1).
It assesses semantic equality, never raw-byte equality, and keeps every
governed mismatch observable.

Every future run must use a new SQLite database and a new output/evidence
workspace, with no inherited database, audit, cache, generated package, or
rendering. Before execution, the operator must identify any other stateful
component that could influence the result; if it cannot be isolated under
these controls, stop under H3. The approved v0.1 interfaces inspected for
preparation are local-Git/Markdown observation, `GovernedRenderInputs`,
`run_governed_render`, `SQLiteStateStore`, and the three renderers. No network,
dependency, application-source, or test change is authorized by this package.

## Boundary

This package does not approve Gate 4B, proving, TD-14 reopening, remediation,
or production readiness. A semantic mismatch is not to be normalized or
explained away: preserve originals and route it through Item 2.11/finding and
H3 governance as applicable.
