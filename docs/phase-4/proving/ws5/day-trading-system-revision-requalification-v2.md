# Day Trading System Revision Requalification v2

**Status:** **REQUALIFICATION COMPLETE — PROJECT OWNER EFFECTIVE-REVISION DECISION REQUIRED**

**Scope:** Read-only requalification of Day Trading System revision
`e29de5c7d26a31f66cf47c30b295591e6b192887` only. This record neither adopts
that revision nor authorizes a successor, Consumer, package/rendering,
WS6A/WS6B, Gate 4C, or production readiness.

## Candidate and diff boundary

| Property | Result |
| --- | --- |
| Previous candidate | `c1f7abf41e1743bc14a95cba244339c8a07a334f` |
| New candidate | `e29de5c7d26a31f66cf47c30b295591e6b192887` (`docs: supersede corrected reproducibility semantic provenance records`) |
| Observed branch / worktree | `main` / clean |
| Lineage | PASS: `c1f7abf…` is an ancestor of `e29de5c…` |
| Changed paths | Exactly the semantic-record README, four v2 semantic-record JSON files, and four append-only lifecycle-relation JSON files |

The diff contains no application source, tests, data, provider configuration or
access material, or change to any of the eight authorized Markdown Sources.
The JSON artifacts remain governed semantic inputs, not additional registered
raw Sources or an expanded ASU.

## Eight-Source integrity

All eight Sources are byte-identical to the `P4-I10-SELECT-001` basis and
retain its SHA-256 values: `AGENTS.md` `6a66…e01f`; project overview
`7822…f8ec`; roadmap `c70a…34c8`; Phase 1 boundary `bd62…090b`; Phase 2 exit
`51a2…8f33`; PDR-016 `2bb0…fb50`; research governance `13f9…4c2a`; and
reproducibility standard `c868…94d8`. Their authority, currentness, and
provenance roles are unchanged. No Source basis was expanded.

## Production semantic corpus and lifecycle result

The isolated production exercise used `load_semantic_record`,
`ingest_semantic_record`, `validate_semantic_record_successor`, and the
production SQLite lifecycle resolver against the candidate repository, with
only a temporary database under `/tmp`.

| Measure | Result |
| --- | ---: |
| Historical maintained record instances | 38 |
| Valid direct ingestions | 34 |
| Historical v1 line-binding rejections | 4 |
| Valid lifecycle relations | 4 |
| Deterministically active records | 34 |

The four preserved v1 records still fail direct ingestion solely with
`semantic record line binding mismatch`: they bind reproducibility-standard
block 3 to lines 5–7. They are retained unchanged as immutable historical
evidence, not reinterpreted as active inputs. Each v2 successor validates
against `docs/research/reproducibility-standard.md`, block ordinal 3, lines
7–7.

For every corrected pair, Claim identity, assertion reference, assertion,
Project/Source identity, source revision/hash, observation, classifications,
limitations, and authority/currentness/governance bases are unchanged. Only
the provenance/evidence location and associated explanatory evidence change.
Each relation has kind `provenance_correction`, names the actual UTF-8 JSON
SHA-256 values, and validates its deterministic relation SHA-256.

The resolver preserves all 38 instances and selects exactly the v2 Code,
Configuration, Data, and Experiment Definition records as terminal active
records. The other 30 Claims remain active v1 records. It found no competing
successor, cycle, missing endpoint, cross-Project relation, Claim mismatch,
ambiguous terminal, duplicate active Claim, or nondeterminism.

## Provenance and fail-closed validation

Every active record was checked for the declared Project, registered Source,
historical selected Source revision/hash, observation identity, exact relative
Source path, Markdown block/line range, semantic-record byte hash, and
authority/currentness/governance basis plus limitations. The record contract
continues to handle Source and JSON content as inert evidence/data; neither
semantic records nor relations grant authority or issue instructions.

Isolated production negative controls passed: altered Source hash, invalid line
binding, altered lifecycle relation hash, Claim-changing provenance correction,
competing successor, cross-Project relation, cycle, and ambiguous-active-
terminal cases fail closed. Focused semantic-ingestion/lifecycle tests also
passed: **15 passed**. No candidate-repository file was changed.

## Independence and eligibility

The corpus remains a maintained, source-grounded Day Trading System artifact.
The JSON corpus contains no WS6A, P1–P8, expected-answer, evaluator, rubric,
Consumer, synthetic-answer, or proving-fixture content. The README's use of
“proving” is an exclusion statement, not proving material. No comparison to
the frozen expected-state matrix was made.

| Checklist criterion | Requalification result |
| ---: | --- |
| 1. Real, independent, non-synthetic Project | PASS — prior Owner attestation and maintained Project history remain applicable. |
| 2. Identity, Bootstrap/configuration, authority, disclosure | PASS for candidate revision; later semantic-input disclosure/allowlisting remains an exact-run control. |
| 3. Bounded observable Git/Markdown Source/ASU | PASS — the same eight-Source boundary and exclusions remain intact. |
| 4. Governed continuation task / legitimate next work | PASS — Phase 3 boundary is unchanged. |
| 5. P1–P8 evidence feasibility | PASS — the complete effective 34-Claim input corpus is production-valid; later task-specific evaluation remains unexecuted. |
| 6. Fair-control feasibility | PASS in principle only — the existing control design is preserved; no Consumer/control action occurred. |
| 7. Separate fresh-Consumer feasibility | PASS in principle only — no usable Consumer is presently created or reserved. |
| 8. Exact-run freezing feasibility | PASS in principle only — inputs can now be validly frozen, but the separately preserved semantic package/rendering preparation prerequisite remains before any run. |

This resolves the prior requalification limitation: the prior candidate's four
active corpus records were not production-valid. At this revision, their v1
forms remain historical while their valid v2 provenance corrections are the
only active forms. The prior failure record is preserved without alteration.

## Classification, lineage, and remaining boundary

**Candidate classification:** **QUALIFIES AS THE EFFECTIVE-REVISION CANDIDATE
FOR THE I10/WS6A EXTERNAL-PROJECT PROVING BASELINE, SUBJECT TO PROJECT OWNER
ADOPTION.** This is a requalification result, not adoption or execution.

`P4-I10-SELECT-001` remains the immutable historical original Project and
revision selection. If the Owner elects to use this candidate, the required
action is an **additive, Owner-approved effective-revision
selection/supersession record** that names `e29de5c7…`, preserves
`P4-I10-SELECT-001`, retains the eight-Source basis, identifies the active
34-record semantic corpus and its four historical v1 predecessors, and freezes
only the later-authorized semantic-input registration/disclosure boundary.

After that distinct adoption decision, prerequisites for a separately
authorized `WS5.5-S-WS6A-003` are substantially present as to the maintained
semantic corpus, but it is **NOT READY TO AUTHORIZE OR EXECUTE**. Remaining
prerequisites are the Owner’s effective-revision adoption; a separately
authorized successor protocol; explicit semantic-record registration/
allowlisting and Consumer-disclosure boundary; a faithful semantic package/
rendering construction resolution and exact hashes; new separate fresh
package/control Consumer handling; and the later, separate WS6A authorization.

## Preserved states and next Owner decision

| Item | State |
| --- | --- |
| `CE-P4-WS5-CONSUMER-001` | **INVALID / DISCARDED / NEVER USABLE** |
| `CE-P4-WS5-CONSUMER-002` | **NOT CREATED** |
| Control Consumer | **NONE** |
| `H3-P4-SEMANTIC-INGESTION-001` | **CLOSED — PROJECT OWNER APPROVED** |
| `DVL-P4-001` | **ACTIVE / ACCEPTED / DEFERRED** |
| TD-14 | **TRIGGER NOT MET / CLOSED / NOT REOPENED** |
| Gate 4B | **PASS — PROJECT OWNER APPROVED** |
| WS5 / WS6A / WS6B | **NOT COMPLETE / NOT AUTHORIZED / NOT AUTHORIZED** |
| Gate 4C / production readiness | **NOT APPROVED / NOT ESTABLISHED** |

**Exact next Project Owner decision:** approve or decline an additive
effective-revision selection/supersession record adopting
`e29de5c7d26a31f66cf47c30b295591e6b192887` as the effective Day Trading
System I10/WS6A proving baseline. That decision must not itself authorize
successor 003, any Consumer, package construction, rendering, WS6A/WS6B,
Gate 4C, or production readiness.

## Local verification

`git diff --check` passes. No commit or push was performed.
