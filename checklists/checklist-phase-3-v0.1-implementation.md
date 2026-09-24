# Phase 3 Master Checklist — v0.1 Implementation

**Status:** **AUTHORIZED — IMPLEMENTATION PLAN PROJECT OWNER APPROVED; WORKSTREAMS 1–8 COMPLETE — PROJECT OWNER APPROVED; GATES 3A — SEMANTIC FOUNDATION, 3B — EVIDENCE PIPELINE, AND 3C — GOVERNED CONTEXT PIPELINE APPROVED; TD-14 CLOSED / NOT REOPENED; WORKSTREAM 9 NOT AUTHORIZED; WORKSTREAM 10 NOT AUTHORIZED; GATE 3D NOT YET REACHED.** H3-WS1-01 remains resolved. This is the approved controlling implementation plan for Phase 3, subordinate to the approved Phase 0–2 record, including the Phase 2 closure decision in commit `ac22ed1`. Phase 4 — Validation & Integration remains **NOT AUTHORIZED**.

## Purpose, authority, and boundaries

Phase 3 implements the approved v0.1 design as an installable application and validates that implementation against the approved design. It does not redesign the governed baseline, execute the Company AI Roadmap proving exercise or Context Engine dogfooding exercise, establish Phase 4 completion, or authorize a later phase.

The Project Owner remains the final approving authority for material decisions. This checklist uses these labels:

| Label | Meaning |
| --- | --- |
| `[IMP]` | Implementation work within the approved Phase 0–2 boundary. |
| `[VAL]` | Implementation-level validation; code existence alone is not completion. |
| `[DOC]` | Traceability, checklist, or implementation-documentation evidence. |
| `[GATE]` | Substantive Project Owner review/disposition point. |
| `[H3]` | A likely materiality/escalation point; stop when triggered. |

**H3 remains controlling.** Codex may make ordinary non-material implementation and documentation choices within the approved architecture. Codex must stop and report—not silently decide—if a choice materially changes scope, architecture, technology, security, governance, data models, dependencies, persistence strategy, semantic behavior, Source/Consumer contract, or phase boundary; if approved records conflict; if the design appears infeasible; or if genuine material ambiguity remains.

**Bulk implementation authorization rule.** Project Owner approval may authorize an entire workstream or defined implementation increment. Individual checklist items within that approved scope do not require separate Project Owner approval unless an item reaches a designated Project Owner Gate or triggers H3. Codex may complete ordinary non-material implementation decisions within the authorized increment and should return the completed increment with implementation, test, documentation, checklist, and unresolved-finding evidence for review.

### Controlling baseline and non-negotiable implementation boundaries

Implement the approved modular single-process ports-and-adapters architecture, governed core semantics independent of physical mechanisms, and least-sufficient design. Preserve `Operator -> CLI -> application services -> core domain -> ports -> adapters/environment`, with core semantics independent of SQL/SQLite rows, Git commands, TOML syntax, Markdown parser tokens, Linux paths, and CLI syntax.

- Use the approved Python/CPython 3.14 release line; installable package, `pyproject.toml`, `src/context_engine/`, CPython virtual environment, and console/CLI entry point. No CLI framework is selected.
- Use SQLite through CPython `sqlite3` behind EB-03, with application-owned deterministic schema evolution/migrations and semantic transaction boundaries. Application state is outside registered Sources by default; backups use SQLite-supported consistent capability.
- Use TOML 1.0.0 through `tomllib`; Bootstrap is independently supplied through an explicit CLI/application reference. There is no implicit Bootstrap discovery from current directory, repository, home directory, nearby Source, or ordinary content. An authorized operator's deliberate explicit reference is the root legitimacy event; validation is deterministic and does not make the reference self-authorizing.
- Use native Git CLI only through shell-free CPython `subprocess` argument vectors; no GitPython or pygit2. Local Git state is observation evidence, not automatic proof of remote/shared/governing/current state.
- Use `markdown-it-py` 4.x with CommonMark and approved table support. Preserve original Markdown as Source evidence. Parser structure creates no Claim, Authority, Governance State, relevance, selection, or sufficiency.
- Implement Deterministic Foundation + Bounded Semantic Assistance. v0.1 deterministic discovery requires no LLM, embeddings, vector database/index, or semantic-search technology. A material deterministic-discovery deficiency must record evidence and reopen TD-14 under governance; do not add AI technology silently.
- Use pytest 9.x. No pytest plugin is automatically approved. The initial runtime is an ordinary non-root, on-demand process on a direct local Linux x86-64 host (Ubuntu initial environment): no container, VM, cloud, daemon/service, HA, or mandatory runtime network dependency.
- Use Python-native diagnostic logging; logs are not durable governed audit. Exclude secret values from normal Context Engine content/state. Safety-critical governance/security enforcement requires deterministic enforcement capability.

The semantic distinctions below are invariant across every workstream: Source observation != interpretation; represented information != Candidate Context != selected Context Item; discovery != applicability != selection != sufficiency; Authority != Governance State; Requester authorization != Consumer disclosure authorization; historical state != current state; persistence/restoration does not establish currentness or Authority; Required Context cannot be waived for Consumer capacity; Conditional Sufficiency does not waive Required Context; Applicable Source Universe (ASU) participates in sufficiency; and logical Context Package != rendering != delivery != receipt != use. Package construction preserves material Provenance, Conflict, Uncertainty, limitations, sufficiency, and Construction-State Coherence. Source-derived imperative/instruction-like content remains Source content unless governance independently establishes instructional applicability. Project isolation is default; cross-Project traversal is bounded and governed; Authority is scoped; required failures fail closed.

## Execution model and evidence

Use vertical increments: executable foundation -> semantic foundation -> Bootstrap/configuration/persistence -> Project/Source lifecycle -> Source observation/representation -> deterministic discovery -> applicability/governance/selection -> sufficiency -> logical Context Package -> rendering -> CLI/application orchestration -> operational hardening -> Phase 3 exit. Each increment must leave a testable path through the boundaries it touches; do not build isolated layers and postpone integration to the end.

Testing accompanies implementation. Select test seams and fixtures that establish actual governed semantics; preserve the distinction between unit, semantic/invariant, component, adapter, persistence/migration, implementation-oriented integration, controlled end-to-end, and future proving tests. A test fixture has no production authority. Record tests, results, traceability, limitations, failures, and operational evidence alongside the increment.

Expected completion evidence generally includes: implemented boundary/behavior; passing relevant tests; documented non-material choices; updated checklist status; requirements/architecture traceability; known limitations; and a finding inventory. Do not execute proving exercises or use a genuine fresh Consumer merely to complete Phase 3 implementation work. The proving-integrity preflight and fresh-Consumer contamination requirements apply when the separately authorized future proving exercises occur.

## Stage I — Implementation Foundation

### Workstream 1 — Repository, Package, and Executable Skeleton

**Objective:** Establish the approved, minimal executable and test foundation without embedding governed semantics in infrastructure.

**Dependencies:** Project Owner authorization of this workstream/increment; Phase 0–2 baseline.

**Implementation status:** **COMPLETE — VALIDATED.** The clean CPython 3.14 environment install, installed console entry point, readiness/unavailable-prerequisite behavior, ordinary non-root direct-host assumptions, dependency-direction checks, and complete pytest suite pass. H3-WS1-01 is resolved. The approved `markdown-it-py` declaration remains unused pending authorized Markdown work. See [Workstream 1 implementation record](../docs/phase-3/workstream-1-repository-package-executable-skeleton.md).

- [x] 1.1 [IMP] Create the approved standard installable Python package structure, `pyproject.toml`, `src/context_engine/`, test layout, and console entry point using only approved dependencies and packaging boundaries.
- [x] 1.2 [IMP] Establish a minimal CLI/application invocation path with explicit arguments, prerequisite/readiness reporting, clean termination, and safe diagnostics; do not select a CLI framework.
- [x] 1.3 [IMP] Establish dependency-direction rules and ports/adapters seams so core code does not import or depend on concrete CLI, SQLite, Git, TOML, Markdown, or host mechanisms.
- [x] 1.4 [IMP] Establish test execution, deterministic fixtures, temporary-state isolation, and development/runtime dependency separation using pytest 9.x; do not introduce plugins without governance review.
- [x] 1.5 [VAL] Test package installation, console invocation, ordinary non-root operation, clean unavailable-prerequisite behavior, and direct-host assumptions without creating a runtime service or network dependency.
- [x] 1.6 [VAL] Test boundary dependency direction and that no installation/configuration path establishes governance, Authority, or currentness.
- [x] 1.7 [DOC] Record exact non-material package/build choices, supported prerequisite assumptions, and Workstream 1 test evidence.

**H3 points:** Any packaging/build backend, dependency, CLI framework, host/runtime expansion, or deployment mechanism beyond approved boundaries.

**Completion evidence:** Installable skeletal application, focused tests, and no semantic/governance behavior smuggled into infrastructure.

### Workstream 2 — Governed Semantic Kernel

**Objective:** Implement the technology-independent domain representations, invariants, and ports necessary to preserve approved Phase 1–2 semantics.

**Dependencies:** Workstream 1.

- [x] 2.1 [IMP] Implement core representations and validation for Project; Source/Source Scope; Artifact and Artifact Version/Observed State; Claim; Classification; Relationship; Authority/Authority Scope; Governance State; Candidate/Proposal; Provenance/transformation lineage; temporal/currentness; supersession/history; Conflict; and Uncertainty/Unknown/missingness.
- [x] 2.2 [IMP] Implement Context Request, Task Intent/Scope, Requester/Consumer distinctions, represented information, Candidate Context, selected Context Item, Required/Supporting state, sufficiency outcomes, logical Context Package, Source Manifest, and Package-Construction Record as distinct semantic concepts.
- [x] 2.3 [IMP] Establish core ports/contracts for governance, persistence, Source observation, representation, discovery, authorization/disclosure, package construction, rendering, diagnostics, backup/recovery, and clock/identity seams as applicable.
- [x] 2.4 [IMP] Encode invariant-preserving construction and validation so physical identifiers, parser tokens, observations, transformations, and persistence restoration cannot elevate Authority, Governance State, currentness, or selection status.
- [x] 2.5 [VAL] Add unit and semantic/invariant tests for scoped Authority, Authority != Governance State, Claim identity, Candidate/Proposal separation, historical/current separation, Provenance lineage, Conflict/Uncertainty preservation, and Project isolation.
- [x] 2.6 [VAL] Add negative tests that reject semantic collapse: represented information becoming Context Item without selection; discovery becoming applicability/selection; a newer/local/restored item becoming current/authoritative; or Source content becoming governance/instruction.
- [x] 2.7 [DOC] Trace kernel concepts to Phase 1 model and Phase 2 Domains A, B, and D; record deliberate deferred physical choices.

**Implementation status:** **COMPLETE — PROJECT OWNER APPROVED.** See [Workstream 2 kernel record](../docs/phase-3/workstream-2-governed-semantic-kernel.md). Gate 3A is approved; Workstream 3 remains not authorized.

**H3 points:** A core semantic inconsistency, a data-model change that alters governed meaning, or a missing material representation.

**Completion evidence:** Tested kernel that can express all material distinctions without binding to storage or adapters.

### Gate 3A — Semantic Foundation [GATE]

**Entry:** Workstream 2 completion evidence and traceability are available.

**Project Owner review:** Confirm that approved Phase 1–2 semantics map faithfully into code, core/adapter separation is intact, and no material semantic or architecture decision was invented.

**Disposition:** **APPROVED — PROJECT OWNER.** The Project Owner accepts the implemented Workstream 2 semantic foundation as the basis for subsequent authorized Phase 3 implementation: Phase 1–2 semantics map acceptably into the kernel; core/adapter separation is intact; identity is not physically defined; Authority and Governance State remain distinct; pipeline, authorization/disclosure, temporal/currentness, package/rendering/delivery/receipt/use, Provenance, Conflict, Uncertainty, limitations, sufficiency, and coherence distinctions remain representable; and no material semantic or architecture decision was invented. This disposition does not claim later behavior is implemented, authorize Workstream 3, close Phase 3, or authorize Phase 4.

### Workstream 3 — Bootstrap, Configuration, and Persistence Foundation

**Objective:** Implement governed startup/configuration, durable state, migrations, audit distinction, and recoverable persistence without granting trust through mechanism.

**Dependencies:** Gate 3A approval; Workstreams 1–2.

- [x] 3.1 [IMP] Implement explicit Bootstrap-reference intake at the CLI/application boundary and deterministic Bootstrap parsing/validation through TOML/`tomllib`: supported version, structure, internal consistency, scope, and downstream governance semantics.
- [x] 3.2 [IMP] Implement root-legitimacy handling: authorized operator + deliberate explicit reference is the root event; no implicit discovery/default/redirect from location or ordinary Source content; fail closed when governance establishment is required but invalid/unavailable/unauthorized.
- [x] 3.3 [IMP] Implement separately scoped Project configuration loading/validation and provenance without merging Project configuration trust with Bootstrap trust or treating valid TOML as valid governance.
- [x] 3.4 [IMP] Implement EB-03 SQLite adapter, deterministic application-owned schema evolution/migrations, startup compatibility checks, and semantic transaction boundaries for coupled governed state.
- [x] 3.5 [IMP] Implement durable state/audit records, with audit distinct from diagnostic logs; preserve failed/denied/interrupted/partial outcomes and avoid secret values in normal state, logs, audit, or backups.
- [x] 3.6 [IMP] Implement Project isolation at persistence boundaries and controlled paths for governed cross-Project relationships/traversal.
- [x] 3.7 [VAL] Add Bootstrap and configuration negative tests: missing/invalid/unsupported/malformed reference, unauthorized operator, scope/consistency failure, implicit-discovery attempt, and untrusted Source-content instruction.
- [x] 3.8 [VAL] Add SQLite component and migration tests: fresh initialization, ordered upgrade, incompatible schema/failure behavior, transaction rollback/partial-state visibility, persistence/restart, Project isolation, and audit-write failure consequence.
- [x] 3.9 [VAL] Test that restoration preserves historical evidence without asserting currentness or Authority; test secret exclusion and authorization-bound protected metadata/audit access.
- [x] 3.10 [DOC] Record schema-evolution policy, migration evidence, config/Bootstrap boundary, durable-state classification, and known recovery limitations.

**Implementation status:** **COMPLETE — PROJECT OWNER APPROVED.** See [Workstream 3 record](../docs/phase-3/workstream-3-bootstrap-configuration-persistence.md). Gate 3B remains pending and unapproved; Workstream 4 is not authorized.

**H3 points:** Any change to Bootstrap legitimacy/security semantics, persistence technology, migration/recovery behavior that changes governed meaning, new crypto/auth/IAM need, or need for a new dependency.

## Stage II — Evidence Pipeline

### Workstream 4 — Project and Source Lifecycle

**Objective:** Implement governed Project and Source registration/lifecycle, scope, authorization, and ASU foundation.

**Dependencies:** Workstream 3 and applicable Gate 3A disposition.

- [x] 4.1 [IMP] Implement Project identity/lifecycle and Source registration identity, type/capabilities, association, Source Scope, governed relationships, and status/history without equating registration/access with Authority or disclosure authorization.
- [x] 4.2 [IMP] Implement governed effective-scope calculation from Project/Source scope, relationships, task scope, and Requester/Consumer authorization; default to isolation and bounded explicitly governed cross-Project traversal.
- [x] 4.3 [IMP] Implement ASU representation and establishment basis, distinct from registered Source set and observed Source set; represent adequate, known-incomplete, and indeterminate evidence boundaries.
- [x] 4.4 [IMP] Implement lifecycle failure/availability states that preserve unavailable, inaccessible, unauthorized, unsupported, partial, and absent distinctions.
- [x] 4.5 [VAL] Add component tests for multi-Project isolation, scoped Authority, cross-Project denial/allowed governed relationship, Source scope narrowing, and authorization versus Consumer disclosure distinction.
- [x] 4.6 [VAL] Add negative tests that reject registration/access as Authority, global traversal by default, and a registered-only search as proof of ASU adequacy.
- [x] 4.7 [DOC] Trace Source lifecycle and ASU behavior to Domains B/C/E and record supported v0.1 limits.

**Implementation status:** **COMPLETE — PROJECT OWNER APPROVED.** Workstream 4 supplies the Project/Source lifecycle and ASU foundation only. Gate 3B remains pending and unapproved. Workstream 5 and later remain unauthorized. See [Workstream 4 record](../docs/phase-3/workstream-4-project-source-lifecycle.md).

### Workstream 5 — Source Observation, Transformation, Representation, and Provenance

**Objective:** Create the controlled evidence path from governed Sources through observations and Markdown representation to provenance-bearing represented information.

**Dependencies:** Workstream 4; SQLite/configuration foundation.

- [x] 5.1 [IMP] Implement the general read-oriented Source Adapter contract and local Git adapter using native Git CLI with shell-free `subprocess` argument vectors, controlled environment, bounded output, and explicit failure handling.
- [x] 5.2 [IMP] Implement governed local Git observation for repository identity, revision/HEAD, branch/equivalent state, relevant working-tree state, relevant history, and material limitations (including detached/unborn/shallow/partial/unavailable/divergent/path ambiguity states as applicable).
- [x] 5.3 [IMP] Preserve Observed Source State and time/provenance separately from assertions of remote/shared/governing/current state; observe local state only and introduce no network/provider integration.
- [x] 5.4 [IMP] Implement Markdown Artifact observation and deterministic `markdown-it-py` transformation with CommonMark plus approved table support, original-content preservation, hierarchy/block-line provenance, inert parsing, and explicit unsupported/failure states.
- [x] 5.5 [IMP] Implement provenance-bearing represented information and transformation lineage from observation/Artifact state while keeping parser output, normalization, and Source text distinct from Claims and governance conclusions.
- [x] 5.6 [IMP] Persist material observations, versions, transformation outcomes, limitations, and historical evidence without claiming stable/current Source state after later change or recovery.
- [x] 5.7 [VAL] Add adapter tests using controlled Git fixtures: clean/dirty, staged/untracked, detached/unborn, history limitation, mutation during observation, unavailable Git/path, unusual/NUL-safe path handling, and hostile/untrusted repository conditions within approved scope.
- [x] 5.8 [VAL] Add Markdown tests for headings, paragraphs, lists, code, links, tables, Unicode, malformed/unsupported cases, raw/instruction-like content, original-to-derived provenance, and parser configuration repeatability.
- [x] 5.9 [VAL] Add provenance/representation tests proving observation != interpretation; original evidence survives; transformations preserve limitations; and local Git facts do not establish remote/current/governing truth.
- [x] 5.10 [DOC] Record supported observation inventory, Git/Markdown version/configuration evidence, transformation rules, unsupported capability behavior, and provenance traceability.

**H3 points:** Git capability requiring a library/network/provider, a Markdown feature/plugin/dependency, an interpretation rule that establishes Claim/governance, or material Source contract expansion.

**Implementation status:** **COMPLETE — PROJECT OWNER APPROVED.** See [Workstream 5 record](../docs/phase-3/workstream-5-source-observation-representation.md). Gate 3B is approved; Workstream 6 is complete and Project Owner approved; Workstream 7 remains unauthorized and unbegun; Workstreams 8–10 remain unauthorized; Gate 3C has not been reached or approved; Phase 4 remains unauthorized.

### Gate 3B — Evidence Pipeline [GATE]

**Entry:** A tested controlled path exists from explicit Bootstrap through Project/Source lifecycle, authorized observation/transformation, represented information, and durable Provenance.

**Project Owner review:** Confirm evidence honesty, Bootstrap/root legitimacy, Source/Project isolation, parser/Git boundaries, persistence integrity, and that observation/representation has not been promoted into governance or selection.

**Disposition:** **APPROVED — PROJECT OWNER.** For the implemented Workstreams 1–5 scope, the Project Owner accepts the tested controlled evidence path from explicit Bootstrap through governed Project, registered Source, authorized Source observation, transformation, represented information, and durable Provenance. The approval accepts the recorded Bootstrap/root-legitimacy, Project-isolation, Source-registration/observation, local read-oriented shell-free bounded non-mutating Git, local-evidence limitation, original-Markdown, inert-parser, Source-content/instruction, representation-stage separation, Provenance/limitation, historical-reload, and semantic-identity evidence. It establishes no discovery, applicability, selection, sufficiency, Context Package construction, Workstream 6 authorization, Gate 3C disposition, or Phase 4 authorization.

## Stage III — Context Decision Pipeline

### Workstream 6 — Deterministic Discovery

**Objective:** Implement bounded, repeatable, governed discovery that creates Candidate Context without deciding applicability, selection, or sufficiency.

**Dependencies:** Gate 3B approval; Workstreams 1–5.

- [x] 6.1 [IMP] Implement deterministic discovery over approved represented information, governed metadata/identity, Classification/Relationships, SQLite, literal/text evidence, Markdown structure, and bounded Git history where task-relevant and authorized.
- [x] 6.2 [IMP] Implement Candidate Context with discovery basis, underlying Provenance, classification, Authority/Governance/currentness data where available, scope, Conflict/Uncertainty, and handling limitations; keep it distinct from governance Candidate/Proposal state.
- [x] 6.3 [IMP] Implement bounded, explainable expansion only when authorized evidence indicates a material resolvable deficiency; preserve inspected universe, negative-result scope, failures, and termination basis.
- [x] 6.4 [VAL] Add deterministic-repeatability tests for fixed governed fixture state and request; test literal/metadata/relationship/history paths, scoped negative results, unavailable/partial Sources, and bounded expansion/termination.
- [x] 6.5 [VAL] Add negative tests proving discovery/ranking does not establish relevance, applicability, Authority, Governance State, selection, sufficiency, or universal absence.
- [x] 6.6 [DOC] Record discovery capability boundary, deterministic inputs/outputs, evidence-boundary behavior, and TD-14 reopening evidence procedure.

**H3 points:** Relevant authorized in-scope Required information is materially or repeatedly undiscoverable through approved deterministic mechanisms, causing incorrect/insufficient context or material harm to meaningful continuation. Record evidence and reopen TD-14; do not add AI/vector technology.

**Implementation status:** **COMPLETE — PROJECT OWNER APPROVED.** Items 6.1–6.6 are complete. Gate 3B remains approved. Workstream 7 is complete and Project Owner approved; Workstream 8 remains unauthorized and unbegun; Workstreams 9–10 remain unauthorized; Gate 3C has not been reached or approved; Phase 4 remains unauthorized. TD-14 remains **CLOSED / NOT REOPENED**: Workstream 6 testing produced no evidence meeting its approved material reopening threshold. See [Workstream 6 record](../docs/phase-3/workstream-6-deterministic-discovery.md).

### Workstream 7 — Applicability, Governance/Security Enforcement, and Selection

**Objective:** Implement deterministic governed evaluation from Candidate Context through applicability and selection, with fail-closed authorization/security enforcement.

**Dependencies:** Workstream 6 and Gate 3B.

- [x] 7.1 [IMP] Implement applicability evaluation that considers task intent/scope, relevance, scoped Authority, Governance State, currentness, Relationships, Conflict, Uncertainty, Provenance, Requester authorization, and Consumer disclosure authorization where applicable.
- [x] 7.2 [IMP] Implement deterministic governance/security enforcement at Bootstrap, Project/Source scope, discovery, retrieval, selection, package construction, rendering, audit, and cross-Project boundaries; fail closed where required.
- [x] 7.3 [IMP] Implement task-relative Required/Supporting determination using the counterfactual omission principle; Consumer capacity, rendering limitations, convenience, and relevance alone cannot alter Required status.
- [x] 7.4 [IMP] Implement sufficiency-oriented selection and material explanation for inclusion, exclusion, prioritization, qualifications, Conflict/Uncertainty, and authorization effects without hidden chain-of-thought or disclosure bypass.
- [x] 7.5 [VAL] Add semantic and security-negative tests for scoped Authority, Authority/Governance separation, currentness/supersession, unresolved Conflict, Candidate/Proposal handling, source instruction inertness, authorization denial, protected metadata, and default Project isolation.
- [x] 7.6 [VAL] Add fail-closed tests for unknown/invalid governance, unresolved authorization, unauthorized cross-Project access, disclosure denial after retrieval, missing deterministic enforcement, and unavailable protected Required context.
- [x] 7.7 [VAL] Add selection tests for Required/Supporting behavior, required constraint preservation, material explanation, no Authority multiplication through repetition, and no selection solely from parser/ranking/recency.
- [x] 7.8 [DOC] Trace enforcement points and selection behavior to Domains B, D, and E; record all qualification/denial behavior.

**H3 points:** A safety-critical rule cannot be deterministically enforced; a material authorization/disclosure ambiguity; or a required new security/crypto/identity technology.

**Implementation status:** **COMPLETE — PROJECT OWNER APPROVED.** Items 7.1–7.8 are complete. Gates 3A, 3B, and 3C remain approved; TD-14 remains **CLOSED / NOT REOPENED**. Workstream 8 is complete and Project Owner approved; Workstream 9 remains unauthorized and unbegun; Workstream 10 remains unauthorized; Gate 3D has not been reached; Phase 4 remains unauthorized. This work implements no sufficiency or logical Context Package construction.

### Workstream 8 — Sufficiency and Logical Context Package Construction

**Objective:** Implement evidence-boundary-aware sufficiency and coherent logical Context Package construction with durable construction evidence.

**Dependencies:** Workstream 7; Gate 3B.

- [x] 8.1 [IMP] Implement ASU/evidence-boundary-aware sufficiency evaluation with explicit Sufficient, Conditionally Sufficient, Insufficient, and Denied behavior as applicable; a package existing does not establish sufficiency.
- [x] 8.2 [IMP] Implement bounded iteration from material deficiency to justified additional authorized discovery; preserve the final inspection boundary, negative results, unavailable/inaccessible/unsupported/partial sources, and termination reason.
- [x] 8.3 [IMP] Enforce the anti-waiver rule: Required Context remains Required. Conditional Sufficiency is available only for a materially bounded task that can proceed without assuming, reconstructing, overriding, or acting on the unavailable Required context; otherwise return Insufficient or Denied.
- [x] 8.4 [IMP] Construct logical Context Packages with request/Consumer association, selected Required/Supporting items, material Authority/Governance/currentness, Source Manifest/Provenance, Conflict/Uncertainty/gaps, authorization/freshness/source limitations, sufficiency, and Construction-State Coherence.
- [x] 8.5 [IMP] Implement Construction-State Coherence evaluation and durable Package-Construction Records; distinguish construction, logical package, rendering, delivery, receipt, use, partial/failure states, and historical package meaning.
- [x] 8.6 [VAL] Add semantic/integration tests for ASU adequacy, known credible Source gap, scoped negative discovery, material Conflict, required omission, Consumer-capacity pressure, inaccessible/undisclosable Required context, bounded iteration, and all sufficiency outcomes.
- [x] 8.7 [VAL] Add coherence/persistence tests for source/governance/authorization change during construction, incomplete package records, crash/retry, provenance and qualification retention, historical reconstruction, and restored state not becoming current.
- [x] 8.8 [DOC] Record package/construction traceability, sufficiency/coherence decision evidence, and limitations/reconstruction behavior.

**H3 points:** A needed sufficiency/coherence behavior contradicts approved semantics; an ASU policy expands scope; or package persistence requires material architectural/technology change.

**Implementation status:** **COMPLETE — PROJECT OWNER APPROVED.** Items 8.1–8.8 are complete. Gate 3C is approved; TD-14 remains **CLOSED / NOT REOPENED**. Workstream 9 is not authorized and has not begun; Workstream 10 remains unauthorized; Gate 3D has not been reached; Phase 4 remains unauthorized. No rendering, delivery, receipt, use, proving, or Phase 4 behavior is implemented.

### Gate 3C — Governed Context Pipeline [GATE]

**Entry:** A tested controlled path exists through deterministic discovery, applicability, governance/security enforcement, selection, sufficiency, and logical Context Package construction.

**Project Owner review:** Confirm strict stage separation, deterministic safety enforcement, ASU-aware sufficiency, non-waivable Required Context, material semantic preservation, durable construction evidence, and no unapproved semantic-assistance technology.

**Disposition:** **APPROVED — PROJECT OWNER.** For implemented Workstreams 1–8, the Project Owner accepts the governed Stage III path: deterministic discovery -> applicability -> deterministic governance/security enforcement -> selection -> ASU/evidence-boundary-aware sufficiency -> logical Context Package. The accepted evidence preserves stage separation; Candidate Context != selected Context Item; scoped Authority != Governance State; Requester authorization != Consumer disclosure authorization; fail-closed Project/cross-Project, protected-metadata, and Source-instruction boundaries; Required Context anti-waiver; Conditional Sufficiency anti-waiver; ASU and bounded-negative-result qualifications; deterministic authorized bounded iteration; preserved Source Manifest/Provenance/Conflict/Uncertainty/limitations; coherence downgrade-only behavior; and Project-scoped historical Package-Construction Records. Package construction creates no Authority, Governance State, or currentness and remains distinct from rendering, delivery, receipt, and use. This disposition establishes no Workstream 9/10 behavior, Gate 3D, Phase 3 closure, or Phase 4 authorization.

## Stage IV — Operational Completion

### Workstream 9 — Consumer Rendering and Application/CLI Orchestration

**Objective:** Provide faithful Human, ChatGPT, and Codex renderings and complete the approved CLI/application orchestration path.

**Dependencies:** Gate 3C approval; Workstreams 1–8.

- [ ] 9.1 [IMP] Implement Consumer Contracts and faithful renderers for Human, ChatGPT, and Codex from one logical Context Package; rendering is derived presentation, not governance reinterpretation.
- [ ] 9.2 [IMP] Preserve/retrievably reference material Required/Supporting status, Authority/Governance/currentness, Provenance, Conflict, Uncertainty, gaps, limitations, sufficiency, and coherence; do not make references materially inaccessible or use prior Consumer memory as Required Context.
- [ ] 9.3 [IMP] Implement CLI/application orchestration for explicit Bootstrap, request handling, governed startup/readiness, Project/Source lifecycle, observation, decision pipeline, package construction, rendering, durable outcome/audit handling, safe diagnostics, and controlled failure termination.
- [ ] 9.4 [IMP] Preserve logical-package != rendering != delivery != receipt != use in state and CLI results; do not implement automated Consumer action or claim receipt/use without evidence.
- [ ] 9.5 [VAL] Add renderer/component tests for semantic fidelity across Consumers, authorization-sensitive non-disclosure, Required capacity pressure, progressive disclosure/reference integrity, rendering failure/truncation, and no semantic elevation by wording.
- [ ] 9.6 [VAL] Add implementation-oriented integration tests from explicit Bootstrap through rendered output using controlled fixtures, including successful qualified/insufficient/denied outcomes and audit/diagnostic distinctions.
- [ ] 9.7 [DOC] Document supported operations, Consumer Contract/rendering limits, CLI behavior, prerequisite/failure behavior, and user/operator evidence boundaries.

### Workstream 10 — Operational Hardening, Recovery, and Implementation Closure

**Objective:** Validate operational integrity, failures, recovery, backup, technology boundaries, documentation, and Phase 3 closure readiness.

**Dependencies:** Workstream 9; Gate 3C.

- [ ] 10.1 [IMP] Complete bounded operational handling for interruption, retry/idempotency where applicable, persistence failure, partial work, unavailable Source/Git/Markdown/configuration, diagnostics, and recovery without falsely reporting success, absence, authorization, currentness, or sufficiency.
- [ ] 10.2 [IMP] Implement SQLite-supported consistent backup and controlled restore capability for required durable state, applying Project isolation, authorization, sensitivity, purpose-driven retention, audit protection, and secret exclusion; restored history is not current state.
- [ ] 10.3 [VAL] Add failure-path and recovery tests for startup/Bootstrap/configuration failures, Git/Source/Markdown failures, SQLite corruption/disk/transaction/migration failure, crash at coupled-state boundaries, duplicate/retry behavior, audit-write failure, and diagnostics that do not leak secrets/protected content.
- [ ] 10.4 [VAL] Add backup/recovery tests for consistent backup, restore validity, recovery of material package/audit/provenance state, stale restored governance/currentness qualification, authorization/isolation, and failed/partial restore behavior.
- [ ] 10.5 [VAL] Run controlled end-to-end implementation tests using fixtures—not a genuine fresh Consumer—to exercise the approved path from explicit Bootstrap through package/rendering, plus security-negative, fail-closed, deterministic-repeatability, and cross-Project boundary cases.
- [ ] 10.6 [VAL] Perform technology-integrity checks: approved runtime/dependencies only; no plugins, Git libraries, vector/LLM/embedding stack, CLI framework, container/VM/cloud/daemon/network dependency, ORM/framework, or unauthorized infrastructure/dependency expansion.
- [ ] 10.7 [DOC] Complete implementation documentation, architecture/requirements traceability, migration/backup/recovery/operator guidance, test inventory/results, limitations, configuration/version record, and findings ledger.
- [ ] 10.8 [DOC] Prepare the Phase 3 closure evidence package and Phase 4 readiness assessment; do not execute proving or Phase 4 validation/integration.

**H3 points:** Recovery/backup semantics requiring a new technology or governance policy; an implementation-discovered material design deficiency; unapproved dependency/infrastructure; or need to execute proving/Phase 4 activity to claim implementation completion.

## Finding classification and closure control

Record every implementation finding with identifier, severity, affected requirement/design reference, evidence, impact, disposition owner, and closure evidence. Classify findings as **BLOCKER**, **MATERIAL**, **MINOR**, or **OBSERVATION**.

- **BLOCKER:** prevents safe/conforming continuation or invalidates a governing boundary. Stop affected work and obtain Project Owner disposition.
- **MATERIAL:** changes or leaves unresolved a material architecture, technology, security, governance, semantic, scope, dependency, persistence, or phase decision. Stop affected work and escalate under H3; it cannot be hidden as deferred.
- **MINOR:** does not cross a material boundary, but must have a documented correction, accepted rationale, or tracked disposition before closure where relevant.
- **OBSERVATION:** non-blocking evidence/lesson that does not alter approved behavior; record when useful without manufacturing an approval gate.

No unresolved BLOCKER or MATERIAL finding is acceptable for Phase 3 closure. A finding’s label does not weaken its actual impact. Corrections must preserve traceability and never silently modify authoritative Phase 0–2 sources to reconcile an inconsistency.

## Phase 3 closure and Phase 4 boundary

### Phase 3 exit criteria

Phase 3 may be presented for closure only when all of the following are evidenced:

- [ ] Approved v0.1 Context Engine is implemented as an installable application within the approved physical architecture and technology selections.
- [ ] The authorized end-to-end implementation path works through explicit Bootstrap, governed semantics, persistence, Project/Source lifecycle, observation/transformation/representation/Provenance, deterministic discovery, governed decision pipeline, sufficiency, logical package construction, rendering, and CLI/application orchestration.
- [ ] Relevant unit, semantic/invariant, component, adapter, persistence/migration, integration, deterministic-repeatability, security-negative, fail-closed, failure-path, backup/recovery, and controlled end-to-end implementation tests pass; remaining limitations are explicit and governed.
- [ ] Material semantic information, provenance, Authority/Governance/currentness distinctions, authorization boundaries, Conflict/Uncertainty, ASU/evidence boundary, sufficiency, and Construction-State Coherence are preserved.
- [ ] Technology-integrity review confirms no unauthorized redesign, dependency, AI/vector/LLM expansion, framework/infrastructure expansion, or scope/non-goal leakage occurred.
- [ ] Documentation accurately describes the implemented state, test evidence, operational limits, migrations, backup/recovery, supported Source/Consumer behavior, findings, and traceability to Phase 0–2.
- [ ] Finding inventory has unresolved BLOCKER **0** and MATERIAL **0**; any MINOR findings have an appropriate documented disposition.
- [ ] Phase 3/Phase 4 boundary review confirms no Company AI Roadmap proving exercise, Context Engine dogfooding exercise, fresh-Consumer evaluation, Phase 4 validation/integration, production-readiness claim, AI-assisted-discovery authorization, automated Consumer action, or broader scope was silently performed or claimed.
- [ ] Phase 4 readiness assessment identifies what is ready for future authorization and what remains outside the implementation-validation result.

### Gate 3D — Phase 3 Exit Review [GATE]

**Entry:** Workstreams 9–10, the closure evidence package, finding ledger, and Phase 4 readiness assessment are complete.

**Project Owner review:** Review implementation/design conformance, tests and failure evidence, semantic/governance/technology integrity, documentation/traceability, unresolved findings, and phase-boundary compliance.

**Required decision:** The Project Owner explicitly approves or declines Phase 3 closure. Approval of Phase 3 closure does **not** automatically authorize Phase 4. Phase 4 requires a separate explicit Project Owner decision.

## Future proving and validation boundary

The Company AI Roadmap external proving exercise and Context Engine dogfooding exercise remain designed future work, not Phase 3 checklist completion tasks. They require separately authorized execution and a genuinely fresh Consumer with the approved contamination preflight: no material Project knowledge via memory, Project context, connected Sources/files, prior sessions, manual briefing, or hidden channels. A contaminated or unverifiable Consumer makes the run invalid and requires discard/restart clean.

Phase 3 implementation validation answers: **“Did we correctly implement the approved v0.1 design?”** Phase 4 validation/integration and future proving answer different questions. Phase 3 completion does not establish external proving success, dogfooding success, Phase 4 completion, production readiness beyond actually validated evidence, authorization for AI-assisted discovery, automated Consumer action, or broader project scope.

## Governing references

- [Phase 0 governance](../docs/phase-0/project-definition-governance.md)
- [Phase 1 baseline and traceability](../docs/phase-1/v0.1-baseline-and-traceability.md) and [conceptual model](../docs/phase-1/conceptual-context-model.md)
- [Phase 2 Domains A–I](../docs/phase-2/architecture-foundation-system-boundary.md), [B](../docs/phase-2/governance-trust-security-architecture.md), [C](../docs/phase-2/source-observation-architecture.md), [D](../docs/phase-2/context-knowledge-representation.md), [E](../docs/phase-2/discovery-selection-sufficiency-architecture.md), [F](../docs/phase-2/context-package-consumer-architecture.md), [G](../docs/phase-2/state-persistence-operational-architecture.md), [H](../docs/phase-2/technology-selection-physical-architecture.md), and [I/exit material](../docs/phase-2/validation-proving-architecture-exit-gate.md)
- [Phase 2 exit-gate closure](../docs/phase-2/phase-2-exit-gate.md), [roadmap](../docs/roadmap.md), [AGENTS.md](../AGENTS.md), and the approved Phase 2 checklist.

This checklist explains the authorized implementation plan; it does not supersede the approved Phase 0–2 records or create Authority.
