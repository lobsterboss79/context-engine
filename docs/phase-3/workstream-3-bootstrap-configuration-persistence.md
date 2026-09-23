# Phase 3 Workstream 3 — Bootstrap, Configuration, and Persistence Foundation

**Status:** **COMPLETE — PROJECT OWNER APPROVED.** Items 3.1–3.10 are complete and their completion is Project Owner approved. Gate 3B is not reached or approved; Workstream 4 and later are not authorized; Phase 4 remains **NOT AUTHORIZED**.

## Implemented foundation

- `application.bootstrap` accepts only a deliberately supplied Bootstrap reference, requires an independently authorized invocation actor, parses TOML with `tomllib`, validates version/structure/scope, and fail-closes without implicit discovery.
- Bootstrap configuration is distinct from Project configuration. The latter is accepted only at the Bootstrap-established reference and only when its Project identity matches the Bootstrap.
- `adapters.sqlite_state` is the EB-03 SQLite adapter. It owns schema version 1, deterministic initialization, startup compatibility rejection, short per-operation transactions, Project-scoped evidence, and minimized Project-scoped audit rows. SQLite row IDs are not semantic identities.
- Restored evidence is explicitly historical with `currentness="unknown"` and no Authority basis. Audit is distinct from diagnostic logging; audit reads are authorization-bound. Apparent secret values are rejected from durable evidence/audit values.

## Deferred behavior and limits

No Bootstrap CLI command, authentication/IAM, cryptographic trust, Source lifecycle, configuration writer, Project/Source traversal, persistence of the full semantic graph, backup/restore workflow, rendering, discovery, selection, sufficiency, or Workstream 4+ behavior is implemented. The application boundary accepts authorized-operator status from a future authorized invocation/authentication boundary; it does not invent one.

## Traceability and validation

| Concern | Implementation | Governing record | Evidence |
| --- | --- | --- |
| Root legitimacy / explicit reference | `establish_bootstrap` | Domain I I15; Domain H H19–H20; Phase 3 3.1–3.2 | missing, unauthorized, malformed, unsupported tests |
| Bootstrap != Project config | `load_project_configuration` | Domain B B5–B6; Domain H TD-03/H22 | substitute/mismatched configuration tests |
| SQLite schema/migrations | `SQLiteStateStore.initialize` | Domain G G6/G12–G14; Domain H H18 | initialization/incompatible schema tests |
| Isolation / transaction / audit | Project-scoped SQL and transactions | Domain G ST-06/ST-12/ST-13; G6/G11 | duplicate rollback, Project isolation, audit authorization tests |
| Restoration / secret exclusion | `PersistedEvidence`, secret rejection | Domain G ST-03/ST-11; G8–G9 | restored unknown/no Authority; secret rejection tests |

Full pytest result: **30 passed**. No dependency, framework, or plugin was introduced.
