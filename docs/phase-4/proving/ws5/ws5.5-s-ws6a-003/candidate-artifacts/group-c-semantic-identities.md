# Group C1 Semantic Identities Candidate

**Status:** **CANDIDATE — NOT FROZEN — PROJECT OWNER APPROVAL PENDING**

This is identity preparation for a possible future successor-004 construction
record. It neither creates successor-004 nor changes any successor-003
identity or binding.

| SemanticIdentity kind | Candidate value | Basis | Validation / limitation |
| --- | --- | --- | --- |
| `request` | `I10-DTS-CONTINUATION-BRIEF-REMEDIATION-v1` | A2 approved request identity | Nonempty kind/value; no persisted object created. |
| `requester` | `project-owner` | A2 approved requester identity | Used only through `Requester(RequesterId(...))` once construction is separately approved. |
| `project` | `day-trading-system` | Effective-project adoption `P4-I10-EFFECTIVE-REVISION-001` | Matches the effective DTS Project; no Project registration is changed. |
| `package` | `I10-DTS-SEMANTIC-PACKAGE-REMEDIATION-CANDIDATE-v1` | New candidate namespace, deliberately distinct from historical successor-003 identities | Candidate only; not a package, freeze, or delivery identity. |
| `record` | `I10-DTS-PACKAGE-CONSTRUCTION-REMEDIATION-CANDIDATE-v1` | New candidate namespace, deliberately distinct from historical successor-003 identities | Candidate only; not a construction record or authorization. |

`SemanticIdentity` validates a supplied nonempty `kind` and `value`; it does
not create authority or establish a repository-wide reservation. The candidate
values are mutually distinct and do not substitute for the unresolved
`Consumer` identity required by `ContextRequest` and `ConsumerContract`.

**Dependencies:** A2 identity approval is established. Approval of the package
and construction-record candidate identities, a separately authorized Consumer
identity, final artifact freeze, successor creation, and execution remain
outside this preparation.
