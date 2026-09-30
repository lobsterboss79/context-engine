# F-P4-4A-001 — Application-owned SQLite connection lifecycle

| Field | Record value |
| --- | --- |
| Finding ID | `F-P4-4A-001` |
| Linked evidence/result | VE-P4-4A-004 semantic PASS; Windows focused regression v2 `59 passed, 1 failed, 13 errors`; Windows SQLite-lock investigation |
| Concise finding | `SQLiteStateStore` application-owned connections did not have established deterministic close/release semantics. |
| Severity | **MINOR** — implementation/resource-lifecycle defect; it did not alter Lane A semantic outcomes, but prevented Windows persistence-test cleanup. |
| Primary finding type | **IMPLEMENTATION** |
| Secondary type | Operational portability |
| Owner/investigator | Project Owner / Codex scoped remediation |
| Cause analysis | Adapter operations used SQLite connection context managers that commit/roll back but do not close. Test-created connections were a separate, mixed contributor to some observed locks. |
| Status/lifecycle | **REMEDIATION IMPLEMENTED — FOCUSED VALIDATION PARTIAL; OWNER RETEST/CLOSURE DISPOSITION REQUIRED** |
| Governed disposition | Project Owner authorized deterministic close for application-owned connections only. |
| Remediation authorization | Current Project Owner SQLite lifecycle disposition. |
| Remediation evidence | `sqlite-connection-remediation-design.md`; `sqlite-connection-remediation-evidence.md` |
| Residual limitation | Two migration-fixture teardown locks remain where tests directly create SQLite connections; no further application remediation is authorized. |
| Closure evidence | Not sufficient. The full frozen Windows regression was not rerun after focused validation stopped on the remaining test-owned locks. |

The finding does not assert that every observed Windows lock was application
caused, that tests/SQLite/Windows are defective, or that VE-P4-4A-004 semantic
validation failed. H3 is not triggered.

## Additive closure record

| Field | Project Owner approved closure value |
| --- | --- |
| Closure date | 2026-09-30 |
| Status/lifecycle | **CLOSED — PROJECT OWNER APPROVED** |
| Original finding/scope | Application-owned SQLiteStateStore connections lacked deterministic close/release semantics; test-owned connections were expressly outside the product Finding scope. |
| Remediation | Private managed application connection contexts preserve transaction commit/rollback and call close in finally across operational, backup, validation, restore, and staged-check paths. |
| Focused validation | Lifecycle, incompatible-schema migration, and persistence paths passed after remediation; residual test-owned lifetimes were separately corrected without application-semantic change. |
| Final regression evidence | Frozen Windows WS3/WS4/WS6/WS8/WS9 regression continuation v4: **61 passed, 0 failed, 0 errors, 0 skipped**. |
| Closure basis | No evidence remains of application-owned SQLite handle retention within the validated scope. |

This closure is additive. The original Finding, its mixed-handle qualification,
all investigations, remediation records, and earlier partial/indeterminate
regression attempts remain preserved above and in their respective records.
