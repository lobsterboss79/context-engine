# VE-P4-2.10-R1V2-002 — R1 v2 identical-input repeatability execution

**Result state:** **PASS**

`R1V2-02` executed from the clean committed baseline
`1b8fe6e230e90e7d93b695831b19dc5c4a21a5ee` under `FX-F3 v1`,
`ER-F3 v1`, `RC-P4-2.10-R1 v2`, `ER-P4-2.10-R1 v2`, and
`SC-P4-2.10 v2`.

The required historical/current provenance checks and all six frozen F3 hashes
passed before execution. A new process, v2-specific workspace, and private
SQLite state were used; no prior-run state, artifact, package, rendering,
audit, or semantically influential cache was inherited. R2 perturbations were
inactive.

Independent ER/SC assessment passed all semantic criteria. Candidate and
selection/package order are CANVAS-HISTORY, DEPOT-UNVERIFIED, SEALED, TOTE;
the Source Manifest is COMPETING, CURRENT, HISTORY, QUALIFICATION; and every
renderer presents Required SEALED, TOTE then Supporting CANVAS-HISTORY,
DEPOT-UNVERIFIED. The unresolved conflict, depot uncertainty, Provenance,
roles, current/historical qualification, ASU basis, insufficiency,
`coherent_with_qualification`, and no delivery/receipt/use assertion remain
preserved.

The semantic projection is exactly equal to R1V2-01. Preserved artifacts
include procedure, stdout/stderr, raw result, private SQLite state, three
renderings, semantic assessment/projection, and SHA-256 manifests.

This is the second passing run only; overall R1 v2 classification remains
pending R1V2-03.
