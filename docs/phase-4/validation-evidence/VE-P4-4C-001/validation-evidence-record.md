# VE-P4-4C-001 — Manual Backup, Controlled Restore, and Historical Recovery

**Result state:** **PASS**

`ER-P4-4C-001 v1` was frozen before execution and all acceptance criteria were met. This is controlled local/manual validation evidence only; it does not establish current live truth, Authority, Governance State, present authorization, sufficiency, receipt, use, production recovery, or readiness.

## Evidence identity and execution basis

| Field | Preserved value |
| --- | --- |
| Evidence / expected result | `VE-P4-4C-001` / `ER-P4-4C-001 v1` |
| Execution time | 2026-09-30 16:22:50 UTC |
| Branch / baseline | `phase4-ws4-backup-restore-linux` / `636afcf72cbd63dc2cfb5f8a0cc5388eb4e9f6f6` |
| Lane / owned obligations | C / 4.3-A/B, 4.4-A/B, 4.5-A/B, 4.6-A |
| Environment | LNX-01 Linux 7.0.0-34-generic x86_64; CPython 3.14.4; SQLite 3.46.1; ext2/ext3 filesystem. Details and pre-execution hashes: [preflight](preflight.md). |
| Governing basis | Phase 4 checklist 4.3–4.6; WS1 §§1.3–1.5 and 1.9; Domain G ST-03–ST-06, CI-01–CI-05, FR-01–FR-07, BR-01–BR-07; Phase 3 WS10 backup/restore closure; WS4 shared execution and failure/recovery contracts. |
| Procedure | Frozen [PC-P4-4C-001 v1](../../ws4-lane-c-backup-restore/PC-P4-4C-001-v1.md), executed by preserved [executor](raw/execute-p4-4c-001.py). |
| Fixture / scope | Synthetic, disposable Alpha source and Beta target databases under this evidence record only; local, network-free, manual invocation. |
| Findings / H3 / DVL / TD-14 | No Finding; no H3 condition observed; DVL-P4-001 remains active and unchanged; TD-14 remains closed/not reopened. |

## Frozen predecessor → successor recovery lineage

```text
VE-P4-4C-001-PRE (scenario-expected RECOVERY REQUIRED)
  controlled process-local os.replace interruption
  -> RestoreError; byte-identical, valid Beta target preserved
  -> immutable predecessor database and raw result retained
VE-P4-4C-001 (independent successor, PASS)
  unchanged backup revalidated -> staged restore -> historical qualification
  -> Alpha state restored and independently checked
```

The predecessor is not a validation-control FAIL: the ER required this controlled failure state and its preservation. It remains distinct historical evidence. The successor neither rewrites nor relabels it. The prior WS3 `VE-P4-3B-002` is supporting/mechanism evidence only, not this sequence's predecessor.

## Observed result against the frozen criteria

| Obligation | Observed evidence / result |
| --- | --- |
| 4.3-A — manual backup | `backup-alpha.sqlite` was created at the explicit lane-private destination. Its one metadata row records identity `backup-p4-4c-001-alpha`, the explicit purpose, fixture-only bounded retention basis, and schema version 5. `validate_backup` and SQLite integrity both passed. |
| 4.3-B — controlled restore | The unchanged backup was revalidated, copied to staging, qualified, revalidated, and then replaced locally. No staging file remained. |
| 4.4-A — state/Provenance/history/isolation | Raw semantic projections show source Alpha equals restored Alpha for evidence, Source, observation, artifact, transformation, representation/Provenance, construction, and audit. Beta is absent after replacement; Project-scoped Beta result sets are empty. |
| 4.4-B — audit/construction | Alpha's historical construction record and authorized audit row survived. The audit read with `authorized=False` raised `PermissionError`; diagnostics were not represented as audit or recovery evidence. |
| 4.5-A — no present-status manufacture | Restored evidence is `currentness: unknown` with `authority_basis: null`. The recovery qualification says `historical-only` and expressly requires independent re-establishment of currentness, Authority, Governance State, and present authorization. |
| 4.5-B — no sufficiency manufacture | The restored construction remains `sufficiency: insufficient` and `coherence: coherent_with_qualification`. Backup metadata and recovery qualification contain no sufficiency/currentness/Authority grant. |
| 4.6-A — recovery after controlled failure | The frozen failure produced `RestoreError` with scenario state `RECOVERY REQUIRED`. Before the successor, Beta's target SHA-256 was unchanged, its semantic projection remained intact, integrity was `ok`, and no staging file remained. The retained predecessor database is a separate immutable artifact. |

The raw [result](raw/state/result.json) contains all 15 passing assertion values, semantic projections, integrity values, predecessor classification, qualification, and four database identities. [stdout](raw/execute.stdout) records the concise result; [stderr](raw/execute.stderr) is intentionally empty.

## Non-manufacture and recovery conclusion

The restored bytes preserve historical durable evidence; they do not make the backup Source truth or a receipt/use claim, make Alpha current, grant Authority or present authorization, establish Governance State, or make the construction sufficient. The modeled operator authorization is only the existing application authorization input required to execute the procedure; it is not evidence of a new authority. The controlled failure remained visible and recoverable without changing its predecessor, losing Provenance, relaxing isolation/authorization, or treating diagnostics as durable audit/recovery evidence.

No scheduler, remote backup, retention duration/deletion workflow, RPO/RTO, HA, service/daemon, container, cloud infrastructure, or additional environment was added or found necessary. This lane result therefore creates no Item 4.7 disposition and no scope expansion.

## Raw-artifact SHA-256 manifest

| Artifact | SHA-256 |
| --- | --- |
| `raw/execute-p4-4c-001.py` | `036ac591384fc3c6d392ba82d005f67dc8778c6e132c26f05a9c28d784114939` |
| `raw/execute.stdout` | `82938a8182ea43d1dcc19a6b6c085eddbbe29db7fb164aa28ccb352bd2a86ddd` |
| `raw/execute.stderr` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `raw/state/backup-alpha.sqlite` | `a197265f66b3f75a118b7d9fa58755f5765b905d448d23f749ad9c33d12fbf9c` |
| `raw/state/predecessor-failed-target-beta.sqlite` | `1a188272fd5c2aed4b7b789641e5e857a925eae1ec6790da98773e926a89be8d` |
| `raw/state/result.json` | `6ad881217f0bee69dd7a57a4505b51db3e713f139e9289d6119ad21c1b676994` |
| `raw/state/source-alpha.sqlite` | `ba1cc8abd23b6d6247564751ed139ac2433b91d4d1c6245550571fe6b5c612fa` |
| `raw/state/target.sqlite` | `bae5ca6be1364c82d1541502f2ace5502ef1773d59e10f4dafeb8af39c439ecd` |

The raw artifacts are lane-private preservation records. No existing evidence or shared material was altered.
