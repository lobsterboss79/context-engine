# Candidate Role and Selection Inputs — Group B

**Status:** **CANDIDATE — NOT FROZEN — OWNER APPROVAL PENDING**

Common proposed selection basis:

> The frozen continuation brief requires the stated purpose, state,
> authorization boundary, constraint/gap, historical distinction, or material
> provenance qualification; selection is task-relative and creates no
> authority.

For every row, `consumer_capacity_limited=False` and
`rendering_limited=False` are proposed only. No role is reduced for assumed
capacity. Selection cannot execute unless the B1 applicability gates pass.

| Claim group / active Claims | Proposed role | Exact RoleInputs flags | Counterfactual basis / alternative |
| --- | --- | --- | --- |
| Governance: `codex-no-material-decisions`, `live-trading-explicit-authorization`, `project-owner-material-decisions` | Required | incorrect=True; improper=False; improves=True | Omission loses governing-decision/authority boundary. |
| Overview: `no-trade-valid-state`, `numerical-validation-gates-unapproved`, `project-purpose`, `research-universe-not-live-trading` | Required | True; False; True | Omission loses purpose or explicit constraint/gap. |
| PDR-016: `approved`, `material-choices-owner-review`, `no-capital-deployment-authority`, `no-live-trading-authority`, `phase3-authorized` | Required | True; False; True | Omission loses current decision/authorization boundary. |
| Phase 1: `complete`, `deferrals-not-incomplete-work`, `live-trading-deferred` | Required | True; False; True | Omission prevents requested historical/current distinction. |
| Phase 2: `no-capital-deployment-authority`, `no-live-trading-authority`, `no-unresolved-major-minor`, `validation-not-implementation` | Required | True; False; True | Omission loses historical constraints and implementation boundary. |
| Roadmap: `no-unapproved-numerical-gates`, `phase2-complete`, `phase3-authorized`, `phase3-implementation-not-begun` | Required | True; False; True | Omission loses current state, gap, or legitimate next boundary. |
| Active v2 reproducibility: `formal-evidence-code`, `formal-evidence-configuration`, `formal-evidence-data`, `formal-evidence-experiment-definition` | Supporting | incorrect=False; improper=False; improves=True | Omission weakens material provenance qualification; v2 only. |
| Other reproducibility: `git-sha-code-identity`, `orphaned-output-not-final-evidence`, `recording-not-reproduction` | Supporting | False; False; True | Omission weakens provenance/limitation explanation. |
| Research governance: `experiments-permanent`, `exploratory-not-confirmatory`, `identifiers-never-reused`, `records-distinct-from-pdrs` | Supporting | False; False; True | Omission weakens material research provenance/history explanation. |

The groups enumerate all 34 active Claims: 23 proposed Required and 11
proposed Supporting. The historical successor-003 34-Required result is
preserved; this candidate does not alter it. The alternative classification is
to retain all 34 as Required, which requires an Owner decision and is not
selected merely to match historical evidence or the evaluator.

## Exact per-Claim RoleInputs bindings

`R` means `RoleInputs(True, False, True, common_selection_basis, False,
False)`; `S` means `RoleInputs(False, False, True, common_selection_basis,
False, False)`. The named `common_selection_basis` is the exact basis quoted
above. These are complete candidate bindings for the active corpus only.

| Active Claim | Binding |
| --- | --- |
| `dts-claim-governance-codex-no-material-decisions-v1` | R |
| `dts-claim-governance-live-trading-explicit-authorization-v1` | R |
| `dts-claim-governance-project-owner-material-decisions-v1` | R |
| `dts-claim-overview-no-trade-valid-state-v1` | R |
| `dts-claim-overview-numerical-validation-gates-unapproved-v1` | R |
| `dts-claim-overview-project-purpose-v1` | R |
| `dts-claim-overview-research-universe-not-live-trading-v1` | R |
| `dts-claim-pdr016-approved-v1` | R |
| `dts-claim-pdr016-material-choices-owner-review-v1` | R |
| `dts-claim-pdr016-no-capital-deployment-authority-v1` | R |
| `dts-claim-pdr016-no-live-trading-authority-v1` | R |
| `dts-claim-pdr016-phase3-authorized-v1` | R |
| `dts-claim-phase1-complete-v1` | R |
| `dts-claim-phase1-deferrals-not-incomplete-work-v1` | R |
| `dts-claim-phase1-live-trading-deferred-v1` | R |
| `dts-claim-phase2-no-capital-deployment-authority-v1` | R |
| `dts-claim-phase2-no-live-trading-authority-v1` | R |
| `dts-claim-phase2-no-unresolved-major-minor-v1` | R |
| `dts-claim-phase2-validation-not-implementation-v1` | R |
| `dts-claim-reproducibility-formal-evidence-code-v1` | S (active record v2) |
| `dts-claim-reproducibility-formal-evidence-configuration-v1` | S (active record v2) |
| `dts-claim-reproducibility-formal-evidence-data-v1` | S (active record v2) |
| `dts-claim-reproducibility-formal-evidence-experiment-definition-v1` | S (active record v2) |
| `dts-claim-reproducibility-git-sha-code-identity-v1` | S |
| `dts-claim-reproducibility-orphaned-output-not-final-evidence-v1` | S |
| `dts-claim-reproducibility-recording-not-reproduction-v1` | S |
| `dts-claim-research-experiments-permanent-v1` | S |
| `dts-claim-research-exploratory-not-confirmatory-v1` | S |
| `dts-claim-research-identifiers-never-reused-v1` | S |
| `dts-claim-research-records-distinct-from-pdrs-v1` | S |
| `dts-claim-roadmap-no-unapproved-numerical-gates-v1` | R |
| `dts-claim-roadmap-phase2-complete-v1` | R |
| `dts-claim-roadmap-phase3-authorized-v1` | R |
| `dts-claim-roadmap-phase3-implementation-not-begun-v1` | R |
