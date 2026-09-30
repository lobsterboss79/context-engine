# Remaining incompatible-schema test-handle investigation

Status: **INVESTIGATION COMPLETE — PROJECT OWNER FINAL TEST-LIFECYCLE / REGRESSION DISPOSITION REQUIRED**

Baseline: `28ea004559ffcbd581b60be172c9f66652a4a99b`. Frozen v3 result: **60 passed, 1 failed, 2 errors**. VE-P4-4A-004 remains semantic PASS and F-P4-4A-001 remains OPEN.

## WS3 — classification A

`test_sqlite_rejects_incompatible_schema_and_preserves_project_isolation` creates `state.sqlite` through the direct test-owned `with sqlite3.connect(database) as connection` setup block, executing only the version-99 table/create and insert. That context commits but does not explicitly close, so its test-local reference persists to the later application call and `database.unlink()`.

`SQLiteStateStore(database).initialize()` then opens an application connection through remediated `_connection`. Its version-99 check raises `StateCompatibilityError`; `_connection` closes in `finally` while the expected exception propagates, returns no connection, and retains none. The expected exception assertion passed before the test's direct `database.unlink()` raised `WinError 32`; Project-isolation steps did not execute and teardown retried removal.

**Classification: A — TEST-OWNED CONNECTION NOT EXPLICITLY CLOSED.** Future correction: wrap only this existing setup connection in `contextlib.closing` while retaining its inner transaction context. It closes after fixture seeding and before application invocation/unlink.

## WS4 — classification A

`test_incompatible_lifecycle_schema_fails_closed` creates `incompatible.sqlite` through one direct test-owned `with sqlite3.connect(database) as connection` setup block, executing only the version-99 table/create and insert. It commits but has no explicit close, so it remains test-local through fixture teardown.

The following `SQLiteStateStore(database).initialize()` uses remediated `_connection`; it raises the expected `StateCompatibilityError` and closes its application connection in `finally`, returning and retaining none. The expected exception assertion completed successfully; teardown `shutil.rmtree` then reached `os.unlink` and received `WinError 32` from the test-owned setup handle.

**Classification: A — TEST-OWNED CONNECTION NOT EXPLICITLY CLOSED.** Future correction: wrap only this existing setup connection in `contextlib.closing` while retaining its inner transaction context. It closes after fixture seeding and before application invocation.

## Determinations and decision

Both corrections are semantically neutral and cross-platform: schema contents, application invocation, expected exception behavior, assertions, and fixture meaning stay unchanged. No platform branch, sleep, retry, forced GC, or cleanup workaround is appropriate. The prior three corrections remain narrow and neutral; their focused validation passed.

These two handles are outside F-P4-4A-001, but block the full Windows regression needed for Finding closure evidence. After separately authorized exact corrections, the unchanged five-module slice is eligible for one final continuation; no Lane A semantic rerun is needed. F-P4-4A-001 requires sustained remediation validation, successful full frozen regression without application-owned retention, and a separate Owner closure disposition before it can be a closure candidate.

Lane A is otherwise blocked only by regression completion and Finding disposition; its direct semantic evidence remains PASS. Lane B historical evidence remains valid; future integration needs bounded adapter-regression corroboration covering initialization/migration, rollback, persistence/reload, and backup/restore paths, not a direct Lane B semantic rerun. Lane C is unaffected. Item 4.7 has no interaction.

Project Owner decision required: authorize only the two described test-owned setup-connection close boundaries, then one separately frozen continuation of the unchanged Windows regression. Do not authorize semantic rerun, source change, Finding closure, or cross-lane work.
