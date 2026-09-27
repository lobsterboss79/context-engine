# VE-P4-2.10-R1V2-003 — R1 v2 identical-input repeatability execution

**Result state:** **PASS**

`R1V2-03` executed from clean committed baseline
`1b8fe6e230e90e7d93b695831b19dc5c4a21a5ee` under the frozen F3 inputs,
`ER-F3 v1`, and R1/SC v2 controls. Historical/current provenance and all six
F3 input hashes passed. The run used its own fresh process, workspace, audit,
generated artifacts, and private SQLite state; R2 perturbations were inactive.

Independent ER/SC assessment passed: all four identities, Candidates,
applicability/selection, Provenance, roles, unresolved Conflict, Uncertainty,
current/history distinction, ASU basis, insufficiency,
`coherent_with_qualification`, package/rendering/delivery/receipt/use
boundary, and three renderer payloads were preserved.

The independent orders passed: Candidate/selection/package
CANVAS-HISTORY, DEPOT-UNVERIFIED, SEALED, TOTE; Manifest COMPETING, CURRENT,
HISTORY, QUALIFICATION; renderer Required SEALED, TOTE and Supporting
CANVAS-HISTORY, DEPOT-UNVERIFIED. Its projection equals both R1V2-01 and
R1V2-02.

Raw procedure, stdout/stderr, result, SQLite state, renderings, projection,
assessment, and SHA-256 manifests are preserved in this directory.
