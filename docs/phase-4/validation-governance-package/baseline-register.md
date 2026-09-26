# Baseline Register

**Template status:** Pre-execution only. The sole populated implementation origin is historical baseline evidence, not validation execution.

## Governing semantic/design baseline

| Baseline ID | Governed record(s) | Authority/lineage | Status |
| --- | --- | --- | --- |
| SDB-P0 | [Phase 0 project definition and governance](../../phase-0/project-definition-governance.md) | Project Owner-approved governing baseline | Governing |
| SDB-P1 | [Phase 1 requirements, conceptual model, and traceability](../../phase-1/README.md) | Project Owner-approved governing baseline | Governing |
| SDB-P2 | [Phase 2 architecture foundation](../../phase-2/architecture-foundation-system-boundary.md), [technology/physical architecture](../../phase-2/technology-selection-physical-architecture.md), [validation/proving architecture](../../phase-2/validation-proving-architecture-exit-gate.md), and [Phase 2 exit gate](../../phase-2/phase-2-exit-gate.md) | Project Owner-approved governing baseline | Governing |
| SDB-P4-WS1 | [WS1 governance record](../workstream-1-validation-governance-evidence-model.md) and [Phase 4 checklist](../../../checklists/checklist-phase-4-validation-integration.md) | Project Owner-approved Phase 4 plan design | Governing pre-results control |

Expected semantics derive from these records, never solely from implementation behavior.

## Immutable implementation origin baseline

| Baseline ID | Exact commit | Description | Lineage/status |
| --- | --- | --- | --- |
| IVB-P4-ORIGIN | `9862497` | `Close Phase 3 v0.1 implementation` | Immutable Phase 4 implementation origin; preserves [Phase 3 closure](../../phase-3/phase-3-closure.md) evidence |

## Future derived validation baseline record

Do not create this record until authorized remediation creates an implementation change. Do not rewrite `IVB-P4-ORIGIN`.

| Field | Record value |
| --- | --- |
| Derived Baseline ID | `[future stable ID]` |
| Originating baseline | `[IVB-P4-ORIGIN or prior derived baseline]` |
| Exact commit/version | `[future value]` |
| Reason for change | `[linked finding/remediation]` |
| Authorized change boundary | `[approved boundary]` |
| Approving authority/date | `[future governed authority]` |
| Affected components/semantics | `[future value]` |
| Configuration/Bootstrap provenance | `[identity, version/digest where applicable, storage location]` |
| Fixture/Source/input provenance | `[controlled identities, versions/digests, ASU/scope basis where applicable]` |
| Affected validation/retest/proving evidence | `[future Evidence/Proving IDs]` |
| Lineage and preservation statement | `[original baseline/evidence remain preserved]` |
