# Candidate Delivery and Evidence Manifest — WS6A Remediation

**Status:** **PROPOSED SERIAL PROCEDURE — NO DELIVERY OR EXECUTION**

The approved direction is strictly serial: package arm first, then control
arm, and only after package first-response preservation and integrity checking.
The candidate delivery order is:

1. Package arm: frozen task, future-frozen rendering, then the candidate
   wrapper exactly once.
2. Preserve and integrity-check the package first response.
3. Control arm: the same frozen task, then the candidate control baseline
   exactly once.
4. Preserve and integrity-check the control first response.
5. Perform no evaluation until both first responses are preserved.

This sequence is subject to final artifact freeze and a separate explicit
Project Owner WS6A authorization. No Consumer has received any candidate
artifact.

| Arm | Exact delivery record | Raw first response | Ordered events | Response digest | Intervention/deviation record |
| --- | --- | --- | --- | --- | --- |
| Package | `docs/phase-4/validation-evidence/VE-P4-I10-WS6A-003-PACKAGE-001/raw/delivered-input.md` | `docs/phase-4/validation-evidence/VE-P4-I10-WS6A-003-PACKAGE-001/raw/first-response.md` | `docs/phase-4/validation-evidence/VE-P4-I10-WS6A-003-PACKAGE-001/ordered-events.md` | `docs/phase-4/validation-evidence/VE-P4-I10-WS6A-003-PACKAGE-001/derived/first-response.sha256` | `docs/phase-4/validation-evidence/VE-P4-I10-WS6A-003-PACKAGE-001/interventions.md` |
| Control | `docs/phase-4/validation-evidence/VE-P4-I10-WS6A-003-CONTROL-001/raw/delivered-input.md` | `docs/phase-4/validation-evidence/VE-P4-I10-WS6A-003-CONTROL-001/raw/first-response.md` | `docs/phase-4/validation-evidence/VE-P4-I10-WS6A-003-CONTROL-001/ordered-events.md` | `docs/phase-4/validation-evidence/VE-P4-I10-WS6A-003-CONTROL-001/derived/first-response.sha256` | `docs/phase-4/validation-evidence/VE-P4-I10-WS6A-003-CONTROL-001/interventions.md` |

These are destination reservations only. Raw response destinations must remain
empty until a separately authorized event occurs. The first received response
must be copied verbatim and hashed before cleanup, interpretation, evaluation,
or control-arm delivery. Package/control records remain isolated.

Stop and preserve evidence on Consumer discontinuity, quarantine breach,
unexpected interaction, delivery-integrity mismatch, cross-arm disclosure, or
an evaluator-boundary violation. See the
[candidate serial procedure](candidate-execution-procedure.md) for the full
pre-execution and stop-condition sequence.
