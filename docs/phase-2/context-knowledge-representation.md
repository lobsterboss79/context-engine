# Phase 2 Domain D — Context Knowledge Representation

**Current Phase status:** **COMPLETE — PASS — PROJECT OWNER APPROVED.**

**Domain D status:** **COMPLETE — PROJECT OWNER APPROVED — PASS.**

**Unresolved BLOCKER:** **0.**

**Unresolved MATERIAL:** **0.**

**Unresolved MINOR:** **0.**

**Domain E status:** **COMPLETE — PROJECT OWNER APPROVED — PASS.**

**Domain F status:** **COMPLETE — PROJECT OWNER APPROVED — PASS.**

**Domain G status:** **COMPLETE — PROJECT OWNER APPROVED — PASS.**

**Domain H status:** **COMPLETE — PROJECT OWNER APPROVED — PASS.**

**Domain I status:** **COMPLETE — PASS — PROJECT OWNER APPROVED.**

**Phase 3:** **AUTHORIZED — NOT YET BEGUN.**

**Phase 4:** **NOT AUTHORIZED.**

## Governance record

This record durably documents the Project Owner-approved D1–D19 Context Knowledge Representation baseline. It records already-approved logical representation architecture and introduces no new material architecture, technology, security, governance, scope, persistence, logical-representation, discovery/retrieval, selection, Consumer, or implementation decision. Domains E–I are **COMPLETE — PROJECT OWNER APPROVED — PASS**. Phase 3 is **AUTHORIZED — NOT YET BEGUN**; Phase 4 remains **NOT AUTHORIZED**.

## D1 — Domain D representation constraints

| ID | Approved constraint |
| --- | --- |
| KR-01 | **Semantic Identity Is Distinct from Locator.** Filesystem paths, URLs, repository locations, filenames, and equivalent locators do not universally define semantic identity. |
| KR-02 | **Identity Is Distinct from Version/State.** The same identifiable entity may exist across multiple versions, states, or observations. |
| KR-03 | **Identity Is Distinct from Content Equality.** Different Artifacts may contain identical content, while one Artifact may change content without inherently becoming a different Artifact. |
| KR-04 | **Native Identity May Contribute Without Becoming Universal Identity.** Source-native identifiers may provide strong identity evidence without making Git or another Source's identity semantics universal Context Engine identity. |
| KR-05 | **Unknown Identity Relationships Remain Unknown.** Where equivalence/continuity cannot be reliably established, do not force same/different identity merely from names, paths, or content similarity. |
| KR-06 | **Identity Does Not Confer Authority.** Establishing identity does not establish Authority, Governance State, currentness, relevance, truth, or authorization. |
| KR-07 | **Historical Identity Remains Addressable.** Locator, version, currentness, or Governance State changes must not make historical evidence conceptually unreferenceable. |
| KR-08 | **Identity Operations Preserve Project Isolation.** Cross-Project similarity or shared native identifiers do not silently merge Project-specific context. |
| KR-09 | **Provenance Accompanies Material Identity Assertions.** Where equivalence, continuity, or distinction materially affects interpretation, its basis must remain explainable. |
| KR-10 | **Logical Identity Does Not Prescribe Physical Keys.** No UUID, integer, hash, composite key, database primary key, or other physical identifier mechanism is selected by Domain D. |

## D2 — Logical identity principles

The logical model distinguishes **semantic identity**, **Source-native identity**, and **locator**. Semantic identity may be supported by Source-native identity, may have one or more locators over time, and may persist across versions/observations. Native Source identifiers are evidence usable by the logical model; they are not automatically universal Context Engine identifiers. A locator answers where/how something may be accessed; identity answers what identifiable thing it is.

Comparison preserves three conceptual outcomes: same identity established, distinct identity established, and identity relationship unresolved. Unresolved cases are not forced into same/different.

## D3 — Project representation

A logical Project represents the governed context/isolation identity rather than a repository or Source. It must logically support Project identity; Project registration state/reference; applicable Governance Bootstrap/governance association; applicable scope information; relationships to registered Sources; and Project-level Provenance needed to explain establishment.

Project representation is not all Project context. A Project is not a Git repository, may have one Source, multiple Sources, or no currently observable Source while remaining the same Project. Project identity is distinct from governed Project-configuration version/state; changing Source registration or governance configuration does not inherently create a new Project. Domain D selects no physical Project identifier.

## D4 — Source and Source Scope representation

Source representation must logically support Source identity; Source type/capability information; locator/access references; governed Project association(s); Source Scope; registration/governance state; Provenance; and known availability/capability information where appropriate. Source identity != Source locator != Source observation.

Source Scope is first-class governed information because it may materially affect authorization, evidence boundaries, Provenance, Applicable Source Universe, explanation, and reproducibility. It must be capable of expressing which portion/aspect of a Source is governed as potentially eligible for a Project, without requiring one universal Source Scope language. Where material, logical Source Scope preserves the Source to which it applies, governed scope meaning, native expression/reference where needed, and Provenance/governance basis. Source Scope remains distinct from task-specific relevance.

## D5 — Artifact, Artifact Version/State, and observation

The model preserves three distinct concepts: **Artifact**, **Artifact Version/State**, and **Observation / Observed Source State**.

An Artifact is an identifiable information-bearing unit exposed through a Source. For v0.1, a Markdown file may commonly be an Artifact candidate, but Artifact=file is not a universal rule. Artifact identity may preserve continuity across locator/version changes where sufficient evidence establishes continuity; similar content or names do not establish it.

Artifact Version/State represents a materially distinguishable state of an Artifact. It may correspond to a committed Git version, working-tree state, historical version, or another Source-native version/state. Not every Source must expose immutable or numbered versions.

An observation is not itself an Artifact Version/State. Multiple observations may observe the same Artifact Version/State, and one observation may establish multiple relevant states, such as a committed state plus a modified working-tree state. Artifact Version/State describes information-bearing state; Observed Source State describes what the Context Engine established during a particular observation boundary. For Git, committed state and observed working state remain distinguishable. Artifact Version is not defined solely by content hash, and content equality does not establish semantic identity.

## D6 — Claim representation

A **Claim** is an identifiable semantic assertion at governed granularity, attributable to one or more information-bearing inputs and represented independently of whether it is true, authoritative, approved, current, relevant, or selected as context.

Claim identity is the semantic assertion at governed granularity and remains independent of changing Authority, Governance State, Authority Scope, temporal applicability, Source location, Provenance/support, or supporting Artifact/Artifact Version. Materially changed semantic assertions are distinct Claims. Where semantic equivalence cannot be reliably established, uncertainty is preserved rather than forcing Claim identity consolidation.

Claim is not a text span; its identity is not normalized-text equality; and it is distinct from Artifact. One Artifact may support zero, one, or many Claims, and one Claim may have multiple Artifact/Source supports. Repeated/similar wording does not automatically establish semantic equivalence, and repetition does not create or elevate Authority. Claim representation supports material Provenance to supporting observations/Artifacts/states and direct versus derived status. Domain D selects no semantic-equivalence algorithm.

## D7 — Context Item representation

A **Context Item** is a governed, task-specific unit of selected information used in context construction. A Context Item may represent selected Claims, Conflicts, Relationships, Constraints, gaps, Uncertainty, availability conditions, authorization limitations, historical information, Candidates/Proposals, or other contextual information justified by the approved conceptual model.

Context Item is broader than Claim, but is not synonymous with all represented knowledge. Before task-relative selection, underlying represented information remains Claims, Relationships, Conflict state, Unknown/gap state, Candidates, Artifact-derived information, or other governed represented knowledge. Context Item status arises through task-relative selection. The governing distinction is:

```text
represented information
    !=
candidate for this request
    !=
Context Item / selected information
    !=
Required or Supporting Context
```

Required/Supporting classification remains downstream Domain E work. Selection does not create Authority.

## D8 — Classification representation

Classification expresses extensible semantic role. Approved conceptual examples include Identity, Governance, Requirement, Decision, Constraint, State, Architecture, Implementation, Evidence, Risk, Assumption, Open Question, and History. Multiple Classifications are permitted.

Classification remains distinct from truth, Authority, Governance State, Provenance, currentness, task relevance, and Required/Supporting status. It does not make a Proposal approved or authoritative. Where Classification is derived/inferred, its derivation/Provenance must be representable. Domain D selects no classifier or classification technology.

## D9 — Relationship representation

Relationships are explicit, directed, typed, scoped where material, Provenance-bearing semantic connections between identifiable governed information. The extensible vocabulary may include derives-from, supports, contradicts, supersedes, amends, applies-to, depends-on, implements, satisfies, constrains, belongs-to/scoped-to, and other justified governed relationships.

Relationship direction may matter. Relationships do not automatically transfer Authority or Governance State, and cross-Project relationships do not merge Projects. A Relationship may itself be Source-expressed, governance-established, deterministically derived, inferred/proposed, or uncertain as appropriate. Material Relationship scope remains representable and Relationship Provenance traceable.

## D10 — Authority and Authority Scope

**Authority** is a governed basis for information to control or materially influence interpretation or action. Its representation must be capable of associating, where material, applicable information/entity, governing basis/origin, Authority Scope, temporal applicability, Provenance, and governed delegation/precedence relationships.

Authority is not inherited merely from a Source container: authoritative Sources may contain drafts, quotations, history, rejected proposals, or untrusted content. Artifact approval does not automatically make every contained/quoted Claim authoritative. Authority is distinct from truth, confidence, evidence, popularity, Governance State, relevance, and authorization. Unknown Authority Scope is not unrestricted Authority. Transformation, repetition, retrieval, relationships, persistence, or package inclusion do not broaden Authority.

Authority Scope supports governed limitation by dimensions such as Project, domain/component, phase, action, subject, time, or other legitimate governance boundaries without requiring a rigid universal schema.

## D11 — Governance State and Candidate/Proposal lifecycle

Conceptual Governance States include Proposed, Pending, Approved, Rejected, Withdrawn, Superseded, and Unknown. Domain D imposes no universal workflow between them. Governance State applies to identifiable information/version. Approval of version/state X does not automatically approve materially changed version/state Y merely because it retains the same filename, locator, or Artifact identity.

Candidate/Proposal state remains distinct from evidence strength, confidence, truth, Authority, and relevance. A Candidate may be useful and well-supported while remaining non-approved. Retrieval, repetition, transformation, persistence, summarization, or package inclusion does not convert Candidate/Proposal information into an approved Decision.

## D12 — Provenance and transformation lineage

Provenance is traceable origin, support, observation, transformation, and governed action rather than one flat Source field. Material Provenance must be capable of identifying, where applicable, originating Project/Source; Artifact/version/state; relevant observation; location/reference; supporting Claims/Context Items or other upstream information; transformation nature; governing action; and honest missing Provenance. Multiple upstream inputs are supported.

Transformation distinctions include direct/Source-derived, normalized, summarized, inferred, and proposed. Transformation does not erase prior state. A summary/derived representation of approved or authoritative information does not automatically acquire independent identical Authority or Governance State. Derived information retains lineage to material inputs and its own transformation state. Compact/retrievable lineage is permitted where material Provenance remains recoverable. No graph database or graph technology is selected.

## D13 — Temporal and currentness representation

Logical representation must be capable of distinguishing, where applicable, event/assertion time; effective time; Source/Artifact version or modification time; observation time; and request/package-construction time. These are not interchangeable.

Freshness != currentness. Currentness is a governed applicability assessment informed by relevant evidence including time, version, Governance State, Authority, scope, supersession, and available evidence. Recency alone does not establish currentness: old information may remain current and recent information may already be superseded. Unknown or coarse temporal information remains honestly unknown/coarse rather than fabricated precision.

## D14 — Supersession and historical context

Supersession is a governed Relationship indicating that newer/different information replaces some or all applicability of earlier information within a defined scope. It is scoped, does not delete history, and leaves superseded information eligible for historical tasks. It is distinct from ordinary Artifact/version evolution; a new Git commit does not automatically supersede every prior Claim. Inferred/likely supersession remains inferred/proposed until governed evidence establishes it. Partial supersession preserves applicability outside the superseded scope.

Historical reconstruction must be capable of distinguishing contemporaneously applicable knowledge from later retrospective knowledge.

## D15 — Conflict representation

A **Conflict** is a material incompatibility among information sufficiently applicable within overlapping scope such that the information cannot all be accepted or acted upon together without qualification or resolution. Evaluation may need to consider subject/meaning, scope, time, Authority, Governance State, supersession, and applicability.

Conflict detection != Conflict resolution. The Context Engine may identify Conflict without Authority to resolve it. Domain D adopts no arbitrary resolution rules such as newest wins, majority wins, most repeated wins, highest similarity wins, first/last retrieved wins, or AI/model preference wins; such a rule may apply only if applicable governance separately establishes it. Unresolved material Conflict remains explicit and may later affect sufficiency.

## D16 — Uncertainty, Unknown, missingness, and epistemic state

The model preserves structured epistemic distinctions. **Unknown** means a relevant fact/state is not established. **Missing** means expected/required information is not present within the established observation/evidence boundary. **Unavailable** means relevant information/Source is known but cannot currently be obtained. **Unauthorized / Undisclosable** means relevant information may exist or may be known but cannot legitimately participate in the affected operation or disclosure. **Ambiguous** means available evidence supports multiple materially plausible interpretations. **Unresolved Conflict** means materially incompatible applicable information remains unresolved. **Unverified** means information exists or has been reported, but a stronger proposition has not been independently established. **Inferred / Proposed** means information is derived beyond direct observation and retains its inference/proposal state. These states may overlap where semantically appropriate.

The following distinctions are mandatory: unknown != false; not found != nonexistent; unavailable != absent; unauthorized != absent; rejected != false; and superseded != historically invalid. Missingness is always relative to an established observation/evidence boundary. “Not found” means not found within the inspected/evaluable evidence boundary; it does not mean the information does not exist anywhere.

Numeric confidence is not a required core semantic. A future mechanism may provide confidence information, but it cannot replace structured Provenance, Authority, Governance State, Conflict, Uncertainty, Source availability, or evidence-boundary state.

## D17 — Integrated logical-representation review

D17 reviewed D1–D16 for identity continuity and ambiguity; Project/Source/Artifact boundaries; Artifact Version/State versus observation; Claim semantic identity; Context Item semantics; Classification; Relationships; Authority and Authority Scope; Governance State; Candidate/Proposal lifecycle; Provenance and transformation lineage; temporal/currentness semantics; supersession and history; Conflict; Uncertainty/Unknown/missingness/epistemic state; circularity; technology leakage; and consistency with Phase 0/1 and Domains A–C.

**D17 result:** **PASS — PROJECT OWNER APPROVED.** Findings were BLOCKER: 0; MATERIAL: 0; MINOR: 1 identified; MINOR unresolved after disposition: 0.

The MINOR finding concerned provisional D7 wording that described a Context Item too broadly as information merely eligible to participate in later selection. That wording drifted from the governed Phase 1 definition of Context Item as task-specific selected information. The Project Owner approved the remediation: a Context Item is a governed, task-specific unit of selected information used in context construction; represented Claims, Relationships, Conflicts, gaps, Candidates/Proposals, and other governed knowledge may exist without automatically being Context Items; and Context Item status arises through task-relative selection. The D7 distinction above is controlling.

This correction restores exact alignment with the governed Phase 1 conceptual model, introduces no new concept, changes no other D1–D16 decision, selects no technology, and leaves Required/Supporting determination to Domain E.

D1–D16 form a coherent logical representation architecture preserving the governed Phase 1 conceptual model, Domains A–C boundaries, semantic-dimension separation, Provenance, historical meaning, epistemic integrity, and technology independence. No unresolved BLOCKER, MATERIAL, or MINOR logical-model finding remains after the D7 clarification.

## D18 — Requirements / conceptual-model traceability review

**D18 result:** **PASS.** Principal approved mapping:

| Phase 1 conceptual area | Domain D coverage |
| --- | --- |
| Project / Source / Source Scope | D2–D4 |
| Artifact / Artifact Version / Observed State | D5 |
| Claim | D6 |
| Context Item | D7, including the Project Owner-approved D17 clarification preserving task-specific selected-information semantics |
| Classification / Relationships | D8–D9 |
| Authority / Authority Scope / Governance State | D10–D11 |
| Provenance / transformation state | D12 |
| Temporal / currentness / supersession / historical context | D13–D14 |
| Conflict / Uncertainty / Unknown | D15–D16 |

Domain D preserves the Phase 1 model's central principle that information has multiple non-substitutable dimensions rather than one generic trust/status/confidence property. The Phase 1 requirements and traceability baseline covering Source, Artifact, Claim, Provenance, Relationships, currentness, Conflict, and Uncertainty are not weakened by D1–D17.

Domain D does not redefine downstream task-relative semantics for Context Request; Task Intent / Scope; discovery/retrieval; candidate-context evaluation; Context Selection; Required versus Supporting Context; sufficiency; Context Package; or Consumer rendering. These remain downstream Domain E/F concerns. No requirements/conceptual-model contradiction or material traceability gap was identified.

## D19 — Adversarial semantic-representation review

**Approved scenarios and safe behavior:**

1. Same sentence copied into multiple files: do not determine Claim count/identity solely from text equality; preserve support/Provenance and establish semantic identity only when justified.
2. Same Claim appears repeatedly: additional support may be recorded; repetition does not create Authority.
3. Claim wording changes while the semantic assertion remains materially the same: Claim continuity may be established at governed semantic granularity; literal text equality is not identity.
4. Semantic meaning materially changes while filename remains the same: represent a distinct Claim; filename/Artifact continuity cannot hide semantic change.
5. Claim/Artifact identity equivalence is uncertain: preserve uncertainty rather than forcing merge.
6. An approved document/version is materially edited: the new state does not silently inherit prior approval.
7. An approved Claim is summarized or transformed: preserve transformation lineage; the derived representation does not automatically inherit identical independent Authority/Governance State.
8. An authoritative Artifact quotes an unapproved Proposal: the quoted Proposal does not inherit Authority through containment.
9. A non-authoritative Artifact quotes an authoritative Decision: quotation does not transfer Authority to the quoting Artifact.
10. The same content is copied into another Project: preserve Project isolation and Provenance; copying does not transfer Project-scoped Authority.
11. Newest information contradicts an older approved Decision: recency alone does not resolve Conflict.
12. Many documents repeat one Proposal while one applicable authoritative Decision rejects it: popularity/repetition does not override governed Authority.
13. Two applicable Approved Claims materially conflict: preserve Conflict until applicable governance legitimately resolves it.
14. AI/model identifies a contradiction: it may produce an inferred/proposed Conflict relationship but cannot autonomously resolve Conflict or create governing Authority.
15. The Engine infers likely supersession from newer wording: preserve inferred/proposed supersession rather than established governed supersession.
16. A Decision supersedes another only within one scope: preserve prior applicability outside that scope and preserve history.
17. A historical request asks what governed at time T: use contemporaneously applicable state and distinguish later retrospective knowledge rather than rewriting history from current governance.
18. A Source disappears after prior observation: last-known evidence remains historical; disappearance does not make it current or false.
19. A Source is unavailable during the current request: represent Unavailable/Unknown consequences rather than absence.
20. Search finds no matching information: Missingness remains scoped to the established evidence boundary.
21. A Consumer lacks authorization for relevant information: Unauthorized/Undisclosable remains distinct from absent or Missing.
22. Identical Git object/content exists in two registered Sources: native/content identity does not silently merge semantic Source/Artifact identity.
23. A locator/path is later reused for an unrelated file: locator reuse does not establish Artifact continuity.
24. A file is renamed with strong native identity/history evidence: Artifact continuity may survive locator change where justified.
25. A persistence layer later assigns a database/row identifier: a physical storage key does not redefine semantic identity.
26. A future inference mechanism reports numeric confidence such as 0.99: confidence does not replace Provenance, Authority, Governance State, Conflict, Uncertainty, or governed epistemic state.

### Historical reconstruction test

The logical model is architecturally capable of representing “What did the Project legitimately know, and what governed it, at time T?” provided later persistence retains necessary governed states. Its representation basis includes Artifact/version/observation distinctions; Authority and Authority Scope; Governance State; Provenance/transformation lineage; temporal/effective/observation state; scoped supersession; Conflict; and Uncertainty and evidence limitations. Actual persistence obligations for historical reconstruction remain a Domain G concern.

### Technology-leakage check

Domain D selects no database, relational/physical schema, graph database, ORM, UUID scheme, hash identity scheme, vector representation, embedding model, semantic-equivalence algorithm, confidence algorithm, temporal database, event sourcing, serialization format, or persistence mechanism.

**D19 findings:** unresolved BLOCKER: 0; unresolved MATERIAL: 0; new MINOR findings: 0; unresolved MINOR: 0. The earlier D17 MINOR Context Item wording finding is resolved.

**D19 result:** **PASS — PROJECT OWNER APPROVED.**

## Domain D closing result

**Domain D — Context Knowledge Representation: COMPLETE — PROJECT OWNER APPROVED — PASS.** Final unresolved findings are BLOCKER: **0**; MATERIAL: **0**; MINOR: **0**.

Domain D is internally consistent with the Phase 0/1 baseline and approved Domains A–C. D1–D17 establish technology-independent logical identity; Project representation; Source and Source Scope representation; Artifact, Artifact Version/State, and observation separation; Claim semantic identity; task-relative Context Items; extensible Classification; explicit directed/scoped/provenance-bearing Relationships; scoped Authority and Authority Scope; Governance State and Candidate/Proposal lifecycle; Provenance and transformation lineage; temporal/currentness representation; historical and scoped supersession semantics; explicit Conflict; and structured Uncertainty/Unknown/missingness/epistemic state. D18 confirms requirements/conceptual-model traceability. D19 adversarial validation identifies no unresolved BLOCKER, MATERIAL, or MINOR finding.

Physical identifiers, schemas, persistence mechanisms, semantic-equivalence algorithms, and other implementation technologies remain intentionally undecided. Domains E–I are **COMPLETE — PROJECT OWNER APPROVED — PASS**. Phase 3 is **AUTHORIZED — NOT YET BEGUN**; Phase 4 remains **NOT AUTHORIZED**.
