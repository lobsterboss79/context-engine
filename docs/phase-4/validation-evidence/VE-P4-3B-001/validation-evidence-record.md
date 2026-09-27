# VE-P4-3B-001 — ER-P4-3B-001 v1 Validation Evidence Record

**Result state:** **INDETERMINATE — STOP AND PRESERVE**  
**Disposition:** No PASS classification, coverage review, proposed PASS
disposition, rerun, control revision, remediation, Finding disposition, Item
3.9 work, or shared-file change occurred.

| Field | Preserved record |
| --- | --- |
| Execution branch / baseline | `phase4-ws3-trust-state-audit`; `a06e4da5647df26db4ebe886f7bdfd0a95e00767` (`a06e4da`) |
| Execution time | 2026-09-27 America/Chicago local session |
| Control / expected result | Frozen `ER-P4-3B-001 v1`; [preflight](preflight.md) records its pre-execution hash `4496ac47c23fbec8161dfc63c90dae19f7eac897e4682e89211e53ae56abce24` and runner hash `94d1b0b29fdcacbd3f7199658ae03f6ec6863faf7bfda31f45402c051c22f06c`. |
| Environment | Local network-free CPython 3 execution with `PYTHONPATH=src`; existing repository interfaces only. |
| Exact procedure | `test ! -e docs/phase-4/validation-evidence/VE-P4-3B-001/raw && mkdir -p docs/phase-4/validation-evidence/VE-P4-3B-001/raw && PYTHONPATH=src python3 docs/phase-4/ws3-lane-b-trust-state-audit/control-runner.py docs/phase-4/validation-evidence/VE-P4-3B-001/raw > docs/phase-4/validation-evidence/VE-P4-3B-001/raw/stdout.txt 2> docs/phase-4/validation-evidence/VE-P4-3B-001/raw/stderr.txt` |
| Process outcome | Exit code `0`. The runner's preserved `raw/result.json` reports all frozen B1–B4 assertions and `"result": "PASS"`. This is not sufficient for a validation PASS. |
| Retained raw artifacts | `source.sqlite`, `backup.sqlite`, `restored.sqlite`, and `result.json` exist in [raw](raw/). Their SHA-256 values are listed below. |
| Missing required artifacts | `raw/stdout.txt` and `raw/stderr.txt` do **not** exist after execution. A post-run read confirmed their absence. |
| Cause evidenced by procedure/runner | The shell opened the two redirection paths before process start. The frozen runner receives the already-existing `raw` directory and begins with `shutil.rmtree(output)`, unlinking those paths, then recreates the directory. The process's output descriptors remained usable but no directory entries remained for preservation. |
| Governing classification | WS3 execution contract requires raw stdout/stderr for each deliberate execution as applicable. The ER also makes missing preserved artifacts a non-PASS stop condition. Available evidence is therefore insufficient to establish PASS even though its surviving result artifact reports passing assertions: **INDETERMINATE** under WS1 §1.5. |
| Finding / H3 | No product/security semantic discrepancy is demonstrated. No Finding severity/disposition or H3 conclusion is made; evaluation stops at the evidence-integrity boundary. |

## Retained-artifact SHA-256 manifest

| Artifact | SHA-256 |
| --- | --- |
| `raw/backup.sqlite` | `77c3d59caa8c1976e1e410a11be8c50f215e68b034a8901ac04b47136159b6c0` |
| `raw/restored.sqlite` | `af356d9c91043b96c64879e0161842c6fcb347bffc9f3411d9e64c4ed8c32aee` |
| `raw/result.json` | `5b873563096e3d3e099ffd6834399b327605b491030d8436019cd8253b21baf4` |
| `raw/source.sqlite` | `1de898b0595a04f6121a8fa195f14ca03d2cf86dc836e5bbbbb3504f5723501b` |
| `ER-P4-3B-001.md` | `4496ac47c23fbec8161dfc63c90dae19f7eac897e4682e89211e53ae56abce24` |
| `control-runner.py` | `94d1b0b29fdcacbd3f7199658ae03f6ec6863faf7bfda31f45402c051c22f06c` |

## Stop boundary

This is preserved as a historical INDETERMINATE evidence lineage. The frozen
ER and runner are not altered. Any future control correction, successor
expected-result control, rerun, protocol disposition, or finding decision
requires the applicable governed authority; none is authorized by this record.
