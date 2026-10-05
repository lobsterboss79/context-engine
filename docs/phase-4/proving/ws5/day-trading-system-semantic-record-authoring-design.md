# Day Trading System Governed Semantic-Record Authoring Design

**Status:** **DESIGN COMPLETE — PROJECT OWNER AUTHORING DECISION REQUIRED**

**Scope:** Design only. No Project artifact, Consumer, WS5.5 successor, or
proving activity is created.

## Boundary, purpose, and location

This design uses only the eight Markdown Sources at Day Trading System revision
`653858dd9197f528ef0b323800d42892c7cfbf57` recorded in
[P4-I10-SELECT-001](day-trading-system-project-selection.md). It does not
alter them or expand their Source/ASU boundary.

Semantic records are maintained, machine-readable Project context: useful for
governed status/decision representation, provenance, authority/currentness
qualification, downstream context consumers, and later automation. They do not
replace governing Markdown or Project Owner authority. They are not
expected-answer fixtures and must exclude the WS6A task, P1–P8 matrix,
evaluator rubric, Consumer outputs, and proving analyses.

The proposed repository location is:

```text
docs/project/semantic-records/
```

It is version-controlled Project governance/context data, not application
source, tests, research results, or a Context Engine proving namespace. The
linked Markdown Source owner maintains grounding; the Project Owner approves
maintained status.

## Exact production format

Use one UTF-8 JSON object per atomic record, not a grouped manifest: the
implemented production loader accepts one record and has no manifest schema.
Use `sr-<source-identity>-<stable-topic>-v<record-version>.json`; names must
not encode a task, Consumer, test, or answer.

Each object uses the implemented contract exactly: `identity`, `version`,
`claim_identity`, `assertion_reference`, `project_identity`, `source_identity`,
`artifact_locator`, `source_revision`, `source_sha256`, `observation_identity`,
`block_ordinal`, `line_start`, `line_end`, and `authoring_process`. For
Markdown, the maintained block and lines must exactly match the transformation.
`classifications`, `limitations`, `authority_basis`, `currentness_basis`, and
`governance_basis` are the implemented optional fields; the maintained policy
requires applicable explicit bases and retained limitations.

The JSON byte SHA-256 is the implemented record hash. The contract has no
separate Claim-version/hash fields: record identity/version/hash plus
`claim_identity` is the supported binding. No second schema is authorized.

## Authority, atomicity, and coverage

The Project Owner is the approving authority. The future workflow is:

```text
Markdown Source -> proposed atomic JSON record -> literal grounding check
-> deterministic schema/provenance validation -> Owner approval -> maintained artifact
```

Codex may later mechanically draft only from the approved Sources. It may not
autonomously resolve meaning, Authority, currentness, supersession, conflict,
or limitations.

One record is one independently citable, Source-grounded assertion with one
primary Artifact/block: purpose, approved decision, phase/state, authorization
boundary, explicit constraint, known gap, deferred capability,
historical/superseded state, or provenance/authority fact. Prohibit task
synthesis, recommendations, inferred facts, unrepresented implementation or
trading claims, expected answers, and “the correct answer to WS6A is ...”.

The initial envelope is approximately **25–45 records**, based on Project
semantics rather than P1–P8: governance roles/boundaries (`AGENTS.md`);
purpose, research/risk principles, non-goals (overview); phase sequence/current
state (roadmap); historical Phase 1 and deferrals; Phase 2 completion and
non-authorities; PDR-016 current Phase 3 authority/non-authority; and durable
research/reproducibility governance. Do not convert every sentence, temporary
review detail, speculative detail, or unestablished fact. Duplicates use a
primary Source or preserved corroborating records; conflicts and historical/
current distinctions remain separate qualified records.

## Authority/currentness and change lifecycle

Records do not establish authority/currentness themselves. Bases must be
explicit: `AGENTS.md` for operating governance; overview/roadmap for current
Project context; PDR-016 for bounded Phase 3 authority; Phase 1 as
historical/superseded-as-current; Phase 2 exit as completed historical-status
evidence with current deferrals; research/reproducibility documents as current
governance. Unsupported classification is a validation failure or limitation,
not inference.

If a linked Markdown Artifact changes, revision/hash validation fails closed.
The owner reviews the changed block and bases, creates an incremented version
or successor, and retains the old record append-only as historical evidence.
Removed/superseded assertions retain reason and lineage. Missing, unparseable,
unauthorized, stale, or mismatched records produce no Claim.

## Context Engine ingestion

After separate authorization, normal production flow is: observe registered
Markdown Source; transform it; discover an explicitly allowlisted record; load
JSON; validate Project, Source, Artifact, revision/hash, observation, block,
and line bindings; emit existing Claim/RepresentedInformation; and persist
append-only Project-scoped semantic-record evidence in SQLite. Only validated
records enter unchanged discovery through WS9. No proving shortcut, Markdown
extraction, manual Consumer rendering, or stale-record fallback is allowed.

## Governance updates, review, and anti-leakage

Minimum later Project changes: a short `AGENTS.md` source-owner/Owner-approval
rule, a README/governance navigation entry, and a concise authoring guide for
the contract, review, versioning, stale-record, and anti-leakage rules. Do not
change application code, tests, research taxonomy, or unrelated documents.

Bounded Source-based batch review is permitted only if every candidate receives
literal-location, grounding, basis/limitation, deterministic-validation, and
explicit Owner-approval review. Batch approval cannot approve unreviewed files.
Inputs are restricted to the eight Project Sources, their observations, the
production contract, and Owner-approved Project procedure. Exclude all WS6A,
evaluator, proving-analysis, and Consumer material; record review inputs and
reject task/evaluator language.

## New revision, eligibility, and lineage

A legitimate new revision contains Owner-approved JSON records at the stated
path and the minimum governance documentation, with no Context Engine proving
evidence, task, rubric, package, or Consumer material. Before commit, verify
schema/provenance against exact Markdown bytes/locations; identity/version/hash
uniqueness; stale/supersession lineage; approvals; absence of secret/prohibited
content; and no application, test, or unrelated-Source change.

Later read-only eligibility must establish repository/branch/HEAD/worktree;
exact Source/record manifests and hashes; registration/disclosure basis;
maintenance approval/provenance; atomicity/anti-leakage; preserved
authority/currentness/limitations; unchanged scope; and production-path package
feasibility. Semantic records alone do not qualify a revision.

`P4-I10-SELECT-001` and `WS5.5-S-WS6A-002` remain immutable historical
evidence. A qualifying baseline is separately identified; only later Owner
authorization may create `WS5.5-S-WS6A-003`. Consumer 001 remains
invalid/discarded; Consumer 002 and a control Consumer remain uncreated.

## Exact next Project Owner decision

Decide whether to authorize bounded Day Trading System source-owner semantic-
record authoring under this design: this path, review authority, implemented
JSON contract, eight-Source scope, anti-leakage controls, and minimum Project
governance updates. It must not authorize successor/Consumer creation,
WS5.5/WS6 execution, Gate 4C, or production readiness.
