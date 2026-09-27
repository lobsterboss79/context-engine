# WS2 Item 2.10 — F3 Register Provenance Investigation

**Status:** **INVESTIGATION COMPLETE / PROJECT OWNER DISPOSITION REQUIRED**

## Scope and boundary

This is the Project Owner-authorized bounded provenance investigation following
the pre-execution stop of `RC-P4-2.10-R1 v1`. It compares only the historical
and current `FX-F3 v1` and `ER-F3 v1` register records. It does not execute
R1 or R2, change a control, alter F3, create validation evidence, create a
Finding, modify application source or tests, change a checklist status, or
make a Gate/proving/TD-14/production-readiness disposition.

## Investigation baseline and stopped preflight

| Field | Value |
| --- | --- |
| Clean investigation baseline | `67bfeb74ef47ca050e12befe74707377e41e9340` — `Prepare Phase 4 repeatability controls`; `git status --short` was empty before this investigation record was created. |
| Historical F3 materialization baseline | `c7d17714a3983335f8564aa9360739d9ec785410` — `Prepare Phase 4 deterministic validation fixtures`, the first materialization commit for the F3 fixture/expected-result records. |
| Stopped activity | The prior R1 preflight stopped before any Context Engine pipeline invocation because the shared-register whole-file hashes in `ER-P4-2.10-R1 v1` did not equal the current whole-file hashes. |
| Execution status | No R1 execution occurred; no R1 validation evidence exists; no R2 activity occurred. Historical `VE-F3-001` remains immutable and was not used as runtime state. |

## Shared-register hash comparison

| Register | SHA-256 at `c7d17714` | SHA-256 at investigation HEAD | Result |
| --- | --- | --- | --- |
| `fixture-records.md` | `ddc68a86d135c4927e519d1c037b2d4cdad8e91c4b89516b8ef7c879ace7c794` | `201dc4d13c927ce424e66c7615365e9e3f494ed998195f10d88f48f892244cec` | Whole shared file changed. |
| `expected-results.md` | `a8aa072209f6d0b2515ababadcd51bb787bec470b82f04e6c8b0d834016a2600` | `b285bfcca4b7afd748b2c6a3f020ea08d6fe2a0b464313cd56a396a4cb231744` | Whole shared file changed. |

The historical values are accurate SHA-256 values for the complete shared
files at `c7d17714`; the current values are accurate values for the complete
shared files at the investigation baseline. They therefore establish
historical provenance, but do not by themselves establish continuing identity
of an individual record in a mutable shared register.

## Exact FX-F3 v1 record comparison

The record was extracted from its `## FX-F3 — Conflict, uncertainty, and
provenance` heading through immediately before the next level-two heading,
including its terminal blank line. The historical and current extracted text
is exactly the following in both versions:

```markdown
## FX-F3 — Conflict, uncertainty, and provenance

| Field | Predetermined record |
| --- | --- |
| Purpose / Project scope | Project Atlas (`fixture-atlas-f3`); task: prepare a current release recommendation while preserving a controlled unresolved current conflict, historical state, and inventory uncertainty. |
| Exact artifacts / configuration | `F3/bootstrap.toml`; `F3/project.toml`; `F3/sources/current-decision.md` (`SRC-F3-CURRENT`); `F3/sources/competing-decision.md` (`SRC-F3-COMPETING`); `F3/sources/historical-note.md` (`SRC-F3-HISTORY`); `F3/sources/qualification.md` (`SRC-F3-QUALIFICATION`). |
| ASU / authorization | Adequate four-Source ASU, scope `field-kit-release`; requester and all Consumers authorized; unlimited capacity. Bootstrap-established fixture governance marks the first two claims Approved/current and overlapping; it marks the canvas-bag claim Approved/historical; it marks depot availability Unverified. No supersession relationship is supplied. |
| Expected observation / representation / Provenance | Direct observation with distinct Source/artifact/observation lineage for `RI-F3-SEALED`, `RI-F3-TOTE`, `RI-F3-CANVAS-HISTORY`, and `RI-F3-DEPOT-UNVERIFIED`. Representation preserves current/historical qualification and transformation state as direct/source-derived. |
| Candidate / applicability / role | All four become Candidates. Sealed and tote claims are applicable current competing decisions; both are Required because omitting either would conceal material incompatible guidance. Canvas history is applicable Supporting historical context; depot report is applicable Supporting uncertainty/availability qualification. |
| Conflict / uncertainty / selection | Preserve `CON-F3-CASE-CHOICE` between sealed/tote; do not choose by recency, order, or implementation preference. Preserve `UNC-F3-DEPOT` as unverified. Select all four contextual items with their distinct Provenance and temporal state. |
| Sufficiency / coherence / package | `Insufficient` because material current Conflict is unresolved (and the unverified depot qualification remains). Expected coherence is `coherent_with_qualification`: intentional temporal coexistence is explicit, not merged. Logical package exists with conflict, uncertainty, Source Manifest, roles, and insufficiency; no hidden conflict resolution. |
| Renderer expectations | Every renderer exposes both competing current claims, historical qualification, uncertainty, Provenance, `Insufficient`, and coherence qualification. It must not label either decision superseded/currently controlling beyond supplied governance. |
| Governing references / result | P0 §§5–10; P1 model Conflict/Uncertainty; P2 D D15–D16; P2 E SEL-02, §§sufficiency; P2 F F16; P3 WS7 §37, WS8 §§7–25, WS9 §§5–11. `ER-F3 v1`. |
| Known limitation | This deliberately supplies governance facts as fixture metadata; source wording alone is not Bootstrap Authority. |
```

| Comparison | Result |
| --- | --- |
| Historical extracted-record SHA-256 | `6bda6616a07021a2d54a10bc07331675337a910e1a9958525aacbba8ed226e6e` |
| Current extracted-record SHA-256 | `6bda6616a07021a2d54a10bc07331675337a910e1a9958525aacbba8ed226e6e` |
| Textual / semantic result | **TEXTUALLY IDENTICAL**; therefore semantically identical. No adjacent-heading, formatting, or F3-record change exists. |

## Exact ER-F3 v1 record comparison

The record was extracted from `## ER-F3 v1` through immediately before the
next level-two heading, including its terminal blank line. The historical and
current extracted text is exactly the following in both versions:

```markdown
## ER-F3 v1

| Template field | Frozen value |
| --- | --- |
| Governing requirement/design reference | P0 §§5–10; P1 Conflict/Uncertainty; P2 D D15–D16; P2 E SEL-02/sufficiency; P2 F F16; P3 WS7–WS9. |
| Validation/checklist relationship | WS2 Item 2.1; future WS2 Items 2.4, 2.5, 2.7, and 2.8. |
| Controlled fixture/input identity | `FX-F3 v1`; `F3/bootstrap.toml`, `F3/project.toml`, and four named F3 source files. |
| Bootstrap/configuration/environment basis | Explicit v1 TOML; `fixture-atlas-f3`; `c9b39a3`; future environment separately recorded. |
| Governed expectation | Preserve two competing current Approved decisions as unresolved Conflict, one historical supporting claim, and unverified availability; select all relevant context with distinct lineage; package is Insufficient and coherent-with-qualification. |
| Acceptance criteria | No newer-wins/order/model resolution; conflict participants/currentness/historical role/uncertainty/provenance remain explicit in logical package and all renderings. |
| Negative/failure criteria | Resolving or omitting material conflict; promoting historical claim to current; presenting unverified availability as established; calling the package Sufficient. |
| Limitations / reviewer / authority / lineage | Fixture metadata supplies scoped governance rather than elevating Markdown; shared reviewer/authority basis; initial frozen version. |
```

| Comparison | Result |
| --- | --- |
| Historical extracted-record SHA-256 | `72e5b2de99cd2b23c00f845dbb2e1f10aae481dc3a0f9afbf38ece248ff5b02f` |
| Current extracted-record SHA-256 | `72e5b2de99cd2b23c00f845dbb2e1f10aae481dc3a0f9afbf38ece248ff5b02f` |
| Textual / semantic result | **TEXTUALLY IDENTICAL**; therefore semantically identical. No adjacent-heading, formatting, or ER-F3-record change exists. |

## Git-history findings

`git log --follow` identifies exactly two commits after the F3 materialization
that changed each shared register:

| Commit | Register effect | Effect on F3 record |
| --- | --- | --- |
| `2b7435b294da68a2e99847d26bf447f9eb71f87c` — `Prepare Phase 4 conditional sufficiency fixture` | Added the unrelated `FX-F4-E v1` and `ER-F4-E v1` records; updated the shared fixture-inventory count/wording. | None. F3 sections are outside every changed hunk. |
| `362ea3ceb7164e9fbddee0606c63be1bb9c78deb` — `Clarify Phase 4 fixture provenance` | Revised only common-register provenance/preamble text, distinguishing the pre-preparation authorization baseline from the original F1–F5 materialization baseline. | None. F3 sections are outside every changed hunk. |

`git blame` for every current F3-record line attributes all FX-F3 lines and all
ER-F3 lines to `c7d17714`. The `c7d17714..HEAD` file diff contains no F3
heading or F3-record content hunk. No later broad formatting/reorganization
commit changed either shared register. No F3 semantic field changed.

## Controlled F3 input-file verification

All six actual F3 controlled fixture files match their frozen Item 2.10
SHA-256 values:

| File | SHA-256 | Result |
| --- | --- | --- |
| `F3/bootstrap.toml` | `1c27f2dd2eb882adadcd2a5ea3f7cc9ec6a223348d49662e51d710a52a180a46` | Match |
| `F3/project.toml` | `6d6982c01382108a970b60830f0d65fa4edf35cc32bee758f16005f613b668be` | Match |
| `F3/sources/competing-decision.md` | `afcb9ebb82eca7b9842078f8f8891c9d2fd912b7e28bebcd9745d31d9717b7c0` | Match |
| `F3/sources/current-decision.md` | `c22ea350f759e63c0315a2d6c4a370498449e7a2f30e16cf33c2e8b7b8f1a776` | Match |
| `F3/sources/historical-note.md` | `e4c12c53455c16b11d2a723104d65310f142450ec82d20f6005107b90ac73008` | Match |
| `F3/sources/qualification.md` | `fc90e05050be6c023c8214b7acdb28dddc56033d5c7171f5eb68895d9b0af9d2` | Match |

## Root cause and classification

**Root cause:** `ER-P4-2.10-R1 v1` represented the identity of `FX-F3 v1` and
`ER-F3 v1` by freezing SHA-256 values for their entire shared-register files.
Those shared files later received governed additions and provenance-preamble
clarifications unrelated to F3. The resulting whole-file mismatch is real,
but it is not a changed F3 semantic record or a changed controlled F3 input.

**Classification: A — CONTROL PROVENANCE / RECORDING ERROR.** FX-F3 v1 and
ER-F3 v1 are textually identical at the record level, so no material F3
provenance change occurred.

**Finding assessment:** A Finding is not warranted at this stage. The stop
rule worked as designed, the discrepancy is fully explained by shared-register
aggregation, and no execution result or governed semantic discrepancy exists.
This assessment does not itself change any control or disposition.

## Least-invasive correction options for Project Owner decision

The least-invasive governed correction is to retain the two historical
whole-file SHA-256 values and `c7d17714` as provenance evidence, while adding
an explicit record-level integrity basis for the current F3 records: the exact
historical snapshot/range definition and the corresponding extracted-record
SHA-256 values above. A future preflight could verify both (a) the historical
whole-file provenance at `c7d17714` using Git and (b) equality of the current
extracted F3 records to those frozen record hashes.

Other bounded options for Project Owner consideration are:

1. Preserve exact F3 record snapshots in the repeatability control and compare
   the current extracted records byte-for-byte to them.
2. Preserve `c7d17714` Git blob/object provenance plus a stable heading/range
   extraction rule and the extracted-record hashes.
3. Define a repository-conventional canonical record serialization/hash only
   if approved as a general governance mechanism; this is less invasive to
   runtime behavior but broader than the snapshot/range approach.

No option should replace the historical whole-file hashes with current
whole-file hashes, because that would lose the provenance fact that the
historical F3 materialization existed within those exact files at `c7d17714`.

## Semantic independence and required decision

Any of the bounded provenance-only corrections above would leave unchanged:

- FX-F3 semantics and ER-F3 semantics;
- R1 and R2 semantic expectations, R1 run count, and the R2 matrix;
- `SC-P4-2.10 v1`; and
- application behavior.

The Project Owner must decide whether to authorize a specific provenance-only
control correction and its approval/materialization process. Until then,
R1 remains unexecuted and R2 remains unauthorized.
