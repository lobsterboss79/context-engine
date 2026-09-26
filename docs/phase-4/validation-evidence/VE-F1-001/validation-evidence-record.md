# VE-F1-001 — FX-F1 v1 Validation Evidence Record

**Result state:** **PASS**  
**Status/disposition:** Complete governed F1 execution evidence; no finding;
awaiting Project Owner/ChatGPT review. This record establishes neither Gate 4B,
fresh-Consumer authorization, TD-14 reopening, remediation authority, Phase 4
scope change, nor production readiness.

## Identity, baseline, and controls

| Field | Record value |
| --- | --- |
| Evidence ID / execution time | `VE-F1-001`; 2026-09-26T14:56:03.114054+00:00 (UTC) |
| Exact execution baseline | `c7d17714a3983335f8564aa9360739d9ec785410` — `Prepare Phase 4 deterministic validation fixtures` |
| Item 2.1 fixture-preparation commit | The exact execution baseline; it contains the committed Item 2.1 artifacts. |
| Implementation origin / lineage | `IVB-P4-ORIGIN`, `9862497` — `Close Phase 3 v0.1 implementation`; `git diff 9862497 c7d1771 -- src` was empty. Gate 4A authorization `c9b39a3` is an ancestor; `git diff c9b39a3 c7d1771 -- src` was empty. |
| Validation/checklist relationship | WS2 Item 2.2; F1 nominal end-to-end construction and all approved renderings. |
| Fixture / expected result | `FX-F1 v1` against frozen `ER-F1 v1`, governed for authorized execution. No later history revision of `fixture-records.md` or `expected-results.md` exists, and both are unchanged from `c7d1771`. |
| Governing references | Phase 0 §§4–12; Phase 2 Domain E DS-02/selection/sufficiency and Domain F; Phase 3 WS8–WS9; Phase 4 checklist; Gate 4A authorization; WS1 evidence controls; Item 2.1 preparation record; F1 fixture and ER-F1 records. |
| Reviewer/evaluator | Codex, execution/evidence recorder; Project Owner/ChatGPT review pending. |

## Fixture provenance and environment

All F1 artifacts were compared byte-for-byte to `c7d1771`; their Git blob
identities match the committed provenance. The fixture is synthetic and has no
production Authority, as explicitly stated in the frozen fixture records.

| Controlled input | SHA-256 |
| --- | --- |
| `F1/bootstrap.toml` | `9ac83244ab0987ae993ec3a5731b4ade02b90e3c0fcd7ce6e7c6fd4a9e368648` |
| `F1/project.toml` | `7f2a972f0514716eaffb9f4f92cfdd366e538549fdd0ce10c4f1a1b819d45220` |
| `F1/sources/atlas-charter.md` | `7ef0e2775b33d4e25231e5c236480a8a57c1474d600b416c16091067f369d687` |
| `F1/sources/atlas-delivery.md` | `6b464f4a5d416da056e79a55e3e9adef572615217f7959ff6100544ec8493623` |

Runtime: Python `3.14.4`; Git `2.53.0`; `markdown-it-py 3.0.0`; local,
network-free repository execution. The explicit Bootstrap validates Project
`fixture-atlas-f1`, controlled-validation-fixture scope, and its named Project
configuration (original CLI output: `raw/bootstrap-validate.stdout`).

## Procedure and original evidence

1. Verified a clean tree, current HEAD, Git history, Gate 4A ancestry, committed
   F1 blob provenance, frozen ER/F1 registers, and the controlled input hashes.
2. Ran existing `context_engine` CLI `bootstrap-validate` with the exact F1
   Bootstrap/configuration.
3. Ran `raw/f1-execution.py` with `PYTHONPATH=src`. This execution-only script
   invokes existing v0.1 interfaces: `LocalGitSourceAdapter`, Markdown
   observation/transformation, explicit represented-information records,
   deterministic `discover`, applicability/selection, `evaluate_sufficiency`,
   logical package construction/persistence, and existing Human/ChatGPT/Codex
   rendering. It introduces no application path, dependency, or fixture change.

Original, non-normalized artifacts are in [`raw`](raw/), including the complete
JSON transition result, SQLite construction/audit state, command output, exact
execution script, and three renderer outputs. Controlled derivative hashes and
their lineage are in [the raw-artifact manifest](derived/raw-artifact-sha256.md).

## Observed pipeline transitions

| Transition | Preserved observation |
| --- | --- |
| Bootstrap/configuration | Explicit F1 Bootstrap and matching `fixture-atlas-f1` Project configuration established. |
| Lifecycle / ASU | `SRC-F1-CHARTER` and `SRC-F1-DELIVERY` are available, inspected, and form the adequate explicit F1 ASU. |
| Observation / transformation / representation | Both Markdown artifacts observed; both local Git observations are `observed` at `c7d17714…`; normalized Markdown transformations preserve artifact/version/observation Provenance. `RI-F1-RELEASE-CONSTRAINT` and `RI-F1-AVAILABILITY` were represented. |
| Discovery / Candidate Context | Both items are literal deterministic Candidates; no Source is excluded and no expansion occurred. |
| Applicability / governance | Both are applicable using the pre-established F1 task mappings with Bootstrap, requester, and Consumer disclosure authorization true. |
| Role / selection | Release constraint selected **Required** on incorrect-performance omission risk; availability selected **Supporting** on material preparation/validation benefit. |
| Conflict, Uncertainty, ASU, sufficiency | No Conflict and no item-level material Uncertainty. The ASU boundary record explicitly states `adequate`; package outcome is **Sufficient**. Its generic boundary annotation is not a material uncertainty or deficiency. |
| Construction / logical package | `PKG-F1-001`, record `PCR-F1-001`, is `coherent`, completed, and contains both selected items. Source Manifest preserves both Sources and observation identities. |
| Renderings | Human, ChatGPT, and Codex all have status `rendered`, each derives from `PKG-F1-001`, and each preserves roles, Provenance, ASU/sufficiency/coherence state and the Source-content boundary. |
| Delivery/receipt/use boundary | Each rendering expressly records presentation only; no delivery, receipt, use, or Consumer action is asserted. |

## ER-F1 v1 comparison

| ER-F1 acceptance criterion | Result |
| --- | --- |
| Both Sources / lineage / manifest survive through each rendering | Satisfied: both named Sources, artifacts, observations, and normalized Provenance appear in the package and every rendering. |
| Required/Supporting distinction survives | Satisfied: sealed-case constraint is Required; availability is Supporting; both are selected. |
| Adequate ASU, Sufficient package, coherent construction | Satisfied: two-Source adequate ASU; `sufficient`; `coherent`; logical package exists. |
| Same logical package is faithfully rendered for Human, ChatGPT, Codex | Satisfied: all three `rendered` outputs refer to `PKG-F1-001`; canonical semantic payloads preserve the required material fields. Byte identity was not required. |
| No delivery/receipt/use assertion | Satisfied by renderer reason codes and presentation text. |

Negative/failure criteria were not observed: no role collapse, omitted
Provenance, artificial Conflict, material/unsupported Uncertainty,
inadequate-ASU claim, package/rendering collapse, or semantic renderer loss.

## Finding and evidence lineage

No finding is created: the evidence establishes PASS with no unresolved
discrepancy. `VE-F1-001` is the originating execution evidence (not a retest);
raw artifacts remain preserved separately from this controlled assessment.

## Scope and stop attestation

Only `FX-F1 v1` was executed. F2, F3, F4-A–F4-D, and F5-A–F5-C were not run.
No remediation, application/source-code modification, Consumer reservation,
fresh-Consumer preflight/proving, TD-14 action, Gate 4B review, or scope change
occurred. Gate 4B remains **NOT APPROVED**; TD-14 remains **CLOSED / NOT
REOPENED**; production readiness is not established.
