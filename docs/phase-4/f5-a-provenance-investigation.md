# F5-A Provenance Investigation

**Status:** **INVESTIGATION COMPLETE / DISPOSITION REQUIRED**

## 1. Status and non-execution boundary

This is a documentation and Git-history investigation authorized after the
pre-execution provenance check stopped.  `FX-F5-A v1` was **not executed**.
No Validation Evidence Record, result state, finding, remediation, fixture,
expected-result revision, application/source/test change, checklist change, or
proving activity was created by this investigation.

Item 2.6 remains **INCOMPLETE**.  Gate 4B remains **NOT APPROVED**; proving
remains **NOT AUTHORIZED**; TD-14 remains **CLOSED / NOT REOPENED**; and
production readiness remains **NOT ESTABLISHED**.

## 2. Current baseline and discrepancy

The investigation started from clean `HEAD`
`a6db6f8562c7749a7401139503ae8e2960f920c9` — *Review Phase 4 ASU
validation coverage*.  The stopped pre-execution check correctly observed
that the frozen expected-result register describes the WS2 Item 2.1
fixture-design baseline as `c9b39a3`, but the actual F5-A fixture paths and
both fixture/expected-result registers do not exist at that commit.

The ambiguity is a provenance-reference ambiguity, not a demonstrated
semantic difference: `c9b39a3` is the immediately preceding Gate 4A execution
authorization baseline; the physical fixture family and its v1 expected
results were committed at `c7d17714`.

## 3. Git-history timeline

| Commit / time | Historical role and relevant contents |
| --- | --- |
| `48df5148cba14415a41f5abd5cbde43247645a7c` — 2026-09-26 08:49:52 -05:00 | *Complete Phase 4 validation governance package*.  Adds the pre-results expected-result and evidence controls; no WS2 fixtures, fixture records, or F5 records exist. |
| `c9b39a3e950225498e06e687e69fdf15e9f37235` — 2026-09-26 08:58:04 -05:00 | *Approve Gate 4A and authorize Phase 4 execution*.  Changes Gate 4A/checklist/governance documentation only; its parent is `48df514`.  It contains neither `ER-F5-A`, `FX-F5-A`, a fixture register, an expected-result register, nor F5-A design prose. |
| `c7d17714a3983335f8564aa9360739d9ec785410` — 2026-09-26 09:11:40 -05:00 | *Prepare Phase 4 deterministic validation fixtures*.  Introduces all F1–F5 physical inputs, `fixture-records.md`, `expected-results.md`, and the WS2 Item 2.1 fixture-preparation record in one commit.  It is the sole relevant commit between `c9b39a3` and itself. |
| `2b7435b294da68a2e99847d26bf447f9eb71f87c` — 2026-09-26 11:27:26 -05:00 | *Prepare Phase 4 conditional sufficiency fixture*.  Adds F4-E only.  Its diff leaves the F5-A/B/C entries and paths unchanged. |
| `a6db6f8562c7749a7401139503ae8e2960f920c9` | Current review baseline.  No F5-A input or F5-A/ER-F5-A semantic revision appears after `c7d17714`. |

`c7d17714` adds the six F5-A controlled input files, the FX-F5-A entry, and
ER-F5-A together.  The Item 2.1 preparation record at that same commit says
the inputs and expected results were “frozen before execution,” identifies
`c9b39a3` as the exact **committed execution baseline**, and expressly attests
that no fixture was run and no execution result/evidence existed.  Thus
`c9b39a3` is traceable as the pre-preparation authorization baseline, but not
as the commit containing materialized F5 inputs or ER-F5-A.

## 4. ER-F5-A history

`ER-F5-A v1` first appears in `c7d17714`; it has no predecessor.  Its first
content names `FX-F5-A v1`, the Atlas Bootstrap/project files and Atlas/Beacon
Source files; establishes cross-Project authorization denial; requires default
isolation before representation/Candidate use; and defines the acceptance and
negative criteria now present at `HEAD`.

The only later commit touching the expected-result register is `2b7435b`,
which adds ER-F4-E before the ER-F5-A heading and does not alter any ER-F5-A
line.  `git diff c7d17714..a6db6f8` shows no ER-F5-A acceptance, negative, or
other semantic change.  The history has no F5-A execution record before or
after `c7d17714`; the original preparation record's non-execution attestation
and the current F5-A absence from the validation-evidence inventory agree.
Repository history therefore contains no result-informed ER-F5-A alteration.

## 5. FX-F5-A history

Each controlled F5-A input first appears in `c7d17714` and has no later
modification:

| Controlled input | First appearance | Later modification | Classification |
| --- | --- | --- | --- |
| `F5-A/bootstrap.toml` | `c7d17714` | None | semantic controlled input, unchanged |
| `F5-A/project.toml` | `c7d17714` | None | semantic controlled input, unchanged |
| `F5-A/beacon-bootstrap.toml` | `c7d17714` | None | semantic controlled input, unchanged |
| `F5-A/beacon-project.toml` | `c7d17714` | None | semantic controlled input, unchanged |
| `F5-A/sources/atlas-task.md` | `c7d17714` | None | semantic controlled input, unchanged |
| `F5-A/sources/beacon-note.md` | `c7d17714` | None | semantic controlled input, unchanged |
| FX-F5-A entry in `fixture-records.md` | `c7d17714` | None | semantic control, unchanged |

The register was later structurally edited only to add F4-E and update the
family inventory.  That change is documentation for a different fixture and
does not modify the FX-F5-A block.  There is no later semantic, structural
nonsemantic, documentation-only, or unknown change to an F5-A controlled
input itself.

## 6. Semantic comparison: documented design and materialized F5-A

The earliest available F5-A semantic design is the FX-F5-A and ER-F5-A record
pair in `c7d17714`; no F5-A design record exists at `c9b39a3` or earlier.
The following comparison is therefore between that original record pair and
the physical files introduced in the same commit.

| Required semantic element | Original FX/ER record at `c7d17714` | Materialized F5-A control / conclusion |
| --- | --- | --- |
| Projects and Sources | Atlas `fixture-atlas-f5`; external synthetic Beacon `fixture-beacon-f5`; `SRC-F5A-ATLAS` and `SRC-F5A-BEACON`. | The two Bootstrap/project TOML pairs establish those Project identities; the two named Source files are present. Faithful. |
| Relationship and authorization | No governed Atlas–Beacon relationship; cross-Project Requester authorization denied; Beacon Consumer disclosure not established; Atlas authorized. | These are fixture-record semantic inputs in the FX record, not claims inferred from Markdown. They exactly match the ER’s cross-Project-denied premise. Faithful. |
| ASU/traversal and observation | Atlas task scope only; traversal/discovery stops at Atlas; Beacon is outside effective ASU/discovery and is not observed as authorized content. | Atlas and Beacon files are separately registered controlled material; the record confines the effective boundary to Atlas. Faithful. |
| Representation/Candidate/applicability/selection | Atlas is represented, Candidate, applicable, Required, and selected; Beacon is none of these. | ER requires exclusion before representation/Candidate use and the FX record states the same downstream boundary. Faithful. |
| Package and rendering | Adequate Atlas-only ASU; Sufficient Atlas package and authorized renderings with Atlas provenance only. | ER requires no Beacon content, metadata, Provenance, relationship, or authorization implication in package/renderings. Faithful. |
| Negative criteria | No useful-but-unauthorized traversal/retrieval, Project merge, or Beacon leak. | The ER negative criteria exactly correspond to the declared unauthorized boundary. Faithful. |

No repository evidence shows material F5-A semantics being changed during or
after physical materialization.  The files, FX record, and ER were introduced
atomically as a controlled pre-execution fixture package; the file prose alone
is intentionally not the source of governance semantics.

## 7. Expected-result-control determination and classification

**Expected-result-control determination: YES — TRACEABLE.**

The repository establishes that the actual FX-F5-A inputs and ER-F5-A v1 were
created together at `c7d17714`, after Gate 4A authorization and before any
recorded F5-A execution.  The same commit's preparation record derives
expected semantics from the approved Phase 0–3 and WS1 controls, identifies
the relevant controlled artifacts, and records a non-execution attestation.
The unchanged F5-A paths and unchanged ER-F5-A block preserve that lineage.
This is sufficient repository evidence that the recorded material expectation
was pre-results and corresponds to the actual frozen fixture semantics.  It
does not establish an unrecorded activity outside repository history.

**Classification: A — RECORDING / DOCUMENTATION ERROR.**

The imprecise use of `c9b39a3` in the expected-result register's
“fixture-design baseline” wording can be read as identifying the commit that
contains the fixture/ER, although it is instead the authorized baseline from
which the subsequent `c7d17714` preparation commit was made.  The valid
pre-results lineage is `48df514` (governance package) -> `c9b39a3` (Gate 4A
authorization/execution baseline) -> `c7d17714` (atomic materialization of
FX-F5-A and ER-F5-A with non-execution attestation).  No correction is made
by this record.

## 8. Finding assessment

**FINDING NOT YET WARRANTED.**

The discrepancy warranted a safe stop and this investigation, but the
preserved history establishes a pre-results, unchanged fixture/ER pair and no
demonstrated validation-integrity breach, runtime result contamination, or
semantic mismatch.  The ambiguity is a documentation-reference defect needing
governed disposition before future execution, not evidence of a failed
validation run or a presently demonstrated implementation/integration/security
defect.  A finding would require a separately governed determination that the
recording ambiguity itself has sufficient impact under the approved severity
and type model.

## 9. Other-fixture impact

| Fixture | Assessment | Evidence |
| --- | --- | --- |
| F5-B | **AFFECTED** | Its inputs and ER-F5-B first appear in the same `c7d17714` fixture family and ER-F5-B repeats the same `c9b39a3` baseline reference.  Its material semantics are unchanged, but its provenance wording needs the same governed review before execution. |
| F5-C | **AFFECTED** | Same family, first appearance, unchanged history, and shared `c9b39a3` wording as F5-B/F5-A. |
| F4-C | **AFFECTED** | Its inputs and ER-F4-C also first appear in `c7d17714` and share the register-level `c9b39a3` baseline wording.  It has no distinct later semantic revision; the documentation-reference ambiguity applies equally before any execution. |

These assessments do not execute, invalidate, revise, or otherwise dispose of
any fixture.

## 10. Prior Phase 4 evidence impact

The same register-level provenance wording exists for the original F1–F4-D
fixture family.  It does **not** presently invalidate or change the accepted
F1, F2, F3, F4-A, F4-B, or F4-D results: their preserved evidence records
independently identify `c7d17714` as the actual fixture/ER origin, record
their own clean execution baselines, and preserve controlled hashes where
applicable.  The F4-E original/retest uses a separately introduced
`2b7435b` controlled fixture/ER and is not dependent on ER-F5-A or its
controlled inputs.

Accordingly, no already accepted validation result is reclassified by this
investigation.  The shared reference wording is an evidence-governance matter
for Project Owner disposition, not evidence that the prior runs used changed
or result-informed controls.

## 11. Possible governed next-action categories

No next action is selected or authorized.  Possible governed categories are:

- Project Owner disposition of the documentation-reference ambiguity, with a
  bounded decision on whether a clarification/correction record is required;
- a governed cross-family provenance review before any unexecuted original
  F4/F5 fixture is considered for execution; or
- confirmation that the established `c7d17714` pre-results lineage is the
  approved execution provenance, followed only by separately authorized
  fixture execution.

## 12. Non-execution attestation

No F5-A, F5-B, F5-C, F4-C, or other fixture was executed for this
investigation.  No F5-A PASS/FAIL/INDETERMINATE result exists.  No frozen
fixture/ER, validation evidence, application/source code, tests, or checklist
was modified.  No finding, remediation, commit, or push was created.
