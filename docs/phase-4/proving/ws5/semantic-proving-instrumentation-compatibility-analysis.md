# Semantic Proving-Instrumentation Compatibility Analysis

**Status:** **ANALYSIS COMPLETE — PROJECT OWNER SEMANTIC-INPUT DECISION REQUIRED**

## Determination

Explicit, Source-grounded Claims are architecture-compatible inputs to the
existing downstream v0.1 pipeline. They are not an implemented arbitrary
Markdown ingestion capability.

They could prove downstream discovery, selection, sufficiency, package, and
rendering behavior given valid governed semantic inputs. They cannot prove that
Context Engine automatically derives those inputs from the frozen Markdown
without material human reconstruction. They are not an unqualified substitute
for the full I10 Source-to-Consumer claim.

## Claim contract and authoring seam

Phase 1 Item 12 and Phase 2 D6 define a Claim as a governed-granularity
semantic assertion, distinct from Artifact, Authority, Governance State,
currentness, and task selection. The model is
`Claim(identity, assertion_reference, provenance)`. Claims can be direct,
transformed, summarized, inferred, or proposed, with uncertainty retained.

No production Claim-creation service is implemented. The core model permits
explicit construction, and Phase 3 fixtures construct semantic objects through
model/application APIs. That is a supported input shape, not a production
Markdown-to-Claim interface or standing authority to author project semantics.

| Category | Result |
| --- | --- |
| Supported input | Explicit Claim/RepresentedInformation with provenance and separately supplied assessments can enter downstream stages. |
| Test fixture | Hand-authored semantic objects validate bounded components; they are not external-project proof by themselves. |
| Proving instrumentation | Not approved yet; it needs an Owner-governed frozen Source-to-Claim procedure. |
| Product-generated semantics | Not implemented for arbitrary Markdown. |

The architecture permits a Source owner or Project Owner through governed
semantic records, an approved ingestion/import/preprocessing process, or an
expressly authorized proving-instrumentation process to author Claims. A
controller, fixture, or AI cannot create Authority by constructing a model
object; Provenance explains authorship but does not establish Authority.

## I10 boundary and Phase 1 requirement

Phase 0 requires reading supported Sources, representing relevant context
without hard-coding project semantics, generating a package, preserving
provenance, and enabling fresh-Consumer continuation with substantially less
manual reconstruction. Phase 1 requires Source observation/provenance,
semantic representation, discovery, package construction, and useful Consumer
context. It does not expressly require automatic arbitrary Markdown-to-Claim
extraction; Claim technology/extraction was never selected.

That absence does not make human reconstruction invisible. The acceptance
interpretation requires Consumer performance from a generated package without
the Owner supplying material prior project state. If the Owner/controller
authors that semantic state solely to form the package, the following boundary
controls:

| Proven | Not proven |
| --- | --- |
| Downstream governed processing and Consumer usefulness given valid, Source-grounded semantic inputs. | Automatic Markdown extraction; absence of material human reconstruction; full unqualified I10 external Source-to-Consumer capability. |

## Phase 2 seam and Phase 3 precedent

Phase 2 C6-C10 makes adapters observation boundaries; C10 preserves Markdown
for downstream Claim identification. D6/D7 model Claims and Context Items; E7
starts from already represented information; F8-F10 render an already built
package. The architecture selects neither adapter extraction, Consumer-side
Source interpretation, nor automatic arbitrary-Markdown semantics. It leaves
the producer unselected:

```text
governed Claim / represented semantic information
-> DiscoveryEvidence -> CandidateContext -> ContextItem
-> ContextPackage -> Consumer rendering
```

WS5 preserves original Markdown and inert structure but expressly excludes
Claim extraction. WS6 consumes already represented evidence and caller-supplied
literal text; that text is search input, not retained semantic content. WS7/8
consume explicit inputs; WS9 renders an already constructed package. Existing
WS3/WS6-WS9 fixtures hand-author semantic identities and assessments. That is
a valid component-test technique, not precedent that fixtures satisfy a real
external-project proving claim automatically.

## Circularity, provenance, and eight-Source feasibility

The frozen eight Sources plausibly support an objective bounded set of roughly
**25-45 atomic Claims**: Project purpose; phase/history; PDR-016 authority and
non-authority; governance/research rules; reproducibility/provenance; known
gaps and unavailable state. This is a feasibility estimate, not Claim text or
authorization to create Claims. It cannot infer unlisted files, Phase 3
implementation, provider state, or trading authority.

Each Claim needs a Project, Source/scope, artifact path, frozen revision and
SHA-256, artifact version, block/line location, observation identity/time and
local-only limitation, Claim identity/version/hash, authoring-process and
transformation state, upstream provenance, asserted assessment basis, and
uncertainty/conflict/supersession/limitations. Applicability and
Required/Supporting remain later task inputs.

Necessary anti-circularity controls are:

1. Atomic Source-grounded facts only; no task-answer prose, continuation brief,
   recommendation, or task-specific synthesis.
2. Exact provenance and a frozen Claim manifest before discovery/package work.
3. Claim authors cannot access P1-P8 expected state, evaluator rubric, control
   or Consumer output, or expected answer.
4. Claims cannot self-create Authority/Governance/currentness; every assessment
   needs an independent Source-grounded basis and limitation.
5. Discovery, selection, sufficiency, rendering, raw-output preservation, and
   independent evaluation remain unchanged.

These controls can make a downstream exercise non-circular. They cannot erase
human semantic authoring, so do not preserve the unlimited I10 claim.

## Pipeline compatibility and control fairness

Existing code can technically consume explicit semantic objects without product
source/test changes:

```text
Claim -> RepresentedInformation/DiscoveryEvidence -> Candidate
-> explicit applicability -> ContextItem -> sufficiency -> ContextPackage
-> render_package
```

Using fixture-style APIs in proving needs separate Owner authorization and a
durable proving-only controller/manifest; they are not a normal ingestion path.
No manual Consumer rendering is legitimate.

The ordinary minimal-pointer/access control is fair only for the narrowed
comparison: same task, package arm receives the Context Engine package, control
does not receive Claims/package, and neither arm is denied an ordinary access
route it actually has. Reconstruction evidence must disclose human-authored
instrumentation. It cannot establish that Context Engine eliminated authoring
effort.

## Permissible claim, gap treatment, and decision matrix

If an instrumented run succeeds, the permissible claim is:

> Context Engine transformed the frozen governed semantic input set, with
> preserved source/provenance/qualification lineage, into useful Consumer
> context for the defined continuation task with less Consumer-side
> reconstruction than the frozen ordinary control baseline.

It cannot claim automatic Markdown understanding/extraction, no human semantic
reconstruction, generic real-project ingestion, or full unqualified I10
satisfaction.

Markdown-to-Claim absence is a v0.1 capability boundary and proving limitation,
not DVL-P4-001, TD-14, or an automatic Finding. It becomes a remediation
candidate only if the Owner decides full I10 requires product ingestion.

| Option | Compatibility/evidence | Changes and risk | Owner authorization |
| --- | --- | --- | --- |
| A. Bounded instrumentation | Compatible with downstream seam; proves valid-semantic-input processing only. | No product change necessarily; human-input risk controlled but not erased. | Material semantic-input and claim-boundary decision. |
| B. Markdown -> Claim ingestion | May support full end-to-end I10 after design and validation. | Source/tests; material semantic and Source/Consumer-contract work. | H3 remediation/architecture decision. |
| C. Amend/reduce I10 | Can align claim with metadata/downstream capability. | Materially changes proving intent. | Multi-baseline Owner approval. |
| D. Defer | Fully preserves current rigor. | No additional evidence; WS5 incomplete. | Owner disposition. |

## Recommendation and required Owner decision

The architecture-consistent recommendation is **not to use Option A as a silent
replacement for full I10**. It is supportable only as a separately approved,
explicitly limited downstream proving exercise with atomicity, provenance,
anti-leakage, and fair-control controls frozen first.

The Owner must decide whether to authorize that limited proving-only Claim
manifest, require product ingestion for full I10, amend the claim, or defer.
The decision must preserve selected revision, eight-Source scope, task, P1-P8,
Consumer quarantine, and all provenance/authority/currentness qualifications.
`CE-P4-WS5-CONSUMER-001` remains **RESERVED / PREFLIGHTED FRESH / QUARANTINED
/ ZERO MESSAGES / UNEXPOSED**; no control Consumer exists.
