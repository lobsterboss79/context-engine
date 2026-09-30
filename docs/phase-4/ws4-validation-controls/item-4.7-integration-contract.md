# WS4 Item 4.7-A Main-Only Integration Contract

**Status:** **PRE-RESULTS CONTROL — MAIN-ONLY AFTER LANE INTEGRATION**

Item 4.7-A belongs only to main after every lane product is integrated. No
lane may claim completion of it. The review inventories all WS4 evidence,
obligations, expected scenario states/result classifications, predecessor/
successor lineages, Findings/H3, DVL-P4-001, TD-14, platform coverage,
operational limitations, and cross-lane contradictions.

It applies the exact controlling test: if evidence demonstrates a material need
for backup scheduling, retention duration, deletion workflow, RPO/RTO, HA,
daemon/service deployment, containers, cloud infrastructure, or an additional
integration environment, **STOP**, record H3/governance review, and do not add
the capability to Phase 4. Absence of such evidence does not establish
production readiness.

Preferred integration order is Lane A, then B, then C; B and C may execute in
parallel. Parked, reviewed, self-contained commits may be integrated only after
their baseline and ownership are verified. Shared status files remain untouched
until a separate Project Owner disposition. Gate 4B, fresh-Consumer preflight,
proving, remediation, and readiness are outside this contract.
