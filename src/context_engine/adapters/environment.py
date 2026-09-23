"""Direct-host adapter for non-governed prerequisite observation."""

from __future__ import annotations

import os
import platform
import shutil
import sys

from context_engine.ports.environment import PrerequisiteCheck


class HostPrerequisiteProbe:
    """Observe only approved direct-host prerequisites for the skeleton."""

    def checks(self) -> tuple[PrerequisiteCheck, ...]:
        implementation = platform.python_implementation()
        runtime_ok = implementation == "CPython" and sys.version_info[:2] == (3, 14)
        platform_ok = platform.system() == "Linux" and platform.machine().lower() in {"x86_64", "amd64"}
        non_root = not hasattr(os, "geteuid") or os.geteuid() != 0
        git_available = shutil.which("git") is not None
        return (
            PrerequisiteCheck("cpython-3.14", runtime_ok, implementation),
            PrerequisiteCheck("linux-x86-64", platform_ok, platform.system()),
            PrerequisiteCheck("ordinary-non-root", non_root, "process privilege check"),
            PrerequisiteCheck("git-cli", git_available, "git executable check"),
        )
