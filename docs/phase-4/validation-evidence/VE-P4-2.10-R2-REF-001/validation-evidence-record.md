# VE-P4-2.10-R2-REF-001 — R2 v2 reference execution

**Result state:** **PASS**

| Field | Record value |
| --- | --- |
| Run / baseline | `R2-REF`; clean Lane A baseline `cc8e866a0985809eeab16cb67866bde55c1b2128` (`phase4-item-2.10-r2`). |
| Controls | `FX-F3 v1`; unchanged `ER-F3 v1`; `RC-P4-2.10-R2 v2`; `ER-P4-2.10-R2 v2`; `SC-P4-2.10 v2`. |
| Preflight | PASS: clean branch/worktree; v2 control and R1 v2 PASS lineage committed; no R2 evidence before execution; historical/current provenance checks and all six controlled-file hashes matched; no later F3 semantic revision; R2 matrix unchanged. |
| Procedure / isolation | Fresh process with `PYTHONHASHSEED=101`, normal F3 observation presentation and mapping construction; new evidence workspace and private SQLite state. |
| ER/SC assessment | PASS: all F3 identities, qualifications, Provenance, unresolved Conflict, Uncertainty, ASU basis, insufficiency, coherence, package/rendering boundary, and independent order domains match the frozen controls. |
| Artifacts | Raw procedure/result/stdout/stderr, private SQLite, three renderings, semantic projection/assessment, and SHA-256 manifests are preserved here. |

This predesignated reference is not selected from observed results. It is the
comparison baseline for the three separately preserved R2 perturbation runs.
