# Phase 2 Checklist — Architecture & Technology Design

**Status:** **PROPOSED / NOT AUTHORIZED.** This is a pre-authorization planning artifact. Its existence does not authorize Phase 2 work, implementation, a next phase, or any material decision. Phase 0 and Phase 1 are complete; the Project Owner remains the final approving authority. Codex is not a material decision authority.

## Mission and completion condition

Phase 2 will define and validate the Context Engine architecture necessary to satisfy the approved Phase 0 and Phase 1 baseline; establish logical components, responsibilities, boundaries, interactions, state and information representations, security/governance enforcement points, failure behavior, and validation approach; and select only those technologies necessary to establish an implementation-ready v0.1 architecture.

It preserves governed Phase 1 semantics, compares reasonable architectural and technological alternatives before material selections, maintains requirements traceability, and produces sufficient design specificity for implementation to proceed without delegating material architecture decisions to the implementer. It does not implement the Context Engine, execute proving exercises, or expand v0.1 for potentially useful future technologies.

Phase 2 is complete only when the approved v0.1 architecture is sufficiently specified, traced, challenged, and validated that implementation can begin without unresolved material architecture, technology, security, governance, or scope decisions, and no unresolved BLOCKER or MATERIAL findings remain. Completion does not automatically authorize the next phase.

**Governing philosophy:** “Design generally. Implement narrowly.” Use the least sufficient architecture capable of satisfying approved requirements and proving v0.1.

## Classification, escalation, and findings

| Label | Meaning |
| --- | --- |
| `[PO]` | Material decision requiring explicit Project Owner approval. |
| `[DG]` | Design work within an already approved material boundary. |
| `[VAL]` | Validation/review activity. |
| `[GATE]` | Formal governance checkpoint requiring Project Owner disposition. |

Codex may inspect the repository, analyze approved requirements, draft documentation, apply explicitly approved decisions, perform mechanical consistency updates, execute approved validation procedures, and make ordinary non-material documentation/design choices within established boundaries. Codex must stop and escalate rather than decide when a material architecture, technology, security, governance, or scope decision is missing; approved decisions conflict; an approved design appears infeasible; a materially different decision is required; multiple materially different viable designs arise during `[DG]` work; or proceeding would change requirements, semantics, dependencies, security behavior, Source/Consumer contracts, persistence strategy, or phase boundaries.

Finding severity is **BLOCKER**, **MATERIAL**, **MINOR**, or **OBSERVATION**. Phase 2 exit requires unresolved BLOCKER findings: **0**, and unresolved MATERIAL findings: **0**. A material unresolved architecture issue is not acceptable merely because it is labeled “deferred.”

## Scope guardrails

Phase 2 will not:

- implement production or v0.1 application functionality; build, deploy, or operate a runtime; perform production-scale Source ingestion; or execute either proving exercise;
- expand v0.1 Source coverage merely because future Source types are possible, or establish universal Source/document/Consumer/provider support;
- introduce vector/embedding retrieval, graph databases/knowledge graphs, autonomous agents, cloud infrastructure, GUI/web applications, enterprise IAM/SSO, real-time/event-driven ingestion, or similar capabilities without independently demonstrated requirements;
- select technologies before architecture requirements and evaluation criteria exist, or optimize for enterprise scale, HA, or distributed operation without requirements;
- redefine or weaken Phase 0/1 semantics, delegate material decisions to Codex, automatically modify authoritative Sources, or retrieve, store, expose, or manage secrets as Context Engine content;
- treat observed local Git state as inherently verified remote/shared/governing/current state, infer sufficiency merely because registered Sources were searched, or silently combine materially incompatible observations during package construction.

## Pre-authorization Domain A baseline

**PRE-AUTHORIZATION PLANNING BASELINE — PROJECT OWNER APPROVED — PENDING FORMAL ADOPTION UPON PHASE 2 AUTHORIZATION.** A1–A14 are not ordinary Phase 2 work already completed. The first governance action after any future Phase 2 authorization must formally adopt this approved Domain A baseline into the governed Phase 2 baseline. Do not redo Domain A merely because it preceded authorization.

| ID | Approved planning objective/outcome | Status |
| --- | --- | --- |
| A1 | Establish architectural design principles, preserving AP-01 through AP-12. | Approved pre-authorization baseline; pending formal adoption |
| A2 | Define the Context Engine system boundary. | Approved pre-authorization baseline; pending formal adoption |
| A3 | Identify external actors, systems, and trust relationships. | Approved pre-authorization baseline; pending formal adoption |
| A4 | Define major system responsibilities. | Approved pre-authorization baseline; pending formal adoption |
| A5 | Define major responsibility separations, preserving SEP-01 through SEP-07. | Approved pre-authorization baseline; pending formal adoption |
| A6 | Establish the Phase 0/1 Architecture Constraint Register, AC-01 through AC-19. | Approved pre-authorization baseline; pending formal adoption |
| A7 | Develop candidate architectural styles: AS-1 Modular Single-Process; AS-2 Layered Modular; AS-3 Ports-and-Adapters / Hexagonal; AS-4 Process-Separated Components. | Approved pre-authorization baseline; pending formal adoption |
| A8 | Evaluate architectural styles against CR-01 through CR-12 approved criteria. | Approved pre-authorization baseline; pending formal adoption |
| A9 | Select the approved v0.1 direction: modular single-process ports-and-adapters architecture. | Approved pre-authorization baseline; pending formal adoption |
| A10 | Define conceptual component boundaries, CC-01 through CC-07. | Approved pre-authorization baseline; pending formal adoption |
| A11 | Define high-level processing, control, and data flows, including the governed iterative context-construction cycle. | Approved pre-authorization baseline; pending formal adoption |
| A12 | Define architectural extension boundaries, EB-01 through EB-04, including XC-01 Identity/Provenance/Lineage and XC-02 Audit/Explanation/Failure State. | Approved pre-authorization baseline; pending formal adoption |
| A13 | Define portability/deployment constraints, PD-01 through PD-06. | Approved pre-authorization baseline; pending formal adoption |
| A14 | Validate Domain A against Phase 0/1 and approved Phase 2 planning constraints. | **PASS**; pending formal adoption |

The detailed wording of the approved pre-authorization Domain A registers and decisions must be documented in governed Phase 2 architecture records during formal adoption. The checklist preserves their approved identifiers and outcomes and must not be treated as a substitute for those detailed records. Formal adoption must preserve the Project Owner-approved planning baseline without introducing new material decisions.

## Proposed checklist

All items below are **PENDING — PHASE 2 NOT AUTHORIZED** unless and until separately authorized. `[PO]` and `[GATE]` labels retain their stated approval/disposition requirements after authorization.

### Domain B — Governance, Trust & Security Architecture

| ID | Objective | Classification |
| --- | --- | --- |
| B1 | Derive Domain B architectural requirements and constraints. | [DG] |
| B2 | Define governance establishment, interpretation, and enforcement boundaries. | [DG] |
| B3 | Establish Governance Bootstrap capability and non-circular trust requirements. | [DG] |
| B4 | Develop and compare Governance Bootstrap alternatives. | [DG] |
| B5 | Select v0.1 Governance Bootstrap architecture. | [PO][GATE] |
| B6 | Define Authority, Authority Scope, Governance State, and applicable-governance evaluation architecture. | [DG] |
| B7 | Define Requester/Consumer authorization architecture and enforcement points. | [DG] |
| B8 | Define Project isolation and governed cross-Project security boundaries. | [DG] |
| B9 | Define sensitive-information handling architecture. | [DG] |
| B10 | Define secret-exclusion architecture. | [DG] |
| B11 | Define untrusted-content/governing-instruction separation. | [DG] |
| B12 | Define deterministic-enforcement boundaries. | [DG] |
| B13 | Define security-relevant audit and explanation requirements. | [DG] |
| B14 | Define security/governance failure and degraded-operation behavior. | [DG] |
| B15 | Perform Domain B traceability and consistency review. | [VAL] |
| B16 | Perform Domain B security/governance architecture review and resolve findings. | [VAL][GATE] |

### Domain C — Source & Observation Architecture

**Boundary:** Domain C establishes observation-state evidence. It does not determine final task sufficiency or package coherence.

| ID | Objective | Classification |
| --- | --- | --- |
| C1 | Derive Domain C requirements and constraints. | [DG] |
| C2 | Define Project registration. | [DG] |
| C3 | Define Source registration, identity, Source Scope, and Project association. | [DG] |
| C4 | Define governance and authorization interaction. | [DG] |
| C5 | Define Applicable Source Universe and evidence-boundary interaction. | [DG] |
| C6 | Define the general Source Adapter contract. | [DG] |
| C7 | Obtain Project Owner approval of the Source Adapter architecture. | [PO][GATE] |
| C8 | Define local Git Source behavior, including identity and material Git-native state. | [DG] |
| C9 | Define Observed Source State and its epistemic-strength boundary. | [DG] |
| C10 | Define Markdown Artifact handling. | [DG] |
| C11 | Define structured-metadata necessity requirements without selecting format or storage. | [DG] |
| C12 | Define Source observation temporal, availability, failure, and last-known-state behavior. | [DG] |
| C13 | Preserve security, sensitivity, secret-exclusion, and untrusted-content boundaries. | [DG] |
| C14 | Define Source extensibility proof criteria. | [DG] |
| C15 | Perform traceability and consistency review. | [VAL] |
| C16 | Perform adversarial v0.1 Source-boundary validation. | [VAL][GATE] |

### Domain D — Context Knowledge Representation

No Domain D item creates a database schema, ORM model, DDL, migration, or physical storage schema.

| ID | Objective | Classification |
| --- | --- | --- |
| D1 | Derive Domain D requirements. | [DG] |
| D2 | Define logical identity principles. | [DG] |
| D3 | Define Project representation. | [DG] |
| D4 | Define Source and Source Scope representation. | [DG] |
| D5 | Define Artifact and Artifact Version/Observed State representation. | [DG] |
| D6 | Define Claim representation. | [DG] |
| D7 | Define Context Item representation. | [DG] |
| D8 | Define Classification representation. | [DG] |
| D9 | Define Relationship representation. | [DG] |
| D10 | Define Authority and Authority Scope representation. | [DG] |
| D11 | Define Governance State and Candidate/Proposal lifecycle representation. | [DG] |
| D12 | Define Provenance and transformation lineage representation. | [DG] |
| D13 | Define temporal and currentness representation. | [DG] |
| D14 | Define supersession and historical-context representation. | [DG] |
| D15 | Define Conflict representation. | [DG] |
| D16 | Define Uncertainty, Unknown, missingness, and epistemic-state representation. | [DG] |
| D17 | Conduct integrated logical-representation review and obtain Project Owner approval. | [PO][GATE] |
| D18 | Perform requirements/conceptual-model traceability review. | [VAL] |
| D19 | Perform adversarial semantic-representation review. | [VAL][GATE] |

### Domain E — Discovery, Selection & Sufficiency

No retrieval technology may be selected before capability criteria are approved.

| ID | Objective | Classification |
| --- | --- | --- |
| E1 | Derive Domain E requirements. | [DG] |
| E2 | Operationalize Context Request, Task Intent, and Task Scope. | [DG] |
| E3 | Define discovery responsibility boundaries. | [DG] |
| E4 | Define discovery/retrieval capability requirements and evaluation criteria. | [DG] |
| E5 | Develop candidate discovery/retrieval alternatives. | [DG] |
| E6 | Select v0.1 discovery/retrieval architecture. | [PO][GATE] |
| E7 | Define candidate-context representation. | [DG] |
| E8 | Define applicability evaluation: relevance, Authority, Governance State, currentness, relationships, Conflict, Uncertainty, provenance, and authorization. | [DG] |
| E9 | Define Required versus Supporting Context. | [DG] |
| E10 | Define Context Selection and material explanation. | [DG] |
| E11 | Define sufficiency-state architecture. | [DG] |
| E12 | Define Applicable Source Universe/evidence-boundary interaction. | [DG] |
| E13 | Define bounded iteration and termination. | [DG] |
| E14 | Define inaccessible or undisclosable Required Context behavior. | [DG] |
| E15 | Conduct integrated Project Owner review. | [PO][GATE] |
| E16 | Perform traceability and consistency review. | [VAL] |
| E17 | Perform adversarial discovery, negative-result, and sufficiency review. | [VAL][GATE] |

### Domain F — Context Package & Consumer Architecture

No serialization, prompt template, API, package storage, or file format is selected here.

| ID | Objective | Classification |
| --- | --- | --- |
| F1 | Derive Domain F requirements. | [DG] |
| F2 | Define logical Context Package identity and request, project, and task association. | [DG] |
| F3 | Define Required/Supporting package structure. | [DG] |
| F4 | Define Source manifest and provenance. | [DG] |
| F5 | Define package representation of material Authority, Governance, currentness, Conflict, Uncertainty, gap, and sufficiency qualifications. | [DG] |
| F6 | Define Construction-State Coherence evaluation and incoherence behavior. | [DG] |
| F7 | Define package-construction record for explanation, audit, and reproducibility. | [DG] |
| F8 | Define Consumer contract. | [DG] |
| F9 | Define Human rendering. | [DG] |
| F10 | Define ChatGPT rendering. | [DG] |
| F11 | Define Codex rendering. | [DG] |
| F12 | Define logical-package, rendering, delivery, receipt, and use distinction. | [DG] |
| F13 | Define Consumer-capacity and rendering-limitation behavior. | [DG] |
| F14 | Conduct integrated Project Owner review. | [PO][GATE] |
| F15 | Perform traceability and semantic-consistency review. | [VAL] |
| F16 | Perform adversarial coherence, rendering, provenance, and receipt review. | [VAL][GATE] |

### Domain G — State, Persistence & Operational Architecture

Requirements and capability baselines are approved before persistence technology selection. No test framework is selected in this domain.

| ID | Objective | Classification |
| --- | --- | --- |
| G1 | Derive Domain G requirements. | [DG] |
| G2 | Define logical-state inventory and classification. | [DG] |
| G3 | Define persistent versus transient/reconstructable state. | [DG] |
| G4 | Define lifecycle, retention, and history requirements. | [DG] |
| G5 | Define persistence security, isolation, and sensitive-information requirements. | [DG] |
| G6 | Define consistency, integrity, and atomicity requirements. | [DG] |
| G7 | Define concurrency, retry, and idempotency requirements. | [DG] |
| G8 | Define failure-state preservation and recovery. | [DG] |
| G9 | Define backup/recovery capability requirements where justified. | [DG] |
| G10 | Define observability and measurability requirements. | [DG] |
| G11 | Define audit-state persistence requirements. | [DG] |
| G12 | Define v0.1 testability/validation architecture: test seams, controllable Source observations, failure simulation/injection needs, reproducible fixtures, and unit/component/integration/proving distinctions. | [DG] |
| G13 | Derive persistence capability requirements. | [DG] |
| G14 | Obtain Project Owner approval of the persistence/state capability baseline. | [PO][GATE] |
| G15 | Define v0.1 runtime/deployment operational requirements. | [DG] |
| G16 | Perform traceability and consistency review. | [VAL] |
| G17 | Perform failure, recovery, and persistence adversarial review. | [VAL][GATE] |

### Domain H — Technology Selection & v0.1 Physical Design

No selected technology may be installed, initialized, scaffolded, or deployed in Phase 2.

| ID | Objective | Classification |
| --- | --- | --- |
| H1 | Establish technology-selection standard. | [DG] |
| H2 | Create technology decision inventory. | [DG] |
| H3 | Classify decisions by materiality and approval requirement. | [DG] |
| H4 | Derive language/runtime requirements and criteria. | [DG] |
| H5 | Compare/select language/runtime. | [PO][GATE] |
| H6 | Derive persistence/storage technology requirements from approved G baseline. | [DG] |
| H7 | Compare/select persistence/storage mechanism(s). | [PO][GATE] |
| H8 | Derive structured-metadata/interchange/serialization requirements. | [DG] |
| H9 | Compare/select required metadata/serialization mechanisms. | [PO][GATE] |
| H10 | Derive local Git interaction requirements. | [DG] |
| H11 | Compare/select Git interaction mechanism. | [PO][GATE] |
| H12 | Derive Markdown-processing requirements. | [DG] |
| H13 | Compare/select Markdown-processing mechanism. | [PO][GATE] |
| H14 | Identify additional libraries, frameworks, infrastructure, and testing technologies actually required. | [DG] |
| H15 | Evaluate/approve material additional dependencies individually. | [PO][GATE] |
| H16 | Select application packaging/execution mechanism. | [PO][GATE] |
| H17 | Select least-sufficient v0.1 deployment mechanism/environment. | [PO][GATE] |
| H18 | Produce integrated v0.1 physical architecture. | [DG] |
| H19 | Perform dependency-direction and semantic-leakage review. | [VAL] |
| H20 | Perform technology-specific security/dependency review. | [VAL] |
| H21 | Perform technology-to-requirement/architecture traceability. | [VAL] |
| H22 | Perform integrated physical-architecture review and resolve material findings. | [VAL][GATE] |

### Domain I — Validation, Proving Architecture & Exit Gate

The proving plans in I10–I12 are designs only; they do not execute the Company AI Roadmap or Context Engine dogfooding exercises.

| ID | Objective | Classification |
| --- | --- | --- |
| I1 | Reconcile complete Phase 2 decision inventory. | [VAL] |
| I2 | Complete traceability for all 46 CE-FRs and 32 CE-NFRs. | [VAL] |
| I3 | Trace material Phase 1 conceptual/adversarial semantics into Phase 2. | [VAL] |
| I4 | Validate all 12 Phase 0 success criteria. | [VAL] |
| I5 | Audit all 23 Phase 0 non-goal categories for leakage. | [VAL] |
| I6 | Perform integrated architecture consistency review. | [VAL] |
| I7 | Perform integrated security/governance review. | [VAL] |
| I8 | Perform integrated failure/degraded-operation review. | [VAL] |
| I9 | Perform auditability/provenance/historical-reconstruction/reproducibility review. | [VAL] |
| I10 | Design Company AI Roadmap proving-ground implementation/acceptance plan without executing it. | [DG] |
| I11 | Design Context Engine dogfooding implementation/acceptance plan without executing it. | [DG] |
| I12 | Validate proving plans for fresh Consumers, meaningful continuation, and no project-specific core behavior. | [VAL] |
| I13 | Perform implementation-readiness review, specifically whether Codex/implementers would still need to invent material decisions. | [VAL] |
| I14 | Conduct formal `/grill-me` adversarial review. | [VAL][GATE] |
| I15 | Resolve/disposition adversarial findings under Project Owner governance. | [PO][GATE] |
| I16 | Perform focused material-findings disposition audit. | [VAL] |
| I17 | Perform formal Phase 2 exit-gate audit and issue PASS/FAIL recommendation. | [VAL][GATE] |
| I18 | Project Owner separately decides whether to close Phase 2 and whether to authorize the next phase. | [PO][GATE] |

## Traceability and exit record

Future Phase 2 documentation must trace each material design decision and validation result to the approved Phase 0/1 baseline, including all 46 CE-FRs, all 32 CE-NFRs, the 12 Phase 0 success criteria, the 23 Phase 0 non-goal categories, and material conceptual/adversarial semantics (including Governance Bootstrap, Applicable Source Universe, Observed Source State, and Construction-State Coherence). Traceability may explain approved decisions; it does not create authority or silently change governed semantics.

The Phase 2 exit record must state the unresolved BLOCKER and MATERIAL totals, record Project Owner dispositions, and keep phase closure separate from next-phase authorization. Until explicit Project Owner authorization, every proposed item above remains pending and Phase 2 remains **NOT AUTHORIZED**.
