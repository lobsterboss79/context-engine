# WS2 Item 2.6 — ASU Establishment and Boundaries Coverage Review

**Status:** **REVIEW COMPLETE / ITEM 2.6 COMPLETE WITH ACCEPTED VALIDATION LIMITATION**

## 1. Status and boundary

This is a documentation and evidence-coverage review only.  It classifies
preserved Phase 4 evidence against the approved Item 2.6 obligations; it does
not execute a fixture, assign a validation result, create validation evidence,
alter frozen controls, remediate, or change application/source/test code.

Gate 4B remains **NOT APPROVED**.  Proving remains **NOT AUTHORIZED**.
TD-14 remains **CLOSED / NOT REOPENED**.  Production readiness is not
established. The later Project Owner final disposition marks Item 2.6
**COMPLETE WITH ACCEPTED VALIDATION LIMITATION**; it does not alter the
evidence classifications below or complete Items 2.7–2.11.

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
`VE-F4-E-002`, `VE-F4-D-001`, `VE-F5-A-001`, immutable procedure-deficient
`VE-F6-D-001`, faithful retest `VE-F6-D-002`, `VE-F6-EF-001`, and `VE-F6-J-001`; plus `F-F4-E-001` and
`R-F4-E-001` for original-FAIL/remediation lineage. The underlying raw
results, package and renderer artifacts linked by those records were considered
where needed.

Reviewed frozen, unexecuted controls: `FX/ER-F4-C`, `FX/ER-F5-B`, and
`FX/ER-F5-C`, in the fixture and expected-result registers.
Their pre-execution status is potential coverage only, never execution
evidence.

## 5. Requirement-by-requirement coverage matrix

| Obligation | Classification | Governing semantic references | Exact Phase 4 evidence | Observed behavior; why it does or does not satisfy | Residual gap |
| --- | --- | --- | --- | --- | --- |
| **2.6-A — ASU establishment / basis** | **DIRECTLY VALIDATED** | P1 conceptual model ASU; P2 C5; P3 WS4 §9; P3 WS6 §§17–21 | `VE-F1-001`; corroborated by `VE-F2-001`, `VE-F3-001`, `VE-F4-A-001`, `VE-F4-B-001`, `VE-F4-E-002`, `VE-F4-D-001` | F1 deliberately established an explicit two-Source ASU from Bootstrap/Project registration and task mapping; the boundary record states `adequate`, and package/renderer preserve ASU/sufficiency/coherence. Later records independently preserve explicit fixture ASU bases rather than infer adequacy from Source count. | No gap for establishment/basis itself. This does not prove every adequacy state or expansion. |
| **2.6-B — adequate ASU** | **DIRECTLY VALIDATED** | P1 ASU; P2 C5; P2 E12; P3 WS4 §9; P3 WS8 §§7–9 | `VE-F1-001`, `VE-F2-001`, `VE-F3-001`, `VE-F4-A-001`, `VE-F4-D-001`; `VE-F4-E-002` for its bounded ASU | Each named execution deliberately used a frozen `adequate` ASU with an explicit basis. F1/F2/F4-A/F4-D produced sufficient packages under their separate controls; F3 remained insufficient for conflict despite adequate ASU, directly showing ASU is distinct from sufficiency. E-002 establishes adequacy only for the separately supplied bounded task. | No gap for adequate-ASU behavior. It does not establish broad-ASU adequacy or bounded expansion. |
| **2.6-C — known-incomplete ASU** | **DIRECTLY VALIDATED** | P1 ASU; P2 C5/C12; P2 E12–E14; P3 WS4 §10; P3 WS8 §§7–15 | `VE-F4-B-001`; immutable `VE-F4-E-001`; `VE-F4-E-002` | F4-B deliberately preserves named `SRC-F4B-REQUIRED-MISSING` as an unavailable Required Source in a `known-incomplete` ASU; it remains a RequiredDeficiency and makes the package insufficient. E-002 separately preserves the broad named unavailable Required Source and broad `known_incomplete` ASU through logical package and every rendering. The original E-001 omission remains preserved as a FAIL, not overwritten. | No gap for known-incomplete behavior and known missing/unavailable boundary preservation. It is not evidence of indeterminate ASU. |
| **2.6-D — indeterminate ASU** | **DIRECTLY VALIDATED** | P1 ASU; P3 WS4 §9; P3 WS8 §9 | `VE-F6-D-002` PASS; with immutable procedure-deficient predecessor `VE-F6-D-001` INDETERMINATE | The authorized named-argument retest deliberately exercised frozen `FX-F6-D v1` / `ER-F6-D v1`. It preserves the nonempty known-boundary basis, `indeterminate` (not adequate or known-incomplete), no invented particular gap, Insufficient unbounded-task result, `coherent_with_qualification`, and the limitation through logical package and all renderings. | No gap for direct indeterminate-ASU behavior. The original INDETERMINATE remains historical evidence and is not reclassified. |
| **2.6-E — scoped negative results** | **DIRECTLY VALIDATED** | P1 conceptual model (scoped “not found”); P2 C5/C12; P2 RC-08; P3 WS6 §§19–21 | `VE-F6-EF-001` PASS | The authorized frozen E+F control inspected origin only first, found zero exact matching Candidates, and then completed the sole governed expansion. Its logical package and all three renderings preserve “not found within the governed inspected ASU” without asserting universal absence. | No gap for the scoped result within this governed bounded reporting task. |
| **2.6-F — bounded expansion** | **DIRECTLY VALIDATED** | P1 bounded cross-Project traversal; P2 E13/E17; P3 WS6 §§21–25; P3 WS8 §19 | `VE-F6-EF-001` PASS | The E+F control preserves distinct initial `[origin]` and expanded `[target]` inspection evidence, the material/resolvable authorized deficiency, represented relationship, pre-frozen one-hop `ExpansionRequest`, and termination after the sole approved target. The ASU was already two-Source adequate; expansion changed inspection only. | No gap for direct one-hop bounded-expansion behavior. |
| **2.6-G — unavailable limitation** | **DIRECTLY VALIDATED** | P1 ASU/package limitations; P2 C5, SA-05, E12–E14; P3 WS4 §10; P3 WS8 §15 | `VE-F4-B-001`; `VE-F4-E-001`; `VE-F4-E-002` | F4-B deliberately retained a named unavailable Required Source as a limitation rather than absence, substitution, or fabricated content. E-002 confirms the same broad unavailable Required deficiency and limitation after remediation through package/rendering. | No gap for unavailable handling. This evidence must not be relabeled inaccessible. |
| **2.6-H — inaccessible limitation** | **SUPPORTING EVIDENCE ONLY** | P1 ASU; P2 SA-05/OBS-04; P2 E12–E14; P3 WS4 §10; P3 WS6 §19 | `VE-F4-B-001`; `VE-F4-E-001` / `VE-F4-E-002` | These runs preserve unavailable Sources and are relevant to limitation handling, but none establishes a Source that exists and is in scope yet cannot be read via the approved mechanism. The governing records explicitly distinguish the states. | Direct inaccessible-Source observation/limitation/package-or-rendering preservation is absent. |
| **2.6-I — unauthorized limitation** | **DIRECTLY VALIDATED** | P1 ASU and authorization-bound explanation; P2 C5, E13 T-04, E14; P3 WS6 §19 | `VE-F5-A-001` | F5-A deliberately establishes an Atlas-only adequate ASU while a controlled Beacon Source identity exists outside a governed relationship. Cross-Project Requester authorization is denied and Consumer disclosure is not established. Beacon is explicitly uninspected before observation/representation/Candidate use; no Beacon content enters applicability, selection, package, or renderings. This is preserved as an authorization/governance boundary, not absence, unavailable, inaccessible, unsupported, or indeterminate ASU. | No gap for the unauthorized Source-path obligation. It does not establish inaccessible or unsupported handling. |
| **2.6-J — unsupported limitation** | **DIRECTLY VALIDATED** | P1 Source adapter boundary; P2 SA-05/C12; P2 E13 T-05; P3 WS4 §10; P3 WS6 §19; P3 WS8 §15 | `VE-F6-J-001` PASS | The authorized frozen F6-J control establishes an otherwise available, accessible, requester-authorized, supported, in-scope Source with a relevant Required PDF Artifact. The existing capability check reports `unsupported-artifact-type` before content parsing. Zero Artifact-derived represented information/Candidates result; the explicit Required deficiency produces Insufficient, `coherent_with_qualification`, package preservation, and faithful Human/ChatGPT/Codex renderings without collapsing Source and Artifact state. | No gap for direct unsupported-Artifact-capability handling. It does not alter H's inaccessible-Source limitation. |
| **2.6-K — limitation preservation** | **DIRECTLY VALIDATED** | P1 package limitation preservation; P2 E10/E14; P3 WS8 §§15–25; P3 WS9 rendering boundary | `VE-F4-B-001`; immutable `VE-F4-E-001`; `F-F4-E-001`; `R-F4-E-001`; `VE-F4-E-002` | F4-B preserves unavailable Required/ASU limitation through the insufficient logical package and all renderings. E-001 directly exposed the material integration omission of broad ASU/two-scope qualification, which was preserved as immutable FAIL. E-002 then directly verifies the corrected general qualification in package and all renderings while retaining original evidence and remediation lineage. | No gap for preservation where the demonstrated unavailable/known-incomplete limitations occur. It does not substitute for proving inaccessible, unauthorized, or unsupported limitations. |

Coverage count: **10 DIRECTLY VALIDATED** (A, B, C, D, E, F, G, I, J, K); **1 SUPPORTING
EVIDENCE ONLY** (H); **0 NOT YET VALIDATED**; **0
AMBIGUOUS-H3**.

## 6. Frozen-but-unexecuted potential coverage

**FROZEN POTENTIAL COVERAGE != VALIDATED EVIDENCE.** None of the following
records changes the matrix classifications until separately authorized,
executed against its frozen expected result, and preserved/reviewed.

| Frozen fixture | Predetermined semantics relevant to Item 2.6 | Potential future coverage | Limit |
| --- | --- | --- | --- |
| `FX/ER-F4-C v1` | Available adequate ASU; requester may inspect but Consumer disclosure of Required material is denied; non-sensitive denial/qualification is required. | Authorization-limitation preservation at package/rendering boundary; potentially supporting 2.6-I/K. | It is a Consumer-disclosure denial, not clearly a Source inspection exclusion/inaccessibility; alone it does not meet the exact 2.6-I Source-path obligation. |
| `FX/ER-F5-B v1` | One already bounded authorized traversal reaches Beacon, whose item is Candidate but inapplicable/excluded. | Supporting cross-Project boundary/applicability evidence only. | It is not a scoped negative result and does not state an initial set, deficiency-driven expansion trigger, expansion request, or stopping condition required by 2.6-F. |
| `FX/ER-F5-C v1` | Named authorized Beacon Source is included as Supporting context under a bounded relationship. | Supporting evidence for static bounded cross-Project ASU and limitation/provenance distinction. | It is not bounded discovery expansion; its two Sources are statically governed for the request. |

The now-executed `FX/ER-F6-D v1` directly validates indeterminate ASU through
`VE-F6-D-002`; `FX/ER-F6-EF v1` directly validates scoped negative results and
bounded expansion through `VE-F6-EF-001`; and `FX/ER-F6-J v1` directly
validates unsupported Artifact capability through `VE-F6-J-001`. No remaining
frozen unexecuted fixture is predesigned for inaccessible Source handling.

## 7. Accepted/deferred validation limitation

The sole non-direct obligation is inaccessible limitation evidence (2.6-H).
The Project Owner has accepted it as the active deferred v0.1 validation
limitation `DVL-P4-001`; see the [final disposition](ws2-item-2.6-final-disposition.md)
and [deferred-validation/accepted-limitations register](deferred-validation-accepted-limitations-register.md).
H remains **SUPPORTING EVIDENCE ONLY**. Supporting records do not make it
directly validated. Item 2.6 is complete only for the approved v0.1 executable
validation boundary: 10 directly validated obligations plus this accepted
limitation, not universal direct proof of every semantic condition.

## 8. Minimum future validation-scenario grouping

This is grouping only; it does not design fixtures, expected results, or
execution procedures.

| Minimum scenario | Obligations covered | Existing frozen fixture usable? | Why needed |
| --- | --- | --- | --- |
| Indeterminate evidence boundary | 2.6-D | No. | A controlled ASU must have adequacy genuinely not establishable as adequate or known-incomplete, with qualification preserved. |
| Existing but unreadable in-scope Source | 2.6-H | No. | It must distinguish access failure from absence/unavailability and preserve the limitation at the applicable downstream boundary. |
| Relevant unsupported capability | 2.6-J | No. | It requires a real approved relevant unsupported condition, not an invented technology/type, and preservation of the limitation. |

## 9. TD-14 assessment

**TD-14 TRIGGER NOT MET.**

`VE-F1-001` demonstrates a normal deterministic result in an adequate ASU;
`VE-F2-001` demonstrates Candidate and applicability exclusions, not a
deterministic discovery deficiency; `VE-F4-B-001` and `VE-F4-E-001/E-002`
demonstrate named unavailable Required Sources and appropriately preserve the
resulting insufficiency/qualification; `VE-F5-A-001` demonstrates expected
authorization/governance exclusion before inspection, not an inability to
discover authorized in-scope material; `VE-F6-EF-001` demonstrates the
expected exhaustion of the sole bounded path and a scoped negative result for
its reporting task, not a deterministic-discovery deficiency; `VE-F6-J-001`
demonstrates the approved unsupported-PDF Artifact capability boundary while
preserving an available, accessible, authorized Source and insufficiency. No
execution demonstrates inaccessible Source handling, nor materially or
repeatedly undiscoverable relevant, authorized, in-scope Required Context
through approved deterministic mechanisms that causes incorrect/insufficient
context or material harm.

The coverage gaps mean the required cases have not yet been validated; they do
not themselves show deterministic discovery failure.  No AI/vector/model-based
discovery recommendation follows from this review.

## 10. Disposition and future tracking

The F6-J execution directly validates J. The Project Owner has completed the
final Item 2.6 disposition: **COMPLETE WITH ACCEPTED VALIDATION LIMITATION**.
`DVL-P4-001` remains active until its governed closure criteria are met.
Items 2.7–2.11 are authorized to proceed under existing Phase 4 controls; this
does not approve Gate 4B or proving.

## 11. Non-execution attestation

`FX-F6-J v1` was executed against `ER-F6-J v1`, with `VE-F6-J-001`
preserved as PASS. H was not created or simulated; no other fixture was run or
prepared in this task and no finding, remediation, expected-result change, fixture change,
application/source/test change, Gate 4B action, proving action, or TD-14 action
was made. The later final disposition changes only Item 2.6's documentation
status to **COMPLETE WITH ACCEPTED VALIDATION LIMITATION**; H remains
**SUPPORTING EVIDENCE ONLY** and Items 2.7–2.11 remain incomplete.
