# WS4 Lane B — Interruption and Persistence Matrix

| Obligation | Independent v2 evidence | Observed governed state | Classification |
| --- | --- | --- | --- |
| 4.2-A interrupted operations | `VE-P4-4B-002` predecessor | Deliberate application-seam replacement interruption returned the expected application-level failure; old target hash was unchanged. | **PASS** |
| 4.2-B persistence integrity | predecessor plus v3 regression | Target and backup `PRAGMA integrity_check` were `ok`, schema was 5, and the focused persistence slices passed. This observes SQLite state; it does not assert unobserved filesystem durability. | **PASS** |
| 4.2-C transaction/partial state | predecessor and `VE-P4-4B-002-S1` | Predecessor retained only Project-B old state, no source replacement, recovery qualification, or staging file. Independent successor copied predecessor state, restored Project-A links/audit, excluded Project B, and retained historical-only/unknown/no-Authority state. | **PASS** |
| 4.2-D migration where applicable | `VE-P4-4B-002-M1` plus v3 regression | Supported application-owned v1→v5 migration retained v1 evidence, created expected tables, and passed integrity. | **PASS** |

`VE-P4-4B-001` remains permanently **INDETERMINATE** because its durable preflight record was absent. It is immutable mechanism/history evidence and is not replaced by this independent v2 family.
