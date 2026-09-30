# VE-P4-4A-003 Portable Preflight Record

**Result:** **PASS — preserved before semantic execution.**

## Lineage and literal Git checks

Preflight ran on `phase4-ws4-input-diagnostics-win` at committed HEAD
`0af099b62de675ad01daf01aa17a3e077cee74a9`. It used only frozen literal-SHA
forms `git rev-parse --verify --quiet <SHA>` and
`git merge-base --is-ancestor <SHA> HEAD`, never `^{commit}` or another
shell-sensitive revision expression. The checks passed for shared baseline
`636afcf72cbd63dc2cfb5f8a0cc5388eb4e9f6f6`, VE-001
`1fdef6ee07c5a6f5e6663f34b85b6e339845bd03`, its investigation
`f55d2541b7c650e28cdfa70dc0ff3648ff11fa51`, VE-002
`85d0adfcf0dd8aa5122f452fb654f0a7c6338c82`, and its investigation
`0af099b62de675ad01daf01aa17a3e077cee74a9`.

## Artifact, environment, and scope checks

The 003 namespace was fresh before creation. The preflight verified that the
unchanged 002 semantic ER, three v1 fixture files, and corrected v2 runner
match the committed 002 basis; direct `SemanticIdentity` construction remains
exactly one two-field `(kind, value)` call. Source, tests, `pyproject.toml`,
shared WS4 surfaces, and Lane B/C namespaces are unchanged.

Execution environment: Microsoft Windows NT 10.0.22631.0; external isolated
venv `Z:\temp\context-engine-phase4-validation\Scripts\python.exe`, CPython
3.14.7, pytest 9.1.1. The external environment's collection-only PASS collected
60 tests for the frozen five-module regression slice.

The exact controlled-artifact hashes, literal Git command output, and frozen
semantic invocation/expected-state/acceptance/negative criteria are preserved
in [`raw/`](raw/). This record is the durable pre-execution evidence for
`PROC-P4-4A-003 v1`; its SHA-256 is preserved in `raw/preflight-record-sha256.txt`
before semantic execution.
