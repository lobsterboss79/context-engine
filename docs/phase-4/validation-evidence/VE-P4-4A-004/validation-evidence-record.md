# VE-P4-4A-004 validation evidence record

Status: STOPPED — FOCUSED REGRESSION FAILED; PROJECT OWNER DISPOSITION REQUIRED

## Lineage and frozen basis

This independently frozen successor preserves, without alteration, the
predecessor states: VE-P4-4A-001 is INDETERMINATE (runner construction);
VE-P4-4A-002 is INDETERMINATE (Windows preflight procedure); and VE-P4-4A-003
is FAIL (over-specific top-level `DiscoveryResult.limitations` criterion).

CTL/PROC-P4-4A-004 v1 and ER-P4-4A-004 v1 use the authority-traced semantic
criterion: material partial evidence must remain attributable, qualified,
visible, non-authoritative, and insufficient where applicable.  They do not
require that qualification to be carried in a particular top-level field.

## Preflight and semantic execution

Portable preflight passed before execution.  The durable preflight record SHA-256
is `C24B068E14D77ABC4C8F1456447CE41FE3CA75FA29AD8F6575A8C7C7D8A88831`.
It records literal-SHA Git existence and ancestry checks, unchanged 002 semantic
artifact hashes, Windows environment, external validation-environment identity,
and source/test/shared/Lane B/C integrity checks.

The frozen semantic invocation then completed once with exit status 0.  Its
result is `PASS`: all fourteen frozen assertions are true in
`raw/result.json`.

Observed partial evidence was represented as Candidate, selected Context Item,
and Source Manifest qualification `Source source-partial: partial`.  The
bounded downstream path preserved it into the rendered package; authority count
was zero and sufficiency was `insufficient`.  The semantic runner deliberately
did not require the unrelated top-level `DiscoveryResult.limitations` field to
carry that condition.

The observed semantic states remained distinct: application-level failure
(malformed input and invalid configuration), absence, unavailable, partial
evidence, and successful completion.  The frozen diagnostic assertions passed:
the diagnostic was attributable and classified, did not expose the fixture
secret, was not durable audit or recovery evidence, and did not convert failure
to success.

## Focused regression stop

After the semantic PASS, the frozen focused regression was invoked exactly once
using only `Z:\temp\context-engine-phase4-validation\Scripts\python.exe`:

```text
python -m pytest -p no:cacheprovider -q tests/test_workstream_3.py tests/test_workstream_4.py tests/test_workstream_6.py tests/test_workstream_8.py tests/test_workstream_9.py
```

It exited 1: `43 passed, 17 errors in 0.48s`.  The errors occurred during test
fixture setup, before their test bodies, because the tests call
`tempfile.mkdtemp(dir=Path.home() / "temp", ...)` and the resolved Windows path
`C:\Users\talbo\temp` did not exist.  Raw stdout, stderr, exit status, and a
post-regression raw-artifact hash manifest are preserved under `raw/`.

This is a required regression FAIL and mandatory stop condition.  It does not
alter the separately preserved semantic-control PASS, and this record does not
classify the setup-path condition as a product Finding, H3, or a Lane B/C
impact.  No rerun, repair, fallback-path creation, post-results coverage review,
or final Lane A disposition was performed.

## Integrity boundary

No source, tests, shared WS4 materials, predecessor artifacts, or Lane B/C
artifacts were changed.  No packages were installed after the environment
verification.  The virtual environment remains external to Git.
