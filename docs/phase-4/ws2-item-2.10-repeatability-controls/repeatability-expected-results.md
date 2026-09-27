# Item 2.10 Additive Expected Results and Semantic Contract

**Record status:** Pre-results only. These records are additive to, and do not
reuse the identity of, `ER-F3 v1`. They are frozen before any R1/R2 execution.
They inherit the approved Phase 0–3 baseline, Phase 4 checklist, validation
governance package, and approved Item 2.10 analysis.

## F3 input inventory and hash control

Every R1/R2 run must first verify this exact inventory. A mismatch is a
controlled-input failure, not an allowed variation.

| SHA-256 | Frozen input |
| --- | --- |
| `1c27f2dd2eb882adadcd2a5ea3f7cc9ec6a223348d49662e51d710a52a180a46` | `F3/bootstrap.toml` |
| `6d6982c01382108a970b60830f0d65fa4edf35cc32bee758f16005f613b668be` | `F3/project.toml` |
| `afcb9ebb82eca7b9842078f8f8891c9d2fd912b7e28bebcd9745d31d9717b7c0` | `F3/sources/competing-decision.md` |
| `c22ea350f759e63c0315a2d6c4a370498449e7a2f30e16cf33c2e8b7b8f1a776` | `F3/sources/current-decision.md` |
| `e4c12c53455c16b11d2a723104d65310f142450ec82d20f6005107b90ac73008` | `F3/sources/historical-note.md` |
| `fc90e05050be6c023c8214b7acdb28dddc56033d5c7171f5eb68895d9b0af9d2` | `F3/sources/qualification.md` |
| `ddc68a86d135c4927e519d1c037b2d4cdad8e91c4b89516b8ef7c879ace7c794` | `fixture-records.md` (`FX-F3 v1` record) |
| `a8aa072209f6d0b2515ababadcd51bb787bec470b82f04e6c8b0d834016a2600` | `expected-results.md` (`ER-F3 v1` register) |

The controlled request is `REQ-F3-RELEASE-RECOMMENDATION`, Project is
`fixture-atlas-f3`, and scope is `field-kit-release`. The four Sources,
represented-information identities, artifact/observation/provenance identities,
and F3 governed metadata remain exactly those established by `FX-F3 v1`.

## Shared semantic-comparison contract `SC-P4-2.10 v1`

### Comparison rule

For each run, derive a reviewable semantic projection from the preserved raw
result, logical package/construction record, and all three rendering payloads.
Compare that projection to unchanged `ER-F3 v1` and, where required, to the
predesignated peer/reference projection. Equality means every field in the
following table is equal in the stated semantic order. No omitted, reordered,
substituted, or newly introduced governed value is equal.

| Required semantic projection | Required comparison |
| --- | --- |
| Request/task and scope | identity, intent, Project, governed scope |
| Sources and artifacts | Source identities/states; applicable artifact identities/versions |
| Observation and representation | observation identities/material states; represented-information identities |
| Lineage | complete Provenance paths and location/transformation references |
| Discovery | Candidate identities in semantic order; discovery reasons/basis |
| Applicability | outcome and reasons for every Candidate |
| Selection | Required/Supporting roles, selected identities/order, exclusions/reasons |
| Qualification | Conflict identity/participants/state; Uncertainty identity/state; current/historical/currentness qualification |
| ASU and deficiencies | ASU state/establishment basis; Required deficiencies; sufficiency state |
| Construction | coherence outcome/basis; logical-package identity semantics, membership, canonical item order |
| Source Manifest | membership and governed order |
| Limits | material limitations and qualifications |
| Renderings | Human, ChatGPT, and Codex material semantic content and semantic item order |
| Boundary | package != rendering != delivery != receipt != use; no delivery/receipt/use assertion |

The expected F3 order is the established canonical semantic order from the
result: `RI-F3-SEALED`, `RI-F3-TOTE`, `RI-F3-CANVAS-HISTORY`,
`RI-F3-DEPOT-UNVERIFIED`; Required order is sealed then tote; Supporting order
is canvas history then depot. The Source Manifest's governed identity order is
the order preserved by the package (`SRC-F3-COMPETING`, `SRC-F3-CURRENT`,
`SRC-F3-HISTORY`, `SRC-F3-QUALIFICATION`).

### Prohibited normalization

The comparison must not normalize Source identity/state, represented
information, Provenance, Candidate identity/order, applicability, role,
selection, selected order, exclusion reason, Conflict, Uncertainty,
current/historical qualification, ASU state/basis, Required deficiency,
sufficiency, coherence, package membership/order, Source Manifest order,
material limitation/qualification, or renderer material content/order. A
mismatch in any such value remains observable and prevents PASS.

### Narrow non-semantic allowlist

The following may differ only when the recorded artifact demonstrates the
stated non-semantic basis: execution/evidence/audit timestamp (run recording
only); isolated temporary workspace/path; run/evidence identity; process ID;
platform/runtime metadata not consumed by semantics; SQLite physical bytes and
private row IDs not exposed by the semantic projection; hashes changed only by
those volatile fields; and insignificant renderer whitespace outside the parsed
material payload/order. This is not an automatic waiver. Any other difference,
or a claimed field whose non-semantic basis is not demonstrated, is a mismatch.

Byte equality is therefore supporting only. Future evidence may report
byte-identical stable derivatives after run-specific metadata is excluded, but
neither matching nor nonmatching bytes determine Item 2.10 PASS.

## `ER-P4-2.10-R1 v1`

| Field | Frozen value |
| --- | --- |
| Control / relationship | `RC-P4-2.10-R1 v1`; deliberately exercises 2.10-A and 2.10-B, and applies the shared 2.10-I semantic-stability contract. |
| Governed expectation | Three independent isolated executions with the F3 hashes/inventory, Bootstrap/configuration semantics, request, Sources, artifacts, Consumer contracts, approved application baseline, and this ER version unchanged. |
| Acceptance | Each run individually satisfies unchanged `ER-F3 v1`; each matches `SC-P4-2.10 v1`; and all three projections are mutually semantically equal, including established order and all F3 qualifications. |
| Required preservation | Two current Required conflict participants remain unresolved; historical Supporting and unverified Supporting Context remain qualified; Insufficient and `coherent_with_qualification` remain; all renderers remain materially faithful and make no delivery/receipt/use assertion. |
| Failure | Any input-hash failure, state contamination, F3 failure, semantic mismatch, order change, lost qualification, or only-two-of-three agreement is not PASS. |
| Evidence placeholder | Future run evidence only: `VE-P4-2.10-R1-001` through `-003`, plus a derived comparison record. |

## `ER-P4-2.10-R2 v1`

| Field | Frozen value |
| --- | --- |
| Control / relationship | `RC-P4-2.10-R2 v1`; deliberately exercises 2.10-D, 2.10-G, and 2.10-H through the supported perturbations/negative criteria, corroborates 2.10-B, and applies the shared 2.10-I semantic-stability contract. |
| Designated reference | `R2-REF` is the first future R2 execution: unperturbed F3 presentation/mapping order with `PYTHONHASHSEED=101`. It is designated now, never selected after results. |
| Governed expectation | Every supported perturbation run verifies the F3 hashes, individually satisfies `ER-F3 v1`, and equals `R2-REF` under `SC-P4-2.10 v1`. |
| Negative criteria | No order/recency/frequency/row-ID/score/count/timestamp mechanism may select, omit, reorder, or resolve Context. No run changes governed F3 input, Authority, authorization, relationship, currentness assessment, Conflict, Uncertainty, ASU semantics, role, or expected result. |
| Evidence placeholder | Future run evidence only: `VE-P4-2.10-R2-REF`, `-H`, `-P`, and `-M`, plus a derived comparison record. |

## Obligation mapping and future evidence disposition

**FUTURE EVIDENCE CLASSIFICATION IS NOT PREDETERMINED.** PASS, FAIL, or
INDETERMINATE applies to each future control execution. DIRECT, SUPPORTING,
NOT-YET, or accepted-limitation classification is a separate, bounded
post-results governance disposition based on what preserved evidence actually
proves. It is not determined by this pre-results control design.

If faithful execution satisfies the frozen criteria and the cross-run semantic
equality contract, 2.10-A and 2.10-B are eligible for DIRECT validation. If
faithful R2 execution demonstrates the frozen hash/set/dictionary/order
independence obligation, 2.10-D is eligible for DIRECT validation. If it
preserves F3's governed current/historical/conflict semantics and demonstrates
the no-newer-wins criterion, 2.10-G is eligible for DIRECT validation. If
preserved R2 evidence directly demonstrates that no score, count, timestamp,
or incidental value becomes a semantic-ranking basis, 2.10-H is eligible for
DIRECT validation. If R1/R2 evidence demonstrates semantic stability while
permitted non-semantic fields vary, 2.10-I is eligible for DIRECT validation.

For 2.10-C, 2.10-E, and 2.10-F, this design neither automatically classifies
the obligation DIRECT nor creates an accepted limitation. Their eventual
evidence classification and Item 2.10 closure treatment require a bounded
post-results coverage/disposition review of the approved architecture
prohibition, implementation/interface evidence, applicability or
non-applicability, R1/R2 integrated semantic evidence, and whether the Item
2.10 completion standard requires separate executable perturbation evidence.

| Obligation | Frozen coverage basis |
| --- | --- |
| 2.10-A | R1 deliberately exercises three individually F3-faithful and cross-run equal projections; eligible for DIRECT validation only after faithful execution and post-results disposition. |
| 2.10-B | R1 deliberately exercises canonical order; R2 corroborates it. Eligible for DIRECT validation only after faithful execution and post-results disposition. |
| 2.10-C | F3 path filesystem perturbation is not applicable; preserve the explicit negative criterion that filesystem order cannot be semantic rank. No artificial path is permitted. Future classification is deferred. |
| 2.10-D | R2-H fixed `PYTHONHASHSEED` variation, R2-P presentation permutation, and R2-M mapping insertion-order permutation deliberately exercise the obligation; eligible for DIRECT validation only after faithful execution and post-results disposition. |
| 2.10-E | No safe F3 SQLite insertion-order perturbation exists: the single F3 construction write cannot be permuted without adding a path. Preserve row-ID prohibition and require the projection not to expose row IDs. Future classification is deferred. |
| 2.10-F | No safe distinct frequency perturbation exists under F3 semantics; preserve the architecture prohibition, absence of frequency ranking, and R1/R2 no-ranking inspection. Future classification is deferred. |
| 2.10-G | R2 deliberately preserves the unresolved current conflict, historical Supporting item, and no-newer-wins criterion; eligible for DIRECT validation only after faithful execution and post-results disposition. |
| 2.10-H | R2 deliberately exercises the frozen no-unapproved-score/count/timestamp/incidental-value criterion; eligible for DIRECT validation only after faithful execution and post-results disposition. |
| 2.10-I | `SC-P4-2.10 v1` deliberately exercises semantic stability across both controls; eligible for DIRECT validation only after faithful execution and post-results disposition. Byte identity remains supporting only. |

If later review finds a genuine uncovered governing obligation, execution must
stop and the gap must be reported under H3 rather than filled with static
evidence.
