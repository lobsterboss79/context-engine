# VE-P4-4B-002 Durable Preflight Record

**Status:** PRE-EXECUTION — durable hard-gate record. Created before any `VE-P4-4B-002` runner invocation or raw state.

## Identity and contemporaneous environment

| Field | Observed value |
| --- | --- |
| Branch / HEAD | `phase4-ws4-persistence-linux` / `4fe1f26a431cf09bfe3dbf6793e94aba4ec522b1` |
| Required baseline / ancestry | `636afcf` / `git merge-base --is-ancestor 636afcf HEAD` exit 0 |
| Linux | Ubuntu 26.04.1 LTS (resolute), kernel `7.0.0-34-generic`, x86_64 |
| Python / SQLite | CPython 3.14.4 / SQLite 3.46.1 |
| Workspace mount | `/dev/mapper/ubuntu--vg-ubuntu--lv`, ext4, `rw,nosuid,nodev,relatime` |
| Worktree status | Only the newly frozen v2 ER/PC/runner were untracked; no tracked modifications or other paths were reported. This is the expected lane-private preparation state, not a claim of empty porcelain output. |
| Source integrity | baseline `src` tree `fc30779888150acdd9e15eb35d38ec04cdaf5564`; `git diff --quiet 636afcf HEAD -- src tests` exit 0 |
| Test integrity | baseline `tests` tree `a77d5907ce0c64d7c465e64a3e5dda76a6b91b78`; same comparison exit 0 |
| Shared integrity | `git diff --quiet 636afcf HEAD -- AGENTS.md README.md docs/phase-4/ws4-validation-controls docs/phase-4/ws4-shared-control-materialization.md docs/phase-4/workstream-1-validation-governance-evidence-model.md docs/phase-4/deferred-validation-accepted-limitations-register.md` exit 0 |

## Frozen artifacts and sequence

| Artifact | SHA-256 |
| --- | --- |
| `ER-P4-4B-002-v1.md` | `bcddf25ab09d4dea6b0599474daf651da9f0ae7f60bc8ddd6c4b4c0e3bef99fe` |
| `PC-P4-4B-002-v1.md` | `bfb84b31a92d88acce1633ecbe5f54df53b061ce9a4fefae7ef2e0813ea29445` |
| `FX-P4-4B-002-runner.py` | `33a5eb4b1ae45fd77fbc803cbff1463f2bd101ddb274947a6ee7830b325f7928` |

The runner compiled successfully before this record. Before this record was created, `test ! -e docs/phase-4/validation-evidence/VE-P4-4B-002` exited 0. The frozen identities are predecessor `VE-P4-4B-002`, successor `VE-P4-4B-002-S1`, and migration `VE-P4-4B-002-M1`.

The exact frozen invocations are:

```bash
PYTHONPATH=src python3 docs/phase-4/ws4-lane-b-persistence/FX-P4-4B-002-runner.py predecessor --out docs/phase-4/validation-evidence/VE-P4-4B-002/raw/state > docs/phase-4/validation-evidence/VE-P4-4B-002/raw/stdout.txt 2> docs/phase-4/validation-evidence/VE-P4-4B-002/raw/stderr.txt
PYTHONPATH=src python3 docs/phase-4/ws4-lane-b-persistence/FX-P4-4B-002-runner.py successor --predecessor-state docs/phase-4/validation-evidence/VE-P4-4B-002/raw/state --out docs/phase-4/validation-evidence/VE-P4-4B-002-S1/raw/state > docs/phase-4/validation-evidence/VE-P4-4B-002-S1/raw/stdout.txt 2> docs/phase-4/validation-evidence/VE-P4-4B-002-S1/raw/stderr.txt
PYTHONPATH=src python3 docs/phase-4/ws4-lane-b-persistence/FX-P4-4B-002-runner.py migration --out docs/phase-4/validation-evidence/VE-P4-4B-002-M1/raw/state > docs/phase-4/validation-evidence/VE-P4-4B-002-M1/raw/stdout.txt 2> docs/phase-4/validation-evidence/VE-P4-4B-002-M1/raw/stderr.txt
```

Expected predecessor scenario state is `APPLICATION-LEVEL FAILURE / RECOVERY REQUIRED`; validation PASS requires the exact expected `RestoreError`, unchanged old target hash, Project-B-only old target, integrity/schema/backup pass, no recovery qualification, and no staging file. Negative criteria are any successful replacement/source state in predecessor target, hash change, integrity/schema discrepancy, qualification/staging state, missing raw output, or evidence/control/source/test/shared change. Only then may the already frozen successor and migration commands execute; each is independently classified and never changes predecessor history.
