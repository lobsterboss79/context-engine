# WS2 Item 2.10 — Repeatability-Control Preparation Record

**Status:** **COMPLETE PRE-RESULTS PREPARATION ONLY.** Item 2.10 remains
**INCOMPLETE**. This record creates no run, result, evidence record, finding,
completion decision, Gate 4B approval, proving authorization, TD-14 action, or
production-readiness claim.

## Authority, scope, and result boundary

The Project Owner approved
[`ws2-item-2.10-evidence-coverage-design-analysis.md`](ws2-item-2.10-evidence-coverage-design-analysis.md)
as the committed design basis and approved its F3 semantic baseline, the
three-run R1 direction, semantic (not accidental byte) stability, and the
additive pre-results control requirement. This preparation implements that
approved direction only. It does not revise `FX-F3 v1`, `ER-F3 v1`, or
`VE-F3-001`; the originals remain immutable.

## Inspection and H3 check

Read-only inspection covered `AGENTS.md`; the Phase 4 checklist and
validation-governance package; the F3 fixture/ER, historical F3 procedure,
raw result, manifest, and evidence record; the Phase 1–3 ordering records; and
the current v0.1 discovery, orchestration, persistence, construction, and
rendering interfaces. No material contradiction with the approved Phase 0–3
records was found. Therefore H3 is not triggered for this preparation.

The inspected records establish semantic ordering by discovery mechanism then
represented-information and Provenance identities; Source Manifest order by
Source identity; canonical renderer presentation from one package view; and
SQLite row IDs as private implementation details. They also establish that
recency/currentness, frequency, rank, and score do not create selection
semantics. These are supporting design evidence only; the future controls are
the required integrated observations.

## Prepared artifacts

The additive package is [ws2-item-2.10-repeatability-controls](ws2-item-2.10-repeatability-controls/):

- `RC-P4-2.10-R1 v1` / `ER-P4-2.10-R1 v1`: three frozen, independent,
  identical-input runs.
- `RC-P4-2.10-R2 v1` / `ER-P4-2.10-R2 v1`: one predesignated reference and
  three bounded, individually isolated incidental-order runs.
- `SC-P4-2.10 v1`: one shared semantic-comparison contract, narrow volatile
  allowlist, and prohibited-normalization rule.

The control package separately records F3's original fixture/ER baseline, this
preparation baseline, and the future control-materialization baseline. The
Project Owner-approved provenance-only correction retains the two historical
whole-register hashes at `c7d17714` as provenance evidence and adds two frozen
current extracted-record integrity hashes for `FX-F3 v1` and `ER-F3 v1`. It
does not require current shared-register whole-file equality, and it does not
copy or change F3. The six actual F3 controlled-file hashes remain frozen.
See [the F3 register provenance investigation](ws2-item-2.10-f3-register-provenance-investigation.md):
R1 stopped before execution, no validation evidence was created, Classification
A is Project Owner approved, and Finding not warranted is approved.

This correction is provenance/control representation only. It does not change
`FX-F3 v1`, `ER-F3 v1`, F3 controlled Sources, F3 semantics,
`SC-P4-2.10 v1`, either R1/R2 semantic expectation, the R1 three-run design,
the R2 reference/four-run matrix, Item 2.10 obligation mapping, application
behavior, or tests. Item 2.10 remains incomplete; R1 is authorized in
principle but not re-executed, and R2 remains not authorized for execution.

## R2 feasibility disposition

Fixed `PYTHONHASHSEED`, in-memory Source/observation presentation order, and
application-input mapping insertion order are supported by current existing
interfaces without product changes. SQLite insertion ordering and filesystem
enumeration are not applicable to the normal F3 execution path; adding either
would create an unsupported path and is excluded. No semantically equivalent
frequency perturbation is safe for F3. Currentness is intentionally preserved,
not changed. The R2 negative acceptance criteria retain the corresponding
prohibitions and require every supported perturbation result to expose no
unauthorized rank basis.

## Non-execution attestation

No R1, R2, or F3 execution occurred. No application/source code, test,
checklist status, historical F3 artifact, expected-result baseline, finding,
limitation register, or governance disposition was modified. No dependency was
introduced. Future execution remains separately governed and must preserve
original artifacts before comparison.
