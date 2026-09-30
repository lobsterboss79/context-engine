# WS4 Shared Obligation Register

**Status:** **PRE-RESULTS CONTROL — FROZEN FOR LANE-SPECIFIC MATERIALIZATION**

The labels below are approved analysis aids. Exact parent wording remains
controlling; no row creates a new requirement. Governing record abbreviations:
`P4` = Phase 4 checklist; `WS1` = governance/evidence model; `G` = Phase 2
Domain G; `WS10` = Phase 3 operational hardening/recovery closure; `Topo` =
approved WS4 topology.

| ID | Parent exact wording / semantic meaning | Owner / platform | Mode, evidence, reuse | Dependency / deliberate execution / integration |
| --- | --- | --- | --- | --- |
| 4.1-A | 4.1: “Validate malformed input…” — classified malformed input. | A / Windows | Negative; frozen input and preserved classified result. New control. G, WS1, P4. | No dependency; deliberate execution; feeds 4.1-D. |
| 4.1-B | 4.1: “invalid configuration…” — invalid Bootstrap/configuration without false readiness/success. | A / Windows | Negative; frozen configuration/result. New control. G, WS1, P4. | No dependency; deliberate execution; feeds 4.1-D. |
| 4.1-C | 4.1: “missing/unavailable Sources where applicable” — controlled Source outcome. | A / Windows | Negative/positive; controlled Source and outcome evidence. Existing evidence SUPPORTING ONLY. | No dependency; deliberate execution if direct gap remains; feeds 4.1-D. |
| 4.1-D | 4.1: “Confirm that failure, absence, partial evidence, and successful completion remain distinct.” | A / Windows | Static plus execution comparison. New reconciliation control. G/WS10, WS1, P4. | HARD on A/B/C; no separate injection; lane review and later integration input. |
| 4.2-A | 4.2: “Validate interrupted operations…” — predetermined approved-seam interruption and preserved evidence. | B / LNX-01 | Controlled failure/recovery; raw before/after state. New control. G, WS10, WS1, P4. | No hard predecessor; deliberate execution; soft input to B/C and 4.6-A. |
| 4.2-B | 4.2: “persistence integrity…” — integrity and semantic-link checks after controlled operation. | B / LNX-01 | Failure/static evidence; SQLite integrity/state where applicable. New control. | SOFT after 4.2-A; deliberate execution where applicable; integration input. |
| 4.2-C | 4.2: “transaction/partial-state behavior…” — no partial operation appears complete. | B / LNX-01 | Controlled failure/recovery; rollback/incomplete/isolation evidence. New control. | SOFT after 4.2-A; deliberate execution; soft input to 4.6-A. |
| 4.2-D | 4.2: “migration behavior where applicable…” — supported migration or frozen applicability determination. | B / LNX-01 | Conditional execution/static applicability. Phase 3 WS10 SUPPORTING ONLY. | No dependency except applicability; execute only if applicable; integration input. |
| 4.3-A | 4.3: “Validate the existing manual backup capability…” — local/manual backup with explicit destination, purpose, retention basis. | C / LNX-01 | Positive; backup identity/hash and validation evidence. New control. G/WS10, WS1, P4. | No predecessor; deliberate execution; HARD predecessor of 4.3-B. |
| 4.3-B | 4.3: “…and controlled restore only within the approved local/manual boundary.” | C / LNX-01 | Positive/recovery; validated staged restore. New control. | HARD on 4.3-A; deliberate execution; HARD predecessor of 4.4/4.5. |
| 4.4-A | 4.4: “Validate restored Project/Source state, Provenance, governance state, history… and Project isolation as historical evidence where applicable.” | C / LNX-01 | Positive/static comparison. WS3 Lane B restore evidence SUPPORTING ONLY. | HARD on 4.3-B; deliberate execution through restore; integration input. |
| 4.4-B | 4.4: “…audit/construction evidence…” — durable construction/audit retention and authorization-bound access. | C / LNX-01 | Positive/negative restore evidence. New control. | HARD on 4.3-B; deliberate execution; integration input. |
| 4.5-A | 4.5: “restore does not manufacture currentness, Authority, Governance State, present authorization…” | C / LNX-01 | Negative/recovery; recovery qualification/non-elevation evidence. WS3 Lane B is MECHANISM EVIDENCE. | HARD on 4.3-B; deliberate execution; integration input. |
| 4.5-B | 4.5: “…or sufficiency; historical state remains historical until independently re-established.” | C / LNX-01 | Negative/recovery; no manufactured sufficiency/currentness. New control. | HARD on 4.3-B; deliberate execution; integration input. |
| 4.6-A | 4.6: “Validate recovery after controlled failure…” | C / LNX-01 | Predetermined controlled failure/recovery predecessor/successor evidence. New control. | SOFT on 4.2-C; deliberate execution; integration input. |
| 4.6-B | 4.6: “…useful diagnostic/error behavior without treating diagnostics as durable audit or a recovery claim.” | A / Windows | Failure/static diagnostic evidence. New control. | No dependency; deliberate execution where applicable; integration input. |
| 4.7-A | 4.7 exact H3 wording: “If evidence demonstrates a material need for backup scheduling, retention duration, deletion workflow, RPO/RTO, HA, daemon/service deployment, containers, cloud infrastructure, or an additional integration environment, stop and raise it through governance. Do not add it to Phase 4.” | Main only / platform-neutral | Post-lane static evidence review; no lane execution. | HARD POST-LANE on all products; main-only integration/H3 review. |

Historical reuse is never promoted automatically: F4-E, F6-D, R1 v1/v2, and
WS3 Lane B predecessor/successor are **MECHANISM EVIDENCE**; WS3 Lane B
restore/persistence and Phase 3 WS10 are **SUPPORTING ONLY**; DVL-P4-001 is an
active qualification, not WS4 closure evidence.
