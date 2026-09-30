# VE-P4-4B-002 Focused Regression Preflight v3

**Status:** COMPLETE BEFORE V3 INVOCATION.

The Project Owner authorized only the designated test temporary root. Codex successfully created, verified, and deleted `/home/lobsterboss79/temp/context-engine-ws4-codex-write-probe`; its command exited 0. No regression ran before this record.

| Check | Observed result |
| --- | --- |
| Branch / HEAD | `phase4-ws4-persistence-linux` / `c221e4e77d99f54fb617cc762ab4efb2b6f90f24` |
| Baseline ancestry | `git merge-base --is-ancestor 636afcf HEAD` exit 0 |
| Interpreter | `/home/lobsterboss79/temp/context-engine-ws2-validation.qNq9B4/bin/python`, executable |
| Python / pytest | CPython 3.14.4 / pytest 9.1.1, successful imports |
| Source/tests | `git diff --quiet 636afcf HEAD -- src tests` exit 0 |
| Shared material | frozen shared-file comparison to `636afcf` exit 0 |
| Semantic evidence | predecessor/successor/migration result hashes below; no semantic invocation is included |

```text
2aadbcfa4d89337633f200b04a79f39202585d4e21dcf738b954083c8bf6d0a4  tests/test_workstream_3.py
158b9ef1943f03a755edf0a26fb71d537b07a212da5c6295ad3ad86e9b08ca75  tests/test_workstream_4.py
a8cd8bf5c40032012bf684f41cc3b3e618f4d097d610ed5fd8aa1d49cf644e13  tests/test_workstream_8.py
1265bcfcecfa532b711dbb112a5175ccd333b1226c0c10f43dfc1af6df2465a8  tests/test_workstream_10.py
d2e3f4a32744df2bb1c35014e7bb0f8cbfa8f52b96f45e1a962e36ef986002c9  ../preflight.md
5a332e69a38f1492908a734973fee728b5045a873582f9c7b4a4fcf5d3a18fec  ../raw/state/result.json
c6462d0868ff988c5d198676ed1855e1ac47c61c5e0d67e3e73672963aca239d  ../../VE-P4-4B-002-S1/raw/state/result.json
e8865f18012c0ef3e9c0ef511c34529a66c00599e7100b5ac6893688bdd28c6a  ../../VE-P4-4B-002-M1/raw/state/result.json
41705a3c937b89d205e6df8e4b66960c4de065a31341880d21bc1c4e76771baf  procedure-v3.md
```

Frozen invocation:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src /home/lobsterboss79/temp/context-engine-ws2-validation.qNq9B4/bin/python -m pytest -p no:cacheprovider tests/test_workstream_3.py tests/test_workstream_4.py tests/test_workstream_8.py tests/test_workstream_10.py > docs/phase-4/validation-evidence/VE-P4-4B-002/regression/stdout-v3.txt 2> docs/phase-4/validation-evidence/VE-P4-4B-002/regression/stderr-v3.txt
```

Expected result is exit 0 with all four frozen slices passing. Preserve stdout/stderr and a result record. Nonzero exit, setup/environment error, assertion failure, missing artifact, or protected-state change is STOP AND PRESERVE without retry.
