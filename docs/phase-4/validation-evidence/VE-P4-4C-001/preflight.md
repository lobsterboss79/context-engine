# VE-P4-4C-001 Preflight Record

**Status:** **COMPLETE BEFORE EXECUTION**

| Check | Observed / frozen value |
| --- | --- |
| Lane / branch | C / `phase4-ws4-backup-restore-linux` |
| Exact baseline | `636afcf72cbd63dc2cfb5f8a0cc5388eb4e9f6f6` |
| Shared ancestry | `git merge-base --is-ancestor 636afcf HEAD` succeeded; `HEAD` is the stated common baseline |
| Starting worktree | Clean before lane-private materialization (`git status --short` produced no output). The only subsequent changes are in this lane's owned namespaces. |
| Platform | LNX-01: Linux `7.0.0-34-generic`, `x86_64`, GNU/Linux |
| Runtime | CPython `3.14.4`; stdlib `sqlite3` `3.46.1` |
| Filesystem | `ext2/ext3`, block size 4096 (reported by `stat -f`) |
| Network / external systems | None used or required. |
| ER hash | `ER-P4-4C-001-v1.md`: `d031e370ffb02cbd70a05add0f295960b65434ad3cbfb13d529e9271c65d3785` |
| Procedure hash | `PC-P4-4C-001-v1.md`: `cf8c8e2eefdc82685f6d1763f30d9254ab73fa04f9b3ef5917843520a2ef6ce6` |
| Executor hash | `raw/execute-p4-4c-001.py`: `036ac591384fc3c6d392ba82d005f67dc8778c6e132c26f05a9c28d784114939` |
| Freeze review | The ER identifies the source, manual backup destination/purpose/retention basis, backup criteria, controlled failure boundary, staged restore, semantic/hash comparisons, historical-only/non-elevation/sufficiency criteria, audit/construction and isolation criteria, and predecessor/successor identities before first execution. |
| Scope / H3 review | The procedure selects no scheduler, remote store, retention duration, deletion workflow, RPO/RTO, HA, service, container, cloud, or added environment. It uses only a lane-private disposable directory. No H3 condition is observed at preflight. |

`git diff --check` passed before execution. Existing source, tests, shared WS4 controls, WS1–WS3 records/evidence, DVL/TD-14, and other lane namespaces remain read-only.
