# VE-P4-4A-003 Semantic-Failure Investigation

**Status:** **INVESTIGATION COMPLETE — PROJECT OWNER SEMANTIC FAILURE DISPOSITION REQUIRED**

## Baseline and immutable lineage

This bounded read-only investigation began on committed baseline `8a2894e`
(`Preserve Phase 4 input diagnostics semantic failure`). It preserves the full
immutable lineage: `VE-P4-4A-001` INDETERMINATE (runner identity construction),
approved investigation; `VE-P4-4A-002` INDETERMINATE (PowerShell preflight),
approved investigation; and `VE-P4-4A-003` FAIL after portable-preflight PASS
and one semantic execution. None is reclassified by this record.

## Exact frozen failure and observed representation

Frozen `ER-P4-4A-002 v1` required partial evidence to have a candidate and a
`partial` entry in `DiscoveryResult.limitations`. In the partial fixture,
`Availability.PARTIAL` had represented matching evidence. Execution produced
one `CandidateContext`, with the source state and qualification preserved in
`candidate.limitations` as `Unknown: Source source-partial: partial`. The
top-level `DiscoveryResult.limitations` contained only the ASU adequacy
qualification (`known_incomplete`). Frozen runner assertion `partial_preserved`
therefore returned false and `VE-P4-4A-003` remains permanently **FAIL**.

## Authoritative semantic trace

The controlling requirement is semantic preservation, not an object-field
location. Phase 1 `CE-NFR-029` requires that an incomplete-source-availability
limitation be identifiable in a constructed package when material; `CE-NFR-030`
requires source-failure isolation while completeness limitations remain visible.
Phase 2 Domain G ST-06 and source/observation state require partial/failure
state and evidence-boundary information to be representable, and CI-02/FR-03
prohibit partial work or Unknown evidence appearing complete or strengthened.
Neither record prescribes `DiscoveryResult.limitations` as the carrier.

Phase 3 WS6 is more specific to discovery: every Candidate retains represented
information/Provenance, Conflict, Uncertainty, and discovery limitations;
partial evidence may participate **only with its preserved qualification**.
The same record separately says the discovery result records ASU adequacy/basis,
scoped negative-result boundary, exclusions, limitations, and termination.
Phase 3 WS8 requires source availability (including partial evidence) to remain
a limitation rather than absence and requires packages to preserve material
limitations; it likewise does not require a DiscoveryResult field location.

Accordingly, governed records require **qualification to survive correctly**.
They allow the partial qualification on the represented Candidate and do not
require it at top-level. The top-level and Candidate layers have different
semantic roles, rather than being two mandated duplicate representations.

## Read-only implementation and test trace

`discover()` adds `Source <id>: partial` as an `Unknown` uncertainty to the
`CandidateContext` when a represented Source is `Availability.PARTIAL`. Its
`_boundary_limitations()` constructs the top-level tuple from ASU adequacy plus
excluded/unrepresented Sources. A participating partial Source is neither
excluded nor unrepresented, so its partial qualification correctly does not
appear in that boundary tuple. Thus no information is lost and no candidate is
treated as clean/complete.

The downstream code preserves the distinction: applicability exposes
`candidate.limitations`; `ContextItem.select` copies candidate limitations;
package construction places item limitations in `SourceManifestEntry`; and
rendering exposes `item.represented.uncertainty + item.limitations` and manifest
limitations. Existing WS6 tests support candidate preservation for a partial
Source and confirm partial may yield a Candidate while unavailable states do
not. Existing WS8/WS9 tests support package/manifest/rendering qualification
paths. These are supporting implementation evidence, not a new executed
downstream WS4 result. VE-003 itself executed discovery only, so it does not
directly validate later selection/package/rendering preservation.

Candidate-level qualification does not create Authority, Governance State,
currentness, selection, sufficiency, ordering/rank advantage, or success. The
fixed ordering mechanism is independent of uncertainty; applicability and
selection retain limitations; later sufficiency/package rules must evaluate
their material effect.

## Classification, Finding, and impact

**Root-cause classification: D — GOVERNING ARCHITECTURE / REQUIREMENTS ALLOW
MULTIPLE VALID REPRESENTATIONS AND THE FROZEN CONTROL WAS OVER-SPECIFIC.** The
failed criterion improperly made top-level DiscoveryResult representation a
semantic prerequisite. The observed Candidate uncertainty is semantically
sufficient for the governed partial-evidence requirement. No application
product semantic defect, fixture defect, platform difference, or governing
ambiguity is evidenced.

**Finding/H3 recommendation: NO FINDING; H3 NOT TRIGGERED.** The product
conforms to the authoritative preservation model; the control/ER discrepancy
requires a governed successor decision but does not establish a product Finding
or material governance ambiguity. `VE-P4-4A-003` nevertheless remains FAIL.

| Obligation | Evidence impact |
| --- | --- |
| 4.1-A | Expected rejection observed; supporting observation only after overall FAIL. |
| 4.1-B | Expected rejection observed; supporting observation only after overall FAIL. |
| 4.1-C | Partial/absent/unavailable Source observations preserved; not directly validated by failed control. |
| 4.1-D | Four named states observed distinct; supporting observation only, not direct validation. |
| 4.6-B | Attributable, canary-safe, non-audit/non-recovery diagnostic assertions observed; supporting observation only. |

**Platform:** WINDOWS NOT MATERIAL. The discrepancy is produced by deterministic
in-memory semantic objects and field layering before any Windows-specific
filesystem, path, Git, or process behavior. Lane B/C are unaffected. **Item
4.7:** NO INTERACTION.

## Options and required decision

The appropriate path is **Option 1**: Project Owner may authorize a separately
frozen successor control/ER that validates the approved semantic requirement
without requiring top-level duplication, while preserving the 003 FAIL. It
should prove partial qualification at Candidate level and, if downstream scope
is included, its retained item/manifest/rendered qualification—not alter
application behavior merely to satisfy 003. No fixture change or product
remediation is indicated.

**Exact Project Owner decision required:** approve or decline preparation and
execution of a separately identified successor with corrected, authority-traced
partial-evidence acceptance criteria and fresh evidence; confirm whether its
bounded scope should remain discovery-only or include a frozen downstream
selection/package/rendering preservation check. No action is authorized by
this investigation.
