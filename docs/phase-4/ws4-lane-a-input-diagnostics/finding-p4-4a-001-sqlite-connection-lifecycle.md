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
