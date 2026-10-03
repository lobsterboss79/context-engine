# WS6A Semantic Package / Consumer-Rendering Gap Investigation

**Status:** **INVESTIGATION COMPLETE — PROJECT OWNER DISPOSITION REQUIRED**

## Conclusion

The condition is **expected v0.1 observation/rendering behavior exposed by a
proving-protocol incompatibility with an unimplemented semantic-ingestion
capability**. It is not a configuration omission or demonstrated renderer
defect. Workstream 5 deliberately preserves Markdown as inert Artifact/block
evidence and expressly excludes Claim extraction; Workstream 9 deliberately
renders an already-constructed logical package and does not create semantics.

The frozen task requires governed semantic facts. The protocol incorrectly
assumed that arbitrary Markdown observation would directly supply those facts
to Context Items and the Consumer. It does not. This is **SEMANTICS NEVER
INGESTED**, not semantics ingested and later lost.

## Complete implemented path

| Boundary | Input -> output | Retained | Not represented/carried | Requirement and implementation |
| --- | --- | --- | --- | --- |
| Source observation | relative UTF-8 Markdown -> `MarkdownArtifactObservation` | original Markdown, path, read/size/encoding limits | Claim, authority, governance, relevance | Phase 2 C10; `application.representation.observe_markdown_artifact` |
| Git observation | authorized `RegisteredSource` -> `GitObservation` | local HEAD/branch/worktree/history, provenance, local-only limits | document assertions; remote/shared/current truth | Phase 2 C6–C9; `adapters.git_source.LocalGitSourceAdapter.observe` |
| Transformation | original Markdown -> `MarkdownTransformation` | original text; inert blocks/content, structure, lines, parser version/configuration | semantic assertion/Claim identity or assessments | Phase 3 WS5; `transform_markdown` |
| Representation | transformation -> `RepresentedInformation` | artifact/version/observation Provenance, block location, identities, limitations | `MarkdownBlock.content`, assertion text, Claim | Phase 2 D6–D7; `represent_markdown_blocks` |
| Discovery | explicit `DiscoveryEvidence` -> `CandidateContext` | represented reference; explicit metadata, relationships, authority, governance, currentness, conflicts, limits | `DiscoveryEvidence.text` is only a literal-search input and is not retained | Phase 2 E7; WS6 `discover` |
| Applicability/selection | Candidate + explicit inputs -> decision / `ContextItem` | existing representation and supplied governed assessments, selection basis, role | source-text interpretation or new semantic facts | Phase 2 E8–E12; WS7 `decision_pipeline` / `ContextItem.select` |
| Package | selected items + explicit ASU/deficiencies/coherence -> `ContextPackage` | items, manifest, sufficiency, coherence, limits | semantic enrichment or repair of missing Required context | Phase 2 F; WS8 `package_construction` |
| Rendering | `ContextPackage` + `ConsumerContract` -> `RenderingResult` | request/item IDs, selection, governance/currentness/authority fields, Provenance, conflicts, limits, manifest, sufficiency/coherence | raw Markdown, block content, assertion text, unrepresented facts | Phase 2 F8–F10; WS9 `render_package` |

`run_governed_render` only composes downstream services. Its inputs already
require `DiscoveryEvidence`, applicability/role/sufficiency inputs, and a
Consumer contract; it neither invokes a Source Adapter nor produces Markdown
Claims.

## Observation, assertion model, and first non-ingestion point

The frozen eight Day Trading System Sources were observed read-only. Their
ordinary assertions exist in source text, and the implementation preserves
that text in `MarkdownArtifactObservation.original_markdown` and
`MarkdownTransformation.original_markdown`. The first relevant non-ingestion
point is `represent_markdown_blocks`, whose output is:

```text
RepresentedInformation(identity, artifact, provenance, classifications, uncertainty)
```

It has no content/assertion field and creates no `Claim`. Thus no semantic
fact such as the Phase 2/Phase 3 state, PDR-016 boundary, current/historical
distinction, or known gap enters discovery as retained semantic information,
becomes a Context Item, enters the package, or reaches WS9.

The semantic kernel does define
`Claim(identity, assertion_reference, provenance)`. Phase 2 D6 defines a
Claim as a governed-granularity semantic assertion; D7 makes Context Items
task-relative selected information. But neither core model nor application
contains a Markdown-Claim extractor, Claim registration/ingestion API, Claim
persistence/rehydration path, or a transformation producing authority,
governance/currentness, applicability, and uncertainty assessments from
arbitrary Markdown. The controlled tests construct semantic objects as
fixture/controller inputs; they do not implement a producer for external
Markdown.

Arbitrary Markdown is therefore not expected to become assertions
automatically. A Claim would need a separately governed semantic-record or
ingestion mechanism. No such production mechanism is implemented or frozen
for this proving run.

## Approved requirements and architecture

| Record | Governing meaning | Result here |
| --- | --- | --- |
| Phase 1 CE-FR-006, 013, 021–026 | Discover information, distinguish information state, package selected context with provenance, and render without semantic loss. | A package must contain semantic items before rendering; identifiers cannot substitute for Required facts. |
| Phase 1 CE-FR-017–020, 034–037 | No false sufficiency; preserve Required governing context; authorize disclosure; Source content is not instruction. | Missing semantic facts cannot be hidden by a Sufficient label or raw ungoverned source disclosure. |
| Phase 1 v0.1 Source boundary | Markdown retrieves governed Artifact evidence/provenance and relevant native information. | Does not require automatic semantic extraction or raw-Source Consumer delivery. |
| Phase 1 acceptance interpretations | Meaningful continuation requires a generated package to establish state, boundaries, uncertainty, and next work without Owner reconstruction. | The frozen task legitimately requires semantic content. |
| Phase 2 C6–C10 | Adapters observe native evidence, not final Claims/Context Items; C10 preserves Markdown for downstream Claim identification. | Adapter is not the semantic producer. |
| Phase 2 D6–D7 and E7 | Claim/Context Item logical models; represented information -> Candidate -> selection. | A semantic producer must precede discovery; discovery cannot manufacture it. |
| Phase 2 F8–F10 | Rendering faithfully presents a logical package. | It expects semantic Context Items already to exist; it is not a summarizer/interpreter. |

The architecture selects neither adapter extraction, Consumer-side Source
interpretation, nor automatic arbitrary-Markdown semantics. It permits a
separately governed semantic producer before Domain E/F, but did not select
its technology or mechanism.

## Phase 3 and WS9 comparison

- WS5 implemented local Git/Markdown observation, original-text preservation,
  inert structural representation, and provenance. Its record explicitly says
  **no Claim creation/extraction, discovery, Candidate Context, selection,
  package construction, rendering, or Consumer action**.
- WS6 consumes already represented evidence; WS7 consumes explicit governed
  inputs; WS8 cannot repair missing Required context.
- WS9 accepts an **already-constructed** `ContextPackage`, faithfully renders
  its package fields, and expressly does not discover, select, create
  authority/currentness, or execute/interpret Source content.

Therefore the Phase 3 closure claims are accurate within their approved
boundaries. They never claimed arbitrary Markdown-to-Claim ingestion or an
external-project continuation package. The earlier proof fixtures validated
explicitly constructed semantic Context Items, not this missing producer.

## Requirement / implementation comparison

| Requirement | Architecture | Phase 3 claim | Proving observation | Classification |
| --- | --- | --- | --- | --- |
| Meaningful continuation/I10 requires state, authority, gaps, history, next boundary in generated context. | Semantics precede selection/package/rendering. | I10 execution not claimed. | Frozen task needs facts; eight Sources provide only raw evidence to the app. | Unmet proving prerequisite. |
| Markdown support preserves Artifact evidence/provenance. | C10 preserves content/structure for downstream Claim identification. | WS5 explicitly implements inert evidence, not Claims. | All eight files observed correctly. | Implemented as approved. |
| Claims/Context Items preserve selected semantics/provenance. | D6/D7 provide logical model. | WS2 implements model, not producer. | No arbitrary-Markdown Claim producer. | Approved logical capability, unimplemented ingestion behavior. |
| Discovery through rendering retains governed inputs. | E/F/WS9 downstream of semantic inputs. | WS6–9 use explicit inputs. | Metadata flows; assertions do not. | Correct downstream boundary; protocol cannot supply inputs. |
| Rendering preserves package meaning. | F10 faithful rendering. | WS9 canonical payload. | No assertion text was ever packaged. | No demonstrated renderer defect. |

## Proving validity and governance impact

The current proving protocol is invalid for Consumer exposure because no
faithful semantic package/rendering can be frozen. `WS5.5-S-WS6A-002` correctly
stopped before exposure.

This is an **H3 stop and Owner-decision boundary**: any resolution changes the
semantic Source-to-Consumer contract, proving protocol, implementation scope,
or effective proving claim. A new formal Finding is not unambiguously required
by investigation alone. No nonconformance to the expressly narrow WS5/WS9
implementation boundary is established; whether this is an implementation
obligation, authorized proving instrumentation, or a scope/claim change is the
material Owner disposition. This record preserves the evidence and creates no
Finding/disposition.

`DVL-P4-001` is unaffected. `TD-14` remains **TRIGGER NOT MET / CLOSED / NOT
REOPENED**: this is not deterministic discovery failing to find already
ingested information; it is absence of semantic ingestion. It does not support
an AI/vector/semantic-search conclusion.

Gate 4B remains **PASS — PROJECT OWNER APPROVED**. Its controlled validation
evidence correctly established the tested observation/representation boundary
and rendering of explicitly constructed semantic fixtures. This result exposes
a new external-project proving prerequisite, not a contradiction of that
narrower Gate 4B claim. No Gate reopening occurs.

## Resolution classes requiring Owner authorization

| Class | Viability and effect | Source/tests | Architecture/proving effect |
| --- | --- | --- | --- |
| Use existing semantic-input mechanism | Not presently available as a governed production mechanism; core objects/test inputs are not one. | None only if such an approved mechanism is identified. | Cannot be assumed. |
| Governed proving instrumentation | Bounded semantic records from the fixed eight Sources, with explicit Claim/provenance/authority/currentness/limits. | Potentially none. | Material protocol/semantic-input decision; must not become a manual Consumer rendering. |
| Implement semantic ingestion | Bounded Source-evidence-to-governed-Claim producer. | Source and tests required. | Material semantic/Source/Consumer contract work; Owner must decide architecture compatibility/scope. |
| Repair propagation | Only if later evidence finds a real producer whose data is discarded. Current evidence does not. | Evidence-dependent. | Not a supported current defect hypothesis. |
| Amend proving claim/task | Make metadata-only output sufficient. | Possibly none. | Materially changes/weakens I10 unless separately approved equivalent. |
| Defer proving | Preserve this stop. | None. | Maintains rigor; WS5 remains incomplete. |

## Exact Owner decision and preserved state

The Project Owner must choose whether to authorize a governed semantic-input
path for the frozen run (and whether it is bounded proving instrumentation or
product remediation), amend/defer the proving claim, or make another governed
disposition. The decision must preserve the selected revision, 8-Source scope,
task, P1–P8 matrix, provenance/authority/currentness/uncertainty distinctions,
independent evaluation, and Consumer quarantine. Raw Markdown or controller
prose cannot be an ungoverned Context Package substitute.

`WS5.5-S-WS6A-002` remains **PARTIALLY FROZEN / INDETERMINATE — STOP AND
PRESERVE**; overall WS5 remains incomplete; WS6A/WS6B remain unauthorized;
Gate 4C remains not approved; production readiness remains not established.
`CE-P4-WS5-CONSUMER-001` remains **RESERVED / PREFLIGHTED FRESH / QUARANTINED
/ ZERO MESSAGES / UNEXPOSED**. No control Consumer exists.
