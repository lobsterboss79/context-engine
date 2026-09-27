# WS2 Item 2.6 — Residual Control Authorization Disposition

**Status:** **PROJECT OWNER APPROVED / PRE-RESULTS PREPARATION AUTHORIZED**

## 1. Decision context

The Project Owner reviewed and approved the residual direct-gap design work for WS2 Item 2.6. This disposition records the Project Owner's six decisions for the residual controls. It authorizes only future pre-results preparation under the sequence in this record; it does not authorize fixture creation in this documentation change, execution, validation evidence, proving, or any completion disposition.

Item 2.6 remains **INCOMPLETE**. Items 2.7–2.11 remain **INCOMPLETE**. Gate 4B remains **NOT APPROVED**, proving remains **NOT AUTHORIZED**, and production readiness is not established.

## 2. Relationship to the committed residual-gap design analysis

This is the Project Owner disposition of [`ws2-item-2.6-residual-gap-design-analysis.md`](ws2-item-2.6-residual-gap-design-analysis.md), whose status was design analysis complete with pre-results controls not yet authorized. It accepts the analysis's ready-control conclusions for D, combined E+F, and J/J1; its three-control separation; J's Artifact-versus-Source framing; the non-expressibility limitation for H; and its TD-14 assessment.

This disposition does not rewrite, supersede, or alter the analysis's historical conclusions or any evidence classification.

## 3. 2.6-D — Indeterminate ASU authorization

The Project Owner approves future pre-results fixture/expected-result preparation for **2.6-D — Indeterminate ASU** using one controlled local Project, one known local inspected Source/scope, and a known task. The ASU establishment basis must be explicit and nonempty. Available governed boundary/inventory evidence must be unable reliably to establish whether another Source or Source scope is applicable, without asserting any particular omitted material Source, scope, or relationship.

The ASU must genuinely be `indeterminate`, not `known_incomplete`. The task must be unbounded, not a separately safe bounded subtask. The frozen expected outcome is **Insufficient**, with coherence `coherent_with_qualification`; a logical package is expected with explicit indeterminate-ASU qualification. Renderings must preserve that qualification and must not claim universal absence or complete inspection.

## 4. 2.6-E + 2.6-F — Scoped negative result and bounded expansion authorization

The Project Owner approves future pre-results fixture/expected-result preparation for one combined controlled scenario for **2.6-E — scoped negative results** and **2.6-F — bounded expansion**.

The scenario must use one controlled local Project and one adequate governed ASU containing an initial Source and one expansion-only Source. Only the initial Source is inspected at first. Its inspection establishes a supplied material, potentially resolvable deficiency. A represented governed relationship identifies the only approved expansion target, authorization permits that one-hop expansion, and an explicit `ExpansionRequest` or approved equivalent invokes the existing bounded expansion mechanism. The expansion-only Source is then inspected.

The exact controlled target information must be absent from both inspected Sources, and bounded termination must occur after the sole authorized hop. The negative result must mean only **“not found within the governed inspected ASU”** or a repository-approved semantically equivalent wording; it must not mean “does not exist.” Candidate or applicability exclusion must not substitute for the negative result.

For the explicitly bounded reporting task, the frozen expected outcome is **Sufficient** with `coherent` coherence. The package and renderings must preserve the initial inspected Source set, expanded inspected Source set, expansion basis, governed relationship, termination basis, and scoped negative-result boundary. The ASU is not dynamically enlarged: the inspected set changes within the already-governed ASU.

## 5. 2.6-J / J1 — Unsupported Artifact capability authorization

The Project Owner approves future pre-results fixture/expected-result preparation for **2.6-J — unsupported capability** and accepts **J1 — REAL V0.1 UNSUPPORTED CONDITION EXISTS**.

The approved boundary is a governed local-Git Source that is available, authorized, and in governed task/ASU scope, with relevant Required information in an Artifact whose format is outside the approved v0.1 Markdown observation/transformation capability. Preparation must use the already approved non-Markdown PDF/Office Artifact capability boundary. It must not invent a new Source technology, adapter, connector, protocol, or external service.

The Source remains available, authorized, and in scope; the unsupported Artifact outcome must be preserved; no represented information may be fabricated from that Artifact; and the Required deficiency and ASU/capability limitation must remain explicit. The frozen expected outcome is **Insufficient** with `coherent_with_qualification` coherence. Logical package and renderings must preserve the unsupported capability limitation and must not relabel it unavailable, inaccessible, unauthorized, absent, or universally nonexistent.

## 6. Approved control grouping

The minimum presently preparable control set is three separate controls:

1. D — Indeterminate ASU.
2. E+F — Bounded expansion plus scoped negative result.
3. J — Unsupported Artifact capability.

D must not be combined with E+F. J must not be combined with D or E+F. Their evidence conditions must remain independently attributable.

## 7. J Artifact-versus-Source framing

For J, **Source != Artifact capability**. The Source remains registered and governed as applicable, available, authorized, and in scope. The limitation is specifically that the Required Artifact cannot be observed/transformed because its format is unsupported by the approved v0.1 Artifact capability.

Preparation must not describe the Source itself as unsupported unless the approved model independently requires that terminology. Unsupported format must not be treated as inaccessible or unavailable.

## 8. 2.6-H disposition

The Project Owner disposition is:

> “2.6-H remains an open validation limitation for v0.1. The approved semantics distinguish inaccessible Sources, but the current approved v0.1 observation interfaces do not expose a deterministic distinct inaccessible outcome. No synthetic enum-only fixture is authorized, and no application change is authorized solely to manufacture validation coverage. The limitation will remain explicitly documented pending later implementation capability or a future governed disposition.”

Accordingly, no H fixture or expected-result record may be created; no inaccessibility may be simulated by manually asserting an enum or filesystem permission tricks; no application/source change is authorized solely to make H testable; unavailable behavior must not be relabeled inaccessible; and H must not be marked directly validated. This is a governed validation limitation, not an H3 semantic ambiguity.

## 9. Item 2.6 completion consequence

Item 2.6 remains **INCOMPLETE**. Even if separately authorized D, E+F, and J executions later pass, 2.6-H will still lack direct v0.1 validation evidence under this disposition. No Item 2.6 completion is pre-authorized; any future Item 2.6 disposition after D/E+F/J validation must separately address the preserved H validation limitation.

## 10. TD-14 disposition

None of the approved D, E+F, or J controlled scenarios, if behaving as expected, is a TD-14 reopening candidate. H's v0.1 expressibility limitation also does not itself meet the TD-14 reopening threshold. TD-14 remains **CLOSED / NOT REOPENED**.

## 11. Exact authorization boundary

Authorized: future pre-results preparation and freezing of the D, E+F, and J fixture/expected-result controls, one control at a time and only in the approved sequence below.

Not authorized by this disposition: creation of any fixture, expected-result record, controlled Source/TOML file, hash, validation evidence, finding, or execution; application/source or test change; alteration of existing fixture, expected-result, or evidence semantics; H implementation or synthetic H coverage; Item 2.6 completion; Gate 4B approval; proving; TD-14 reopening; or any production-readiness claim.

## 12. Recommended preparation sequence

The approved sequence is:

1. Prepare/freeze D.
2. Review/commit D pre-results controls.
3. Execute D only after separate authorization.
4. Prepare/freeze E+F.
5. Review/commit E+F pre-results controls.
6. Execute E+F only after separate authorization.
7. Prepare/freeze J.
8. Review/commit J pre-results controls.
9. Execute J only after separate authorization.

Execution authorization must not be batched. This preserves the Phase 4 pre-results review boundary used for prior controls.

## 13. Non-execution attestation

This record is governance/documentation only. It creates no D, E+F, J, or H fixture; no expected-result record; no controlled Source/TOML file; no hash; no validation evidence; and no finding. No fixture was executed. No application/source or test file was changed. No existing fixture, expected result, or validation evidence was modified. Item 2.6 remains **INCOMPLETE**; Gate 4B remains **NOT APPROVED**; proving remains **NOT AUTHORIZED**; TD-14 remains **CLOSED / NOT REOPENED**; and production readiness is not claimed.
