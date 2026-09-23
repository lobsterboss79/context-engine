"""Deterministic Markdown evidence transformation for Workstream 5.

The output is structural evidence.  It does not identify Claims, infer
governance, create Candidate Context, or select Context Items.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from markdown_it import MarkdownIt
import markdown_it

from context_engine.core.model import (
    Artifact, ArtifactVersion, EpistemicState, Provenance, RepresentedInformation, SemanticIdentity,
    TransformationKind, Uncertainty,
)


PARSER_CONFIGURATION = "markdown-it-py-4/commonmark+table"
MAX_MARKDOWN_BYTES = 1024 * 1024


@dataclass(frozen=True)
class MarkdownArtifactObservation:
    """Bounded local Artifact evidence before parsing/transformation."""

    locator: str
    outcome: str
    original_markdown: str | None = None
    limitations: tuple[Uncertainty, ...] = ()


def observe_markdown_artifact(repository_root: Path, source_relative_locator: str, *, max_bytes: int = MAX_MARKDOWN_BYTES) -> MarkdownArtifactObservation:
    """Read one in-scope Markdown file without executing or interpreting it.

    A relative locator is required so a registered Git Source cannot use this
    path to escape its observed work-tree boundary.  UTF-8 is the supported
    v0.1 textual evidence encoding; other byte sequences remain an explicit
    uninterpretable Artifact condition rather than silently normalized text.
    """
    candidate = Path(source_relative_locator)
    if candidate.is_absolute() or ".." in candidate.parts:
        return _artifact_failure(source_relative_locator, "artifact-path-outside-source", "Artifact path is outside the observed Source boundary.")
    if candidate.suffix.lower() not in {".md", ".markdown"}:
        return _artifact_failure(source_relative_locator, "unsupported-artifact-type", "Only Markdown Artifacts are supported in this workstream.")
    try:
        root = repository_root.resolve(strict=True)
        path = (root / candidate).resolve(strict=True)
        path.relative_to(root)
        payload = path.read_bytes()
    except (OSError, ValueError):
        return _artifact_failure(source_relative_locator, "artifact-unavailable", "Markdown Artifact could not be read within the observed Source boundary.")
    if len(payload) > max_bytes:
        return _artifact_failure(source_relative_locator, "artifact-output-bounded", "Markdown Artifact exceeds the configured observation bound.")
    try:
        original = payload.decode("utf-8")
    except UnicodeDecodeError:
        return _artifact_failure(source_relative_locator, "artifact-uninterpretable-encoding", "Markdown Artifact is not supported UTF-8 text.")
    return MarkdownArtifactObservation(source_relative_locator, "observed", original)


def _artifact_failure(locator: str, code: str, detail: str) -> MarkdownArtifactObservation:
    return MarkdownArtifactObservation(locator, "failed", limitations=(Uncertainty(EpistemicState.UNAVAILABLE, detail=code + ": " + detail),))


@dataclass(frozen=True)
class MarkdownBlock:
    ordinal: int
    kind: str
    content: str
    line_start: int | None
    line_end: int | None
    parent_heading: int | None
    links: tuple[str, ...] = ()


@dataclass(frozen=True)
class MarkdownTransformation:
    artifact: Artifact
    version: ArtifactVersion
    original_markdown: str
    parser_version: str
    parser_configuration: str
    blocks: tuple[MarkdownBlock, ...]
    limitations: tuple[Uncertainty, ...] = ()


def transform_markdown(
    *, source_identity: SemanticIdentity, artifact_identity: SemanticIdentity,
    artifact_version_identity: SemanticIdentity, source_locator: str,
    native_state_reference: str | None, original_markdown: str,
    observation_provenance: Provenance,
) -> MarkdownTransformation:
    """Preserve original text and derive deterministic, inert block evidence."""
    if artifact_identity.kind != "artifact" or artifact_version_identity.kind != "artifact_version":
        raise ValueError("explicit Artifact and Artifact Version semantic identities are required")
    parser = MarkdownIt("commonmark").enable("table")
    tokens = parser.parse(original_markdown)
    blocks: list[MarkdownBlock] = []
    heading_stack: list[tuple[int, int]] = []
    for token in tokens:
        if token.type in {"heading_open", "paragraph_open", "bullet_list_open", "ordered_list_open", "fence", "code_block", "table_open", "blockquote_open", "html_block"}:
            line_start, line_end = _line_range(token.map)
            parent = heading_stack[-1][1] if heading_stack else None
            kind = "raw_html" if token.type == "html_block" else token.type.removesuffix("_open")
            content, links = "", ()
            if token.type in {"fence", "code_block", "html_block"}:
                content = token.content
            if token.type == "heading_open":
                level = int(token.tag[1:])
                while heading_stack and heading_stack[-1][0] >= level:
                    heading_stack.pop()
                parent = heading_stack[-1][1] if heading_stack else None
                heading_stack.append((level, len(blocks)))
            blocks.append(MarkdownBlock(len(blocks), kind, content, line_start, line_end, parent, links))
        elif token.type == "inline" and blocks:
            links = tuple(child.attrGet("href") for child in token.children or () if child.type == "link_open" and child.attrGet("href"))
            prior = blocks[-1]
            if prior.kind in {"heading", "paragraph"}:
                blocks[-1] = MarkdownBlock(prior.ordinal, prior.kind, token.content, prior.line_start, prior.line_end, prior.parent_heading, links)
    artifact = Artifact(artifact_identity, source_identity, (source_locator,))
    version = ArtifactVersion(artifact_version_identity, artifact_identity, native_state_reference, observation_provenance)
    return MarkdownTransformation(artifact, version, original_markdown, markdown_it.__version__, PARSER_CONFIGURATION, tuple(blocks))


def represent_markdown_blocks(
    transformation: MarkdownTransformation,
    representation_identities: Iterable[SemanticIdentity],
    provenance_identities: Iterable[SemanticIdentity],
) -> tuple[RepresentedInformation, ...]:
    """Create only explicitly identified representation records for blocks."""
    identities = tuple(representation_identities)
    provenance_ids = tuple(provenance_identities)
    if len(identities) != len(transformation.blocks) or len(provenance_ids) != len(transformation.blocks):
        raise ValueError("each represented block requires explicit representation and Provenance semantic identities")
    represented: list[RepresentedInformation] = []
    for identity, provenance_identity, block in zip(identities, provenance_ids, transformation.blocks, strict=True):
        if identity.kind != "represented_information":
            raise ValueError("represented information requires an explicit semantic identity")
        if provenance_identity.kind != "provenance":
            raise ValueError("represented information Provenance requires an explicit semantic identity")
        location = _location(block)
        provenance = Provenance(
            provenance_identity,
            source=transformation.artifact.source, artifact=transformation.artifact.identity,
            artifact_version=transformation.version.identity,
            upstream=(transformation.version.provenance.identity,) if transformation.version.provenance else (),
            transformation=TransformationKind.NORMALIZED,
            location_reference=location,
            transformation_reference=f"{transformation.parser_configuration}; version={transformation.parser_version}",
            limitations=transformation.limitations,
        )
        represented.append(RepresentedInformation(identity, transformation.artifact.identity, provenance, uncertainty=transformation.limitations))
    return tuple(represented)


def _line_range(token_map: list[int] | None) -> tuple[int | None, int | None]:
    if token_map is None:
        return None, None
    return token_map[0] + 1, token_map[1]


def _location(block: MarkdownBlock) -> str:
    if block.line_start is None:
        return f"block:{block.ordinal}"
    return f"block:{block.ordinal};lines:{block.line_start}-{block.line_end}"
