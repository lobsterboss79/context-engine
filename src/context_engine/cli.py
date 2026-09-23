"""Native-CLI boundary for the Workstream 1 executable skeleton."""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Sequence

from context_engine.application.readiness import ReadinessReport, assess_readiness
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
    if args.operation != "readiness":  # Defensive until later operations are authorized.
        return 2

    report = assess_readiness(HostPrerequisiteProbe())
    output = _render_json(report) if args.format == "json" else _render_text(report)
    print(output)
    return 0 if report.ready else 2
