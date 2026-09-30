# Remaining test-owned SQLite handle investigation

Status: **INVESTIGATION COMPLETE — PROJECT OWNER TEST-LIFECYCLE / REGRESSION DISPOSITION REQUIRED**

## Baseline and finding state

Baseline: committed `36b73316c9ca736e4d25298eb5a066747519bb2b`
(`Remediate SQLite connection lifecycle`) on
`phase4-ws4-input-diagnostics-win`.

F-P4-4A-001 remains open: it concerns only deterministic release of
application-owned `SQLiteStateStore` connections. The committed remediation
uses `_connection` and `_managed_sqlite_connection`, each of which wraps the
existing transaction context and calls `connection.close()` in `finally`.
No adapter method returns or retains a connection. VE-P4-4A-004 semantic PASS
is unchanged.

## Exact remaining cases

### WS4 migration — classification A

`tests/test_workstream_4.py::test_lifecycle_schema_migrates_deterministically_from_version_one`
uses `version-one.sqlite`.

1. The **test** opens `sqlite3.connect(database)` to create a version-one
   schema and commits through `with connection`; that context does not close
   the test-owned connection.
2. `SQLiteStateStore(database).initialize()` opens the application connection
   through `_connection`; on normal migration completion it commits and closes
   before returning.
3. The **test** opens a second `sqlite3.connect(database)` for schema-version
   and table readback. It exits its transaction context but remains bound to
   the local variable `connection` through the end of the test function.
4. The semantic migration assertions pass. Fixture teardown then calls
   `shutil.rmtree`, which reaches `os.unlink(version-one.sqlite)` and receives
   `WinError 32`.

The second test-owned readback connection is the remaining concrete live-handle
candidate. No application connection remains after `initialize()` returns.

### WS8 migration/duplicate retry — classification A

`tests/test_workstream_8.py::test_package_construction_schema_migration_and_duplicate_retry_are_explicit`
uses `version-three.sqlite`.

1. The **test** opens `sqlite3.connect(database)` to create and commit schema
   version three. It has no explicit close and remains bound to local
   `connection` through the test function.
2. `store.initialize()`, `persist_construction`, the expected duplicate-write
   exception, and `package_constructions_for_project` all use application
   `_connection` contexts. They respectively close after success and, for the
   duplicate insertion, close in `finally` after rollback/exception.
3. The duplicate-retry and count assertion pass. Fixture teardown then reaches
   `os.unlink(version-three.sqlite)` through `shutil.rmtree` and receives
   `WinError 32`.

The setup connection is test-owned and is the remaining concrete live-handle
candidate. No application connection is intentionally returned or retained.

## Determination

Both cases are **A — TEST-OWNED CONNECTION NOT EXPLICITLY CLOSED**. The prior
application resource defect is not the remaining cause: normal and exception
adapter paths in these exact tests traverse the committed managed contexts and
close before return. The fixture owns directories only, not SQLite handles.

The test connections exist only to seed a legacy schema or inspect migrated
schema state. Retaining them through teardown has no test semantic purpose.
An explicit test-owned close would not alter test inputs, migration behavior,
expected application result, assertion set, Project isolation, or duplicate
rollback behavior. It is a cross-platform test resource-lifecycle correction:
POSIX may permit unlink of a still-open file, but deterministic close is
appropriate on both Windows and Linux. Sleeps, retries, forced GC, conditional
Windows branches, or altered unlink behavior are neither needed nor
recommended.

## Exact proposed test-only correction

If separately authorized, replace each test-owned pattern:

```python
with sqlite3.connect(database) as connection:
    ...
```

with a local `try`/`finally` boundary that retains the existing transaction
context and closes the same test-created connection:

```python
connection = sqlite3.connect(database)
try:
    with connection:
        ...
finally:
    connection.close()
```

Apply this only to the two direct connection blocks in the WS4 migration test
and the one direct connection block in the WS8 migration test. Do not change
assertions, inputs, fixtures, source, test selection, or application behavior.

## Finding, regression, and lane impact

The two test-owned handles are outside F-P4-4A-001's product scope. They do,
however, prevent the Windows regression evidence required to support the
Finding's closure and Lane A's bounded post-results review. After the proposed
test-only correction is frozen and applied under separate Owner authorization,
the same focused Windows regression is eligible for one continuation; no Lane
A semantic control need rerun.

F-P4-4A-001 closure still requires successful focused lifecycle validation,
sufficient Windows regression evidence without application-owned handle
retention, and a separate Owner closure disposition.

Lane A remains semantically evidenced but not finalizable. Lane B's historic
semantic evidence remains valid: the adapter remediation changes only resource
lifetime and no frozen Lane B semantic expectation. The minimum future Lane B
treatment is bounded post-remediation adapter regression corroboration during
integration, not direct re-execution of Lane B semantic controls unless later
evidence contradicts this conclusion. Lane C is unaffected. Item 4.7 has no
interaction.

## Project Owner decision required

Authorize the exact three test-owned connection close boundaries described
above, then a separately frozen continuation of the unchanged focused Windows
regression under the established external environment and bounded write path.
Do not authorize semantic rerun, further source change, Finding closure, or
cross-lane execution in that decision.
