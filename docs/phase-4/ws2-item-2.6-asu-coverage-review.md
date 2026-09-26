# WS2 Item 2.6 — ASU Establishment and Boundaries Coverage Review

**Status:** **REVIEW COMPLETE / ITEM 2.6 INCOMPLETE**

## 1. Status and boundary

This is a documentation and evidence-coverage review only.  It classifies
preserved Phase 4 evidence against the approved Item 2.6 obligations; it does
not execute a fixture, assign a validation result, create validation evidence,
alter frozen controls, remediate, or change application/source/test code.

Gate 4B remains **NOT APPROVED**.  Proving remains **NOT AUTHORIZED**.
TD-14 remains **CLOSED / NOT REOPENED**.  Production readiness is not
established.  This review does not mark Item 2.6 or Items 2.7–2.11 complete.

## 2. Exact review baseline

The review began from clean committed `HEAD`
`37f4dbe822c9024673ce12a2f839df30f391581c` — **Complete Phase 4
sufficiency validation**.  It reviews the committed records at that baseline,
including the immutable original `VE-F4-E-001` FAIL, its closed material
integration finding/remediation lineage, and the separate `VE-F4-E-002` PASS.

Classification vocabulary is used exactly as follows:

| Classification | Meaning in this review |
| --- | --- |
| **DIRECTLY VALIDATED** | Frozen expected-result controls deliberately exercised the behavior and preserved Phase 4 evidence directly demonstrates it. |
| **SUPPORTING EVIDENCE ONLY** | Preserved evidence is relevant but deliberately did not establish this separate obligation. |
| **NOT YET VALIDATED** | No preserved Phase 4 execution adequately demonstrates the obligation. |
| **AMBIGUOUS-H3** | Controlling semantics or required evidence are materially unclear or conflicting. |

There are no material conflicts in the approved semantic records relevant to
this review; no obligation is classified **AMBIGUOUS-H3**.

## 3. Governing semantic references

The controlling records are internally consistent and establish these limits:

- Phase 1 [conceptual model](../phase-1/conceptual-context-model.md) defines
  ASU as the governed potentially applicable Source/Source-scope universe,
  distinguishes adequately established, known-incomplete, and
  adequacy-unestablished universes, and requires negative results to remain
  scoped to the inspected universe (especially the ASU and selection passages).
- Phase 2 [Source and Observation Architecture](../phase-2/source-observation-architecture.md), C5, SA-05, OBS-04, and C12, distinguishes Registered,
  Applicable, and Observed sets; requires visible unavailable, inaccessible,
  unauthorized, unsupported, partial, failed, and unknown limitations; and
  says no-answer results are scoped to inspected evidence.
- Phase 2 [Discovery, Selection, and Sufficiency Architecture](../phase-2/discovery-selection-sufficiency-architecture.md), DS-07, RC-02, RC-08–09,
  E12–E14, and E17, separates discovery, applicability, selection, and
  sufficiency; requires ASU adequacy for unqualified sufficiency; preserves
  negative-result boundaries; and defines evidence-driven bounded
  iteration/termination and authorization/capability boundaries.
- Phase 3 [WS4](../phase-3/workstream-4-project-source-lifecycle.md) records
  explicit request, Source boundary, non-empty establishment basis, and the
  `adequate` / `known_incomplete` / `indeterminate` ASU states.  [WS6](../phase-3/workstream-6-deterministic-discovery.md), especially §§17–25, requires
  explicit ASU/basis, initial and expanded inspected Sources, expansion basis,
  limitations, and deterministic termination; expansion is an authorized,
  one-hop, deficiency-based action, not crawling.  [WS8](../phase-3/workstream-8-sufficiency-package-construction.md), §§7–19, preserves Source
  limitations into sufficiency/package construction and distinguishes bounded
  negative results from universal absence.
- The approved TD-14 threshold is Phase 2 [MN-I14-02](../phase-2/validation-proving-architecture-exit-gate.md#mn-i14-02--td-14-reopening-trigger): relevant,
  authorized, in-scope information necessary to Required Context or a success
  criterion must be materially or repeatedly undiscoverable through approved
  deterministic mechanisms, causing incorrect/insufficient context or material
  harm to meaningful continuation.

These records do not equate unavailable with inaccessible, authorization with
availability, static multi-Source scope with expansion, Candidate/applicability
exclusion with a negative discovery result, or known-incomplete with
indeterminate.  They also do not require an invented unsupported Source type.

## 4. Evidence reviewed

Reviewed preserved execution records: `VE-F1-001`, `VE-F2-001`, `VE-F3-001`,
`VE-F4-A-001`, `VE-F4-B-001`, immutable `VE-F4-E-001`, remediation retest
`VE-F4-E-002`, and `VE-F4-D-001`; plus `F-F4-E-001` and `R-F4-E-001` for
original-FAIL/remediation lineage.  The underlying raw results, package and
renderer artifacts linked by those records were considered where needed.

Reviewed frozen, unexecuted controls: `FX/ER-F4-C`, `FX/ER-F5-A`,
`FX/ER-F5-B`, and `FX/ER-F5-C`, in the fixture and expected-result registers.
Their pre-execution status is potential coverage only, never execution
evidence.

## 5. Requirement-by-requirement coverage matrix

| Obligation | Classification | Governing semantic references | Exact Phase 4 evidence | Observed behavior; why it does or does not satisfy | Residual gap |
| --- | --- | --- | --- | --- | --- |
| **2.6-A — ASU establishment / basis** | **DIRECTLY VALIDATED** | P1 conceptual model ASU; P2 C5; P3 WS4 §9; P3 WS6 §§17–21 | `VE-F1-001`; corroborated by `VE-F2-001`, `VE-F3-001`, `VE-F4-A-001`, `VE-F4-B-001`, `VE-F4-E-002`, `VE-F4-D-001` | F1 deliberately established an explicit two-Source ASU from Bootstrap/Project registration and task mapping; the boundary record states `adequate`, and package/renderer preserve ASU/sufficiency/coherence. Later records independently preserve explicit fixture ASU bases rather than infer adequacy from Source count. | No gap for establishment/basis itself. This does not prove every adequacy state or expansion. |
| **2.6-B — adequate ASU** | **DIRECTLY VALIDATED** | P1 ASU; P2 C5; P2 E12; P3 WS4 §9; P3 WS8 §§7–9 | `VE-F1-001`, `VE-F2-001`, `VE-F3-001`, `VE-F4-A-001`, `VE-F4-D-001`; `VE-F4-E-002` for its bounded ASU | Each named execution deliberately used a frozen `adequate` ASU with an explicit basis. F1/F2/F4-A/F4-D produced sufficient packages under their separate controls; F3 remained insufficient for conflict despite adequate ASU, directly showing ASU is distinct from sufficiency. E-002 establishes adequacy only for the separately supplied bounded task. | No gap for adequate-ASU behavior. It does not establish broad-ASU adequacy or bounded expansion. |
| **2.6-C — known-incomplete ASU** | **DIRECTLY VALIDATED** | P1 ASU; P2 C5/C12; P2 E12–E14; P3 WS4 §10; P3 WS8 §§7–15 | `VE-F4-B-001`; immutable `VE-F4-E-001`; `VE-F4-E-002` | F4-B deliberately preserves named `SRC-F4B-REQUIRED-MISSING` as an unavailable Required Source in a `known-incomplete` ASU; it remains a RequiredDeficiency and makes the package insufficient. E-002 separately preserves the broad named unavailable Required Source and broad `known_incomplete` ASU through logical package and every rendering. The original E-001 omission remains preserved as a FAIL, not overwritten. | No gap for known-incomplete behavior and known missing/unavailable boundary preservation. It is not evidence of indeterminate ASU. |
| **2.6-D — indeterminate ASU** | **NOT YET VALIDATED** | P1 ASU; P3 WS4 §9; P3 WS8 §9 | None that deliberately invokes `indeterminate` | The evidence exercises `adequate` and `known-incomplete`, both of which presuppose a different basis than inability to establish adequacy. No preserved Phase 4 run makes ASU adequacy unestablished/indeterminate and preserves its resulting qualification. | Deliberate controlled indeterminate-ASU execution and preservation are absent. |
| **2.6-E — scoped negative results** | **SUPPORTING EVIDENCE ONLY** | P1 conceptual model (scoped “not found”); P2 C5/C12; P2 RC-08; P3 WS6 §§19–21 | `VE-F2-001`; `VE-F1-001`; `VE-F3-001` | F2 proves a represented item can be non-Candidate and another Candidate can be inapplicable, with exclusion reasons retained. Those are not “nothing found within inspected ASU” results. F1 records deterministic discovery without exclusion/expansion, and F3 records full Candidates under static scope; neither freezes and evaluates a no-result outcome with inspected boundary, limitations, and non-universal meaning. | A deliberately controlled negative/no-result with explicit inspected ASU/scope, state, and limitation is not yet directly validated. |
| **2.6-F — bounded expansion** | **SUPPORTING EVIDENCE ONLY** | P1 bounded cross-Project traversal; P2 E13/E17; P3 WS6 §§21–25; P3 WS8 §19 | `VE-F1-001`; static multi-Source `VE-F3-001`; two-scope `VE-F4-E-001` / `VE-F4-E-002` | F1 has deterministic termination but no expansion. F3’s four Sources were a statically declared ASU, not initial Sources followed by a governed expansion. E-001/E-002 distinguish a broad known-incomplete ASU from a bounded adequate ASU for a separately supplied task; they do not add Sources through an expansion request. Thus the records support the distinction but do not exercise initial set, deficiency trigger/basis, newly inspected Sources, bounded stop, and resulting scope. | No direct bounded-expansion execution. |
| **2.6-G — unavailable limitation** | **DIRECTLY VALIDATED** | P1 ASU/package limitations; P2 C5, SA-05, E12–E14; P3 WS4 §10; P3 WS8 §15 | `VE-F4-B-001`; `VE-F4-E-001`; `VE-F4-E-002` | F4-B deliberately retained a named unavailable Required Source as a limitation rather than absence, substitution, or fabricated content. E-002 confirms the same broad unavailable Required deficiency and limitation after remediation through package/rendering. | No gap for unavailable handling. This evidence must not be relabeled inaccessible. |
| **2.6-H — inaccessible limitation** | **SUPPORTING EVIDENCE ONLY** | P1 ASU; P2 SA-05/OBS-04; P2 E12–E14; P3 WS4 §10; P3 WS6 §19 | `VE-F4-B-001`; `VE-F4-E-001` / `VE-F4-E-002` | These runs preserve unavailable Sources and are relevant to limitation handling, but none establishes a Source that exists and is in scope yet cannot be read via the approved mechanism. The governing records explicitly distinguish the states. | Direct inaccessible-Source observation/limitation/package-or-rendering preservation is absent. |
| **2.6-I — unauthorized limitation** | **NOT YET VALIDATED** | P1 ASU and authorization-bound explanation; P2 C5, E13 T-04, E14; P3 WS6 §19 | No executed F4-C/F5 evidence | Existing runs contain authorized requester/Consumer fields, but authorization configuration is not unauthorized-path validation. F4-B/E are unavailable, not authorization-denied. F4-C and F5-A are frozen but unexecuted. | A deliberate Source exclusion or inability to inspect due to authorization/governance, with preserved non-disclosing limitation, is not validated. |
| **2.6-J — unsupported limitation** | **NOT YET VALIDATED** | P1 Source adapter boundary; P2 SA-05/C12; P2 E13 T-05; P3 WS4 §10; P3 WS6 §19; P3 WS8 §15 | No preserved Phase 4 execution | Phase 3 documents supported capability semantics, but no Phase 4 fixture execution deliberately presents an otherwise relevant Source/mechanism that the approved implementation cannot handle and preserves an unsupported limitation. No unsupported technology or type is inferred from a gap. | Direct evidence is absent; an actual approved relevant unsupported condition would be needed before validation design. |
| **2.6-K — limitation preservation** | **DIRECTLY VALIDATED** | P1 package limitation preservation; P2 E10/E14; P3 WS8 §§15–25; P3 WS9 rendering boundary | `VE-F4-B-001`; immutable `VE-F4-E-001`; `F-F4-E-001`; `R-F4-E-001`; `VE-F4-E-002` | F4-B preserves unavailable Required/ASU limitation through the insufficient logical package and all renderings. E-001 directly exposed the material integration omission of broad ASU/two-scope qualification, which was preserved as immutable FAIL. E-002 then directly verifies the corrected general qualification in package and all renderings while retaining original evidence and remediation lineage. | No gap for preservation where the demonstrated unavailable/known-incomplete limitations occur. It does not substitute for proving inaccessible, unauthorized, or unsupported limitations. |

Coverage count: **5 DIRECTLY VALIDATED** (A, B, C, G, K); **3 SUPPORTING
EVIDENCE ONLY** (E, F, H); **3 NOT YET VALIDATED** (D, I, J); **0
AMBIGUOUS-H3**.

## 6. Frozen-but-unexecuted potential coverage

**FROZEN POTENTIAL COVERAGE != VALIDATED EVIDENCE.** None of the following
records changes the matrix classifications until separately authorized,
executed against its frozen expected result, and preserved/reviewed.

| Frozen fixture | Predetermined semantics relevant to Item 2.6 | Potential future coverage | Limit |
| --- | --- | --- | --- |
| `FX/ER-F4-C v1` | Available adequate ASU; requester may inspect but Consumer disclosure of Required material is denied; non-sensitive denial/qualification is required. | Authorization-limitation preservation at package/rendering boundary; potentially supporting 2.6-I/K. | It is a Consumer-disclosure denial, not clearly a Source inspection exclusion/inaccessibility; alone it does not meet the exact 2.6-I Source-path obligation. |
| `FX/ER-F5-A v1` | No governed Atlas–Beacon relationship; cross-Project requester authorization denied; discovery/traversal stops at Atlas and Beacon is outside effective discovery/ASU. | Best existing frozen candidate for 2.6-I: authorization/governance causes Source exclusion and preserves no-Beacon outcome. | It contains no unavailable/inaccessible/unsupported condition, no negative-result inspection record, and no expansion. |
| `FX/ER-F5-B v1` | One already bounded authorized traversal reaches Beacon, whose item is Candidate but inapplicable/excluded. | Supporting cross-Project boundary/applicability evidence only. | It is not a scoped negative result and does not state an initial set, deficiency-driven expansion trigger, expansion request, or stopping condition required by 2.6-F. |
| `FX/ER-F5-C v1` | Named authorized Beacon Source is included as Supporting context under a bounded relationship. | Supporting evidence for static bounded cross-Project ASU and limitation/provenance distinction. | It is not bounded discovery expansion; its two Sources are statically governed for the request. |

No frozen unexecuted fixture is predesigned for indeterminate ASU, a scoped
negative result, a deficiency-driven expansion, inaccessible Source handling,
or unsupported capability handling.

## 7. Residual validation gaps

The unresolved obligations are: direct indeterminate-ASU evidence (2.6-D);
direct scoped negative-result evidence (2.6-E); direct bounded-expansion
evidence (2.6-F); direct inaccessible limitation evidence (2.6-H); direct
unauthorized Source-path evidence (2.6-I); and direct unsupported limitation
evidence (2.6-J).  Supporting records do not close any of those gaps.

## 8. Minimum future validation-scenario grouping

This is grouping only; it does not design fixtures, expected results, or
execution procedures.

| Minimum scenario | Obligations covered | Existing frozen fixture usable? | Why needed |
| --- | --- | --- | --- |
| Authorization-governance exclusion | 2.6-I | Yes: `FX-F5-A v1` appears usable. | Its frozen premise is a denied cross-Project authorization that stops traversal before representation and should preserve the boundary without treating configuration alone as evidence. |
| Indeterminate evidence boundary | 2.6-D | No. | A controlled ASU must have adequacy genuinely not establishable as adequate or known-incomplete, with qualification preserved. |
| Deficiency-driven bounded expansion ending in a scoped result | 2.6-E, 2.6-F | No. | One coherent scenario can establish initial inspected Sources, authorized governed deficiency/expansion basis, newly inspected Sources, bounded termination, and a resulting explicitly scoped no-result (or otherwise scoped result). It must not be static multi-Source scope. |
| Existing but unreadable in-scope Source | 2.6-H | No. | It must distinguish access failure from absence/unavailability and preserve the limitation at the applicable downstream boundary. |
| Relevant unsupported capability | 2.6-J | No. | It requires a real approved relevant unsupported condition, not an invented technology/type, and preservation of the limitation. |

## 9. TD-14 assessment

**TD-14 TRIGGER NOT MET.**

`VE-F1-001` demonstrates a normal deterministic result in an adequate ASU;
`VE-F2-001` demonstrates Candidate and applicability exclusions, not a
deterministic discovery deficiency; `VE-F4-B-001` and `VE-F4-E-001/E-002`
demonstrate named unavailable Required Sources and appropriately preserve the
resulting insufficiency/qualification; no execution demonstrates inaccessible,
unauthorized, or unsupported discovery.  No preserved evidence demonstrates
bounded-expansion exhaustion, nor materially or repeatedly undiscoverable
relevant, authorized, in-scope Required Context through approved deterministic
mechanisms that causes incorrect/insufficient context or material harm.

The coverage gaps mean the required cases have not yet been validated; they do
not themselves show deterministic discovery failure.  No AI/vector/model-based
discovery recommendation follows from this review.

## 10. Recommended next validation step

Seek the separately authorized next WS2 validation decision for the smallest
already-frozen match: execute and review `FX-F5-A v1` if the Project Owner
authorizes it for the unauthorized-boundary obligation.  The remaining gaps
need future governed fixture design/expected-result approval before execution;
this review does not design them.

## 11. Non-execution attestation

No fixture was executed for this review.  No Validation Evidence Record,
PASS/FAIL/INDETERMINATE result, finding, remediation, expected-result change,
fixture change, application/source/test change, Gate 4B action, proving action,
or TD-14 action was made.  Item 2.6 remains **INCOMPLETE**; Items 2.7–2.11
remain unchanged.
