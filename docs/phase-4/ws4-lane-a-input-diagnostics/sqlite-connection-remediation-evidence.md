# SQLite application-connection remediation evidence

Status: **IMPLEMENTED — FOCUSED VALIDATION STOPPED ON REMAINING TEST-OWNED LOCKS**

## Implemented bounded change

Before-change `sqlite_state.py` Git blob:
`60809114b7aeb82f1f8c60fcc3d09b2db15a9671`.

After-change working-tree Git blob:
`2e948c02a2d2fea96c93e46ea5a38657dd7e468c`.

`src/context_engine/adapters/sqlite_state.py` now uses private managed
connection contexts. Each preserves the prior SQLite transaction context
(commit on normal exit and rollback on exception) and calls `close()` in a
`finally` block. The operational helper preserves `PRAGMA foreign_keys = ON`.
All adapter-owned operational, backup, backup-validation, restore, and staged
integrity-check connection paths were moved to those private contexts. No
public interface, schema, migration sequence, Project isolation query, or
error type was changed.

The frozen necessary lifecycle test was added only to
`tests/test_workstream_3.py` (after-change blob
`231e1ac53c3e1b05a37547e70ca836229aba1907`). It creates no test-owned SQLite
connection: it initializes and writes through `SQLiteStateStore`, unlinks the
database after the adapter calls return, and verifies deletion. Its purpose is
only the Owner-approved application-owned release expectation.

## Focused remediation validation

Using the established Windows venv and approved external regression-home write
context, the focused unchanged paths plus the new lifecycle test produced:

```text
7 passed, 2 errors in 0.47s
```

The following passed: direct application-owned release; successful persistence;
duplicate-write rollback; Project isolation/restart; persisted evidence reload
ordering; and full governed composition. This confirms transaction success,
rollback, persistence, and relevant application-owned release paths after the
change.

The only errors were teardown `WinError 32` for these tests:

- `test_lifecycle_schema_migrates_deterministically_from_version_one`
- `test_package_construction_schema_migration_and_duplicate_retry_are_explicit`

Both directly create their migration database with test-owned
`with sqlite3.connect(...) as connection` before calling the adapter. The
adapter-owned calls now close deterministically, but those direct test
connections remain without explicit close. Per the frozen stop condition, the
full Windows regression retest was not run and no test lifecycle change was
made.

No semantic control was rerun. VE-P4-4A-004 semantic PASS remains unchanged.
