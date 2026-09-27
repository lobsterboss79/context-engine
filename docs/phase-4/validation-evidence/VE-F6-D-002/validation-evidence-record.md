# VE-F6-D-002 — FX-F6-D v1 Corrected-Procedure Retest

**Result state:** **PASS**

| Field | Record value |
| --- | --- |
| Evidence / execution | `VE-F6-D-002`; `2026-09-26T20:58:05.457961-05:00` (America/Chicago; UTC offset `-05:00`). |
| Exact retest baseline | Clean pre-procedure `HEAD` `5a46b97654e25abc3ea954fb264339178c74aecb` — *Record Phase 4 indeterminate ASU execution attempt*. `git status --short` was empty. This HEAD contains committed D preparation, `FX-F6-D v1`, `ER-F6-D v1`, and `VE-F6-D-001` **INDETERMINATE**. |
| Original evidence lineage | Immutable original `VE-F6-D-001` remains **INDETERMINATE**. Its execution-only procedure used `RoleInputs(False, True, False, ...)`; the second positional value is `omission_risks_improper_performance`, a Required trigger. That was a contained procedure deficiency, not a product finding. No Finding Record exists for it. |
| Fixture / ER preservation | Unchanged `FX-F6-D v1` against unchanged `ER-F6-D v1`; no later ER-F6-D revision exists. No application, Source, test, fixture, ER, controlled-request, ASU-basis, task-boundary, or expected-result change occurred after the original attempt. |
| Controlled hashes | `bootstrap.toml` `a36761630dead061f856b74624b35605db24ffe16bcbc5f89e56d05b3904781e`; `project.toml` `98fe288577b9f7bb1beb0334a206f693ed668a3886db1accef47249ba5f5e4cc`; `controlled-request.toml` `43154878e540b32b0d3b21bd022f8de80a81fde78cbc04d4f7a2a718216b0a2b`; `sources/field-operations-note.md` `7f04af1022fdf6d7358a4083a4985b391aecef1d7aa8706f68cf4646e194b08d`. Aggregate (SHA-256 over sorted standard per-file records) `22912363fb5500bd90cfee37f765771dd09b009335fb406176503fc000e60b8b`. |
| Corrected procedure | The disposable execution procedure instantiates `RoleInputs` by name only: `omission_risks_incorrect_performance=False`, `omission_risks_improper_performance=False`, `materially_improves_understanding_or_validation=True`, with the frozen Supporting basis. It encodes no expected ASU/sufficiency/coherence/renderer outcome or PASS decision. |
| Local procedure preflight | [Preflight](raw/roleinputs-preflight.json) constructed only that input: no pipeline executed; both Required triggers were false; the Supporting trigger was true; result **PASS**. |
| Scope | Only F6-D was retested using existing v0.1 interfaces. E+F, J, H, F4-C, F5-B, and F5-C were not executed or prepared. |
| Raw evidence | [Corrected execution script](raw/f6-d-execution.py), [preflight script](raw/f6-d-roleinputs-preflight.py), [raw result](raw/raw-result.json), state/audit database, three renderings, execution streams, [controlled-input manifest](raw/controlled-input-sha256.txt), and [raw SHA-256 manifest](derived/raw-artifact-sha256.md). |

## Observed product result

The local known Source `SRC-F6D-FIELD-OPERATIONS-NOTE` was observed normally
at `atlas/field-operations/current-plan`. It was transformed into
`RI-F6D-ATLAS-STAGING-SAFETY-REVIEW` with direct and normalized Provenance,
became a Candidate, was applicable, was selected as **Supporting**, and was
preserved in the source manifest and logical package
`PKG-F6D-ATLAS-DEPLOYMENT`.

The package preserves `ASU-F6D-ATLAS-DEPLOYMENT`, its explicit nonempty
establishment basis, and `BoundaryAdequacy = indeterminate`. The basis
establishes only the known local boundary and expressly does not assert any
particular omitted Source, Source scope, or relationship. The selected known
Context is not treated as adequate ASU proof. The unbounded task is
**Insufficient** (neither Sufficient nor Conditionally Sufficient) and
coherence is `coherent_with_qualification`.

The logical package, Source Manifest, and each Human, ChatGPT, and Codex
rendering preserve Provenance, ASU identity/basis/state, the evidence-boundary
limitation, and the package/rendering distinction. None claims complete
inspection, universal absence, or a particular missing Source/scope/relationship;
each disclaims delivery, receipt, and use.

## ER-F6-D v1 comparison

| Frozen ER criterion group | Retest evidence | Result |
| --- | --- | --- |
| 1–6: normal observation, Provenance, Candidate, applicable, Supporting, selected | `raw-result.json` records observed Source, provenance-bearing RI, deterministic Candidate, `applicable`, and selected `supporting`; the renderings preserve it. | PASS |
| 7–14: ASU basis/state and no invented gap or adequacy inference | Explicit nonempty basis; `indeterminate`, not adequate or known-incomplete; no named omitted Source/scope/relationship; selected Context does not establish adequacy. | PASS |
| 15–18: sufficiency and coherence | Unbounded package is `insufficient`, not Sufficient/Conditional; coherence is `coherent_with_qualification`. | PASS |
| 19–24: package, manifest, limitation, and all renderers | Logical package and Source Manifest exist; ASU identity/basis/limitation and Provenance are preserved in Human, ChatGPT, and Codex presentations. | PASS |
| 25–30: negative assertions and delivery boundary | No complete-inspection, universal-absence, or invented-gap assertion; package/rendering distinction and no delivery/receipt/use assertion are explicit. | PASS |

No frozen negative/failure criterion was observed. The evidence faithfully
exercises the frozen fixture and establishes **PASS**. No Finding Record is
created.

## Evidence lineage and stop disposition

`VE-F6-D-001` **INDETERMINATE** (immutable, procedure-deficient attempt)
→ `VE-F6-D-002` **PASS** (faithful named-argument retest).

This PASS directly validates 2.6-D only. Item 2.6 remains **INCOMPLETE**;
H remains the governed v0.1 limitation. Gate 4B remains **NOT APPROVED**,
proving **NOT AUTHORIZED**, TD-14 **CLOSED / NOT REOPENED**, and production
readiness is not established.

## Regression and final review

The existing unchanged regression suite completed after the retest: **105
passed** under CPython 3.14.4 / pytest 9.1.1. `git diff --check` passed. No
source or test files are changed; the only worktree changes are this additive
evidence directory and the authorized 2.6-D coverage-review update. No commit
or push was performed.
