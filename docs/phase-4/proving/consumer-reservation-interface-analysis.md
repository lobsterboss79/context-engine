# Consumer Reservation Interface Analysis

**Status:** **ANALYSIS COMPLETE — PROJECT OWNER CONSUMER-MECHANISM DECISION REQUIRED.**

This is an operational analysis only. No Consumer was identified, contacted,
reserved, created, preflighted, or exposed; WS5 and WS6 remain unexecuted.

## Governed Consumer definition

The Consumer is an external downstream role, not a Context Engine-owned model
or application. Phase 2 Domain A lists Consumers, AI providers/models, and the
downstream task environment as separate external classes; Context Engine renders
authorized context for Consumers but does not own Consumers, providers/models,
or downstream actions. A Consumer Contract governs what a Consumer may rely on,
not what technology it must use.

The role encompasses Human, ChatGPT, and Codex renderings in the approved
architecture. This is distinct from Consumer implementation: the architecture
is provider/model independent and selects no API, prompt protocol, delivery
technology, provider, or Consumer-specific implementation technology.

For the approved proving plans, however, Phase 2 I10 identifies the primary
external-proving Consumer as a genuinely fresh ChatGPT Consumer/session/execution,
and I11 likewise specifies a genuinely fresh ChatGPT Consumer for dogfooding.
A different provider can fit the general Consumer architecture but cannot
silently replace the named proving Consumer; that would require a separate
Project Owner proving-protocol decision.

## Freshness dimensions

| Dimension | Governing treatment | Required status for approved proving |
| --- | --- | --- |
| Model identity | No new/different model requirement. | **NOT REQUIRED.** |
| Session/conversation state | I10/I11 require fresh session/execution; new chat alone is insufficient. | **REQUIRED** to assess. |
| Prior task exposure | Hidden briefing or accumulated task knowledge is prohibited. | **REQUIRED** absent/materially clean. |
| Prior Context Package exposure | Prior package/run exposure is a named WS1 preflight channel. | **REQUIRED** absent/materially clean. |
| Prior Project knowledge | Material Project-specific knowledge that could compensate for package defects contaminates. | **REQUIRED** absent/materially clean. |
| Project/repository/workspace access | WS1 requires assessment of Project/workspace and connected files/Sources. | **REQUIRED** to assess; material accessible Project knowledge contaminates. |
| Memory/history | Persistent/model memory and prior sessions are named preflight channels. | **REQUIRED** to assess; not automatically disqualifying unless material. |
| Account identity | No particular account identity is selected. | **NOT SPECIFIED**, except its settings/exposures are preflight evidence. |
| Custom instructions, tools, connectors | Product-specific mechanisms are not selected, but hidden/system/developer context and tool/connector exposure are named channels. | **REQUIRED** to assess when applicable. |

Freshness is a combination of session state, relevant accessible state, and
prior Project/task/package exposure—not vendor identity or a metaphysical claim
that the model has never heard the Project name. The Consumer must not have
material knowledge that could compensate for omissions, errors, ambiguity, or
insufficient Context Package content. New project/repository attachment,
connected files, prior session context, manual briefing, or a prior proving run
can contaminate it if materially task-relevant.

The current Codex agent/session and this conversation are contaminated: they
contain extensive Context Engine Project and proving knowledge. They cannot be
a WS5 candidate. This is a governed inference from the freshness standard, not
a claim about Codex product behavior.

## Existing implementation and interfaces

The v0.1 implementation has a Consumer identity model, disclosure authorization,
Consumer Contract, and Human/ChatGPT/Codex renderers. The rendering service
produces faithful presentation content from a logical package and expressly does
not claim delivery, receipt, use, or downstream action. It has no direct
Consumer invocation, API client, prompt/output exchange adapter, session
reservation mechanism, or Consumer-output capture adapter.

Thus the repository supports package/rendering export suitable for a controlled
handoff, but no existing interface permits current Codex to reserve, preflight,
deliver to, or capture output from an external Consumer. A new adapter is not
required by the approved architecture and must not be built merely to execute
proving.

## Option analysis

| Option | Architecture / approved proving compatibility | Freshness, evidence, and control | New software or protocol decision |
| --- | --- | --- | --- |
| A. Fresh ChatGPT conversation/session | **Approved proving-compatible.** I10/I11 name fresh ChatGPT. | Achievable only by WS5 assessment of all material knowledge channels; preserve exact session boundary, inputs, output, interventions, and preflight basis. | No API required; product settings/capabilities require operational verification. |
| B. Fresh Codex session | Architecture-compatible Consumer rendering exists, but **not the named I10/I11 proving Consumer**. Current session is contaminated. | Could be assessed only under an amended Owner-approved protocol. | Separate Owner decision required. |
| C. Fresh Claude conversation/session | General architecture-compatible but not named proving Consumer. | Vendor identity does not establish freshness; same WS5 controls apply. | Separate Owner protocol decision required. |
| D. Fresh Claude Code session | Same as C; agent tooling/repository access raises preflight channels. | Must assess material workspace/tool/history exposure. | Separate Owner protocol decision required. |
| E. Another supported model/agent | Provider-neutral architecture permits Consumer types in principle. | Must be reservable, preflightable, identifiable, and able to preserve raw output. | Separate Owner protocol decision required. |
| F. Owner-mediated transfer to fresh ChatGPT | **Compatible with I10/I11 and the technology-neutral delivery architecture.** | Valid if frozen inputs and transfer/output provenance are preserved and Owner does not add material briefing or alteration. | No new software/API required. |
| G. Programmatic/API Consumer | Architecture-compatible in principle. | Could preserve identity/inputs/output, but does not by itself establish freshness. | Not required; introducing it now would require separate approval and credentials/cost decisions. |
| H. Existing Context Engine Consumer adapter | No such adapter exists. The renderer is not an invocation/delivery adapter. | Cannot reserve or preflight a real Consumer. | Building one is not authorized. |
| I. Other already contemplated mechanism | Human Consumer and technology-neutral delivery are contemplated generally. | Must preserve the same freshness, input/output, and intervention evidence. | A non-ChatGPT proving substitution still needs Owner protocol approval. |

## Manual Project Owner mediation

The proposed manual procedure is valid in principle for the named ChatGPT plan;
the approved architecture intentionally selects no API, delivery protocol, or
receipt technology. It remains valid only if it preserves the distinctions among
logical package, rendering, delivery, receipt, and use and does not let manual
transfer become material reconstruction or coaching.

Required operational controls:

1. Repository-side controller freezes candidate eligibility, preflight procedure,
   allowed/prohibited inputs, expected evidence, and run identity before contact.
2. The Owner opens/reserves an eligible fresh ChatGPT session and records the
   minimum session/account/configuration identity needed for audit, without
   Project briefing.
3. The Owner performs only the frozen preflight, preserves the original
   interaction verbatim (or otherwise durably and completely), and records
   relevant unknowns and exposure channels.
4. A PASS Consumer receives no other interaction before the separately
   authorized WS6A run.
5. Before WS6A, the repository-side controller freezes task, package/rendering,
   criteria, and allowed input. The Owner transfers those materials verbatim,
   records the delivery procedure/time, and does not add explanation,
   correction, or task-relevant information.
6. The Owner returns raw Consumer output verbatim with sufficient identity/time
   and transfer provenance. Repository-side records preserve it before
   evaluation; all intervention is separately recorded.
7. The evaluator reviews frozen original evidence and does not repair, coach,
   rewrite, or alter criteria before classification.

Hashes can strengthen integrity but are not a repository-mandated requirement.
Verbatim retained content plus run/session identity, timestamps or equivalent
sequence evidence, frozen inputs, transfer record, raw output, and intervention
record are the minimum audit-relevant evidence. Owner participation in later
governance decisions is not manual reconstruction; providing prior material
Project state beyond the frozen task/package is.

## ChatGPT, Codex, Claude, and product-specific facts

A fresh ChatGPT session can be a valid Consumer only when its exact session and
exposure state satisfy WS5. Project/repository attachment, memory, prior history,
custom instructions, connected files, and tools/connectors are not assumed
safe or unsafe by repository policy; they must be assessed as applicable
preflight channels. The repository does not specify how a product exposes or
disables those features. That requires operational/product verification before
a particular candidate is reserved.

A fresh Codex, Claude, Claude Code, or other agent is not inherently fresher.
For Claude Code and tool-enabled agents, repository/workspace and tool access
are particularly relevant preflight channels. The approved external and
dogfooding plans name ChatGPT, so use of any of these alternatives requires
an explicit Owner decision to amend the frozen proving protocol rather than a
convenience substitution.

## Minimum controllable interface and recommendation

A valid interface needs no API. It must permit the controller/Owner to:

- create or reserve an identifiable session before material Project exposure;
- determine and record relevant memory, context, workspace/files, history,
  connector, manual-briefing, and hidden-context exposure;
- restrict WS5 interaction to the frozen preflight;
- preserve the exact preflight exchange before assessment;
- preserve the session unexposed after a freshness PASS;
- later deliver frozen task/package material verbatim;
- capture raw output and all material interventions; and
- return the evidence to repository-side preservation/evaluation.

The least complex architecture-compliant mechanism now is **Project Owner
manual mediation with a new, controllable ChatGPT session**, using the frozen
WS5 contract and a repository-side evidence package. It does not require new
software, an API, a Consumer adapter, Windows, LNX-01, cloud infrastructure,
or another integration environment. It does require that the Owner can
operationally establish and document the session's material exposure state;
if that cannot be done faithfully, WS5 must stop rather than create an
additional environment or adapter.

## DVL, TD-14, Findings, and decision boundary

The absence of a Consumer-control interface in the current Codex environment is
an execution dependency, not evidence of a product defect, accepted limitation,
Finding, H3, TD-14 trigger, or architecture gap. It does not change DVL-P4-001,
which remains ACTIVE / ACCEPTED / DEFERRED, and it does not reopen TD-14, which
remains TRIGGER NOT MET / CLOSED / NOT REOPENED. No new environment is required.

**Exact Project Owner action required:** make available an eligible, controllable
fresh ChatGPT session and act as the constrained manual mediator under the
frozen WS5 procedure, with a durable method to preserve the preflight exchange
and later raw output. If the Owner instead wishes to use Codex, Claude, Claude
Code, another model/agent, or an API, first record a separate proving-protocol
decision specifying that substitution and its controls.
