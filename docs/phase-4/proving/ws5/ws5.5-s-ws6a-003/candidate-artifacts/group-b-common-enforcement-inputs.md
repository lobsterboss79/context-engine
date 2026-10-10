# Candidate Common Enforcement Inputs — Group B

**Status:** **CANDIDATE — NOT FROZEN — OWNER APPROVAL PENDING**

This maps directly to `EnforcementInputs` in
`application/decision_pipeline.py`. It is intentionally not an instantiable
runtime value while required authorization facts remain unresolved.

| Field | Proposed value / state | Evidence / dependency |
| --- | --- | --- |
| `bootstrap_valid` | **UNRESOLVED**; may be `True` only after a separately authorized runtime bootstrap validation | A1 proves candidate TOML bytes, not runtime operator authorization or bootstrap establishment. |
| `request_project` / `candidate_project` | `SemanticIdentity("project", "day-trading-system")` | A2 and active corpus; same-Project scope. |
| `requester_authorized` | **UNRESOLVED** | Owner authorized Group A/B preparation, not Context Package construction. |
| `consumer_disclosure_authorized` | **UNRESOLVED** | No Group C ConsumerContract or delivery authority exists. |
| `protected_metadata_authorized` | Proposed `True` for the approved semantic field allowlist only | No protected/raw/evaluator material is a Group B input; Owner must approve the runtime value. |
| `task_requires_current` | Proposed `False` | Frozen task requires distinguishing current, historical, and superseded information, not a current-only task. |
| `task_is_historical` | Proposed `False` | Frozen task is a continuation brief, not a historical-only task. |
| `task_domain` | Proposed `day-trading-system-governed-continuation` | Narrow task label; Owner decision. |
| `task_phase` | Proposed `phase-3-continuation` | Frozen task asks current phase/state and next legitimate boundary; no Phase 3 implementation is asserted. |
| `task_action` | Proposed `brief` | Report-only task; Owner decision. |
| `requires_governing_authority` | Proposed `False` | Task requests no decision, authorization, or governed action. Semantic bases remain evidence. |
| `instructional_use_requested` / `instructional_authority_established` | `False` / `False` | Claim text is inert evidence; no instruction use is requested. |
| `cross_project_prerequisites` | `False` | A3 scope is one local DTS Project; no expansion is authorized. |

Until `bootstrap_valid`, `requester_authorized`, and
`consumer_disclosure_authorized` are established as `True` by separate Owner
authority, `evaluate_applicability` must fail closed. This candidate grants no
operator, disclosure, or Consumer authority.
