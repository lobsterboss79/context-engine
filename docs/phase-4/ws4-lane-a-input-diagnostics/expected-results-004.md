# Lane A Expected Results — `ER-P4-4A-004 v1`

**Status:** Frozen for authorized execution. `VE-P4-4A-004` is an independent
successor; it preserves immutable 001/002 INDETERMINATE and 003 FAIL lineage.

## Authority-traced partial-evidence criterion

Checklist 4.1 requires distinct failure, absence, partial evidence, and
successful completion. Phase 1 CE-NFR-029/030, Phase 2 Domain G ST-06,
CI-02/FR-03, Phase 3 WS6, and Phase 3 WS8 require partial evidence to remain
qualified and visible when material, not to occupy a prescribed physical field.
For a participating represented partial Source, PASS requires an attributable
Candidate/Source `Unknown` partial qualification; it must remain through
selected Context Item, Source Manifest, and rendered item/manifest where the
bounded pipeline selects/renders it; it must not become Authority, certainty,
complete evidence, or Sufficient outcome. `DiscoveryResult.limitations` is
recorded but is not an acceptance-location requirement.

## Frozen acceptance criteria

The unchanged v1 fixture supports two CLI `APPLICATION-LEVEL FAILURE` outcomes
(exit 2, attributable generic diagnostics, no validation-success text/canary)
and bounded `ABSENCE`, `UNAVAILABLE`, `PARTIAL EVIDENCE`, and `SUCCESSFUL
COMPLETION`. PASS requires these named states to be distinct; absent/unavailable
have no candidate, unavailable remains a limitation, partial and success each
have one candidate, and partial is qualified at Candidate level. The bounded
partial downstream check requires copied Context Item limitation, attributed
Source Manifest limitation, rendered item/manifest limitation, no Authority,
and an Insufficient result from known-incomplete ASU rather than manufactured
sufficiency. Diagnostics must be attributable, canary-safe, and neither audit,
recovery, nor success.

Validation FAIL means a frozen semantic criterion is violated. INDETERMINATE
means preflight/evidence is insufficient. An expected negative scenario that
satisfies this record can yield validation PASS.
