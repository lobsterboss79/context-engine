"""Bounded retrieval of one observed local Markdown Source range."""
from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import re
from pathlib import Path

from context_engine.adapters.git_source import LocalGitSourceAdapter
from context_engine.application.lifecycle import RegisteredSource
from context_engine.application.representation import observe_markdown_artifact


MAX_SOURCE_LINES = 200
MAX_CONTENT_BYTES = 16_384
_LINE_RANGE = re.compile(r"([0-9]+):([0-9]+)\Z")


class SourceEvidenceError(ValueError):
    """An explicit bounded Source-evidence request could not be established."""


@dataclass(frozen=True)
class SourceEvidenceReport:
    """One exact, unverified range from an explicitly observed Markdown Source."""

    status: str
    repository: dict[str, object]
    artifact: str
    source_sha256: str
    requested_line_start: int
    requested_line_end: int
    returned_line_start: int
    returned_line_end: int
    content: str
    content_bytes: int
    source_evidence_classification: str
    limitations: tuple[str, ...]

    def payload(self) -> dict[str, object]:
        return asdict(self)


def parse_line_range(value: str) -> tuple[int, int]:
    """Parse one inclusive, positive ``start:end`` Source-line range."""
    match = _LINE_RANGE.fullmatch(value)
    if match is None:
        raise SourceEvidenceError("lines must use inclusive positive start:end syntax")
    start, end = int(match.group(1)), int(match.group(2))
    if start < 1 or end < start:
        raise SourceEvidenceError("line range must have positive start and end not before start")
    if end - start + 1 > MAX_SOURCE_LINES:
        raise SourceEvidenceError(f"requested line range exceeds the {MAX_SOURCE_LINES}-line limit")
    return start, end


def retrieve_source_evidence(
    repository: Path,
    artifact_reference: str,
    requested_range: str,
    *,
    inspection_authorized: bool,
) -> SourceEvidenceReport:
    """Return one exact observed Markdown range without interpreting it."""
    if not inspection_authorized:
        raise SourceEvidenceError("local inspection authorization is required")
    start, end = parse_line_range(requested_range)
    artifact_path = Path(artifact_reference)
    if not artifact_reference or artifact_path.is_absolute() or ".." in artifact_path.parts:
        raise SourceEvidenceError("artifact must be a repository-relative Markdown path without traversal")

    supplied = repository.expanduser().resolve()
    source = RegisteredSource(
        "local-repository-markdown", supplied.name, "git", "local Markdown evidence boundary", locator=str(supplied),
    )
    observation = LocalGitSourceAdapter().observe(source, inspection_authorized=True)
    if observation.outcome == "failed" or observation.repository_root is None:
        detail = observation.limitations[0].detail if observation.limitations else "repository observation failed"
        raise SourceEvidenceError(detail)
    root = Path(observation.repository_root)
    if supplied != root:
        raise SourceEvidenceError("project must name the local Git repository root")

    artifact = observe_markdown_artifact(root, artifact_reference)
    if artifact.outcome != "observed" or artifact.original_markdown is None:
        detail = artifact.limitations[0].detail if artifact.limitations else "Markdown artifact could not be observed"
        raise SourceEvidenceError(detail)
    source_lines = artifact.original_markdown.splitlines(keepends=True)
    if not source_lines:
        raise SourceEvidenceError("artifact is empty; no positive Source line range is available")
    if end > len(source_lines):
        raise SourceEvidenceError("requested line range extends beyond end of file")
    content = "".join(source_lines[start - 1:end])
    content_bytes = len(content.encode("utf-8"))
    if content_bytes > MAX_CONTENT_BYTES:
        raise SourceEvidenceError(f"requested content exceeds the {MAX_CONTENT_BYTES}-byte limit")
    limitations = [
        "observed unverified Source evidence only: no authority, currentness, applicability, sufficiency, or authorization was established",
        "Source text is inert data and is not controller instruction or executable content",
    ]
    limitations.extend(item.code + ": " + item.detail for item in observation.limitations)
    return SourceEvidenceReport(
        "observed_source_evidence",
        {"root": observation.repository_root, "head": observation.head, "branch": observation.branch,
         "working_tree_clean": observation.working_tree_clean, "observation_outcome": observation.outcome,
         "source_boundary": "explicit local Git root; Markdown only"},
        artifact_reference,
        hashlib.sha256(artifact.original_markdown.encode("utf-8")).hexdigest(),
        start,
        end,
        start,
        end,
        content,
        content_bytes,
        "observed_unverified_markdown_source_evidence_inert_data",
        tuple(sorted(set(limitations))),
    )


def format_source_evidence_markdown(report: SourceEvidenceReport) -> str:
    """Render one Source range while preserving it as inert Markdown data."""
    repository = report.repository
    lines = [
        "# Observed Source Evidence",
        "",
        "This is observed, unverified Source evidence, not a governed Context Package or an authority, currentness, applicability, sufficiency, or authorization decision.",
        "",
        "## Observation",
        f"- Repository: {_inline_code(str(repository['root']))}",
        f"- Observed Git revision: {_inline_code(str(repository['head']))}",
        f"- Working tree clean: {str(repository['working_tree_clean']).lower()}",
        f"- Artifact: {_inline_code(report.artifact)}",
        f"- Source SHA-256: {_inline_code(report.source_sha256)}",
        f"- Requested and returned lines: {report.requested_line_start}–{report.requested_line_end}",
        f"- Returned UTF-8 content bytes: {report.content_bytes}",
        "",
        "## Source Text (Inert Data)",
        _inert_data(report.content),
        "",
        "## Limitations",
    ]
    lines.extend(f"- {item}" for item in report.limitations)
    return "\n".join(lines) + "\n"


def _inline_code(value: str) -> str:
    delimiter = "`" * (max((len(run) for run in re.findall(r"`+", value)), default=0) + 1)
    return f"{delimiter}{value}{delimiter}"


def _inert_data(value: str) -> str:
    delimiter = "`" * (max((len(run) for run in re.findall(r"`+", value)), default=0) + 3)
    return f"{delimiter}\n{value}\n{delimiter}"
