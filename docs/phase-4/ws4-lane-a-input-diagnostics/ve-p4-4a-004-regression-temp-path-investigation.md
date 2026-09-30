# VE-P4-4A-004 regression temp-path investigation

Status: **INVESTIGATION COMPLETE — PROJECT OWNER REGRESSION TEMP-PATH DISPOSITION REQUIRED**

## Baseline and preserved result

Investigation baseline: `9b8481f54b7817a74e7d8dd7bd3818bdad4ebee3`
(`Preserve Phase 4 input diagnostics validation`) on
`phase4-ws4-input-diagnostics-win`.

VE-P4-4A-004's portable preflight and frozen semantic control remain preserved
as PASS.  The semantic evidence establishes the Lane A cases, the four-state
distinction, diagnostics, and bounded partial-qualification preservation.  The
focused regression did not establish a semantic or product failure: it stopped
in test fixture setup with `43 passed, 17 errors in 0.48s`.

## Exact failure and path derivation

Each selected test module defines a local `controlled_dir` fixture that calls:

```python
tempfile.mkdtemp(dir=Path.home() / "temp", prefix="context-engine-ws…-")
```

The selected modules and fixture locations are:

| Module | Fixture line | Prefix |
| --- | ---: | --- |
| `tests/test_workstream_3.py` | 18 | `context-engine-ws3-` |
| `tests/test_workstream_4.py` | 30 | `context-engine-ws4-` |
| `tests/test_workstream_6.py` | 29 | `context-engine-ws6-` |
| `tests/test_workstream_8.py` | 24 | `context-engine-ws8-` |
| `tests/test_workstream_9.py` | 34 | `context-engine-ws9-` |

`mkdtemp` creates a uniquely named child directory but does not create its
explicit parent.  All 17 errors therefore occurred before a test body when it
tried to create a child below the missing parent
`C:\Users\talbo\temp`.

The process and external validation interpreter both recorded:

```text
HOME=C:\Users\talbo
USERPROFILE=C:\Users\talbo
HOMEDRIVE=C:
HOMEPATH=\Users\talbo
TEMP=C:\Users\talbo\AppData\Local\Temp
TMP=C:\Users\talbo\AppData\Local\Temp
TMPDIR=C:\Users\talbo\AppData\Local\Temp
Path.home()=C:\Users\talbo
```

On this CPython 3.14 Windows runtime, `ntpath.expanduser` (and therefore
`Path.home`) first uses `USERPROFILE`; only if it is absent does it use
`HOMEDRIVE` plus `HOMEPATH`.  `HOME`, `TEMP`, `TMP`, and `TMPDIR` do not select
this fixture's explicit `Path.home() / "temp"` parent.  Thus the path came from
the fixture's `Path.home()` expression and `USERPROFILE`, not from `tempfile`'s
normal temporary-directory selection, pytest's `tmp_path`, application code,
or a repository helper.

The repository has the same explicit fixture pattern in Workstreams 5 and 10.
Prior Linux Phase 4 evidence shows it was made usable through a process-scoped
`HOME=/tmp` invocation, which is compatible with that platform's home-path
resolution but is not the portable Windows mechanism.

## Classification and application involvement

**Root-cause classification: F — MULTIPLE / COMPOUND ISSUE.**

1. **B — test fixture/test-harness portability defect:** the tests select an
   explicit, host-home-relative parent and assume it already exists instead of
   using pytest's managed temporary fixtures or creating the parent.
2. **C — validation-environment configuration deficiency:** the Windows
   regression process did not supply a dedicated existing home-relative `temp`
   parent compatible with that fixture contract.

This is not an application/product defect.  Read-only source inspection found
no `Path.home`, `expanduser`, `USERPROFILE`, `HOME`, `TEMP`, `TMP`, or `TMPDIR`
use in `src/`; its only `tempfile` use stages beside an already-selected SQLite
database parent.  The application never executed before the fixture errors.

Windows is material only to the path-resolution mechanism: Windows CPython
prefers `USERPROFILE`, whereas the prior Linux process-scoped `HOME` convention
could redirect `Path.home()`.  The failed condition is not a Lane A semantic
or product-platform difference.

## Project convention and Z:\\temp compatibility

The governing architecture treats temporary paths as ordinary physical detail
while requiring governed temporary state, explicit environment assumptions,
and relocation-stable semantics.  This test workspace is disposable test
infrastructure; it is outside governed application semantics.  No repository
instruction requires this fixture workspace to be beneath the actual Windows
profile.

`Z:\temp` is compatible: these fixtures only create and remove unique child
directories below their supplied parent.  They do not inspect the user's real
profile, require an absolute `C:` path, or use the selected workspace as a
semantic application input.

## Options assessed

| Option | Assessment |
| --- | --- |
| 1. Create `C:\Users\talbo\temp` | Would satisfy the immediate parent prerequisite, but modifies the user-profile environment and does not follow the Owner's preferred `Z:\temp` location. Not recommended. |
| 2. Set `HOME`, `TEMP`, `TMP`, or `TMPDIR` only | Insufficient on this Windows runtime: the fixture uses `Path.home()` and Windows resolves it from `USERPROFILE` while present. |
| 3. Dedicated external regression home below `Z:\temp`, with process-scoped `USERPROFILE` | Sufficient and recommended.  Create an existing `...\temp` child, then set `USERPROFILE` only for the regression process.  This leaves global environment settings and tests/source unchanged. |
| 4. Change test harness | Not required to satisfy the present regression prerequisite.  It may be a later portability improvement, but is outside this Lane A authorization. |

The recommended minimum external layout is:

```text
Z:\temp\context-engine-phase4-regression-home\temp
```

For one future authorized regression process only, set:

```text
USERPROFILE=Z:\temp\context-engine-phase4-regression-home
```

`HOMEDRIVE` and `HOMEPATH` need not change because `USERPROFILE` is the active
Windows resolution input.  `HOME`, `TEMP`, `TMP`, and `TMPDIR` need not change.
This is a process-scoped test-environment configuration, not a test/source
change.  The parent must be created before invocation because `mkdtemp` creates
only its unique children.

## Evidence and continuation impact

The VE-P4-4A-004 semantic PASS remains valid and immutable.  The unresolved
regression is a separate infrastructure result and prevents Lane A completion,
but does not reinterpret the semantic result.  After the Owner authorizes only
the external directory creation and the frozen regression invocation with the
documented process-scoped `USERPROFILE`, the same regression slice may be run
once as continuation of the existing regression requirement.  No semantic
control needs rerunning and no new VE identity is required for that regression
continuation.

No Finding, Material Finding, or H3 is recommended: the evidence supports a
test/validation-infrastructure portability and configuration condition, not a
product discrepancy.  Lane A obligations remain semantically evidenced by
004 but cannot receive final closure classification until the required
regression succeeds.  Lane B/C are unaffected.  Item 4.7 has no interaction.

## Project Owner decision required

Authorize the following bounded external test-infrastructure continuation:

1. create `Z:\temp\context-engine-phase4-regression-home\temp` outside all
   worktrees;
2. run the already-frozen focused Lane A regression exactly once using the
   established external validation interpreter and a regression-process-only
   `USERPROFILE=Z:\temp\context-engine-phase4-regression-home`;
3. preserve environment, invocation, output, exit status, and result; and
4. perform the already-authorized bounded post-results review only if that
   regression passes.

Do not authorize source/test changes, semantic rerun, or a new VE successor as
part of this decision.
