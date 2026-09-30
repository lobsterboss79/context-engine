# Windows Phase 4 Validation Environment

**Status:** Dependency decision frozen before isolated-environment installation.

## Authorization and location

Project Owner authorized installation only into the isolated external
environment `Z:\temp\context-engine-phase4-validation`; it is outside Git and
all worktrees. Base interpreter: `C:\Python314\python.exe`, CPython 3.14.7.
Venv interpreter: `Z:\temp\context-engine-phase4-validation\Scripts\python.exe`.
Windows is Microsoft Windows NT 10.0.22631.0; venv pip is 26.2.1.

## Minimum dependency decision

Install **only** direct package `pytest==9.1.1` with the venv's own Python.
This is necessary because every frozen Lane A regression module imports
`pytest`; `pyproject.toml` declares the compatible development constraint
`pytest>=9,<10`. Existing successful Phase 4 environments used pytest 9.1.1.
The official pytest 9.1.1 release declares Python `>=3.10`, explicitly lists
Windows and Python 3.14 support, and is not yanked; it is therefore compatible
with CPython 3.14.7/Windows and the repository constraint.

No additional direct package is required for the frozen Lane A semantic runner
or regression slice (`tests/test_workstream_3.py`, `_4.py`, `_6.py`, `_8.py`,
and `_9.py`): their imports require the repository source plus pytest and
standard-library modules. `markdown-it-py` is a project dependency used by the
unselected representation adapter, not by this slice. Pip-resolved runtime
dependencies of pytest are permitted only as required transitive dependencies
and will be recorded exactly after installation.

Frozen installation command:

```powershell
& 'Z:\temp\context-engine-phase4-validation\Scripts\python.exe' -m pip install pytest==9.1.1
```

No global, user, repository, source, test, dependency-file, or lockfile
installation/change is authorized.

## Installed environment and collection verification

Installation completed successfully with the frozen command against the venv's
default configured package index. Direct package installed: `pytest==9.1.1`.
Exact resulting inventory: `colorama==0.4.6`, `iniconfig==2.3.0`,
`packaging==26.3`, `pip==26.2.1`, `pluggy==1.6.0`, `Pygments==2.21.0`, and
`pytest==9.1.1`. The non-pytest packages are pip-resolved pytest dependencies.
External installation stdout, stderr, exit status, pip configuration, inventory,
and hashes remain under the canonical external environment.

The venv interpreter/import/version verification passed. Collection-only passed
with `PYTHONPATH=src`, `PYTHONDONTWRITEBYTECODE=1`, and cache provider disabled:
`Z:\temp\context-engine-phase4-validation\Scripts\python.exe -m pytest -p no:cacheprovider --collect-only -q tests/test_workstream_3.py tests/test_workstream_4.py tests/test_workstream_6.py tests/test_workstream_8.py tests/test_workstream_9.py`.
It collected 60 tests. Repository source, tests, and shared WS4 files were
unchanged before this verification.
