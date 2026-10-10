# A1 Candidate DTS Bootstrap and Project Configuration Assessment

**Status:** **CANDIDATES VALIDATED — PROJECT OWNER CONFIGURATION APPROVAL REQUIRED**

## Authority and boundary

Project Owner decision A1 authorizes preparation and validation of these two
candidate artifacts only. It does not approve either artifact, establish an
operator authorization, authorize package construction or rendering, create a
successor, transfer a Consumer binding, disclose evidence, or authorize WS6A/
WS6B. `WS5.5-S-WS6A-003` remains unchanged historical frozen control evidence.

The artifacts use the production TOML contract in
`src/context_engine/application/bootstrap.py`. There is no authorization field
in either TOML. `operator_authorized` is a separate runtime argument and must
receive separate authority before any governed construction call.

## Candidate values and provenance

| Candidate / field | Value classification | Basis and implication |
| --- | --- | --- |
| `dts-bootstrap.toml`: `version = 1` | Recovered production requirement | `establish_bootstrap` accepts only version 1. |
| Bootstrap `project` | Recovered | `day-trading-system`, from P4-I10-EFFECTIVE-REVISION-001 and the active corpus. |
| Bootstrap `scope` | Recovered naming / candidate use | `authorized-eight-governed-project-markdown`, the frozen corpus Source-scope identifier. It identifies a bounded upstream observation scope; it does not disclose raw Sources. |
| Bootstrap `governance_basis` | Newly proposed, bounded candidate text | References the effective-revision record and A1's preparation-only limitation. It creates no authority. |
| Bootstrap `project_configuration` | Recovered implementation convention / newly chosen relative filename | `dts-project.toml` is a same-directory relative reference, resolved by the production loader. Owner must approve the artifact pair together. |
| `dts-project.toml`: `version = 1` | Recovered production requirement | `load_project_configuration` accepts only version 1. |
| Project `identity` | Recovered | Matches bootstrap and approved Project identity exactly. |
| Project `governance_reference` | Newly proposed, bounded candidate text | References P4-I10-EFFECTIVE-REVISION-001 and preserves the frozen/no-WS6A boundary. It is not an authorization token or disclosure grant. |

No value conveys a repository path, raw Markdown, semantic assertion,
evaluator/expected-answer content, Consumer identity, credentials, tool
permission, or project-execution authority.

## Candidate identities and exact bytes

| Artifact | Repository path | UTF-8 bytes | SHA-256 | Terminal newline |
| --- | --- | ---: | --- | --- |
| Bootstrap | `candidate-artifacts/dts-bootstrap.toml` | 348 | `d18b2ed34150e0fbc782609917f6ddf97a65a8901eda90a188db144a3858f832` | present (`0a`) |
| Project configuration | `candidate-artifacts/dts-project.toml` | 226 | `feb449068bff66ab9521ff5acd6425671073ef8e54e02058d07cfc7a9ccd3ee0` | present (`0a`) |

These are candidate byte identities only. They are neither a freeze nor an
exact-run binding.

## Production validation

The candidate pair must satisfy all of the following existing checks:

1. TOML parses; each top-level `version` is integer `1`.
2. Bootstrap has a `[bootstrap]` table with nonempty string `project`, `scope`,
   `governance_basis`, and `project_configuration`.
3. The relative project configuration reference resolves to this candidate
   pair's `dts-project.toml` path.
4. Project configuration has `[project]` with matching nonempty `identity` and
   nonempty `governance_reference`.
5. A call with `operator_authorized=False` must fail closed before bootstrap
   establishment. A structural parsing test may use `True` solely to exercise
   the parser/matching contract; it does not establish real operator authority.

**Result:** PASS. Both TOMLs parse through the production loader with the
expected matching Project/configuration reference when exercised structurally.
The `operator_authorized=False` control fails closed as required.

## Outstanding Owner decisions

1. Approve or decline both candidate TOML byte artifacts, including their
   proposed governance-basis/reference text and relative pairing.
2. Later, separately authorize an operator for a governed construction call;
   A1 does not supply that authorization.
3. Resolve the remaining canonical construction-input decisions (Context
   Request, ASU basis, discovery, applicability/roles, sufficiency/coherence,
   identities, and ConsumerContract) before any construction is attempted.

No configuration-specific technical blocker remains. These candidates are not
approved, frozen, or a replacement for the missing canonical construction-input
record.
