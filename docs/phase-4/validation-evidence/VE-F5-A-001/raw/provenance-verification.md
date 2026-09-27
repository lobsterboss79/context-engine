# F5-A Pre-execution Provenance Verification

**Result:** **VERIFIED FOR EXECUTION**

| Check | Result | Preserved basis |
| --- | --- | --- |
| 1. Current F5-A controlled inputs match `c7d17714` | PASS | Byte comparison of the six controlled artifacts against `c7d17714a3983335f8564aa9360739d9ec785410`; hashes in `controlled-input-sha256.txt`. |
| 2. FX-F5-A semantics match the materialized fixture record | PASS | The exact `## FX-F5-A` section of `fixture-records.md` is byte-identical to `c7d17714`. |
| 3. ER-F5-A semantics match the materialized expected-result record | PASS | The exact `## ER-F5-A v1` section of `expected-results.md` is byte-identical to `c7d17714`. |
| 4. No later semantic revision exists | PASS | `git log c7d17714..362ea3c` identifies only `2b7435b` (F4-E addition) and `362ea3c` (provenance clarification); neither changes the F5-A fixture section, ER-F5-A section, or controlled paths. |
| 5. Original preparation/non-execution attestation remains traceable | PASS | `c7d17714:docs/phase-4/workstream-2-item-2.1-fixture-preparation.md` records its frozen controls and expressly attests that no fixture was run. |
| 6. Clarification is present and controls the historical shorthand | PASS | `docs/phase-4/original-fixture-family-provenance-clarification.md` is present and identifies `c9b39a3` as Gate 4A/pre-preparation authorization and `c7d17714` as fixture/ER materialization. |

The clean execution baseline was `362ea3ceb7164e9fbddee0606c63be1bb9c78deb`.
