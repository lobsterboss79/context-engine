# WS3 Lane A — Analysis and Preparation

**Status:** PRE-RESULTS ANALYSIS COMPLETE — ONE LANE-PRIVATE CONTROL PREPARED.

## Baseline, authority, and scope

This lane began on `phase4-ws3-crossing-disclosure` at common baseline
`a06e4da5647df26db4ebe886f7bdfd0a95e00767`.  The shared execution contract
and Gate 4A execution authority permit this lane's vertical PASS path.  This
record owns only 3.1-A/B, 3.2-A–F, 3.3-A–C, and 3.6-C.  Item 3.9 is main-only.

## Governing semantics

P2 B7 requires distinct observation/processing/package/disclosure authorization
and fail-closed treatment of ambiguity.  P2 B8 makes Projects isolated by
default; an external path requires task need, governed relationship, relevant
Requester and Consumer authorization, bounded traversal, and identifiable
origin.  P3 WS4 implements the four scope prerequisites in `ScopeInputs` and
`effective_sources`; P3 WS7 separately enforces Requester, Consumer, and
cross-Project facts; P3 WS9 denies a non-disclosable rendering without content,
metadata, reference, or package identifier.

## Existing-evidence assessment

`VE-F5-A-001` is a **DIRECT CANDIDATE only for the narrow default-denial
baseline**: Atlas-only processing excluded an uninspected Beacon before
representation and rendering.  Per the committed WS3 register it is not
pre-approved direct WS3 closure.  It is **SUPPORTING ONLY** for 3.1-A/B and
3.2-C/D/F/3.3-C/3.6-C, and **INSUFFICIENT** for 3.2-A/B/E and 3.3-A/B because
it has neither an all-prerequisite bounded traversal nor independent
Requester/Consumer comparisons.  Phase 3 test evidence is implementation
testing, supporting only for WS3 integrated validation.

## Minimum new control

`CTL-P4-3A-001 v1` uses only approved v0.1 interfaces and one synthetic,
two-Project fact fixture.  It deliberately checks: default and each individual
missing prerequisite scope denial; all-prerequisite one-hop scope inclusion;
corresponding applicability denial/allowance; Requester and Consumer denial as
separate reason codes; and a separately constructed logical package whose
disclosure-denied render has no content or exposed package identifier.  It does
not manufacture an observation, relationship discovery, transitive traversal,
delivery, receipt, use, or an unsupported permission path.

The fixture, expected result, and control were frozen before execution.  A
fresh temporary run directory is required by the control.  Any mismatch is a
FAIL/INDETERMINATE stop, not an invitation to edit this control.
