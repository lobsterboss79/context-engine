# Validation Evidence Record and Inventory Template

**Template status:** No execution evidence is recorded here. Preserve original material artifacts; derived/rendered artifacts must link to their source. Retain evidence proportionally, with stronger preservation for FAIL, INDETERMINATE, security/governance, material findings, proving, gate, and material remediation/retest evidence.

## Evidence inventory

| Evidence ID | Record/result state | Baseline | Expected Result ID/version | Finding IDs | Original artifact location | Lineage |
| --- | --- | --- | --- | --- | --- | --- |
| `[future stable ID]` | `[PASS / FAIL / INDETERMINATE]` | `[exact commit/version]` | `[ER-ID vN]` | `[future IDs / none]` | `[repository-conventional path]` | `[origin/derived/retest relation]` |

## Individual Validation Evidence Record

| Field | Record value |
| --- | --- |
| Evidence ID | `VE-[stable ID]` |
| Execution date/time | `[future timestamp/timezone]` |
| Exact baseline/commit/version | `[IVB/derived baseline and exact value]` |
| Validation/checklist/protocol item | `[future item]` |
| Governing references | `[approved requirement/design/governance references]` |
| Environment/runtime | `[host/runtime/version and material conditions]` |
| Bootstrap/configuration | `[exact identity/provenance]` |
| Controlled Sources/fixtures/inputs | `[exact identities/provenance/ASU where applicable]` |
| Predetermined expected-result reference | `[ER-ID/version]` |
| Procedure/command | `[exact governed procedure/command]` |
| Raw/original result | `[immutable artifact/link]` |
| Derived/rendered result | `[controlled derivative/link or N/A]` |
| Result state | `[PASS / FAIL / INDETERMINATE]` |
| Linked finding IDs | `[future IDs / none]` |
| Reviewer/evaluator | `[identity/role]` |
| Disposition | `[governed disposition or pending]` |
| Evidence lineage | `[prior/derived/retest/proving links]` |

`INDETERMINATE` is not PASS. A FAIL does not itself establish root cause. Preserve both even if later remediation/retest passes.
