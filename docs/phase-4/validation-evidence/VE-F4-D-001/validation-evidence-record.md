# VE-F4-D-001 — FX-F4-D v1 Validation Evidence Record

**Result state:** **PASS**  
**Disposition:** Frozen `ER-F4-D v1` satisfied; no finding and no remediation.

| Field | Record value |
| --- | --- |
| Execution baseline | Clean pre-execution `HEAD` `922131ccafd0b8c541b29bb0031d9e517bb0ea51` (`922131c` — *Preserve Phase 4 construction qualifications*). `9862497` and the committed F4-E remediation lineage are ancestors. |
| F4-E baseline verification | Immutable `VE-F4-E-001` remains **FAIL**; `F-F4-E-001` retains **MATERIAL / INTEGRATION** and is **CLOSED**; `R-F4-E-001` remains traceable; `VE-F4-E-002` remains **PASS**. |
| Scope | Only frozen synthetic `FX-F4-D v1` against frozen `ER-F4-D v1`; no production Authority. No F4-C, F5, proving, Consumer preflight, Gate 4B action, TD-14 action, remediation, or application/source change occurred. |
| Fixture / ER provenance | The F4-D fixture records and `ER-F4-D v1` originate at `c7d17714a3983335f8564aa9360739d9ec785410`; subsequent fixture-register history contains no later `ER-F4-D` revision. `FX-F4-D` and `ER-F4-D` remained unchanged at execution. |
| Controlled inputs | `F4-D/bootstrap.toml` `1de419e408a20311c0560aeb252e69b1e70af745e3c473e7e655b0b20284e040`; `project.toml` `65aee1971e72b7a095b0a21749a256c2f36096173cae34a694e84b6181925893`; `sources/release-decision.md` `8ed3fa3e923d2d385e7ac4c878f6097fa93ed84e7f83351409e04998bc92bcdf`; governing fixture record `23520e1cd7997668bad33ca3eb595db8600865c288a4e81acdd858481fe17f86`; ER register `6538707ee1b5b765defa7dadaddc6ab431abde02586f69508d607d98f021773d`. The raw [controlled-input manifest](raw/controlled-input-sha256.txt) is `df31ae0c13f2188714576aa3a00f1cd45b6967bd102e822272bb4f6e6175fbe8`. |
| Runtime | Local network-free CPython 3.14, markdown-it-py 3.0.0, Git, Linux. |
| Regression | Full existing suite in the established validation environment: **105 passed**. |
| Procedure | Successful existing CLI Bootstrap validation followed by [execution-only orchestration](raw/f4-d-execution.py) through existing Bootstrap/configuration, observation, transformation, discovery, applicability, Required determination, selection, sufficiency, construction/persistence, and rendering interfaces. Initial malformed CLI invocations are retained as non-semantic procedure diagnostics; they did not enter the pipeline. |
| Capacity | Exactly `1` character for Human, ChatGPT, and Codex, with no approved condensation, external reference, multipart continuation, waiver, or lossy fallback. |
| Package identity / derivative | `PKG-F4-D-001`; canonical derived [logical package](derived/logical-package.json) SHA-256 `358c6ac9584c282df35a7fb183109df3ebe9c950174f9a941b5b525bb31730fa`. |
| Raw evidence | [Raw artifacts](raw/) and [raw/derived SHA-256 manifest](derived/raw-artifact-sha256.md). Evaluator: Codex. |

## Observed pipeline and rendering result

`RI-F4-REQUIRED-DECISION` was observed, represented with direct and normalized Source/artifact/observation/transformation Provenance, became a Candidate, was applicable, remained **Required**, and was selected. The controlled ASU is `adequate`; no material Conflict or Uncertainty is present. The logical package is **Sufficient** and Construction-State Coherence is **coherent**. The capacity limitation is present in Required-selection reason evidence (`consumer-capacity-does-not-waive-required`) and does not alter package semantics.

Human, ChatGPT, and Codex each used the exact declared capacity of one character. Each returned `failed`, no `ConsumerRendering` reference, no content payload, and `rendering-capacity-insufficient-required-context-not-omitted`. Their preserved rendering files are zero-byte payload artifacts. The audit preserves `rendering-failed`; it contains no delivery, receipt, or use assertion.

| ER-F4-D criteria | Evaluation |
| --- | --- |
| 1–9 | **PASS** — Required Context is observed, represented, Candidate, applicable, Required, selected; ASU is adequate; logical package is Sufficient and coherent. |
| 10 | **PASS** — capacity does not mutate selection, package identity, contents, sufficiency, or coherence. |
| 11–16 | **PASS** — Human, ChatGPT, and Codex each explicitly fail and each has no payload/reference. |
| 17–19 | **PASS** — no truncation, silent omission, or Required-to-Supporting downgrade. |
| 20–21 | **PASS** — rendering failure remains distinct from package insufficiency, and no delivery/receipt/use assertion exists. |

No frozen negative criterion was observed. This evidence is directly relevant to future WS2 Item 2.9 disposition, but does **not** complete, PASS, or review Item 2.9.
