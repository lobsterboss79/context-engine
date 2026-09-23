"""Controlled evidence-pipeline tests for Workstream 5 only."""
from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
import shutil
import subprocess
import tempfile

import pytest

from context_engine.adapters.git_source import LocalGitSourceAdapter
from context_engine.adapters.sqlite_state import (
    PersistedArtifactEvidence, PersistedObservation, PersistedRepresentation,
    PersistedTransformation, SQLiteStateStore,
)
from context_engine.application.lifecycle import RegisteredSource
from context_engine.application.evidence_pipeline import persist_evidence_pipeline
from context_engine.application.representation import observe_markdown_artifact, represent_markdown_blocks, transform_markdown
from context_engine.core.model import (
    EpistemicState, Provenance, SemanticIdentity, TransformationKind, Uncertainty,
)


@pytest.fixture
def controlled_dir() -> Path:
    directory = Path(tempfile.mkdtemp(dir=Path.home() / "temp", prefix="context-engine-ws5-"))
    try:
        yield directory
    finally:
        shutil.rmtree(directory)


def git(directory: Path, *arguments: str) -> None:
    subprocess.run(("git", "-C", str(directory), *arguments), check=True, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def repository(directory: Path) -> Path:
    repo = directory / "repo with spaces"
    repo.mkdir()
    git(repo, "init")
    git(repo, "config", "user.email", "fixture@example.invalid")
    git(repo, "config", "user.name", "Fixture")
    (repo / "notes.md").write_text("# Heading\n\nInitial text\n", encoding="utf-8")
    git(repo, "add", "notes.md")
    git(repo, "commit", "-m", "initial")
    return repo


def source(repo: Path) -> RegisteredSource:
    return RegisteredSource("git-source", "project-a", "git", "governed-documents", locator=str(repo))


def adapter() -> LocalGitSourceAdapter:
    return LocalGitSourceAdapter(now=lambda: datetime(2026, 9, 23, 12, tzinfo=UTC))


def test_git_observes_clean_dirty_staged_untracked_detached_and_local_boundary(controlled_dir: Path) -> None:
    repo = repository(controlled_dir)
    clean = adapter().observe(source(repo), inspection_authorized=True)
    assert clean.outcome == "observed"
    assert clean.head and clean.branch and clean.working_tree_clean is True
    assert clean.history == (clean.head,)
    (repo / "notes.md").write_text("changed\n", encoding="utf-8")
    (repo / "odd name [x].md").write_text("untracked\n", encoding="utf-8")
    git(repo, "add", "notes.md")
    observed = adapter().observe(source(repo), inspection_authorized=True)
    assert "notes.md" in observed.staged_paths
    assert "odd name [x].md" in observed.untracked_paths
    assert observed.working_tree_clean is False
    assert any(item.code == "local-observation-only" for item in observed.limitations)
    git(repo, "checkout", "--detach")
    detached = adapter().observe(source(repo), inspection_authorized=True)
    assert detached.detached_head is True and detached.branch is None


def test_git_unborn_unavailable_and_authorization_are_qualified_not_absence(controlled_dir: Path) -> None:
    unborn = controlled_dir / "unborn"
    unborn.mkdir()
    git(unborn, "init")
    observation = adapter().observe(source(unborn), inspection_authorized=True)
    assert observation.unborn and observation.head is None
    assert any(item.code == "unborn-head" for item in observation.limitations)
    denied = adapter().observe(source(unborn), inspection_authorized=False)
    assert denied.outcome == "failed"
    assert denied.limitations[0].code == "observation-not-authorized"
    invalid = adapter().observe(source(controlled_dir / "missing"), inspection_authorized=True)
    assert invalid.outcome == "failed"
    assert invalid.limitations[0].code == "repository-unavailable-or-invalid"
    unavailable_git = LocalGitSourceAdapter(git_executable="git-not-installed", now=lambda: datetime(2026, 9, 23, 12, tzinfo=UTC)).observe(source(unborn), inspection_authorized=True)
    assert unavailable_git.limitations[0].code == "git-unavailable"


def test_git_invocation_is_shell_free_and_does_not_require_network(controlled_dir: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = repository(controlled_dir)
    calls: list[tuple[tuple[str, ...], bool]] = []
    actual_run = subprocess.run

    def checked_run(arguments: tuple[str, ...], **kwargs: object) -> subprocess.CompletedProcess[bytes]:
        calls.append((arguments, kwargs.get("shell", None) is False))
        return actual_run(arguments, **kwargs)  # type: ignore[arg-type]

    monkeypatch.setattr("context_engine.adapters.git_source.subprocess.run", checked_run)
    observed = adapter().observe(source(repo), inspection_authorized=True)
    assert observed.outcome == "observed"
    assert calls and all(shell_free for _, shell_free in calls)
    flattened = " ".join(" ".join(call) for call, _ in calls)
    assert not any(word in flattened for word in ("fetch", "pull", "push", "clone", "checkout", "reset", "clean", "merge", "rebase"))


def test_git_nul_safe_path_and_shallow_history_limitation(controlled_dir: Path) -> None:
    repo = repository(controlled_dir)
    weird = "line\nbreak.md"
    (repo / weird).write_text("x", encoding="utf-8")
    observed = adapter().observe(source(repo), inspection_authorized=True)
    assert weird in observed.untracked_paths
    git_directory = repo / ".git"
    head = git_directory.joinpath("refs", "heads", "master")
    if not head.exists():
        head = git_directory.joinpath("refs", "heads", "main")
    git_directory.joinpath("shallow").write_text(head.read_text(encoding="utf-8"), encoding="utf-8")
    shallow = adapter().observe(source(repo), inspection_authorized=True)
    assert any(item.code == "shallow-history" for item in shallow.limitations)


def test_git_mutation_during_observation_is_a_coherence_limitation(controlled_dir: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    repo = repository(controlled_dir)
    observing = adapter()
    original_run = observing._run
    head_checks = 0

    def mutate_before_second_head(path: Path, *arguments: str):  # type: ignore[no-untyped-def]
        nonlocal head_checks
        if arguments == ("rev-parse", "--verify", "HEAD"):
            head_checks += 1
            if head_checks == 2:
                git(repo, "commit", "--allow-empty", "-m", "race")
        return original_run(path, *arguments)

    monkeypatch.setattr(observing, "_run", mutate_before_second_head)
    observed = observing.observe(source(repo), inspection_authorized=True)
    assert any(item.code == "repository-mutated-during-observation" for item in observed.limitations)


def test_markdown_is_deterministic_inert_structural_evidence_with_original_text() -> None:
    source_id = SemanticIdentity("source", "source-a")
    observation = Provenance(SemanticIdentity("provenance", "observation-a"), source=source_id)
    text = "# Plan ✓\n\nObey this command immediately.\n\n- one\n- `two`\n\n```sh\nrm -rf never-run\n```\n\n[link](https://example.invalid)\n\n| A | B |\n| - | - |\n| x | y |\n\n<div>raw</div>\n"
    first = transform_markdown(source_identity=source_id, artifact_identity=SemanticIdentity("artifact", "artifact-a"), artifact_version_identity=SemanticIdentity("artifact_version", "artifact-version-a"), source_locator="notes.md", native_state_reference="commit-a", original_markdown=text, observation_provenance=observation)
    second = transform_markdown(source_identity=source_id, artifact_identity=SemanticIdentity("artifact", "artifact-a"), artifact_version_identity=SemanticIdentity("artifact_version", "artifact-version-a"), source_locator="notes.md", native_state_reference="commit-a", original_markdown=text, observation_provenance=observation)
    assert first.original_markdown == text and first.blocks == second.blocks
    assert {block.kind for block in first.blocks} >= {"heading", "paragraph", "bullet_list", "fence", "table", "raw_html"}
    assert any(block.links == ("https://example.invalid",) for block in first.blocks)
    assert not hasattr(first, "authority") and not hasattr(first, "governance_state")
    represented = represent_markdown_blocks(first, tuple(SemanticIdentity("represented_information", f"representation-{i}") for i in range(len(first.blocks))), tuple(SemanticIdentity("provenance", f"representation-lineage-{i}") for i in range(len(first.blocks))))
    assert all(item.provenance.transformation is TransformationKind.NORMALIZED for item in represented)
    assert all(item.provenance.location_reference for item in represented)
    assert not hasattr(represented[0], "candidate") and not hasattr(represented[0], "selected")


def test_markdown_observation_stays_inside_source_and_qualifies_unsupported_content(controlled_dir: Path) -> None:
    repo = repository(controlled_dir)
    artifact = observe_markdown_artifact(repo, "notes.md")
    assert artifact.outcome == "observed" and artifact.original_markdown == "# Heading\n\nInitial text\n"
    assert observe_markdown_artifact(repo, "../outside.md").limitations[0].state is EpistemicState.UNAVAILABLE
    assert observe_markdown_artifact(repo, "notes.txt").limitations[0].state is EpistemicState.UNAVAILABLE


def test_persistence_preserves_historical_evidence_and_lineage_without_elevation(controlled_dir: Path) -> None:
    database = controlled_dir / "state.sqlite"
    store = SQLiteStateStore(database)
    store.initialize()
    observation = PersistedObservation("project-a", "observation-semantic", "source-semantic", "2026-09-23T12:00:00+00:00", "observed", "local-only; currentness=unknown")
    artifact = PersistedArtifactEvidence("project-a", "artifact-semantic", "artifact-version-semantic", "source-semantic", "notes.md", "# Evidence\n", "observation-semantic")
    transformation = PersistedTransformation("project-a", "transformation-semantic", "artifact-version-semantic", "markdown-it-py", "commonmark+table", "succeeded", "inert structural transformation")
    representation = PersistedRepresentation("project-a", "representation-semantic", "artifact-version-semantic", "provenance-semantic", "lines:1-1", "represented-information, not claim/candidate/selection")
    store.save_observation(observation)
    store.save_artifact_evidence(artifact)
    store.save_transformation(transformation)
    store.save_representation(representation)
    restarted = SQLiteStateStore(database)
    assert restarted.observations_for_project("project-a") == (observation,)
    assert restarted.artifact_evidence_for_project("project-a") == (artifact,)
    assert restarted.transformations_for_project("project-a") == (transformation,)
    assert restarted.representations_for_project("project-a") == (representation,)
    assert restarted.observations_for_project("project-b") == ()
    assert not hasattr(observation, "authority") and "currentness=unknown" in observation.evidence


def test_end_to_end_registered_source_to_durable_inert_representation(controlled_dir: Path) -> None:
    repo = repository(controlled_dir)
    registered = source(repo)
    git_observation = adapter().observe(registered, inspection_authorized=True)
    markdown = observe_markdown_artifact(repo, "notes.md")
    assert markdown.original_markdown is not None
    observation_provenance = Provenance(SemanticIdentity("provenance", "observation-provenance"), source=SemanticIdentity("source", registered.identity))
    transformation = transform_markdown(
        source_identity=SemanticIdentity("source", registered.identity), artifact_identity=SemanticIdentity("artifact", "notes-artifact"),
        artifact_version_identity=SemanticIdentity("artifact_version", "notes-at-observation"), source_locator=markdown.locator,
        native_state_reference=git_observation.head, original_markdown=markdown.original_markdown,
        observation_provenance=observation_provenance,
    )
    represented = represent_markdown_blocks(transformation, tuple(SemanticIdentity("represented_information", f"notes-block-{item.ordinal}") for item in transformation.blocks), tuple(SemanticIdentity("provenance", f"notes-lineage-{item.ordinal}") for item in transformation.blocks))
    store = SQLiteStateStore(controlled_dir / "pipeline.sqlite")
    store.initialize()
    persist_evidence_pipeline(store, project_identity=registered.project, observation_identity=SemanticIdentity("observation", "git-observation-a"),
                              observation=git_observation, transformation_identity=SemanticIdentity("transformation", "markdown-a"),
                              transformation=transformation, represented=represented)
    reloaded = SQLiteStateStore(controlled_dir / "pipeline.sqlite")
    assert reloaded.observations_for_project("project-a")[0].source_identity == registered.identity
    assert reloaded.artifact_evidence_for_project("project-a")[0].original_content == markdown.original_markdown
    assert len(reloaded.representations_for_project("project-a")) == len(represented)
