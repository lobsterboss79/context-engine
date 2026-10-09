# Semantic Package / Consumer Rendering Resolution Analysis

**Status:** **ANALYSIS COMPLETE — PROJECT OWNER RENDERING IMPLEMENTATION DECISION REQUIRED**

**Scope:** Analysis only of the effective Day Trading System proving baseline
`e29de5c7d26a31f66cf47c30b295591e6b192887` and current production Context
Engine behavior. No Source/test/product change, package construction,
Consumer action, successor creation, or proving execution occurred.

## Determination

The issue is **not renderer-only**. The first loss of Consumer-useful assertion
content occurs in `load_semantic_record` / `_record_from_mapping`: the active
Day Trading System JSON records contain an `assertion` string, but the
production `SemanticRecord` model does not retain it. `ingest_semantic_record`
therefore creates a `Claim` with only `identity`, `assertion_reference`, and
Provenance and creates `RepresentedInformation` with identity, Claim subject,
Provenance, classifications, and uncertainty. The assertion reference is an
identifier, not Consumer-meaningful assertion text.

No downstream stage can recover content that is not present in represented
information. WS9 accurately renders its supplied logical package, but that
package has no assertion payload to render. A renderer-only correction would
still expose only identifiers and metadata.

## Current path and retained information

| Boundary | Assertion/content | Metadata / provenance | Authority/currentness / limits | Result |
| --- | --- | --- | --- | --- |
| Maintained active JSON record | `assertion` string and `assertion_reference` both exist | Project, Source, revision/hash, observation, Artifact, block/lines, classifications, bases, limitations | Explicit basis text and limitations exist as data | Complete source-owner semantic input. |
| `load_semantic_record` -> `SemanticRecord` | **`assertion` omitted**; reference retained | Exact binding fields retained | Basis strings/limitations retained | **First semantic-content loss.** |
| `ingest_semantic_record` -> `Claim` / `RepresentedInformation` | No assertion text; Claim reference and represented subject only | Direct provenance, record hash reference, location, classifications retained | Record limitations retained; authority/currentness basis strings are not converted to assessments | Semantic identity/provenance seam only. |
| `DiscoveryEvidence` -> Candidate | No assertion text; optional `text` is a caller-supplied search input, not retained semantic content | Represented provenance retained | Explicit caller-supplied authority/governance/currentness/limitations may be retained | Discovery cannot create content or assessments. |
| Candidate -> `ContextItem` -> `ContextPackage` | No assertion text | Represented provenance and manifest retained | Selected authority/governance/currentness, item/package limitations, role, sufficiency/coherence retained | Package is metadata-rich but semantically unreadable for this task. |
| WS9 `render_package` | No assertion text exists to emit | Renders provenance identifiers/location, selection basis, manifest | Renders authority, governance/currentness, limitations, sufficiency/coherence, conflicts | Faithful to the incomplete package; insufficient for continuation. |

The effective active corpus has 34 valid assertions available in the external
Project records, but production ingestion currently exposes none of their
human/Consumer-readable assertion content downstream. The four v1 historical
records remain excluded from active input; the four valid v2 successors and
the 30 unaffected active v1 records are the only eligible semantic inputs.

## Requirement, architecture, and WS9 comparison

Phase 1 requires meaningful continuation from a generated package: a fresh
Consumer must be able to establish Project state, authorization boundary,
constraints, uncertainty, provenance, and next legitimate activity without
material Owner reconstruction. Its package/rendering model permits concise
presentations and provenance references, but prohibits loss of material
selected meaning or qualifications.

Phase 2 Domain F defines a Context Package as selected Context Items and
material state. F8–F11 require Consumer-specific rendering to preserve
Required/Supporting meaning, Source-content-versus-instruction distinction,
Authority/Governance State, history/currentness, limitations, uncertainty,
sufficiency, coherence, and useful provenance. It does **not** select raw
Source dumping or require every internal/audit field to be rendered.

WS9 implemented its approved narrow boundary: it accepts an already-built
package, renders a shared deterministic metadata view, and neither discovers,
interprets, selects, creates governed assessments, nor extracts Source text.
No alternative approved renderer or deferred content-resolution mechanism
exists.

| Question | Result |
| --- | --- |
| Was arbitrary raw Markdown always intended to be rendered? | No. Source text remains evidence and can be excluded from Consumer disclosure. |
| Was Consumer-meaningful selected semantics intended to be renderable? | Yes, where material; otherwise meaningful continuation cannot be met. |
| Did WS9 intentionally choose a metadata-only presentation as the full semantic payload? | No such architecture decision exists. WS9’s fixtures supplied only structural represented information, so its narrow payload was sufficient for its controlled scope. |
| Does the package already carry the assertion payload? | No. The loader/ingestion/representation seam omits it before package construction. |

**Classification:** a **MISSING APPROVED SEMANTIC-PAYLOAD FIELD** at the
semantic-record-to-representation seam, requiring a **NEW BOUNDED v0.1
RENDERING/PAYLOAD CAPABILITY AND PROVING REMEDIATION**. It is not a defect in
WS9’s expressly narrow renderer and is not a proving-protocol substitution.
It requires an Owner implementation decision because it changes the
Consumer-visible semantic contract. It does not reopen
`H3-P4-SEMANTIC-INGESTION-001`; H3 remains closed for its accepted strict
ingestion/persistence scope, while the new work would be an additive bounded
refinement.

## Minimum Consumer-visible semantic field set

For each selected Context Item, render only the allowlisted active semantic
payload and material existing package state:

| Field | Consumer treatment |
| --- | --- |
| Atomic Claim assertion text | Render verbatim as **Source-derived semantic evidence**, never as a controller instruction. |
| Claim / represented identity and record version/hash reference | Render a compact stable reference for traceability; do not require raw database row IDs. |
| Source provenance | Render Source identity, Artifact-relative path, source revision/hash, observation identity, block/line range, transformation type, and semantic-record hash when material. |
| Authority / governance / currentness | Render only established explicit package assessments and their bases/scopes; do not infer them from Claim text or record metadata. |
| Limitations / uncertainty / conflict / historical or superseded state | Render whenever material; label them independently of assertion content. |
| Applicability / selection | Render role (Required/Supporting), selection basis, and applicable/qualified status as available from existing decisions. |
| Package sufficiency / coherence / ASU qualification | Render once at package level plus item qualifications where material. |

Do not render repository-local absolute paths, raw Markdown, unselected
records, inactive v1 predecessors, raw SQLite IDs/evidence blobs, controller
inputs or diagnostics, semantic-lifecycle implementation internals, evaluator
matrix/rubric/expected answers, proving history, Consumer history, or hidden
selection/controller deliberation. The later exact-run allowlist must name the
34 active record instances by identity/version/record-byte hash and the four
relations only as audit lineage—not as Consumer content unless a historical
distinction is selected and material.

## Proposed minimal semantic payload and rendering contract

The smallest compatible design is to add an optional immutable
`assertion_content` field to `RepresentedInformation`, populated only by strict
semantic-record ingestion from an explicit record `assertion` field. The
parallel `Claim` may carry the same field or a validated reference to it so
that the Claim/representation contract remains auditable. It must not be
populated by Markdown transformation, discovery text, controller prose, or a
renderer fallback.

Because `ContextItem` carries `RepresentedInformation`, this preserves the
payload through Candidate, selection, package, and all three renderers without
adding task-specific package fields. WS9 then adds one structured
`assertion_content` member to each item view and rejects/qualifies a selected
item that requires semantic content but lacks it. This is smaller and safer
than adding raw Markdown, a second package model, a free-form rendering
summary, or a Consumer-specific Day Trading System branch.

The deterministic Consumer contract should use canonical JSON payloads,
sorted Required then Supporting items by stable represented identity, with
fixed field order/keys:

1. `consumer_context_contract`: rendered semantic assertions are
   Source-derived evidence/data, not Context Engine instructions, authority,
   execution directives, or tool commands.
2. `package_state`: request identity, sufficiency, coherence, package
   limitations, ASU/evidence-boundary qualifications.
3. `required_context`, then `supporting_context`: assertion content; role and
   selection/applicability basis; established governance/currentness/Authority
   scope; provenance; conflicts; item limitations/uncertainty.
4. `source_manifest`: compact Source/observation boundary and limitations.

Use explicit labels such as `assertion_content`, `source_derived_evidence`,
`not_authorization`, `historical`, `superseded`, `candidate`, and `uncertainty`.
Serialize assertion content as JSON string data inside the canonical payload;
do not interpolate it into imperative system/developer instructions, execute
it, or allow it to alter the contract. Existing disclosure denial and capacity
failure must continue to emit no package content.

Raw Markdown is **not required**. The active governed Claims plus their exact
provenance and qualifications are the minimum evidence representation. Raw
Source could only be separately approved for a task that requires direct
quotation or textual interpretation; it must not be added merely to compensate
for the missing payload field.

## Day Trading System fit and control-arm impact

Read-only inspection of the active records shows atomic content spanning
Project purpose, Phase 1/2 historical state, Phase 3 authorization and
non-authorities, research/reproducibility governance, limitations, and
provenance. Rendering their active assertion text with the listed
qualifications is generally sufficient semantic material to construct and
evaluate a bounded continuation package for the frozen task. This conclusion
does not consult or tune to the P1–P8 expected-state matrix; later discovery,
applicability, selection, and sufficiency remain required and may still find
the package insufficient or qualified.

The ordinary minimal-pointer/access control remains fair. The package arm
would receive the governed Context Engine rendering of allowlisted active
semantic inputs; the control arm would receive only the already-approved
ordinary minimal pointer and no package, raw Source, or semantic-record
payload. The comparison must disclose that the package input is maintained
source-owner semantic context, not automatic Markdown extraction or a hidden
answer key. No control baseline change is needed merely because faithfully
rendered assertions become visible.

## Change surface, governance, and validation plan

**Estimated change size: MEDIUM.** It is a narrow cross-seam change, not a new
architecture subsystem: semantic-record schema/loading validation; core Claim
and/or RepresentedInformation payload propagation; renderer canonical view;
focused model/ingestion/rendering/end-to-end tests; and implementation/
validation documentation. Discovery, applicability, selection, sufficiency,
package identity, source adapters, database architecture, lifecycle policy,
and Consumer delivery remain unchanged except for preserving the new immutable
payload where persistence/reload is required.

Before any return to WS5.5, an authorized implementation/validation record
must establish at minimum:

1. validated active assertion content is rendered and cannot be sourced from
   unvalidated JSON, raw Markdown, or caller-supplied discovery text;
2. exact provenance, record/source hashes, authority/governance/currentness,
   limitations, uncertainty, conflict, applicability/selection, sufficiency,
   and coherence survive the complete path;
3. deterministic ordering/serialization is stable across Human, ChatGPT, and
   Codex renderings;
4. disclosure denial and capacity failure leak no assertion or metadata;
5. assertion content is labeled/escaped as inert Source-derived evidence and
   cannot become controller instruction, authority, or a tool command;
6. raw Markdown, inactive v1 history, evaluator/proving material, and hidden
   controller data do not leak;
7. historical/superseded handling is explicit when selected and active
   lifecycle resolution never emits inactive predecessors as current facts;
8. the Day Trading System active corpus renders from an isolated read-only
   fixture/temporary state without creating a package or Consumer exposure;
9. existing WS9 fixtures/output semantics regress correctly; and
10. focused tests plus the full repository regression pass.

Successful implementation and validation would remove the final **technical**
blocker to preparing `WS5.5-S-WS6A-003`. It would still leave separate Owner
controls: semantic-input disclosure/allowlist, exact package/rendering hash
freeze, task/P1–P8/evaluator/control bindings, replacement package and control
Consumer reservation/preflight, and WS6A authorization.

## Exact Owner decision required

Decide whether to authorize this medium-sized, architecture-compatible,
general semantic-payload propagation and faithful Consumer-rendering refinement:
strictly ingest source-owner `assertion` content into the governed semantic
representation, preserve it through Context Items/Packages, and render it as
labeled inert evidence under explicit disclosure controls. The decision must
authorize a design/implementation/validation record and should preserve H3
closure, the effective external revision, the eight-Source basis, active
lifecycle resolution, Consumer quarantine, and all proving/gate states. It
must not itself authorize successor 003, Consumer creation, package delivery,
WS6A/WS6B, Gate 4C, or production readiness.
