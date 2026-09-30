# VE-P4-4B-002 Focused Regression Preflight v2

**Status:** COMPLETE BEFORE REGRESSION INVOCATION.

| Check | Observed result |
| --- | --- |
| Branch / HEAD | `phase4-ws4-persistence-linux` / `5ec5c7df57cfbe8e9536eba5f706163ec98975c2` |
| Shared baseline ancestry | `git merge-base --is-ancestor 636afcf HEAD` exit 0 |
| Interpreter | `/home/lobsterboss79/temp/context-engine-ws2-validation.qNq9B4/bin/python`, exists and executable |
| Python / pytest | CPython 3.14.4 / pytest 9.1.1; both imported successfully |
| Source/test integrity | `git diff --quiet 636afcf HEAD -- src tests` exit 0 |
| Shared integrity | governed shared-file comparison to `636afcf` exit 0 |
| Semantic evidence integrity | predecessor, successor, migration result hashes recorded below; no semantic control is invoked by regression |

## Frozen identities and SHA-256

```text
2aadbcfa4d89337633f200b04a79f39202585d4e21dcf738b954083c8bf6d0a4  tests/test_workstream_3.py
158b9ef1943f03a755edf0a26fb71d537b07a212da5c6295ad3ad86e9b08ca75  tests/test_workstream_4.py
a8cd8bf5c40032012bf684f41cc3b3e618f4d097d610ed5fd8aa1d49cf644e13  tests/test_workstream_8.py
1265bcfcecfa532b711dbb112a5175ccd333b1226c0c10f43dfc1af6df2465a8  tests/test_workstream_10.py
d2e3f4a32744df2bb1c35014e7bb0f8cbfa8f52b96f45e1a962e36ef986002c9  ../preflight.md
05342f9713615f7217e7de74f86034e6f0d7b8a68a1d639b4541225e4243d4aa  ../preflight.sha256
5a332e69a38f1492908a734973fee728b5045a873582f9c7b4a4fcf5d3a18fec  ../raw/state/result.json
c6462d0868ff988c5d198676ed1855e1ac47c61c5e0d67e3e73672963aca239d  ../../VE-P4-4B-002-S1/raw/state/result.json
e8865f18012c0ef3e9c0ef511c34529a66c00599e7100b5ac6893688bdd28c6a  ../../VE-P4-4B-002-M1/raw/state/result.json
85c7d80fba321c8dcbc91d4951d29db1d43cd5155daf3ce52846f45514473986  procedure-v2.md
```

## Exact invocation and criteria

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src /home/lobsterboss79/temp/context-engine-ws2-validation.qNq9B4/bin/python -m pytest -p no:cacheprovider tests/test_workstream_3.py tests/test_workstream_4.py tests/test_workstream_8.py tests/test_workstream_10.py > docs/phase-4/validation-evidence/VE-P4-4B-002/regression/stdout-v2.txt 2> docs/phase-4/validation-evidence/VE-P4-4B-002/regression/stderr-v2.txt
```

Expected result: exit 0 with all collected tests passing. Preserve stdout, stderr, exit status, count, and hashes. Any nonzero exit, failed test, missing artifact, changed protected state, or unavailable approved environment is STOP AND PRESERVE without retry.
