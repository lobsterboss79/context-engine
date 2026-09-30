# VE-P4-4B-002 Regression-Environment Investigation

**Status:** **INVESTIGATION COMPLETE — PROJECT OWNER REGRESSION-ENVIRONMENT DISPOSITION REQUIRED**

## Boundary and committed state

This investigation did not run regression, semantic controls, or migration; install packages; create environments; alter frozen/evidence artifacts; or modify source, tests, shared material, Lane A/C, or Item 4.7. The committed Lane B sequence baseline is `01eb85c20daed3efcc6c70e4c92c0e9e87432514` (`Preserve Phase 4 persistence validation sequence`). The semantic `VE-P4-4B-002` predecessor, `VE-P4-4B-002-S1` successor, and `VE-P4-4B-002-M1` migration observations remain preserved and valid as observed; their regression requirement remains incomplete.

## Classification

**F — MULTIPLE / COMPOUND ISSUE.** The attempted system interpreter was CPython 3.14.4, which is the approved project runtime version, but it lacks the optional development dependency `pytest`. An already-existing, previously validated, isolated CPython 3.14.4 environment with pytest 9.1.1 is available. Thus this is both a wrong-interpreter selection for regression (A) and an expected dev-dependency absence in the system interpreter (B), not a Python 3.14 compatibility problem.

## Current and available environments

| Environment | Observed state | Suitability |
| --- | --- | --- |
| `/usr/bin/python3` -> `/usr/bin/python3.14` | CPython 3.14.4; `importlib.util.find_spec("pytest")` is `None` | Not suitable for the declared pytest regression without installation, which is not authorized. |
| `/home/lobsterboss79/temp/context-engine-ws2-validation.qNq9B4/bin/python` | Existing isolated venv, created 2026-09-23 by `/usr/bin/python3.14 -m venv`; CPython 3.14.4; `include-system-site-packages = false`; imports pytest 9.1.1 and markdown-it-py 4.2.0 successfully | Candidate suitable existing Phase 4 validation environment, subject to Owner authorization to use it. |

The temporary venv is repository-independent: it is outside the worktree, has its own `site-packages`, and use of its Python interpreter does not modify repository source or tests. The project declares `requires-python >=3.14,<3.15`, `pytest>=9,<10` as a `dev` optional dependency, and standard pytest testpaths; pytest is therefore required by the intended invocation but is not required to be installed in the system runtime used for the semantic runner.

## Prior Phase 4 provenance and intended slice

The exact venv path is established Phase 4 precedent. `VE-P4-3A-001` records it executing a focused regression under CPython 3.14.4 / pytest 9.1.1. `VE-P4-3B-002/regression.md` records the precise Linux invocation pattern with `PYTHONDONTWRITEBYTECODE=1`, `PYTHONPATH=src`, the same venv interpreter, and `-p no:cacheprovider`, with 25 tests passing. Earlier Phase 4 records also identify CPython 3.14.4 / pytest 9.1.1 as the validated test pairing.

The intended Lane B slice remains:

```text
tests/test_workstream_3.py
tests/test_workstream_4.py
tests/test_workstream_8.py
tests/test_workstream_10.py
```

It requires pytest. Repository convention does not require the semantic fixture and regression to use the identical executable; it requires the approved Linux/CPython 3.14 runtime and preserved evidence. The candidate venv uses the same CPython 3.14.4 version as the semantic execution and established Phase 4 regression. The semantic raw results are not downgraded by the absent regression: they remain valid observations, but cannot establish complete Lane B validation without the required regression.

## Options and recommendation

| Option | Assessment |
| --- | --- |
| 1 — use existing validated environment | **Recommended minimum.** Authorize the established venv path above for exactly the frozen focused slice, preferably with `PYTHONDONTWRITEBYTECODE=1`, `PYTHONPATH=src`, and `-p no:cacheprovider`; preserve stdout/stderr and environment identity. |
| 2 — create fresh isolated environment | Not necessary while the validated environment exists; would require a new Owner-approved procedure. |
| 3 — install into system/existing environment | Not authorized and unnecessary. |
| 4 — regression unavailable | Not supported by current evidence; a suitable candidate environment exists. |

No product Finding, validation Finding, or H3 is warranted: the condition is an unambiguous regression-invocation environment selection issue, with a supported existing alternative and no demonstrated product or semantic defect. 4.2-A through 4.2-D remain semantically observed but overall Lane B remains STOPPED/INDETERMINATE pending regression. Lane A/C are unaffected. Item 4.7 has no interaction.

## Required Project Owner decision

Authorize or reject use of `/home/lobsterboss79/temp/context-engine-ws2-validation.qNq9B4/bin/python` for one focused, evidence-preserving Lane B regression invocation against the unchanged worktree and stated four test files. If authorized, the exact invocation/environment and preservation method must be frozen before it runs; no package installation, semantic-control rerun, or modification is implied.
