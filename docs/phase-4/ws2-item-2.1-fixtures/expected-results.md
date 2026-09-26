# WS2 Item 2.1 — Frozen Expected-Result Records

**Register status:** Pre-execution. Every record is `v1`, **governed for
authorized execution**, and frozen at the WS2 Item 2.1 fixture-design baseline
`c9b39a3`. This status is not PASS, FAIL, or INDETERMINATE; no execution has
occurred. Revision requires a new version, governing rationale, and applicable
approval—never overwriting this record to fit an observed result.

**Shared governing/approval basis:** Project Owner-approved Phase 0–3 baseline;
WS1 expected-result controls; Gate 4A PASS / Project Owner approval; Phase 4
execution authorization; Project Owner approval of the Item 2.1 fixture
architecture. Detailed semantic references and controlled inputs are frozen in
[fixture records](fixture-records.md). Future affected-evidence placeholder for
each record: `VE-[future stable ID]`; reviewer basis: cited governing semantic
records, not implementation output.

## ER-F1 v1

| Template field | Frozen value |
| --- | --- |
| Governing requirement/design reference | P0 §§4–12; P2 Domain E DS-02/selection/sufficiency; P2 Domain F; P3 WS8 and WS9. |
| Validation/checklist relationship | WS2 Item 2.1; future WS2 Items 2.2 and 2.8 execution. |
| Controlled fixture/input identity | `FX-F1 v1`; `F1/bootstrap.toml`, `F1/project.toml`, `F1/sources/atlas-charter.md`, `F1/sources/atlas-delivery.md`. |
| Bootstrap/configuration/environment basis | Explicit v1 TOML files; `fixture-atlas-f1`; exact committed baseline `c9b39a3`; future controlled local validation environment to be separately recorded. |
| Governed expectation | Represent two provenance-bearing items; form applicable Candidates; select one Required constraint and one Supporting availability item; construct a coherent, Sufficient logical package and faithful authorized renderings. |
| Acceptance criteria | Required/Supporting, both Sources' lineage/manifest, `Sufficient`, and coherent state survive through each renderer; no renderer asserts delivery/receipt/use. |
| Negative/failure criteria | Any role collapse, omitted provenance, artificial conflict/uncertainty, inadequate-ASU claim, loss of package/rendering distinction, or semantic renderer loss. |
| Limitations / reviewer / authority / lineage | No byte identity required; review against records above; approving authority as shared basis; initial frozen version, no predecessor. |

## ER-F2 v1

| Template field | Frozen value |
| --- | --- |
| Governing requirement/design reference | P1 Context Item; P2 D D7; P2 E DS-02, DS-09, selection/sufficiency; P3 WS6–WS8. |
| Validation/checklist relationship | WS2 Item 2.1; future WS2 Items 2.3–2.5 and 2.8. |
| Controlled fixture/input identity | `FX-F2 v1`; `F2/bootstrap.toml`, `F2/project.toml`, `F2/sources/atlas-boundaries.md`. |
| Bootstrap/configuration/environment basis | Explicit v1 TOML; `fixture-atlas-f2`; `c9b39a3`; future environment separately recorded. |
| Governed expectation | Preserve four represented items; only three become Candidates; select Required constraint and Supporting label; exclude historical non-applicable Candidate and irrelevant non-Candidate; package is Sufficient. |
| Acceptance criteria | Boundary reasons remain distinct: represented ≠ Candidate ≠ selected; discovery ≠ applicability ≠ selection ≠ sufficiency; included items retain provenance and renderer fidelity. |
| Negative/failure criteria | Selecting history/irrelevant material merely because represented/discovered; failing to represent excluded material; treating score/order as applicability; insufficient/conditional result without governed basis. |
| Limitations / reviewer / authority / lineage | Explicit task mapping is fixture governance, not inferred semantic similarity; shared reviewer/authority basis; initial frozen version. |

## ER-F3 v1

| Template field | Frozen value |
| --- | --- |
| Governing requirement/design reference | P0 §§5–10; P1 Conflict/Uncertainty; P2 D D15–D16; P2 E SEL-02/sufficiency; P2 F F16; P3 WS7–WS9. |
| Validation/checklist relationship | WS2 Item 2.1; future WS2 Items 2.4, 2.5, 2.7, and 2.8. |
| Controlled fixture/input identity | `FX-F3 v1`; `F3/bootstrap.toml`, `F3/project.toml`, and four named F3 source files. |
| Bootstrap/configuration/environment basis | Explicit v1 TOML; `fixture-atlas-f3`; `c9b39a3`; future environment separately recorded. |
| Governed expectation | Preserve two competing current Approved decisions as unresolved Conflict, one historical supporting claim, and unverified availability; select all relevant context with distinct lineage; package is Insufficient and coherent-with-qualification. |
| Acceptance criteria | No newer-wins/order/model resolution; conflict participants/currentness/historical role/uncertainty/provenance remain explicit in logical package and all renderings. |
| Negative/failure criteria | Resolving or omitting material conflict; promoting historical claim to current; presenting unverified availability as established; calling the package Sufficient. |
| Limitations / reviewer / authority / lineage | Fixture metadata supplies scoped governance rather than elevating Markdown; shared reviewer/authority basis; initial frozen version. |

## ER-F4-A v1

| Template field | Frozen value |
| --- | --- |
| Governing requirement/design reference | P2 E SEL-04/sufficiency; P2 F; P3 WS8–WS9. |
| Validation/checklist relationship | WS2 Item 2.1; future WS2 Items 2.5, 2.8, 2.9. |
| Controlled fixture/input identity | `FX-F4-A v1`; `F4-A/bootstrap.toml`, `F4-A/project.toml`, `F4-A/sources/release-decision.md`. |
| Bootstrap/configuration/environment basis | Explicit v1 TOML; `fixture-atlas-f4`; `c9b39a3`; future environment separately recorded. |
| Governed expectation | Available, authorized Required decision is observed through selected with provenance; coherent Sufficient package and faithful all-Consumer renderings. |
| Acceptance criteria | Required status, adequate ASU, sufficiency, manifest/provenance, and renderer semantic preservation are explicit. |
| Negative/failure criteria | Omission/downgrade of Required context, unjustified qualification, absent lineage, or renderer semantic loss. |
| Limitations / reviewer / authority / lineage | Control case only; shared reviewer/authority basis; initial frozen version. |

## ER-F4-B v1

| Template field | Frozen value |
| --- | --- |
| Governing requirement/design reference | P1 ASU/uncertainty; P2 C C5/C12; P2 E Required limitation/sufficiency; P3 WS8; P3 WS9. |
| Validation/checklist relationship | WS2 Item 2.1; future WS2 Items 2.5–2.6 and 2.8. |
| Controlled fixture/input identity | `FX-F4-B v1`; `F4-B/bootstrap.toml`, `F4-B/project.toml`, `F4-B/sources/available-support.md`, named unavailable required Source. |
| Bootstrap/configuration/environment basis | Explicit v1 TOML; `fixture-atlas-f4`; `c9b39a3`; future environment separately recorded. |
| Governed expectation | Required deficiency and unavailable/ASU limitation remain explicit; supporting item may be selected; result is Insufficient, never silently sufficient. |
| Acceptance criteria | Missing Required identity/basis and non-disclosing qualification survive logical package/rendering; selected support does not substitute for it. |
| Negative/failure criteria | Treating unavailable as nonexistent, omitting deficiency, Conditional Sufficiency without a separately supplied safe bounded task, or fabricating required content. |
| Limitations / reviewer / authority / lineage | No claim about contents of unavailable Source; shared reviewer/authority basis; initial frozen version. |

## ER-F4-C v1

| Template field | Frozen value |
| --- | --- |
| Governing requirement/design reference | P0 §12; P2 B B7; P2 E Required limitation; P2 F; P3 WS8–WS9. |
| Validation/checklist relationship | WS2 Item 2.1; future WS2 Items 2.5, 2.7–2.9. |
| Controlled fixture/input identity | `FX-F4-C v1`; `F4-C/bootstrap.toml`, `F4-C/project.toml`, `F4-C/sources/restricted-decision.md`. |
| Bootstrap/configuration/environment basis | Explicit v1 TOML; `fixture-atlas-f4`; `c9b39a3`; future environment separately recorded. |
| Governed expectation | Requester inspection authorization does not transfer Consumer disclosure. The Required item remains semantically Required but disclosure-denied; result is Denied, with no logical package or Consumer content leak. |
| Acceptance criteria | Non-sensitive denial/qualification only; no restricted content, provenance, metadata, reference, or package identifier rendered. |
| Negative/failure criteria | Disclosure of protected material; fake empty/partial Sufficient package; role downgrade; confusing Requester and Consumer authorization. |
| Limitations / reviewer / authority / lineage | Restricted content itself is synthetic but must remain undisclosed in future Consumer result; shared reviewer/authority basis; initial frozen version. |

## ER-F4-D v1

| Template field | Frozen value |
| --- | --- |
| Governing requirement/design reference | P2 E SEL-04; P2 F capacity/F16; P3 WS7 §37; P3 WS8; P3 WS9 §§7–11. |
| Validation/checklist relationship | WS2 Item 2.1; future WS2 Items 2.5, 2.8–2.9. |
| Controlled fixture/input identity | `FX-F4-D v1`; `F4-D/bootstrap.toml`, `F4-D/project.toml`, `F4-D/sources/release-decision.md`. |
| Bootstrap/configuration/environment basis | Explicit v1 TOML; `fixture-atlas-f4`; `c9b39a3`; exact declared capacity `1` character below complete faithful output; future environment separately recorded. |
| Governed expectation | Logical package remains coherent and Sufficient; constrained rendering explicitly fails with no content because Required context and qualifications may not be truncated, waived, or downgraded. |
| Acceptance criteria | Required status and logical package remain unchanged; no delivery/receipt/use assertion; every constrained renderer reports failure without payload. |
| Negative/failure criteria | Truncation, Supporting conversion, silent omission, false rendered status, or treating rendering failure as package insufficiency. |
| Limitations / reviewer / authority / lineage | v0.1 has no approved condensation/reference/multipart alternative; shared reviewer/authority basis; initial frozen version. |

## ER-F5-A v1

| Template field | Frozen value |
| --- | --- |
| Governing requirement/design reference | P0 §§11–12; P2 B B7–B8; P2 C C5; P3 WS6–WS7. |
| Validation/checklist relationship | WS2 Item 2.1; future WS2 Items 2.6, 2.8, 2.10. |
| Controlled fixture/input identity | `FX-F5-A v1`; `F5-A/bootstrap.toml`, `F5-A/project.toml`, Atlas task and Beacon note files. |
| Bootstrap/configuration/environment basis | Explicit v1 TOML; `fixture-atlas-f5`; `c9b39a3`; cross-Project authorization denied. |
| Governed expectation | Default isolation excludes Beacon before representation/Candidate use; Atlas Required task item alone yields sufficient Atlas package and authorized renderings. |
| Acceptance criteria | No Beacon content, metadata, provenance, relationship, or authorization implication enters package/renderings; Atlas origin remains explicit. |
| Negative/failure criteria | Traversal/retrieval because useful, merging Project scope, or any Beacon leak. |
| Limitations / reviewer / authority / lineage | It tests an explicit denial rather than real permission infrastructure; shared reviewer/authority basis; initial frozen version. |

## ER-F5-B v1

| Template field | Frozen value |
| --- | --- |
| Governing requirement/design reference | P0 §11; P2 B B8; P2 E DS-02/selection; P3 WS6–WS7. |
| Validation/checklist relationship | WS2 Item 2.1; future WS2 Items 2.3–2.4, 2.8, 2.10. |
| Controlled fixture/input identity | `FX-F5-B v1`; `F5-B/bootstrap.toml`, `F5-B/project.toml`, Atlas task and Beacon note files. |
| Bootstrap/configuration/environment basis | Explicit v1 TOML; `fixture-atlas-f5`; `c9b39a3`; bounded crossing and both authorizations established. |
| Governed expectation | Beacon note is represented/Candidate with origin preserved but inapplicable and excluded; Atlas Required item is selected; package is Sufficient. |
| Acceptance criteria | Traversal authorization does not cause selection; exclusion reason and distinct Project provenance remain explainable; renderer lacks Beacon selected context. |
| Negative/failure criteria | Relevance inferred from mere availability/usefulness, cross-Project Authority propagation, or Beacon selection. |
| Limitations / reviewer / authority / lineage | One bounded relationship only; shared reviewer/authority basis; initial frozen version. |

## ER-F5-C v1

| Template field | Frozen value |
| --- | --- |
| Governing requirement/design reference | P0 §§11–12; P1 relationships/provenance; P2 B B8; P2 E; P3 WS6–WS9. |
| Validation/checklist relationship | WS2 Item 2.1; future WS2 Items 2.3–2.4, 2.8, 2.10. |
| Controlled fixture/input identity | `FX-F5-C v1`; `F5-C/bootstrap.toml`, `F5-C/project.toml`, Atlas task and Beacon supply files. |
| Bootstrap/configuration/environment basis | Explicit v1 TOML; `fixture-atlas-f5`; `c9b39a3`; request, relationship, Requester, and Consumer authorization explicitly permit bounded Beacon source. |
| Governed expectation | Atlas Required task and Beacon Supporting compatibility confirmation are represented/Candidates/applicable/selected; origin remains separate; two-Source adequate ASU produces sufficient package. |
| Acceptance criteria | Package/each renderer show bounded relationship, separate provenance/manifest, Required vs Supporting roles, and no automatic Authority transfer or transitive traversal. |
| Negative/failure criteria | Beacon loss despite authorization/relevance, unbounded traversal, Project merge, authority laundering, or cross-Project disclosure beyond named Source. |
| Limitations / reviewer / authority / lineage | Controlled relationship is fixture-only and has no production authority; shared reviewer/authority basis; initial frozen version. |

No record in this register is linked to actual evidence, a result state, a finding, remediation, Consumer preflight, or proving activity.
