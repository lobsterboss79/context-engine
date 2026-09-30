# Test-owned SQLite close correction record

Status: **FROZEN BEFORE IMPLEMENTATION**

| Item | Frozen value |
| --- | --- |
| Branch / HEAD | `phase4-ws4-input-diagnostics-win` / `d33b244b0c6107a5d482d31145bcbdd67ee0a576` |
| WS4 test blob | `c7dcf0e1eee6290348e03a0b9c912e929c1d6b48` |
| WS8 test blob | `914e6e0b5438b443de1a7e89c11c61c3ed98bc44` |
| Remediated adapter blob | `2e948c02a2d2fea96c93e46ea5a38657dd7e468c` |
| Scope | Exactly three test-owned `sqlite3.connect` lifetimes; no source, assertion, fixture, input, expected-result, or test-selection change. |

The exact sites are the two direct connections in
`test_lifecycle_schema_migrates_deterministically_from_version_one` (WS4):
one creates the version-one migration fixture and one reads migrated schema
state. The third is the direct connection in
`test_package_construction_schema_migration_and_duplicate_retry_are_explicit`
(WS8), which creates the version-three fixture.

All three are test-owned setup/readback resources. Their existing `with
sqlite3.connect(...) as connection` blocks preserve transaction behavior but
do not deterministically close the connection. The connections have no semantic
purpose after their local SQL work completes. The authorized correction is to
wrap each with `contextlib.closing` while retaining its existing `with
connection` transaction block. This commits/rolls back exactly as before and
then closes at the test-owned boundary on every path.

No additional direct connection, including application adapter connections,
is in scope. The expected tests, migration inputs, application calls, and
assertions remain exactly unchanged.
