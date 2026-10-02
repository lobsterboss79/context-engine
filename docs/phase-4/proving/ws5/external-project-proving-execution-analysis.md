# External-Project Proving Execution Analysis

**Status:** **ANALYSIS COMPLETE — PROJECT OWNER EXECUTION-MODEL DECISION REQUIRED.**

**Scope:** Architecture/governance analysis only. No Company AI Roadmap material
was accessed, copied, transferred, observed, or exposed; no Consumer was
contacted; no successor was executed; and no WS6A execution is authorized.

## Current governed state

I10/WS6A remains unchanged: the proving Project is Company AI Roadmap and WS6A
remains a real-project external proving exercise. The earlier records remain
unchanged:

- predecessor WS5.5: **INDETERMINATE — STOP AND PRESERVE**;
- `WS5.5-S-WS6A-001`: **PARTIALLY FROZEN / INDETERMINATE — STOP AND PRESERVE**;
- `CE-P4-WS5-CONSUMER-001`: **RESERVED + PREFLIGHTED FRESH + QUARANTINED + ZERO
  MESSAGES + UNEXPOSED**, assigned only as the package arm; and
- no control Consumer exists.

## 1. Architecture compatibility: co-location is not required

Approved architecture treats Sources as external, preserves a Source's
identity separately from its locator, and treats Project registration as a
governed context boundary rather than a filesystem location. A Source Adapter
is a Source-specific observation boundary; the architecture does not choose a
physical Project identity or require Context Engine and its observed Project to
reside in one local environment. It also distinguishes logical package,
rendering, delivery, receipt, and use. Therefore a controlled external
Project/Source environment and Owner-mediated rendering delivery are
architecture-compatible in principle.

This conclusion does **not** establish that an arbitrary transfer is safe or
that present v0.1 supports it. Source authorization, Consumer disclosure
authorization, sensitivity/secret handling, Source Scope, ASU, observation
state, provenance, and construction-state coherence remain controlling.

## 2. Source-observation boundary

### Required governed information

For a valid Company AI Roadmap package, Context Engine requires an established
Project/Bootstrap/configuration relationship; registered Source identities and
scopes; task-relative ASU; inspection authorization; the Source content needed
to represent task-relevant evidence; and material native observation state.
For local Git/Markdown v0.1, material native state includes repository/work-tree
boundary, observed HEAD/revision, branch/detached state, working-tree state,
relevant history, and limitations. It is not enough to supply an ungrounded
hash, summary, or manually asserted expected state.

| Distinction | Meaning / boundary |
| --- | --- |
| Raw Source | Native Git repository and Markdown artifact content, metadata, and working/history state. It remains external and may be sensitive. |
| Source observation | What the adapter actually established from a bounded authorized Source scope, with native identity/version/state/time/capability/limitation provenance. It is evidence, not a final package. |
| Logical Context Package | Governed task-specific selection, authority/currentness/provenance/uncertainty/limitation/sufficiency/coherence result associated with a request. |
| Consumer rendering | Faithful Consumer-specific presentation of a completed package. It is not delivery, receipt, use, or new authority. |

No approved requirement says raw Source contents or observation artifacts must
be copied into the Context Engine repository. It does require enough authorized
evidence, wherever retained, to substantiate/reconstruct the governed result
and preserve the applicable limitations.

## 3. Package-construction location models

| Model | Architecture compatibility | Current v0.1 support | Data movement / provenance / risk | Decision |
| --- | --- | --- | --- | --- |
| **A. LNX-01 consumes exported observations** | A general external Source boundary could support an approved import/adapter. | **Not supported.** v0.1 implements only a local Git/Markdown adapter and no governed observation import/export format or adapter. | Requires work-derived observation/content to leave the work environment; manual normalization can lose native semantics or create unverified claims. | Not viable without separately authorized product/protocol work and external permission. |
| **B. Existing Context Engine capability runs in work environment** | **Compatible.** Sources remain external to the engine repository; local Git observation occurs where the local repository is authorized. | Potentially supported by the local Git/Markdown capability, provided the approved v0.1 code/runtime and local Git repository are available there. No Consumer adapter is needed. | Raw Sources, observation, package construction, and sensitive evidence can remain in the work environment. Preserve native provenance closest to observation. Direct rendering transfer still needs disclosure authorization. | **Recommended conditional model.** Requires Owner execution-model decision and applicable company authorization. |
| **C. Owner manually constructs/transfers observation inputs to LNX-01** | Architecture permits governed inputs but does not treat human assertions as adapter observation automatically. | **Not supported as a faithful current-v0.1 observation path.** No import boundary exists. | Requires work data movement and risks manual reconstruction, provenance loss, and unverified semantic elevation. | Do not use without a separately governed import/protocol capability. |
| **D. Owner-mediated final-rendering transfer from Model B** | **Compatible.** Delivery is intentionally technology-neutral and distinct from package construction. | Supported as manual mediation under the frozen proving procedure; renderer does not claim delivery/receipt/use. | Transfers only permitted frozen rendering/task directly to Consumer; preserves verbatim delivery record and hashes. | Required complement to Model B, conditional on disclosure authorization. |

Model B is not an architecture amendment, but running it in a work environment
is a separate execution-location choice. Existing Phase 4 controls do not
silently authorize a new environment; the Owner must decide the exact
environment and preserve its identity/configuration. Whether that use is
permitted in the work environment is an external/company permission question,
not a Context Engine governance inference.

## 4. Minimum cross-boundary data

The recommended Model B minimizes movement by retaining raw and constructed
work-derived artifacts in the work environment. Required cross-boundary data
depends on the authorized retention location, not simply on artifact type.

| Artifact | Needed for package construction | Need retain in Context Engine repository? | Boundary treatment |
| --- | --- | --- |
| Raw Company AI Roadmap Sources / Git repository | Yes, at the observation location. | No. | Remain in authorized work environment. |
| Normalized observations / Source content | Yes, if represented by current pipeline. | No. | Remain with construction evidence; no LNX export under current constraint. |
| Source metadata, hashes, authority/applicability data | Material to provenance/selection when applicable. | Only non-sensitive bounded identity/hash/classification evidence if disclosure permits. | Preserve externally in full; record minimal non-sensitive references in repository. |
| Source/ASU manifest | Required for package construction/evaluation. | Not necessarily in full. | External full manifest; repository may retain opaque ID/hash, non-sensitive scope/classification, and limitation statement. |
| Logical Context Package | Required before rendering. | No. | Retain in authorized work evidence location unless approved for repository storage. |
| Consumer rendering | Required Consumer-visible artifact. | No prerequisite to repository storage. | Freeze/hash at work location; Owner may deliver directly and preserve controlled evidence externally. |
| Proving task | Required Consumer input. | Yes if non-sensitive and approved; otherwise retain externally with ID/hash. | Freeze before exposure. |
| Consumer output | Required proving evidence. | No requirement that it be in this repository. | Preserve original in an authorized evidence location; repository may hold ID/hash/classification/order and non-sensitive rationale. |
| Evaluator evidence | Required for evaluation. | Only enough authorized, non-sensitive evidence for the claimed repository record. | Full sensitive assessment may remain externally, with bounded repository lineage. |

Generated does not mean safe to transfer. A rendering, manifest, hash locator,
or Consumer output can itself disclose sensitive content, metadata, or
relationships; Consumer disclosure authorization and external/company policy
remain separate from generation.

## 5. Evidence retention

Approved requirements demand material auditability, provenance, and substantial
reproducibility; they do not require indefinite retention, wholesale repository
copying, or disclosure of protected provenance. Audit is explicitly
authorization/security/privacy/retention bound. Thus the Context Engine
repository may retain only authorized non-sensitive proving lineage such as
opaque evidence IDs, artifact hashes, classifications, ordered events,
attestations, non-sensitive manifest facts, criteria/result state, and links or
references usable by authorized reviewers.

Actual raw Source, logical package, rendering, raw Consumer output, and full
evaluation evidence must be preserved somewhere sufficient and authorized to
support the proving claim. If no authorized location can preserve those
originals and their provenance, the run is INDETERMINATE or INVALID as the
frozen protocol requires; a hash alone does not replace evidence needed for
authorized evaluation.

## 6. Consumer delivery

The package-arm Consumer may receive the authorized frozen rendering directly
from the work environment through Owner mediation; the rendering need not first
be stored in the personal Context Engine repository. Before delivery, the work
environment record must freeze task, package, rendering, source/ASU and
construction basis, criteria, exact-run ID, and integrity values. The Owner
copies the exact task followed by the exact rendering verbatim, records the
ordered delivery, and preserves the first raw response before evaluation.

This supports integrity without claiming that rendering equals delivery,
receipt, or use. It remains conditional on Consumer disclosure authorization
and any external/company permission for transferring the rendering to ChatGPT.

## 7. Control arm under the external boundary

I10 requires the same task plus ordinary minimal pointer/access for a distinct
fresh control Consumer, rather than the Context Engine package. The governing
records do not choose the exact pointer/access mechanism. For a real work
Project, a meaningful baseline may require the control Consumer to receive an
authorized ordinary pointer or direct access to work material; that is not
automatically permitted by Context Engine governance.

The Owner must freeze a baseline that is legitimate, ordinary, no more helpful
than the normal access route, and not deliberately handicapped. It cannot be
the package, expected answer, rubric, coaching, or package-arm output. Any
direct Consumer access to Company AI Roadmap content, repository, links, or
systems requires separate external/company authorization. No control Consumer
may be created or exposed until that baseline and its authorization are frozen.

## 8. Current implementation and minimum work-environment capability

The architecture's general Source Adapter boundary permits external Source
types and locations. The current implementation is narrower:

- `LocalGitSourceAdapter` observes only a registered **local** Git repository
  selected by a filesystem locator; it does not contact remotes or import an
  observation artifact.
- v0.1's Git/Markdown path needs access to the actual local repository and
  task-relevant Markdown content to preserve required native/source evidence.
- the renderer produces a transient Consumer-facing presentation and has no
  delivery, receipt, use, session, or external-observation import/export
  adapter.

Therefore Model A/C would require new product implementation—an observation
import/export adapter or equivalent governed capability—not mere proving
instrumentation. That is neither authorized remediation nor a proven defect;
it is a potential implementation/scope decision under H3.

Model B's minimum capability is only: an authorized environment with the
existing approved v0.1 Context Engine code/runtime, its already-required Python
and dependency runtime, a local `git` executable, read access to the approved
local Company AI Roadmap repository, and an authorized controlled location for
the run's state/evidence. No Codex, Claude Code, GitHub access, administrative
rights, or new Consumer adapter is inherently required. Availability and
permission for those capabilities are external facts to verify, not assumed.

## 9. Permission and governance decision boundaries

| Decision/action | Decision owner |
| --- | --- |
| Freeze Context Engine task, criteria, package/run protocol, evaluation, and non-sensitive repository evidence treatment | Project Owner under Context Engine governance. |
| Authorize Model B as the exact proving execution location and preserve its environment/baseline evidence | Project Owner, subject to applicable external permission. |
| Permit access to Company AI Roadmap repository/Bootstrap/Sources in work environment | External/company authorization; not inferred here. |
| Permit Source-derived package/rendering or control pointer/access to be sent to ChatGPT | External/company authorization plus Context Engine Consumer disclosure authorization. |
| Retain raw Sources/package/rendering/output outside the Context Engine repository | External/company retention authorization, with Context Engine evidence requirements applied to the authorized record. |
| Transfer any work-derived artifact to LNX-01 or a personal repository | External/company authorization; currently prohibited by the Owner constraint. |

## 10. WS5.5, DVL, TD-14, and Finding impact

A viable approved Model B/D protocol could be recorded under a new successor
such as `WS5.5-S-WS6A-002` without repeating WS5.1–WS5.4 for
`CE-P4-WS5-CONSUMER-001`, provided that Consumer remains exactly quarantined,
the successor freezes all missing package-arm controls, and no breach occurred.
The distinct comparative control Consumer still needs its own WS5 reservation
and freshness PASS before the control arm can be valid.

The inability to access the real Project on LNX-01 is an execution-location and
current-implementation-interface constraint, not evidence that I10 conflicts
with external-source architecture. It does not change DVL-P4-001, trigger
TD-14, or create a Finding by itself. TD-14 concerns material deterministic
discovery deficiency, not lack of cross-environment import/export. A new import
adapter, data-transfer mechanism, or scope change would require separate Owner
review; no such change is selected here.

## Recommended model and exact next Owner action

**Recommended conditional model:** Model B plus Model D. Run the existing
read-only v0.1 local Git/Markdown capability in the authorized work environment
against the authorized local Company AI Roadmap Source boundary; retain raw and
full work-derived evidence there; freeze/hash the permitted package/rendering;
then have the Owner deliver only the exact task and authorized rendering
verbatim directly to the package-arm Consumer. Retain only authorized,
non-sensitive lineage in the Context Engine repository.

**Exact next Owner action:** obtain and record the applicable external/company
authorization for this execution location, local Source observation, Consumer
disclosure, control-baseline access, and external evidence retention; then make
a separate Context Engine Project Owner decision whether to authorize Model B/D
as `WS5.5-S-WS6A-002`. Until both are in place, stop: do not access work
material, create a control Consumer, alter the package-arm Consumer, or execute
WS5.5/WS6A.
