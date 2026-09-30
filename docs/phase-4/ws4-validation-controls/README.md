# Phase 4 WS4 Validation Controls — Shared Foundation

**Status:** **PRE-EXECUTION SHARED FOUNDATION PREPARED — PROJECT OWNER REVIEW / COMMIT REQUIRED BEFORE CROSS-MACHINE BRANCHING**

This pre-results package freezes the shared controls for the approved WS4
three-lane topology. It is subordinate to the Phase 4 checklist, WS1
validation-governance package, and the approved
[WS4 topology](../ws4-dependency-parallelization-execution-plan.md). It
creates no fixture, expected result (ER), procedure, execution, evidence,
Finding, branch, worktree, status change, Gate activity, proving, remediation,
or readiness claim.

## Contents and frozen use

- [Obligation register](obligation-register.md): ownership, exact checklist
  wording, platform, dependency, evidence and reuse classification for all
  approved analytical obligations.
- [Execution contract](execution-contract.md): shared evidence, platform,
  cross-machine, ownership, vertical-authority, immutability and stop rules.
- [Failure/recovery contract](failure-recovery-contract.md): expected scenario
  state versus validation result; predecessor/successor and recovery invariants.
- [Item 4.7 integration contract](item-4.7-integration-contract.md): the
  main-only H3 review after lane integration.

## Arithmetic reconciliation

The approved topology text calls for “16 approved analytical obligations” but
lists `4.1-A` through `4.6-B` (16 lane-owned obligations) **and** main-only
`4.7-A`. This foundation therefore freezes **17 total analytical obligations**:
**16 lane-owned + 1 main-only integration obligation**. It neither adds a
requirement nor omits Item 4.7.

## Frozen topology

| Owner | Obligations | Platform | Namespace / evidence |
| --- | --- | --- | --- |
| Lane A — Input, Configuration & Diagnostic Distinctions | 4.1-A–D, 4.6-B | Windows | `docs/phase-4/ws4-lane-a-input-diagnostics/`; `VE-P4-4A-*` |
| Lane B — Interruption, Persistence & Partial State | 4.2-A–D | LNX-01 | `docs/phase-4/ws4-lane-b-persistence/`; `VE-P4-4B-*` |
| Lane C — Manual Backup, Restore & Historical Recovery | 4.3-A/B, 4.4-A/B, 4.5-A/B, 4.6-A | LNX-01 | `docs/phase-4/ws4-lane-c-backup-restore/`; `VE-P4-4C-*` |
| Main-only integration | 4.7-A | main only | this package and later main-only review |

Lane A branch/worktree: `phase4-ws4-input-diagnostics-win` /
`/z/projects/context-engine-worktrees/ws4-input-diagnostics-win`.

Lane B branch/worktree: `phase4-ws4-persistence-linux` /
`~/Projects/context-engine-worktrees/ws4-persistence-linux`.

Lane C branch/worktree: `phase4-ws4-backup-restore-linux` /
`~/Projects/context-engine-worktrees/ws4-backup-restore-linux`.

All lanes must originate from the same later committed shared-foundation commit.
No lane may originate from uncommitted state. Windows must commit and push the
foundation before LNX-01 creates a worktree. LNX-01 must fetch and verify that
exact commit; no cross-machine file copy or assumed unpushed work can establish
lineage.

## Boundary

Gate 4B remains **NOT APPROVED**; fresh-Consumer preflight/proving remain
**NOT AUTHORIZED**; production readiness remains **NOT ESTABLISHED**.
