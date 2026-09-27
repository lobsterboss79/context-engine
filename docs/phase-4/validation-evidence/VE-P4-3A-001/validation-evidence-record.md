# VE-P4-3A-001 — Lane A Crossing and Disclosure Evidence

**Result state:** **PASS**

| Field | Record value |
| --- | --- |
| Evidence ID / executed | `VE-P4-3A-001`; 2026-09-27T10:55:46-05:00 (America/Chicago) |
| Exact baseline | `phase4-ws3-crossing-disclosure` at `a06e4da5647df26db4ebe886f7bdfd0a95e00767` before lane-private artifacts; IVB-P4 origin remains `9862497`. |
| Scope | WS3 3.1-A/B, 3.2-A–F, 3.3-A–C, and 3.6-C only.  Item 3.9, proving, Gate 4B, source/test changes, and shared controls were not involved. |
| Governing references | P2 B7–B8; P3 WS4, WS7, WS9; WS1 §§1.3–1.5; WS3 obligation register and execution contract. |
| Frozen control / fixture / ER | `CTL-P4-3A-001 v1`, `FX-P4-3A-001 v1`, and `ER-P4-3A-001 v1`; pre-run SHA-256 values are preserved in [controlled-input-sha256.txt](raw/controlled-input-sha256.txt). |
| Runtime and isolation | Network-free CPython 3.14.4; `PYTHONPATH=src`; fresh temporary run directory `/tmp/ws3-lane-a-RxDMHJ`. |
| Procedure | `PYTHONPATH=src python3.14 docs/phase-4/ws3-lane-a-crossing-disclosure/controls/CTL-P4-3A-001-v1.py /tmp/ws3-lane-a-RxDMHJ/raw-result.json` |
| Raw result | [raw-result.json](raw/raw-result.json), SHA-256 `d057b7a44033c29b587177fa56d64d1d99c21db758bf168609b40e2625b69b41`.  The control emitted no stdout/stderr. |
| Supporting regression | `HOME=/tmp PYTHONPATH=src /home/lobsterboss79/temp/context-engine-ws2-validation.qNq9B4/bin/python -m pytest tests/test_workstream_4.py tests/test_workstream_7.py tests/test_workstream_9.py` — **34 passed** (CPython 3.14.4 / pytest 9.1.1).  This confirms the frozen source/test baseline was not changed; it does not replace the dedicated Lane A control. |
| ER comparison | Every missing-prerequisite scope case retained only Atlas; the all-prerequisite case included exactly named Atlas and Beacon; unauthorized crossing and each authorization denial returned their frozen reason; the authorized crossing was applicable with Beacon origin; the disclosure-denied render had neither content nor rendering/package exposure. |
| Result / Findings | **PASS**; no discrepancy, Finding, H3, or TD-14 trigger.  Expected denials are PASS conditions, not evidence of absence or universal security. |
| Disposition / lineage | Frozen control satisfied; no remediation or retest.  `VE-F5-A-001` remains supporting-only historical evidence, not this control's predecessor or closure substitute. |
