# Phase 3 Workstream 6 — Deterministic Discovery

**Status:** **COMPLETE — PROJECT OWNER APPROVED.** Items 6.1–6.6 are accepted. Gate 3B remains approved. Workstream 7 is complete and Project Owner approved; Workstream 8 remains unauthorized and unbegun; Workstreams 9–10 remain unauthorized; Gate 3C has not been reached or approved; Phase 4 remains **NOT AUTHORIZED**.

## Implemented boundary

The implemented transition is `represented information -> deterministic discovery -> Candidate Context`. `application.discovery.discover` accepts an established `ContextRequest`, Workstream 4 ASU, explicit literal/structured query terms, already represented `DiscoveryEvidence`, and already established effective-scope prerequisites. It does not observe Sources, interpret task intent, decide applicability, enforce later Workstream 7 governance/security policy, select a Context Item, assign Required/Supporting, assess sufficiency, construct a package, or render.

The deterministic mechanisms actually implemented are exact semantic identity; explicit governed metadata; represented Classification; represented Relationship kind/target; literal text; retained Markdown block kind; and bounded local Git history identifiers. Query terms are deliberately explicit inputs rather than a natural-language inference mechanism. No available signal is automatically used.

## Candidate Context and ordering

Each Candidate Context retains the existing represented-information reference and Provenance plus source scope, relevant Relationships, available Authority/Governance/currentness records, Conflict, Uncertainty, and discovery limitations. These are copied as evidence, not evaluated. Candidate Context remains distinct from Candidate/Proposal governance state and from selected Context Item.

Ordering is stable and semantic: first by the fixed mechanism order (identity, metadata, Classification, Relationship, literal, Markdown structure, local Git history), then represented-information semantic identity, then Provenance semantic identity. SQLite retrieval APIs now sort by their public semantic identity rather than private row ID. No filesystem order, hash iteration, SQLite row ID, frequency, recency, or score is semantic ranking.

## Scope, ASU, and limitations

Discovery requires an ASU for the exact request. It starts with Project-local Sources. Cross-Project evidence can participate only through existing `ScopeInputs` prerequisites: task requirement, governed relationship, Requester authorization, and Consumer disclosure authorization. Evidence outside the ASU, excluded by effective scope, unavailable, inaccessible, unauthorized, or unsupported is excluded and recorded; it is not used for a candidate or ranking. Partial evidence may participate only with its preserved qualification.

The result records initial and expanded inspected sources, exclusions, ASU adequacy/basis, scoped negative-result boundary, expansion bases, limitations, and a deterministic termination statement. It makes no universal-absence assertion. Registered/observed Source inspection is never ASU adequacy.

## Bounded expansion

Expansion is one explicit relationship hop per supplied `ExpansionRequest`, ordered by origin/relationship/target semantic identities. It runs only when an authorized upstream record supplies a nonempty basis and says a material, potentially resolvable deficiency exists. The relationship must already be represented; its target must already be in the governed effective scope. There is no crawling, transitive traversal, Project-boundary bypass, or automatic deficiency determination. An unavailable target remains a limitation, not an expansion success.

## Persistence and temporal behavior

Workstream 6 adds no discovery schema and does not persist candidates as a selected/authoritative/current result. It consumes historical represented evidence already persisted by Workstream 5. Public EB-03 reload ordering is semantic rather than `row_id`; reload remains historical evidence and cannot establish currentness, remote/shared/governing truth, Authority, or Governance State. Local Git history identifiers are local bounded observation evidence only.

## TD-14 disposition and future procedure

**TD-14 remains CLOSED / NOT REOPENED.** Workstream 6 implementation and testing produced no evidence meeting the approved material reopening threshold. The implemented v0.1 foundation contains no LLM, embedding, vector, semantic-search engine, reranker, external API, or local model. If later test or operation evidence shows relevant, authorized, in-scope, materially Required information is materially or repeatedly undiscoverable by approved deterministic mechanisms with consequential incorrect/insufficient context, material information loss, or inability to continue meaningfully, stop affected work; preserve fixture/request/evidence/scope/result evidence; record a MATERIAL finding; trigger H3; identify it as a potential TD-14 reopening; and await Project Owner/ChatGPT disposition. Do not compensate with AI or vector technology.

Observed limitations here are expected bounded limitations: explicit query terms do not bridge vocabulary mismatch; unsupported/unavailable/inaccessible/unauthorized evidence remains unavailable; and ASU adequacy is not a discovery result. No fixture demonstrated the approved material TD-14 threshold.

## Validation and findings

`tests/test_workstream_6.py` provides controlled `~/temp` fixtures for mechanisms, candidate preservation, scope/isolation, availability states, expansion/termination, persistence ordering, repeatability, and semantic-collapse negatives. It records no BLOCKER, MATERIAL, or MINOR finding. The focused and full-suite results are recorded in the Workstream 6 review reports under `~/temp`.
