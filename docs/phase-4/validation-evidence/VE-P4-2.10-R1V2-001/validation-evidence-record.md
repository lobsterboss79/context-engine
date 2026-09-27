# VE-P4-2.10-R1V2-001 — R1 v2 identical-input repeatability execution

**Result state:** **PASS**

| Field | Record value |
| --- | --- |
| Run / execution | `R1V2-01` / `VE-P4-2.10-R1V2-001`; preserved in raw artifacts. |
| Exact baseline | Clean pre-execution `HEAD` `1b8fe6e230e90e7d93b695831b19dc5c4a21a5ee` — *Reconcile Phase 4 repeatability ordering controls*. |
| Controls | `FX-F3 v1`, unchanged `ER-F3 v1`, `RC-P4-2.10-R1 v2`, `ER-P4-2.10-R1 v2`, and `SC-P4-2.10 v2`. The v1 failure is historical lineage only. |
| Preflight | **PASS.** Historical whole-file hashes at `c7d17714a3983335f8564aa9360739d9ec785410`: fixture register `ddc68a86d135c4927e519d1c037b2d4cdad8e91c4b89516b8ef7c879ace7c794`; expected-results register `a8aa072209f6d0b2515ababadcd51bb787bec470b82f04e6c8b0d834016a2600`. Current extracted records: FX-F3 `6bda6616a07021a2d54a10bc07331675337a910e1a9958525aacbba8ed226e6e`; ER-F3 `72e5b2de99cd2b23c00f845dbb2e1f10aae481dc3a0f9afbf38ece248ff5b02f`. All six frozen F3 input hashes matched. |
| Isolation | **PASS.** Fresh process, new v2-specific evidence/output workspace, and private `raw/f3-state.sqlite`; no inherited database, audit, package, rendering, prior-run artifact, or semantically influential shared cache. R2 perturbations were inactive. |
| ER/SC assessment | **PASS.** Four identities, Candidates, applicability, selection, roles, Provenance, current/history, unresolved `CON-F3-CASE-CHOICE`, `UNC-F3-DEPOT`, ASU basis, insufficiency, and `coherent_with_qualification` were preserved. |
| Independent order domains | **PASS.** Candidate, traversal, and package: CANVAS-HISTORY, DEPOT-UNVERIFIED, SEALED, TOTE. Manifest: COMPETING, CURRENT, HISTORY, QUALIFICATION. Each renderer: Required SEALED, TOTE; Supporting CANVAS-HISTORY, DEPOT-UNVERIFIED. |
| Boundary | **PASS.** Human, ChatGPT, and Codex renderings are faithful presentations and make no delivery, receipt, or use assertion. |
| Artifacts | Raw procedure, stdout/stderr, raw result, private SQLite state, three renderings, semantic projection/assessment, and SHA-256 manifests are preserved in this directory. |

This is one independently passing v2 run only. It does not establish overall R1
v2 PASS, close the historical finding, complete Item 2.10, authorize R2,
approve Gate 4B, authorize proving, reopen TD-14, or establish readiness.
