# VE-P4-3B-002 — PC-P4-3B-001 v2 Validation Evidence Record

**Result state:** **PASS**  
**Disposition:** The frozen successor procedure, unchanged `ER-P4-3B-001 v1`
semantic expectations, and all B1–B4 assertions were satisfied. This is an
independent successor result; it does not alter `VE-P4-3B-001`, which remains
immutable **INDETERMINATE**.

| Field | Preserved record |
| --- | --- |
| Execution identity / baseline | `VE-P4-3B-002`; `phase4-ws3-trust-state-audit` at committed investigation baseline `243f44eb36efae4a332508ee3e4b419fd7c17aca`. Original application validation baseline remains `9862497`; predecessor execution baseline remains `a06e4da`. |
| Predecessor lineage | `VE-P4-3B-001` -> immutable INDETERMINATE procedure/evidence-capture defect -> approved investigation Classification A / NO FINDING / H3 not triggered -> Project Owner Option-1 procedure/runner successor -> this independent evidence. |
| Governing controls | Unchanged `ER-P4-3B-001 v1` (hash `4496ac47c23fbec8161dfc63c90dae19f7eac897e4682e89211e53ae56abce24`); frozen `PC-P4-3B-001 v2` (hash `b9ce18b1e4efc95d5eee0383352449c56a294f048f7dc6d5f3e24361e0cda96b`); frozen runner v2 (hash `57dac66485a26bf5fd7a8681498a960499c42e932b0f32bceb27f9ccc1503f69`). |
| Inputs / fixture semantics | Same synthetic B1–B4 values and existing public v0.1 decision/state-store interfaces as v1. No fixture or semantic expected-result change occurred. |
| Environment | Local network-free `PYTHONPATH=src python3` execution; raw process invocation is preserved in `raw/procedure.txt`. |
| Exact procedure | [raw/procedure.txt](raw/procedure.txt); `raw/` existed, `raw/state/` was absent, stdout/stderr were opened outside state, and runner v2 received only the fresh state path. |
| Procedure integrity | PASS — runner v2 rejected existing state, had no delete/clear operation, created `raw/state/`, and did not remove the capture paths. |
| Raw stream preservation | PASS — [stdout](raw/stdout.txt) exists (821 bytes); [stderr](raw/stderr.txt) exists (0 bytes). Both remained path-addressable after process completion. |
| Raw state/result | PASS — `source.sqlite`, `backup.sqlite`, `restored.sqlite`, and `result.json` each exist under [raw/state](raw/state/). |
| B1 comparison | PASS — matching scoped/Approved/CURRENT candidate `applicable`; mismatch scope, PROPOSED state, and absent Authority `unresolved`; HISTORICAL `inapplicable` for current task and `applicable` for explicit historical task. |
| B2 comparison | PASS — reload/restore returned `currentness: unknown` and no Authority basis; Project-B lookups were absent; recovery qualification retained historical-only/independent-re-establishment semantics. |
| B3 comparison | PASS — restored Alpha representation retained `ws3b-provenance`; Beta representation was absent; historical governed use for current task was inapplicable. |
| B4 comparison | PASS — Alpha's minimized audit row survived restoration; Beta audit was empty; unauthorized audit read raised `PermissionError`; no audit Authority/currentness field exists. |
| Result / Finding | PASS; no discrepancy, Finding, or H3 condition. |

## Raw-artifact SHA-256 manifest

| Artifact | SHA-256 |
| --- | --- |
| `raw/procedure.txt` | `2965c77d498f77012d51c3ef699c58993ae614dcce6c108fe2a86e95f780dd20` |
| `raw/stdout.txt` | `3922c23229128075bafef871616049bf88221992707c70f3c924c49bf3e32f3b` |
| `raw/stderr.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `raw/state/backup.sqlite` | `1749581af1795c4e770bee3f67169822d12c7275e714df499844086be0ca375d` |
| `raw/state/restored.sqlite` | `3fad4499159c72171bbcf0b2538659ebf28346fa4decac1cbdb5ef43815d13e0` |
| `raw/state/result.json` | `5b873563096e3d3e099ffd6834399b327605b491030d8436019cd8253b21baf4` |
| `raw/state/source.sqlite` | `1de898b0595a04f6121a8fa195f14ca03d2cf86dc836e5bbbbb3504f5723501b` |

`VE-P4-3B-001` predecessor raw hashes and its ER/runner hashes were verified
unchanged in this successor's preflight. The successor does not convert,
overwrite, or reinterpret the predecessor.
