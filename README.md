# Context Engine

Context Engine is a general-purpose system for identifying, retrieving, prioritizing, and assembling authoritative information into task-specific context packages for AI systems and human users.

Project knowledge is often distributed across repositories, documents, decision records, implementation artifacts, and AI interactions. Without controlled context management, consumers can receive incomplete, stale, contradictory, irrelevant, or unnecessarily large context. Context Engine addresses that problem while preserving provenance, authority, relevance, and currency; it does not independently make project decisions.

**Design generally. Implement narrowly.**

## Status and governance

**Phase 0 — Project Definition & Governance is COMPLETE.** **Phase 1 — Requirements & Context Model is COMPLETE.** **Phase 2 — Architecture & Technology Design is COMPLETE — PASS — PROJECT OWNER APPROVED.** **Phase 3 — v0.1 Implementation is COMPLETE — PROJECT OWNER APPROVED; Workstreams 1–10 and Gates 3A–3D are complete/approved.** Final unresolved findings are BLOCKER **0**, MATERIAL **0**, and MINOR **0**; WS10-OBS-01 is **ACCEPTED — NON-BLOCKING**. **Phase 4 — Validation & Integration master-plan/checklist design is PROJECT OWNER APPROVED; Gate 4A is NOT APPROVED and Phase 4 execution is NOT AUTHORIZED.** Phase 3 closure establishes implementation-level validation only; it does not authorize proving, fresh-Consumer validation, Phase 4 execution, or broader deployment/scope.

The Project Owner has final authority for material decisions. ChatGPT analyzes, challenges, recommends, and reviews. Codex implements and documents approved decisions. See [AGENTS.md](AGENTS.md) for operating rules.

## Documentation

- [Phase 0 governing decisions](docs/phase-0/project-definition-governance.md)
- [Project roadmap](docs/roadmap.md)
- [Phase 0 exit checklist](checklists/checklist-phase-0-project-definition-governance.md)
- [Phase 1 approved baseline](docs/phase-1/README.md)
- [Phase 1 checklist](checklists/checklist-phase-1-requirements-context-model.md)
- [Phase 2 Domain A architecture foundation](docs/phase-2/architecture-foundation-system-boundary.md)
- [Phase 2 Domain B governance, trust, and security architecture](docs/phase-2/governance-trust-security-architecture.md)
- [Phase 2 Domain C source and observation architecture](docs/phase-2/source-observation-architecture.md)
- [Phase 2 Domain D context knowledge representation](docs/phase-2/context-knowledge-representation.md)
- [Phase 2 Domain E discovery, selection, and sufficiency architecture](docs/phase-2/discovery-selection-sufficiency-architecture.md)
- [Phase 2 Domain F context package and Consumer architecture](docs/phase-2/context-package-consumer-architecture.md)
- [Phase 2 Domain G state, persistence, and operational architecture](docs/phase-2/state-persistence-operational-architecture.md)
- [Phase 2 Domain H technology selection and physical architecture](docs/phase-2/technology-selection-physical-architecture.md)
- [Phase 2 Domain I validation, proving architecture, and exit gate](docs/phase-2/validation-proving-architecture-exit-gate.md)
- [Phase 2 exit-gate audit and closure record](docs/phase-2/phase-2-exit-gate.md)
- [Phase 2 checklist](checklists/checklist-phase-2-architecture-technology-design.md)
- [Phase 3 approved master implementation checklist](checklists/checklist-phase-3-v0.1-implementation.md)
- [Phase 4 approved master plan & checklist (execution not authorized)](checklists/checklist-phase-4-validation-integration.md)
- [Phase 3 Workstream 1 implementation record](docs/phase-3/workstream-1-repository-package-executable-skeleton.md)
- [Phase 3 Workstream 2 implementation record](docs/phase-3/workstream-2-governed-semantic-kernel.md)
- [Phase 3 Workstream 3 implementation record](docs/phase-3/workstream-3-bootstrap-configuration-persistence.md)
- [Phase 3 Workstream 4 implementation record](docs/phase-3/workstream-4-project-source-lifecycle.md)
- [Phase 3 Workstream 10 implementation and closure record](docs/phase-3/workstream-10-operational-hardening-recovery-closure.md)
- [Phase 3 closure record](docs/phase-3/phase-3-closure.md)
