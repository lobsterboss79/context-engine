# Phase 3 Workstream 9 — Consumer Rendering and Application/CLI Orchestration

**Status:** **COMPLETE — PROJECT OWNER APPROVED.** Items 9.1–9.7 are accepted within the authorized Workstream 9 boundary. Gates 3A, 3B, and 3C remain approved; TD-14 remains **CLOSED / NOT REOPENED**. Workstream 10 is not authorized or begun; Gate 3D has not been reached; Phase 3 remains **IN PROGRESS**; Phase 4 remains **NOT AUTHORIZED**.

## Consumer contracts and rendering

`application.rendering` accepts an already-constructed logical `ContextPackage` and an explicit `ConsumerContract`. It provides Human, ChatGPT, and Codex presentations from one canonical, deterministically ordered package view. The presentation retains Context Request, Required and Supporting items, item selection basis, Authority and scoped Authority, Governance State, currentness/temporal qualification, Provenance, Conflict, Uncertainty, Source Manifest, package limitations, sufficiency, and Construction-State Coherence.

The three formats differ only in Consumer-facing introduction and organization. Their canonical governed payload is the same. Human output is comprehensible Markdown; ChatGPT and Codex outputs explicitly state that represented Source content, including imperative-looking content, is evidence rather than Context Engine instruction. A renderer never discovers, evaluates applicability, selects, assigns Required/Supporting, assesses sufficiency, creates Authority/Governance/currentness, resolves Conflict, or executes Source content.

Consumer disclosure is independent of Requester authorization at this boundary. If Consumer disclosure is absent, unknown, or denied, rendering fails closed with a non-sensitive reason and no content, metadata, reference, or package identifier. This v0.1 implementation does not select condensation, reference/progressive-disclosure, or multipart mechanisms. A declared capacity below the complete faithful rendering causes explicit failure; Required Context and qualifications are never silently truncated or waived.

## Local composition and CLI

`application.orchestration.run_governed_render` composes the already-approved services without duplicating their decisions:

```text
explicit Bootstrap -> Bootstrap/Project configuration validation
-> represented evidence / deterministic discovery -> applicability
-> governed selection -> sufficiency -> logical package construction
-> authorized Consumer rendering
```

Source observation, Markdown transformation, and representation remain their existing upstream application boundaries; this composition consumes their already-governed `DiscoveryEvidence`. It accepts explicit governed request, ASU/scope, applicability, role, sufficiency, coherence, and Consumer-contract inputs. Missing applicability inputs fail closed through the Workstream 7 evaluator. It is not a Context Package import/export format and creates no alternate semantic engine.

The native `context-engine bootstrap-validate` CLI operation establishes the explicit authorized-operator Bootstrap root, validates the Bootstrap-established Project configuration, and returns safe deterministic diagnostics. `readiness` remains a non-governed physical prerequisite diagnostic. The CLI does not infer Bootstrap, parse an ungoverned package import, or embed discovery/selection/sufficiency policy.

When an EB-03 store is supplied to application composition, package-construction history remains Workstream 8 durable evidence and a minimized `rendering-rendered`, `rendering-denied`, or `rendering-failed` audit outcome is written. Diagnostic output is not audit; audit detail contains public identifiers/reason codes only. Rendering success is not delivery, receipt, use, or Consumer action.

## State, failure, and deferrals

`ContextPackage != ConsumerRendering != DeliveryAttempt != ConsumerReceipt != ConsumerUse` remains explicit in the semantic kernel and outcome types. A rendering failure leaves the package unchanged; no rendering API creates a delivery, receipt, use, action, Authority, or currentness assertion. Historical package semantics remain historical after rendering or persistence reload.

No Human/ChatGPT/Codex API, model, LLM, embedding, vector/index, semantic search, renderer/template/CLI framework, network service, delivery mechanism, receipt mechanism, Consumer automation, backup/recovery workflow, Workstream 10 behavior, Gate 3D, proving, or Phase 4 behavior is implemented. Known limitation: no progressive-disclosure/reference or multipart renderer is selected; rather than claim that a reference was received, v0.1 preserves the full package view or fails on declared capacity.

## Validation and traceability

`tests/test_workstream_9.py` covers shared cross-renderer semantic payloads; Required/Supporting, Authority/Governance/currentness, Provenance/Conflict/Uncertainty/limitations, sufficiency/coherence fidelity; inert Source-content boundary; independent Consumer disclosure denial; capacity failure; no Authority/currentness creation; explicit Bootstrap-to-rendered controlled composition; durable audit versus diagnostic boundary; Sufficient rendering; and Denied construction without a fake rendering. The controlled fixtures use `~/temp` only. Existing Workstreams 1–8 tests continue to validate upstream discovery, enforcement, selection, sufficiency, package, persistence, and semantic boundaries.

This implements CE-FR-025–026 and 043 and CE-NFR-015–016, respecting Phase 1 conceptual Items 36–39 and Phase 2 A, B, E, F8–F13, G, and H. Findings: BLOCKER 0; MATERIAL 0; MINOR 0; OBSERVATION 0.
