# Phase 2 Domain C — Source & Observation Architecture

**Phase status:** **AUTHORIZED / IN PROGRESS.**

**Domain C status:** **COMPLETE — PROJECT OWNER APPROVED — PASS.**

**Unresolved BLOCKER:** **0.**

**Unresolved MATERIAL:** **0.**

**Domain D status:** **NOT BEGUN.**

**Next activity:** **D1.**

**Implementation:** **NOT AUTHORIZED.**

## Governance record

This record durably documents the Project Owner-approved C1–C16 Source & Observation Architecture baseline. It records already-approved architecture and does not introduce new material architecture, technology, security, governance, scope, persistence, logical-representation, Source, Consumer, or implementation decisions. Domain D has not begun. Phase 3 and later phases remain **NOT AUTHORIZED**.

## C1 — Domain C requirements and constraints

| ID | Approved constraint |
| --- | --- |
| SC-01 | **Sources Remain External.** A Source is something the Context Engine observes; registration or observation does not transfer ownership or Authority to it. |
| SC-02 | **Registration Does Not Establish Authority.** Registration establishes governed eligibility for consideration, not authority, approval, currentness, relevance, completeness, or safety of Source content. |
| SC-03 | **Source Access Does Not Establish Consumer Authorization.** Domain B Requester/Consumer authorization remains controlling. |
| SC-04 | **Preserve Material Native Semantics.** Interpretation-material Source-native semantics survive observation; Git is not reduced to a folder of Markdown when Git-native state matters. |
| SC-05 | **Preserve Observation Epistemic Strength.** Local observation does not silently become verified remote, shared, governing, official, complete, or current state. |
| SC-06 | **Evidence Boundaries Are Explicit.** Observation/search results are meaningful only relative to the actually established Sources, scopes, and inspection boundaries. |
| SC-07 | **Source Failure Remains Visible.** Unavailable, inaccessible, partially inspected, unsupported, or failed observations do not silently disappear from completeness reasoning. |
| SC-08 | **Security Boundaries Survive Observation.** Project isolation, authorization, native permissions, sensitive-information handling, secret exclusion, and untrusted-content boundaries remain applicable. |
| SC-09 | **Design Generally, Implement Narrowly.** Stable boundaries support materially different future Sources; v0.1 implements only the approved local Git/Markdown Source capability. |

## C2 — Project registration

Project registration is a governed declaration establishing a Project as a recognizable Context Engine isolation/context boundary. At the logical level it must be capable of establishing Project identity, the applicable Governance Bootstrap relationship, Project scope/boundary where necessary, references needed to discover registered Sources, eligibility status for Context Engine operations, and registration/configuration Provenance.

Project registration is not the Project’s context. Project identity is distinct from a filesystem path or other locator; a locator may change without inherently creating a new Project. This architecture does not choose a physical Project-identity representation.

## C3 — Source registration, identity, Source Scope, and Project association

Registered Source information must logically support Source identity, Source type/capability, Source locator/access reference, Project association, Source Scope, and registration Provenance/state. Source identity is distinct from locator: a local path or remote URL is not automatically universal Source identity. Source Scope defines the portion governed as potentially eligible for a Project and is distinct from task-specific relevance. Source capabilities may materially differ; adapters report capabilities honestly rather than fabricating unavailable semantics. This architecture selects no physical identity format or identifier.

## C4 — Governance and authorization interaction

Registration establishes eligibility for governed observation. It grants neither Authority, authorization, trust, currentness, relevance, approval, sensitivity clearance, nor instructional status.

```text
Governance Bootstrap
    ->
Project registration/configuration
    ->
Source registration + Source Scope
    ->
authorization to inspect
    ->
Source observation
```

Adapters do not autonomously establish Project association. Discovering a possible Source does not register it; it may at most become a Candidate/Proposal under later governed behavior. Domain B authorization and security controls remain controlling.

## C5 — Applicable Source Universe and evidence boundary

The **Applicable Source Universe (ASU)** is the governed set of Sources and Source Scopes reasonably applicable to a Context Request’s Project/task evidence boundary, including known material Sources that cannot currently be inspected.

The following remain distinct:

1. **Registered Source Set:** everything governed as registered for the Project.
2. **Applicable Source Universe:** Sources/scopes reasonably applicable to the particular Context Request/evidence boundary.
3. **Observed Source Set:** Sources/scopes actually inspected during the construction attempt.

ASU is task-sensitive and is not merely the Sources successfully searched. Unavailable, inaccessible, or unauthorized material Sources may remain in it; known gaps may be represented without pretending their full identity or contents are known. Negative retrieval results remain scoped to inspected evidence. ASU does not require exhaustive discovery of every theoretically possible Source, and later sufficiency reasoning remains qualified by evidence-boundary adequacy.

## C6–C7 — General Source Adapter architecture

A **Source Adapter** is a Source-specific observation boundary.

| ID | Approved adapter requirement |
| --- | --- |
| SA-01 | **Capability Declaration.** Honestly expose relevant native capabilities—such as identity, version/history, change state, time, hierarchy, metadata, relationships, bounded enumeration, or historical retrieval—where supported. No Source must support every capability. |
| SA-02 | **Governed Scope Translation.** Receive an already-established Source and Source Scope and translate that governed scope into native inspection boundaries; do not decide the scope. |
| SA-03 | **Native Observation.** Observe native state without converting it into stronger Context Engine claims. |
| SA-04 | **Observation Provenance.** Preserve the registered Source, native identity/reference and version/state where available, applicable Source Scope, observation time/state, and material capability/limitation information. |
| SA-05 | **Explicit Limitation and Failure Reporting.** Distinguish successful, partial, unavailable, inaccessible, unsupported, malformed/uninterpretable, failed, and unknown outcomes. “I could not inspect it” never means “nothing relevant exists.” |
| SA-06 | **Preserve Material Native Semantics.** Preserve material native semantics rather than flattening them for uniformity; immaterial details need not become universal core semantics. |

Adapters do not independently determine Project identity or association, Source registration or Source Scope, Governance Bootstrap, Authority or Authority Scope, Governance State, authorization, sensitivity policy, instructional applicability, task relevance, Required/Supporting Context, Context Selection, sufficiency, Construction-State Coherence, or Consumer rendering.

Adapters may perform necessary Source-specific normalization, but it remains distinguishable from semantic interpretation/inference. They produce observation evidence rather than final governed Claims/Context Items; capability asymmetry is supported, useful native semantics are retained, and unsupported semantics are not fabricated. They enforce already-established security/authorization constraints at the observation boundary without owning security policy.

**C7 result: SOURCE ADAPTER ARCHITECTURE — PROJECT OWNER APPROVED.**

## C8 — Local Git Source behavior

For v0.1, local Git observation treats Git as overlapping repository/version evidence and working-tree evidence. Where available and material, the adapter must be capable of observing:

- repository identity evidence: repository/work-tree boundary, relevant native identity/reference information, and configured remotes where relevant;
- revision state: observed HEAD revision, symbolic branch/reference when one exists, detached-HEAD or equivalent state, and relevant commit identity;
- working-tree state: clean/dirty, staged and unstaged changes, modified tracked content, applicable in-scope untracked content, and material deletions/renames; and
- historical/version evidence: task-required relevant commit/version history, available historical Artifact states, and native relationships necessary to interpret material version evolution.

Complete history is not required for every request. Configured remotes are observations, not proof of remote currentness, reachability, Authority, synchronization, or governing status. C8 requires neither network access nor fetch; local state never silently becomes verified remote/shared/governing state. This architecture does not choose Git CLI versus library/API.

## C9 — Observed Source State

**Observed Source State** is what the Context Engine actually established about a Source during a particular observation under a particular Source Scope and observation boundary.

| ID | Epistemic distinction |
| --- | --- |
| OBS-01 | **Directly Observed:** established directly from the Source during observation. |
| OBS-02 | **Source-Reported:** exposed by the Source and observed without independently verifying any stronger proposition it might imply. |
| OBS-03 | **Derived Observation:** deterministically derived from observed native state. |
| OBS-04 | **Unestablished / Unknown:** potentially relevant property not observed, unavailable, unsupported, inaccessible, or otherwise unestablished. |

Material observations must eventually be capable of association with Source, Source Scope, observation time, relevant native state, capability/limitation information, Provenance, and success/partial/failure state. Local observation establishes neither official/shared/governing/current truth nor absence from absence of evidence. Previous/last-known observations are historical evidence, not current truth. No persistence or logical-storage representation is selected here.

## C10 — Markdown Artifact handling

For v0.1, an in-scope Markdown file is a Source-native candidate Artifact representation, subject to later Domain D identity/representation rules. Observation preserves, where material, Source-relative locator/path, observed content, associated Git/version/working-state evidence, observation Provenance, and relevant native metadata.

Headings, lists, tables, code fences, links, and front matter may be useful Source evidence, but do not independently establish Authority, Governance State, Classification, relevance, or other governed semantics. One Markdown file may commonly correspond to one Artifact in v0.1, but **Artifact = file** is not universal. A Markdown Artifact may contain multiple Claims/Context Items and must remain faithful enough for downstream Claim identification, evidence location, structure inspection, transformation, and Provenance. This architecture chooses neither raw-byte/normalized-text/AST representation nor a Markdown parser.

## C11 — Structured metadata necessity

Explicit structured metadata is introduced only for governed information that cannot be safely, reliably, or non-circularly derived from Source content or native Source state. Likely capability areas, without physical placement or format selection, are:

1. Bootstrap / Project governance metadata: Project identity, Bootstrap state/reference, governed configuration reference.
2. Source registration metadata: Source identity/type/capability expectation, locator/reference, Project association, Source Scope, registration Provenance/state.
3. Governance metadata not safely inferable from ordinary content: where later design requires it, Authority assignments/scopes, governed Relationships, explicit Governance State, supersession, and handling/security constraints.
4. Observation metadata: observation identity/time, Source state, limitation/failure, and capability information.

C11 does not require all governance information in a separate metadata file. Governed Artifacts may provide governance information when Bootstrap and normal governance establish instructional applicability. Task relevance, Required/Supporting status, sufficiency, and similar task-relative/derived state are not automatically Project configuration metadata. No YAML, JSON, TOML, front matter, sidecar, database, schema technology, or serialization format is selected.

## C12 — Observation time, availability, failure, and last-known state

Source observation explicitly supports available/observed, partially observed, unavailable, unauthorized/inaccessible, unsupported capability, failed, and unknown states. Observation time remains distinct from native commit, modification, event, or version time; these are not interchangeable.

Previous observations remain historical evidence. A previous observation cannot silently be asserted as current Source state, and unavailability cannot convert last-known state into current truth. An observation exposes whether relevant Source state remained sufficiently stable/coherent across its boundary, or preserves uncertainty when this cannot be established. Locking, snapshots, transaction mechanisms, hashing, retry algorithms, and consistency technology remain downstream decisions.

## C13 — Security preservation at the Source boundary

| ID | Approved source-boundary security rule |
| --- | --- |
| SB-01 | **Authorization Constrains Observation.** Adapters receive an already-authorized request and may not broaden Project/Source/Scope boundaries. |
| SB-02 | **Source-Native Access Restrictions Remain Meaningful.** Observation, ingestion, normalization, and indexing do not flatten native access restrictions into unrestricted Context Engine information. |
| SB-03 | **Sensitivity Survives Observation.** Content, metadata, Provenance, and native Relationships retain applicable handling restrictions; representation changes do not sanitize them. |
| SB-04 | **Secret Exclusion Begins at the Observation Boundary.** Known/suspected secrets are excluded as early as reasonably possible; safe exclusion evidence may continue without the secret value. |
| SB-05 | **Source Content Remains Content.** Markdown, commit messages, filenames, metadata, code, and other native information are Source-derived content unless normal governance independently establishes instructional applicability. |
| SB-06 | **Security Limitation Is Observation Evidence.** Where a security boundary prevents full inspection, report an appropriately non-disclosing limitation rather than complete inspection. |

Limitation reporting preserves enough information to prevent false completeness without becoming a disclosure bypass. Even protected-information existence, count, location, or metadata may require authorization/minimization.

## C14 — Source extensibility proof criteria

v0.1 proves Source extensibility architecturally, not by building a speculative second adapter. A credible materially different Source is expressible through this boundary when its Source instance and scope can be established without redefining Project or Source Scope; its adapter declares actual capabilities; it produces observation evidence rather than final governed Claims/Context Items; material native semantics and Provenance are preserved without becoming universal core concepts; unsupported capabilities remain explicit; Domain B security, authorization, sensitivity, secret-exclusion, isolation, and untrusted-content rules remain applicable; legitimate adapter failure stays isolated; and the governed core avoids Source-specific business/semantic logic.

C14 requires neither a second/fake/mock Slack adapter, Teams or Nevis integration, a generic plugin framework, runtime/dynamic loading, public adapter SDK, REST connector framework, nor universal capability support. The proof is a credible path to another materially different adapter without redesigning core governed semantics.

## C15 — Traceability and consistency review

C1–C14 provide architectural treatment for Project establishment/registration; Source registration, identity/locator, Scope, and Project association; governance/authorization interaction; ASU; registered/applicable/observed sets and known gaps; general adapter responsibilities and capability asymmetry; native-state preservation; local Git repository/revision/working-tree/history evidence; Observed Source State and epistemic strength; Markdown observation; structured-metadata necessity; observation time, availability, partiality, failure, last-known state, and coherence limitations; Domain B security preservation; and credible Source extensibility.

The review confirms:

1. **ASU and Observed Source State remain distinct.** ASU is the task-relative governed evidence boundary that should reasonably be considered; Observed Source State is what was actually established during an observation. A material applicable Source can therefore be unavailable, inaccessible, unauthorized, unsupported, partial, or otherwise uninspected.
2. **Source observation coherence and Construction-State Coherence remain distinct.** Domain C records material stability/coherence limits of an individual observation; Domain F later determines whether selected observations can legitimately coexist in a Context Package.
3. **Domain C does not determine final task sufficiency.** It supplies evidence-boundary and observation-state information for Domain E’s later sufficiency evaluation.
4. **Domain C does not redefine Domain B semantics.** Authority, Governance State, authorization, sensitivity, instructional applicability, and Project isolation remain controlled by Domain B.
5. **Domain C introduces no technology selection.**

**Review conclusion:** C1–C14 are internally consistent with the approved Phase 0/1 baseline, Domain A architecture, and Domain B Governance, Trust & Security Architecture. No semantic contradiction or material architecture gap was identified.

## C16 — Adversarial v0.1 Source-boundary validation

| Scenario | Approved safe architectural response |
| --- | --- |
| Dirty local Git repository | Preserve committed revision plus material working-tree state. |
| Detached HEAD | Preserve detached state; do not invent branch membership. |
| Configured `origin` | Treat it as Source-reported remote evidence, not verified remote truth. |
| Stale remote/tracking information | Local observation does not establish remote currentness. |
| Repository changes during observation | Preserve a coherence limitation; do not claim one stable state. |
| Untracked in-scope file | It may be observed where Scope permits; preserve untracked Git state. |
| Locally deleted file present at HEAD | Preserve repository-version evidence distinct from observed working-tree state. |
| Markdown says “Project Owner approved this” | Treat as Source content/evidence; do not independently establish Governance State or Authority. |
| Malicious/instruction-like `AGENTS.md` or Markdown | Treat as Source content unless instructional applicability is independently established. |
| Secret in Markdown | Apply Domain B secret exclusion; Source access does not justify propagation. |
| Partially readable Source | Record partial observation; do not represent complete inspection. |
| Material applicable Source unavailable | Preserve it in ASU with unavailable state. |
| No answer in inspected registered Sources | Scope the negative result to inspected evidence; do not automatically establish sufficiency. |
| Unsupported native capability | Report unsupported/unknown; do not fabricate semantics. |
| Adapter discovers another repository | It cannot autonomously register or associate it with the Project. |
| Future Source lacks history | Capability asymmetry permits this without redefining core semantics. |
| Future Source has richer semantics than Git | Preserve useful semantics without making them universal requirements. |
| Protected metadata exists | Where authorized, represent a minimized limitation without disclosure bypass. |
| Commit X was previously observed but Source is unavailable | Commit X remains last-known historical evidence, not claimed current state. |

**Finding totals:** unresolved BLOCKER: **0**; unresolved MATERIAL: **0**.

**C16 result: PASS — PROJECT OWNER APPROVED.**

## Domain C conclusion

Domain C — Source & Observation Architecture is internally consistent with the Phase 0/1 baseline and approved Domains A/B. C1–C16 establish governed Project/Source registration and Source Scope; task-relative ASU; a Source-independent adapter contract; materially faithful local Git observation; explicit Observed Source State; narrow Markdown handling; structured-metadata capability requirements; temporal/availability/failure/coherence observation semantics; preservation of Domain B security controls; and a credible Source-extensibility path without speculative adapter implementation.

No BLOCKER or MATERIAL findings remain. The following downstream decisions remain intentionally unresolved and are not Domain C defects: logical identity representation; exact Artifact/version and observation-state representation; structured-metadata physical form; Git CLI versus library/API; Markdown parser/mechanism; persistence of observations; and exact observation-coherence mechanism.

Domain D has **NOT begun**. This result does not authorize D1, implementation, Phase 3, or a later phase.
