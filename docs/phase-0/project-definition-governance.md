# Phase 0 — Project Definition & Governance

**Status:** COMPLETE. The decisions documented here are approved. The documentation and consistency review are complete, and the Project Owner explicitly approved the Phase 0 exit gate. Phase 1 — Requirements & Context Model is AUTHORIZED to begin requirements and context-model work, but is not complete. Phase completion and authorization of the next phase remain separate Project Owner decisions. Phase 2 and later phases are NOT AUTHORIZED.

## 1. Purpose and problem statement

Context Engine is a general-purpose system for identifying, retrieving, prioritizing, and assembling authoritative information into task-specific context packages for AI systems and human users. It addresses distributed project knowledge and the risk of incomplete, stale, contradictory, irrelevant, or unnecessarily large context while preserving provenance, authority, relevance, and currency. It does not independently make project decisions.

**Design generally. Implement narrowly.** The model and architecture should support multiple project, source, and consumer types without broad v0.1 feature coverage.

## 2. Initial users and consumers

The system supports human and machine users/consumers and is not inherently coupled to a particular AI provider, model, agent, or interface. Initial v0.1 consumers are human-readable output, ChatGPT-oriented context, and Codex-oriented context. Authorized AI systems may request and retrieve context within their permissions.

## 3. Governance and decision authority

The Project Owner is final approving authority for material decisions. ChatGPT may analyze, challenge, recommend, and review. Codex implements and documents approved decisions, may make ordinary implementation choices within approved requirements and architecture, and must escalate material changes to scope, architecture, technology, security, governance, data models, dependencies, or approved boundaries. The engine may communicate authority but cannot create it.

## 4. Definition of context

Context is information selected from available sources because it is relevant to understanding or performing a particular task, with enough metadata to establish meaning, provenance, authority, and currency. Conceptual classes are identity, governance, state, requirements, decisions, constraints, architecture, evidence, implementation, history, relationships, and open items. These are conceptual classes, not an approved implementation schema. Context includes relationships, and source artifacts remain distinct from assembled context.

## 5. Authoritative-source principles

Authority derives from a source and its governed role and may be fact/domain-specific. Approved decisions and explicit supersession relationships must be honored. Material conflicts between authoritative sources must be surfaced, not silently discarded. AI summaries and inferences remain distinguishable from authoritative source information. Provenance must explain why information was considered authoritative; uncertain authority remains uncertain.

## 6. Provenance requirements

Material context claims must trace to their originating sources, and provenance must survive retrieval, prioritization, summarization, and assembly. Compact references are acceptable if full provenance remains retrievable. Direct source information, transformed/summarized information, and inferred information remain distinguishable.

## 7. Task-specific context

Assembly is task-specific and seeks **minimum sufficient context**: the smallest body of authoritative information reasonably sufficient for correct task understanding and performance. Correctness takes priority over token efficiency; governing information and constraints must not be omitted for size. Required and supporting context may be distinguished, selection should eventually be explainable, and packaging may vary by consumer without changing meaning, provenance, authority, or uncertainty.

## 8. Initial source scope and extensibility

v0.1 initially targets local Git repositories, Markdown artifacts, and structured metadata where necessary. The structured-metadata representation is not selected. Git state/history may itself be context, distinct from file content. Direct ChatGPT-conversation ingestion and integrations including Slack, Teams, email, Google Drive, GitHub APIs, databases, Nevis Data Lake, arbitrary APIs, PDFs, and Office documents are not required for v0.1; they are anticipated future source types, not permanently unsupported. Source extensibility is first-class: new types should use defined source interfaces/adapters without material core redesign.

## 9. Context packages and outputs

A Context Package is first-class, not inherently a prompt: task-specific context for a defined consumer. Its logical form should support a structured/machine-readable representation, consumer-specific rendering, source manifest/provenance, conflicts and uncertainty, relevant unresolved questions, and metadata sufficient for auditing and substantial reproducibility. Human, ChatGPT, and Codex renderings may differ while preserving meaning, authority, provenance, and uncertainty.

## 10. Freshness and supersession

The engine must distinguish currently applicable information from historical information. Superseded information is retained. Explicit supersession overrides recency assumptions; newer is not inherently authoritative or current. Approval state, authority, effective scope, supersession, version, and temporal freshness may affect currentness. Suspected supersession must not silently become authoritative supersession. Historical information can matter for historical tasks, context types may differ in freshness characteristics, and uncertain currency remains uncertainty.

## 11. Project isolation and cross-project context

Projects are context-isolation boundaries by default. Cross-project retrieval is permitted only when the task explicitly requires it or an approved relationship/dependency authorizes it. Cross-project information preserves origin and provenance. Authority is scope-bound and does not automatically propagate; security/authorization may further restrict retrieval.

## 12. Security and sensitive-information boundaries

Access to a source does not authorize disclosure to every consumer; authorization occurs before unauthorized information enters a package. Preserve source permissions and project boundaries where applicable. Exclude secrets and credentials from normal ingestion/retrieval by default; any future secret retrieval requires separately approved security design. Packages may be sensitive, and aggregation must not silently weaken source security. Keep retrieved source content distinguishable from trusted governance/system instructions and anticipate malicious/untrusted content and indirect prompt injection. Security-relevant retrieval/authorization decisions should eventually be auditable. When authorization is uncertain, fail closed. AI consumers cannot expand their permissions or authority by requesting more context.

## 13. Human control and AI autonomy

Authorized AI systems may request permitted context and propose conflicts, relationships, classifications, corrections, supersession candidates, and context improvements. Proposals remain distinct from approved authoritative information. AI systems may not establish authority, approve material decisions, resolve governance conflicts, expand permissions, or declare their inferences authoritative. The engine must not silently modify authoritative sources to reconcile inconsistencies. AI-derived information retains derived/proposed status; automated governance or source modification needs explicit approval and controls.

## 14. v0.1 success criteria

v0.1 is a functional proof of concept, not a production platform. It succeeds by demonstrating all of the following:

1. Read supported initial sources from at least one real Git project.
2. Represent relevant context without hard-coding that project's semantics into the core.
3. Generate a task-specific Context Package.
4. Preserve usable provenance for material claims.
5. Distinguish current and superseded information when sources provide sufficient evidence.
6. Represent material conflicts/uncertainty rather than silently resolving them.
7. Maintain project isolation.
8. Produce human, ChatGPT, and Codex renderings from one logical package.
9. Let a fresh ChatGPT session use an AI Roadmap package to resume meaningful work with substantially less manual reconstruction.
10. Produce useful context for continued Context Engine development.
11. Demonstrate a path to another source adapter without core redesign.
12. Explain why important information was included and where it originated.

No arbitrary token-reduction percentage is approved.

## 15. Initial proving ground

The Company AI Roadmap is the first external proving ground. Context Engine itself is the dogfooding case. Validation projects may supply project-specific configuration/metadata but must not embed project-specific behavior in the core.

## 16. Dogfooding

Context Engine must eventually produce sufficient context to continue its own development through the same core mechanisms used for other projects, with no hard-coded privileged self-knowledge. Manual context management is expected during bootstrap. Dogfooding failures should inform general requirements, not automatically create project-specific hacks.

## 17. Explicit v0.1 non-goals

v0.1 does not require vector/embedding retrieval; a knowledge graph/database; an autonomous agent framework; GUI/web application; cloud deployment; enterprise-scale/high-availability architecture; Slack/Teams; ChatGPT conversation; email; Google Drive/SharePoint; GitHub Issues/PR API; Nevis Data Lake; Salesforce/Practifi/Orion; arbitrary database/API; PDF/Office ingestion; automatic modification of authoritative documents; AI authority to approve decisions or resolve conflicts; secret/credential retrieval; full enterprise IAM/SSO; large-scale optimization; real-time/event-driven ingestion; multi-user collaborative UI; or universal project/document-structure support. Non-goals may guide extensibility but must not be implemented merely because they are interesting. If one becomes necessary for a success criterion, scope requires explicit reconsideration.

## 18. Phase 0 exit gate

Phase 0 may close only when all 18 items are documented; documentation accurately reflects approved decisions; purpose, scope, governance, authority, security, source boundaries, context principles, success criteria, and non-goals are internally consistent; no unresolved Phase 0 issue materially blocks requirements work; `AGENTS.md` establishes operating rules and Project Owner authority; the README communicates purpose and status; a roadmap identifies major phases without prematurely fixing implementation details; the checklist links completed items to governing documentation; documentation passes consistency review; and the Project Owner explicitly approves the exit gate. These conditions have been met: the Project Owner explicitly approved Phase 0. Phase 1 — Requirements & Context Model is AUTHORIZED to begin requirements and context-model work, but is not complete. Phase completion and authorization of the next phase remain separate Project Owner decisions. Phase 2 and later phases are NOT AUTHORIZED.
