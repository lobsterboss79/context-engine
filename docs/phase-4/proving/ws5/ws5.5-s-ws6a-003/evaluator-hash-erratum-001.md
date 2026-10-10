# P4-I10-WS6A-EVALUATOR-HASH-ERRATUM-001

**Status:** **OWNER-APPROVED FACTUAL ERRATUM — FUTURE BINDING ONLY**

This append-only erratum does not edit evaluator criteria or historical
successor records. It corrects only the factual SHA-256 reference for future
successor/run bindings.

| Field | Verified value |
| --- | --- |
| Evaluator | `I10-DTS-P1-P8-EVALUATOR-v1` |
| Artifact | `docs/phase-4/proving/ws5/ws5.5-s-ws6a-002/frozen-expected-state-evaluator-matrix.md` |
| Original recorded digest | `fec79e941ba875850d5b8feb869f63cada4f48df9f406042ce5d1718584b` |
| Verified SHA-256 | `fec79e941ba875850d5b8feb869f63cada4f48df9f406042ce5d1718584b342b` |
| Earliest artifact commit/blob | `5dbbd69962375dae47e11ff34cc368a3cbe3deb6` / `b8da69858c06ff032790612015e41a7758e69c59` |
| Rebinding control | `74ce1dc2fb0ed901c565d3652dea60836f1a8b80` |

Direct SHA-256 of the historic Git blob and current artifact is the verified
64-character value above. The original recorded value is its 60-character
prefix. The evaluator blob is unchanged from its first committed appearance
through the successor-003 freeze and current repository state; this is a
truncated digest, not an evaluator-content modification or a hashing-boundary
difference.

Affected historical references remain immutable:

- `docs/phase-4/proving/ws5/ws5.5-successor-control-ws6a-002.md`
- `docs/phase-4/proving/ws5/ws5.5-s-ws6a-003/ws5.5-s-ws6a-003.md`

Any future successor that uses this evaluator must reference this erratum and
the verified digest. This erratum neither freezes a successor nor authorizes
execution.
