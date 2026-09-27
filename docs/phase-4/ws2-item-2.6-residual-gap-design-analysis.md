# WS2 Item 2.6 — Residual Direct-Gap Design Analysis

**Status:** **DESIGN ANALYSIS COMPLETE / PRE-RESULTS CONTROLS NOT YET AUTHORIZED**

## 1. Current state

This analysis began from clean committed `HEAD`
`3f5887224c11abde1e1166b3c31be03e6e35cb75` — **Validate Phase 4
authorization boundary**. `VE-F5-A-001` is committed at that baseline and
directly validates Item 2.6-I. The checklist still marks Item 2.6 incomplete;
its residual direct-validation gaps are **D, E, F, H, and J**. Gate 4B is
**NOT APPROVED**, proving remains **NOT AUTHORIZED**, TD-14 remains **CLOSED /
NOT REOPENED**, and production readiness is not established.

## 2. Analysis boundary

This is design analysis only. It creates no fixture, Source file, TOML,
expected-result record, hash, Validation Evidence Record, or execution result.
It changes no checklist state, application/source code, or test. The v0.1
inspection below is limited to whether approved semantics can be represented by
existing interfaces; it is not a source of expected semantics and no runtime
experimentation was performed.

The determinations use three independent questions:

| Term | Meaning |
| --- | --- |
| **Semantically valid** | Approved Phase 0–3 records define the condition sufficiently to validate it. |
| **Expressible in v0.1** | Existing approved interfaces can exercise it without a source change. |
| **Safe to freeze** | A controlled fixture and expected result can be predetermined without observing a runtime result. |

## 3. Governing semantic basis

The analysis uses the Phase 1 conceptual model’s ASU/evidence-boundary,
negative-result, access, and coherence rules; Phase 2 C5, SA-01–SA-05,
OBS-04, E11–E14, RC-05/RC-12, and TD-14; and Phase 3 WS4, WS5, WS6, WS8, and
WS9 boundaries. In particular:

- An ASU is task-relative and distinct from registered and observed sets. It
  can be `adequate`, `known_incomplete`, or `indeterminate`; registration or
  successful inspection alone does not establish adequacy.
- A known/credible material gap is not the same thing as adequacy that cannot
  reliably be established. An unsupported hypothetical possibility alone does
  not defeat otherwise defensible adequacy.
- A negative result means only what was not found within its governed inspected
  boundary. Discovery, Candidate status, applicability, selection, and
  sufficiency remain separate.
- Expansion is one explicit, authorized relationship hop for a supplied
  material, potentially resolvable deficiency; it is not crawling or a static
  multi-Source ASU.
- Unavailable, inaccessible, unauthorized, unsupported, partial, and absent
  are distinct limitations. A limitation does not become absence.
- Unqualified Sufficient requires adequate ASU. Indeterminate or
  known-incomplete ASU permits Conditional Sufficiency only for an explicitly
  safe bounded task with preserved qualification; otherwise it is Insufficient.

## 4. Scenario 1 — Indeterminate ASU (2.6-D)

### Governed condition

The controlled Project/request should establish a known local Project, a known
task, and a known inspected local Source/scope containing the bounded task
record. Its explicit ASU establishment basis should also state the actual
unresolved fact: the available governed boundary/inventory evidence does not
reliably establish whether a further Source *or Source scope* is applicable to
the task. It must identify no particular omitted material Source, scope, or
relationship. The unknown is adequacy of the governing evidence boundary, not
an invented object called an “unknown Source.”

Thus the system cannot call the ASU adequate because its establishment basis is
not defensible for the defined unbounded task. It cannot call it
known-incomplete because no known/credible materially applicable omitted Source
or scope has been established. The remaining basis is the explicit known local
boundary plus the documented inability to establish its completeness/applicability
adequacy. The known local Source identity/scope is preserved; further identities
and scopes are deliberately not asserted.

Choose an unbounded continuation/decision task, not a separately authorized
safe bounded subtask. Its expected outcome is **Insufficient** because the
indeterminate boundary could materially affect correctness. This is not a rule
that indeterminate always means Insufficient: the approved design permits
Conditionally Sufficient only when a distinct safe bounded task is explicitly
established. Construction can remain `coherent_with_qualification` if the
explicit indeterminate boundary is consistently retained; it is not inherently
incoherent. A logical package is expected, marked Insufficient and qualified,
not an empty success. Renderings must name the indeterminate ASU/evidence
boundary and the resulting limitation, and must not say that no other Source
exists, that all relevant Sources were inspected, or that the package is
unqualified Sufficient.

### Existing-interface assessment

`ApplicableSourceUniverse` requires the request reference, a nonempty basis,
and `BoundaryAdequacy.INDETERMINATE`; `evaluate_sufficiency` deterministically
returns Insufficient for an indeterminate non-bounded task. Existing package
and rendering inputs preserve limitations and qualified coherence. This is an
approved input-state exercise, not an inference from a runtime result.

| Determination | Result | Basis |
| --- | --- | --- |
| Semantically valid | **YES** | Phase 1 ASU; Phase 2 C5/E12; Phase 3 WS4/WS8 explicitly distinguish indeterminate. |
| Expressible in v0.1 | **YES** | Existing ASU adequacy/basis and sufficiency/package/rendering interfaces represent it. |
| Safe to freeze | **YES** | The nonempty establishment basis, known facts, omitted facts, task boundary, and qualifications can all be frozen in advance. |

Acceptance themes are explicit nonempty basis; `indeterminate`, not
`known_incomplete`; no fabricated omitted Source; Insufficient unbounded task;
preserved ASU limitation through logical package and all renderings. Failure
themes are relabeling it known-incomplete, asserting universal absence, or
presenting unqualified Sufficient.

## 5. Scenario 2 — Deficiency-driven bounded expansion with scoped negative result (2.6-E/F)

### Governed condition

Use one Project and one adequate ASU containing two governed local Sources:
`SRC-EF-ORIGIN` and `SRC-EF-EXPANSION`. The second is in the ASU but its
represented evidence is marked expansion-only, so it is not initially
inspected. The initial Source contains a represented, governed relationship to
the second and no item matching an explicit controlled query identifier.

The controlled upstream record identifies a material, potentially resolvable
deficiency: the initial inspection has no evidence for that exact task-relevant
identifier, and the represented relationship identifies the only approved
additional in-scope evidence area that could resolve it. It supplies a
nonempty basis, authorization, the origin identity, relationship identity, and
target Source identity. One `ExpansionRequest` then permits the one-hop
inspection of `SRC-EF-EXPANSION`. That Source likewise contains no match.

The ASU is not enlarged during this process: it was already the governed
two-Source universe. The observed/inspected set changes from the initial
origin Source to origin plus the expanded target. Termination is bounded after
the sole authorized relationship hop and completed inspection of the specified
target; it does not imply that no information exists outside the ASU. The
negative result must preserve the initial and expanded inspected identities,
ASU adequacy/basis, expansion basis, deterministic termination statement, and
the exact wording “not found within the governed inspected ASU.”

There are no Candidates for the exact identifier, so there is no
Candidate/applicability exclusion to use as evidence. The task should be
explicitly limited to reporting this governed inspection result, rather than
requiring the absent information for a material decision. With the adequate
ASU, no Required deficiency, and that bounded reporting task, **Sufficient**
is the proposed outcome for reporting the scoped result only. Construction is
`coherent`; a logical package and renderings must carry the boundary and must
not transform the scoped negative result into a claim of universal absence or
a conclusion outside the task.

### Existing-interface assessment

WS6 already exposes `ExpansionRequest`, `DiscoveryEvidence.expansion_only`,
and `DiscoveryResult.initial_inspected_sources`,
`expanded_inspected_sources`, `expansion_basis`, `negative_result_scope`, and
`termination_basis`. The expansion is accepted only for a supplied material,
authorized, nonempty-basis request targeting an in-effective-scope Source with
a represented relationship. WS8 also has a deterministic bounded-iteration
plan input. The new controlled preparation must preserve the upstream
deficiency/iteration-plan-to-expansion-request lineage; manually passing two
ordinary searchable Sources would not exercise this path.

| Determination | Result | Basis |
| --- | --- | --- |
| Semantically valid | **YES** | Phase 2 E13 and Phase 3 WS6/WS8 define deficiency-driven, bounded expansion and scoped negative results. |
| Expressible in v0.1 | **YES** | Existing expansion request, expansion-only evidence, result fields, and bounded-iteration interfaces implement the mechanism. |
| Safe to freeze | **YES** | The initial set, deficiency, relationship, authorization, one-hop target, absent identifier, stop condition, and qualified result are fixed inputs. |

Evidence must show different initial and expanded sets, a nonempty expansion
basis, the represented relationship, authorized target, absent identifier in
both inspected Sources, and a post-expansion scoped negative result. Failure
themes are static two-Source inspection, automatic traversal, expansion without
a material/authorized basis, Candidate/applicability exclusion substituted for
no-result evidence, or universal-absence wording.

## 6. Scenario 3 — Existing but unreadable in-scope Source (2.6-H)

### Governed condition

The semantic scenario is clear: a registered Source/scope exists, is in the
task ASU, is relevant/potentially applicable, and is authorized and available;
the approved observation mechanism cannot read/observe it. Its observation is
therefore inaccessible, produces no represented information from that Source,
and preserves an inaccessible limitation. If the unreadable content is
Required for the task, the expected sufficiency is Insufficient; the proposed
clean case uses Required material so the limitation cannot be waived.
Construction may be `coherent_with_qualification` if every downstream record
faithfully retains the limitation. A logical insufficient package and
qualified renderings are expected; renderings may describe the access
limitation only to the extent authorization allows and must not call the Source
absent, unavailable, unauthorized, unsupported, or inspected.

### Existing-interface assessment

The lifecycle/discovery/sufficiency layers can accept
`Availability.INACCESSIBLE` and preserve the word in a limitation. That is not
a genuine access observation. The only implemented observation paths do not
provide a distinct inaccessible outcome: the Git adapter converts an invalid
or unreadable repository path to an unavailable/invalid failure; Markdown
artifact reading catches `OSError` as `artifact-unavailable`; and the result is
not wired to a distinct lifecycle accessibility state. A filesystem permission
denial is consequently not a safe mechanism: it is environment/identity
dependent (and may not deny a privileged process) and, if it occurs, existing
v0.1 behavior does not classify it as inaccessible.

No current controlled input may honestly turn a real read failure into a
direct inaccessible-observation validation merely by predeclaring an enum.
Doing so would validate manually asserted state, not the required distinction.

| Determination | Result | Basis |
| --- | --- | --- |
| Semantically valid | **YES** | Phase 1, Phase 2 SA-05/C12/E14, and Phase 3 WS4/WS6/WS8 explicitly preserve inaccessible separately. |
| Expressible in v0.1 | **NO** | No current approved adapter-level, deterministic read-failure path maps to the inaccessible lifecycle state. |
| Safe to freeze | **NO** | A fixture cannot predetermine genuine inaccessible observation behavior without either environment-dependent failure or a source change. |

This is not an H3 semantic ambiguity. It is an expressibility limitation that
requires Project Owner direction before any implementation/remediation or a
governance disposition; no permission mechanism or fake enum-only fixture is
proposed here.

## 7. Scenario 4 — Unsupported capability (2.6-J)

### J determination: J1 — REAL V0.1 UNSUPPORTED CONDITION EXISTS

There is a real, approved, relevant v0.1 capability boundary: a governed
local-Git Source may expose an in-scope Artifact, but v0.1 supports only
relative UTF-8 `.md`/`.markdown` Artifact observation/transformation. The
approved v0.1 baseline expressly lists PDF/Office ingestion as unsupported,
and WS5 expressly rejects an unsupported Artifact type. The existing Markdown
observation interface returns the distinct `unsupported-artifact-type` outcome
for such a type. This is not a proposed new adapter, protocol, service, Source
type, or technology.

The controlled future case can therefore use an otherwise available,
authorized, in-scope governed local Git Source whose only relevant Required
Artifact is a PDF/Office-format decision record. The Git Source itself is
observable; the relevant artifact-format capability is unsupported, so it
cannot yield represented information. The ASU retains the Source/scope and the
unsupported capability limitation. The task requires that decision; therefore
the expected outcome is Insufficient, not an invented interpretation or a
substitute. Coherence can be `coherent_with_qualification` when the unsupported
artifact limitation is preserved consistently. An insufficient logical package
is expected. Renderers must state that required governed information could not
be observed through the supported v0.1 capability, without claiming that the
information is absent, unreadable, unauthorized, or available through a
different adapter.

The frozen control must make the source-versus-artifact distinction explicit:
the Source is available and authorized, while the required in-scope Artifact
format/capability is unsupported. It must preserve the limitation as an ASU/
Required deficiency; it must not relabel the whole Source unavailable.

| Determination | Result | Basis |
| --- | --- | --- |
| Semantically valid | **YES** | Phase 1 adapter/capability boundary and v0.1 baseline; Phase 2 SA-01/SA-05, C12, E13 T-05; Phase 3 WS5/WS8. |
| Expressible in v0.1 | **YES** | Existing artifact observation has an unsupported-type outcome, and existing lifecycle/sufficiency/package inputs preserve an unsupported limitation. |
| Safe to freeze | **YES** | The approved restricted format, required-artifact role, absence of an alternative supported path, limitation, and insufficient outcome are all pre-results facts. |

Acceptance themes are successful source registration/scope/authorization;
actual unsupported format outcome; no represented information fabricated from
that Artifact; Required deficiency and unsupported limitation retained; and
qualified logical/rendered package. Failure themes are inventing a connector,
calling a format failure inaccessible/unavailable, changing the capability
boundary, treating binary content as Markdown, or claiming the Source/Artifact
does not exist.

## 8. Cross-scenario distinction matrix

| Distinction | Separation | Observable proof needed |
| --- | --- | --- |
| Indeterminate vs known-incomplete | Indeterminate lacks a known/credible material omitted Source/scope but has inadequate establishment evidence; known-incomplete has a known/credible gap. | ASU basis, named gap only for known-incomplete, and adequacy state. |
| Scoped negative vs inapplicable/excluded | A scoped negative follows inspection and no match; exclusion means a represented item/source was not eligible or applicable. | Inspected identities/query and zero matching Candidates versus exclusion/applicability reason. |
| Bounded expansion vs static bounded scope | Expansion changes inspected sources through a supplied deficiency/basis/relationship; static scope starts with all sources searchable. | Different initial/expanded sets, expansion request/basis, relationship, and one-hop stop. |
| Inaccessible vs unavailable | Inaccessible exists/is available but cannot be observed; unavailable cannot be made available for inspection. | Registration/scope/authorization/availability plus a distinct access-failure observation. |
| Inaccessible vs unauthorized | Inaccessible has authorization; unauthorized is stopped by governance before permitted observation. | Authorization decision and access attempt/result versus authorization exclusion. |
| Unsupported vs inaccessible | Unsupported is a capability/format boundary; inaccessible is a supported path that cannot be read. | Supported-capability declaration/unsupported-type outcome versus distinct read/access-failure outcome. |
| Unsupported vs unavailable | Unsupported capability exists but no supported method can process it; unavailable is an unavailable Source/state. | Available registered Source and unsupported artifact type versus unavailable status/path. |

## 9. v0.1 expressibility matrix

| Family | Existing interface evidence | Semantic validity | Expressible | Freeze readiness | Limiting condition |
| --- | --- | --- | --- | --- | --- |
| D — indeterminate ASU | `BoundaryAdequacy.INDETERMINATE`, ASU basis, sufficiency/package/rendering inputs | YES | YES | YES | Basis must be true boundary uncertainty, not a named gap. |
| E+F — negative plus expansion | `ExpansionRequest`, `expansion_only`, inspection/result fields, bounded iteration plan | YES | YES | YES | Must preserve plan-to-request lineage and actual initial-to-expanded inspection. |
| H — inaccessible Source | Lifecycle enum only; no distinct adapter outcome mapping | YES | NO | NO | Current adapters conflate real read failures with unavailable/failure. |
| J — unsupported capability | Unsupported artifact-type observation and limitation-preservation inputs | YES | YES | YES | Use approved non-Markdown artifact boundary, not a new source technology. |

## 10. Expected-result design-readiness matrix

| Family | Proposed synthetic Project/task and Source shape | ASU / auth / access-support state | Discovery and Candidate/applicability | Sufficiency / coherence / package / rendering | Criteria themes | H3 concern | Ready |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D | One local Project; unbounded continuation task; one known local Source with task evidence; no asserted omitted Source. | Indeterminate ASU; local authorization; known Source available/accessible/supported; completeness of ASU basis unestablished. | Normal scoped discovery only; no invented external Candidate. | Insufficient; coherent_with_qualification; insufficient package; boundary stated, no universal-absence or unqualified-success claim. | Basis and unknown facts explicit; D differs from known-incomplete; limitation survives rendering. | None identified. | **YES** |
| E+F | One local Project; task reports exact-identifier result; origin Source plus one expansion-only target Source. | Adequate two-Source ASU; local authorized available supported Sources. | Initial origin inspection; material resolvable deficiency; authorized represented one-hop relationship; target expansion; no match/Candidate; bounded stop. | Sufficient only to report scoped result; coherent; package/rendering say not found within inspected ASU, never does-not-exist. | Initial/expanded records, basis, relationship, negative scope, termination, anti-static proof. | None identified. | **YES** |
| H | One local Project; task depends on a known required unreadable Source. | Adequate/known-incomplete as separately justified; registered/in-scope/authorized/available but inaccessible; supported capability. | No represented information from access failure; no Candidate from it. | Insufficient; qualified coherence/package/rendering; must state inaccessible only. | Actual access evidence distinct from all neighboring states. | No semantic H3; infeasible in current v0.1. | **NO** |
| J | One local Project; task requires content of an in-scope PDF/Office Artifact in an otherwise governed local Git Source. | ASU preserves available/authorized Source and unsupported relevant artifact capability. | Source observation succeeds; artifact produces unsupported-type outcome; no fabricated representation/Candidate. | Insufficient; coherent_with_qualification; insufficient package/rendering state unsupported capability, no substitute/absence claim. | Actual approved capability boundary and absence of alternate supported path. | None identified; artifact-versus-Source wording must remain precise. | **YES** |

## 11. Minimum fixture-count recommendation

Three new controls are presently ready to prepare: one each for **D**, combined
**E+F**, and **J**. They cannot coherently be merged: D tests boundary
establishment uncertainty; E+F tests a positive expansion transition and
scoped no-result; J tests a real capability boundary. Combining them would
make the observed limitation ambiguous and weaken direct evidence.

No honest H fixture can presently be recommended. Accordingly, **three is the
minimum preparable count**, but there is no current fixture count that closes
all residual direct gaps. If the Project Owner later authorizes a bounded
adapter/access-state correction or another governed disposition for H, H would
need its own fourth fixture because access failure must remain distinguishable
from unsupported capability and ASU uncertainty.

## 12. TD-14 assessment

None of these scenarios, if it behaves as designed, is itself a TD-14 reopening
candidate. D is expected ASU qualification; E+F deliberately reaches a
governed bounded negative result; H is a controlled access limitation; and J
is a known unsupported capability boundary. They do not by themselves show
relevant, authorized, in-scope Required/success-critical information that is
materially or repeatedly undiscoverable through approved deterministic
mechanisms with incorrect/insufficient context or material continuation harm.
TD-14 remains **CLOSED / NOT REOPENED**.

## 13. Project Owner decisions required

Before Codex could prepare/freeze controls, the Project Owner must decide:

1. Whether to authorize fixture/expected-result preparation for ready D,
   combined E+F, and J scenarios.
2. Whether the proposed three-control grouping and the specific separation of
   D, E+F, and J are approved.
3. How to disposition H’s current v0.1 expressibility gap: authorize a bounded
   design/remediation decision, defer it, or otherwise govern Item 2.6-H. No
   H fixture is proposed pending that decision.
4. Whether the approved non-Markdown artifact capability boundary is accepted
   as the J1 direct-validation scenario and whether its artifact-versus-Source
   limitation wording is approved for future pre-results controls.

No decision in this analysis constitutes any of those approvals.

## 14. Recommended sequencing

If authorized, freeze D first, then E+F with its explicit upstream deficiency
and expansion lineage, then J. Do not prepare H until its v0.1 expressibility
disposition is recorded. For every approved control, freeze the fixture and
expected result before any execution and preserve the existing Phase 4
governance/provenance procedure.

## 15. Non-execution attestation

This record is documentation-only analysis. No fixture, expected-result record,
controlled Source file, TOML, hash, Validation Evidence Record, or execution
was created. No existing fixture/ER/checklist was changed. No application,
source, or test file was changed. No fixture was executed. Item 2.6 remains
**INCOMPLETE**; Gate 4B remains **NOT APPROVED**; proving remains **NOT
AUTHORIZED**; TD-14 remains **CLOSED / NOT REOPENED**; and no production
readiness claim is made.
