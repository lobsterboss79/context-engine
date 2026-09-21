# Functional Requirements Register

**Governed status:** Approved Phase 1 baseline. Each identifier occurs once in this register and has stable, exact approved wording.

| ID | Name | Approved requirement |
| --- | --- | --- |
| CE-FR-001 | Accept Context Requests | The Context Engine shall accept a Context Request describing a task for which context is required. |
| CE-FR-002 | Identify Requester and Consumer | The engine shall be capable of distinguishing the Requester from the intended Consumer. |
| CE-FR-003 | Establish Request Scope | The engine shall determine the applicable project/context scope before retrieving information. |
| CE-FR-004 | Validate Request Sufficiency | The engine shall identify when a request lacks information necessary to determine an appropriate context scope or task. |
| CE-FR-005 | Access Authorized Sources | The engine shall retrieve information only from sources available within the Requester's and Consumer's applicable authorization boundaries. |
| CE-FR-006 | Discover Candidate Information | The engine shall identify information potentially relevant to the requested task. |
| CE-FR-007 | Preserve Source Identity | Retrieved information shall remain associated with its originating source. |
| CE-FR-008 | Preserve Project Boundary | Retrieved information shall remain associated with its applicable project or other governing scope. |
| CE-FR-009 | Evaluate Relevance | The engine shall determine whether candidate information is relevant to the requested task. |
| CE-FR-010 | Evaluate Authority | The engine shall preserve and consider the governed authority of information when determining applicability. |
| CE-FR-011 | Evaluate Currentness | The engine shall consider applicable freshness, version, effective state, and supersession information when determining current context. |
| CE-FR-012 | Evaluate Relationships | The engine shall consider material relationships among information when determining applicable context. |
| CE-FR-013 | Distinguish Information State | The engine shall distinguish direct/source information, transformed or summarized information, and inferred or proposed information. |
| CE-FR-014 | Surface Material Conflicts | The engine shall represent material conflicts rather than silently discard or resolve them without governed authority. |
| CE-FR-015 | Represent Uncertainty | The engine shall represent material uncertainty when authority, currentness, meaning, scope, or other necessary properties cannot be established reliably. |
| CE-FR-016 | Identify Material Gaps | The engine shall identify when information necessary to support a requested task is unavailable or insufficient. |
| CE-FR-017 | Prevent False Sufficiency | The engine shall not represent a Context Package as sufficient when known material information gaps prevent trustworthy performance of the task. |
| CE-FR-018 | Select Minimum Sufficient Context | The engine shall seek the smallest body of authorized, authoritative, and relevant information reasonably sufficient for correct task performance. |
| CE-FR-019 | Preserve Governing Context | The engine shall not exclude applicable governing decisions, constraints, security requirements, or other necessary context merely to reduce package size. |
| CE-FR-020 | Distinguish Required and Supporting Context | The engine shall be capable of distinguishing information necessary for task performance from information that materially improves understanding or validation. |
| CE-FR-021 | Assemble Context Packages | The engine shall assemble selected information into a logical Context Package associated with the originating Context Request. |
| CE-FR-022 | Preserve Provenance | Material context claims shall remain traceable to their originating source or sources. |
| CE-FR-023 | Preserve Transformation Provenance | When information is transformed, summarized, or inferred, the engine shall preserve the relationship between the resulting information and its source material. |
| CE-FR-024 | Provide Source Manifest | A Context Package shall be capable of identifying the material sources used in its construction. |
| CE-FR-025 | Render for Consumers | The engine shall support consumer-appropriate representations of a logical Context Package. |
| CE-FR-026 | Preserve Semantics Across Renderings | Consumer-specific rendering shall not silently change material meaning, authority, provenance, conflicts, or uncertainty. |
| CE-FR-027 | Explain Included Context | The engine shall be capable of explaining why material information was included in a Context Package. |
| CE-FR-028 | Explain Provenance and Authority | The engine shall be capable of identifying where material context originated and the basis upon which its authority was assessed. |
| CE-FR-029 | Explain Currentness/Supersession | Where relevant, the engine shall be capable of explaining why information was treated as current, historical, or superseded. |
| CE-FR-030 | Explain Material Exclusion or Deprioritization | Where practical and material to understanding the package, the engine shall be capable of explaining why candidate information was excluded or deprioritized. |
| CE-FR-031 | Isolate Projects by Default | The engine shall treat projects as context-isolation boundaries by default. |
| CE-FR-032 | Control Cross-Project Retrieval | The engine shall retrieve cross-project information only when explicitly required by the task or permitted by an approved relationship/dependency and applicable authorization. |
| CE-FR-033 | Preserve Cross-Project Origin | Cross-project context shall remain identifiable as originating outside the primary project. |
| CE-FR-034 | Authorize Before Packaging | The engine shall ensure information is authorized for the applicable Consumer before including it in a Context Package. |
| CE-FR-035 | Fail Closed | When authorization cannot be reliably established, the engine shall exclude the information. |
| CE-FR-036 | Exclude Secrets by Default | Secrets and credentials shall be excluded from normal context ingestion and retrieval. |
| CE-FR-037 | Preserve Trust Boundary | Retrieved source content shall remain distinguishable from trusted system/governance instructions. |
| CE-FR-038 | Support Non-Authoritative Proposals | Authorized users and AI systems shall be able to propose context-model improvements without those proposals automatically becoming authoritative. |
| CE-FR-039 | Preserve Proposal Status | AI-derived or other unapproved proposals shall remain distinguishable from approved authoritative information. |
| CE-FR-040 | Prevent Authority Laundering | Retrieval, repetition, transformation, or storage of non-authoritative information shall not independently elevate its authority. |
| CE-FR-041 | Prevent Unauthorized Governance Changes | The Context Engine shall not independently approve material decisions, resolve governed conflicts, expand permissions, or modify authoritative sources without separately authorized capability. |
| CE-FR-042 | Support Source Extensibility | The conceptual system shall permit additional source types without requiring material redesign of core context semantics. |
| CE-FR-043 | Support Consumer Extensibility | The conceptual system shall permit additional Consumer types without requiring material redesign of the logical Context Package. |
| CE-FR-044 | Retain Package Construction Context | The system shall preserve enough information to substantially explain how a Context Package was constructed. |
| CE-FR-045 | Associate Package with Request | A Context Package shall remain traceable to the Context Request that caused its construction. |
| CE-FR-046 | Support Material Audit | The system shall make material source-selection, authority, provenance, conflict, and security decisions inspectable to an appropriately authorized actor. |

## Approved normative semantic relationships (Item 56 resolution)

The approved conceptual Items 6–55 are normative semantic definitions and behavioral qualifications applicable to this stable register; they are not merely explanatory prose. This section adds cross-references and does not alter any stable requirement wording or create identifiers.

- Context Package, source-manifest, rendering, package-construction, and request-association requirements use the package, rendering, and audit semantics in Items 36–39.
- Authority/currentness evaluation and explanation requirements use the distinct Authority, Governance State, temporal, currentness, and supersession semantics in Items 17–25. Neither approval, recency, storage, nor implementation alone substitutes for those distinctions.
- The requirements preventing false sufficiency and selecting minimum sufficient context use the Sufficient, Conditionally Sufficient, and Insufficient semantics in Item 33 and the logical-package qualifications in Items 36–37.
- Source access, authorization-before-packaging, and fail-closed requirements use Items 40–46. Information may enter Consumer-visible context only when applicable disclosure authorization permits that Consumer to receive it; a more-authorized Requester cannot transfer broader access to a less-authorized Consumer. If Required Context cannot be disclosed, that limitation participates in sufficiency.
- Material-exclusion/deprioritization explanation is task-specific. Practicality/materiality considers whether omission of an explanation could materially impair an authorized actor’s understanding, validation, or audit of the package; every irrelevant candidate need not be explained.
