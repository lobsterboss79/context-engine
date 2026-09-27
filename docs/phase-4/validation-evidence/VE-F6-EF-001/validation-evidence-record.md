# VE-F6-EF-001 — FX-F6-EF v1 Scoped Negative / Bounded Expansion Execution

**Result state:** **PASS**

| Field | Record value |
| --- | --- |
| Evidence / execution | `VE-F6-EF-001`; `2026-09-26T21:28:39.405220-05:00` (America/Chicago; UTC offset `-05:00`; raw UTC `2026-09-27T02:28:39.405220+00:00`). |
| Exact execution baseline | Clean pre-execution `HEAD` `0c1001a347fc62e05ffaa91c4430eba0f0d617f4` — *Prepare Phase 4 bounded expansion control*. `git status --short` was empty. |
| F6-EF materialization baseline | `0c1001a347fc62e05ffaa91c4430eba0f0d617f4` — *Prepare Phase 4 bounded expansion control*. HEAD contains that materialization, approved residual-control disposition (`656047b` ancestor), E+F preparation record, `FX-F6-EF v1`, and `ER-F6-EF v1`. |
| Implementation origin | `IVB-P4-ORIGIN`: `9862497` — *Close Phase 3 v0.1 implementation*; verified ancestor of execution HEAD. It is implementation lineage, not an expected-semantics source. |
| Prior/later control verification | No prior `VE-F6-EF-001` existed in the worktree or Git history before execution. Git history contains no later `ER-F6-EF` revision; `ER-F6-EF v1` is the frozen controlling expected result. |
| Fixture / ER / scope | `FX-F6-EF v1` against `ER-F6-EF v1`, only. No J preparation/execution, H simulation, F4-C/F5-B/F5-C execution, or F6-D rerun occurred. |
| Synthetic / authority boundary | `fixture-harbor-f6ef` is explicitly synthetic and has no production authority. |
| Controlled hashes | `bootstrap.toml` `3cd49b98a18a75fbf26b1a3fddce4c256d10d7330f8a89795a5b7fd4d0a50184`; `project.toml` `a46568e2eedafde3e700b29b953bd945958de9523b275f6225ebd9a625085ff2`; `controlled-request.toml` `6d69ba781811f67c96135d1b24375c309b094f2666a8e5b994fb57f456f4f2e5`; `sources/origin-register.md` `b3c3c4173086b4d25e97a8e92f33c7c22bdd5dac418ca6443677457988708c48`; `sources/expansion-target-annex.md` `431c2c4870029999a82f9971a53e92eb629153cb12f050797620be35847d444b`. Aggregate: `ea14628675d9614d54f32d24ab7f13eb6722a412c1da8ae22e14359671133f34`. |
| Procedure preflight | [Preflight](raw/procedure-preflight.json) is a local TOML-only check and records `pipeline_executed: false`, all ten required checks true, and PASS. It verified the two-Source ASU, origin-only initial state, expansion-only target, frozen ExpansionRequest fields/basis, one-target plan, exact-literal-only query, no second target, and no injected PASS/Sufficient/coherence outcome. |
| Raw evidence / integrity | [Procedure](raw/f6-ef-execution.py), [execution result](raw/raw-result.json), [stdout](raw/f6-ef-execution.stdout), [stderr](raw/f6-ef-execution.stderr), three [renderings](raw/rendering-human.md), [controlled-input manifest](raw/controlled-input-sha256.txt), aggregate record, and [raw SHA-256 manifest](derived/raw-artifact-sha256.md). |

## Observed controlled execution

Task `REQ-F6EF-HARBOR-SCOPED-IDENTIFIER-REPORT` used exact query
`CE-F6EF-ABSENT-IDENTIFIER-7Q3M` and adequate ASU
`ASU-F6EF-HARBOR-SCOPED-REPORT`. The ASU basis names exactly
`SRC-F6EF-HARBOR-ORIGIN` and `SRC-F6EF-HARBOR-EXPANSION-TARGET`, both governed
and available for this bounded reporting task. The exact literal was verified
absent from both Source contents before execution.

The origin was normally observed, transformed, and represented as
`RI-F6EF-HARBOR-ORIGIN-REGISTER`, with direct and normalized Provenance. Its
represented relationship is `REL-F6EF-HARBOR-ORIGIN-TO-ANNEX`, targeting only
`SRC-F6EF-HARBOR-EXPANSION-TARGET`. The initial discovery record preserves
`initial_inspected_sources = [SRC-F6EF-HARBOR-ORIGIN]`, no expanded Source,
and zero exact matching Candidates. This establishes the frozen
`DEF-F6EF-INITIAL-EXACT-QUERY-ABSENCE`; it is material, resolvable,
authorized, and in scope.

The pre-frozen `EXP-F6EF-HARBOR-ONE-HOP` uses that origin RI, represented
relationship, target, `material_resolvable_deficiency = true`,
`inspection_authorized = true`, and its nonempty frozen basis. The bounded
iteration plan records the origin ASU boundary, exactly the target as its only
additional Source, and `authorized_to_discover = true`. Only then was the
expansion-only target normally observed, transformed, and represented with
Provenance. Final discovery preserves
`expanded_inspected_sources = [SRC-F6EF-HARBOR-EXPANSION-TARGET]` and effective
inspection of origin then target. No excluded Source, second target, second
hop, recursion, or crawl occurred.

The final result contains zero matching Candidates. It is no-result evidence,
not a Candidate made inapplicable, excluded by policy, or rejected during
selection. The retained scope is **not found within the governed inspected
ASU**: it does not decide whether the identifier exists outside the two
governed Sources. The retained termination basis is origin inspection;
authorized one-hop target inspection; no exact match in either Source; sole
path exhausted; no second hop authorized.

Sufficiency is `sufficient` only for this bounded reporting task: the ASU is
adequate, both governed Sources were inspected by termination, and no Required
deficiency exists for reporting that scoped result. Coherence is `coherent`.
The logical package retains the two-Source universe and material qualified
inspection/result facts. With zero selected Candidates, its Source Manifest is
empty by the existing selected-Provenance interface; raw observations preserve
both Source Provenance and the logical package preserves the Source universe
and qualifications. Human, ChatGPT, and Codex renderings were all `rendered`,
retain the bounded scope and one-hop facts, remain distinct from the logical
package, and make no delivery, receipt, or use assertion.

## ER-F6-EF v1 comparison

| Frozen ER criterion group | Evidence | Result |
| --- | --- | --- |
| 1–5: adequate ASU, two Sources, origin-only initial state, no origin match | `raw-result.json` ASU, initial discovery, source observations, and controlled hashes | PASS |
| 6–12: material deficiency, represented relationship, pre-frozen authorized one-hop expansion, target-only expanded state | Raw deficiency, ExpansionRequest, iteration plan, final discovery, and target observation | PASS |
| 13–16: zero Candidates, scoped negative result, explicit bounded termination, no second hop/crawl | Final discovery plus construction termination basis and rendering qualifications | PASS |
| 17–18: Sufficient only for reporting and coherent | Raw sufficiency decision and construction record | PASS |
| 19–21: logical package, source/provenance evidence, all renderers, package/rendering/delivery boundary | Raw package/construction and three rendering artifacts | PASS |

No frozen negative/failure criterion was observed: Sources were not statically
inspected from the start; target was not initial; no automatic traversal,
ungoverned expansion, second hop, Candidate substitution, universal-absence
claim, generalized sufficiency, or delivery/receipt/use assertion occurred.
There is no finding. **TD-14 TRIGGER NOT MET**: the expected exhaustion of this
adequate bounded reporting ASU is not a deterministic-discovery deficiency.

## Coverage and stop disposition

This PASS directly validates only WS2 Items **2.6-E** and **2.6-F**. The
[coverage review](../ws2-item-2.6-asu-coverage-review.md) now records A, B, C,
D, E, F, G, I, K as directly validated; H as supporting only; and J as not yet
validated. Item 2.6 remains **INCOMPLETE**. H remains the Project
Owner-governed v0.1 validation limitation. Gate 4B remains **NOT APPROVED**;
proving remains **NOT AUTHORIZED**; TD-14 remains **CLOSED / NOT REOPENED**;
and production readiness is not established. Stop: no J work was prepared or
executed.

## Regression and final review

The unchanged regression suite completed: **105 passed** under CPython 3.14.4
and pytest 9.1.1. `git diff --check` passed. No application/source, test,
fixture, ER, controlled Source, query, relationship, or task-boundary file was
modified. The worktree changes are limited to this additive evidence directory
and the authorized E/F coverage-review update; no commit or push was performed.
