# WS4 Failure and Recovery Contract

**Status:** **PRE-RESULTS CONTROL — FROZEN FOR LANE-SPECIFIC MATERIALIZATION**

## Two distinct dimensions

A **scenario-expected failure state** is a governed semantic outcome such as
`DENIED`, `UNAVAILABLE`, `INCOMPLETE`, `RECOVERY REQUIRED`, or
`APPLICATION-LEVEL FAILURE`. If the frozen ER predicts it and preserved
evidence satisfies its criteria, the validation control can be **PASS**.

A **validation-control FAIL** means preserved evidence violates the frozen ER
acceptance/negative criteria. It is not synonymous with an application failure
or other expected scenario state. Every lane ER must state both dimensions
before execution.

## Predetermined lineage only

Only this already-frozen conceptual sequence may proceed without another Owner
decision:

```text
controlled expected-failure attempt
-> immutable predecessor evidence
-> pre-frozen non-semantic recovery/successor procedure
-> independent successor evidence
-> independent classification
```

The predecessor never becomes PASS because a successor succeeds. Unexpected
FAIL, INDETERMINATE, evidence loss, semantic discrepancy, product defect, or a
procedure defect outside this frozen sequence is STOP AND PRESERVE. No automatic
remediation is authorized.

## Approved recovery invariants

The controlling Domain G/WS10 invariants are preserved: failure states remain
distinct; failed work does not appear successful; last durable state remains
distinct from intended state; Unknown/evidence is not strengthened; isolation,
authorization, sensitivity/secret exclusion and governance remain preserved;
availability does not relax governance/security; partial state is not normal
complete state; recovery is explainable; restored state remains historical-only
until independently re-established; backup is not Source truth, Authority,
Governance State, currentness, receipt, or use; repeated observations do not
multiply Authority; and diagnostics do not become durable audit. This contract
selects no retry, scheduler, retention, deletion, RPO/RTO, HA, service,
container, cloud, or other operational policy.
