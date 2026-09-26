# Phase 4 Master Plan & Checklist — Validation & Integration

**Status:** **PLAN/CHECKLIST DESIGN — PROJECT OWNER APPROVED. PHASE 4 EXECUTION — NOT AUTHORIZED.** Gate 4A is **NOT APPROVED**. This governed plan is subordinate to the approved Phase 0–3 baseline, including the clean Phase 3 closure baseline at commit `9862497` (`Close Phase 3 v0.1 implementation`). It creates neither execution authority nor a production-readiness claim.

## Purpose, authority, and phase boundary

Phase 4 is the future governed-evidence phase for determining what the completed v0.1 Context Engine demonstrably supports as an integrated system. It will validate behavior across realistic controlled workflows, semantic/governance/security/isolation invariants, failure/recovery behavior, and (only after the applicable gates) genuinely fresh-Consumer proving. It will preserve sufficient evidence for the Project Owner to decide which claims are supported and whether any later phase should be proposed or authorized.

Phase 4 does **not** automatically establish production readiness, authorize technology or scope expansion, authorize automated Consumer action, or authorize a later phase. It does not redesign the approved Phase 0–3 baseline. The Project Owner remains the final approving authority for material decisions; ChatGPT remains the design partner, analyst, reviewer, challenger, and recommendation source; Codex implements and documents approved decisions.

This checklist is a planning artifact only. It does **not** execute validation, proving, a fresh-Consumer contamination preflight, a fresh-Consumer reservation or exposure, remediation, or any change to application behavior. Creating this checklist does not approve Gate 4A.

### Labels and H3 control

| Label | Meaning |
| --- | --- |
| `[PLAN]` | Planning/documentation for later authorized execution; no execution occurs merely by completing the plan. |
| `[VAL]` | Future controlled validation activity, permitted only after Gate 4A PASS and explicit execution authorization. |
| `[PROVE]` | Future fresh-Consumer proving activity, permitted only after Gate 4B PASS and the applicable authorization. |
| `[DOC]` | Evidence, register, protocol, traceability, or checklist record. |
| `[GATE]` | Project Owner review and disposition point. |
| `[H3]` | Materiality/escalation point; stop and obtain Project Owner review when triggered. |

**H3 remains controlling.** Codex may make ordinary non-material documentation choices within this approved plan. Codex must stop and report rather than decide if work would materially change scope, architecture, technology, security, governance, data models, dependencies, approved semantics, validation/proving methodology, Consumer protocol, or phase boundaries; if approved records conflict; if a required result is genuinely ambiguous; or if an approved procedure is infeasible. A finding label never reduces its actual impact.

### Controlling distinctions and non-negotiable validation invariants

Every planned activity must preserve and evaluate these distinctions; a passing component test does not by itself establish their integrated preservation:

- Source observation != interpretation; represented information != Candidate Context != selected Context Item; and discovery != applicability != selection != sufficiency.
- Authority != Governance State; Authority is scoped; Requester authorization != Consumer disclosure authorization; Project isolation is default; and cross-Project traversal is bounded and governed.
- Historical state != current state. Persistence and restoration do not create currentness, Authority, Governance State, or present authorization.
- Required Context cannot be waived for Consumer capacity; Conditional Sufficiency does not waive Required Context; and the Applicable Source Universe (ASU) participates in sufficiency.
- Logical Context Package != rendering != delivery != receipt != use.
- Source-derived imperative/instruction-like content remains Source content unless governance independently establishes instructional applicability.
- Material Provenance, Conflict, Uncertainty, limitations, sufficiency, and Construction-State Coherence remain preserved.

### Scope and explicit exclusions

Planned Phase 4 scope is governed validation/integration, evidence review, controlled proving when separately gate-authorized, findings disposition, authorized remediation, retest, and final acceptance review of the completed v0.1 baseline.

Phase 4 does not silently add LLM discovery, embeddings, semantic search, vector database/index, reranking/model-based discovery, a Git library, ORM, framework, security/IAM/cryptography framework, queue, cloud/service/container/VM/HA capability, runtime network dependency, additional integration environment, automated Consumer action, backup scheduling, retention duration, deletion workflow, RPO/RTO, or new deployment/infrastructure scope. It does not reopen TD-14 unless the approved trigger is met and governance reopens it. It does not convert validation or proving into production-readiness certification.

## Workstream 1 — Validation Governance & Evidence Model

**Objective:** Establish the rules, expected results, protocols, evidence model, and finding controls before validation results exist. The rules used to determine success or failure must exist before results are observed.

**Dependencies:** Approved Phase 0–3 baseline; no Phase 4 execution authority is implied.

- [x] 1.1 [PLAN][DOC] Record the immutable/reference validation baseline: Phase 0–2 approved records, the Phase 3 closure record, clean closure commit `9862497`, approved configuration/fixture provenance, and any later approved baseline amendment with its authority and scope. Do not rewrite historical baseline evidence. See the [WS1 governance and evidence-model record](../docs/phase-4/workstream-1-validation-governance-evidence-model.md#11--reference-validation-baseline).
- [x] 1.2 [PLAN][DOC] Define Phase 4 scope, exclusions, and the distinction among implementation testing, validation, proving, and production readiness. State that implementation-level tests are evidence inputs, not a substitute for Phase 4 integrated validation or proving. See the [WS1 governance and evidence-model record](../docs/phase-4/workstream-1-validation-governance-evidence-model.md#12--four-evidence-levels).
- [x] 1.3 [PLAN][DOC] Establish evidence-preservation rules: immutable original result artifacts; controlled copies/derivations with lineage; task/request, fixture/Source, configuration/Bootstrap, environment, version/commit, command/procedure, raw result, rendering, reviewer assessment, finding, and disposition linkage as applicable. Preserve failures and inconclusive results as evidence. See the [WS1 governance and evidence-model record](../docs/phase-4/workstream-1-validation-governance-evidence-model.md#13--evidence-preservation).
- [x] 1.4 [PLAN][DOC] Establish expected-result controls before execution: predetermined expected outcomes and acceptance/negative criteria, known limitations, fixture identity, reviewer basis, and rules for recording an unanticipated result. Expected behavior may not be changed merely to make a test pass. See the [WS1 governance and evidence-model record](../docs/phase-4/workstream-1-validation-governance-evidence-model.md#14--expected-result-controls).
- [x] 1.5 [PLAN][DOC] Define validation result states: **PASS**, **FAIL**, and **INDETERMINATE**, including evidence linkage and the rule that INDETERMINATE is not PASS or silent success. See the [WS1 governance and evidence-model record](../docs/phase-4/workstream-1-validation-governance-evidence-model.md#15--validation-result-states).
- [x] 1.6 [PLAN][DOC] Establish impact-based finding severities: **BLOCKER**, **MATERIAL**, **MINOR**, and **OBSERVATION**, with H3 controlling actual materiality. See the [WS1 governance and evidence-model record](../docs/phase-4/workstream-1-validation-governance-evidence-model.md#16--finding-severity-model).
- [x] 1.7 [PLAN][DOC] Establish independent finding types: **IMPLEMENTATION**, **INTEGRATION**, **SECURITY/GOVERNANCE**, **OPERATIONAL**, **DESIGN**, **PROVING-PROTOCOL**, and **CONSUMER-USABILITY**, with a required primary type and preserved classification lineage. See the [WS1 governance and evidence-model record](../docs/phase-4/workstream-1-validation-governance-evidence-model.md#17--finding-type-model).
- [x] 1.8 [PLAN][DOC] Define finding ownership, lifecycle, and governed disposition, separating investigation from disposition authority and requiring evidence-based closure without independently authorizing remediation. See the [WS1 governance and evidence-model record](../docs/phase-4/workstream-1-validation-governance-evidence-model.md#18--finding-ownership-lifecycle-and-disposition).
- [x] 1.9 [PLAN][H3] Define H3 escalation boundaries and Codex remediation boundaries. Stop for material or genuinely ambiguous scope, architecture, technology, security, governance, semantic, data-model, dependency, Consumer-protocol, or phase decision. Require Project Owner approval before material remediation; no remediation authority arises from finding discovery alone. See the [WS1 governance and evidence-model record](../docs/phase-4/workstream-1-validation-governance-evidence-model.md#19--h3-escalation-and-codex-remediation-boundaries).
- [x] 1.10 [PLAN][DOC] Define remediation evidence and retest requirements: causal hypothesis, authorized change boundary, exact changed baseline, focused retest, affected-suite retest, relevant end-to-end regression validation, residual limitations, and evidence-based closure. See the [WS1 governance and evidence-model record](../docs/phase-4/workstream-1-validation-governance-evidence-model.md#110--remediation-evidence-and-retest-requirements).
- [x] 1.11 [PLAN][DOC] Establish anti-overfitting controls. A remedy must address a general mechanism/invariant, not hard-code a proving case, project vocabulary, Consumer identity, expected answer, or special path absent an approved general requirement. Expected results may not be altered solely to eliminate failure. See the [WS1 governance and evidence-model record](../docs/phase-4/workstream-1-validation-governance-evidence-model.md#111--anti-overfitting-controls).
- [x] 1.12 [PLAN][DOC] Establish proving evidence preservation and independent evaluation expectations: freeze protocol/package/rendering before Consumer evaluation; retain immutable original Consumer-facing evidence and interventions; separate construction from evaluation; preserve omissions, inappropriate inclusions, qualifications, and negative outcomes; and obtain evaluation by a reviewer not responsible for changing the result under review where practicable. See the [WS1 governance and evidence-model record](../docs/phase-4/workstream-1-validation-governance-evidence-model.md#112--proving-evidence-preservation-and-independent-evaluation).
- [x] 1.13 [PLAN][DOC] Design (but do not execute) the fresh-Consumer contamination protocol: assess memory, Project context, connected Sources/files, prior sessions, manual briefing, hidden channels, and other plausible material Project knowledge; record evidence and freshness state **PASS**, **FAIL**, or **INDETERMINATE**. FAIL and INDETERMINATE Consumers are unsuitable; discard/restart rather than weaken freshness criteria. See the [WS1 governance and evidence-model record](../docs/phase-4/workstream-1-validation-governance-evidence-model.md#113--fresh-consumer-contamination-protocol).
- [x] 1.14 [PLAN][DOC] Define reserved-Consumer protection and proving-run discard criteria. No planned reservation may expose Project facts, package contents, task-specific material state, or other contamination before actual preflight. A run is discarded/restarted for freshness FAIL/INDETERMINATE, protocol breach, material uncontrolled intervention, unpreserved original evidence, or another condition that invalidates the established evidence basis. See the [WS1 governance and evidence-model record](../docs/phase-4/workstream-1-validation-governance-evidence-model.md#114--reserved-consumer-protection-and-run-discard-criteria).
- [x] 1.15 [PLAN][H3] Record the TD-14 stop/reopening procedure. Preserved evidence may make TD-14 a reopening candidate only when relevant, authorized, in-scope information necessary to Required Context or an approved success criterion is materially or repeatedly undiscoverable through approved deterministic mechanisms, with the specified material consequence. The procedure requires stage distinction, non-trigger analysis, a MATERIAL-or-higher finding, a complete TD-14 Reopening Evidence Record, stop behavior, and Project Owner review; it does not reopen TD-14 or authorize AI/vector technology. See the [WS1 governance and evidence-model record](../docs/phase-4/workstream-1-validation-governance-evidence-model.md#115--td-14-stopreopening-procedure).
- [x] 1.16 [PLAN][H3] Define the material Phase 4 scope-change procedure. Evidence can require consideration but cannot silently change scope. The procedure requires a complete Scope-Change Candidate Record, impact/alternatives/urgency analysis, an explicit Project Owner disposition, and explicit assessment of invalidated or reapproval-required evidence if a bounded amendment is approved. A useful future capability is not authorization. See the [WS1 governance and evidence-model record](../docs/phase-4/workstream-1-validation-governance-evidence-model.md#116--material-phase-4-scope-change-procedure).
- [x] 1.17 [PLAN][DOC] Assemble the [Phase 4 validation-governance package](../docs/phase-4/validation-governance-package/README.md): baseline register, scope/exclusions, methodology, expected-result register, evidence inventory/template, finding register/template, remediation/retest protocol, contamination/proving-protocol architecture, TD-14 control, H3 escalation record, and traceability to this checklist. **Workstream 1 is COMPLETE / READY FOR GATE 4A REVIEW.** This completion does not approve Gate 4A or authorize execution.

**Completion evidence:** A reviewable pre-results governance package that makes the applicable methods, expected outcomes, evidence, finding rules, remediation boundaries, and proving protections explicit without running validation or proving.

## Gate 4A — Validation Plan & Execution Authorization [GATE]

**Entry:** Workstream 1 planning package is complete and internally consistent; no validation/proving execution is implied by entry.

**Project Owner review:** Phase 4 scope; validation methodology; evidence model; finding taxonomy; expected-result controls; remediation/retest model; contamination protocol; proving-protocol architecture; TD-14 escalation control; and materiality/escalation rules.

**Gate outcomes:** **PASS**, **HOLD**, or **FAIL**.

**Required decision:** Only a Project Owner **PASS**, together with explicit Phase 4 execution authorization, may permit planned execution activities to begin. HOLD or FAIL does not permit execution. This checklist’s creation is not Gate 4A approval.

**Disposition:** **NOT APPROVED. Phase 4 execution is NOT AUTHORIZED.**

## Workstream 2 — Deterministic End-to-End Integration Validation

**Objective:** After Gate 4A PASS and explicit execution authorization, validate the complete governed pipeline using controlled Sources, deterministic fixtures, known inputs, and predetermined expected results:

`Bootstrap -> configuration -> Project/Source lifecycle -> observation -> transformation -> represented information / Provenance -> deterministic discovery -> Candidate Context -> applicability -> governance/security -> Required/Supporting determination -> selection -> sufficiency -> logical Context Package -> Human/ChatGPT/Codex rendering.`

**Dependencies:** Gate 4A PASS; authorized execution; approved WS1 expected-result/evidence controls.

- [ ] 2.1 [VAL] Establish controlled deterministic fixtures and known inputs with explicit Bootstrap/configuration, Project/Source scope, ASU basis, authorization/disclosure conditions, expected represented information, expected candidates, and expected package/rendering results. Fixture content has no production authority.
- [ ] 2.2 [VAL] Validate normal end-to-end construction from explicit Bootstrap through each pipeline boundary to a logical Context Package and all approved renderings; preserve the construction record and evidence of every material transition.
- [ ] 2.3 [VAL] Validate multiple Sources and multiple represented-information items without Source observation becoming interpretation, representation becoming selection, or Source count becoming ASU adequacy.
- [ ] 2.4 [VAL] Validate competing Candidate Context, applicable versus non-applicable context, and Required versus Supporting determinations; preserve the reasons/evidence for inclusion, exclusion, and qualification.
- [ ] 2.5 [VAL] Validate sufficient, insufficient, and Conditional Sufficiency outcomes. Confirm that Required Context and ASU adequacy participate, Consumer capacity cannot waive Required Context, and Conditional Sufficiency does not conceal a Required deficiency.
- [ ] 2.6 [VAL] Validate ASU establishment/basis, known-incomplete and indeterminate boundaries, scoped negative results, bounded expansion, and preservation of unavailable/inaccessible/unauthorized/unsupported limitations.
- [ ] 2.7 [VAL] Validate preservation of Conflict, Uncertainty, Provenance/transformation lineage, material limitations, and Construction-State Coherence from observation through rendering; do not silently resolve, omit, or upgrade them.
- [ ] 2.8 [VAL] Validate Human, ChatGPT, and Codex renderings from the same logical Context Package while preserving the logical-package/rendering distinction and material Required/Supporting, provenance, qualification, and sufficiency information.
- [ ] 2.9 [VAL] Validate declared Consumer-capacity behavior. Confirm that capacity limits do not drop or waive Required Context; preserve the limitation or fail according to established behavior rather than claim delivery, receipt, or use.
- [ ] 2.10 [VAL] Validate deterministic repeatability and governed ordering/stability: identical controlled inputs must produce the established semantic result/order without filesystem order, hash iteration, row identifier, frequency, recency, or unapproved scoring becoming semantic rank.
- [ ] 2.11 [VAL][DOC] Preserve all discrepancy evidence and create findings for differences from predetermined expected results, unexpected instability, missing qualification, or evidence gaps. Do not normalize fixture data or revise expected results solely to obtain PASS.

**Completion evidence:** Controlled end-to-end evidence set, repeatability results, rendering artifacts, discrepancy/finding register, and traceability to expected-result controls.

## Workstream 3 — Security, Governance & Isolation Validation

**Objective:** After Gate 4A PASS and explicit execution authorization, validate integrated enforcement of approved security, governance, provenance, disclosure, and isolation semantics.

**Dependencies:** Gate 4A PASS; authorized execution; WS1 controls; controlled security/governance fixtures.

- [ ] 3.1 [VAL] Validate default Project isolation and fail-closed unauthorized cross-Project access.
- [ ] 3.2 [VAL] Validate bounded cross-Project traversal only when the established task requirement, governed relationship, Requester authorization, and Consumer disclosure authorization prerequisites are present; validate denial when any prerequisite is absent.
- [ ] 3.3 [VAL] Validate Requester authorization separately from Consumer disclosure authorization, including cases where Requester access does not permit disclosure to the Consumer.
- [ ] 3.4 [VAL] Validate scoped Authority; Authority distinct from Governance State; current versus historical state; and denial of unsupported elevation.
- [ ] 3.5 [VAL] Validate that restoration/persistence does not create currentness, Authority, Governance State, or present authorization.
- [ ] 3.6 [VAL] Validate Provenance and governance-state enforcement, disclosure restrictions, and authorization-bound material metadata/audit handling within approved scope.
- [ ] 3.7 [VAL] Validate Source-derived imperative/instruction-like content, including hostile/malicious instruction-like Source content within approved scope, remains evidence/content and does not establish governing instruction, Authority, or unauthorized action.
- [ ] 3.8 [VAL] Validate preservation—not suppression—of Required Context, Conflict, Uncertainty, and material limitations under security/governance constraints; undisclosable or unavailable Required Context must affect qualification/sufficiency according to approved semantics.
- [ ] 3.9 [VAL][DOC] Record unauthorized Consumer exposure attempts, denied paths, and any discrepancy/finding evidence without treating a denial as proof that all other paths are secure.

**Completion evidence:** Controlled positive/negative security and isolation evidence, enforcement-path explanation, disclosure results, and governed finding disposition.

## Workstream 4 — Failure, Recovery & Operational Validation

**Objective:** After Gate 4A PASS and explicit execution authorization, validate approved failure, persistence, manual-backup, controlled-restore, recovery, and diagnostic behavior without expanding operational scope.

**Dependencies:** Gate 4A PASS; authorized execution; WS1 controls; controlled non-production failure/recovery procedures.

- [ ] 4.1 [VAL] Validate malformed input, invalid configuration, and missing/unavailable Sources where applicable. Confirm that failure, absence, partial evidence, and successful completion remain distinct.
- [ ] 4.2 [VAL] Validate interrupted operations, persistence integrity, transaction/partial-state behavior, and migration behavior where applicable using controlled procedures and preserved evidence.
- [ ] 4.3 [VAL] Validate the existing manual backup capability and controlled restore only within the approved local/manual boundary.
- [ ] 4.4 [VAL] Validate restored Project/Source state, Provenance, governance state, history, audit/construction evidence, and Project isolation as historical evidence where applicable.
- [ ] 4.5 [VAL] Validate that restore does not manufacture currentness, Authority, Governance State, present authorization, or sufficiency; historical state remains historical until independently re-established.
- [ ] 4.6 [VAL] Validate recovery after controlled failure and useful diagnostic/error behavior without treating diagnostics as durable audit or a recovery claim.
- [ ] 4.7 [VAL][H3] If evidence demonstrates a material need for backup scheduling, retention duration, deletion workflow, RPO/RTO, HA, daemon/service deployment, containers, cloud infrastructure, or an additional integration environment, stop and raise it through governance. Do not add it to Phase 4.

**Completion evidence:** Failure/recovery matrix, backup/restore and historical-state evidence, diagnostic results, operational limitations, and findings register.

## Gate 4B — Controlled Validation Acceptance & Proving Readiness [GATE]

**Entry:** WS2–WS4 evidence has been preserved and assessed under WS1 controls. No fresh Consumer may be consumed before this gate passes.

**Project Owner review:** Evidence completeness; findings; unresolved BLOCKER/MATERIAL findings; semantic invariants; security/governance/isolation results; failure/recovery results; technology boundaries; unauthorized scope expansion; TD-14 status; and the justification for consuming a fresh-Consumer proving opportunity.

**TD-14 control:** If evidence meets the approved material deterministic-discovery deficiency threshold, **STOP**. Preserve evidence and reopen TD-14 through governance; do not silently introduce LLM discovery, embeddings, semantic search, vector database/index, reranking, or model-based discovery.

**Required decision:** Gate 4B PASS is required before actual fresh-Consumer contamination preflight or either proving exercise. It does not itself authorize remediation, technology change, or production readiness.

**Disposition:** **NOT APPROVED.**

## Workstream 5 — Fresh-Consumer Proving Readiness

**Objective:** After Gate 4B PASS and explicit authorization, protect proving validity by assessing a reserved Consumer’s actual freshness before any package delivery or material Project exposure.

**Dependencies:** Gate 4B PASS; applicable proving authorization; WS1 contamination protocol; protected reserved Consumer.

- [ ] 5.1 [PROVE] Identify/reserve a candidate Consumer without exposing material Project knowledge. Record Consumer identity/session boundary only to the degree necessary for governed evidence.
- [ ] 5.2 [PROVE] Execute the actual contamination preflight only after Gate 4B: assess memory exposure, Project-context exposure, connected Source/file exposure, prior-session exposure, manual briefing exposure, hidden-channel exposure, and other plausible material Project knowledge.
- [ ] 5.3 [PROVE][DOC] Record preflight basis/evidence and classify freshness **PASS**, **FAIL**, or **INDETERMINATE**. FAIL and INDETERMINATE Consumers are unsuitable.
- [ ] 5.4 [PROVE] Discard/restart rather than weaken freshness criteria whenever the Consumer fails or cannot be reasonably established as fresh. Preserve the invalidation evidence without using the Consumer for proving.
- [ ] 5.5 [PROVE][DOC] Record permitted Sources and permitted Consumer inputs; freeze the proving protocol and success/failure evidence requirements before package construction/delivery.

**Completion evidence:** A valid freshness PASS for the exact proving run, frozen permitted-input/protocol records, or an explicitly preserved invalid/discarded-run record. This workstream does not claim a proving outcome.

## Workstream 6 — Controlled Proving

**Objective:** Conduct the two approved proving exercises in sequence, using frozen protocols and a genuinely fresh Consumer. Proving evaluates governed useful context; it does not authorize automated Consumer action or establish production readiness.

**Dependencies:** Gate 4B PASS; WS5 freshness PASS for the exact run; applicable Project Owner authorization; frozen protocol and expected-result/evidence requirements.

### WS6A — Company AI Roadmap External Proving

**Purpose:** Determine whether v0.1 can provide governed useful context to a genuinely fresh Consumer for a real project other than Context Engine.

- [ ] 6A.1 [PROVE] Confirm the exact run’s freshness PASS and frozen protocol, controlled Sources, permitted inputs, task, success/failure criteria, and independent evaluation arrangement.
- [ ] 6A.2 [PROVE] Construct the Context Engine output through controlled approved mechanisms and preserve the exact logical Context Package, Source Manifest/construction evidence, Consumer-facing rendering, and delivery boundary. Do not equate delivery with receipt or use.
- [ ] 6A.3 [PROVE] Preserve Consumer outcome evidence, questions, interventions, omissions, inappropriate inclusions, governance/security behavior, Provenance/Conflict/Uncertainty behavior, sufficiency behavior, and material limitation handling.
- [ ] 6A.4 [PROVE][DOC] Preserve immutable original evidence before evaluation. Evaluate the run independently against the frozen criteria, including meaningful continuation, state/governance accuracy, isolation, qualifications, and reconstruction burden where applicable.
- [ ] 6A.5 [PROVE][H3] Do not remediate before original evidence evaluation is complete. Record a finding or invalid run where warranted; do not fold repair, briefing, or package alteration into a PASS.

**Completion evidence:** A preserved and evaluated proving-evidence package, including a valid run or an explicit invalid/failure/indeterminate result. A successful case demonstrates only its evidence-supported external-project claim, not universality or production readiness.

### WS6B — Context Engine Dogfooding

**Purpose:** Determine whether Context Engine can construct governed context sufficient for a genuinely fresh Consumer to work with the Context Engine project itself.

**Sequence control:** WS6B may run only after WS6A evidence has been preserved and evaluated. The recursive case receives heightened contamination scrutiny and uses the same evidence discipline.

- [ ] 6B.1 [PROVE] Confirm WS6A evidence preservation/evaluation, then establish a distinct exact-run freshness PASS and frozen protocol for the dogfooding Consumer.
- [ ] 6B.2 [PROVE] Use ordinary governed Context Engine Project configuration, Sources, semantics, and renderers. No privileged `if project == "context-engine"` logic, Project-specific core behavior, or hidden self-knowledge is permitted.
- [ ] 6B.3 [PROVE] Preserve the exact package/rendering, Consumer outcome, interventions, omissions/inappropriate inclusions, governance/security, Provenance/Conflict/Uncertainty, sufficiency, and recursive-case limitations.
- [ ] 6B.4 [PROVE][DOC] Independently evaluate the frozen evidence, including current/historical/future authorization distinctions, next legitimate activity, general-mechanism integrity, and whether manual reconstruction was materially required.
- [ ] 6B.5 [PROVE][H3] Do not remediate before evidence evaluation is complete. Preserve invalidation/failure evidence and govern any proposed correction through WS7.

**Completion evidence:** A preserved and independently evaluated dogfooding-evidence package, including a valid run or explicit invalid/failure/indeterminate result. It does not establish privileged self-knowledge, universality, or production readiness.

## Gate 4C — Proving Evidence Acceptance [GATE]

**Entry:** For each proving exercise, the applicable WS5/WS6 evidence is preserved and independently evaluated; no remediation is folded into the evidence under review.

**Project Owner review for each exercise:** Freshness; protocol compliance; evidence completeness; Context Package validity; rendering validity; Required Context; material omissions; inappropriate inclusions; governance/security behavior; Provenance/Conflict/Uncertainty; sufficiency; Consumer-usability observations; finding classification; and validity of the proving evidence itself.

**Required decision:** Gate 4C accepts or rejects evidence **before remediation**. Acceptance of evidence does not mean all findings are closed, production readiness is established, or a later phase is authorized.

**Disposition:** **NOT APPROVED.**

## Workstream 7 — Findings, Remediation & Retest

**Objective:** Govern the loop `Finding -> cause -> classification -> governed disposition -> authorized remediation -> focused retest -> affected-suite retest -> relevant end-to-end regression validation -> evidence-based closure` without silent redesign, result manipulation, or proving-case overfitting.

**Dependencies:** A preserved finding from WS2–WS6 or final review; applicable authorization before remediation; Gate 4C evidence decision where a proving finding is involved.

- [ ] 7.1 [DOC] Register and preserve each finding’s original evidence; classify severity and type; distinguish implementation defect, integration defect, security/governance issue, operational issue, design deficiency, proving-protocol issue, and Consumer-usability observation.
- [ ] 7.2 [H3] Apply H3 to cause/disposition. Escalate material or ambiguous decisions, including a potential design change, semantic change, technology need, security/governance change, scope expansion, or whether existing proving evidence is invalidated.
- [ ] 7.3 [DOC] Obtain the required governed disposition and, before material remediation, Project Owner approval. A finding does not independently authorize changes.
- [ ] 7.4 [VAL] Apply authorized remediation only through a general mechanism/invariant. Prohibit proving-case hard-coding, project-vocabulary special-casing absent an approved general requirement, Consumer-specific special-casing, and changing expected results solely to eliminate failure.
- [ ] 7.5 [VAL] Preserve remediation evidence and execute focused retest, affected-suite retest, and relevant end-to-end regression validation against the established expected-result controls.
- [ ] 7.6 [DOC] Assess whether remediation changes the baseline or invalidates prior validation/proving evidence; determine through governance whether another genuinely fresh proving run is required. Never reuse a contaminated/invalid Consumer as a substitute for freshness.
- [ ] 7.7 [DOC] Close findings only when the governed disposition, evidence, retests, residual limitations, and any required re-proving decision are recorded. Preserve failures that remain open or are accepted as governed limitations.

**Completion evidence:** Complete findings register with original evidence, authority/disposition, remediation and retest evidence where authorized, re-proving assessment, and evidence-based closure/open status.

## Workstream 8 — Final Validation & Acceptance Review

**Objective:** Assemble the evidence-based Phase 4 closure package and separate supported claims, unsupported claims, limitations, production-readiness disposition, future-work candidates, and later-phase authorization decisions.

**Dependencies:** Mandatory workstream evidence; findings/retest status; Project Owner review at Gate 4D.

- [ ] 8.1 [DOC] Review completion/evidence status for all workstreams and the complete findings register, including BLOCKER, MATERIAL, MINOR, and OBSERVATION disposition.
- [ ] 8.2 [DOC] Review remediation/retest evidence; unauthorized-redesign and overfitting checks; semantic-boundary integrity; technology-boundary integrity; scope integrity; and TD-14 disposition.
- [ ] 8.3 [DOC] Evaluate and state separately the evidence-supported deterministic integration validation claim, security/governance validation claim, failure/recovery validation claim, operational validation claim, Company AI Roadmap proving claim, Context Engine dogfooding claim, and overall Phase 4 validation claim.
- [ ] 8.4 [DOC] State explicitly what Phase 4 did **not** prove, including any unsupported generality, production-readiness, deployment, scale, HA, automated Consumer action, technology, or future-scope claim.
- [ ] 8.5 [DOC][GATE] Prepare the production-readiness disposition for Project Owner decision. Production readiness must be explicitly dispositioned; it is not inferred from Phase 4 completion or any individual PASS.
- [ ] 8.6 [DOC] Record remaining governed limitations and future-work candidates without authorizing them. A proposal for another phase is separate from authorization of that phase.
- [ ] 8.7 [DOC] Assemble the Phase 4 closure package: baseline/evidence inventory, expected-result register, workstream results, finding/retest ledger, proving evidence and Gate 4C dispositions, claim/limitation matrix, production-readiness disposition, TD-14 record, and Gate 4D decision record.

**Completion evidence:** A reviewable final validation and acceptance package that accurately separates evidence, claims, limitations, recommendations, and Project Owner decisions.

## Gate 4D — Phase 4 Exit Gate [GATE]

**Entry:** WS1–WS8 completion/evidence package and required findings dispositions are available for Project Owner review.

**The Project Owner must separately answer:**

1. Did Phase 4 complete according to the approved plan?
2. What claims are supported by the evidence?
3. What limitations remain?
4. What is the production-readiness disposition?
5. Should another phase be proposed?
6. Should that phase be authorized?

Questions 5 and 6 are separate decisions. Gate 4D PASS closes Phase 4 only; it does **not** automatically authorize another phase.

**Disposition:** **NOT APPROVED.**

## Planned Phase 4 exit criteria

Phase 4 may be presented for Gate 4D only when all of the following are evidenced:

- [ ] All mandatory workstreams are completed according to the approved plan, or any approved exception is explicit, bounded, and recorded.
- [ ] Required validation and proving evidence is preserved with adequate baseline, procedure, expected-result, result, and disposition traceability.
- [ ] No unresolved BLOCKER findings remain.
- [ ] No unresolved MATERIAL findings remain, except through a previously established and explicitly Project-Owner-approved exception mechanism.
- [ ] Required authorized remediation and retesting are completed and evidence-based.
- [ ] Semantic, governance, security, provenance, isolation, sufficiency, and construction-state invariants remain preserved.
- [ ] No unauthorized technology or scope change occurred; any material need was stopped and governed.
- [ ] No validation/proving-case overfitting, project-vocabulary special-casing, Consumer-specific special-casing, or expected-result manipulation occurred.
- [ ] TD-14 was correctly governed, including stopping/reopening through governance if the approved threshold was met.
- [ ] Mandatory proving exercises are completed with valid evidence, or a Project Owner decision explicitly establishes a governed non-completion/exception disposition before Gate 4D review.
- [ ] Supported and unsupported claims are explicitly separated; remaining limitations and future-work candidates are explicit and non-authorizing.
- [ ] Production readiness is explicitly dispositioned by the Project Owner.
- [ ] Final Project Owner approval is recorded at Gate 4D.

## Governing references

- [Phase 0 governance](../docs/phase-0/project-definition-governance.md)
- [Phase 1 baseline and traceability](../docs/phase-1/v0.1-baseline-and-traceability.md) and [conceptual model](../docs/phase-1/conceptual-context-model.md)
- [Phase 2 validation, proving architecture, and exit gate](../docs/phase-2/validation-proving-architecture-exit-gate.md)
- [Phase 3 master implementation checklist](checklist-phase-3-v0.1-implementation.md) and [Phase 3 closure record](../docs/phase-3/phase-3-closure.md)
- [Project roadmap](../docs/roadmap.md) and [AGENTS.md](../AGENTS.md)

This plan documents the approved Phase 4 master-plan/checklist design. It does not supersede the approved Phase 0–3 record, create Authority, authorize validation/proving/remediation, or establish production readiness.
