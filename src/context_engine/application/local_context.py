"""Bounded local-repository candidate-context preparation.

This convenience boundary observes an explicitly authorized local Git working
tree.  It intentionally stops before governed applicability, role selection,
package construction, or rendering.  Markdown blocks are inert, unverified
structural candidates; semantic assertions appear only after their existing
record bindings validate against the observed checkout.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
import re
from pathlib import Path

from context_engine.adapters.git_source import GitObservation, LocalGitSourceAdapter
from context_engine.application.lifecycle import Availability, RegisteredSource
from context_engine.adapters.sqlite_state import PersistedSemanticRecordSupersession, semantic_record_supersession_sha256
from context_engine.application.representation import observe_markdown_artifact, transform_markdown
from context_engine.application.semantic_ingestion import SemanticRecordError, ingest_semantic_record, load_semantic_record
from context_engine.core.model import Provenance, SemanticIdentity


MAX_CANDIDATES = 64
_TERM = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]*")
_NON_DISCOVERY_TERMS = frozenset({"a", "an", "and", "for", "help", "i", "in", "me", "my", "of", "on", "please", "the", "to", "with"})


class LocalContextError(ValueError):
    """The local candidate boundary could not be safely established."""


@dataclass(frozen=True)
class MarkdownCandidateDiscovery:
    """The existing ordered candidate slice plus non-governing diagnostics."""

    candidates: tuple[dict[str, object], ...]
    total_matches: int

    def diagnostics(self) -> dict[str, int | bool]:
        returned = len(self.candidates)
        return {
            "total_matches": self.total_matches,
            "returned_candidates": returned,
            "excluded_by_limit": self.total_matches - returned,
            "distinct_source_documents": len({str(item["artifact"]) for item in self.candidates}),
            "truncated": self.total_matches > returned,
            "candidate_limit": MAX_CANDIDATES,
        }


@dataclass(frozen=True)
class LocalContextReport:
    """Serializable candidate output, explicitly not a governed package."""

    status: str
    task: str
    repository: dict[str, object]
    task_terms: tuple[str, ...]
    verified_semantic_evidence: tuple[dict[str, object], ...]
    unverified_markdown_candidates: tuple[dict[str, object], ...]
    discovery_diagnostics: dict[str, int | bool]
    limitations: tuple[str, ...]

    def payload(self) -> dict[str, object]:
        return asdict(self)


def format_local_context_markdown(report: LocalContextReport) -> str:
    """Present one prepared candidate report without changing its evidence.

    Source-derived strings are fenced as inert data.  This keeps Markdown
    headings, links, or instructions present in an observed Source from being
    interpreted as briefing structure or authority.
    """
    repository = report.repository
    diagnostics = report.discovery_diagnostics
    lines = [
        "# Candidate Context Briefing",
        "",
        "This is a candidate context briefing, not a governed Context Package. It establishes no authority, currentness, applicability, role, sufficiency, coherence, or disclosure decision.",
        "",
        "## Request",
        f"- Repository: {_inline_code(str(repository.get('root', 'unavailable')))}",
        f"- Observed Git revision: {_inline_code(str(repository.get('head', 'unavailable')))}",
        "- Task (user-supplied, inert data):",
        _inert_data(report.task),
        "",
        "## Evidence Summary",
        f"- Provenance-verified semantic records reused: {len(report.verified_semantic_evidence)}",
        f"- Unverified Markdown candidates returned: {len(report.unverified_markdown_candidates)}",
        f"- Discovery: {diagnostics['total_matches']} total match(es); {diagnostics['returned_candidates']} returned; {diagnostics['excluded_by_limit']} excluded by the {diagnostics['candidate_limit']}-candidate limit; {diagnostics['distinct_source_documents']} Source document(s); truncation: {str(diagnostics['truncated']).lower()}.",
        "",
        "## Provenance-Verified Evidence",
    ]
    if not report.verified_semantic_evidence:
        lines.extend(["No semantic assertion was reused as provenance-verified evidence.", ""])
    else:
        for index, evidence in enumerate(report.verified_semantic_evidence, start=1):
            lines.extend([
                f"### Semantic assertion {index}",
                f"- Semantic record: {_inline_code(str(evidence['semantic_record']))}",
                f"- Source: {_inline_code(str(evidence['provenance']))}; bound revision: {_inline_code(str(evidence['source_revision']))}",
                "- Qualification: provenance-verified against the recorded binding only; this is not a currentness or authority conclusion.",
                "- Assertion (inert evidence):",
                _inert_data(str(evidence['assertion_content'])),
                "",
            ])
    lines.append("## Relevant Markdown Candidates")
    if not report.unverified_markdown_candidates:
        lines.extend(["No task-matching Markdown candidates were returned.", ""])
    else:
        for index, candidate in enumerate(report.unverified_markdown_candidates, start=1):
            lines.extend([
                f"### Candidate {index}",
                f"- Source: {_inline_code(str(candidate['artifact']))}, lines {candidate['line_start']}–{candidate['line_end']}",
                "- Matched task terms: " + ", ".join(_inline_code(str(term)) for term in candidate['matched_terms']),
                "- Status: unverified Markdown candidate; inert structural data only.",
                "- Excerpt:",
                _inert_data(str(candidate['content'])),
                "",
            ])
    lines.append("## Limitations")
    lines.extend(f"- {_plain_text(str(limitation))}" for limitation in report.limitations)
    return "\n".join(lines) + "\n"


def _inline_code(value: str) -> str:
    """Return an inline-code form safe for arbitrary observed identifiers."""
    delimiter = "`" * (max((len(run) for run in re.findall(r"`+", value)), default=0) + 1)
    return f"{delimiter}{value}{delimiter}"


def _inert_data(value: str) -> str:
    """Fence arbitrary observed text with a delimiter it cannot terminate."""
    delimiter = "`" * (max((len(run) for run in re.findall(r"`+", value)), default=0) + 3)
    return f"{delimiter}\n{value}\n{delimiter}"


def _plain_text(value: str) -> str:
    """Prevent report limitations from becoming Markdown structure."""
    return value.replace("\\", "\\\\").replace("#", "\\#").replace("[", "\\[").replace("]", "\\]")


def prepare_local_context(repository: Path, task: str, *, inspection_authorized: bool) -> LocalContextReport:
    """Observe one local Git root and prepare deterministic, qualified context.

    ``inspection_authorized`` is deliberately explicit.  It permits a local
    observation only; it does not establish Project authority, currentness,
    applicability, selection, or Consumer disclosure.
    """
    if not task.strip():
        raise LocalContextError("task must not be empty")
    supplied = repository.expanduser().resolve()
    source = RegisteredSource("local-repository-markdown", supplied.name, "git", "local Markdown candidate boundary", locator=str(supplied))
    observation = LocalGitSourceAdapter().observe(source, inspection_authorized=inspection_authorized)
    if observation.outcome == "failed" or observation.repository_root is None:
        detail = observation.limitations[0].detail if observation.limitations else "repository observation failed"
        raise LocalContextError(detail)
    root = Path(observation.repository_root)
    if supplied != root:
        raise LocalContextError("project must name the local Git repository root")
    terms = _task_terms(task)
    markdown = _markdown_candidates(root, terms)
    verified, semantic_limitations = _verified_semantic_records(root, observation)
    limitations = ["candidate context only: no Bootstrap, requester authorization, applicability, role, sufficiency, coherence, or Consumer disclosure decision was established"]
    limitations.extend(item.code + ": " + item.detail for item in observation.limitations)
    limitations.extend(semantic_limitations)
    if not verified:
        limitations.append("no semantic assertion was reused as verified current evidence")
    return LocalContextReport(
        "candidate_context", task, _repository_payload(observation), terms,
        tuple(verified), markdown.candidates, markdown.diagnostics(), tuple(sorted(set(limitations))),
    )


def _task_terms(task: str) -> tuple[str, ...]:
    # Literal token matching is a deterministic candidate mechanism, not a
    # relevance or applicability decision.
    return tuple(sorted({term.casefold() for term in _TERM.findall(task) if len(term) > 1 and term.casefold() not in _NON_DISCOVERY_TERMS}))


def _markdown_candidates(root: Path, terms: tuple[str, ...]) -> MarkdownCandidateDiscovery:
    result: list[dict[str, object]] = []
    for path in sorted(root.rglob("*"), key=lambda item: item.as_posix()):
        if ".git" in path.parts or not path.is_file() or path.suffix.casefold() not in {".md", ".markdown"}:
            continue
        try:
            relative = path.relative_to(root).as_posix()
        except ValueError:
            continue
        artifact = observe_markdown_artifact(root, relative)
        if artifact.outcome != "observed" or artifact.original_markdown is None:
            continue
        source = SemanticIdentity("source", "local-repository-markdown")
        transformation = transform_markdown(
            source_identity=source, artifact_identity=SemanticIdentity("artifact", "local:" + relative),
            artifact_version_identity=SemanticIdentity("artifact_version", "local:" + relative), source_locator=relative,
            native_state_reference=None, original_markdown=artifact.original_markdown,
            observation_provenance=Provenance(SemanticIdentity("provenance", "local-observation"), source=source),
        )
        for block in transformation.blocks:
            text = block.content.strip()
            words = {term.casefold() for term in _TERM.findall(text)}
            matched = tuple(term for term in terms if term in words)
            if not matched:
                continue
            result.append({
                "artifact": relative, "block_ordinal": block.ordinal, "kind": block.kind,
                "line_start": block.line_start, "line_end": block.line_end,
                "matched_terms": matched, "content": text[:512],
                "content_status": "unverified_markdown_structure_inert_data",
            })
    result.sort(key=lambda item: (-len(item["matched_terms"]), str(item["artifact"]), int(item["block_ordinal"])))
    return MarkdownCandidateDiscovery(tuple(result[:MAX_CANDIDATES]), len(result))


def _verified_semantic_records(root: Path, observation: GitObservation) -> tuple[list[dict[str, object]], list[str]]:
    directory = root / "docs" / "project" / "semantic-records"
    if not directory.is_dir() or observation.head is None:
        return [], ([] if directory.is_dir() else ["no supported semantic-record directory found"])
    superseded, lifecycle_error = _superseded_record_keys(directory / "lifecycle")
    if lifecycle_error:
        return [], [lifecycle_error]
    records: list[dict[str, object]] = []
    stale = invalid = 0
    for path in sorted(directory.glob("*.json")):
        try:
            record, digest = load_semantic_record(path)
        except SemanticRecordError:
            invalid += 1
            continue
        if (record.identity, record.version, digest) in superseded:
            continue
        artifact_path = root / record.artifact_locator
        try:
            source_hash = hashlib.sha256(artifact_path.read_bytes()).hexdigest()
        except OSError:
            stale += 1
            continue
        # A later repository HEAD does not invalidate an immutable semantic
        # record when the bound artifact bytes and location still validate.
        # Preserve the record's own revision/observation binding below rather
        # than promoting the later local observation into its provenance.
        if record.source_sha256 != source_hash:
            stale += 1
            continue
        source = RegisteredSource(record.source_identity, record.project_identity, "git", "semantic-record-declared-source-scope", Availability.AVAILABLE, str(root))
        artifact = observe_markdown_artifact(root, record.artifact_locator)
        if artifact.original_markdown is None:
            stale += 1
            continue
        source_identity = SemanticIdentity("source", record.source_identity)
        transformation = transform_markdown(
            source_identity=source_identity, artifact_identity=SemanticIdentity("artifact", "local:" + record.artifact_locator),
            artifact_version_identity=SemanticIdentity("artifact_version", "local:" + record.artifact_locator),
            source_locator=record.artifact_locator, native_state_reference=record.source_revision,
            original_markdown=artifact.original_markdown,
            observation_provenance=Provenance(SemanticIdentity("provenance", record.observation_identity), source=source_identity),
        )
        try:
            ingested = ingest_semantic_record(record, record_sha256=digest, source=source, transformation=transformation,
                project_identity=record.project_identity, observation_identity=record.observation_identity,
                source_revision=record.source_revision, source_sha256=source_hash)
        except SemanticRecordError:
            invalid += 1
            continue
        records.append({"claim_identity": ingested.claim.identity.value, "semantic_record": record.identity + ":" + record.version,
                        "semantic_record_sha256": digest, "assertion_content": ingested.claim.assertion_content,
                        "provenance": record.artifact_locator, "source_identity": record.source_identity,
                        "source_revision": record.source_revision, "source_sha256": record.source_sha256,
                        "limitations": record.limitations,
                        "content_status": "validated_semantic_record_evidence_bound_to_recorded_revision_not_currentness_or_authority"})
    limitations: list[str] = []
    if stale:
        limitations.append(f"{stale} semantic record(s) were not reused because their bound Source hash does not match the observed artifact")
    if invalid:
        limitations.append(f"{invalid} semantic record(s) could not be validated through existing ingestion")
    return records, limitations


def _superseded_record_keys(directory: Path) -> tuple[set[tuple[str, str, str]], str | None]:
    """Read only validated append-only lifecycle edges before reuse.

    A malformed lifecycle directory is not ignored: candidate preparation then
    cannot safely decide which semantic-record instances are active.
    """
    if not directory.exists():
        return set(), None
    superseded: set[tuple[str, str, str]] = set()
    expected = {"project_identity", "relation_identity", "version", "relation_sha256", "predecessor_record_identity", "predecessor_version", "predecessor_record_sha256", "successor_record_identity", "successor_version", "successor_record_sha256", "kind", "creation_basis", "evidence"}
    for path in sorted(directory.glob("*.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(payload, dict) or set(payload) != expected or any(not isinstance(value, str) or not value for value in payload.values()):
                raise ValueError
            relation = PersistedSemanticRecordSupersession(**payload)
            if relation.relation_sha256 != semantic_record_supersession_sha256(relation):
                raise ValueError
        except (OSError, ValueError, TypeError, UnicodeDecodeError, json.JSONDecodeError):
            return set(), "semantic lifecycle relation is unavailable or invalid; semantic assertions were not reused"
        superseded.add((relation.predecessor_record_identity, relation.predecessor_version, relation.predecessor_record_sha256))
    return superseded, None


def _repository_payload(observation: GitObservation) -> dict[str, object]:
    return {"root": observation.repository_root, "head": observation.head, "branch": observation.branch,
            "working_tree_clean": observation.working_tree_clean, "observation_outcome": observation.outcome,
            "source_boundary": "explicit local Git root; Markdown only"}
