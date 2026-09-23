# Phase 2 Domain B — Governance, Trust & Security Architecture

**Phase status:** **AUTHORIZED / IN PROGRESS.**

**Domain B status:** **COMPLETE — PROJECT OWNER APPROVED — PASS.**

**Domain C status:** **COMPLETE — PROJECT OWNER APPROVED — PASS.**

**Domain D status:** **COMPLETE — PROJECT OWNER APPROVED — PASS.**

**Domain E status:** **COMPLETE — PROJECT OWNER APPROVED — PASS.**

**Domain F status:** **COMPLETE — PROJECT OWNER APPROVED — PASS.**

**Domain G status:** **COMPLETE — PROJECT OWNER APPROVED — PASS.**

**Domain H status:** **COMPLETE — PROJECT OWNER APPROVED — PASS.**

**Domain I status:** **NOT BEGUN.**

**Next activity:** **I1 — Reconcile complete Phase 2 decision inventory.**

**Implementation:** **NOT AUTHORIZED.**

## Governance record

This record durably documents the Project Owner-approved B1–B16 Governance, Trust & Security Architecture baseline. It records already-approved architecture and does not introduce new material architecture, technology, security, governance, scope, persistence, identity/authentication, Source, Consumer, or implementation decisions. Phase 3 and later phases remain **NOT AUTHORIZED**.

## B1–B4 — Governance Bootstrap requirements and alternatives

**Governance Bootstrap** is the minimal, independently established, scoped, provenance-bearing governing basis necessary for the Context Engine to begin legitimate Project governance interpretation without relying upon ordinary Source content to establish that content's own Authority.

The Bootstrap establishes or securely identifies only what is necessary to enter normal governed processing:

- Project identity;
- initial governance Authority/basis;
- initial applicable governance scope;
- a legitimate reference/location from which further governed Project configuration may be obtained;
- enough authorization/trust information to determine what may be inspected next;
- Bootstrap Provenance/origin;
- applicable Bootstrap version/state where material; and
- explicit failure when Bootstrap cannot be established reliably.

Bootstrap remains intentionally small. It establishes legitimate entry into governance interpretation; it is not the complete Project governance model.

The conceptual trust dependency is:

```text
Independent Bootstrap
    ->
Project-governed configuration
    ->
normal governance interpretation
    ->
ordinary Source content
```

This is a trust dependency, not a required file, process, or component topology.

| ID | Non-circularity requirement |
| --- | --- |
| GB-01 | **Independent Initial Basis.** At least one initial governing fact originates outside the ordinary Source-content Authority chain being evaluated. |
| GB-02 | **No Self-Authorization.** A Source, Artifact, path, filename, metadata field, or embedded instruction cannot establish its own governing Authority merely by asserting it. |
| GB-03 | **Scoped Bootstrap Authority.** Bootstrap Authority applies only to its explicitly established purpose/scope and does not confer universal Authority on everything reachable from it. |
| GB-04 | **Traceable Delegation.** When Bootstrap points to further governed configuration, the chain establishing that configuration's applicability remains explainable and auditable. |
| GB-05 | **Fail Closed on Bootstrap Ambiguity.** If the required initial governing basis cannot be established reliably, affected governed operations do not proceed under assumed Authority. |
| GB-06 | **Bootstrap Is Configuration, Not Project Truth.** Bootstrap establishes how legitimate governance interpretation begins; it does not make every statement in referenced Sources true, current, relevant, authoritative, or authorized for every Consumer. |

Alternatives considered were:

| Alternative | Assessment |
| --- | --- |
| 1 — Invocation-Supplied Bootstrap | A small external trust root; simple and non-circular; a potential physical v0.1 mechanism. By itself it does not define the complete trust architecture. |
| 2 — Engine-Controlled Local Registry | A legitimate possible architecture that is durable and convenient, but would introduce engine-owned persistent governance state before Domain G persistence requirements are established. |
| 3 — Convention-Based Repository Bootstrap | Simple and portable, but **REJECTED** as a standalone Bootstrap architecture because repository content, filename, or path cannot establish its own governing Authority. |
| 4 — Hybrid External Bootstrap Reference + Project-Governed Configuration | A minimal independent trust root with Project identity, initial scope, and a legitimate governed-configuration reference; richer governance remains Project-portable and it avoids prematurely requiring an engine-owned registry. Selected at B5. |

## B5 — Governance Bootstrap architecture selection

**Project Owner-approved selection:** **Hybrid External Bootstrap Reference + Project-Governed Configuration.**

An independently established minimal Bootstrap establishes:

- Project identity;
- Bootstrap Provenance/origin;
- initial governance scope;
- a legitimate reference to Project-governed configuration; and
- enough integrity/identity information to establish that the referenced configuration is the intended configuration.

The referenced Project-governed configuration may establish richer governance only through Authority delegated by the Bootstrap and normal governed semantics. Ordinary Source content cannot bootstrap its own Authority. If the required Bootstrap cannot be established, or the intended governed configuration cannot be established within Bootstrap scope, affected governed Project processing fails closed. Material Context Engine operations must remain capable of identifying which Bootstrap state governed the operation.

This selection does **not** select a Bootstrap file format, Project configuration format, filesystem location, environment variable, CLI argument, registry/database, cryptographic signature, hashing scheme, Git identity mechanism, serialization mechanism, authentication system, or persistence technology. Invocation-supplied Bootstrap remains a possible downstream physical mechanism beneath the selected architecture; it was not selected here.

## B6 — Authority, Authority Scope, and Governance State

Governance applicability is evaluated rather than represented as an intrinsic boolean such as “is_authoritative.” Material governance evaluation must be capable of considering information/version identity, Governance State, applicable Authority, Authority Scope, Project/task/phase/domain/component/action scope, temporal applicability, supersession, applicable higher-scope governance, and an explainable basis for the resulting determination.

Authority and Governance State are independent dimensions. Approved does not mean universally authoritative; authoritative origin does not automatically make an unapproved Proposal governing; and superseded information may remain historically authoritative while no longer governing current action. Unknown Authority Scope is not unrestricted scope. Relationships, retrieval, transformation, copying, repetition, or persistence do not broaden or create Authority.

## B7 — Requester and Consumer authorization

Authorization uses a multi-stage architecture that distinguishes:

1. **Observation authorization:** May the engine inspect the Source/information for this request?
2. **Processing authorization:** May the engine internally use or transform the information for this governed operation?
3. **Package authorization:** May the information participate in the logical package intended for this Consumer?
4. **Disclosure authorization:** May the content and material metadata/Provenance be rendered or delivered to the Consumer/destination?

Requester and Consumer authorization are distinct. Source credentials do not establish Consumer authorization, and Requester access does not transfer disclosure rights to a less-authorized Consumer. Authorization may need re-evaluation as information is transformed, aggregated, classified, packaged, rendered, explained, or audited. It applies to content and protected metadata/Provenance where applicable. Ambiguous required authorization fails closed for the affected operation.

Inaccessible known information does not become nonexistent information. Known inaccessible Required Context must later participate in uncertainty/sufficiency evaluation rather than producing false completeness. This architecture selects no authentication or IAM technology.

## B8 — Project isolation and cross-Project retrieval

Projects are context-isolation boundaries by default. Cross-Project retrieval/use becomes eligible only when the task explicitly requires external Project context or an approved Relationship establishes potential applicability; applicable governance permits the crossing; Requester/Consumer authorization permits relevant operations; traversal remains bounded; and external origin remains identifiable.

A Relationship establishes potential applicability, not unrestricted retrieval. Authority does not automatically transfer across Projects. Originating Project, Source identity, Provenance, Authority Scope, Governance State, sensitivity, and temporal state remain identifiable. Each material boundary crossing is governed and authorized, and traversal is bounded rather than automatically transitive. Inaccessible Required external information affects later uncertainty/sufficiency.

Cross-Project information retrieval differs from higher-scope governance legitimately applicable to multiple Projects. Higher-scope governance must not be misrepresented as Authority transferred from one Project to another.

## B9 — Sensitive-information handling

Authorized information is not necessarily unrestricted information. Sensitive-information handling may apply to content, metadata, Provenance, Relationships, transformations, derived/inferred information, aggregation, historical state, and Consumer/destination/environment.

| ID | Requirement |
| --- | --- |
| SI-01 | **Preserve Sensitivity Semantics.** Source/governance sensitivity information remains associated with relevant information through observation, transformation, selection, packaging, rendering, explanation, and audit. |
| SI-02 | **Transformation Does Not Automatically Remove Sensitivity.** Summarization, extraction, normalization, inference, or other transformation does not inherently make information unrestricted. |
| SI-03 | **Derived Sensitivity Is Possible.** Individually non-sensitive information may produce sensitive information through aggregation or inference. |
| SI-04 | **Minimum Sufficient Context Applies to Sensitive Information.** Avoid exposing sensitive information that does not materially contribute to the task even where access is technically permitted. |
| SI-05 | **Unknown Sensitivity Does Not Mean Unrestricted.** Material uncertainty about handling requirements must be resolved or safely constrained rather than silently treated as unrestricted. |

No universal sensitivity-classification taxonomy is selected.

## B10 — Secret exclusion

Secret material is outside normal Context Engine content by default. Secret values include credentials, authentication material, and cryptographic material such as passwords, API keys, tokens, private keys, session secrets, recovery codes, signing secrets, and equivalent future secret types.

Known or suspected secret values should be excluded as early as reasonably possible and must not normally enter observed Context Engine content, derived Context Items, retrieval/indexing state, Context Packages, Consumer renderings, or audit logs.

The distinction is preserved:

```text
secret VALUE -> excluded normal context

safe information about existence, purpose, configuration requirement,
external reference, or external execution dependency -> may be context
where authorized and appropriate
```

A secret may be an external execution dependency without becoming Required Context content. Hashing, masking, truncating, encoding, or partial disclosure does not automatically make secret material safe. Context Requests cannot override secret exclusion. Actual secret retrieval would require separately approved future security/governance capability and is not authorized by Domain B.

## B11 — Untrusted content and governing-instruction separation

**Governing rule:** Retrieved or derived content is information to evaluate unless governed Authority, Governance State, scope, Provenance, and applicable Relationships establish instructional applicability. Imperative language alone grants no governing status.

This applies to Markdown/document content, source code, comments, strings, filenames, metadata, Git commit messages, API fields, generated/derived content, and other Source-derived information.

The architecture keeps three questions separate:

1. Content relevance.
2. Instructional applicability.
3. Consumer exposure.

Malicious or instruction-like content may still be Required Context for a security-analysis task without becoming an instruction to the Context Engine. Retrieval, indexing, repetition, transformation, or rendering does not elevate instructional Authority. Consumer renderers must preserve the conceptual distinction between “The Source says X” and “The Context Engine instructs the Consumer to do X.”

## B12 — Deterministic enforcement boundaries

Nondeterministic inference may not be the sole enforcement mechanism for safety-critical governed rules.

| ID | Deterministic enforcement boundary |
| --- | --- |
| DE-01 | **Authorization Decisions.** Applicable authorization rules require deterministic enforcement capability. |
| DE-02 | **Secret Exclusion.** Known governed secret-exclusion rules require deterministic enforcement capability; secret handling may not rely solely on probabilistic detection. |
| DE-03 | **Governance / Authority Enforcement.** Explicit governed Authority/Governance State cannot be replaced by an AI/model judgment that information “looks authoritative.” |
| DE-04 | **Project / Security Boundary Enforcement.** Default Project isolation, governed boundary crossing, and other hard security boundaries require deterministic enforcement capability. |

Nondeterministic mechanisms may potentially assist bounded semantic operations including relevance assessment, candidate discovery, classification assistance, summarization, inference, Conflict-detection assistance, Relationship discovery, and explanation drafting. Such output must retain appropriate transformation/Provenance/uncertainty state and cannot independently bypass deterministic controls. This does not select or require AI/LLM involvement.

## B13 — Security-relevant audit and explanation

Security auditability must preserve enough information for an appropriately authorized reviewer to understand why a material security/governance outcome occurred without requiring the audit record to duplicate protected information.

Material audit must be capable of representing, where applicable:

- Context Request/operation identity;
- Requester;
- Consumer;
- Project/scope;
- Bootstrap/governance basis;
- authorization outcome and material basis;
- Source-scope restriction;
- cross-Project boundary crossing;
- sensitive-information handling decision;
- secret-exclusion event;
- untrusted-content handling;
- Source failure/incomplete inspection;
- allow/deny/qualification outcome; and
- relevant time/state.

| ID | Audit requirement |
| --- | --- |
| AUD-01 | **Audit Is Authorization-Bound.** Audit access is itself governed and authorized. |
| AUD-02 | **Minimize Protected Content.** Audit should explain outcomes without unnecessarily copying protected content. |
| AUD-03 | **Metadata Is Not Automatically Safe.** Existence of a Source, Project, Relationship, denial, or other metadata may itself be protected. |
| AUD-04 | **Audit Evidence Does Not Create Authority.** Audit records explain historical behavior; they do not make underlying information authoritative. |
| AUD-05 | **AI Explanation Is Not Sole Security Evidence.** AI-generated explanations may summarize but cannot be the sole evidence for material deterministic security/governance enforcement. |

Explanation may summarize the decision; audit evidence supports the explanation. No log format, audit database, retention duration, cryptographic mechanism, or audit technology is selected.

## B14 — Security/governance failure and degraded operation

Failure is scoped rather than represented as one undifferentiated global failure state.

| ID | Failure behavior |
| --- | --- |
| GF-01 | **Governance-Establishment Failure.** Required Bootstrap/governance cannot be established: affected governed processing fails closed. |
| GF-02 | **Authorization Failure/Ambiguity.** Affected operation/information is denied; unrelated authorized operations may continue. |
| GF-03 | **Source/Evidence Failure.** Unavailable, inaccessible, or partially inspected evidence remains explicit; unrelated evidence may continue where legitimate, but completeness/sufficiency must later account for the limitation. |
| GF-04 | **Security-Handling Uncertainty.** If sensitivity, secret status, or instructional applicability cannot be safely resolved, affected operations use safer governed handling rather than assuming unrestricted treatment. |

**Invariant:** Degraded operation may reduce available context or capability; it may not relax governance/security guarantees merely to keep the system running.

Audit-write/persistence failure behavior is not fully decided here where it depends on later persistence/operational design. It is a downstream Domain G obligation; this record does not invent a persistence mechanism.

## B15 — Traceability and consistency review

The approved review result is that B1–B14 cover non-circular Governance Bootstrap; scoped Authority/Governance State; Requester/Consumer authorization; Project isolation/cross-Project behavior; sensitive-information handling; secret exclusion; untrusted-content separation; deterministic enforcement; security auditability; and explicit, fail-closed, degraded behavior.

The architecture is consistent with the approved Phase 0/1 baseline and Domain A architecture. No Domain B requirement inherently requires separate processes, microservices, enterprise IAM/SSO, a security service, a particular authentication technology, a particular persistence mechanism, or AI/LLM involvement. Physical identity/authentication mechanisms remain intentionally unresolved for downstream design and are not a Domain B architecture defect.

## B16 — Domain B security/governance gate

**Result: PASS — PROJECT OWNER APPROVED.**

| Finding type | Unresolved total |
| --- | ---: |
| BLOCKER | 0 |
| MATERIAL | 0 |

Domain B — Governance, Trust & Security Architecture is internally consistent with the Phase 0/1 baseline and Domain A architecture. B1–B16 are complete. Domains C–H are **COMPLETE — PROJECT OWNER APPROVED — PASS**. Domain I has **NOT BEGUN**; I1 is the next Phase 2 activity. This result does not authorize implementation, Phase 3, or any later phase.
