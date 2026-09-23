"""Structural tests that keep the Workstream 1 core mechanism-independent."""

from __future__ import annotations

import ast
from pathlib import Path


FORBIDDEN_CORE_IMPORTS = {"argparse", "sqlite3", "subprocess", "tomllib", "markdown_it", "os", "platform", "shutil"}


def test_core_has_no_concrete_mechanism_imports() -> None:
    core_root = Path(__file__).parents[1] / "src" / "context_engine" / "core"
    imports: set[str] = set()
    for source_file in core_root.glob("*.py"):
        tree = ast.parse(source_file.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.add(node.module.split(".")[0])
    assert not imports & FORBIDDEN_CORE_IMPORTS


def test_workstream_one_does_not_define_governed_semantic_models() -> None:
    core_root = Path(__file__).parents[1] / "src" / "context_engine" / "core"
    source = "\n".join(path.read_text(encoding="utf-8") for path in core_root.glob("*.py"))
    assert "class Authority" not in source
    assert "class GovernanceState" not in source
    assert "class Currentness" not in source
