# Semantic-Record Lifecycle Capability Implementation and Validation Record

**Status:** **IMPLEMENTED — FOCUSED VALIDATION AND FULL REGRESSION PASS**

**Classification:** **NEW BOUNDED SEMANTIC-RECORD LIFECYCLE CAPABILITY REFINEMENT**

## Authority and boundary

The Project Owner approved implementation of the design in [semantic-record-lifecycle-supersession-design.md](semantic-record-lifecycle-supersession-design.md). This record implements only append-only semantic-record succession, bounded lifecycle kinds, active-record selection, SQLite persistence/migration, validation, backup/restore compatibility, and lifecycle documentation.

`H3-P4-SEMANTIC-INGESTION-001` remains **CLOSED — PROJECT OWNER APPROVED**. This refinement neither reopens nor revises it.

## Production contract

A semantic-record predecessor remains immutable historical evidence. Neither its JSON bytes, record hash, stored semantic-record evidence, nor its provenance bindings are updated to express lifecycle state.

A successor is established only by an immutable, Project-scoped `semantic_record_supersession` relation. It includes the Project, its identity/version/SHA-256, full predecessor and successor record instance keys, bounded kind, creation basis, and bounded evidence. The relation SHA-256 is deterministic over all its immutable fields except the hash itself.

The implemented kinds are:

- `provenance_correction`: same Claim identity and same Source identity, Artifact, revision, and Source hash; it corrects record provenance/evidence metadata without changing the atomic assertion.
- `semantic_revision`: new Claim identity; it represents a changed atomic assertion.
- `source_revision_transition`: changed Source revision or Source hash; it is not a provenance-only correction. Claim identity is retained only when the atomic assertion remains the same.

Records and lifecycle relations are data/evidence only. They grant no Authority, change no governance, and issue no controller instruction.

## Resolution and failure behavior

Normal current-state processing calls `active_semantic_records_for_project`, which returns only terminal records in a valid Project-local lineage. An unlinked valid record is active. For `v1 -> v2 -> v3`, only v3 is active; predecessor records and relations remain available through explicit historical queries.

The resolver fails closed on missing endpoints, malformed hashes, logical identity/version ambiguity, relation-kind invariant violations, multiple incoming/outgoing edges, cycles, and any other ambiguous lineage. It does not select the latest version, timestamp, or arbitrary winner.

Ingestion is idempotent for an exact record replay and an exact relation replay. A same record identity/version with a different hash, a relation identity/version with a different hash, a competing successor, a missing predecessor, an invalid kind, or a cross-Project successor submission is rejected.

## Persistence and migration

SQLite schema v7 adds only `semantic_record_supersession` with foreign keys to the existing v6 `semantic_record_evidence` instance key and unique constraints for immutable relation identity/version, one predecessor successor edge, and one successor predecessor edge. The v6-to-v7 migration is additive and does not rewrite historical semantic evidence. Existing v6 rows remain unlinked active roots until a valid relation is appended.

Backup metadata/validation uses schema v7. Backup and restore preserve predecessor rows, successor rows, relations, and active-resolution results; restore continues to qualify recovered state as historical only.

## Validation result

Focused lifecycle, semantic-ingestion, and backup/restore coverage passed: **19 passed**. It covers initial active selection, provenance correction, immutable historical predecessor retention, multi-version resolution, ambiguity/cycle/missing-endpoint rejection, Claim and Source-revision rules, hash/kind validation, replay, Project isolation, v6-to-v7 migration, and restored active resolution.

The approved full repository regression suite passed: **121 passed**. No unrelated regression failure or stop condition was encountered.

## Implementation surface and limitations

Changed surfaces are the SQLite adapter, a narrow semantic lifecycle validation module, focused tests, schema-version regression expectation, and this record. The Claim schema and WS6/WS7/WS8/WS9 semantics are unchanged. No new dependency or database subsystem was introduced.

This capability intentionally does not infer succession, repair stale data, choose a winner from ambiguity, alter external Project files, or authorize proving. Full record-content assertion equality is validated at the semantic ingestion lifecycle helper; durable persistence validates the fields retained by schema v6 plus the lifecycle graph.

## External-project return boundary

This implementation does not alter Day Trading System. If final validation passes, return to the Project Owner for separate authorization before creating any external v2 records, append-only relations, candidate revision, corpus validation, or read-only requalification. It does not authorize a Consumer, WS5.5 successor, WS6A/WS6B, Gate 4C, or production-readiness claim.
