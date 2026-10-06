# Semantic-Record Lifecycle / Supersession Design

**Status:** **DESIGN COMPLETE — PROJECT OWNER LIFECYCLE IMPLEMENTATION DECISION REQUIRED**

**Scope:** Production lifecycle design only. This is not an implementation authorization, a correction of any Day Trading System record, a change to `H3-P4-SEMANTIC-INGESTION-001`, or authorization to resume proving.

## 1. Finding and recommendation

The implemented semantic-record capability has append-only *evidence* storage, but no append-only semantic-record *lifecycle*. A corrected record can be validated and persisted as another row, yet nothing says that it replaces an earlier record, which row is effective, or whether two incompatible candidates are competing. Therefore adding a corrected v2 without a lifecycle mechanism would make normal current-state use unsafe.

The smallest sufficient production addition is an explicit, append-only, Project-scoped **semantic-record supersession relation**. A relation names the complete immutable predecessor and successor record instances (record identity, version, and record SHA-256), declares a bounded relation kind, and is accepted only when it preserves a valid, unambiguous chain. The resolver exposes only terminal, valid records to normal downstream processing; historical records and relations remain queryable only through an explicit history interface.

This is deliberately a relation, not a mutable record status and not a general workflow/version-control system.

## 2. Current implemented contract

| Concern | Current contract | Present limitation |
| --- | --- | --- |
| Record identity/version | Required nonempty `identity` and `version` in the JSON `SemanticRecord`. Provenance and RepresentedInformation use `semantic-record:<identity>:<version>`. | No rule relates versions of one identity or establishes a successor. |
| Record hash | `load_semantic_record` SHA-256 hashes the JSON bytes; ingestion requires a nonempty 64-character supplied hash. The hash is placed in provenance. | The in-memory ingestion function does not recompute a supplied hash; the persistence method does not validate it. No lifecycle key uses it. |
| Claim identity | Required `claim_identity`; emitted as `SemanticIdentity("claim", claim_identity)`. The Claim has `assertion_reference` and provenance but no independent Claim version field. | No record-level rule says whether a later Claim is the same atomic assertion or a semantic revision. |
| Project/Source identity | Ingestion requires the requested Project, record Project, registered Source, transformed Artifact Source, locator, revision/hash, and observation to agree. | No cross-record Project or Source lineage rule. |
| Persistence identity | v6 `semantic_record_evidence` persists Project, record identity/version/hash, Claim identity, Source and Artifact bindings, location reference, and evidence. SQLite `row_id` is private. | No relation, active marker, historical/effective query, or lineage validation. |
| Uniqueness/replay | SQLite uniqueness is only `(project_identity, record_identity, version, record_sha256)`; `save_semantic_record` uses `INSERT OR IGNORE`. Exact persisted-row replay is idempotent. | The schema permits the same logical identity/version with different hashes, and persistence silently ignores only an exact duplicate. It cannot reject or resolve competing candidates. |

The current ingestion checks exact block and line binding and fails closed for a mismatch. It creates Claim and RepresentedInformation but does not persist them itself; the v6 adapter is the available Project-scoped evidence store. Existing `semantic_records_for_project` returns all rows ordered by identity, version, and hash. It does not designate an active record. The existing `currentness_basis` field is author-supplied contextual evidence; it is not lifecycle status or supersession.

## 3. Minimum model and alternatives

| Representation | Assessment |
| --- | --- |
| A. Fields in successor (`supersedes_record_id`, version, hash) | Can name the predecessor, but binds lifecycle policy to a content record and requires parsing/persisting those fields to resolve active state. It also leaves the relationship less independently auditable. Viable, but not preferred. |
| B. Separate append-only predecessor-to-successor relation | **Recommended.** It preserves record bytes, gives the relationship its own durable evidence identity and validation boundary, and makes both history and active resolution explicit. It is the smallest model that does not overload record content or mutable state. |
| C. Mutable/in-record status (`active`, `superseded`) | Rejected. Updating v1 violates immutability; an append-only status event still needs the same predecessor/successor semantics and can create conflicting status histories. |
| D. Existing architecture | Insufficient. Version/hash fields and append-only evidence imply retention, not a successor edge, active selection, or lineage validity. |

### Recommended relation

```text
SemanticRecordSupersession {
  project_identity,
  predecessor: (record_identity, version, record_sha256),
  successor:   (record_identity, version, record_sha256),
  kind: provenance_correction | semantic_revision | source_revision,
  evidence
}
```

`evidence` is bounded descriptive audit evidence, not an authority grant or unstructured workflow state. The relation is written only with a validated successor and, unless a later design supports a separately governed staged operation, in the same database transaction as that successor. It references full immutable instance keys so a later byte-distinct record cannot be substituted for either endpoint.

The database and application validation together must enforce one outgoing relation per predecessor and one incoming relation per successor, exact relation replay idempotency, and no logical-record identity/version/hash collision. The application must also validate the complete graph before returning active records. Database constraints prevent ordinary races; the resolver remains the fail-closed backstop for corrupted or legacy data.

## 4. Immutability and Claim identity

The following must remain immutable once accepted:

- v1 JSON bytes and its SHA-256; the source-maintained v1 artifact is not rewritten.
- v1 `semantic_record_evidence`, emitted provenance evidence, and all original Project/Source/revision/location bindings.
- Every accepted v2/v3 JSON and persisted evidence row; each new file has a new SHA-256 even where the semantic assertion is unchanged.
- Every supersession relation. A later correction is another successor relation from the then-effective record, never an update/delete of an earlier edge.

For a **provenance-only correction**, the atomic assertion is unchanged: retain `claim_identity`, retain the assertion reference, use a new record version/hash, and use `kind=provenance_correction`. This is the triggering case.

For a **semantic revision**, the atomic assertion changes. The successor must have a new `claim_identity`; this follows the existing Claim semantics, where identity identifies the atomic Claim rather than a mutable topic. It uses `kind=semantic_revision`; the explicit relation supplies the continuity link. A same-Claim relation marked semantic revision, or a changed-Claim relation marked provenance correction, is rejected. A changed Claim with no valid semantic-revision relation is an unrelated record, not a successor.

For a **source revision** where the source bytes/revision change, use `kind=source_revision`. Retain Claim identity only if the atomic assertion is literally still the same; otherwise use a new Claim identity and treat it as a semantic revision caused by the source revision. The relation must not assert that a changed source is equivalent merely because its path is unchanged.

Thus the three kinds are useful but minimal: they tell a reviewer whether a lineage change corrects evidence location, changes asserted meaning, or revalidates against a changed Source. They do not introduce lifecycle states, approvals, or a workflow engine.

## 5. Active-record resolution

Resolve within one Project only, over accepted records and accepted relations. The normal resolver returns records that are valid nodes and have no accepted outgoing successor. It must perform these checks before returning any result:

| Situation | Required result |
| --- | --- |
| One valid record, no successor | That record is active. |
| Valid `v1 -> v2` | v2 is active; v1 is historical/superseded. |
| Valid `v1 -> v2 -> v3` | v3 alone is active; full ancestry remains queryable. |
| Multiple competing successors of one predecessor | Reject the relation/ingestion transaction; if discovered in stored state, fail closed for that lineage and return no active record from it. |
| Missing predecessor or successor | Reject ingestion; stored incomplete lineage fails closed. |
| Different Project | Reject. Neither endpoint nor relation may cross a Project boundary. |
| Wrong Claim identity | Reject unless `kind=semantic_revision` and the new Claim is a valid atomic assertion. A provenance correction requires exactly equal Claim identity and assertion reference. |
| Cycle/self-edge | Reject. A graph containing a cycle fails closed for all nodes in that lineage. |
| Exact duplicate relation | Idempotent replay: no additional relation/effect. Any non-identical duplicate for an endpoint is a conflict and rejected. |
| Invalid successor | Do not persist it or its relation. A pre-existing invalid successor makes that lineage unresolved; do not fall back silently to v1 for current-state processing. |

The resolver must validate relation kind invariants, endpoint existence and Project equality, no duplicate logical record instance, indegree/outdegree at most one, acyclicity, and predecessor/successor admissibility. Ordering records lexically, choosing the highest version, or choosing a newest timestamp is not permitted: those rules conceal ambiguity and do not establish replacement.

An unlinked initial record is valid. An unlinked later record with the same Claim is not automatically a successor; it remains a separate record and must not be folded into an active set by inference.

## 6. Source revision treatment

Same-source provenance correction keeps the source revision/hash, Source, Artifact and assertion intact; only the record's exact valid block/line provenance (and resulting record hash/version) changes. It is not source revalidation.

When the linked Markdown Source changes, ordinary ingestion continues to reject an old record against the new revision/hash. A replacement must bind the new observed Source revision and SHA-256, observation, transformed block and lines, and undergo normal semantic validation. A `source_revision` relation then connects the historical record to that new evidence. It does not make either record currently authoritative, and it does not remove independent Source, currentness, authority, or governance assessment obligations.

## 7. Persistence and ingestion impact

Schema v6 cannot represent a durable relation: it has only record evidence columns and no predecessor/successor keys. An additive **v6-to-v7 migration** is therefore required. It should add an append-only `semantic_record_supersession` table keyed by Project plus the full predecessor and successor instance keys, with foreign keys to the v6 record evidence table and uniqueness enforcing a single outgoing predecessor and single incoming successor. The migration must not rewrite v6 rows.

The existing schema-v6 semantic-record evidence remains valid historical record evidence. On migration, each v6 row is an initial unlinked active root unless and until a validated successor relation is added. Backup validation and metadata must advance to v7; backup/restore tests must cover a v6 database migration and a v7 database with relationships. Restoring remains historical state only and cannot establish current authority/currentness.

Required ingestion behavior:

| Submission | Behavior |
| --- | --- |
| Initial v1 | Validate current record contract; persist one immutable record. It is active if no valid successor exists. |
| Valid v2 superseding v1 | Validate both record contract and relation in one transaction; persist v2 and the relation; v2 becomes the sole active terminal record for that lineage. |
| Replay v1 or v2 | Same immutable record instance is idempotent; no duplicate output/effect. |
| Replay relation | Exact same relation is idempotent. |
| Competing v2 | Reject, preserving the established chain. |
| Invalid successor | Reject without persisting record or relation. |
| Successor with absent predecessor | Reject without persisting the relation/successor as a lifecycle submission. |

The implementation should make `load_semantic_record` the source of persisted record hashes, verify hash format/content at the persistence seam, and treat a same logical identity/version with a different hash as conflict rather than letting the present v6 composite uniqueness admit it.

## 8. Downstream boundary and change surface

Normal discovery, package construction, and rendering should receive only the validated effective active semantic records. An explicit provenance/history query may return all historical rows plus their lineage; it must not be used by normal current-state processing by accident.

This can remain principally at the semantic-input/persistence seam: persist, validate, resolve active records, then supply the existing Claim / RepresentedInformation seam. WS6/WS7/WS8/WS9 semantic rules and the Claim schema need not change. Discovery/package/rendering may need only the narrow input selection call to use the active resolver if they currently enumerate all stored semantic records directly; no new semantic interpretation is required.

The bounded implementation surface is semantic ingestion, SQLite persistence/migration/backup compatibility, lifecycle resolution, focused tests, and documentation. No new dependency, Source model, Claim schema, general workflow feature, or Day Trading System change is required. If an audit or rendering consumer is found to query v6 rows directly, that consumer seam is an additional implementation surface and must be enumerated before approval.

## 9. Focused validation plan (not executed)

1. Accept a valid provenance correction; verify v1 bytes/evidence are unchanged, v2 has a new hash, relation is immutable, and only v2 is active.
2. Verify v1-to-v2-to-v3 lineage, full historical queryability, and v3-only active output.
3. Reject competing successors, duplicate non-identical relations, cycles and self-edges, cross-Project endpoints, missing predecessors, malformed endpoint hashes, and changed logical identity/version hashes.
4. Reject a Claim mismatch for provenance correction; accept a valid semantic revision with a new Claim identity and correct kind; reject kind/Claim mismatches.
5. Cover same-Source provenance correction and a new-Source-revision transition, including source hash/revision, observation, block/line validation, and unchanged-versus-changed assertion identity.
6. Prove exact record and relation replay idempotency, and invalid-successor atomic rollback/no partial active state.
7. Verify active-only discovery/downstream inputs and explicit history output; regress the pre-existing ingestion rejection paths.
8. Validate v6-to-v7 migration, v7 backup/restore with lineage, v6 backup migration behavior, schema incompatibility failure, and the relevant full regression suite.

## 10. Governance classification

This is a **new, narrowly bounded production lifecycle capability refinement** that follows the closed `H3-P4-SEMANTIC-INGESTION-001`; it is not evidence that the accepted H3 implementation failed its approved contract. H3 delivered strict ingestion and append-only v6 record evidence, but did not define supersession or effective-record selection. Reopening H3 would inaccurately rewrite that approved scope and closure.

Because the change adds a schema migration and new production semantic lifecycle rule, it requires a separate Project Owner implementation decision and an authorized remediation/change record with derived baseline and retest plan. It does not itself reopen DVL, TD-14, Gate 4B, Gate 4C, WS5.5 lineage, or Consumer states.

## 11. Later treatment of the four triggering records

After, and only after, implementation authorization and a separately approved source-owner correction revision:

The procedure applies independently to `dts-semantic-reproducibility-formal-evidence-data`, `dts-semantic-reproducibility-formal-evidence-code`, `dts-semantic-reproducibility-formal-evidence-configuration`, and `dts-semantic-reproducibility-formal-evidence-experiment-definition`.

1. Preserve each v1 JSON file and its persisted/historical evidence unchanged.
2. Create one v2 record for each named v1, with its own new JSON SHA-256 and incremented record version. Retain its existing `claim_identity` and unchanged assertion reference because this is provenance-only.
3. Bind each v2 to the same Source revision/hash, Source, Artifact, and observation as its v1, but set the actual transformation binding to block 3, line 7 (`line_start: 7`, `line_end: 7`).
4. Add one `provenance_correction` supersession relation per v1/v2 pair, referencing each complete immutable instance key in the Day Trading System Project.
5. Active resolution returns the four v2 records for normal processing. The four v1 records remain historical provenance evidence and are never silently altered or selected as current records. No semantic assertion, Claim identity, Source content, or source revision is changed by this correction.

## 12. Exact Project Owner decision required

Decide whether to authorize the bounded production implementation of the append-only, Project-scoped semantic-record supersession relation and fail-closed active-record resolver described here, including the v7 SQLite migration, backup/restore compatibility, focused validation, and documentation.

That decision must explicitly preserve the closed H3 record and all listed proving/governance states. It must not authorize modifying Day Trading System, creating v2 records, selecting a new proving baseline, creating a Consumer, resuming WS5.5, executing WS6A/WS6B, changing Gates, committing, or pushing.
