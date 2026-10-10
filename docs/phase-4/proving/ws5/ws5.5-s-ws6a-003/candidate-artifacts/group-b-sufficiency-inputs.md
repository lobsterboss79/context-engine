# Candidate Sufficiency Inputs — Group B

**Status:** **CANDIDATE — NOT FROZEN — OWNER APPROVAL PENDING**

This maps to `SufficiencyInputs`; it is not a sufficiency result because no
selection may occur while B1 enforcement is unresolved.

| Field | Proposed value | Assessment |
| --- | --- | --- |
| `selected` | unresolved until applicability/selection approvals | Must be the selected ContextItems, not a Claim count. |
| `universe` | A3 `KNOWN_INCOMPLETE` ASU | Approved boundary; not package sufficiency. |
| `required_deficiencies` | empty tuple | Proposed only if Owner accepts the Required map and every frozen-task field has selected coverage. |
| `material_conflict` | False | Proposed: active lifecycle has no conflict; historical/current distinctions remain qualified. |
| `material_uncertainty` | False | Proposed only for the sufficiency boolean; Source/ASU and record limitations remain material package qualifications. |
| `bounded_task_safe` | True | Proposed from the task's explicit limitation/inference constraints and bounded documentary scope. |
| expected output | `CONDITIONALLY_SUFFICIENT` | Derived only if proposed inputs pass: known-incomplete ASU plus safe bounded task. It is not predetermined. |

Fail closed if a Required Claim is omitted, an unknown material deficiency is
identified, an unresolved material conflict/uncertainty applies, or the task
is broadened beyond the eight-Source documentary boundary. This does not claim
the external Project is complete or ready for implementation/trading.
