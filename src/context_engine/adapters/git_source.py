"""Local, read-oriented Git observation adapter for Workstream 5.

This module deliberately observes only the local repository supplied by a
registered Source.  It never contacts a remote, executes a shell, runs hooks,
or turns native Git facts into governance/currentness assertions.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
import os
import subprocess
from typing import Callable

from context_engine.application.lifecycle import RegisteredSource


MAX_OUTPUT_BYTES = 256 * 1024
DEFAULT_TIMEOUT_SECONDS = 5.0


@dataclass(frozen=True)
class GitLimitation:
    code: str
    detail: str


@dataclass(frozen=True)
class GitCommandResult:
    arguments: tuple[str, ...]
    returncode: int
    stdout: bytes
    stderr: bytes
    truncated: bool = False


@dataclass(frozen=True)
class GitObservation:
    """Evidence established during one bounded local observation."""

    source_identity: str
    source_scope: str
    locator: str
    observation_time: str
    outcome: str
    repository_root: str | None = None
    head: str | None = None
    branch: str | None = None
    detached_head: bool = False
    unborn: bool = False
    working_tree_clean: bool | None = None
    staged_paths: tuple[str, ...] = ()
    unstaged_paths: tuple[str, ...] = ()
    untracked_paths: tuple[str, ...] = ()
    history: tuple[str, ...] = ()
    remote_names: tuple[str, ...] = ()
    limitations: tuple[GitLimitation, ...] = ()


class LocalGitSourceAdapter:
    """Use native Git through fixed, shell-free argument vectors only."""

    def __init__(
        self,
        *,
        git_executable: str = "git",
        timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
        max_output_bytes: int = MAX_OUTPUT_BYTES,
        now: Callable[[], datetime] | None = None,
    ) -> None:
        self._git = git_executable
        self._timeout = timeout_seconds
        self._max_output = max_output_bytes
        self._now = now or (lambda: datetime.now(UTC))

    def capabilities(self) -> tuple[str, ...]:
        return ("repository-identity", "head", "branch", "working-tree", "bounded-history", "local-remotes")

    def _environment(self) -> dict[str, str]:
        environment = {"PATH": os.environ.get("PATH", "")}
        environment.update({
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_TERMINAL_PROMPT": "0",
            "GIT_PAGER": "cat",
            "GIT_OPTIONAL_LOCKS": "0",
            "LC_ALL": "C",
            "LANG": "C",
        })
        return environment

    def _run(self, repository: Path, *arguments: str) -> GitCommandResult:
        command = (
            self._git, "-c", "core.hooksPath=/dev/null", "-c", "core.fsmonitor=false",
            "-c", "credential.helper=", "-C", os.fspath(repository), *arguments,
        )
        try:
            completed = subprocess.run(
                command, shell=False, check=False, stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                env=self._environment(), timeout=self._timeout,
            )
        except FileNotFoundError:
            return GitCommandResult(command, 127, b"", b"git executable unavailable")
        except subprocess.TimeoutExpired:
            return GitCommandResult(command, 124, b"", b"git observation timed out")
        stdout, stderr = completed.stdout, completed.stderr
        truncated = len(stdout) > self._max_output or len(stderr) > self._max_output
        return GitCommandResult(command, completed.returncode, stdout[:self._max_output], stderr[:self._max_output], truncated)

    @staticmethod
    def _text(value: bytes) -> str:
        return value.decode("utf-8", errors="surrogateescape")

    def observe(self, source: RegisteredSource, *, inspection_authorized: bool) -> GitObservation:
        """Observe one registered local Git Source without changing it.

        ``inspection_authorized`` is an already-established input.  This
        adapter neither evaluates nor broadens authorization.
        """
        timestamp = self._now().astimezone(UTC).isoformat()
        locator = source.locator or ""
        if source.source_type != "git":
            return self._failure(source, locator, timestamp, "unsupported-source-type", "Source is not registered as a local Git Source")
        if not inspection_authorized:
            return self._failure(source, locator, timestamp, "observation-not-authorized", "inspection authorization was not established")
        if not locator:
            return self._failure(source, locator, timestamp, "unavailable-locator", "registered Source has no local repository locator")
        repository = Path(locator)
        inside = self._run(repository, "rev-parse", "--is-inside-work-tree")
        if inside.returncode == 127:
            return self._failure(source, locator, timestamp, "git-unavailable", "native Git executable is unavailable")
        if inside.returncode == 124:
            return self._failure(source, locator, timestamp, "git-timeout", "repository inspection timed out")
        if inside.truncated:
            return self._failure(source, locator, timestamp, "git-output-bounded", "repository identity output exceeded observation bound")
        if inside.returncode != 0 or self._text(inside.stdout).strip() != "true":
            return self._failure(source, locator, timestamp, "repository-unavailable-or-invalid", "registered local repository was not established")

        root_result = self._run(repository, "rev-parse", "--show-toplevel")
        if root_result.returncode != 0 or root_result.truncated:
            return self._failure(source, locator, timestamp, "repository-identity-unavailable", "repository root could not be established")
        root = self._text(root_result.stdout).rstrip("\n")
        limitations: list[GitLimitation] = [
            GitLimitation("local-observation-only", "No remote, shared, governing, or current state was established."),
            GitLimitation("scope-native-expression-unavailable", "The registered Source Scope is retained as governed provenance; no unapproved native scope grammar was interpreted."),
        ]
        head_before = self._run(repository, "rev-parse", "--verify", "HEAD")
        if head_before.returncode in {124, 127} or head_before.truncated:
            return self._failure(source, locator, timestamp, "head-state-unavailable", "HEAD state could not be established within observation bounds")
        unborn = head_before.returncode != 0
        head = None if unborn else self._text(head_before.stdout).strip()
        branch_result = self._run(repository, "symbolic-ref", "--quiet", "--short", "HEAD")
        branch = self._text(branch_result.stdout).strip() if branch_result.returncode == 0 else None
        detached = not unborn and branch is None
        if unborn:
            limitations.append(GitLimitation("unborn-head", "HEAD has no commit; revision/history evidence is unavailable."))
        if detached:
            limitations.append(GitLimitation("detached-head", "No symbolic branch membership was established."))

        status = self._run(repository, "status", "--porcelain=v1", "-z", "--untracked-files=all")
        staged, unstaged, untracked = self._parse_status(status.stdout) if status.returncode == 0 and not status.truncated else ((), (), ())
        if status.returncode != 0:
            limitations.append(GitLimitation("working-tree-state-unavailable", "Working-tree state could not be completely observed."))
        if status.truncated:
            limitations.append(GitLimitation("working-tree-output-bounded", "Working-tree output exceeded the observation bound."))
        if branch_result.returncode not in {0, 1} or branch_result.truncated:
            limitations.append(GitLimitation("branch-state-unavailable", "Symbolic branch state could not be completely observed."))

        history_result = self._run(repository, "log", "--format=%H", "-n", "32") if not unborn else None
        history = ()
        if history_result is not None and history_result.returncode == 0 and not history_result.truncated:
            history = tuple(item for item in self._text(history_result.stdout).splitlines() if item)
        elif not unborn:
            limitations.append(GitLimitation("history-unavailable-or-bounded", "Only unavailable or bounded local history could be established."))
        shallow_result = self._run(repository, "rev-parse", "--is-shallow-repository")
        if shallow_result.returncode == 0 and self._text(shallow_result.stdout).strip() == "true":
            limitations.append(GitLimitation("shallow-history", "Repository reports shallow local history; history completeness was not established."))
        remotes_result = self._run(repository, "remote")
        remote_names = tuple(item for item in self._text(remotes_result.stdout).splitlines() if item) if remotes_result.returncode == 0 and not remotes_result.truncated else ()
        if remote_names:
            limitations.append(GitLimitation("remote-names-source-reported", "Configured remote names are local configuration evidence, not remote reachability or synchronization evidence."))
        elif remotes_result.returncode != 0 or remotes_result.truncated:
            limitations.append(GitLimitation("remote-configuration-unavailable", "Configured local remote names could not be completely observed."))
        head_after = self._run(repository, "rev-parse", "--verify", "HEAD")
        after = self._text(head_after.stdout).strip() if head_after.returncode == 0 else None
        if head_after.returncode in {124, 127} or head_after.truncated:
            limitations.append(GitLimitation("observation-coherence-unavailable", "HEAD could not be rechecked across the observation boundary."))
        elif after != head:
            limitations.append(GitLimitation("repository-mutated-during-observation", "HEAD changed across the observation boundary; a coherent single state was not established."))
        partial_codes = {
            "working-tree-state-unavailable", "working-tree-output-bounded", "branch-state-unavailable",
            "history-unavailable-or-bounded", "shallow-history", "remote-configuration-unavailable",
            "repository-mutated-during-observation", "observation-coherence-unavailable",
        }
        outcome = "partial" if any(item.code in partial_codes for item in limitations) else "observed"
        return GitObservation(source.identity, source.scope, locator, timestamp, outcome, root, head, branch, detached, unborn,
                              status.returncode == 0 and not status.truncated and not (staged or unstaged or untracked),
                              staged, unstaged, untracked, history, remote_names, tuple(limitations))

    def _failure(self, source: RegisteredSource, locator: str, timestamp: str, code: str, detail: str) -> GitObservation:
        return GitObservation(source.identity, source.scope, locator, timestamp, "failed", limitations=(GitLimitation(code, detail),))

    def _parse_status(self, payload: bytes) -> tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]:
        staged: list[str] = []
        unstaged: list[str] = []
        untracked: list[str] = []
        parts = payload.split(b"\0")
        index = 0
        while index < len(parts):
            entry = parts[index]
            index += 1
            if not entry:
                continue
            if entry.startswith(b"?? "):
                untracked.append(self._text(entry[3:]))
                continue
            if len(entry) < 4:
                continue
            x, y, path = chr(entry[0]), chr(entry[1]), self._text(entry[3:])
            if x != " ":
                staged.append(path)
            if y != " ":
                unstaged.append(path)
            # porcelain v1 rename/copy supplies the original path as a second
            # NUL-delimited field; retain it as native path evidence.
            if x in "RC" and index < len(parts) and parts[index]:
                original = self._text(parts[index])
                index += 1
                staged.append(original)
        return tuple(staged), tuple(unstaged), tuple(untracked)
