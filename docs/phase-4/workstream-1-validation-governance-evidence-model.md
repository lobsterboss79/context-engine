# Phase 4 Workstream 1 — Validation Governance & Evidence Model

**Status:** **ITEMS 1.1–1.17 COMPLETE — WORKSTREAM 1 COMPLETE.** Items 1.1–1.16 document Project Owner-approved decisions; Item 1.17 assembles their [pre-results validation-governance package](validation-governance-package/README.md). The package was reviewed at Gate 4A, which is **PASS — PROJECT OWNER APPROVED**; Phase 4 execution is **AUTHORIZED under the approved validation-governance package**. This authorization is not validation, proving, remediation, fresh-Consumer, or production-use evidence. TD-14 remains **CLOSED / NOT REOPENED**; Gate 4B remains **NOT APPROVED**; H3 remains controlling. See the [Gate 4A decision record](gate-4a-validation-plan-execution-authorization.md).

## Purpose, authority, and governing basis

This pre-results governance record documents the Project Owner-approved decisions for Workstream 1 Items 1.1–1.16. It is subordinate to the approved Phase 0–3 baseline and the [Phase 4 master plan and checklist](../../checklists/checklist-phase-4-validation-integration.md). It creates neither a result nor an authority to execute a planned validation or proving activity.

The governed semantic/design baseline comprises the applicable approved Phase 0–2 records, including:

- [Phase 0 project definition and governance](../phase-0/project-definition-governance.md): purpose, boundaries, governance, authority, security, success criteria, and non-goals;
- Phase 1 approved requirements, conceptual model, and baseline/traceability records, including [functional requirements](../phase-1/functional-requirements.md), [nonfunctional requirements](../phase-1/nonfunctional-requirements.md), [conceptual context model](../phase-1/conceptual-context-model.md), and [v0.1 baseline and traceability](../phase-1/v0.1-baseline-and-traceability.md);
- Phase 2 approved architecture, technology, security/governance, validation/proving, and exit-gate records, including [validation, proving architecture, and exit gate](../phase-2/validation-proving-architecture-exit-gate.md); and
- applicable approved decision records incorporated by those governing records.

The [Phase 3 closure record](../phase-3/phase-3-closure.md) identifies the completed implementation-level baseline and its closure evidence; it does not redefine Phase 0–2 expected semantics.

## 1.1 — Reference validation baseline

Phase 4 adopts a dual-baseline model.

### Governed semantic/design baseline

The approved Phase 0–2 records define what v0.1 is supposed to mean and do. They control the expected semantics for Phase 4, including applicable purpose/boundaries/governance, requirements, conceptual model, architecture, technology decisions, security/governance semantics, validation/proving architecture, and approved decision records.

Expected semantics must derive from these approved governing records. They must not be inferred merely from current implementation behavior.

### Implemented validation origin baseline

The immutable implementation origin baseline for Phase 4 is commit:

`9862497` — `Close Phase 3 v0.1 implementation`

This identifies the implementation initially being evaluated against the governed semantic/design baseline. The controlling rule is:

> Approved requirements, design, and governance define expected semantics; the identified implementation commit defines the implementation being evaluated against those semantics.

The Phase 4 origin baseline is immutable historical evidence. If later authorized remediation changes the implementation, the record must create a traceable **derived validation baseline**; it must not rewrite the origin baseline. Each derived baseline records, as applicable:

- its originating baseline;
- exact commit/version;
- reason for change;
- associated finding or findings;
- approving authority where required;
- affected validation/retest evidence; and
- scope of the baseline change.

The original `9862497` baseline remains preserved. Configuration and fixture provenance, plus every later approved baseline amendment with its authority and scope, must also be preserved.

## 1.2 — Four evidence levels

Phase 4 preserves four distinct evidence levels. Evidence at one level must not be represented as establishing a higher level unless the criteria and activities required for that higher level were actually performed and governed.

| Evidence level | Governing question | Scope and treatment |
| --- | --- | --- |
| **Implementation testing** | Does an implemented component behave as expected under its implementation-level tests? | Examples include Phase 3 pytest results, compilation checks, pip/package checks, entry-point validation, and similar implementation evidence. This is useful evidence input, but does not by itself establish Phase 4 integrated validation. |
| **Validation** | Does the integrated system behave according to approved requirements, semantics, architecture, governance, and security rules under controlled conditions? | Principally the future WS2–WS4 domain. |
| **Proving** | Can the validated system produce an adequate governed result for a real task when used by a genuinely fresh Consumer under a controlled proving protocol? | Principally the future WS5–WS6 domain. |
| **Production readiness** | Is sufficient evidence available to authorize the system for a specifically defined production use and operating environment? | Phase 4 may produce relevant evidence, but Phase 4 completion, validation PASS, or proving PASS does not inherently establish production readiness. |

Accordingly, implementation testing, validation, proving, and production readiness must not be collapsed into a single success claim.

## 1.3 — Evidence preservation

### Standard Validation Evidence Record

For each material validation exercise, create a Validation Evidence Record with the following applicable fields:

- stable Evidence ID;
- execution date/time;
- exact baseline, commit, or version;
- validation, checklist, or protocol item;
- governing requirement/design references;
- relevant environment/runtime;
- Bootstrap/configuration;
- exact controlled Sources, fixtures, or inputs;
- predetermined expected result;
- procedure or command;
- raw/original result;
- derived, processed, or rendered result where applicable;
- **PASS**, **FAIL**, or **INDETERMINATE** state;
- linked finding IDs;
- reviewer/evaluator;
- disposition; and
- lineage to related evidence, remediation, or retest.

Repository-conventional Markdown records and linked ordinary artifacts may represent this evidence. No new technology or tooling is introduced for evidence storage.

### Historical integrity, lineage, and proportionality

Original material evidence is immutable historical evidence. A later PASS must not overwrite an earlier **FAIL** or **INDETERMINATE**. Derived evidence retains lineage to its original evidence. The intended history is:

`Evidence V-001 -> FAIL -> Finding F-003 -> authorized remediation -> Evidence V-017 -> PASS`

not replacement of `V-001` with a successful rerun.

Evidence preservation is proportional. Routine passing validation need not retain every byte of successful command output indefinitely merely for completeness; it must retain enough evidence to substantiate and reproduce the result according to the approved methodology. Stronger preservation applies to:

- **FAIL** results;
- **INDETERMINATE** results;
- security/governance evidence;
- material findings;
- proving runs;
- gate evidence;
- material remediation/retest evidence; and
- evidence necessary to reconstruct a material conclusion.

The objective is trustworthy, reconstructable validation evidence, not conversion of Context Engine into an unrelated evidence-archiving system.

## 1.4 — Expected-result controls

Expected results must be established before associated validation execution. For every applicable validation case, the pre-execution record establishes:

`controlled input -> governed expectation -> acceptance criteria -> negative/failure criteria`

The same case record identifies the controlled fixture or Source identity, known applicable limitations, and the reviewer basis for evaluating the result.

Each expected result traces to an approved basis: an applicable requirement, conceptual-model invariant, architecture decision, governance/security rule, approved technology/behavior decision, or other approved governing record. Expected behavior must not be derived solely from current implementation behavior.

If observed behavior differs from the predetermined expectation, preserve the observed evidence and do not silently modify the expectation. Classify the result under the approved evidence rules; use **INDETERMINATE** where the evidence or approved record is insufficient or genuinely ambiguous; and create or escalate a finding where appropriate.

An unexpected result neither automatically proves the implementation defective nor automatically becomes correct behavior. Governed review distinguishes, with evidence, among such possibilities as:

1. implementation defect;
2. incorrectly derived expected result;
3. ambiguity in the approved governing record;
4. design/governance deficiency; or
5. another properly evidenced cause.

When governance legitimately changes an expected result, version it rather than rewriting its historical record. For example:

- `ER-017 v1 — original predetermined expectation`
- `ER-017 v2 — later governed revision`

The later version records its approving authority, reason, date/version, and affected evidence. The original expectation is never rewritten merely because execution produced a different result.

## 1.5 — Validation result states

Each validation exercise has one result state, linked to its preserved evidence and predetermined expected-result record.

| Result state | Meaning |
| --- | --- |
| **PASS** | The preserved evidence satisfies the predetermined expected result and acceptance criteria, with no unresolved discrepancy that invalidates the result. |
| **FAIL** | The preserved evidence demonstrates that one or more predetermined acceptance criteria were not satisfied, or that a defined failure condition occurred. |
| **INDETERMINATE** | The available evidence is insufficient to establish either **PASS** or **FAIL**. |

Evidence may be **INDETERMINATE**, for example, when it is incomplete, contradictory, materially contaminated, not reproducible where reproducibility is required, insufficient to evaluate the established expectation, or dependent on a genuinely ambiguous approved expectation or governing record.

The following rules control interpretation:

1. **INDETERMINATE** is not **PASS**.
2. **INDETERMINATE** cannot be silently treated as an absence of a finding or as successful validation.
3. **FAIL** describes the result of the exercise; it does not by itself establish root cause.
4. A **FAIL** therefore does not automatically establish an implementation defect.
5. Root cause, finding type, severity, and disposition are separate governed determinations.
6. Result states must remain linked to their preserved evidence and predetermined expected-result record.

## 1.6 — Finding severity model

Severity describes **impact**.

| Severity | Meaning and required treatment |
| --- | --- |
| **BLOCKER** | Continuing the affected activity would make subsequent evidence unsafe, invalid, materially misleading, or impossible to interpret reliably, or otherwise prevents safe/valid continuation. The affected activity stops pending governed disposition. |
| **MATERIAL** | The finding materially affects approved semantics; governance/security; validation/proving validity; an asserted material capability; approved scope; or another material Project decision or claim. H3 applies; the material decision requires Project Owner disposition. |
| **MINOR** | A bounded non-material defect, inconsistency, or discrepancy that does not materially invalidate the affected capability or evidence, but requires documented disposition. |
| **OBSERVATION** | Relevant evidence, lesson, condition, or potential future consideration that does not presently demonstrate a defect and does not presently require remediation. |

Severity does **not** describe implementation effort, remediation difficulty, code-change size, urgency by itself, or finding type. A one-line implementation defect may be **MATERIAL**; a complicated possible improvement may be only an **OBSERVATION**. Finding labels never reduce actual impact: H3 remains controlling where the real impact is material even if an initial label was lower.

## 1.7 — Finding type model

Each finding identifies one primary type. Secondary types may be recorded only where genuinely necessary to represent a cross-cutting finding; they do not eliminate the requirement for a primary type.

| Finding type | Meaning |
| --- | --- |
| **IMPLEMENTATION** | The implementation does not conform to already-approved behavior. |
| **INTEGRATION** | Individually functioning components fail to interact according to approved integrated behavior. |
| **SECURITY/GOVERNANCE** | Approved authorization, disclosure, isolation, Authority, Governance State, Provenance, or related security/governance controls are violated or inadequately preserved. |
| **OPERATIONAL** | Approved failure, recovery, persistence, backup, restore, diagnostic, or other in-scope operational behavior is deficient. |
| **DESIGN** | The implementation may correctly implement the approved design, but evidence indicates that the design itself may be inadequate, contradictory, incomplete, or incapable of satisfying an approved requirement or governed objective. |
| **PROVING-PROTOCOL** | Freshness, protocol design/execution, evidence integrity, uncontrolled intervention, procedure, or another proving control makes a proving result invalid or unreliable. |
| **CONSUMER-USABILITY** | The governed result may be technically correct, but evidence identifies a material or noteworthy difficulty for the intended Consumer in understanding, using, or meaningfully continuing from it. |

Severity and type are independent dimensions. For example, a finding may be **MATERIAL / DESIGN**, **MINOR / IMPLEMENTATION**, or **OBSERVATION / CONSUMER-USABILITY**. Do not infer severity from finding type or type from severity. Finding type may be revised through governed review as evidence develops, while preserving classification history and lineage rather than rewriting the historical record.

## 1.8 — Finding ownership, lifecycle, and disposition

The finding model separates who records or investigates a finding from who possesses authority to decide its material meaning or disposition. A finding record contains, as applicable:

- stable Finding ID;
- linked evidence/result IDs;
- concise finding statement;
- result state that exposed the issue;
- severity;
- primary finding type and secondary finding types where applicable;
- owner/investigator;
- cause analysis;
- current status;
- governed disposition and disposition authority;
- linked remediation authorization where applicable;
- remediation evidence and retest evidence where applicable;
- residual limitation where applicable;
- closure evidence; and
- lineage to superseded, duplicate, or related findings.

The lifecycle supports, as applicable:

`OPEN -> UNDER REVIEW -> DISPOSITIONED -> REMEDIATION AUTHORIZED -> RETEST PENDING -> CLOSED`

Not every finding must pass through every intermediate state. Findings may remain **OPEN** or otherwise unresolved when their governed disposition has not been completed.

### Governed disposition categories

| Disposition | Meaning |
| --- | --- |
| **NO CHANGE REQUIRED** | Evidence establishes that remediation is not required. Preserve rationale and authority. |
| **REMEDIATION AUTHORIZED** | A bounded corrective change has been authorized by the appropriate authority. This does not itself prove successful remediation; required retest and closure evidence remain necessary. |
| **DESIGN/GOVERNANCE REVIEW REQUIRED** | The finding requires a material or otherwise governed design/governance decision before corrective action may proceed. |
| **PROTOCOL/RUN INVALID — DISCARD/RESTART** | The validation/proving evidence basis is invalid for the applicable claim. The affected run must not be converted into **PASS** through repair or reinterpretation. |
| **ACCEPTED LIMITATION** | The appropriate authority explicitly accepts the condition as a bounded limitation. Preserve scope, rationale, impact, and any effect on claims. |
| **FUTURE-WORK CANDIDATE** | The evidence identifies potentially useful later work but does not authorize that work or expand current Phase 4 scope. |
| **DUPLICATE/SUPERSEDED** | Another governed finding or later record represents the finding. Preserve lineage; do not erase the historical finding. |

The following rules control ownership, disposition, and closure:

1. **Cause analysis is not disposition.** Codex or another investigator may gather evidence and identify a likely cause within approved boundaries. That does not grant authority to make a material architecture, technology, security, governance, semantic, scope, proving, or phase decision.
2. **Finding discovery is not remediation authorization.** A finding does not independently authorize application changes, design changes, expected-result changes, technology additions, or other remediation.
3. **Closure requires evidence.** A finding is not closed merely because code or documentation changed. Closure requires satisfaction of the governed disposition and the required closure/retest evidence.
4. **Preserve original evidence and classification history.** Later cause analysis, reclassification, remediation, or closure must not rewrite the original result or evidence.
5. **Materiality controls authority.** Where a finding is **MATERIAL**, **BLOCKER**, genuinely ambiguous, or otherwise triggers H3, Codex stops at the appropriate decision boundary and obtains Project Owner review.

### Distinguishing result, severity, type, and disposition

These dimensions must not be collapsed:

- **Result state** tells what happened in the exercise.
- **Severity** tells how much a finding matters.
- **Type** tells what kind of problem the evidence indicates.
- **Disposition** tells what governed action or status follows.

For example, a validation exercise may **FAIL**; that **FAIL** may create a finding classified **MATERIAL / DESIGN**; its governed disposition may be **DESIGN/GOVERNANCE REVIEW REQUIRED**. None of those facts independently authorizes remediation.

## 1.9 — H3 escalation and Codex remediation boundaries

Codex may correct an unambiguous implementation defect only when the approved behavior and permitted solution boundary are already established. Codex may not decide what the system ought to do when that answer requires a material or genuinely ambiguous judgment.

Within an authorized Phase 4 remediation context, Codex may perform ordinary remediation only when **all** applicable conditions are satisfied:

- the issue is an implementation or integration defect, or another bounded defect whose approved correction is already unambiguous;
- the approved expected behavior is clear from the governing record;
- the correction does not materially change architecture, approved semantics, security/governance policy, Authority/disclosure rules, technology/dependencies, persistent data-model behavior, Consumer/proving protocol, or Phase 4 scope;
- the correction introduces no new material tradeoff and remains within already-approved implementation boundaries;
- applicable remediation authority exists; and
- required evidence and retesting are performed.

For example, correcting an ordinary code defect that violates an already-approved deterministic ordering rule may be ordinary remediation. Deciding what that ordering rule should be is not ordinary remediation.

Codex must stop and escalate under H3 when remediation would require deciding, changing, or materially affecting requirements; approved semantics; architecture; technology or dependencies; material persistent data-model behavior; security/governance behavior; Authority; disclosure/authorization rules; Project isolation; Phase 4 scope; Consumer/proving protocol; an expected result that the governing record leaves genuinely ambiguous; TD-14; production-readiness criteria; another phase boundary; or another material Project decision.

The following controls are explicit:

- Finding discovery does not create remediation authority.
- **BLOCKER** or **MATERIAL** classification does not grant Codex additional remediation authority; materiality strengthens the escalation requirement.
- H3 controls actual impact regardless of an initial finding label.
- Project Owner approval is required before material remediation.
- Codex may investigate and cause-analyze within approved boundaries without that investigation becoming authority to make a material decision.

The concise boundary is: **Codex can repair an already-decided rule. Codex cannot invent the rule in order to repair the failure.**

## 1.10 — Remediation evidence and retest requirements

Each remediation is recorded in a stable **Remediation Record** linked to its applicable finding or findings. Before remediation, the record captures, as applicable:

- stable remediation identity and linked finding/evidence IDs;
- causal hypothesis/cause analysis;
- approved expected behavior and authorized change boundary;
- approving authority where required;
- originating validation baseline;
- affected components/semantics and anticipated regression surface; and
- required retest plan.

After remediation, it captures, as applicable:

- exact derived validation baseline, commit, or version;
- actual change boundary;
- focused retest evidence, affected-suite retest evidence, and relevant end-to-end regression-validation evidence;
- remaining/residual limitations;
- impact on earlier evidence and, where applicable, proving validity; and
- closure recommendation/disposition.

An implementation change creates a traceable derived validation baseline under Section 1.1. It does not rewrite the originating baseline or any original **FAIL**/**INDETERMINATE** evidence. Findings close only when the governed disposition and required evidence are satisfied.

### Impact-based retest levels

Retesting is impact-based; a small bounded remediation need not rerun every Phase 4 exercise merely for procedural completeness.

| Level | Question | Required treatment |
| --- | --- | --- |
| **LEVEL 1 — FOCUSED RETEST** | Did the remediation correct the exact behavior that exposed the finding? | Establish focused evidence for the corrected behavior. |
| **LEVEL 2 — AFFECTED-SUITE RETEST** | Did the remediation preserve related behavior and avoid regression in the reasonably affected area? | Establish evidence across the reasonably affected related behavior. |
| **LEVEL 3 — RELEVANT END-TO-END REGRESSION VALIDATION** | Does the integrated governed pipeline still behave correctly across the material boundaries through which the remediation could propagate? | Establish integrated evidence where those material boundaries are applicable. |

**MATERIAL** remediation presumptively requires every applicable retest level unless a governed record explicitly establishes why a level is not applicable. **BLOCKER** remediation requires evidence adequate to establish that the blocking condition is actually removed before affected continuation. Security/governance remediation requires testing adequate to evaluate both the corrected path and reasonably related enforcement paths.

If remediation affects behavior already used in proving, do not simply rerun an old proving procedure and declare the original result corrected. Explicitly assess whether the earlier proving evidence remains valid, whether its supported claims must be narrowed or invalidated, whether the Consumer is contaminated, and whether another genuinely fresh proving run is required. Any decision requiring material judgment remains governed by H3.

The required chain is:

`Finding -> governed cause/disposition -> authorized change boundary -> remediation -> focused retest -> affected-suite retest -> relevant end-to-end regression where applicable -> proving-validity assessment where applicable -> evidence-based closure`

## 1.11 — Anti-overfitting controls

The governing test for a proposed remediation is:

> Would the proposed remediation still be considered correct if the Company AI Roadmap and Context Engine proving cases did not exist?

A negative or materially uncertain answer warns that the remediation may be fitting a proving case rather than correcting a general governed mechanism.

Remediation must not depend on Project-name checks; privileged handling for Company AI Roadmap or Context Engine; Consumer identity; filenames specially treated merely because they occur in proving; expected-answer strings; proving-specific keywords; special ranking/selection rules invented to make a proving result pass; special semantic paths for a proving case; changing an expected result merely to match observed behavior; hidden self-knowledge; or an equivalent case-specific workaround absent an independently approved general requirement.

A legitimate remediation must trace:

`approved requirement / invariant -> general mechanism -> correction -> validation evidence`

not:

`proving failed -> special case -> proving passes`

A proving case may legitimately discover a general deficiency. Discovery through Company AI Roadmap or Context Engine dogfooding does not prevent remediation, but the correction must repair the general governed mechanism/invariant rather than encode the proving Project's identity or expected answer.

For material remediation discovered through proving, the Remediation Record requires a **Generalization Review** addressing:

1. What approved requirement/invariant was violated?
2. Can the proposed correction be stated without reference to the particular proving Project's identity?
3. Would the same mechanism apply to another Project presenting the same semantic/governance condition?
4. Is there at least one controlled non-proving regression case that demonstrates the general mechanism?

Where practical and within approved scope, a real proving exercise that reveals a general defect must convert the relevant general semantic condition into a deterministic controlled regression case. That case must model the general condition rather than unnecessarily copy Project-specific content. Future correctness must not depend solely on rerunning the original real-world proving case.

If the proposed remediation cannot satisfy the Generalization Review, or satisfaction would require a material design, semantic, or scope decision, Codex must stop under H3 for Project Owner review.

## 1.12 — Proving evidence preservation and independent evaluation

The controlling principle for every future proving run is:

> Preserve what the Consumer actually received and did before anyone attempts to explain, repair, improve, or reinterpret the result.

Proving evidence is stronger than ordinary routine validation preservation because it must establish the evidence boundary for a material proving claim. Each future proving run preserves the following four layers as applicable.

### Pre-run state

Before Consumer interaction, preserve the exact validation/implementation baseline; proving task/request; controlled or permitted Sources; frozen proving protocol; permitted Consumer inputs; predetermined success/failure criteria; known limitations; Consumer/session identity boundary to the degree required for evidence; exact freshness/preflight result; applicable authorization; and environment/configuration information necessary to reconstruct the run.

### Constructed evidence

Preserve the exact logical Context Package; Source Manifest and construction evidence; material Provenance, Conflict, Uncertainty, limitations, sufficiency state, and Construction-State Coherence where applicable; exact Consumer-facing rendering; and delivery boundary.

The following distinct states must not be collapsed:

`logical Context Package != rendering != delivery != receipt != use`

### Consumer interaction evidence

Preserve, as applicable, what was actually delivered; Consumer response/output; Consumer questions and clarification requests; interventions; additional information supplied after initial delivery; who or what supplied it; resulting Consumer outcome; evidence of meaningful continuation or inability to continue; material omissions noticed; inappropriate inclusions; and reconstruction burden where applicable.

Any post-delivery intervention remains distinguishable from the original Context Package and rendering. Later assistance must not be silently folded into the original proving result.

### Evaluation evidence

Preserve evaluator identity/role as appropriate; frozen criteria used; evaluation of the frozen original evidence; supported and unsupported conclusions; qualifications; findings; result state; and disposition/recommendation where appropriate. Evaluation occurs before remediation. No remediation, briefing, package correction, or system change may be treated as though it were part of the original run evidence.

### Independent evaluation

For Phase 4, independent evaluation does not inherently require an external commercial auditor or unrelated organization. It requires separation of evaluation from interactive alteration of the result under review. The evaluator may know the governing requirements, approved expected criteria, validation/proving protocol, and applicable semantic/governance rules, but evaluates the frozen evidence.

The evaluator must not simultaneously alter the Context Package; add missing context; repair the system; rewrite the Consumer rendering; coach the Consumer toward an expected answer; or modify success criteria after observing the result, then grade that altered result as though it were the original run. Where practicable, use a reviewer not responsible for changing the result under review.

Independent evaluation is evidence review, not authority to approve material Project decisions. Material proving conclusions remain subject to Project Owner review and acceptance or rejection at Gate 4C.

## 1.13 — Fresh-Consumer contamination protocol

A Consumer is fresh **for a particular proving run** when it does not possess material prior Project knowledge that would allow it to compensate for omissions, errors, ambiguity, insufficient context, or other deficiencies in the Context Package being proved. Freshness is run-specific, task-specific, and evidence-based. It is not an absolute metaphysical claim that the Consumer has never heard the Project name or has no general knowledge.

General, pretraining, or world knowledge is not automatically contamination. It is relevant when prior knowledge is sufficiently Project-specific and task-relevant that it could materially compensate for what the Context Engine was supposed to supply.

### Future preflight scope and evidence

The future actual preflight, when separately authorized, assesses as reasonably applicable: persistent/model memory; current conversation/context; Project/workspace context; connected files/Sources; prior sessions; prior Context Packages; prior proving runs/results; manual briefing; hidden/system/developer context where reasonably knowable; tool/connector state that may expose Project knowledge; and other plausible channels of material Project-specific/task-relevant knowledge.

For every relevant category, preserve the assessment basis, known exposure, unknown or uncertain exposure, whether the exposure is materially task-relevant, and evidence supporting the conclusion. This documentation does not perform a preflight, identify or test a Consumer, reserve a Consumer, or expose a Consumer to Project information.

### Freshness states and controls

| State | Meaning and control |
| --- | --- |
| **PASS** | There is reasonable evidence that the Consumer lacks material prior Project-specific/task-relevant knowledge that would undermine the proving objective. |
| **FAIL** | Material contamination is known to exist. The Consumer is unsuitable for the proving run. |
| **INDETERMINATE** | Freshness cannot reasonably be established because relevant exposure is unknown, contradictory, unverifiable, or otherwise insufficiently evidenced. The Consumer is unsuitable for the proving run. |

**INDETERMINATE is not PASS.** The standard is reasonable evidence of absence of material task-relevant Project knowledge, not impossible proof of absolute ignorance. Freshness must not be weakened because obtaining a fresh Consumer is inconvenient. Preserve the preflight evidence and decision.

The purpose of freshness is to prevent the Consumer from silently supplying material Project knowledge that should have come from the governed Context Package.

### AI Consumer control

An AI Consumer such as ChatGPT may potentially serve as a fresh Consumer only when the exact proving session/configuration can reasonably satisfy this approved protocol. Opening a new chat alone does not establish freshness. Potential contamination through memory, Project context, connected files/Sources, prior-session context, or other context channels must still be assessed. No actual ChatGPT/AI Consumer is identified, tested, reserved, or exposed by this documentation; that can occur only in the later authorized proving-readiness stage after the required gate.

## 1.14 — Reserved-Consumer protection and run-discard criteria

Treat a reserved candidate Consumer as an unused proving resource. Before the authorized preflight/proving run, do not expose that Consumer to material information including Project files for the proving Project; expected answer/outcome; intended Context Package; success/failure analysis; prior proving results; Project architecture, state, or decisions unnecessary for the authorized preflight; this planning conversation or equivalent material briefing; or other information that would materially contaminate the intended proving objective.

The reservation record, if later authorized, identifies the Consumer/session sufficiently to establish continuity and evidence lineage while avoiding unnecessary Project exposure. This documentation does not create an actual reservation.

### Automatic invalidation and distinction from valid failure

A proving run is **INVALID** for its intended proving claim and must be discarded/restarted, as applicable, when freshness is **FAIL** or **INDETERMINATE**; a material protocol breach occurs; the proving protocol materially changes after the run begins without governed restart; unauthorized Sources/context become available to the Consumer; the Consumer receives material manual assistance not permitted by the frozen protocol; original Context Package/rendering evidence is not adequately preserved; evaluator/interviewer intervention materially changes Consumer inputs before the original outcome is frozen; the wrong implementation/validation baseline, material configuration, or Bootstrap is used; a material uncontrolled event prevents reliable attribution or interpretation; or another condition invalidates the established evidence basis for the intended claim.

Preserve this distinction:

`VALID FAIL != INVALID RUN`

A valid **FAIL** can provide evidence about Context Engine. An invalid run does not establish the intended proving conclusion because its evidence basis is compromised.

### Invalid-run handling

When a run becomes invalid:

`preserve original evidence -> mark the run INVALID -> record the invalidation reason -> preserve relevant finding/protocol evidence -> exclude the run from proving-success claims -> restart under a valid frozen protocol with a fresh suitable Consumer when later authorized`

Do not clean up a contaminated Consumer and continue the same run; retroactively alter the protocol to make the run valid; remove unauthorized assistance from the record and pretend it did not occur; convert an invalid run into **FAIL** or **PASS** for convenience; or discard the historical evidence explaining invalidation. A protocol failure may itself create a **PROVING-PROTOCOL** finding even though the intended proving claim remains unestablished.

### Overall proving-integrity sequence

The intended future sequence is:

`freeze proving protocol and criteria -> establish exact-run Consumer freshness -> freeze/preserve package and rendering -> Consumer interaction -> freeze/preserve original outcome -> independent evaluation of frozen evidence -> Gate 4C evidence acceptance/rejection -> only then governed remediation where applicable`

No part of this sequence is executed by this documentation record. These controls preserve Items 1.1–1.11: original evidence remains immutable; **PASS**, **FAIL**, and **INDETERMINATE** remain distinct; finding severity/type/disposition remain independent; finding discovery does not authorize remediation; H3 and anti-overfitting controls remain controlling; and later remediation cannot retroactively convert an original proving run into a different result.

## 1.15 — TD-14 stop/reopening procedure

**TD-14 remains CLOSED / NOT REOPENED.** This procedure does not reopen TD-14, change the approved deterministic-discovery boundary, authorize a technology evaluation or selection, or authorize implementation. It documents the approved governed route by which future Phase 4 evidence may require the Project Owner to consider reopening TD-14.

### Reopening-candidate threshold

TD-14 becomes a **REOPENING CANDIDATE** only when preserved Phase 4 evidence demonstrates that relevant, authorized, in-scope information necessary to Required Context or an approved success criterion is materially or repeatedly undiscoverable through the approved deterministic discovery mechanisms, **and** that deficiency causes one or more of:

- incorrect context;
- insufficient context;
- material information loss; or
- inability to continue meaningfully.

The threshold is evidence-based. A single surprising result does not automatically establish it. This procedure retains the approved Phase 2 TD-14 materiality rule in [MN-I14-02](../phase-2/validation-proving-architecture-exit-gate.md#mn-i14-02--td-14-reopening-trigger), the approved initial deterministic foundation and semantic-assistance reopening seam in [TD-14/H14](../phase-2/technology-selection-physical-architecture.md#h14h15--additional-technology), and the Phase 3 closure disposition that TD-14 is closed.

### Non-triggers and stage distinction

TD-14 must **not** be treated as meeting the reopening threshold merely because:

- one poorly designed or invalid fixture fails;
- a Source was not actually within the Applicable Source Universe (ASU);
- information was unavailable, inaccessible, unauthorized, or unsupported by the controlled Sources;
- applicability correctly rejected a discovered Candidate Context item;
- selection correctly excluded an item;
- sufficiency correctly reported missing or inadequate Required Context;
- a configuration or Bootstrap error prevented correct discovery;
- an ordinary implementation defect caused the discovery failure, or the approved deterministic mechanism needs an ordinary already-governed implementation correction;
- a proving protocol or run is invalid;
- an LLM, vector, or semantic approach appears easier, more elegant, more powerful, or more convenient; or
- a useful future capability is desired.

Do not collapse the governed stages:

`discovery != applicability != selection != sufficiency`

Before identifying a reopening candidate, distinguish a genuine deterministic-discovery deficiency from a failure in another governed stage. In particular, a correct downstream rejection, exclusion, or inadequacy report does not establish that discovery failed; nor may a genuine discovery deficiency be relabeled as another stage merely to avoid TD-14 governance.

### TD-14 Reopening Evidence Record

Before the Project Owner is asked to reopen TD-14, create a reviewable **TD-14 Reopening Evidence Record** containing, as applicable:

- stable record/finding identity;
- exact request/task;
- exact validation baseline;
- exact configuration/Bootstrap;
- exact controlled Sources;
- ASU and its basis;
- relevant information that should have been discoverable, why it is relevant, and why it is authorized and in scope;
- why the information is necessary to Required Context or the applicable approved success criterion;
- deterministic discovery mechanisms exercised;
- predetermined expected discovery result and actual discovery result;
- preserved raw and derived evidence;
- repeat/reproduction evidence where applicable;
- downstream material consequence;
- linked finding or findings, including severity and type;
- analysis excluding ordinary implementation, configuration, and protocol causes;
- analysis distinguishing discovery from applicability, selection, and sufficiency;
- why the deficiency cannot be adequately resolved through existing approved deterministic mechanisms within the approved boundary;
- reviewer assessment; and
- Project Owner disposition.

When the approved reopening threshold is asserted, the applicable finding must be **MATERIAL** at minimum. If the evidence warrants **BLOCKER** treatment under the existing severity model, preserve that higher actual severity. Do not lower actual impact merely to fit this procedure.

### Stop behavior and authority boundary

When evidence appears to meet the threshold:

`STOP affected work -> preserve the original evidence -> create/register the applicable MATERIAL-or-higher finding -> identify potential TD-14 reopening -> assemble the TD-14 Reopening Evidence Record -> obtain Project Owner review`

Do **not** silently introduce AI-assisted discovery; embeddings; semantic search; vector indexing or database technology; model-based reranking; or altered deterministic-discovery semantics to avoid the governance decision. Do not treat the threshold as authorization to implement a new technology.

Meeting the threshold authorizes only **governed reconsideration** of TD-14. It does not reopen TD-14 automatically, select a replacement or additional technology, authorize AI-assisted discovery, authorize implementation, or authorize Phase 4 scope expansion. The Project Owner must explicitly decide whether TD-14 is reopened. If it is later reopened, technology evaluation and selection remain separate governed decisions.

## 1.16 — Material Phase 4 scope-change procedure

Evidence may create a reason to **consider** expanding or changing Phase 4 scope. Evidence does **not** itself expand or change Phase 4 scope. A useful, desirable, production-relevant, or technically attractive capability is insufficient by itself to add that capability to Phase 4. There must be a material relationship to the approved Phase 4 validation/integration/proving objective, and the required Project Owner decision must occur before the change enters Phase 4 scope.

The concise controlling rule is: **Evidence can force us to CONSIDER changing Phase 4. Evidence cannot silently CHANGE Phase 4.**

### Scope-Change Candidate Record

Before any material Phase 4 scope change, create a reviewable **Scope-Change Candidate Record** containing, as applicable:

| Record area | Required content |
| --- | --- |
| **Proposed change** | What exactly is proposed to enter, leave, or change in Phase 4? |
| **Triggering evidence** | What evidence caused consideration of the change? Link the applicable validation, proving, or finding evidence. |
| **Current boundary** | What approved boundary currently excludes or limits the proposed work, and why is it not already authorized? |
| **Material relationship to Phase 4** | Why is the change materially related to the approved validation/integration/proving objective? Is it actually required for Phase 4, or merely useful for future production or later work? |
| **Impact** | Assess the impacts listed below. |
| **Alternatives** | Assess the relevant evidence-supported alternatives listed below. |
| **Urgency/dependency** | State whether Phase 4 actually requires a decision now or whether the matter can be deferred without invalidating the approved Phase 4 objective. |
| **Recommendation** | Analysis may recommend a disposition, but recommendation is not authorization. |
| **Project Owner decision** | Record the explicit governed disposition. |

The impact assessment covers, as applicable: requirements; semantics; conceptual model; architecture; security/governance; Authority/disclosure; technology/dependencies; persistent data model; infrastructure/environment; validation methodology; expected results; existing validation evidence; proving protocol; Consumer freshness/proving validity; baseline; findings; gates; exit criteria; schedule/sequence; production-readiness disposition; and future phase boundaries.

Relevant alternatives include, where viable: continue Phase 4 without the change; defer the change to future work; use an already-approved mechanism; narrow the affected claim; accept a bounded limitation through proper governance; and other evidence-supported alternatives.

### Scope-change dispositions

| Disposition | Governed meaning |
| --- | --- |
| **APPROVE INTO PHASE 4** | The Project Owner explicitly approves a bounded amendment to Phase 4 scope. The record identifies the exact authorized boundary. |
| **DEFER TO FUTURE WORK** | Preserve the candidate and evidence without changing Phase 4 scope or authorizing implementation. |
| **REJECT** | The evidence does not justify the proposed Phase 4 scope change, or the Project Owner otherwise rejects it. |

A rejected or deferred candidate remains historical evidence where appropriate. Neither a candidate record nor an analysis/recommendation changes scope or authorizes implementation.

### Consequences of an approved scope change

If the Project Owner approves a material change into Phase 4, explicitly assess whether the amendment invalidates or requires revision/reapproval of the validation baseline; expected-result records; validation methodology; previous validation evidence; finding classifications/dispositions; remediation/retest requirements; proving protocol; Consumer freshness assumptions; prior proving evidence; Gate 4A, 4B, or 4C status; Phase 4 exit criteria; or another governed record.

Do not silently preserve a prior **PASS**, gate decision, or proving conclusion when the approved scope change materially invalidates its evidence basis. Any required amendment, revalidation, or reapproval must be explicit and traceable.

### Anti-scope-creep control

A capability being useful, desirable, production-relevant, or a reasonable future enhancement does not establish Phase 4 scope. This applies particularly to already identified future topics: backup scheduling; retention duration; deletion workflow; RPO/RTO; HA; daemon/service deployment; containers; cloud infrastructure; additional integration environments; broader deployment/infrastructure; automated Consumer action; and other production-readiness capabilities.

If Phase 4 evidence shows that any such topic is materially necessary to the approved Phase 4 objective, create a Scope-Change Candidate Record and stop at the applicable governance boundary. Do not silently add it.

### Relationship to TD-14

TD-14 reopening and a Phase 4 scope change are related but distinct governance questions. A TD-14 reopening candidate does not automatically reopen TD-14, change Phase 4 scope, authorize AI-assisted discovery, or select technology. A Phase 4 scope-change candidate does not automatically change Phase 4 scope, reopen TD-14, or authorize implementation.

If evidence implicates both TD-14 and Phase 4 scope, preserve both decision boundaries and obtain the applicable explicit Project Owner decisions. Do not collapse them into one authorization.

## Retained execution boundary

This record documents planning controls only. It does not execute Phase 4 validation or proving; create or run fixtures; perform a fresh-Consumer contamination preflight; reserve, test, or expose a fresh Consumer; modify application behavior; remediate implementation behavior; reopen TD-14; change Phase 4 scope; approve Gate 4A or Gate 4B; or establish production readiness. Material conflict, ambiguity, infeasibility, or need for a new material decision remains subject to H3 escalation and Project Owner review.
