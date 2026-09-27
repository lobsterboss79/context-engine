# VE-P4-2.10-R1-001 — R1-01 identical-input repeatability execution

**Result state:** **FAIL**

| Field | Record value |
| --- | --- |
| Run / execution | `R1-01` / `VE-P4-2.10-R1-001`; `2026-09-27T12:51:09.167004+00:00` UTC (America/Chicago UTC−05:00). |
| Exact baseline | Clean pre-execution `HEAD` `aeb2d59801370e660356a27e5407f2cead149798` — *Correct Phase 4 F3 provenance verification*. |
| Lineage | Controls materialized at `67bfeb74ef47ca050e12befe74707377e41e9340`; provenance correction at this HEAD; F3 materialized at `c7d17714a3983335f8564aa9360739d9ec785410`; implementation origin `IVB-P4-ORIGIN` / `9862497`. |
| Controls | `FX-F3 v1`, unchanged `ER-F3 v1`, `RC-P4-2.10-R1 v1`, `ER-P4-2.10-R1 v1`, and `SC-P4-2.10 v1`. Historical `VE-F3-001` was not runtime state. |
| Corrected provenance preflight | **PASS.** Git historical hashes at `c7d17714`: fixture register `ddc68a86d135c4927e519d1c037b2d4cdad8e91c4b89516b8ef7c879ace7c794`; expected-results register `a8aa072209f6d0b2515ababadcd51bb787bec470b82f04e6c8b0d834016a2600`. Current extracted FX-F3 and ER-F3 hashes: `6bda6616a07021a2d54a10bc07331675337a910e1a9958525aacbba8ed226e6e`; `72e5b2de99cd2b23c00f845dbb2e1f10aae481dc3a0f9afbf38ece248ff5b02f`. No current whole-register equality requirement was used. |
| Controlled F3 files | **PASS.** The six frozen hashes matched: `1c27f2dd2eb882adadcd2a5ea3f7cc9ec6a223348d49662e51d710a52a180a46`, `6d6982c01382108a970b60830f0d65fa4edf35cc32bee758f16005f613b668be`, `afcb9ebb82eca7b9842078f8f8891c9d2fd912b7e28bebcd9745d31d9717b7c0`, `c22ea350f759e63c0315a2d6c4a370498449e7a2f30e16cf33c2e8b7b8f1a776`, `e4c12c53455c16b11d2a723104d65310f142450ec82d20f6005107b90ac73008`, `fc90e05050be6c023c8214b7acdb28dddc56033d5c7171f5eb68895d9b0af9d2`. |
| Isolation / environment | **PASS for R1-01.** New process, `PYTHONDONTWRITEBYTECODE=1`, new workspace and private `raw/f3-state.sqlite`; no inherited package/rendering/audit/database/prior-run artifact. Network-free CPython 3.14.4, markdown-it-py 3.0.0, Linux `7.0.0-34-generic`, native Git. No semantically influential shared cache/process state was identified. |
| Preserved originals | [Procedure](raw/r1-01-execution.py), [stdout](raw/r1-01-execution.stdout), [stderr](raw/r1-01-execution.stderr), [raw result](raw/raw-result.json), SQLite state, and three renderings. |
| ER-F3 comparison | F3 identity, four represented items, Conflict, Uncertainty, current/historical qualifications, Provenance, Insufficient, and `coherent_with_qualification` are present. The governed order is not. |
| SC / R1 ER comparison | **FAIL.** Expected Candidate/package order: `SEALED`, `TOTE`, `CANVAS-HISTORY`, `DEPOT-UNVERIFIED`. Observed: `CANVAS-HISTORY`, `DEPOT-UNVERIFIED`, `SEALED`, `TOTE`. This is prohibited normalization. Source Manifest order itself matches: `SRC-F3-COMPETING`, `SRC-F3-CURRENT`, `SRC-F3-HISTORY`, `SRC-F3-QUALIFICATION`. |
| Renderer comparison | **PASS individually.** Human, ChatGPT, and Codex are each `rendered`, retain the package/rendering/delivery/receipt/use boundary reason code, and materially present Required `SEALED`, `TOTE` then Supporting `CANVAS-HISTORY`, `DEPOT-UNVERIFIED`. The renderer result cannot cure the separate failed Candidate/logical-package order; no delivery/receipt/use assertion occurred. |
| Result / finding | **FAIL**; [F-P4-2.10-R1-001](finding-record.md), MATERIAL / H3 triggered. |
| Stop boundary | R1-02/R1-03 and all R2 runs were not executed. No remediation, control/ER/fixture/source/test change, Item 2.10 completion, Gate 4B, proving, TD-14 reopening, or production-readiness assertion occurred. |

The [semantic projection](derived/semantic-projection.json) is derived from the
preserved raw result. [Raw SHA-256 manifest](derived/raw-artifact-sha256.txt)
preserves artifact-integrity values.
