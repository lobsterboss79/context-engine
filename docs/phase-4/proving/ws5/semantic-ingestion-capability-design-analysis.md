# Semantic-Ingestion Capability Design Analysis

**Status:** **DESIGN COMPLETE — PROJECT OWNER IMPLEMENTATION DECISION REQUIRED**

## Minimum capability and recommendation

The minimum production capability is governed source-owner semantic records
associated with existing Markdown Artifacts. Context Engine would observe those
versioned records, validate deterministic provenance bindings, and emit existing
Claim and RepresentedInformation inputs to the unchanged downstream pipeline.

This is not generic Markdown understanding, model extraction, or proving-only
instrumentation. It is a durable project documentation capability. It is the
smallest architecture-compatible design because the frozen eight prose files
have no existing machine-readable assertions. A generic deterministic prose
extractor cannot reliably establish atomic meaning, authority, or supersession;
model extraction is materially broader and nondeterministic.

This design cannot make the current frozen revision runnable. A later Owner
decision would need to authorize a new eligible project revision/scope with
real maintained semantic records. `WS5.5-S-WS6A-002` remains preserved.

## Required boundary and approach comparison

| Must have for I10 | Future useful | Out of scope |
| --- | --- | --- |
| Consume bounded semantic records linked to observed Markdown and validate atomic Claims, provenance, state, authority basis, uncertainty, limitations, and instruction/data separation. | Consolidation, authoring aids, richer relationships, semantic diff. | Embeddings/vector index, autonomous authoring, general AI document understanding, crawling. |
| Bind each Claim to source revision/hash and exact block/location; emit existing Claim/RepresentedInformation. | Cache/index optimization. | Inferred authority, executable Source content, manual Consumer rendering. |

| Approach | Assessment |
| --- | --- |
| Deterministic prose rules | Deterministic but cannot reliably resolve prose meaning, authority, history, or negation in the selected documents. Insufficient. |
| Governed annotations/sidecars | Explicit atomic assertions and assessments with exact source bindings; deterministic validation and low hallucination risk. Recommended. |
| Model-assisted extraction | Can propose meaning but cannot deterministically validate truth/authority; introduces model/version/retry/drift risk. Not necessary. |
| Hybrid | Annotation baseline plus optional future proposal-only model aid. Future only. |

Full I10 does not require fully automatic arbitrary Markdown-to-Claim
extraction. It requires a production-supported semantic-input process that does
not need task-specific Owner/controller reconstruction at proving time.
Source-owner records can meet that bar only if they are normally maintained,
governed/versioned independently of proving, not backfilled as an answer key.

## Contract, provenance, authority, and safety

Existing Claim schema is sufficient: `identity`, `assertion_reference`, and
`provenance`. No schema change is required if ingestion population rules use
existing companion models for Classification, Authority, GovernanceState,
Currentness, Conflict, and Uncertainty.

Each Claim requires Project; Source/scope; artifact path/version; frozen Git
revision and source hash; parser version/configuration, block ordinal and line
range; observation identity/time/local-only limits; Claim identity/version/hash;
authoring-process and transformation state; upstream provenance; and assessment
bases/limitations. Changed Artifact or parser result requires a new observation
and semantic-record version.

Authority comes from Source registration/configuration and explicit
source-grounded assessment records, never from prose or annotation assertion.
Historical, reference, superseded, unresolved, and unavailable information stays
explicitly qualified. Semantic records and Markdown remain inert evidence: the
ingester rejects executable directives/tool requests/authority changes in source
content, and failures produce invalid or unavailable evidence rather than Claims.

Model assistance is unnecessary. If ever considered, it must be proposal-only:
frozen input, fixed schema, no tools/repository/execution authority, raw-output
preservation, model/version recording, deterministic span/schema validation,
unsupported-Claim rejection, bounded retry, and indeterminate failure. It may
not establish Authority, Governance, currentness, or final acceptance.

## Day Trading System fit and downstream seam

The eight frozen files contain roughly 25-45 potential atomic facts covering
identity/purpose, phase/history, PDR-016 authorization/non-authority,
governance/research rules, provenance, limitations, and gaps. Difficult cases
are mixed historical/current state, scoped authorization, local-only Git facts,
absence of Phase 3 implementation, and unavailable state. Semantic records
could represent them faithfully; prose rules cannot safely resolve them.

The new capability stops at the existing seam:

```text
semantic record -> Claim / RepresentedInformation / DiscoveryEvidence
-> existing discovery -> selection -> sufficiency -> package -> WS9 rendering
```

Downstream modules remain unchanged. No manual package/rendering is permitted.

## Lifecycle, change surface, and validation

Semantic records and validated results must be versioned and persisted as
append-only, Project-scoped historical evidence linked to observed Artifact and
Provenance. Ephemeral per-run Claims are insufficient. Reuse the existing SQLite
evidence pattern; no large database subsystem or cache is required.

Estimated size is **MEDIUM**: a semantic-ingestion module/port, Markdown
handoff, explicit record registration/configuration, SQLite migration/store,
controlled application input, tests, and documentation. This is not a small
parser patch because provenance, persistence, security, and failure behavior
are material.

It is a new v0.1 capability completing an approved semantic seam and material
Phase 4 proving remediation. H3/Project Owner authorization is required.
Additive governance can preserve closed phases; model aid or a changed semantic
schema would require architecture reapproval.

Required validation: semantic-record acceptance/rejection; exact
revision/hash/location and source-mutation provenance; authority/governance,
current/historical/supersession, limitation/uncertainty/conflict, scope/secret,
and instruction-as-data tests; invalid/unavailable fail-closed tests; end-to-end
ingestion through unchanged downstream pipeline and WS9; full regressions; then
a read-only Day Trading System test at a newly governed semantic-record revision
without Consumer exposure.

## Proving lineage, alternatives, and Owner decision

WS5.5, successor 001, and successor 002 remain immutable. If authorized,
implemented, validated, and re-frozen at an eligible later external-project
revision/scope, the next protocol should be `WS5.5-S-WS6A-003`; do not create it
now.

Instrumentation proves downstream processing only and was rejected for full
I10. Amendment changes the objective; deferral retains rigor but proves nothing
more. The recommended deterministic source-owner semantic-record seam is
proportionate: it adds governed ingestion at the existing Claim boundary, no AI
dependency or general document-understanding system, and preserves the stronger
real-project objective.

The Owner must decide whether to authorize this medium-sized production
semantic-record/sidecar ingestion capability, including provenance, persistence,
security, validation, and a later external-project revision/scope decision.
That is separate from implementation, record authoring, successor creation,
Consumer work, and WS6A.

`CE-P4-WS5-CONSUMER-001` remains **RESERVED / PREFLIGHTED FRESH / QUARANTINED
/ ZERO MESSAGES / UNEXPOSED**. No control Consumer exists.
