# VE-P4-2.10-R2-H-001 — R2 v2 hash-seed perturbation

**Result state:** **PASS**

| Field | Record value |
| --- | --- |
| Run / baseline | `R2-H`; clean Lane A baseline `cc8e866a0985809eeab16cb67866bde55c1b2128` (`phase4-item-2.10-r2`). |
| Controls | `FX-F3 v1`; unchanged `ER-F3 v1`; `RC-P4-2.10-R2 v2`; `ER-P4-2.10-R2 v2`; `SC-P4-2.10 v2`. |
| Preflight | PASS: six controlled F3 hashes and historical/current provenance checks matched; no later F3 semantic revision or R2-control change was present. |
| Procedure / isolation | Fresh process with the frozen alternate `PYTHONHASHSEED=907`; otherwise R2 reference procedure, with a new evidence workspace and private SQLite state. |
| ER/SC and reference comparison | PASS: individual frozen-control assessment passed; the complete semantic projection equals R2-REF. No governed field or independent order domain changed. |
| Negative result | No hash/set/dictionary iteration basis selected, omitted, reordered, or resolved Context; currentness was preserved rather than treated as generic recency. |
| Artifacts | Raw procedure/result/stdout/stderr, private SQLite, three renderings, semantic projection/assessment, and SHA-256 manifests are preserved here. |
