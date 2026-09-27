# `RC-P4-2.10-R2 v1` — Incidental-Order Independence

**Pre-results only; not executed.** This is the frozen procedure control for
`ER-P4-2.10-R2 v1` and shared `SC-P4-2.10 v1`. Each future run uses fresh,
isolated state and the exact F3 hash inventory. `R2-REF` is predesignated, not
derived from observed results.

## Exact bounded matrix

| Future run | One controlled mechanism | Fixed value / mechanism | Classification |
| --- | --- | --- | --- |
| `R2-REF` | Reference | Unperturbed F3 in-memory definition/pair order; `PYTHONHASHSEED=101`. | Reference |
| `R2-H` | Python hash iteration | Same reference procedure except `PYTHONHASHSEED=907`. | Supported for R2 |
| `R2-P` | Source/observation presentation | Same F3 definitions, identities, files, and governed metadata, presented to the existing observation/discovery API in this fixed order: depot, canvas history, tote, sealed. No file is rewritten, moved, or retimestamped. `PYTHONHASHSEED=101`. | Supported for R2 |
| `R2-M` | Mapping insertion order | Same F3 values, but the `applicability` and `role_inputs` input pairs are constructed in fixed order depot, tote, sealed, canvas history before the existing orchestration converts them to mappings. `PYTHONHASHSEED=101`. | Supported for R2 |

No combined run is needed: each supported mechanism is isolated, and the
normal F3 public composition path contains no interaction requiring a combined
case. All perturbations are execution-procedure input presentation only; they
do not alter a product interface or production behavior.

## Candidate review and negative controls

| Candidate | Classification and exact reason |
| --- | --- |
| A. `PYTHONHASHSEED` | **SUPPORTED FOR R2.** Fixed, recorded values `101` and `907` can change incidental hash/set iteration. The discovery implementation normalizes set-derived mechanisms and sorts semantic results; the integrated result, not that code reading, is compared. |
| B. Source/observation presentation order | **SUPPORTED FOR R2.** Existing F3 orchestration supplies a tuple of `DiscoveryEvidence`; a control-only invocation can present the same named observations in a different tuple order without changing F3 files or semantics. |
| C. Request/configuration mapping insertion order | **SUPPORTED FOR R2** as governed application-input mapping order: existing `run_governed_render` receives `applicability`/`role_inputs` tuple pairs and constructs mappings. Bootstrap/project TOML file order is not changed. |
| D. SQLite insertion order | **NOT APPLICABLE TO THE F3 EXECUTION PATH.** The normal F3 path initializes fresh SQLite and writes one construction record followed by audit; it does not load F3 semantic input from persisted multi-record state. Inserting extra records merely to vary private row IDs would add an unsupported path, so this control does not do it. Row IDs remain prohibited as semantic rank and absent from the projection. |
| E. Filesystem enumeration | **NOT APPLICABLE TO F3 EXECUTION PATH.** F3 observes four named artifact locators; there is no ambient application-level directory enumeration in this path. A synthetic enumeration path would be invalid. Filesystem order remains prohibited from semantic rank. |

No safe distinct frequency perturbation is required or available for F3:
duplicating Sources/content would change the governed scenario. Recency is not
perturbed because its F3 currentness assessments are semantic inputs. The
negative acceptance criterion is that each supported run preserves both current
conflict participants unresolved, historical Supporting Context historical, and
no generic newer-wins result. There is **NO APPROVED/IMPLEMENTED NUMERIC
SEMANTIC RANKING MECHANISM** in the inspected v0.1 interfaces. Every future R2
reason/result review must show no invented score, rank, weight, count,
timestamp, or row-ID basis.

Any proposed alteration of task, Source/artifact identity/content, Authority,
authorization, Governance State, relationship, currentness, Conflict,
Uncertainty, ASU semantics, role, expected result, or semantic order is not an
R2 perturbation and must not execute under this control.
