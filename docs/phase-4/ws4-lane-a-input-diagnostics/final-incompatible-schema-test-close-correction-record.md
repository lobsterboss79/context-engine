# Final incompatible-schema test-owned close correction record

Status: **FROZEN BEFORE IMPLEMENTATION**

| Item | Frozen value |
| --- | --- |
| Branch / committed HEAD | `phase4-ws4-input-diagnostics-win` / `e95421b27ac01894c60abcdab5a54366c2e144c9` |
| Approved investigation | `remaining-incompatible-schema-test-handle-investigation.md` |
| WS3 test blob | `231e1ac53c3e1b05a37547e70ca836229aba1907` |
| WS4 test blob | `36c77ef2d88bb4054b3efaa00b14a808b7a269b1` |
| Scope | Exactly two direct, test-owned incompatible-schema setup connections; no application-source, assertion, fixture-content, input, expected-result, or test-selection change. |

The WS3 site is the setup connection in
`test_sqlite_rejects_incompatible_schema_and_preserves_project_isolation`.
The WS4 site is the setup connection in
`test_incompatible_lifecycle_schema_fails_closed`. Each creates only the
version-99 `schema_version` fixture and is owned by its test, not by
`SQLiteStateStore`.

The approved boundary is `contextlib.closing(sqlite3.connect(database))`
containing the existing `with connection` transaction context. This preserves
the existing commit/rollback boundary and schema contents, then deterministically
closes the test-owned connection before `SQLiteStateStore.initialize()` and
later unlink/fixture teardown. It is semantically neutral on Windows and
POSIX: it changes neither the incompatible-schema condition nor application
calls, expected exceptions, assertions, fixture contents, or test selection.

No other SQLite connection lifetime is in scope.
