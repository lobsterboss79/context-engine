# WS2 Item 2.10 — Evidence-Coverage & Repeatability-Control Design Analysis

**Status:** **ANALYSIS COMPLETE / REPEATABILITY CONTROLS NOT YET AUTHORIZED**  
**Item status:** **2.10 remains INCOMPLETE.** This is analysis and proposed
control design only. It creates no fixture, expected result, addendum,
execution, evidence, finding, remediation, or completion disposition.

## 1. Exact committed baseline, authority, and boundary

This analysis began from clean committed `HEAD` `9e96753` (*Close Phase 4
Consumer capacity validation*). The committed baseline records Phase 4 in
progress; WS1 complete; Gate 4A PASS and Phase 4 execution authorized under the
validation-governance package; Items 2.1–2.9 complete; Item 2.6 complete with
active accepted limitation `DVL-P4-001`; and Items 2.10–2.11 incomplete but
authorized to proceed. Gate 4B is **NOT APPROVED**, fresh-Consumer
preflight/proving is **NOT AUTHORIZED**, TD-14 is **CLOSED / NOT REOPENED**, and
production readiness is **NOT ESTABLISHED**.

Approved Phase 0–3 requirements and architecture, not implementation output,
control meaning. Frozen expected results must precede execution; preserved
evidence must not be retrofitted to observed behavior. This document neither
changes that governance boundary nor creates authority from analysis.

## 2. Exact Item 2.10 wording and analysis-only obligations

The committed checklist says:

> **Validate deterministic repeatability and governed ordering/stability:
> identical controlled inputs must produce the established semantic result/order
> without filesystem order, hash iteration, row identifier, frequency, recency,
> or unapproved scoring becoming semantic rank.**

The following labels only decompose that wording; they do not alter it.

| Obligation | Analysis-only meaning | Current classification |
| --- | --- | --- |
| **2.10-A** | Repeated identical, controlled inputs produce the same established semantic result. | **NOT YET VALIDATED** |
| **2.10-B** | Repeated identical, controlled inputs produce the established semantic order. | **NOT YET VALIDATED** |
| **2.10-C** | Filesystem enumeration order does not become semantic rank. | **SUPPORTING EVIDENCE ONLY** |
| **2.10-D** | Hash/set/dictionary iteration does not become semantic rank. | **SUPPORTING EVIDENCE ONLY** |
| **2.10-E** | SQLite row identifier/insertion order does not become semantic rank. | **SUPPORTING EVIDENCE ONLY** |
| **2.10-F** | Frequency does not become semantic rank. | **SUPPORTING EVIDENCE ONLY** |
| **2.10-G** | Recency/currentness does not become semantic rank. | **SUPPORTING EVIDENCE ONLY** |
| **2.10-H** | No unapproved score or numerical ranking becomes semantic rank. | **SUPPORTING EVIDENCE ONLY** |
| **2.10-I** | Stability is assessed semantically, preserving required distinctions rather than demanding accidental byte identity. | **SUPPORTING EVIDENCE ONLY** |

Counts: **direct 0; supporting 7; not-yet validated 2; H3 0.** A and B
need deliberately repeated observations. C–I have architecture, code, frozen
control, and single-execution support, but no authorized order-perturbation or
repeatability execution proves them as an integrated result.

## 3. Why current evidence is not repeatability evidence

`VE-F1-001`, `VE-F2-001`, `VE-F3-001`, `VE-F4-A-001`, `VE-F4-B-001`,
`VE-F4-D-001`, `VE-F4-E-002`, `VE-F5-A-001`, `VE-F6-D-002`, `VE-F6-EF-001`,
and `VE-F6-J-001` each preserve one governed execution of their named frozen
control. A single execution can support the claimed semantic result; it cannot
show that the same controlled input repeats it, or that a non-semantic ordering
perturbation leaves it stable.

`VE-F4-E-001` and `VE-F4-E-002` are not a repeatability pair. The first is an
immutable FAIL against `ER-F4-E v1`; the second is an authorized retest after
the material integration remediation `R-F4-E-001`. Their implementation and
evidence circumstances differ, and their lineage proves preservation and
retest governance, not same-input/same-baseline repeatability.

`VE-F6-D-001` and `VE-F6-D-002` are likewise not a pair. D-001 is immutable
INDETERMINATE because its execution procedure supplied a wrong positional
`RoleInputs` value; D-002 is the controlled procedure-only correction. They do
not share identical controlled input and were not designed to test ordering.

Repeated regression-suite PASS counts are supporting only. They show that test
assertions passed at particular times, but are not frozen Item 2.10 end-to-end
controls; they do not preserve a semantic comparison contract, independently
identified controlled input/state, order perturbation, or validation evidence
record. Test repetition cannot manufacture validation coverage.

## 4. Frozen controls and fixture selection

F4-C, F5-B, and F5-C are frozen/unexecuted. They are not repeatability results
and execution cannot be inferred from their preparation. F4-C is disclosure
denial; F5-B/F5-C are relationship/provenance cases. They may be useful future
coverage but none supplies an existing repeatability pair.

**F3 is the preferred repeatability fixture.** `FX-F3 v1`/unchanged `ER-F3 v1`
already freezes a multi-item, competing-current-decision case: two competing
current Approved decisions retained as unresolved Conflict, historical
Supporting context, unverified availability, explicit currentness/history,
selection reasons, an Insufficient and coherent-with-qualification logical
package, and all three renderings. Its acceptance criterion expressly rejects
“newer-wins/order/model resolution.” It therefore has enough ordered,
semantically material structure to reveal instability without adding a new
domain behavior. F3’s original execution remains immutable and is not replaced
or rerun under ER-F3 itself.

## 5. Governed ordering mechanisms and incidental-order risks

The governing architecture requires deterministic, explainable selection and
preservation of Authority, Governance State, currentness/history, Conflict,
Uncertainty, provenance, limitations, sufficiency, and coherence. Phase 3
implements ordinary mechanisms consistent with that boundary: discovery
normalizes/sorts terms, source identifiers, expansions, exclusions, and
mechanisms; construction orders source-manifest entries by identity; rendering
uses one canonical ordered package view; and SQLite reads used for governed
records specify identity-based `ORDER BY` clauses. These are supporting
implementation evidence, not Item 2.10 proof.

Filesystem enumeration is potentially incidental: directory/native-Git or
adapter observation order can vary. It may control inspection mechanics only;
it cannot rank candidates, resolve conflict, or make a decision current. A
repeatability result must show that a controlled enumeration-order perturbation
does not alter the F3 semantic comparison model.

Hash/set/dictionary iteration is also incidental. The implementation converts
several collected values to sorted tuples and copies mapping inputs before use,
but Python insertion/history or hash iteration must not become selection order.
The control must test the observable integrated result, rather than infer it
from a code reading.

SQLite row IDs and insertion order are persistence mechanics, not semantics.
The approved physical architecture expressly says core semantics do not depend
on SQLite row IDs. A `row_id DESC` query exists only for the latest restore
qualification, whose result is explicitly historical and does not assert
currentness or Authority. Identity-ordered retrieval is supporting evidence;
the order-independence control must demonstrate that differing insertion order
does not change F3 result/order.

Frequency is not a relevance, applicability, selection, sufficiency, or rank
rule. A repeated token, representation, observation, or occurrence may be
evidence but does not acquire semantic preference merely by count. Recency is
also not automatic currentness: the decision pipeline evaluates explicit
currentness assessments and a current-task requirement; historical/superseded
state is preserved or qualified, not silently superseded by a newer timestamp.
F3 is specifically suited to this distinction.

No score is approved as semantic rank. The decision pipeline explicitly has no
score; Phase 2 prohibits invented numerical weighting or pseudo-objective
scores. Any control comparison must assess governed decisions and reasons, not
invent a scoring threshold or use counts, dates, or occurrence frequency as a
proxy rank.

## 6. Semantic comparison model and stability criterion

The comparison is **semantic stability**, not byte identity. Volatile evidence
metadata (execution time, temporary output path, Python/platform details,
SQLite physical bytes, audit timestamps, hashes of artifacts containing those
fields, and presentation whitespace) must not be required to match.

For F3 each run must instead match the frozen result and each other on: request,
fixture/configuration and governed scope; represented identities and
provenance; candidates and discovery/selection/applicability reasons; roles;
the two conflict participants and unresolved Conflict; historical versus
current/unverified qualifications; Required deficiency/ASU limitations;
logical-package membership and canonical semantic order; sufficiency
`Insufficient`; coherence `coherent_with_qualification`; and Human, ChatGPT,
and Codex meaning/order for material fields. No run may select a winner because
it was encountered first, newer, more frequent, given a row ID, or numerically
scored. Byte-identical raw JSON/rendering is neither required nor sufficient.

## 7. Complementary proposed controls

Two controls are required because they test distinct claims.

**R1 — identical-input repeatability.** Create a repeatability-specific,
additive ER/addendum referencing unchanged `ER-F3 v1`; do not revise ER-F3.
It should freeze the semantic comparison model, run count, clean committed
baseline/environment, identical F3 inputs, independent fresh state locations,
and expected semantic equivalence. Proposed minimum is **three** independent
runs: sufficient to compare more than one repetition while remaining a bounded
v0.1 control. Each run needs a newly initialized, isolated SQLite state/output
directory and no inherited database, audit, generated output, or process state.
It must preserve raw artifacts and a derived semantic comparison; no result may
be normalized by altering source input or ER after observation.

**R2 — incidental-order independence.** The same additive control family
should separately freeze a permitted perturbation matrix while retaining the
same F3 governed semantic inputs: reversed/permuted fixture source discovery
or observation presentation order; permuted construction/request mapping
insertion order; and deliberately different SQLite insertion order for
semantically identical records. It must not alter content, identities,
authority, authorization, timestamps/currentness assessments, relationships,
task, expected semantics, or source meaning. Any mechanism used to perturb
order must be reviewable, preserve the controlled input inventory, and avoid
introducing a production behavior, dependency, or unapproved rank/scoring rule.

R1 isolates repeatability under identical input. R2 challenges the proposition
that incidental mechanics are not semantic rank. Neither substitutes for the
other; both need Project Owner approval before control preparation and later
separate execution authorization.

## 8. Finding, H3, TD-14, and DVL-P4-001

No discrepancy has been observed because no Item 2.10 control ran. Therefore
**new Finding: not warranted** and **H3: not required** at this analysis stage.
An observed deviation from the pre-frozen semantic model would require
preservation and Item 2.11/finding governance; it must not be normalized away.

**TD-14 trigger not met.** Repeatability/order stability is not evidence that
relevant, authorized, in-scope information is materially or repeatedly
undiscoverable through deterministic mechanisms. TD-14 remains closed/not
reopened. `DVL-P4-001` remains active, unchanged, and materially separate: it
records Item 2.6-H inaccessible-Source direct-validation limitation. It neither
satisfies nor blocks the proposed F3 repeatability controls.

## 9. Completion standard, dependency, and Owner decisions

Item 2.10 can be completed only when Project Owner-approved, pre-results
repeatability-specific control(s) have preserved evidence showing the frozen
semantic comparison model across R1 isolated identical-input runs and R2
authorized incidental-order perturbations; all material F3 qualifications and
all renderer semantics/orders remain stable; no prohibited semantic rank is
observed; discrepancies are preserved and governed; and the Owner separately
accepts the evidence and completion disposition. This document does none of
those things.

Item 2.11 is not a hard checklist prerequisite to designing Item 2.10, but is
the required downstream discrepancy/finding-preservation route if R1 or R2
differs from the predetermined model. Item 2.10 does not begin Item 2.11.

Before any control action, the Project Owner must decide whether to:

1. Accept the A/B not-yet-validated and C–I supporting-only classifications.
2. Approve F3 as the fixture and the semantic (rather than byte) comparison model.
3. Approve additive repeatability ER/addendum(s) that reference unchanged
   `ER-F3 v1`, including R1’s three isolated runs.
4. Approve R2’s exact perturbation matrix and confirmation that it changes no
   governed semantic input, authority, or production behavior.
5. Approve later separate execution/evidence review, including the required
   discrepancy route, or reject/defer either control.
6. Separately accept or reject eventual Item 2.10 completion; no approval here
   authorizes Gate 4B, proving, TD-14 reopening, or production readiness.

## 10. Non-execution/non-change attestation

Only this analysis document was created. No R1/R2 control, repeatability
ER/addendum, ER-F3 change, F3 execution, repeatability run, application/source
code, test, checklist status, Finding, DVL-P4-001 entry, Gate 4B action,
proving authorization, TD-14 action, or production-readiness claim was made.
Referenced artifacts were inspected read-only. Item 2.10 remains incomplete.
