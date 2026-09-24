# Phase 3 Workstream 5 — Source Observation, Transformation, Representation, and Provenance

**Status:** **COMPLETE — PROJECT OWNER APPROVED.** Items 5.1–5.10 are complete within the authorized evidence-pipeline boundary. Gate 3B — Evidence Pipeline is **APPROVED — PROJECT OWNER**. Workstream 6 is complete and Project Owner approved; Workstream 7 remains unauthorized and unbegun; Workstreams 8–10 remain unauthorized; Gate 3C has not been reached or approved; Phase 4 remains **NOT AUTHORIZED**.

## Implemented controlled path

The implemented vertical path is:

```text
explicit Bootstrap (existing Workstream 3 boundary)
  -> governed Project / registered Source (existing Workstream 4 boundary)
  -> caller-established inspection authorization
  -> LocalGitSourceAdapter observation evidence
  -> bounded Markdown Artifact observation
  -> markdown-it-py structural transformation
  -> RepresentedInformation with lineage
  -> EB-03 SQLite historical evidence / reload
```

`LocalGitSourceAdapter` accepts a `RegisteredSource` and an already-established `inspection_authorized` input. It does not interpret Bootstrap, establish registration, decide Source Scope, evaluate authorization, or expand either boundary. A Source Scope is retained in observation Provenance; no new/unapproved native scope grammar is interpreted.

## Git adapter inventory and boundary

The local adapter uses the native `git` executable exclusively through CPython `subprocess.run` with `shell=False`, fixed argument vectors, disabled prompts/pager/system config, disabled hooks/fsmonitor/credential helper, bounded captured output (256 KiB), and a five-second default command limit. It passes no fetch/pull/push/clone/checkout/reset/clean/merge/rebase command and has no provider SDK or mandatory network path.

It can record local work-tree/repository-root identity evidence; HEAD; symbolic branch or detached state; unborn HEAD; NUL-delimited porcelain working-tree evidence (staged, unstaged, untracked paths); a bounded local commit list (32 entries); locally configured remote names; and shallow-history reporting. It also records unavailable executable/path/repository, timeout/bound, working-tree/history/branch/remote incompleteness, and a HEAD-before/after coherence qualification when a repository mutates while it is observed.

All Git output is local evidence. The durable limitation `local-observation-only` expressly preserves that it establishes no remote, shared, governing, authoritative, or current state. Remote names are recorded only as local/source-reported configuration—not URL values—and establish neither reachability nor synchronization. A clean tree means only that the applicable local porcelain state contained no detected change.

## Markdown Artifact and transformation behavior

`observe_markdown_artifact` accepts one relative `.md`/`.markdown` path inside the observed repository root. It rejects absolute/traversal/escaped paths, unsupported types, unreadable paths, oversized files (1 MiB), and non-UTF-8 data with non-success outcomes and structured limitations. It never executes Markdown, follows links, renders HTML, invokes Source commands, or treats content as instruction.

`transform_markdown` preserves the original observed UTF-8 text and uses `markdown-it-py` **4.x**, `MarkdownIt("commonmark").enable("table")`, configuration label `markdown-it-py-4/commonmark+table`. It produces deterministic inert block evidence for headings, paragraphs, lists, fenced/indented code, tables, block quotes, raw HTML blocks, links, hierarchy, and block line ranges. Parser output is structural evidence only. In particular it does not make Claims, Authority, Governance State, relevance, applicability, Candidate Context, selection, Required/Supporting status, sufficiency, or executable instructions.

The application requires explicitly supplied semantic identities for Artifacts, Artifact Versions, transformations, observations, and represented information. No SQLite key, locator, content equality, token, or Git reference defines semantic identity. A representation carries Source/Artifact/version/observation lineage, parser configuration/version, block-line location, transformation kind, and retained limitations. This is representation—not Claim extraction or discovery.

## Persistence and history

EB-03 schema version 3 adds append-only, Project-scoped tables for Source observations, original Artifact evidence, transformation evidence, and representation evidence. Migration 2→3 is application-owned and deterministic. The public API exposes semantic identifiers and Project-scoped data only; `row_id` remains internal. Persistence keeps original Markdown where it is safe to preserve; the existing secret-marker exclusion rejects suspected secret values rather than turning them into ordinary durable evidence.

Reload returns historical observation/representation evidence. It has no construction path to Authority, Governance State, remote/shared status, or currentness. A later Source mutation cannot modify the prior record or make it a current-state assertion.

## Deliberately deferred / unsupported

- No remote/provider/network observation, verification, synchronization, or governing-state conclusion.
- No Git library, hooks, repository mutation, Git history analytics, checkout of historical Artifacts, worktree/submodule semantic interpretation, or generic plugin framework.
- No parser plugins beyond approved table support; no Markdown rendering, sanitization/browser use, rewriting, front-matter governance, or non-UTF-8 normalization.
- No Claim creation/extraction, discovery, Candidate Context, applicability, Authority/Governance assessment, selection, Required/Supporting determination, sufficiency, package construction, rendering, or Consumer action.
- No backup/recovery workflow or Phase 4 proving.

## Traceability and validation

| Concern | Governing record | Evidence |
| --- | --- | --- |
| Adapter, capability, failure, scope boundary | Phase 1 Items 6–12; Phase 2 C6–C16; Phase 3 5.1–5.3 | `git_source.py`; clean/dirty/staged/untracked/detached/unborn/unavailable/NUL/shallow tests |
| Local-only evidence/currentness honesty | Phase 1 Item 27; CE-FR-007/008/011/015/040; Phase 2 C8–C9, D13–D16 | explicit limitation records and tests |
| Markdown evidence/inert parser | CE-FR-013/037; CE-NFR-006/011; Phase 2 C10, H12–H13 | CommonMark+table deterministic tests including imperative/raw HTML text |
| Representation and lineage | Phase 1 Items 13–16, 21–29; CE-FR-022/023; Phase 2 D5, D12 | Artifact/version/observation/block location/parser configuration Provenance |
| Durable historical evidence and identity | CE-NFR-001/004/020/022/023; Phase 2 G2–G8, H18 | v3 migration/store/reload/project isolation and semantic-key tests |

`tests/test_workstream_5.py` supplies controlled Git and Markdown fixtures under `~/temp` and covers the authorized path end to end. Final validation: focused Workstream 5 suite **9 passed**; complete suite **55 passed**; clean CPython 3.14 installed-package validation (`pip check`, console version, full suite) **passed**.

## Findings

No BLOCKER, MATERIAL, or MINOR implementation finding was identified. The adapter deliberately reports bounded/unavailable/unsupported conditions as evidence limitations rather than treating them as defects, false absence, or a basis for Workstream 6+ behavior.

## Gate 3B disposition — approved by the Project Owner

For implemented Workstreams 1–5, the Project Owner accepts the tested controlled path from explicit Bootstrap through governed Project, registered Source, authorized Source observation, transformation, represented information, and durable Provenance. The following evidence is accepted within that boundary; it does not claim discovery, applicability, selection, sufficiency, Context Package construction, or any Workstream 6+ behavior:

1. Existing Workstream 3 retains explicit authorized Bootstrap/root legitimacy; this work neither discovers nor replaces it.
2. Existing Project-scoped registration/isolation remains the precondition; all new persistence rows are Project-scoped.
3. Registered Source and observed Git state are separate records and identifiers.
4. Git inspection is local, read-oriented, shell-free, bounded, and has no network/mutation operation.
5. Local Git observations carry explicit local-only/currentness limitations.
6. Original Markdown is retained as Artifact evidence when safely preservable.
7. Markdown tokens/blocks are inert structural evidence.
8. Parser structures have no Claim, Authority, Governance State, relevance, selection, or sufficiency construction path.
9. Imperative Markdown remains preserved Source content and is never executed.
10. Observation, parser transformation, and representation are distinct records.
11. `RepresentedInformation` remains distinct from existing `CandidateContext` and sealed `ContextItem` types.
12. Source → observation → Artifact/version → transformation → representation lineage survives persistence/reload.
13. Git/Artifact/parser bounds and limitations are persisted with the associated evidence.
14. Reloaded evidence is historical and does not assert currentness.
15. Public persistence APIs use semantic identity plus Project; SQLite row IDs remain private.
16. No Workstream 6+ behavior has been introduced.
