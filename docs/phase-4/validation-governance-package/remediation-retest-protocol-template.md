# Remediation and Retest Protocol/Template

**Template status:** Remediation is not authorized by this template or by discovery of a finding. Use only in an authorized remediation context.

## Remediation Record

| Field | Record value |
| --- | --- |
| Remediation ID | `R-[stable ID]` |
| Linked finding/evidence | `[F-/VE- IDs]` |
| Causal hypothesis | `[evidence-based hypothesis]` |
| Approved expected behavior | `[ER-ID/version and governing reference]` |
| Authorized change boundary | `[explicit boundary]` |
| Authority | `[authority/date/decision]` |
| Originating baseline | `[IVB/derived baseline]` |
| Affected components/semantics | `[future analysis]` |
| Anticipated regression surface | `[future analysis]` |
| Retest plan | `[levels and rationale]` |
| Exact derived baseline after remediation | `[future commit/version]` |
| Actual change boundary | `[actual change and comparison to authorization]` |
| Level 1 focused retest | `[evidence/rationale]` |
| Level 2 affected-suite retest | `[evidence/rationale]` |
| Level 3 relevant end-to-end regression validation | `[evidence/rationale]` |
| Residual limitations | `[future statement]` |
| Prior-evidence/proving impact | `[validity/narrowing/invalidation/fresh-run assessment]` |
| Closure recommendation | `[recommendation; not disposition]` |

Material remediation presumptively requires every applicable retest level unless a governed record explains non-applicability. Security/governance remediation evaluates corrected and reasonably related enforcement paths. A changed baseline never rewrites the original baseline or original FAIL/INDETERMINATE.

## Generalization Review — material remediation discovered through proving

| Question | Review record |
| --- | --- |
| What approved requirement/invariant was violated? | `[future answer]` |
| Can correction be stated without the proving Project identity? | `[future answer]` |
| Would the same mechanism apply to another Project with the same condition? | `[future answer]` |
| Is there a controlled non-proving regression case for the general mechanism? | `[future answer/evidence]` |

Do not hard-code a proving case, Project vocabulary/identity, Consumer identity, expected answer, proving-specific keyword, or special path. If this review cannot be satisfied without a material decision, stop under H3.
