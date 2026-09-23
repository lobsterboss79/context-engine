# Phase 2 Domain G — State, Persistence & Operational Architecture

**Phase status:** **AUTHORIZED / IN PROGRESS**  
**Domain G status:** **COMPLETE — PROJECT OWNER APPROVED — PASS**  
**Unresolved findings:** BLOCKER **0**; MATERIAL **0**; MINOR **0**  
**Domain H:** **NOT BEGUN**  
**Next activity:** **H1 — Establish technology-selection standard**  
**Implementation:** **NOT AUTHORIZED**

This record durably documents the already-approved G1–G17 State, Persistence & Operational Architecture baseline. It introduces no new material architecture, technology, security, governance, scope, persistence, runtime, deployment, testing, backup, observability, or implementation decision. Phase 3 and later phases remain **NOT AUTHORIZED**.

## G1 — Domain G requirements and constraints

The approved state principles are:

| ID | Requirement |
| --- | --- |
| ST-01 | Determine logical state and its required guarantees before selecting storage technology. |
| ST-02 | Physical identifiers, including keys, rows, files, records, hashes, and object IDs, do not redefine semantic identity. |
| ST-03 | Persistence does not create approval, governance, authority, verification, relevance, currentness, or other authority. |
| ST-04 | Persistence preserves material distinctions: Authority, Governance State, Provenance, transformation, temporal/currentness state, Conflict, Uncertainty, authorization, sensitivity, sufficiency, Construction-State Coherence, and other governed distinctions. |
| ST-05 | Where required, later changes do not silently rewrite material historical meaning. |
| ST-06 | Partial operations, denials, observation/persistence/recovery failures, incomplete construction, and degraded outcomes may require representation as state. |
| ST-07 | Durable storage has a purpose; intermediate processing values are not durable merely because they exist. |
| ST-08 | Reconstruction substitutes for persistence only when inputs/evidence remain sufficiently available and it preserves governed meaning reliably. Convenient recomputation is not reconstructability. |
| ST-09 | Processing authority does not inherently authorize indefinite storage, history, backups, audit duplication, or broader access. |
| ST-10 | Transformation and persistence do not sanitize sensitive information. |
| ST-11 | Domain B secret exclusion continues through state management. |
| ST-12 | Project isolation applies to persisted state and metadata. |
| ST-13 | Auditability and minimization coexist: retain enough governed evidence to explain material behavior without retaining every inspected byte, Candidate, model interaction, or protected value indefinitely. |
| ST-14 | v0.1 proportionality does not imply event sourcing, temporal databases, distributed transactions, HA, or enterprise backup systems. |
| ST-15 | G1–G5 select no persistence technology. |

## G2 — Logical-state inventory and classification

Logical state may belong to multiple classes; these are not exclusive containers.

1. **Governance & Project state:** Project identity/registration; Governance Bootstrap; governed configuration; Authority and Authority Scope; Governance State; governed Relationships; Source registration/Scope; applicable security/handling configuration.
2. **Source & observation state:** Source identity/reference and capability; observation identity; Observed Source State; observed Artifact/version/state; observation time; availability/partial/failure state; relevant native state; evidence-boundary information.
3. **Knowledge / representation state:** Artifact identity and version/state; Claims; Classifications; Relationships; Provenance; transformation lineage; temporal/currentness state; supersession; Conflict; Uncertainty/Unknown.
4. **Request & construction state:** Context Request, Requester, Consumer, Task Intent/Scope, ASU/evidence boundary, Candidate Context, applicability and Required/Supporting determinations, selection, sufficiency, bounded iteration, and termination reason.
5. **Package & Consumer state:** Context Package identity/state, Source Manifest, Construction-State Coherence, Package-Construction Record, rendering, delivery, receipt/use evidence where observable, and material limitations/failures.
6. **Audit / explanation / failure state:** material governance/security and authorization outcomes, explanation basis, Source/persistence failures, denied/degraded operations, recovery events, and material validation evidence.

Orthogonal dimensions include governed/derived/observed; current/historical; Persistent/Transient/Reconstructable; authoritative/non-authoritative; sensitive/ordinary; Project-scoped/cross-scope; and audit-relevant/operational. They answer different questions and must not collapse into one generic category.

## G3 — Persistent, Transient, and Reconstructable state

**Persistent** state survives execution because loss would materially undermine governance or identity continuity, historical interpretation, Provenance, auditability, meaningful reconstruction, failure/recovery behavior, or later legitimate use.

**Transient** state exists for legitimate processing but need not survive it, such as temporary parsing structures, intermediate ranking values, short-lived computation, or disposable rendering buffers. These examples select no implementation.

**Reconstructable** state need not itself persist only when necessary Source state, governed inputs, transformation basis, and applicable history can reasonably remain sufficiently available to reproduce the material semantic result. It is not legitimately reconstructable where a Source later disappears, historical state is absent, material transformation state is unknown, or AI-derived state is assumed reproducible by rerunning a changed model/provider. Hybrid durable records plus reconstructed verbose renderings are conceptually permitted, not selected physical design.

## G4 — Lifecycle, retention, and history

LC-01 through LC-10 require meaningful material transitions; distinction of current from historical state; purpose-driven retention; stable historical package meaning; honest limitations after deletion/expiration; last-known state as historical rather than current truth; supersession distinct from deletion; retention constrained by authorization/sensitivity; distinction of package from Source history; and no default indefinite retention.

The historical-reconstruction target, where legitimate retained evidence permits, is: **“What did the Project legitimately know, and what governed it, at time T?”** It does not require retention of every intermediate value.

## G5 — Persistence security, isolation, and sensitive information

PS-01 through PS-11 preserve meaningful persisted authorization scope; default Project isolation for content, metadata, lineage, indexes, audit, history, package/construction records, and related state; no authority merger through physical colocation; sensitivity through primary, derived, indexed, cached, audited, backed-up, and historical copies; sensitivity introduced by aggregation; secret exclusion from normal durable state (while authorized safe exclusion evidence may remain); protected metadata; authorization-bound audit access; governed backups; lifecycle treatment of material derived copies; and no security weakening after persistence failure. No deletion, encryption, backup, or persistence technology is selected.

## G6 — Consistency, integrity, and atomicity

A **logical consistency boundary** is a set of changes whose partial durable application would create materially false, contradictory, unauthorized, or unreconstructable governed state.

CI-01 preserves applicable links between identity/version, Claim/Provenance, transformation/material input, Context Item/selection basis, package/request/items/sufficiency/coherence, observation/outcome, audit/operation, and governance state/governing basis. CI-02 prohibits partial success from appearing complete. CI-03 requires semantic referential integrity without implying foreign keys. CI-04 preserves material prior state through correction. CI-05 makes atomicity proportional: optional observability-counter failure need not invalidate valid governed state, but loss of a Required package qualification can. CI-06 selects no ACID implementation, transaction manager, WAL, event sourcing, two-phase commit, consensus, locking, or other mechanism.

## G7 — Concurrency, retry, and idempotency

CRY-01 preserves distinctions among equivalent, simultaneous, duplicate, and retried Context Requests. CRY-02 prevents retries from silently multiplying governance transitions, Source registrations, successful package records, audit outcomes, or other governed effects. CRY-03 makes idempotency operation-specific. CRY-04 permits repeated observations as evidence without multiplying Authority. CRY-05 prevents newer state replacing an earlier construction’s observation basis. CRY-06 preserves material failed-attempt-to-successful-retry history. CRY-07 selects no key format, queue, mutex/lock, concurrency model, retry count/backoff, or job system.

## G8 — Failure-state preservation and recovery

Recovery restores a legitimately interpretable governed operational state after failure; it does not make failed work appear successful. FR-01 keeps material governance, authorization, Source/observation, persistence, package, rendering, delivery, audit, and recovery failures distinguishable. FR-02 distinguishes last durable from intended state. FR-03 preserves epistemic honesty: Unknown remains Unknown and recovery cannot strengthen evidence. FR-04 preserves isolation, authorization, sensitivity, secret exclusion, audit protections, and governance. FR-05 requires partial state to be safely completed, logically rolled back, isolated, explicitly unusable/incomplete, or otherwise prevented from normal complete treatment. FR-06 makes material recovery outcomes explainable. FR-07 permits explicit degraded operation but never governance/security relaxation for availability. No recovery mechanism is selected.

## G9 — Backup and recovery capability

Backup is justified only for durable state whose loss cannot acceptably be reconstructed with required meaning and guarantees. BR-01 derives recoverability scope from G3; BR-02 requires real reconstructability; BR-03 applies isolation, sensitivity, authorization, retention, and secret exclusion to backup; BR-04 requires sufficiently validated recovery; BR-05 rejects default zero loss/downtime, instant recovery, HA, standby, replication, and geographic redundancy; BR-06 makes backup history purpose-driven; and BR-07 prevents an older restored governance state from silently becoming current. No copy, dump, snapshot, replication, NAS, cloud/Git backup, product, or schedule is selected.

## G10 — Observability and measurability

Authorized operators must be able to understand functioning and locate material limitation/failure. Where material, operational evidence represents request lifecycle; observation, retrieval, denial, construction, sufficiency, coherence, rendering/delivery, persistence, retry/recovery, and justified resource/performance outcomes. OM-01 separates metrics from semantic truth. OM-02 prevents logs, metrics, traces, diagnostics, and related evidence from leaking protected content/metadata. OM-03 distinguishes negative results, unavailable/denied/failed retrieval, failed persistence, insufficiency, and delivery failure. OM-04 provides authorized conceptual correlation to request, attempt, Project, observation, package, and recovery. OM-05 selects no observability stack or correlation technology.

## G11 — Audit-state persistence

Observability operates the system; audit establishes what materially happened and why. AU-01 requires material audit evidence to survive for its approved governance, authorization, reconstruction, history, failure-explanation, or validation purpose. AU-02 prefers minimized references, identities, outcomes, and state over Source copies. AU-03 does not make recorded Claims authoritative. AU-04 prevents silent rewriting of material audit history while allowing corrections with prior record/correction basis where legitimate. AU-05 recognizes failed, denied, interrupted, partial, and degraded operations. AU-06 gives required-audit persistence failure an explicit, non-falsified consequence without selecting one universal outcome. AU-07 rejects default indefinite audit retention.

## G12 — Testability and validation architecture

TV-01 retains controlled test boundaries consistent with ports-and-adapters. TV-02 permits controlled Source conditions, including clean/dirty, unavailable/partial/changing/historical, conflicting/protected evidence, and unsupported capability. TV-03 permits deliberate Source, authorization, persistence/partial-write, retry/recovery, rendering/delivery, and audit-write failures at seams. TV-04 requires fixtures to establish actual governed semantics. TV-05 distinguishes reproducible fixtures from production replay. TV-06 preserves unit, component/boundary, integration, and proving validation scopes. TV-07 requires a fresh Consumer session/execution for applicable Company AI Roadmap proving. TV-08 denies production authority to test fixtures. TV-09 includes negative authorization, cross-Project, secret, protected-metadata, injection, and inaccessible-Required-Context tests. TV-10 selects no framework, container, CI, or coverage tool.

## G13 — Persistence capability and candidate evaluation baseline

### Capability requirements

PC-01 through PC-30 require: governed logical-state fidelity; Persistent/Transient/Reconstructable support and its basis; semantic identity/referential integrity; historical-state, Provenance/lineage, and observation-state preservation; semantically coupled-state integrity; distinguishable incomplete/failed state; concurrency integrity; safe retries/duplicates; recovery integrity; Project isolation; authorization-aware access; sensitivity, secret exclusion, and protected metadata; purpose-driven lifecycle, governed deletion/expiration, and backup/recovery where required; recoverability validation; audit durability/history integrity; persistence-failure visibility; operational diagnosis distinct from semantic truth; controlled test state and failure simulation; meaningful reconstruction without universal byte replay; portable core semantics; v0.1 proportionality; and explicit limitations.

PC-18 is controlled by G14: deletion accounts for material copies/derivatives but cannot fabricate historical nonexistence; neither retention nor deletion is universally prescribed. PC-19–PC-20 require appropriate recoverability and meaningful recovery validation without selecting schedule, RPO/RTO, or product. PC-28 keeps technology-specific capability behind the persistence boundary; PC-29 rejects unjustified distributed/HA/warehouse/broker/multiple-store architecture; PC-30 requires honest limitations.

The individual capability register is: PC-01 Governed Logical-State Fidelity; PC-02 Durable-State Classification Support; PC-03 Identity and Referential Integrity; PC-04 Historical-State Preservation; PC-05 Provenance and Transformation-Lineage Durability; PC-06 Observation-State Preservation; PC-07 Semantically Coupled State Integrity; PC-08 Incomplete / Failed-State Distinguishability; PC-09 Concurrency Integrity; PC-10 Retry / Duplicate-Operation Safety; PC-11 Recovery-State Integrity; PC-12 Project Isolation; PC-13 Authorization-Aware State Access; PC-14 Sensitivity Preservation; PC-15 Secret Exclusion; PC-16 Protected-Metadata Handling; PC-17 Purpose-Driven Lifecycle and Retention; PC-18 Governed Deletion / Expiration; PC-19 Backup / Recovery Capability Where Required; PC-20 Recoverability Validation; PC-21 Audit-State Durability; PC-22 Audit-History Integrity; PC-23 Persistence-Failure Visibility; PC-24 Operational Observability; PC-25 Test-State Controllability; PC-26 Failure-Simulation Seam; PC-27 Meaningful Reconstruction Support; PC-28 Technology Independence / Portability; PC-29 v0.1 Proportionality; and PC-30 Explicit Capability Limitations.

### Candidate criteria

Future candidates are qualified against PC-01–PC-30 before comparative evaluation using PR-01 semantic fidelity; PR-02 integrity support; PR-03 failure/recovery integrity; PR-04 historical/audit support; PR-05 security/isolation; PR-06 lifecycle support; PR-07 testability; PR-08 secure observability; PR-09 v0.1 proportionality; PR-10 portability/reversibility; PR-11 operational complexity; and PR-12 capability honesty. No arbitrary numerical scoring is selected.

G13 selects none of PostgreSQL or SQLite; SQL, document, relational, graph, filesystem, one/multiple-store, normalized/denormalized, event-sourced, or temporal storage; UUID/integer/hash physical identifiers; ORM, migration, JSON column, filesystem layout, index/cache, transaction/lock/concurrency, encryption, backup/RPO/RTO, observability, or test technology.

The approved G13 baseline requires faithful technology-independent state preservation, integrity, security, lifecycle, recoverability, audit, observability, testability, reconstruction, portability, proportionality, and explicit limitations. It does not select a persistence mechanism.

## G14 — Integrated persistence/state capability review

**Result:** **PASS — PROJECT OWNER APPROVED**

G14 reviewed G1–G13 as one capability architecture, including classification/reconstructability, history/lifecycle/deletion, security/isolation/sensitivity/secrets/metadata, coupled integrity/partial persistence/atomicity, concurrency/retry/idempotency, recovery, backup proportionality, observability/audit/testability, PC-01–PC-30, PR-01–PR-12, and technology leakage. Findings were BLOCKER 0, MATERIAL 0, MINOR 1; unresolved MINOR 0.

**MN-G14-01 — RESOLVED: historical preservation/deletion interaction.** Historical reconstruction is subordinate to legitimate retention authority, deletion, security, minimization, and authorization. It does not universally retain deleted/expired content. Where content may remain, retain required history under applicable retention. Where content must be deleted but authorized minimum non-content history may remain, preserve only that evidence necessary to establish such facts as prior existence, material participation, later removal/unavailability, or transition. Where content and existence/metadata may not remain, honor the prohibition and preserve only an authorized limitation, if any. Audit is not a deletion loophole. This introduces no deletion technology, duration, erasure method, storage mechanism, or new historical semantic.

G14 confirmed sound classification; evidence-based rather than convenient reconstructability; no event-sourcing requirement; proportional rather than universal ACID/locking/idempotency; recovery that does not make restored history current; proportional backup without HA/replication/RPO/RTO; compatible audit durability/minimization; secret exclusion through all material copies; framework-neutral testability; sufficient PC and PR registers; and no physical persistence/storage model selection. G1–G13 are a coherent technology-neutral capability architecture and MN-G14-01 is resolved.

## G15 — Runtime and deployment operational requirements

RO-01 through RO-30 require explicit initialization of operation/Project/Bootstrap/configuration/capability/limitation state; governance before governed processing; separation of runtime configuration from governed Project state; operation-relative dependency readiness; explicit scoped degradation; honest clean shutdown and interruption recovery; distinguishable completion/failure/interruption/incompleteness/recovery need; no governance identity from process/host/environment identity; local v0.1 as permitted rather than semantic; governed filesystem and working-directory boundaries; governed temporary state; no unjustified network dependency; isolated external-capability failure; no epistemic strengthening through transport success; explicit resource exhaustion and no performance shortcuts around governed checks; no default enterprise scale; least necessary runtime privilege; operation-specific authorization; governed sensitive memory/temporary representations; secured diagnostics; authorized material operator observability; distinction of process health, Project readiness, and request readiness; authorized correlation; environment behavior behind boundaries; relocation-stable semantics; explicit environment assumptions; and undecided deployment mechanism.

The required conceptual ordering is: runtime start -> establish environment/capabilities -> Governance Bootstrap -> Project/governance -> required dependencies -> accept/perform governed operation. Startup or storage reachability is not governance success. Filesystem access and working directory do not establish Project, Source Scope, or Authority. A local runtime is permitted; network, OS, host, storage, process, container, service, health-check, and deployment technologies remain unselected.

The individual runtime register is: RO-01 Explicit Runtime Initialization; RO-02 Governance Before Governed Processing; RO-03 Operational Configuration != Governed Project State; RO-04 Required Dependency Readiness Is Explicit; RO-05 Degraded Operation Remains Explicit; RO-06 Clean Shutdown Preserves Required State; RO-07 Unexpected Termination Is Recovered Honestly; RO-08 Interrupted Operations Remain Distinguishable; RO-09 Runtime Identity Does Not Create Governance Identity; RO-10 Local v0.1 Is Permitted, Not Semantically Required; RO-11 Filesystem Boundaries Remain Governed; RO-12 Working-Directory Assumptions Do Not Become Semantics; RO-13 Runtime-Generated Temporary State Is Governed; RO-14 No Mandatory Network Dependency Without Requirement; RO-15 External Capability Failure Remains Isolated Where Possible; RO-16 External-Service Success Does Not Strengthen Epistemic State; RO-17 Resource Exhaustion Fails Explicitly; RO-18 Performance Degradation != Semantic Degradation; RO-19 No Enterprise Scaling Requirement; RO-20 Runtime Privilege Follows Least Necessary Capability; RO-21 Runtime Authorization Remains Operation-Specific; RO-22 Sensitive State Remains Governed in Memory and Temporary Representations; RO-23 Runtime Diagnostics Cannot Bypass Security; RO-24 Material Runtime State Is Operator-Observable at an Authorized Level; RO-25 Runtime Readiness != Universal Task Readiness; RO-26 Operational Evidence Remains Correlatable; RO-27 Environment-Specific Behavior Stays Behind Boundaries; RO-28 Deployment Relocation Does Not Redefine Semantics; RO-29 Material Environment Assumptions Are Explicit; and RO-30 Deployment Mechanism Remains Undecided.

## G16 — Traceability and consistency review

**Result:** **PASS**

The responsibility chain is: logical state -> durability classification -> lifecycle/history -> persistence security -> integrity/atomicity -> concurrency/retry -> failure/recovery -> backup/recoverability -> observability -> audit persistence -> testability -> persistence capability -> Project Owner gate -> runtime/deployment operations.

Domain G preserves Domain A’s logical-state/persistence separation, EB-03 boundary, portability, boundary-local environment behavior, optional local operation, no unjustified network, and fail-without-semantic-degradation principle. It operationalizes Domain B authorization/isolation/sensitivity/secrets/protected metadata/audit minimization and explicit audit-write failure. It retains Domain C observation honesty and last-known-state limits. It preserves Domain D semantic identity, Claim, Authority, Governance, Provenance, temporal/currentness, Conflict, and Uncertainty without requiring event sourcing/temporal storage. It retains Domain E request, Candidate/evaluation, selection, Required/Supporting, sufficiency, ASU/boundary, and termination semantics. It supplies Domain F’s deferred persistence/lifecycle/audit/reconstruction capability for packages, manifests, coherence, construction records, rendering, delivery, receipt, and limitations.

MN-G14-01 resolves historical reconstruction versus deletion. G15 remains ports-and-adapters compatible: operational configuration is distinct, filesystem access does not expand scope, startup/health do not establish governance/readiness, and local operation does not become core semantics. No requirements contradiction, conceptual-model contradiction, material cross-domain inconsistency, or unresolved persistence/state capability gap was identified. G1–G15 remain consistent with Phase 0/1 and Domains A–F.

## G17 — Failure, recovery, and persistence adversarial review

**Result:** **PASS — PROJECT OWNER APPROVED**

G17 tested physical identity and repeated persistence/observation against semantic identity and Authority; supersession/history/deletion and prohibited metadata retention; inadequate reconstruction due to disappeared Sources or unknown model transformations; partial package and Provenance failures; overlapping operations, duplicates, retries, and retry history; crash/recovery/older-governance/currentness uncertainty; authorization/security-preserving recovery; backup existence, technical restore, sensitivity, secrets, and staleness; false persistence/audit success; audit minimization/correction; negative-result versus retrieval-failure observability; metric and diagnostic leakage; resource exhaustion and proportional atomicity; startup, bootstrap, capability, filesystem, working-directory, temporary-state, network, resource/performance, and readiness boundaries; and controlled, semantically valid test/proving conditions.

The representative partial-write attack is: package identity -> selected Context Items -> Source Manifest -> crash -> missing sufficiency/coherence -> incomplete Package-Construction Record. Existence of package state does not establish completed construction. A later physical design must establish legitimate completion without requiring SQL transactions or another prescribed atomicity mechanism.

The recovery/currentness attack confirms that restoring Monday’s Governance State A after Tuesday’s then-current State B fails establishes only restoration of A, not present legitimate currentness. The gap remains explicit. The historical-deletion attack confirms MN-G14-01’s three cases: retained content/history where authorized; minimum authorized non-content evidence after content deletion; or prohibition-honoring deletion of content and existence/metadata with only an authorized limitation, if any. Audit/history does not mean keep everything.

If durable audit is required and its write fails, no audit guarantee may be claimed; later physical design may make an explicit failure, denial, qualification, degradation, or other governed outcome without Domain G selecting one universal result. Future architecture must permit controlled tests for partial persistence, overlap/retries/failures/crashes/recovery/stale history, authorization/isolation/secrets/metadata, Source and rendering/delivery failures, and audit-write failure. No test framework is selected.

G1–G15 select none of the storage, schema, identifier, transaction/concurrency/retry, encryption, backup, observability, test, operating-system, VM/container, cloud, process-management, health-check, or deployment technologies listed in the Domain G boundary. Findings: unresolved BLOCKER 0; unresolved MATERIAL 0; new MINOR 0; unresolved MINOR 0. MN-G14-01 remains resolved.

## Domain G closing result

**Domain G — State, Persistence & Operational Architecture: COMPLETE — PROJECT OWNER APPROVED — PASS.**

G1–G15 establish technology-independent logical state; ST-01–ST-15; multidimensional state classification; evidence-based Persistent/Transient/Reconstructable semantics; lifecycle/history; isolation/sensitivity/secret exclusion; logical coupled integrity; mechanism-neutral concurrency/retry/idempotency; failure/recovery; proportional backup; observability/audit/testability; PC-01–PC-30 and PR-01–PR-12; the approved G14 gate and MN-G14-01; and RO-01–RO-30. G16 confirms consistency; G17 finds no unresolved BLOCKER, MATERIAL, or MINOR findings. Persistence, storage, schema, transaction, concurrency, backup, observability, testing, runtime, host, process-management, and deployment technologies remain intentionally undecided.

Domain H has **NOT begun**. **H1 — Establish technology-selection standard** is the next Phase 2 activity. Implementation, Phase 3, and later phases remain **NOT AUTHORIZED**.
