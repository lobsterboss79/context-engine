# Gate 4B Parallel-Lane Execution and Integration Contract

**Status:** **FROZEN FOR FUTURE AUTHORIZED EXECUTION — NO LANES CREATED**

## Ownership and freeze

Future Lane A (`phase4-gate4b-evidence-coherence`) may write only `docs/phase-4/gate-4b/evidence-coherence/`. Future Lane B (`phase4-gate4b-findings-boundaries`) may write only `docs/phase-4/gate-4b/findings-boundaries/`. Both directories are reserved, not created by this shared-foundation materialization.

Main exclusively owns this directory, all shared registers, reconciliation, final Gate review materials, and any shared status update. Parallel lanes must treat as read-only: `AGENTS.md`, `README.md`, `docs/roadmap.md`, the Phase 4 checklist, WS1–WS4 closure records, all existing validation evidence, `DVL-P4-001`, TD-14 records, existing Finding/H3 records, `src/`, `tests/`, `pyproject.toml`, this shared foundation, and the other lane's directory.

Any required alteration to a frozen/shared file is a **STOP AND PRESERVE** condition and becomes a main-only reconciliation issue. Lanes may not modify checklist/README/roadmap status, DVL/TD state, existing evidence or Findings, source/tests, dependencies, or shared registers.

## Common stop conditions

Stop affected work, preserve the original record and observed condition, and report for main/Project Owner review on: unexpected FAIL; unresolved INDETERMINATE; open or newly apparent material Finding; H3; cross-workstream contradiction; evidence-provenance gap; acceptance ambiguity; DVL-P4-001 future trigger; TD-14 threshold; new architecture, technology, security, governance, scope, or policy decision; source/test remediation need; proving-authorization question; production-readiness question; or a required frozen-file change.

No stop condition authorizes remediation, finding closure, DVL/TD change, scope/technology change, Gate decision, proving, WS5, or readiness claim.

## Proving boundary

After reconciliation, Gate 4B may at most support **READY FOR PROJECT OWNER PROVING-AUTHORIZATION DECISION**. It does not itself authorize proving. No lane may reserve or expose a Consumer, execute contamination preflight, start WS5, execute either proving exercise, or establish production readiness. Even a Project Owner Gate PASS requires a separate explicit proving-authorization decision before actual proving.

## Future integration contract

1. Each lane completes a lane-private, bounded assessment and one self-contained commit.
2. Neither lane changes shared files or status.
3. Integrate Lane B first, then Lane A, as preferred by the approved topology; ownership is disjoint, so the order is not a substantive result preference.
4. Main-only reconciliation checks every register ID once, evidence lineage, non-PASS preservation, Finding/H3/DVL/TD inventory, coherence, boundaries, and unresolved discrepancies.
5. Main-only work prepares G4B-12 fresh-Consumer justification and any G4B-13 stopped/reopening package if triggered.
6. The Project Owner alone decides G4B-14. G4B-15 retains the separate proving authorization boundary.
