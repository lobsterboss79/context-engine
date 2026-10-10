# Candidate Successor-004 Arm-Isolated Evidence Destinations

**Status:** **PRE-FREEZE CANDIDATE DESTINATIONS — PRESERVED — FROZEN SUCCESSOR-004 DESIGN EXISTS**

## Boundary

These are proposed, arm-isolated destinations for a future authorized run.
They contain no delivery, event, response, hash, or intervention evidence.
They do not reserve a Consumer or establish successor-004.

| Arm | Proposed root | Required future evidence |
| --- | --- | --- |
| Package | `docs/phase-4/validation-evidence/VE-P4-I10-WS6A-004-PACKAGE-001/` | `raw/delivered-input.md`; `raw/first-response.md`; `ordered-events.md`; `derived/first-response.sha256`; `intervention-deviation.md`; `derived/integrity-validation.md` |
| Control | `docs/phase-4/validation-evidence/VE-P4-I10-WS6A-004-CONTROL-001/` | `raw/delivered-input.md`; `raw/first-response.md`; `ordered-events.md`; `derived/first-response.sha256`; `intervention-deviation.md`; `derived/integrity-validation.md` |

## Retention and ordering requirements

For each arm, the exact delivered input must be preserved before any response
assessment. The first raw Consumer response must be preserved verbatim and
SHA-256-hashed before cleanup, interpretation, evaluation, or control-arm
delivery. Package and control evidence must remain isolated. The control arm
may not begin until package first-response preservation and package-arm
integrity validation pass.

No response has been fabricated, and no event has occurred. The paths above
are candidates retained as preparation evidence. The frozen successor-004
destination design is at
[`../ws5.5-s-ws6a-004/evidence-destinations.md`](../ws5.5-s-ws6a-004/evidence-destinations.md);
separate WS6A authorization remains required.

## Evidence basis

- [Candidate delivery and evidence manifest](candidate-delivery-and-evidence-manifest.md)
- [Candidate serial execution procedure](candidate-execution-procedure.md)
