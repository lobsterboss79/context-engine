# WS4 Shared Execution Contract

**Status:** **PRE-RESULTS CONTROL — FROZEN FOR LANE-SPECIFIC MATERIALIZATION**

## Common evidence and expected-result contract

Each lane-private ER, before execution, shall identify: controlled input and
fixture; approved governing basis; acceptance and negative criteria; scenario-
expected state; separate validation-control result criteria; known limitation;
and reviewer basis. A deliberate execution preserves, as applicable: exact Git
baseline; lane/control/ER/procedure identities and SHA-256 hashes; platform,
OS and runtime; controlled input hashes; injection and recovery boundaries;
stdout/stderr; raw state before/after; SQLite integrity/state; backup/restored
identity/hash; Provenance/audit/construction material; diagnostics; expected-
versus-observed comparison; result; Finding/H3 linkage; and raw-artifact
SHA-256 manifest. Artifacts irrelevant to an obligation are not required merely
for uniformity.

Original FAIL and INDETERMINATE evidence is immutable. An ER, control, fixture,
or procedure cannot be edited after execution to obtain PASS. A later result
is a separately identified, governed successor and does not rewrite its
predecessor.

## Platform and cross-machine contract

Lane A executes on Windows and records that environment. Lanes B/C execute on
the approved Linux runtime, LNX-01, and record its environment. Windows
evidence must not substitute for B/C runtime-sensitive claims. No additional
Linux corroboration of Lane A is required for current WS4 closure planning.

Before any worktree: Windows `main` commits and pushes this shared foundation.
Every branch is created from that exact committed commit; none begins from
uncommitted state. LNX-01 performs `git fetch`, verifies the exact commit, and
then creates its B/C branches. Each lane produces self-contained identifiable
commit(s); cross-machine copying does not substitute for Git lineage.

## Ownership, freeze, and vertical authority

Lane-private namespaces and evidence prefixes are defined in the package
README. During lane execution the following are read-only: AGENTS.md, README,
roadmap, checklist, WS1 package/registers, WS2/WS3 evidence and closure,
DVL/TD-14, shared WS4 package, source/application, tests, `pyproject.toml`,
existing evidence/findings, and every other lane namespace. A required change
is STOP AND PRESERVE.

After lane-specific authorization, a lane may proceed vertically through
analysis; evidence-reuse assessment; lane-private fixture/ER/control/procedure
preparation; pre-results freeze; provenance/static preflight; authorized
controlled execution; preservation; only a pre-frozen successor/recovery;
classification; bounded post-results review; and proposed lane disposition.
Finding creation follows WS1 but does not confer material disposition or
remediation authority.

## Injection and stop boundary

Injection is limited to deterministic, disposable lane-private boundaries:
Lane A fixture/input/configuration/Source; Lane B approved application/SQLite
persistence/interruption seam; Lane C disposable local/manual backup/restore
target and predetermined recovery seam. Host-wide disk or permission changes,
destructive user-data actions, arbitrary process killing, production data, and
external infrastructure failure are prohibited.

STOP AND PRESERVE for unexpected FAIL/INDETERMINATE; H3/material Finding;
semantic ambiguity/governance conflict; out-of-boundary failure; unpredetermined
recovery; evidence loss; remediation/source/test change; post-execution ER
revision; shared-file change; unresolved cross-lane dependency; platform
mismatch; prior-evidence invalidation; DVL/accepted-limitation decision; TD-14
threshold; or Gate/proving/readiness decision.
