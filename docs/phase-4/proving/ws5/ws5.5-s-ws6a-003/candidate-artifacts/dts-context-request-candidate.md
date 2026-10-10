# Candidate Context Request — Group A

**Status:** **INCOMPLETE CANDIDATE — GROUP C CONSUMER REQUIRED**

This is a direct constructor record for the existing `ContextRequest`
dataclass, not a new runtime schema. It must not be instantiated for package
construction until its required Consumer is separately approved.

```text
ContextRequest(
  identity=SemanticIdentity("request", "I10-DTS-CONTINUATION-BRIEF-REMEDIATION-v1"),
  project=SemanticIdentity("project", "day-trading-system"),
  requester=Requester(RequesterId(SemanticIdentity("requester", "project-owner"))),
  consumer=UNRESOLVED_GROUP_C_CONSUMER,
  intent=TaskIntent("Prepare a concise bounded Day Trading System continuation brief from governed Context Engine evidence."),
  scope=TaskScope("State the Project purpose; current phase/state; governing decisions and current authorization boundary; constraints and known gaps; current, historical, or superseded information; material provenance/authority; and the next legitimate work boundary, preserving limitation and uncertainty."),
  constraints=("Do not trade, make an investment recommendation, deploy capital, access external market data, invent Phase 3 implementation, or make an unapproved architecture or governance decision.", "If supplied context cannot establish a requested point, state the limitation rather than infer.")
)
```

The identity, Project, and requester are approved A2 values. The intent,
scope, and constraints are faithful candidate segmentation of the frozen task
`I10-DTS-CONTINUATION-BRIEF-v1`; their exact wording remains Owner-reviewable.
The unresolved Consumer is deliberate: a placeholder would falsely satisfy the
production `ContextRequest` contract and prematurely bind a Consumer.
