# Phase 2 Domain H — Technology Selection & v0.1 Physical Architecture

**Phase status:** **AUTHORIZED / IN PROGRESS.**  
**Domain H status:** **COMPLETE — PROJECT OWNER APPROVED — PASS.**  
**H1–H22:** **COMPLETE.**  
**Unresolved findings:** BLOCKER **0**; MATERIAL **0**; MINOR **0**.  
**MT-H19-01:** **RESOLVED / CLOSED.**  
**Domain I:** **NOT BEGUN.** **Next activity:** **I1 — Reconcile complete Phase 2 decision inventory.**  
**Implementation:** **NOT AUTHORIZED.** Phase 3 and later phases are **NOT AUTHORIZED**.

## Governance record

This record durably documents the already-approved H1–H22 technology and physical-design baseline. It introduces no new material decision. Domain H converts the approved logical/conceptual architecture into a physical v0.1 baseline; physical technology implements Domains A–G and does not redefine them. Selection does not authorize installation, initialization, scaffolding, configuration, deployment, application code, testing, or any later phase.

## H1 — Technology-selection standard

Technology selection follows `requirements -> qualification -> comparison -> Project Owner decision -> durable decision record`.

| IDs | Approved standard |
| --- | --- |
| TS-01–TS-04 | Requirements precede candidates; architecture constrains technology; qualification is **Qualified**, **Qualified With Material Limitation**, or **Not Qualified**; criteria are decision-specific and derive from requirements, architecture, v0.1 proving, security, and operations. A Not Qualified candidate cannot win through convenience. |
| TS-05–TS-06 | No invented numerical weighting or pseudo-objective scores. Real measured evidence—versions, memory, licensing, support lifecycle, and requirement-relevant performance—is permitted. |
| TS-07–TS-10 | Consider a reasonable, diverse set of credible alternatives. Clearly unqualified candidates need only document failed requirements/evidence. Material claims require appropriate authoritative evidence. |
| TS-11–TS-12 | Preserve fact, Project-specific inference, and selection judgment distinctions. Unknown capability remains explicit and may be a limitation, pending evidence, or Not Qualified. |
| TS-13–TS-17 | Prefer least-sufficient qualifying technology; evaluate total-system complexity, familiarity without letting it govern, popularity as evidence rather than qualification, and contextual total cost. |
| TS-18–TS-22 | Evaluate Context Engine-specific security, dependency consequences, licensing/sustainability, reversibility, and honest replacement cost including data, queries, transactions, errors, tests, deployment, and operations. |
| TS-23–TS-27 | Material selections require Project Owner approval and records of requirements, candidates, qualification, tradeoffs, limitations, deferrals, and disposition. Selection does not authorize implementation. New material evidence reopens a decision explicitly: evidence → affected decision → impact → governance reopening → revised approval → durable update. |

**H1 conclusion:** qualification precedes comparison; no technology is selected by H1. Qualifying alternatives are compared for semantic/security fidelity, total-system complexity, operations, dependencies, sustainability, cost, reversibility, and v0.1 proportionality.

## H2/H3 — Decision inventory and materiality

| Decision | Classification |
| --- | --- |
| TD-01 language/runtime; TD-02 persistence; TD-03 Bootstrap/Project configuration representation; TD-04 local Git; TD-05 Markdown; TD-06 package/execution; TD-07 deployment | **Class M** — Project Owner gates H5, H7, H9, H11, H13, H16, H17. |
| TD-08 testing beyond native; TD-09 configuration; TD-10 logging; TD-11 backup; TD-12 concurrency/retry/idempotency; TD-13 security/crypto; TD-14 semantic/AI/vector; TD-15 other libraries/frameworks/infrastructure | **Class C** — establish need at H14, then materiality/selection at H15 if needed. |

Ordinary names, organization, physical tables/columns/indexes, retry/timeouts, logs, temporary paths, DTOs, individual Git syntax, and parser-token organization are Class I unless later material. Dependency direction is H1 → H2 → H3 → language/runtime → persistence/configuration/Git/Markdown → additional necessity → material dependencies → package/execution → deployment → integrated design.

Class M changes can affect architecture, semantics, security/governance, persistence/history, external dependencies, operations, portability, proving, non-goals, or migration. Class C means **no separate technology required** is valid. Class I stays inside approved boundaries. MT-01–MT-10 test Architecture, Semantic, Security/Governance, Persistence/History, External Dependency, Deployment/Operations, Portability/Reversibility, Proving, Scope/Non-Goal, and Ambiguity. SQLite remains M despite `sqlite3`; standard-library use is not automatically non-material. Runtime-family selection is material; compatible patch selection is ordinary only while it does not cross a materiality test.

Codex must stop before introducing/replacing/materially upgrading Class M, introducing technology for an unapproved Class C need, or proceeding through genuine ambiguity.

## H4/H5 — Language/runtime

LR-01–LR-20 require architectural and governed-semantic fitness; deterministic controls; local Git/Markdown and persistence-boundary fitness; testability; explicit failures; security; provider independence; local execution; portability; ecosystem/maintainability; proportional operations; maintained support; reasonable performance; acceptable licensing; packaging path; and no downstream technology smuggling. LR-14, AI-assisted-development fitness, is comparative; the rest are non-negotiable.

LRC-01–LRC-14 compare architecture/semantic fit, simplicity, testability, Git/Markdown, persistence ecosystem, security/dependencies, maintainability, AI development, burden, portability/packaging, sustainability, performance, familiarity, and total complexity—without numerical weighting.

| Candidate | Qualification | Decision reasoning |
| --- | --- | --- |
| Python / CPython | **QUALIFIED** | Selected: best low-ceremony local automation/text/document/transformation/Git/Markdown/testing fit. Its less compiler-enforced discipline than C# requires explicit governed models rather than loose strings/dictionaries. |
| C# / .NET | **QUALIFIED** | Strong static modeling and tooling; more ceremony than justified for v0.1. |
| Go | **QUALIFIED** | Strong compiled/concurrency profile; its comparative strengths solve no demonstrated need and less directly fit the document/context workload. |

**TD-01:** Python 3 / CPython **3.14 release line**. A compatible maintained patch can later be chosen; materially incompatible runtime change is H3-governed. H5 defers framework, ORM, persistence, Git/Markdown, formats, testing/CLI/logging, AI, bundling, OS, and deployment.

## H6/H7 — Persistence

PSR-01–PSR-36 require local CPython fitness; structured governed state while preserving application semantic identity; integrity, semantic atomicity, detectable failure, crash/restart, proportional concurrency/retry; history, Provenance, reconstruction, Project isolation, application authorization, sensitive metadata and secret exclusion; lifecycle/deletion; backup/recovery/audit/diagnosis; controlled testing/failure simulation; EB-03 portability; proportional operation/dependencies; sustainable licensing/capacity/queryability/evolution; and honest limits. PSC-01–PSC-15 compare semantic model, integrity, recovery, history/Provenance/audit, security/isolation, lifecycle/backup, integration, testability, operations/deployment, query/model, migration, portability, sustainability, and total complexity.

| Candidate | Qualification | Result |
| --- | --- | --- |
| SQLite | **QUALIFIED** | **Selected**: embedded/serverless, low burden, transactions, constraints, queryability, crash/restart behavior, backup, and CPython `sqlite3`. Explicit limits: single writer; integrity/durability configuration; foreign keys enabled/verified where relied upon; host/filesystem availability. |
| PostgreSQL | **QUALIFIED** | Strong concurrency/recovery/scale, but needs service lifecycle, administration, access configuration, backup administration, and Python dependency not justified by v0.1. |
| Application-owned filesystem state | **NOT QUALIFIED** primary persistence | Required integrity, atomicity, partial-write/recovery, retry, history, Provenance, querying, evolution, and concurrency would create a custom persistence engine. Files remain valid for configuration, Sources, approved backup artifacts, and other non-primary roles. |
| Hybrid | **NOT JUSTIFIED** | A second primary store adds consistency, recovery, migration, test, failure, and operating complexity. |

**TD-02:** SQLite behind **EB-03**. Core semantics do not depend on SQLite row IDs, SQL, schema, transaction syntax, or layout. H7 defers physical schema, IDs, normalization, ORM/data access, migration mechanism, journal/synchronous/connection/foreign-key details, indexes/queries, topology/path, encryption, backup/retention/archive, PostgreSQL migration, configuration, and deployment.

## H8/H9 — Structured representation

SR-01–SR-07 establish Bootstrap, Project configuration, SQLite-owned state, and explicitly no universal Context Package, Consumer, fixture, or import/export serialization. SMR-01–SMR-20 require human authorability, deterministic Unicode structure, conservative semantics, explicit syntax failure, non-self-authorizing/non-circular trust, loading Provenance, version/evolution, semantic validation, secret exclusion, portability/Git review fitness, CPython 3.14 path, proportional dependency, mature/secure parser behavior, optional comments, and no exact rewrite preservation. Same TOML syntax does not merge Bootstrap and Project trust roles. SMC-01–SMC-10 compare predictability, authoring, Python, structure, validation/evolution, security, diff/review, maturity, dependencies, and total complexity.

| Candidate | Qualification | Result |
| --- | --- | --- |
| JSON | **QUALIFIED** | Simple/mature/deterministic/standard-library, but no comments and comparatively punctuation-heavy. |
| TOML | **QUALIFIED** | **Selected**: configuration-focused, comments, explicit semantics, UTF-8, sufficient structure, mature specification, dependency-free read parsing. |
| YAML | **QUALIFIED WITH MATERIAL LIMITATION** | Rich typing/tag/alias/schema surface and external parser normally need extra constraint not justified by v0.1. |

**TD-03:** TOML 1.0.0, read through CPython 3.14 `tomllib`. Read-only `tomllib` is sufficient because configuration is human-maintained. Valid TOML is not governance/Authority/authorization/semantic validity; deterministic validation controls. H9 defers schemas/fields/paths/delivery, validation or writing libraries, automatic editing, SQLite JSON, package/API/import/export/fixture formats, front matter, sidecars, and database schema.

## H10/H11 — Local Git

GIR-01–GIR-30 require Git-native repository/work-tree/HEAD/ref/index/working/untracked/deletion/rename/history fidelity; identity evidence without path identity; attached/detached/unborn/failure distinctions; local-only/no-network and epistemically bounded remote state; governed Scope and filesystem safety; secret/untrusted-content controls; explicit failures; machine-stable exact/Unicode/bounded handling; shell-free arguments and controlled environment; native restrictions and observation coherence; controlled testing/failure simulation; maintained Git/CPython compatibility; proportional dependencies/performance; diagnostics; replaceability; and no provider/remote/watcher/cache/downstream technology smuggling. GIC-01–GIC-15 compare semantic/failure/machine/security/Python/dependency/test/history/work-tree/compatibility/operations/portability/performance/implementation/total complexity.

| Candidate | Qualification | Result |
| --- | --- | --- |
| Native Git CLI via `subprocess` | **QUALIFIED** | **Selected**: direct semantics, machine interfaces, complete local capability, explicit failures, no Python Git package. |
| GitPython | **QUALIFIED WITH MATERIAL LIMITATION** | Adds abstraction/dependency while generally retaining Git executable; maintenance posture weakens the case. |
| pygit2 / libgit2 | **QUALIFIED WITH MATERIAL LIMITATION** | Adds Python/native/libgit2 compatibility/deployment chain without demonstrated need. |

**TD-04:** native Git CLI via shell-free CPython `subprocess`. Use argument vectors, never interpolation or `shell=True`; use documented machine/plumbing/porcelain output, explicit formatting/NUL paths/status/stdout/stderr/environment. A compatible Git executable is a runtime prerequisite, not network, GitHub, remote API, sync, SSH/HTTPS, credential, or provider selection. Exact commands/version/timeouts/retries/environment/locking/remotes/cache/watchers/diff/rename details are deferred.

## H12/H13 — Markdown

Markdown is deterministic, structure-aware parsing—not raw-text-only primary processing or a publishing pipeline: original observed Source remains evidence plus derived structure. MDR-01–MDR-30 cover original preservation; headings, paragraphs, lists, code, links, approved tables, and hierarchy; useful line/region provenance; derived/failure/unknown syntax visibility; Unicode; inert/local processing with no execution/rendering/fetch; front matter not governance; no rewrite/HTML/canonical output; actual-dialect fitness; bounds/determinism/CPython/dependency/test/version controls; replacement; token-not-Claim; and no downstream renderer/browser/AI/database smuggling. MDC-01–MDC-15 compare structural/location/original-content/determinism/table/failure/security/integration/dependencies/testing/extensibility/maintenance/performance/implementation/total complexity.

| Candidate | Qualification | Result |
| --- | --- | --- |
| Standard-library/custom recognition | **NOT QUALIFIED** primary parser | Would create an unnecessary partial parser; ordinary text processing remains useful for preservation, bounds, and Provenance. |
| markdown-it-py | **QUALIFIED** | **Selected**: deterministic CommonMark token stream, block maps, useful structure/tables/configuration, pure Python, low burden. |
| Marko | **QUALIFIED** | Richer AST/source spans exceed current need. |

**TD-05:** markdown-it-py **4.x** mechanism/API family, CommonMark plus approved table support. Explicit version-controlled configuration enables only demonstrated rules/extensions. Block line ranges satisfy approved Source mapping. Parser output establishes neither Claim, Authority, Governance State, relevance, selection, nor sufficiency. H13 defers HTML/rendering/sanitizer/browser/rewrite/output, plugins, Claim extraction/token mapping, chunking, AI/vector/search, and Consumer format.

## H14/H15 — Additional technology

The necessity test is approved capability → can selected/native baseline satisfy it? → yes: no separate technology; no: specific gap → least sufficient solution → H15 material evaluation.

H14 found **NO SEPARATE TECHNOLOGY REQUIRED** for TD-08 native test capability; TD-09 configuration; TD-10 logging; TD-11 backup; TD-12 concurrency/retry; TD-13 security/crypto; TD-14 initial semantic/AI/vector capability; and TD-15 other technologies. Required behavior remains required. Initial deterministic discovery uses metadata, identity, Classification/Relationships, SQLite, literal/text discovery, Markdown, Git history, and bounded expansion; semantic assistance remains an explicit reopening seam.

At H15, standard-library testing and pytest were both qualified. **pytest 9.x** is selected as the sole additional material dependency, development/test-only: fixtures, lifecycle, temporary paths, monkeypatching, capture, parametrization, exception testing, and discovery reduce custom test infrastructure without changing production semantics. No pytest plugin is selected; future plugins require need/materiality review.

## H16 — Packaging and execution

PE-01–PE-20 approve: a proper installable Python package; standardized `pyproject.toml` metadata (not Bootstrap/governance/state/Source metadata); markdown-it-py runtime and pytest development separation; explicit Python 3.14 compatibility; CPython `venv`; direct dependency declaration; stable `context-engine <operation>` entry; CLI-only/native CLI; prerequisite/readiness checks; explicit Git failure; no governance established by installation; clean termination and interruption recovery; no runtime network requirement; Git boundary containment; portable metadata; safe diagnostics; and test separability.

**TD-06 — PASS — PROJECT OWNER APPROVED:** standard installable Python package, `pyproject.toml`, CPython `venv`, console/CLI entry, and no CLI framework. No standalone bundler or public PyPI/wheel/sdist pipeline is required. Minimal standards-compatible build/install path is approved; exact non-material backend/tooling is Class I. Poetry, uv, Hatch, PDM, pip-tools, and other management frameworks are not selected. Approved convention: `src/context_engine/` with `tests/`, without one-to-one architecture-to-module mapping.

## H17 — Deployment

**TD-07 — PASS — PROJECT OWNER APPROVED:** direct local Linux x86-64 host; Ubuntu Linux initial proving/development environment; on-demand ordinary non-root process.

DER-01–DER-30 require CPython/Git/Source/SQLite/durable-state fitness; application-governed isolation and least privilege; no root/network requirement; checkable prerequisites and venv/reproducibility; simple startup/recovery/backup/diagnosis/updates/proving; portable semantics and low overhead; no service boundary or deployment-specific Source identity; explicit external dependencies; narrow supported host allowed; no HA; VM/container only with justified need; and replaceability.

Direct host is **QUALIFIED**. VM and container are **QUALIFIED WITH MATERIAL LIMITATION**: they complicate fidelity to the actual host dirty/staged/untracked tree and add mounts, path, permission, filesystem, state, and lifecycle boundaries without v0.1 justification. No VM/container/Docker/orchestration/cloud/database service/network/HA/daemon is selected. Application state is in an explicit writable location outside Sources by default; exact path is deferred.

## H18 — Integrated physical architecture

**H18: COMPLETE — PROJECT OWNER APPROVED.** Runtime: Python/CPython 3.14; SQLite/`sqlite3`; TOML 1.0.0/`tomllib`; shell-free native Git; markdown-it-py 4.x/CommonMark/tables; `pyproject.toml`; `venv`; CLI; direct Linux x86-64/Ubuntu proving; Python logging; SQLite backup. Development/test: pytest 9.x.

`Operator -> CLI -> application services -> core domain -> ports -> adapters/environment`. Configuration/TOML, Git Source, Markdown transformation, SQLite persistence, rendering, and CLI/diagnostics are boundaries. Core semantics know neither SQL/rows, Git commands, TOML syntax, parser tokens, Linux paths, nor CLI syntax.

Startup is CLI → prerequisites → explicit Bootstrap → Bootstrap TOML validation → Project TOML under Bootstrap scope → Project/governance/Source/Scope → SQLite readiness → operation dependencies → request. Bootstrap TOML, Project TOML, SQLite state, Git/Markdown evidence, logs, and backups remain separate. Git produces observed state; Markdown retains original evidence plus derived structure; remotes do not establish live currentness.

SQLite is one DB per deployment, with explicit Project association/isolation and state outside registered Sources. Internal keys are not semantic identity. Explicit schema version distinguishes compatible, older-migratable, newer/unsupported, and malformed/unknown; deterministic application migrations suffice and must not falsely appear current. Short transactions implement semantic boundaries after external observation. Required connection integrity and foreign keys where relied upon are verified; PRAGMAs/connections/indexes remain detailed choices.

Abnormal recovery establishes SQLite integrity/schema/incomplete state before governed work; rollback does not settle semantic currentness. SQLite-supported consistent backup is sufficient, with governed destination/handling/retention/identification/restore validation deferred. Python logging is diagnostic, minimized, and not audit. Packages persist only required construction/audit evidence; rendering may be transient/reconstructable. Normal construction does not mutate registered Git Sources. Runtime network is not required.

The architecture excludes ORM/migration/modeling/YAML/TOML-writer/GitPython/pygit2/Click/Typer/Redis/broker/locks/telemetry/backup/security/AI/vector/search products, APIs/GUI/daemon/services/VM/containers/cloud. Its former sole material deferral—Bootstrap delivery—is resolved in H19. H18 authorizes no implementation.

## H19/H20 — Review and adversarial validation

H19 initially passed with MT-H19-01: no physical independent Bootstrap-supply mechanism. BRQ-01–BRQ-10 required independent origin, explicit invocation, no Source self-selection, local proportionality, path-not-Authority, explicit failure, no secret, automation compatibility, no global mutable registry, and auditable Provenance.

Explicit CLI-supplied Bootstrap reference was qualified and selected over an environment variable (ambient/mutable/less visible) and fixed location (implicit default). Governed Project operations require an explicit invocation reference, conceptually `context-engine --bootstrap /trusted/path/bootstrap.toml <operation>`; no current-directory, repository-root, home, nearby Source, or Project-content discovery/default is allowed. Supplying a candidate does not authorize it; invalid/unavailable state fails explicitly. **MT-H19-01: RESOLVED. H19 final PASS: 0/0/0.**

H20 adversarial review passed across Bootstrap/TOML/Git/Markdown/SQLite/cross-Project/recovery/logging/packaging/direct-host/testing/package/Consumer/deterministic-retrieval/replacement attacks. It confirms that syntax, paths, parser tokens, DB rows, backup existence, logs, host readability, or delivery cannot silently establish Authority, currentness, semantic identity, readiness, audit, or Consumer use. Git/parser/persistence/delivery failures remain distinct. AI/vector/LLM additions and material replacements explicitly reopen their TD. **H20: PASS — PROJECT OWNER APPROVED; no technology leakage.**

## H21 — Technology-to-requirement / architecture traceability

**H21: COMPLETE — PASS — PROJECT OWNER APPROVED.** Bidirectional traceability was reviewed: approved requirement/architecture → physical mechanism and selected mechanism → approved driver. BLOCKER 0, MATERIAL 0, MINOR 0, orphan selections 0, unrealized material capability requirements 0; MT-H19-01 remains resolved.

| Physical realization | Principal approved driver | Result |
| --- | --- | --- |
| Python/CPython 3.14 | Domains A/G modular single process, ports/adapters, deterministic local/testable replaceable execution; LR-01–LR-20 | PASS |
| SQLite via `sqlite3` behind EB-03 | Domain G PC-01–PC-30, PR-01–PR-12; PSR-01–PSR-36: durable state, integrity, atomicity, history, Provenance, isolation, recovery, audit, query/test/portability | PASS |
| TOML/`tomllib` | Domain B Bootstrap; Domain C Source registration/Scope; SR-01/02; SMR-01–20 | PASS |
| Explicit CLI Bootstrap | Domain B non-circular trust; H19 BRQ-01–10 | PASS |
| Native Git via subprocess | Domain C source observation and Git fidelity; GIR-01–30 | PASS |
| markdown-it-py/CommonMark/tables | Domain C Markdown; Domain D evidence/provenance; MDR-01–30 | PASS |
| pytest 9.x test-only | Domain G G12; H14/H15 fixture-heavy failure/testing architecture | PASS |
| `pyproject.toml`/venv/package/CLI | A/G runtime boundaries, reproducibility, isolation/readiness, PE-01–20 | PASS |
| Direct Linux host | A local v0.1; C live work-tree; G proportional/reversible runtime; DER-01–30 | PASS |
| Python logging / SQLite backup | Domain G G10 observability / G9 recovery | PASS |
| No initial AI/vector stack | Domain E deterministic foundation and bounded semantic-assistance seam | PASS |

Reverse traceability passed for governance/Bootstrap, authorization/isolation/sensitivity, observation, lineage, discovery/selection/sufficiency, package/Consumer, durable state/history, atomicity/failure, retry, recovery, observability/audit, testing, and deployment. No selected technology lacks a driver; no material upstream capability lacks an H mechanism/boundary. SQLite details, Git inventory/version, schema/indexes, CLI hierarchy, and similar details remain legitimate H3 deferrals. H21 introduces no technology or implementation authority.

## H22 — Integrated physical-architecture review

**H22: COMPLETE — PASS — PROJECT OWNER APPROVED.** The full chain is explicit Bootstrap → TOML → Project/Source → native Git → Markdown → Domain D → deterministic discovery/selection/sufficiency → Context Package/rendering → SQLite/audit/recovery, through CPython, Git, markdown-it-py, SQLite, pytest test environment, package/venv/CLI, and direct Linux.

The following seams passed: Bootstrap/Project configuration; configuration/Source Adapter; adapter/native Git; Git/Markdown Artifact; parser/Domain D; representation/discovery; discovery/package; package/rendering; application/core/SQLite; transaction boundary; SQLite configuration and schema evolution; Project isolation/one-DB topology; adapter-failure propagation; readiness; shutdown/recovery; backup/restore; logging/audit; packaging/deployment; direct-host/Source fidelity; testing; proving; replacement; Codex Class I boundary; and deferred-item review.

The review preserves: Source Adapter does not broaden Scope/register Sources/derive Authority; token is not Claim; no silent AI/vector addition; rendering cannot redefine Required Context; SQL/schema/errors stay in the adapter while core owns semantic identity/state/currentness; Git failure is not absence, parser limit is not Source absence, persistence failure is not success, and delivery failure is not construction failure. Startup distinguishes process health, Project readiness, and request readiness. Backup existence is not recovery proof. pytest can exercise temporary Bootstrap/TOML/Git/Markdown/SQLite/failure/recovery/security-negative fixtures.

MT-H19-01 is resolved/closed by explicit CLI Bootstrap supply; H20 adversarially validated it; H21 traced it to Domain B; H22 confirms startup/configuration/package/test/deployment integration. Remaining TOML fields, schema/IDs/indexes, SQLite PRAGMAs/connections/timeouts, Git inventory/minimum version, paths/schedules, CLI/log formats, retries, and compatible patch releases are Class I unless material.

Final findings: BLOCKER 0; MATERIAL 0; MINOR 0; unresolved prior findings 0; unresolved material technology/physical decisions 0; Domain-H implementation blockers 0. H22 introduces no technology and authorizes no implementation.

## Corrected closing result

**Domain H closes after H22, not H20.** Domain H — Technology Selection & v0.1 Physical Design is **COMPLETE — PROJECT OWNER APPROVED — PASS**. H1–H22 are complete; MT-H19-01 is resolved/closed; Domain I is not begun and I1 is next. The approved baseline is proportional, boundary-preserving, provider-independent, locally operable without mandatory runtime network, and consistent with Phase 0/1 and Domains A–G.
