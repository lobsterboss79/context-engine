# VE-P4-2.10 R1 v2 comparison review

**Overall classification:** **PASS**

| Run | Individual ER-F3 / ER-R1-v2 / SC-v2 result | Isolation | Projection |
| --- | --- | --- | --- |
| R1V2-01 | PASS | PASS | baseline projection |
| R1V2-02 | PASS | PASS | equal to 01 |
| R1V2-03 | PASS | PASS | equal to 01 and 02 |

Each run used the clean committed baseline
`1b8fe6e230e90e7d93b695831b19dc5c4a21a5ee`, matched the historical and
current F3 provenance checks and six frozen F3 hashes, and had fresh process,
SQLite, evidence/output, audit, package, rendering, and cache state. No R2
perturbation was active.

Every independently governed order domain is equal across all three runs:

| Domain | Result |
| --- | --- |
| Candidate; applicability/selection traversal; selected/package | CANVAS-HISTORY, DEPOT-UNVERIFIED, SEALED, TOTE |
| Source Manifest | COMPETING, CURRENT, HISTORY, QUALIFICATION |
| Human, ChatGPT, Codex renderer presentation | Required SEALED, TOTE; Supporting CANVAS-HISTORY, DEPOT-UNVERIFIED |

All projections preserve four F3 identities, roles, Provenance,
current/historical distinctions, unresolved `CON-F3-CASE-CHOICE`,
`UNC-F3-DEPOT`, ASU basis, Required deficiency, `insufficient`,
`coherent_with_qualification`, qualifications, membership, and the
package/rendering/delivery/receipt/use boundary. No mismatch was normalized.

Permitted raw-only differences are run/evidence identifiers, timestamps,
isolated paths, process/runtime metadata, private SQLite physical bytes/row
IDs, and hashes that follow exclusively from them. The semantic projections
exclude those demonstrably non-semantic values and are byte-identical; raw-byte
identity was not used as the acceptance criterion.

Historical `VE-P4-2.10-R1-001` remains immutable **FAIL against v1**. This
review does not reinterpret it, execute R2, complete Item 2.10, close the
finding, approve Gate 4B, authorize proving, reopen TD-14, or establish
production readiness.
