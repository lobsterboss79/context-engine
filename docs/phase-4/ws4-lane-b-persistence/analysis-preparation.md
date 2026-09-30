# Phase 4 WS4 Lane B — Analysis and Preparation

**Status:** Pre-results preparation only. This is not a validation result, Finding, disposition, or WS4 closure activity.

## Scope, baseline, and freeze

Lane B owns only checklist 4.2-A through 4.2-D on LNX-01. The execution branch is `phase4-ws4-persistence-linux`, whose required common baseline is `636afcf` (`Prepare Phase 4 WS4 validation foundation`). Shared controls, source, tests, prior evidence, DVL/TD-14, and Lane A/C paths are read-only. New material is limited to this directory and `VE-P4-4B-*` evidence.

Gate 4A authorizes execution inside the approved validation package. Gate 4B, proving, TD-14 reopening, remediation, and readiness remain unauthorized. DVL-P4-001 remains active, accepted/deferred, and not implicated by this SQLite-only control.

## Governing semantics and applicability

| Obligation | Governing semantics | Frozen applicability / minimum faithful method |
| --- | --- | --- |
| 4.2-A interrupted operations | Domain G ST-06, G8 FR-01/FR-02/FR-05/FR-06, G12 TV-03 | Deliberately raise `OSError` only at the existing `SQLiteStateStore.restore_backup` staged-file `os.replace` seam, after staging validation and before target replacement. This is an application-process, disposable-fixture seam; no process kill, permission, disk, or host failure is used. |
| 4.2-B persistence integrity | Domain G G6 CI-01–CI-05 and G8 FR-04 | Inspect `PRAGMA integrity_check`, schema version, Project-keyed records, and staged-file cleanup in the preserved predecessor state. This observes integrity; it makes no unobserved filesystem-durability claim. |
| 4.2-C transaction/partial state | Domain G G6 CI-02/CI-03 and G8 FR-02/FR-05 | The failed predecessor must preserve the old valid target, retain no recovery qualification, expose no source-backed state as complete, and leave no staged restore database. A pre-frozen successor copies—not modifies—the predecessor evidence, then performs the normal replacement and verifies historical-only, Project-isolated recovered state. |
| 4.2-D migration where applicable | Domain G G6 and G12 TV-03/TV-04; Phase 3 WS10 closure | Applicable: `SQLiteStateStore.initialize` contains supported, ordered v1→v2→v3→v4→v5 migrations. A lane-private v1 database with the documented v1 tables/data will be initialized and inspected for v5, all expected migrated tables, retained v1 evidence, and SQLite integrity. No migration is invented and no migration-interruption claim is made. |

Phase 3 WS10 and existing tests are supporting implementation evidence only. They do not close this WS4 control. The executable runner invokes public state-store interfaces except for constructing the documented v1 schema for the migration input and temporarily replacing the in-process adapter-module `os.replace` reference at the defined seam.

## Frozen predecessor/successor contract

The complete sequence is frozen before predecessor execution:

1. `VE-P4-4B-001`: create disposable source/target SQLite state and a valid backup; force only replacement to fail; preserve source, backup, old target, JSON result, and checksums.
2. `VE-P4-4B-002`: copy the predecessor target and backup into a distinct evidence directory; confirm the copied pre-recovery target hash equals the preserved predecessor target hash; perform the unmodified replacement; preserve independent raw state and result.
3. `VE-P4-4B-003`: independently create and migrate documented v1 state to v5; preserve its raw database and result.

The predecessor's scenario state is `APPLICATION-LEVEL FAILURE / RECOVERY REQUIRED`; its validation result is PASS only if its frozen criteria hold. The successor never changes that predecessor result.

## Negative and stop criteria

The control fails (and execution stops/preserves) if replacement does not produce the expected `RestoreError`; old target identity/state changes; integrity is not `ok`; a source record appears before successful successor recovery; a recovery qualification appears in the predecessor; a staging file remains; predecessor hashes cannot be preserved; Project isolation or historical-only qualification fails; migration does not reach version 5 with retained v1 evidence/integrity; or a result is indeterminate. Any need to alter shared files/source/tests/ER, a durability/atomicity ambiguity beyond the observations, a DVL/TD-14 decision, Finding/H3, or infrastructure requirement also stops work.

The procedure creates no schedule, retention duration, deletion workflow, RPO/RTO, HA, daemon/service, container, cloud, or additional integration environment. The existing manual-local nature of the underlying backup is observed only as a bounded implementation condition, not a Lane B operational-policy conclusion.
