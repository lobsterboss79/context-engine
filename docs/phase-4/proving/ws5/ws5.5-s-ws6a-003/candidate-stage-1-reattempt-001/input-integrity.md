# Stage 1 Reattempt 001 Input Integrity

**Status:** FAIL — PRE-EXECUTION STOP PRESERVED

## Attempt identity and authority

- Attempt: `STAGE-1-REATTEMPT-001`.
- Authority: Project Owner authorization, “STAGE 1 — PREFLIGHT REMEDIATION AND SINGLE REATTEMPT.”
- Authorized remediation: only the temporary B3/B4 Markdown role-table parser correction.
- Logical Consumer: `consumer:I10-DTS-CHATGPT-CANDIDATE-RENDERING-v1` (`CHATGPT`, non-delivery only).
- No physical Consumer was contacted, bound, or disclosed to.

## Successful integrity checks before the stop

- Day Trading System worktree was clean at `e29de5c7d26a31f66cf47c30b295591e6b192887`.
- Frozen task SHA-256 matched `52f3e52bc72c1a9d73789d422f185e15a0d9d56e7889ec98f35eac5eeceec6b4`.
- All approved A1–A4, B1–B6, and C1–C5 candidate artifact SHA-256 values matched the Stage 1 input map.
- The effective-corpus manifest contained SHA-256 `62e55be569bcd8fabd864ab4c4339f384a23c07e53a3d7f5c8579a9b8457680e`.
- Lifecycle preflight found 38 historical semantic records, four valid `provenance_correction` relations, and 34 active terminals including four v2 successors.
- The focused B3/B4 parser validation passed: 34 exact active Claim identities, 23 Required assignments, 11 Supporting assignments, no duplicates, and no historical predecessor record admitted as active.

## Reattempt-specific preflight stop

The reattempt then reached the temporary B2 applicability-matrix parser. That parser reads the approved five-column Markdown table but applies `strip('`')` to the entire first cell before splitting `record / version`. Because the version is outside the Markdown code span, the closing delimiter remains in the parsed record identity. For example, the parser produced:

`dts-semantic-governance-codex-no-material-decisions`` / `v1`

instead of record identity `dts-semantic-governance-codex-no-material-decisions` and version `v1`.

It parsed 34 unique malformed keys, then stopped with:

`KeyError: ('dts-semantic-governance-codex-no-material-decisions', 'v1')`

This is a separate temporary-runner preflight defect. It was not the authorized B3/B4 correction and no correction or further attempt is authorized by the present decision.

## Boundary preservation

- The original attempt remains separately preserved at [`../candidate-stage-1/input-integrity.md`](../candidate-stage-1/input-integrity.md).
- `run_governed_render` was not invoked on this reattempt.
- No Context Package, construction record, or Consumer rendering was produced.
- No approved canonical input, production source, Day Trading System file, frozen successor-003 control, physical Consumer state, or binding was changed.
