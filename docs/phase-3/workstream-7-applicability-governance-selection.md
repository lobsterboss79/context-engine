# Phase 3 Workstream 7 — Applicability, Governance/Security Enforcement, and Selection

**Status:** **COMPLETE — PROJECT OWNER APPROVED.** Items 7.1–7.8 are accepted within the authorized Workstream 7 boundary. Gate 3A and Gate 3B remain approved; TD-14 remains **CLOSED / NOT REOPENED**. Workstream 8 has not begun or been authorized; Workstreams 9–10 remain unauthorized; Gate 3C has not been reached or approved; Phase 4 remains **NOT AUTHORIZED**.

## Implemented transition and boundaries

`application.decision_pipeline` implements the bounded transition:

```text
Candidate Context -> deterministic applicability decision -> explicit selection -> Context Item
```

It consumes Candidate Context and explicitly supplied, already-established task relevance/scope, Bootstrap, Project, authorization, disclosure, currentness, and governing facts. It does not discover evidence, infer those facts from text/rank/parser structure, perform observation, persist hidden reasoning, decide sufficiency, construct a logical Context Package, render, deliver, or perform Consumer action.

`ApplicabilityOutcome` is limited to approved concepts: `applicable`, `inapplicable`, `unresolved`, and `denied`. Each result uses concise reason codes and preserved qualifications rather than a score or chain of thought. Discovery basis/ranking is not relevance evidence. Literal relevance must be supplied through explicit deterministic task evidence; absent or unknown relevance is unresolved.

## Governance and security enforcement

Every applicability operation receives `EnforcementInputs`. Invalid Bootstrap, non-established Requester authorization, non-established Consumer disclosure authorization, and non-established protected-metadata authorization deterministically return `denied` with the material reason. Requester and Consumer controls are independent; either denial does not authorize the other.

Project isolation is default. A Candidate whose supplied Project differs from the request Project is denied unless the pre-existing governed cross-Project prerequisites are explicitly true. The source scope remains preserved on Candidate Context; this work does not introduce a native Source Scope grammar.

Where an operation requires governing instruction/authority, Authority and Governance State are evaluated independently. A usable authority must have a known scope that matches the Candidate Project and any supplied domain, phase, action, and subject restriction; the represented subject must independently have `Approved` Governance State. Relationships, copying, repetition, rank, parser structure, recency, selection, persistence, and local Git evidence neither create nor broaden Authority. Unknown/insufficient governed authority is unresolved, never permissively treated as authority.

For current-direction tasks, currentness must be represented as `CURRENT`; historical or superseded evidence is inapplicable for that task, while unknown currentness is unresolved. Historical tasks retain historical evidence eligibility. Recency and local observation do not establish currentness or supersession.

Source-derived imperative content is information, not instruction. When use as instruction is requested, the candidate is denied unless independently established instructional authority and scoped approved governance are both present. Information can otherwise remain Candidate Context for an authorized task such as security analysis without becoming instruction.

## Required/Supporting and selection

Only an `applicable` Candidate with a nonempty explicit selection basis can become a sealed `ContextItem`. `RoleInputs` encodes the approved counterfactual omission principle as observable inputs:

- omission materially risks incorrect or improper task performance -> `Required`;
- otherwise, material improvement to understanding or validation -> `Supporting`;
- otherwise, no selection.

Consumer capacity, rendering limitation, convenience, rank, recency, repetition, parser shape, and relevance alone cannot change a Required item to Supporting or unselected. A selected item preserves the Candidate's represented information and Provenance. Conflict, Uncertainty, and limitations are retained in the decision explanation/qualifications; selection does not resolve them, create Authority, or establish sufficiency.

Selection explanations are structured reason codes plus explicit material bases. Examples are `consumer-disclosure-authorization-not-established`, `historical-or-superseded-for-current-task`, `counterfactual-omission-material-risk`, and `conflict-preserved`. They preserve decision evidence suitable for later authorized audit without persisting protected metadata or hidden chain-of-thought. Durable package-construction records and package/audit workflow remain Workstreams 8–10 work.

## Deliberately deferred

No Sufficient, Conditionally Sufficient, Insufficient, ASU-adequacy, bounded deficiency iteration, Conditional Sufficiency, logical Context Package, Source Manifest, construction coherence, renderer, delivery, receipt, use, backup/recovery, proving, or Phase 4 behavior is implemented. TD-14 remains closed; this work introduces no semantic-assistance technology.

## Traceability, validation, and findings

This increment implements CE-FR-009–015, 018–020, 027–035, 037, 040–041, and associated NFR safety/traceability boundaries using Phase 1 conceptual Items 17–35 and 40–46; Phase 2 B6–B14, D temporal/governance representations, E7–E10, and F5/F7 constraints.

`tests/test_workstream_7.py` supplies controlled tests for discovery/applicability separation; explicit relevance; scoped Authority/Governance State separation; current/historical/unknown qualification; Bootstrap, Requester, Consumer, protected-metadata, and cross-Project fail-closed behavior; inert Source instructions; Candidate-to-selected transition; Required/Supporting counterfactual roles; Consumer-capacity/rendering anti-waiver; Conflict/Uncertainty/Provenance preservation; no ranking/parser/recency/repetition semantic elevation; and selection/sufficiency separation.

No BLOCKER, MATERIAL, or MINOR finding was identified. The focused and complete validation results are recorded in the Workstream 7 review reports under `~/temp`.
