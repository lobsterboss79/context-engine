# SQLite application-connection remediation design

Status: **FROZEN BEFORE IMPLEMENTATION — OWNER-AUTHORIZED SCOPED REMEDIATION**

## Finding basis and scope

Finding candidate scope: application-owned SQLite connections created by
`SQLiteStateStore` lack established deterministic close/release semantics.
The Owner has approved deterministic release of these application-owned
resources as a v0.1 lifecycle expectation. Test-created SQLite connections
are expressly outside this remediation.

Before-change source identity:

```text
src/context_engine/adapters/sqlite_state.py
Git blob: 60809114b7aeb82f1f8c60fcc3d09b2db15a9671
```

## Affected application paths

`SQLiteStateStore._connect()` creates operational database connections. All of
the following currently use `with self._connect()` and need deterministic
release after their existing transaction scope: initialization/migration,
evidence, source-registration, audit, observation, artifact, transformation,
representation, package-construction writes and reads, operational validation,
and recovery-qualification reads.

The adapter also directly creates application-owned connections in backup and
restore paths: backup target; read-only backup validation; restore source and
staging target; and staged integrity check. These are in scope because their
handles may otherwise outlive the transaction and interfere with
staging/replacement cleanup.

No caller intentionally receives or retains an adapter connection: public
methods expose value records and exceptions only. `SQLiteStateStore` retains
only its database `Path`, not a connection. No public lifecycle API is needed.

## Minimum implementation

Introduce private context-manager helpers in `sqlite_state.py` that:

1. obtain a connection;
2. preserve the existing connection context-manager transaction behavior
   (commit on normal exit; rollback on exception);
3. call `connection.close()` in `finally`, including exception paths.

One helper will wrap `self._connect()` for operational state, retaining the
existing `PRAGMA foreign_keys = ON`. A second private helper will wrap direct
adapter-owned `sqlite3.connect(..., uri=...)` calls. Replace only the current
adapter-owned connection contexts with those helpers.

The close boundary is after the existing `with connection` block completes,
not before reads/writes, migration loops, backup transfer, integrity checks,
or transaction outcome is resolved. The `finally` close executes after commit
or rollback and before a method returns or propagates its exception. This
preserves transaction, rollback, migration, Project isolation, backup, restore,
and error semantics while making resource release deterministic.

## Validation design

Run unchanged focused persistence tests for WS3, WS4, WS6, WS8, and WS9. They
cover success, duplicate-write rollback, migration, persistence/reload, audit,
Project isolation, package construction, and composition.

A new narrow existing-test-family regression is necessary because the prior
fixture teardown failures mix application and test-owned handles. Its frozen
purpose is limited to proving the approved application lifecycle expectation:
after successful `SQLiteStateStore` initialization and an adapter-owned write
return, a test can unlink the database without retaining any test-created
SQLite connection. It will be added only to `tests/test_workstream_3.py` and
will make no semantic assertion beyond deterministic release; it will use the
existing `controlled_dir` fixture and no new dependency or helper.

Stop if the private-helper design would require public API change, changes a
transaction/error semantic, reveals a remaining application-owned lock, or
requires test changes beyond the frozen narrow lifecycle test.
