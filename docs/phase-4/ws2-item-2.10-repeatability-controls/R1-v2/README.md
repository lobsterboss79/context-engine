# RC-P4-2.10-R1 v2 — Identical-Input Repeatability

**PROJECT OWNER APPROVED PRE-RESULTS CONTROL CORRECTION; NOT EXECUTED.**
This supersedes RC-P4-2.10-R1 v1 and references ER-P4-2.10-R1 v2 and
SC-P4-2.10 v2. It changes only the erroneous unified ordering taxonomy.

## Lineage

v1 was executed once as R1-01 and remains an immutable FAIL against its
then-frozen expectation. The Project Owner determined that v1 incorrectly
applied renderer role grouping to Candidate/package order. R1-01 does not
count toward this v2 matrix.

## Future matrix

| Future v2 run | Fixed inputs | Isolation |
| --- | --- | --- |
| R1-v2-01 | Exact F3 hashes/inventory and unmodified semantic inputs | Fresh SQLite, output/evidence workspace, audit/cache state, and generated artifacts. |
| R1-v2-02 | Same | Same; no prior-run artifact or database may be read. |
| R1-v2-03 | Same | Same; no prior-run artifact or database may be read. |

Each future run verifies all v1 provenance and controlled-input checks, ER-F3
v1, ER-P4-2.10-R1 v2, and every SC-P4-2.10 v2 order domain independently.
PASS requires all three individually faithful and pairwise semantically equal.
Any mismatch or unisolatable state stops under H3. Separate Project Owner
execution authorization is required.

