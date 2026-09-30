# VE-P4-4A-004 Windows SQLite file-lock investigation

Status: **INVESTIGATION COMPLETE — PROJECT OWNER REGRESSION / SQLITE-LIFECYCLE DISPOSITION REQUIRED**

## Baseline and preserved semantic evidence

Investigation baseline is committed `bd5e99984c458634386d3fb9cabbdd9800410fe9`
on `phase4-ws4-input-diagnostics-win`.  VE-P4-4A-004 remains an immutable
semantic PASS: its portable preflight, partial-evidence qualification,
Candidate/Context Item/Manifest/rendered preservation, authority-zero,
insufficiency, 4.1-A–D, four-state distinction, and 4.6-B evidence are not
affected by this investigation.

The separately preserved v2 focused regression ran once with the approved
external-write context and reported **59 passed, 1 failed, 13 errors**.  Its
external-write preflight passed.  No semantic control was rerun.

## Non-passing inventory

All thirteen errors occurred in fixture teardown, after their test bodies had
returned; therefore their body assertions completed.  Each fixture calls
`shutil.rmtree(controlled_dir)`, which reached `os.unlink` for a SQLite file and
received `PermissionError: [WinError 32]`.

| Test | Phase / operation | Database |
| --- | --- | --- |
| WS3 `test_sqlite_initializes_and_restores_historical_evidence_without_elevation` | teardown / `shutil.rmtree` -> `os.unlink` | `state.sqlite` |
| WS3 `test_sqlite_rejects_incompatible_schema_and_preserves_project_isolation` | teardown / `shutil.rmtree` -> `os.unlink` | `state.sqlite` |
| WS3 `test_sqlite_transaction_rolls_back_duplicate_partial_state` | teardown / `shutil.rmtree` -> `os.unlink` | `state.sqlite` |
| WS3 `test_audit_is_durable_authorization_bound_and_secret_safe` | teardown / `shutil.rmtree` -> `os.unlink` | `state.sqlite` |
| WS4 `test_lifecycle_persists_and_restarts_with_project_isolation` | teardown / `shutil.rmtree` -> `os.unlink` | `state.sqlite` |
| WS4 `test_source_registration_row_id_is_not_semantic_identity_or_cross_project_key` | teardown / `shutil.rmtree` -> `os.unlink` | `state.sqlite` |
| WS4 `test_lifecycle_schema_migrates_deterministically_from_version_one` | teardown / `shutil.rmtree` -> `os.unlink` | `version-one.sqlite` |
| WS4 `test_duplicate_lifecycle_write_rolls_back_without_partial_state` | teardown / `shutil.rmtree` -> `os.unlink` | `state.sqlite` |
| WS4 `test_incompatible_lifecycle_schema_fails_closed` | teardown / `shutil.rmtree` -> `os.unlink` | `incompatible.sqlite` |
| WS6 `test_persisted_evidence_order_is_semantic_not_sqlite_row_order` | teardown / `shutil.rmtree` -> `os.unlink` | `state.sqlite` |
| WS8 `test_denied_construction_is_not_fake_empty_package_and_persistence_is_historical` | teardown / `shutil.rmtree` -> `os.unlink` | `state.sqlite` |
| WS8 `test_package_construction_schema_migration_and_duplicate_retry_are_explicit` | teardown / `shutil.rmtree` -> `os.unlink` | `version-three.sqlite` |
| WS9 `test_controlled_full_application_composition_and_durable_audit` | teardown / `shutil.rmtree` -> `os.unlink` | `state.sqlite` |

The one pytest **FAIL** is WS3
`test_sqlite_rejects_incompatible_schema_and_preserves_project_isolation` at
its direct `database.unlink()` immediately after the expected
`StateCompatibilityError` from `SQLiteStateStore(database).initialize()`.
That expected exception assertion passed.  No `assert` expression failed; the
later Project-isolation steps did not run because the direct file-unlink
operation received the same `WinError 32`.

Thus all fourteen non-passing outcomes share one common mechanism: Windows
refused deletion of a SQLite database that a still-live native handle had not
released.  The output establishes neither an incorrect governed semantic
assertion nor a Lane A semantic discrepancy.

## Handle-ownership trace

`SQLiteStateStore._connect` creates every adapter connection with
`sqlite3.connect(self._database)` (adapter lines 131–134).  Its public
operations—including `initialize`, persistence writes, reloads, audit reads,
backup validation, and recovery qualification—use `with self._connect() as
connection` but have no `finally: connection.close()` and expose no adapter
`close()` lifecycle method.

The local CPython 3.14 `sqlite3.Connection.__exit__` contract confirms that
context-manager exit commits on success or rolls back on exception; it does
not state that it closes the connection.  Consequently these operations have
short transaction scope, but do not establish deterministic native-handle
release.  Normal local-object destruction may release a handle; exception
tracebacks, retained exception state, or other references can extend that
lifetime.  The incompatible-schema failure is the clearest application-owned
path: the adapter opens the connection, raises from `initialize`, and the test
then immediately tries to unlink the same database.

Tests also directly create SQLite connections with the same non-closing
context-manager pattern, notably the WS3 incompatible-schema setup, WS4
migration/incompatible-schema setup and readback, and WS8 migration setup.
The test fixture itself owns only the temporary directory and invokes
`shutil.rmtree`; it does not open database connections.  The affected normal
operation tests additionally use `SQLiteStateStore`, so they contain
application-owned connection paths even when they do not directly call
`sqlite3.connect`.

Static inspection cannot attribute each individual native handle after the
now-completed process has exited.  It does establish the following ownership
classification:

| Owner | Evidence | Assessment |
| --- | --- | --- |
| Application | `_connect` plus every adapter operation | Confirmed connection creator; no explicit deterministic close path. |
| Test | Explicit `sqlite3.connect` in selected WS3/WS4/WS8 cases | Confirmed additional connection creator; likewise no explicit close. |
| Fixture | `mkdtemp`/`rmtree` only | Not a SQLite-handle creator. |
| Python/SQLite runtime | Windows `WinError 32` exposes unreleased handles | Enforces deletion sharing rules; not shown to originate a handle. |
| Exact live owner of each final handle | No live-process diagnostic was authorized or available | Unknown per path; mixed creation paths prevent sole-owner attribution. |

## Architecture and platform analysis

The approved persistence description assigns `SQLiteStateStore` deterministic
initialization, startup compatibility rejection, and **short per-operation
transactions**.  Runtime architecture requires honest clean shutdown and
governed temporary state, but it does not prescribe a public adapter `close()`
API, a specific Python connection-management idiom, or Windows file-unlink
behavior.  It would therefore be unsound to invent an immediate-close
requirement solely to make this regression pass.  Nonetheless, the source
does not itself guarantee release of the application-created handles before a
caller deletes the database.

On POSIX, unlinking a pathname can succeed while a process retains the open
file; the existing Linux-oriented fixture cleanup may therefore mask this
lifetime issue.  Windows deletion sharing instead rejects removal of an open
SQLite file.  This conclusion follows from the observed paths plus the actual
source lifecycle above; it is not merely a generic platform assertion.

The 59 passing tests show that the focused slice executed meaningful Windows
application paths and that the external-write prerequisite was resolved.  They
do not show full regression success, and cannot prove all SQLite handles were
released.  The errors are concentrated in paths that exercise persistence and
then remove their disposable database.

## Platform and Linux-regression treatment

The shared WS4 execution contract assigns Lane A to Windows and explicitly
states that **no additional Linux corroboration of Lane A is required for
current WS4 closure planning**.  The topology assigns Linux runtime-sensitive
SQLite persistence/recovery claims to Lanes B/C.  Accordingly, a Linux run is
not required to replace VE-P4-4A-004's Windows semantic evidence.

The same frozen slice could be valid **supporting implementation-regression
evidence** on LNX-01 only after that environment verifies the exact committed
baseline and test hashes, its established interpreter provenance, and the
frozen invocation.  Prior Linux Phase 4 evidence records passing unchanged
suites under CPython 3.14.4 / pytest 9.1.1.  Such a run could corroborate that
the unchanged source/test baseline still passes in the approved runtime, but
would not resolve the Windows handle-lifecycle behavior and must not be used
to conceal a Windows application resource-release defect.  It is therefore
not recommended without a separate Owner platform/regression disposition.

## Classification, impact, and options

**Root-cause classification: G — MULTIPLE / COMPOUND ISSUE.**  The evidence
confirms application-created connections without explicit close and
test-created connections with the same lifecycle pattern; Windows exposes the
combined cleanup condition.  It does not prove a sole native-handle owner for
all fourteen paths.

**Product-defect determination:** no confirmed governed product Finding yet.
There is a concrete implementation-level resource-lifecycle deficiency to
evaluate: application operations do not deterministically close their own
connections.  Whether that violates the approved v0.1 lifecycle contract, and
whether remediation is warranted, is a Project Owner decision because the
governing architecture does not specify this physical lifecycle detail.  No
material Finding or H3 is recommended at this point.

VE-P4-4A-004 remains valid direct semantic evidence.  Obligations 4.1-A,
4.1-B, 4.1-C, 4.1-D, and 4.6-B remain directly semantically validated by its
PASS, but their Lane A final classification remains pending the Owner's
required regression disposition.  Lane B/C are not invalidated: their
Linux-based SQLite persistence/recovery evidence concerns different assigned
runtime claims.  Item 4.7 has no interaction.

| Option | Assessment |
| --- | --- |
| 1. Confirmed POSIX-only fixture issue; use Linux regression | Not supported alone: adapter-created handles lack explicit close, so it cannot resolve Windows ownership. |
| 2. Confirmed application-owned leak; Finding/remediate | Plausible but not yet conclusively governed; requires Owner determination of lifecycle requirement and remedy scope. |
| 3. Confirmed test-only lifecycle issue | Not supported alone because adapter creates connections in every affected persistence path without explicit close. |
| 4. Windows behavior material | Supported as a portability/resource-lifecycle concern; Lane A semantic evidence remains valid, but regression disposition is required. |
| 5. Architecture ambiguity | Applicable to whether the observed implementation deficiency is a governed product Finding, not to the observed Windows locks themselves. |

### Recommended minimum next action

Project Owner should decide whether deterministic closure of every
application-owned SQLite connection is an approved v0.1 lifecycle expectation.
If yes, create a governed product Finding and authorize separately scoped
remediation/test changes before any retest.  If no, decide explicitly whether
to treat the Windows cleanup outcome as a test-portability limitation and
authorize an exact-baseline LNX-01 supporting regression; that Linux result
cannot rewrite or replace the preserved Windows result.

No remediation, Linux execution, Finding creation, or further regression is
authorized by this investigation.
