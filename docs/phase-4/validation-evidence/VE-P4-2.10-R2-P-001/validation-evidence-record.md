# VE-P4-2.10-R2-P-001 — R2 v2 observation-presentation perturbation

**Result state:** **PASS**

| Field | Record value |
| --- | --- |
| Run / baseline | `R2-P`; clean Lane A baseline `cc8e866a0985809eeab16cb67866bde55c1b2128` (`phase4-item-2.10-r2`). |
| Controls | `FX-F3 v1`; unchanged `ER-F3 v1`; `RC-P4-2.10-R2 v2`; `ER-P4-2.10-R2 v2`; `SC-P4-2.10 v2`. |
| Preflight | PASS: six controlled F3 hashes and historical/current provenance checks matched; no later F3 semantic revision or R2-control change was present. |
| Procedure / isolation | Fresh process with `PYTHONHASHSEED=101`; the same four observations were presented only in frozen depot, canvas-history, tote, sealed order; new evidence workspace and private SQLite state. |
| ER/SC and reference comparison | PASS: individual frozen-control assessment passed; the complete semantic projection equals R2-REF. Candidate/traversal/package, Manifest, and each renderer order remain independently equal. |
| Presentation-only record | The initial derived projection preserving input presentation order is retained as `derived/semantic-projection-initial-presentation-order.json`. Its sole difference was unordered ASU Source collection order; Source identity/state membership was equal. The final comparison canonicalizes that collection by Source identity only; it does not normalize any SC v2 order domain. |
| Negative result | No presentation order selected, omitted, reordered within a governed domain, or resolved Context. |
| Artifacts | Raw procedure/result/stdout/stderr, private SQLite, three renderings, semantic projection/assessment, and SHA-256 manifests are preserved here. |
