# Candidate Delivery-Artifact Integrity Manifest — WS6A Remediation

**Status:** **CANDIDATES PREPARED — NOT FROZEN, DELIVERED, OR BOUND**

This manifest records only the two exact Owner-approved new text candidates.
It is append-only preparation evidence. It does not recover the historical
successor-003 package or rendering bytes, create a successor-004 control, or
authorize Consumer interaction.

| Delivery element | Candidate artifact | Encoding / terminal newline | Bytes | SHA-256 | Approved placement | State |
| --- | --- | --- | ---: | --- | --- | --- |
| Consumer-contract wrapper | `candidate-artifacts/consumer-contract-wrapper.txt` | UTF-8 / present | 359 | `b1c3d17f53988c1cdd0a3bf8a7c553e50f0a6d31905691bf44aaa371f67707af` | Exactly once after the package-arm rendering | D4 candidate only |
| Ordinary-minimal-pointer control baseline | `candidate-artifacts/control-baseline.txt` | UTF-8 / present | 149 | `90e3fec97a6ad48b7138e8fed7dfe4b0696f7156b7be4c45b4502df91b17eb12` | Exactly once after the same frozen task | D5 candidate only |

The frozen task remains
[`I10-DTS-CONTINUATION-BRIEF-v1`](../ws5.5-s-ws6a-002/frozen-task.md), with
SHA-256 `52f3e52bc72c1a9d73789d422f185e15a0d9d56e7889ec98f35eac5eeceec6b4`.
The evaluator's verified SHA-256 is governed for future reference by
[`P4-I10-WS6A-EVALUATOR-HASH-ERRATUM-001`](evaluator-hash-erratum-001.md).

No package or rendering candidate appears in this manifest: their required
construction inputs are not fully governed in retained evidence, as recorded
in the [candidate construction-input manifest](candidate-construction-input-manifest.md).
No hash in this document is an exact-run binding until separately frozen and
approved by the Project Owner.
