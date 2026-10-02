# WS5 Owner Consumer Reservation and Preflight Procedure

**Status:** **FROZEN PROCEDURE — WS5.1 / WS5.2 MATERIALIZATION ONLY; NOT EXECUTED.**

**Approved mechanism:** Project Owner-mediated fresh ChatGPT session. The
Project Owner is the constrained manual mediator. No API, Consumer adapter,
new environment, alternate provider, or agent substitution is authorized.

This procedure operationalizes the frozen
[freshness contract](freshness-contract.md), [execution contract](execution-contract.md),
[Consumer interface analysis](consumer-reservation-interface-analysis.md), and
[WS5 control](ws5/frozen-preflight-control-record.md). It does not identify,
open, reserve, contact, or preflight a Consumer, and does not authorize WS6A.
WS5 remains unexecuted until the Owner performs this procedure.

## Eligibility requirements for the ChatGPT Consumer

The candidate must be an ordinary **new, standalone ChatGPT conversation**
whose exact session boundary can be recorded. A new visible conversation is
necessary but is not sufficient.

The Owner must be able to establish the following before reservation:

| Channel / condition | Eligibility requirement | Owner verification / consequence |
| --- | --- | --- |
| New conversation | Created as a new conversation before any Context Engine or proving exposure. It has no prior messages. | Record creation time or equivalent ordered event and confirm message count is zero. A prior message is an invalid reservation. |
| Project membership/context | Not created in, moved into, or associated with a ChatGPT Project/workspace that contains Context Engine or proving material. | Verify the conversation is standalone and has no Project context. If product behavior or a Project association cannot be determined, it is indeterminate. |
| Prior Context Engine exposure | No material Context Engine Project knowledge, files, packages, renderings, architecture/state/decision material, or manual briefing accessible through any channel. | Known material exposure fails; an unassessable plausible material channel is indeterminate. General world/pretraining knowledge is not automatically contamination. |
| Prior proving-task exposure | No knowledge of a future WS6A task/request, expected result, rubric, hidden answer, task-specific history, or prior task briefing. | Known exposure fails; unknown material exposure is indeterminate. |
| Prior proving-package exposure | No prior Context Package, rendering, manifest, source material, prior proving result, or package/run discussion for either proving exercise. | Known exposure fails; unknown material exposure is indeterminate. |
| Repository/file access | No Context Engine repository, workspace, folder, cloud file, connected Source, uploaded file, or reachable file tool that can expose material Context Engine/proving information. | Verify no such access is attached, connected, or available. If a connected capability cannot be inspected well enough to assess material exposure, it is indeterminate. |
| Memory/history | Persistent/model memory, prior ChatGPT sessions/history, and any account-level retained context must be assessed for material Project-specific/task-relevant knowledge. | It is not automatically disqualifying merely because memory/history exists; known material knowledge fails, and unknown/contradictory material exposure is indeterminate. |
| Custom instructions | No custom instruction, account/workspace instruction, or other applicable instruction contains material Context Engine or proving knowledge. | Verify applicable instructions as product behavior permits. Material content fails; inability to assess an applicable instruction is indeterminate. |
| Connected apps, tools, connectors | No enabled/available app, connector, tool, or integration may expose material Context Engine/proving knowledge. | Do not attach or enable any. Where the product exposes available tools/connectors, verify that none have material access. Unknown material access is indeterminate. |
| Prior messages | The candidate conversation has none. | Any earlier user, assistant, system-visible, imported, shared, or otherwise retained conversation content is a reservation failure unless it is demonstrably outside every plausible material channel; this procedure does not use that exception—select a new clean conversation instead. |
| Account identity | No particular account identity is required. | Do not provide account name, email, or other unnecessary personal information. Record only a non-personal state attestation sufficient to assess its memory/history/instruction/project/access exposures. |
| Model/configuration | No named model, new model, or different model is required. | Record a displayed model/configuration label only if available and relevant to the session boundary; assess any configuration that can supply hidden context, instructions, memory, files, or tools. Do not infer product behavior that cannot be established. |
| Temporary/incognito-style chat | Not required by governance and not a substitute for the checks above. | It is optional only if it still permits the required session boundary and state assessment. It neither establishes freshness by itself nor excuses missing evidence. |

The repository does not prescribe how ChatGPT exposes Projects, memory,
instructions, tools, connectors, temporary chats, conversation identifiers, or
hidden context. The Owner must verify the product behavior actually available
for the candidate; do not guess that a feature is absent, disabled, isolated,
or harmless.

## PROJECT OWNER ACTION PROCEDURE

### WS5.1 — Identify and reserve an eligible candidate

1. Before opening ChatGPT, open this procedure and the frozen control record.
   Prepare an external, non-Consumer note using the reservation ID format
   `WS5-CHATGPT-<YYYYMMDDThhmmss±ZZZZ>-<sequence>`. Prepare a way to retain
   the exact return information below. Do not prepare, copy, or display any
   future WS6A task, package, rendering, expected result, rubric, answer,
   repository content, or proving history.

2. Use the approved ChatGPT product to create one **new standalone
   conversation**. Do not enter it through a Context Engine-related Project or
   workspace and do not reuse an existing conversation, shared conversation,
   prior temporary conversation, or prior proving conversation.

3. Before sending any message, attachment, file, link, pasted material, or
   voice/image input, inspect the product state to the degree it permits.
   Externally record the bounded session identity (for example, opaque
   conversation ID/URL token or another non-personal boundary), creation time
   or equivalent sequence evidence, and any displayed model/configuration
   label. Do not place the reservation ID in the conversation.

4. Confirm that the conversation has zero prior messages; is standalone rather
   than Project-associated; has no uploaded/attached/imported/shared files;
   and has no Context Engine repository, workspace, Source, package, or
   proving material available to it.

5. Inspect and record the applicable account/session exposure channels:
   memory/history, custom instructions, Project/workspace context, connected
   apps/tools/connectors, and reasonably knowable hidden/system/developer
   context. Record each as `clear`, `contaminated`, or `unknown`, with a short
   basis. Do not ask the Consumer to self-report these matters.

6. Confirm that the Owner has provided no manual briefing and that no one has
   provided material Project, proving, task, package, result, rubric, or answer
   information to the candidate through another channel. Record this as an
   Owner attestation.

7. If all eligibility requirements are established as clear and no prohibited
   action has occurred, associate the external reservation ID with the bounded
   session identity and mark the external note **RESERVED — AWAITING WS5.2**.
   The session becomes formally **RESERVED** at that point—not when the chat is
   merely opened, and not by sending a reservation message to it.

8. Stop immediately on any uncertainty, contamination, or reservation breach.
   Preserve the external note and any available state evidence. Do not clean,
   coach, replace, or silently substitute the candidate.

#### WS5.1 prohibited actions and invalidation

Until a successful WS5.2 classification, the Owner must not send a message;
upload or attach a file; paste a link or repository material; turn on or attach
a tool, app, connector, or Project; move the conversation into a Project;
change a context-affecting model/configuration; use the conversation for an
unrelated question; disclose the reservation identity to the Consumer; or
reveal any future task, package, result, rubric, answer, Project state, or
proving history. Any such action after the candidate is opened invalidates the
reservation. Known pre-existing material exposure is a failure; unresolvable
uncertainty is indeterminate.

### WS5.2 — Governed contamination/freshness preflight

1. Work only with the exact externally recorded `RESERVED` session. Confirm its
   bounded identity matches the reservation record and that no interaction or
   state change has occurred since WS5.1.

2. Apply `PC-WS5-CHATGPT-PREFLIGHT-v1` to the following channels, recording
   for each: known exposure or uncertainty; whether it is materially
   Project-specific/task-relevant; assessment basis; and `clear`,
   `contaminated`, or `unknown` assessment:

   - persistent/model memory;
   - current conversation/context, including prior messages;
   - Project/workspace context;
   - connected Sources/files and repository/workspace access;
   - prior sessions/history;
   - prior Context Packages/renderings;
   - prior proving runs/results, tasks, rubrics, or expected answers;
   - manual briefing or other human transfer;
   - custom instructions and reasonably knowable hidden/system/developer context;
   - tools, apps, and connectors; and
   - any other plausible material channel.

3. Send **no message**. The frozen preflight prompt is:

   > **NONE — no Consumer interaction is authorized or required for WS5.2.**

   The Owner must not replace this with an inquiry about the Project, the
   future task, the package, prior knowledge, or settings. The assessment is
   based on externally observable/knowable session and account state plus the
   Owner’s documented exposure attestation.

4. Before classifying, preserve the completed external channel record, ordered
   timestamps (or equivalent sequence evidence), bounded session identity,
   and the attestation that no Consumer-visible preflight input, attachment,
   or response exists. A screenshot is optional corroboration, not required
   evidence, unless it is the only available way to preserve an observed state.

5. Apply the WS5.2 decision criteria below. Do not solve an unknown by asking
   the Consumer, changing product settings, or exposing the future proving
   material. Return the required evidence to Codex for preservation and WS5
   disposition. A PASS does not authorize WS6A.

## Decision criteria and required Owner action

### WS5.1 reservation result

| Result | Exact condition | Required Owner action |
| --- | --- | --- |
| **PASS (RESERVED)** | Every eligibility channel is reasonably established clear; the chat is new, standalone, message-free, and unexposed; bounded identity and external reservation record exist. | Mark `RESERVED — AWAITING WS5.2`; perform only WS5.2. |
| **FAIL** | Known material prior Project/task/package/proving knowledge or accessible material context exists before formal reservation. | Mark unsuitable; preserve the basis; do not preflight or use it for proving. |
| **INDETERMINATE** | A plausible material channel is unknown, contradictory, or cannot be assessed sufficiently. | Mark unsuitable; preserve the uncertainty; do not preflight or use it for proving. |
| **INVALID RESERVATION** | A prohibited action or material exposure occurs after opening the candidate, or the session boundary/zero-message state cannot be preserved. | Mark invalid; preserve the breach; do not repair, continue, or substitute automatically. |

### WS5.2 preflight result

| Result | Exact condition | Required Owner action |
| --- | --- | --- |
| **PASS (PREFLIGHTED FRESH)** | Preserved evidence reasonably establishes that all plausible material channels are absent or materially clean; no Consumer interaction/exposure occurred; and the exact reservation remains intact. | Mark `RESERVED + PREFLIGHTED FRESH + QUARANTINED FROM FURTHER INTERACTION`; return the evidence to Codex; await a separate WS6A decision. |
| **FAIL** | Preserved evidence establishes material prior Project-specific/task-relevant knowledge or access that could compensate for package defects. | Mark unsuitable; preserve evidence; stop. It is not a valid proving failure and does not permit WS6A. |
| **INDETERMINATE** | Preserved evidence cannot reasonably establish freshness because a relevant channel is unknown, contradictory, unverifiable, or insufficiently evidenced. | Mark unsuitable; preserve evidence; stop. INDETERMINATE is not PASS and does not permit WS6A. |
| **INVALID RUN / INVALID RESERVATION** | Any material protocol breach, prohibited Consumer exposure, state/configuration change that affects the exact session, unpreserved original preflight basis, uncontrolled event preventing attribution, or mismatch with the reserved session occurs. | Preserve original evidence; mark `INVALID — DISCARD/RESTART`; do not normalize it to PASS/FAIL, repair it, or substitute automatically. |

No result authorizes an automatic replacement Consumer. Any later candidate
requires the same frozen procedure and a separately recorded reservation.

## Post-PASS quarantine

After WS5.2 PASS, retain the exact session as:

`RESERVED + PREFLIGHTED FRESH + QUARANTINED FROM FURTHER INTERACTION`

Until a separate Project Owner WS6A authorization, the Owner must not send any
additional message; upload, attach, paste, or link any content; change model
or configuration; enable/attach tools, apps, connectors, or memory features;
move the chat into a Project; expose repository, file, Source, Context Engine,
or proving information; share or import the conversation; or use it for an
unrelated question. Do not reopen it for convenience. If product interaction
or a necessary setting change is unavoidable, stop and report it before doing
so; do not assume the reservation remains valid.

The Owner may preserve the external evidence and return it to Codex. That
external handoff must not modify the Consumer session. A later WS6A decision,
if granted, must separately freeze its task, package/rendering, criteria,
permitted inputs, run identity, and transfer record before any Consumer
exposure.

## OWNER -> CODEX RETURN TEMPLATE

Paste the following into the existing Codex controller session after completing
WS5.1 and/or WS5.2. Do not include account name, email, credentials, or other
unnecessary personal information.

```text
Consumer reservation ID:
WS5 attempted step(s): [WS5.1 only / WS5.1 + WS5.2]
Session type/state: [new standalone ChatGPT conversation; current state]
Bounded session/conversation identity: [opaque ID/URL token or bounded equivalent]
Creation/reservation/preflight timestamps or ordered equivalent:
Displayed model/configuration (if available/relevant):

Eligibility checks:
- New conversation / zero prior messages:
- Project membership/context:
- Prior Context Engine exposure:
- Prior proving-task exposure:
- Prior proving-package/run exposure:
- Repository/file/connected Source access:
- Memory/history exposure:
- Custom instructions:
- Tools/apps/connectors:
- Manual briefing / other human transfer:
- Reasonably knowable hidden/system/developer context:
- Other plausible channel:

For each check: [clear / contaminated / unknown] — assessment basis and material relevance.

Frozen preflight prompt:
NONE — no Consumer interaction is authorized or required for WS5.2.
Raw preflight response:
NONE — no Consumer message was sent and no Consumer response exists.
Consumer-visible preflight input/attachment:
NONE.

Preflight result observed: [PASS / FAIL / INDETERMINATE / INVALID]
Reservation/result state: [RESERVED / PREFLIGHTED FRESH + QUARANTINED / UNSUITABLE / INVALID]
Unexpected interaction, exposure, configuration change, or other relevant state:
Evidence retained outside Consumer: [channel record; timestamps/order; bounded identity; optional screenshot only if used]
Owner attestation: [no future WS6A task, package, expected result, rubric, answer, task-specific history, or Context Engine material was disclosed to the Consumer; no unreported interaction occurred]
```

## WS6A boundary

After a successful WS5.2, Codex may preserve/evaluate WS5 evidence, finish
remaining WS5 obligations, determine WS5 disposition, and prepare the exact
WS6A Owner decision package. Codex must not authorize or execute WS6A. The
reserved Consumer remains untouched until that later Project Owner decision.

## Exact next Owner action

Under the current authorization, the Owner’s next action is: **review this
frozen procedure and make a separate explicit decision before executing WS5.1.**
No Consumer may be identified, opened, reserved, contacted, or preflighted
until that execution direction is given. If execution is later directed, begin
with WS5.1 step 1: prepare the external reservation note, then create one new
standalone ChatGPT conversation without sending it any message or exposing it
to any material.
