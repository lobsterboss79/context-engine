# Stage 1 Candidate Construction and Rendering Authorization Package

**Status:** **OWNER DECISION PACKAGE — STAGE 1 NOT AUTHORIZED**

## Proposed decision scope

Authorize at most one repository-side candidate operation through the existing
`GovernedRenderInputs` orchestration path. It may establish Bootstrap, validate
the paired configuration, discover the lifecycle-resolved active corpus,
evaluate final-approved applicability/selection, compute sufficiency and
coherence, construct a logical package, and create a deterministic ChatGPT
rendering for the approved logical Consumer. It may preserve candidate evidence
only. It may not contact or disclose to a physical Consumer.

## Required bindings

| Binding | Required value / evidence |
| --- | --- |
| Logical Consumer | `consumer:I10-DTS-CHATGPT-CANDIDATE-RENDERING-v1`, `CHATGPT`; logical and non-delivery only |
| DTS / active corpus | `e29de5c7d26a31f66cf47c30b295591e6b192887`; 34 active / four relations; manifest `62e55be569bcd8fabd864ab4c4339f384a23c07e53a3d7f5c8579a9b8457680e` |
| Task | `I10-DTS-CONTINUATION-BRIEF-v1`; `52f3e52bc72c1a9d73789d422f185e15a0d9d56e7889ec98f35eac5eeceec6b4` |
| Evaluator reference | Erratum `P4-I10-WS6A-EVALUATOR-HASH-ERRATUM-001`; verified digest `fec79e941ba875850d5b8feb869f63cada4f48df9f406042ce5d1718584b342b`; evaluator remains inaccessible to construction |
| A/B/C inputs | All entries in `stage-1-canonical-input-reconciliation.md` made final for this operation, with their listed candidate hashes |
| Existing text candidates | D4 wrapper `b1c3d17f53988c1cdd0a3bf8a7c553e50f0a6d31905691bf44aaa371f67707af`; D5 baseline `90e3fec97a6ad48b7138e8fed7dfe4b0696f7156b7be4c45b4502df91b17eb12`; neither is delivered or frozen by Stage 1 |

## Literal runtime facts requiring express Owner authorization

The decision must establish only for this logical non-delivery operation:

```text
operator_authorized = True
bootstrap_valid = True after successful Stage 1 Bootstrap establishment
requester_authorized = True
consumer_disclosure_authorized = True
protected_metadata_authorized = True for the approved allowlist only
ConsumerContract.disclosure_authorized = True
capacity_characters = None, with no actual delivery-capacity claim
```

These are authorization facts for repository-side semantic processing and
rendering, not permission to expose data to a physical Consumer. They do not
authorize successor-004, Consumer carry-forward, final disclosure, final
freeze, delivery, WS6A, or WS6B.

## Allowlist and prohibited material

Permit only active governed assertion content; compact Claim/represented
information/Source/Artifact/revision/observation/location provenance;
authority/governance/currentness bases and classifications; limitations,
uncertainty, conflicts; and final-approved applicability/selection,
sufficiency/coherence, ASU, and Source-boundary qualifications. Prohibit raw
Markdown, Source files/attachments, filesystem paths, SQLite/controller IDs,
lifecycle internals, evaluator/P1–P8 material, expected answers, proving
history, physical Consumer IDs, controller deliberation, tools/connectors, and
all unapproved Project information.

## Candidate outputs and required evidence

If the Owner also resolves the output-evidence limitation in the reconciliation
record, the sole proposed candidate-output root is
`docs/phase-4/proving/ws5/ws5.5-s-ws6a-003/candidate-stage-1/`. It is not a
successor-004 control and is not created by this package. The proposed evidence
set is `input-integrity.md`, `construction-result.md`,
`rendering-chatgpt.txt`, `rendering-chatgpt.sha256`, and `validation.md`.
Preserve exact rendering UTF-8 bytes, SHA-256, byte count, terminal-newline
state, deterministic-order check, input-manifest hashes, effective DTS/corpus/
lifecycle evidence, allowlist check, and construction/result record. Preserve
failures verbatim as adverse evidence.

No production canonical full-`ContextPackage` byte serializer currently exists.
This package does not authorize inventing one. A separate Owner decision is
required before making an exact logical-package-byte/hash claim.

## One-operation termination and stop conditions

Terminate after one preserved candidate result. Stop and preserve on any input
hash/revision/corpus mismatch; unapproved value; Bootstrap/configuration
failure; denied/unresolved applicability; selection/sufficiency/coherence result
inconsistent with final approved inputs; lifecycle/provenance/allowlist
failure; raw-Source/evaluator/expected-answer/controller/control leakage;
rendering failure; need for a serialization/code/DTS change; or evidence-write
failure. Do not retry with changed inputs without another Owner decision.

## Explicit prohibitions and remaining decisions

No physical Consumer interaction, task/package/rendering delivery, reservation
or binding transfer, successor-004 creation, final artifact freeze, control-arm
execution, WS6A/WS6B, Gate 4C, or production-readiness action is authorized.

The Owner must still decide final A/B/C values, all runtime facts above, the
logical-package evidence boundary, then—after candidate review—final artifact
freeze, successor-004, per-arm continuity/carry-forward, final disclosure, and
a separate WS6A authorization.
