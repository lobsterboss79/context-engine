# WS2 Item 2.6 — Additive Residual-Control Fixture Records

**Register status:** Pre-execution. This register is separate from the
historical F1–F5 family in `ws2-item-2.1-fixtures/`; it records post-authorization
residual controls only. `FX-F6-D v1` is governed for separately authorized
execution, not executed, and has no PASS, FAIL, or INDETERMINATE execution
result. It does not validate Item 2.6-D, complete Item 2.6, approve Gate 4B,
authorize proving, reopen TD-14, or establish production readiness.

## FX-F6-D v1 — Indeterminate ASU

| Field | Frozen value |
| --- | --- |
| Fixture ID / purpose | `FX-F6-D v1`. A synthetic, separately attributable control for **WS2 Item 2.6-D — Indeterminate ASU**. It exercises the approved indeterminate evidence-boundary condition, not an unavailable, inaccessible, unauthorized, unsupported, or known-incomplete Source condition. |
| Synthetic Project / task | Local synthetic Project `fixture-atlas-f6d`; `REQ-F6D-ATLAS-DEPLOYMENT-RECOMMENDATION`: prepare an unqualified deployment recommendation for the complete unbounded Atlas field-operations plan. No safe bounded subtask is supplied. |
| Exact controlled artifacts | `F6-D/bootstrap.toml`; `F6-D/project.toml`; `F6-D/controlled-request.toml`; `F6-D/sources/field-operations-note.md`. The controlled-input hashes are frozen in the preparation record. |
| Known Source / scope | `SRC-F6D-FIELD-OPERATIONS-NOTE`, local Markdown Source at `sources/field-operations-note.md`, governed scope `atlas/field-operations/current-plan`. It is available, accessible, requester-authorized, supported, and in the known governed scope. Normal local Markdown observation is expected. |
| ASU identity / establishment basis | `ASU-F6D-ATLAS-DEPLOYMENT`; `BoundaryAdequacy = indeterminate`. Its explicit nonempty basis identifies the known inspected local boundary and available governed boundary/inventory evidence, while stating that those facts cannot reliably establish whether an additional Source or Source scope could be applicable to the complete unbounded task. No particular omitted material Source, scope, or relationship is known or asserted. |
| Expected observation / representation / Provenance | Observe the known Source normally; represent its staging and scheduled safety-review information as task-relevant, provenance-bearing information with identity, scope, and Source lineage preserved. Do not infer a complete evidence universe from successful observation. |
| Candidate, applicability, role, and selection | Under the frozen task mapping, the represented information becomes Candidate Context, is applicable as Supporting Context, and is selected as known useful Context. Candidate/applicability/selection do not establish ASU adequacy or complete sufficiency. |
| Expected ASU / sufficiency / coherence | `indeterminate`; **Insufficient** for this unbounded task; `coherent_with_qualification`. This fixture-specific Insufficient result follows from unqualified sufficiency requiring adequate ASU and from there being no separately supplied safe bounded task. It is not a universal rule about every indeterminate ASU. |
| Expected logical package | A logical package is expected: selected known Context; Source Manifest and Provenance for observed material; ASU identity and nonempty basis; `indeterminate`; Insufficient; `coherent_with_qualification`; and the explicit limitation that adequacy of the governed evidence boundary could not be established for the full task. It must not claim complete inspection, universal absence, a particular missing Source/scope/relationship, adequate ASU, known-incomplete ASU, or unqualified sufficiency. |
| Expected renderings | Human, ChatGPT, and Codex renderings faithfully preserve the known selected Context, Provenance, ASU identity/basis and `indeterminate` state, Insufficient sufficiency, coherence qualification, and the evidence-boundary limitation. In substance: the known governed Source was inspected and provides the stated Context, but adequacy/completeness of the evidence boundary for the full task could not be established. Renderings remain distinct from the logical package and assert no delivery, receipt, or use. |
| Authorization / governing references | Project Owner authorization: `ws2-item-2.6-residual-control-authorization-disposition.md` §3 and §12. Design: `ws2-item-2.6-residual-gap-design-analysis.md` §4. Semantics: Phase 1 conceptual model ASU; Phase 2 C5/E12 and Domain E sufficiency; Phase 3 WS4, WS6, WS8, and WS9; Phase 4 checklist Item 2.6 and WS1 controls. |
| Known limitations / pre-results status | The control does not establish that no other Source exists, and does not invent one. It is pre-results only: no execution, evidence, finding, remediation, result classification, Item 2.6 completion, or production authority is assigned. |
