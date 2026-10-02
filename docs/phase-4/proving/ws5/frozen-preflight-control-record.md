# WS5 Frozen Consumer Preflight Control Record

**Control ID:** `PC-WS5-CHATGPT-PREFLIGHT-v1`  
**Status:** **FROZEN PROCEDURE CONTROL — NOT AN EXECUTION RECORD.**

This control fixes the WS5.2 interaction boundary for the approved
Owner-mediated fresh ChatGPT mechanism.  It creates no Consumer, reservation,
preflight evidence, or WS5 result.

| Control | Frozen value |
| --- | --- |
| Consumer mechanism | Owner-mediated, eligible fresh standalone ChatGPT conversation/session. |
| Consumer-visible preflight input | **None.** The Owner sends no preflight message and attaches/uploads no material. |
| Frozen preflight prompt | **NONE — no Consumer interaction is authorized or required for WS5.2.** |
| Assessment method | Owner-observed and Owner-attested session/account/product state against the channel checklist in `ws5-owner-consumer-reservation-preflight-procedure.md`. |
| Required preservation before classification | Reservation ID; bounded session identity; creation/reservation/preflight timestamps or their ordered equivalent; all channel attestations including unknowns; relevant displayed state/configuration; and confirmation that no message, attachment, or other Consumer exposure occurred. |
| Unknown product behavior or exposure state | **INDETERMINATE**; do not infer safety or substitute a Consumer. |
| PASS condition | Reasonable evidence that every plausible material Project-specific/task-relevant knowledge channel is absent or materially clean, and the exact reserved session has received no material exposure. |
| Post-PASS state | `RESERVED + PREFLIGHTED FRESH + QUARANTINED FROM FURTHER INTERACTION` pending a separate WS6A decision. |

This no-message control is narrower than a task probe: asking the Consumer
about a Project, task, package, status, or prior knowledge would itself create
an unnecessary interaction and could disclose prohibited information.  It does
not relax the requirement to assess reasonably knowable hidden/system/developer
context; an unverified material channel remains indeterminate.
