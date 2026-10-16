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


@dataclass(frozen=True)
class SourceEvidenceMetadata:
    """Metadata for one observed Markdown Source, without Source text."""

    status: str
    repository: dict[str, object]
    artifact: str
    source_sha256: str
    source_bytes: int
    source_lines: int
    maximum_retrieval_lines: int
    maximum_retrieval_content_bytes: int
    largest_valid_initial_range: dict[str, int] | None
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
    start, end = parse_line_range(requested_range)
    observation, artifact = _observe_markdown_source(repository, artifact_reference, inspection_authorized=inspection_authorized)
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


def inspect_source_evidence(
    repository: Path,
    artifact_reference: str,
    *,
    inspection_authorized: bool,
) -> SourceEvidenceMetadata:
    """Return bounded-request metadata without returning or interpreting Source text."""
    observation, artifact = _observe_markdown_source(repository, artifact_reference, inspection_authorized=inspection_authorized)
    assert artifact.original_markdown is not None
    source_lines = artifact.original_markdown.splitlines(keepends=True)
    initial_range = _largest_valid_initial_range(source_lines)
    limitations = [
        "observed Source metadata only: no authority, currentness, applicability, sufficiency, or authorization was established",
        "metadata does not disclose or interpret Source text",
    ]
    limitations.extend(item.code + ": " + item.detail for item in observation.limitations)
    return SourceEvidenceMetadata(
        "observed_source_metadata",
        {"root": observation.repository_root, "head": observation.head, "branch": observation.branch,
         "working_tree_clean": observation.working_tree_clean, "observation_outcome": observation.outcome,
         "source_boundary": "explicit local Git root; Markdown only"},
        artifact_reference,
        hashlib.sha256(artifact.original_markdown.encode("utf-8")).hexdigest(),
        len(artifact.original_markdown.encode("utf-8")),
        len(source_lines),
        MAX_SOURCE_LINES,
        MAX_CONTENT_BYTES,
        initial_range,
        "observed_unverified_markdown_source_metadata_inert_data",
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


def format_source_evidence_metadata_markdown(report: SourceEvidenceMetadata) -> str:
    """Render Source metadata without including raw Source text."""
    repository = report.repository
    initial_range = report.largest_valid_initial_range
    range_description = (
        f"1–{initial_range['line_end']} ({initial_range['content_bytes']} UTF-8 content bytes)"
        if initial_range is not None else "none (the Source is empty or its first line exceeds the byte limit)"
    )
    lines = [
        "# Observed Source Metadata",
        "",
        "This is observed, unverified Source metadata, not a governance, authority, currentness, applicability, sufficiency, or authorization determination. No Source text is included.",
        "",
        "## Observation",
        f"- Repository: {_inline_code(str(repository['root']))}",
        f"- Observed Git revision: {_inline_code(str(repository['head']))}",
        f"- Working tree clean: {str(repository['working_tree_clean']).lower()}",
        f"- Artifact: {_inline_code(report.artifact)}",
        f"- Source SHA-256: {_inline_code(report.source_sha256)}",
        f"- Source UTF-8 bytes: {report.source_bytes}",
        f"- Source lines: {report.source_lines}",
        f"- Retrieval limits: {report.maximum_retrieval_lines} lines; {report.maximum_retrieval_content_bytes} UTF-8 content bytes",
        f"- Largest valid initial retrieval range: {range_description}",
        "",
        "## Limitations",
    ]
    lines.extend(f"- {item}" for item in report.limitations)
    return "\n".join(lines) + "\n"


def _observe_markdown_source(
    repository: Path,
    artifact_reference: str,
    *,
    inspection_authorized: bool,
):
    """Apply the shared authorization, Git-root, and Markdown-containment checks."""
    if not inspection_authorized:
        raise SourceEvidenceError("local inspection authorization is required")
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
    return observation, artifact


def _largest_valid_initial_range(source_lines: list[str]) -> dict[str, int] | None:
    """Find the exact contiguous 1:N range that obeys both retrieval limits."""
    content_bytes = 0
    line_end = 0
    for line in source_lines[:MAX_SOURCE_LINES]:
        next_bytes = len(line.encode("utf-8"))
        if content_bytes + next_bytes > MAX_CONTENT_BYTES:
            break
        content_bytes += next_bytes
        line_end += 1
    if line_end == 0:
        return None
    return {"line_start": 1, "line_end": line_end, "line_count": line_end, "content_bytes": content_bytes}


def _inline_code(value: str) -> str:
    delimiter = "`" * (max((len(run) for run in re.findall(r"`+", value)), default=0) + 1)
    return f"{delimiter}{value}{delimiter}"


def _inert_data(value: str) -> str:
    delimiter = "`" * (max((len(run) for run in re.findall(r"`+", value)), default=0) + 3)
    return f"{delimiter}\n{value}\n{delimiter}"
