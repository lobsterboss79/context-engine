"""Native-CLI boundary for the Workstream 1 executable skeleton."""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from collections.abc import Sequence
from pathlib import Path

from context_engine.application.readiness import ReadinessReport, assess_readiness
from context_engine.application.bootstrap import GovernanceEstablishmentError, establish_bootstrap, load_project_configuration
from context_engine.application.cli_render_inputs import CliRenderInputError, load_governed_render_inputs
from context_engine.application.orchestration import run_governed_render
from context_engine.adapters.environment import HostPrerequisiteProbe


def build_parser() -> argparse.ArgumentParser:
    """Build the intentionally small, framework-free CLI parser."""
    parser = argparse.ArgumentParser(
        prog="context-engine",
        description="Context Engine executable skeleton.",
    )
    parser.add_argument("--version", action="version", version="context-engine 0.1.0")
    subparsers = parser.add_subparsers(dest="operation", required=True)
    readiness = subparsers.add_parser(
        "readiness",
        help="report non-governed runtime prerequisites",
    )
    readiness.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="diagnostic output format",
    )
    bootstrap = subparsers.add_parser(
        "bootstrap-validate",
        help="validate an explicit Bootstrap and its governed Project configuration",
    )
    bootstrap.add_argument("--bootstrap", required=True, help="explicit Bootstrap TOML reference")
    bootstrap.add_argument("--project-configuration", required=True, help="Bootstrap-established Project configuration TOML reference")
    render = subparsers.add_parser(
        "render",
        help="construct and render one explicitly governed local input document",
    )
    render.add_argument("--input", required=True, help="v1 governed render-input JSON document")
    render.add_argument("--output", required=True, help="new UTF-8 rendering destination; existing files are never overwritten")
    return parser


def _render_text(report: ReadinessReport) -> str:
    lines = [f"status: {'ready' if report.ready else 'not ready'}"]
    lines.extend(f"{check.name}: {'ok' if check.available else 'unavailable'}" for check in report.checks)
    return "\n".join(lines)


def _render_json(report: ReadinessReport) -> str:
    return json.dumps(
        {
            "status": "ready" if report.ready else "not_ready",
            "checks": [
                {"name": check.name, "available": check.available, "detail": check.detail}
                for check in report.checks
            ],
        },
        sort_keys=True,
    )


def main(argv: Sequence[str] | None = None) -> int:
    """Run a non-governed CLI operation with safe prerequisite diagnostics."""
    args = build_parser().parse_args(argv)
    if args.operation == "bootstrap-validate":
        try:
            bootstrap = establish_bootstrap(Path(args.bootstrap), operator_authorized=True)
            configuration = load_project_configuration(bootstrap, Path(args.project_configuration))
        except GovernanceEstablishmentError as error:
            print("bootstrap validation failed: " + str(error), file=sys.stderr)
            return 2
        print(json.dumps({"bootstrap": str(bootstrap.reference), "project": configuration.project_identity, "status": "validated"}, sort_keys=True))
        return 0
    if args.operation == "render":
        return _run_render(Path(args.input), Path(args.output))
    if args.operation != "readiness":
        return 2

    report = assess_readiness(HostPrerequisiteProbe())
    output = _render_json(report) if args.format == "json" else _render_text(report)
    print(output)
    return 0 if report.ready else 2


def _run_render(input_reference: Path, output_reference: Path) -> int:
    """Run one governed composition and atomically create a new rendering file."""
    try:
        inputs = load_governed_render_inputs(input_reference)
        outcome = run_governed_render(inputs)
        if outcome.rendering.status != "rendered" or outcome.rendering.content is None:
            print("render failed: " + ",".join(outcome.rendering.reason_codes), file=sys.stderr)
            return 2
        _write_new_utf8(output_reference, outcome.rendering.content)
    except (CliRenderInputError, GovernanceEstablishmentError, ValueError, OSError) as error:
        print("render failed: " + str(error), file=sys.stderr)
        return 2
    package = outcome.construction.package
    assert package is not None  # a rendered outcome always has a logical package
    print(json.dumps({
        "coherence": outcome.construction.record.coherence.outcome if outcome.construction.record.coherence else None,
        "output": str(output_reference),
        "rendering_status": outcome.rendering.status,
        "selected_context_items": len(package.items),
        "status": "rendered",
        "sufficiency": package.sufficiency.value,
    }, sort_keys=True))
    return 0


def _write_new_utf8(destination: Path, content: str) -> None:
    """Publish only a complete rendering and never replace an existing artifact."""
    parent = destination.parent
    if destination.exists():
        raise ValueError("output destination already exists")
    if not parent.is_dir():
        raise ValueError("output destination parent directory does not exist")
    encoded = content.encode("utf-8")
    temporary_name: str | None = None
    try:
        with tempfile.NamedTemporaryFile(mode="xb", dir=parent, prefix=".context-engine-render-", delete=False) as temporary:
            temporary_name = temporary.name
            temporary.write(encoded)
            temporary.flush()
            os.fsync(temporary.fileno())
        # link is atomic and fails if another process created the destination.
        os.link(temporary_name, destination)
    finally:
        if temporary_name is not None:
            try:
                Path(temporary_name).unlink()
            except FileNotFoundError:
                pass
