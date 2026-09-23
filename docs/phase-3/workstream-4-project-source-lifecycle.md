# Phase 3 Workstream 4 — Project and Source Lifecycle

**Status:** **COMPLETE — PROJECT OWNER APPROVED.** Items 4.1–4.7 have implementation and validation evidence, and their completion is Project Owner approved. Gate 3A remains approved. Gate 3B remains pending and unapproved; Workstream 5 and later remain unauthorized; Phase 4 remains **NOT AUTHORIZED**.

## Implemented foundation

- `application.lifecycle.RegisteredSource` records explicit semantic Source identity, Project association, type, Source Scope, bounded availability, and optional locator. Registration has no Authority, Governance State, currentness, applicability, selection, or disclosure field.
- `ScopeInputs` and `effective_sources` preserve Project isolation by default. Cross-Project scope requires all of: task need, governed relationship, Requester authorization, and Consumer disclosure authorization. Relationship or shared locator alone is insufficient and transfers no semantic status.
- `ApplicableSourceUniverse` carries an explicit request reference, Source boundary, adequacy (`adequate`, `known_incomplete`, or `indeterminate`), and non-empty establishment basis. Registered Sources and availability conditions cannot themselves prove ASU adequacy.
- Availability retains `unavailable`, `inaccessible`, `unauthorized`, `unsupported`, `partial`, `absent`, and `not_inspected` as distinct lifecycle conditions. A bounded failed or incomplete inspection is not silently made absent.
- The EB-03 adapter’s application-owned schema version 2 adds only Project-scoped lifecycle registrations. Its `row_id` is internal and never exposed; `(project_identity, source_identity)` remains caller-supplied semantic data. Version 1 deterministically migrates to version 2 within the initialization transaction.

## Deliberate limits

No Source observation or access adapter, Git invocation, Markdown transformation, represented-information generation, discovery, applicability, selection, sufficiency, package construction, rendering, delivery, backup/recovery workflow, or Workstream 5+ behavior is implemented. This workstream establishes no Authority, Governance State, currentness, or Consumer disclosure authorization from registration, locator, relationship, persistence, or restoration.

## Traceability and validation

| Concern | Implementation | Governing record | Evidence |
| --- | --- | --- | --- |
| Project/Source identity and Source Scope | `RegisteredSource` | Phase 1 conceptual model; Phase 2 Domain D; Phase 3 4.1 | required lifecycle fields; shared locator/identity test |
| Isolation and bounded traversal | `ScopeInputs`, `effective_sources` | Phase 2 Domain B; Domain G; Phase 3 4.2 | default denial and all-prerequisite positive path |
| Requester vs Consumer boundary | separate authorization inputs | Phase 1 functional requirements; Phase 2 Domain B/E | either missing authorization denies external scope |
| ASU boundary | `ApplicableSourceUniverse`, `BoundaryAdequacy` | Phase 2 Domains C/E; Phase 3 4.3 | same registration set can be known-incomplete or indeterminate |
| Availability distinctions | `Availability` | Phase 1 model; Phase 2 Domains C/E | parameterized non-absence tests |
| Durable lifecycle facts and identity | `PersistedSourceRegistration`, `SQLiteStateStore` v2 | Phase 2 Domains G/H; Phase 3 4.1/4.5 | restart, isolation, row-id independence, v1 migration, rollback |

Final validation evidence is recorded in the Workstream 4 review report under `~/temp`. The final suite passes with 46 tests; no dependency, framework, or plugin was introduced.
