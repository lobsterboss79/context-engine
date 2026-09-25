# Phase 4 Workstream 1 — Validation Governance & Evidence Model

**Status:** **ITEMS 1.1–1.8 COMPLETE — PROJECT OWNER-APPROVED DECISIONS DOCUMENTED.** Workstream 1 planning/documentation remains in progress. This record establishes no validation, proving, remediation, fresh-Consumer, or production-use authority. Gate 4A is **NOT APPROVED**; Phase 4 validation/proving execution is **NOT AUTHORIZED**. H3 remains controlling.

## Purpose, authority, and governing basis

This pre-results governance record documents the Project Owner-approved decisions for Workstream 1 Items 1.1–1.8. It is subordinate to the approved Phase 0–3 baseline and the [Phase 4 master plan and checklist](../../checklists/checklist-phase-4-validation-integration.md). It creates neither a result nor an authority to execute a planned validation or proving activity.

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

## Retained execution boundary

This record documents planning controls only. It does not execute Phase 4 validation or proving; create or run fixtures; perform a fresh-Consumer contamination preflight; reserve or expose a fresh Consumer; modify application behavior; remediate implementation behavior; reopen TD-14; approve Gate 4A; or establish production readiness. Material conflict, ambiguity, infeasibility, or need for a new material decision remains subject to H3 escalation and Project Owner review.
