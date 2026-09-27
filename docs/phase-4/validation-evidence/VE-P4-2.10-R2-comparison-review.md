# VE-P4-2.10 R2 v2 comparison review

**Overall classification:** **PASS**

All runs executed from clean Lane A baseline
`cc8e866a0985809eeab16cb67866bde55c1b2128` on `phase4-item-2.10-r2`.
Preflight passed for each: committed v2 controls and R1 v2 PASS lineage,
absence of prior R2 evidence, historical/current F3 provenance, six controlled
F3 input hashes, no later F3 semantic revision, and unchanged R2 matrix.
Each used a separate process, workspace, and private SQLite state.

| Run | Perturbation | Individual ER-F3 / ER-R2-v2 / SC-v2 | Semantic comparison to REF |
| --- | --- | --- | --- |
| R2-REF | Normal presentation/mapping; seed 101 | PASS | Reference |
| R2-H | Seed 907 | PASS | Equal |
| R2-P | Observation presentation: depot, canvas, tote, sealed | PASS | Equal |
| R2-M | Mapping insertion: depot, tote, sealed, canvas | PASS | Equal |

The complete semantic projections are equal. The comparison separately verifies:

| Independent domain | Equal frozen result in REF, H, P, and M |
| --- | --- |
| Candidate; applicability/selection traversal | CANVAS-HISTORY, DEPOT-UNVERIFIED, SEALED, TOTE |
| Selected Context / logical package | CANVAS-HISTORY Supporting; DEPOT-UNVERIFIED Supporting; SEALED Required; TOTE Required |
| Source Manifest | COMPETING, CURRENT, HISTORY, QUALIFICATION |
| Human, ChatGPT, Codex rendering | Required SEALED, TOTE; Supporting CANVAS-HISTORY, DEPOT-UNVERIFIED |

All four preserve represented identities and lineage, Authority/Governance
State, current/historical/unverified qualifications, unresolved
`CON-F3-CASE-CHOICE`, `UNC-F3-DEPOT`, ASU basis, `insufficient`,
`coherent_with_qualification`, and the package/rendering/delivery/receipt/use
boundary. No order domain was normalized by another.

For R2-P, the preserved initial projection records the intended change to the
unordered ASU Source presentation collection. The final semantic comparison
sorts only that identity-membership collection; it does not sort Candidate,
traversal/package, Manifest, or renderer orders. The raw result and initial
derivation are retained.

Negative criteria PASS: no hash/set/dictionary iteration, presentation order,
mapping insertion order, row ID, frequency/count, generic recency/newer-wins,
numeric score/rank/weight, timestamp, or other incidental value entered a
semantic ranking basis. Currentness remained a governed F3 semantic input.

The frozen design conclusions remain unchanged: filesystem enumeration is not
applicable to this named-locator F3 path; no safe F3 SQLite insertion-order or
distinct frequency perturbation exists without manufacturing a new path.

Unchanged regression suite: **105 passed**.
