# Proving Sequential Execution Contract

**Status:** **FROZEN FOR WS5; WS6A/WS6B EXECUTION NOT AUTHORIZED.**

Proving is read-only application execution plus run-specific control, fixture,
and evidence preservation. Source/test modification, remediation, architecture
or policy changes, DVL/TD changes, and Finding closure are prohibited.

Order: freeze controls -> protected reservation -> actual freshness preflight ->
preserve raw preflight evidence -> classify WS5 -> freeze future WS6A contract ->
separate Owner WS6A decision -> only then task/package exposure and proving.

WS5 may expose only what is necessary for reservation and contamination
assessment. It must not disclose a WS6A task, expected result, task-priming
rubric, intended Context Engine package, task-specific history, or dogfooding
material.

Result states: PASS (valid criteria satisfied); FAIL (valid criteria not
satisfied); INDETERMINATE (valid attempt lacks reliable evidence); INVALID RUN
— DISCARD / RESTART (freshness/exact-run violation; preserve but do not
normalize into another result).

Stop and preserve for FAIL/INDETERMINATE, invalid run, BLOCKER, MATERIAL,
H3, provenance gap, DVL reconsideration, TD-14 trigger, remediation need, new
environment/technology/scope decision, or inability to execute faithfully.
