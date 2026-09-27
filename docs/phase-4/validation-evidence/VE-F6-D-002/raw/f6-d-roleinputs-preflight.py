"""Local-only procedure preflight for the frozen FX-F6-D role input."""
from __future__ import annotations

from dataclasses import asdict
import json

from context_engine.application.decision_pipeline import RoleInputs


def main() -> None:
    # This constructs only the frozen role input; it does not invoke a pipeline.
    role = RoleInputs(
        omission_risks_incorrect_performance=False,
        omission_risks_improper_performance=False,
        materially_improves_understanding_or_validation=True,
        basis=(
            "FX-F6-D frozen task mapping establishes the known staging and "
            "safety-review information as useful Supporting Context, without "
            "treating it as proof of ASU adequacy."
        ),
    )
    fields = asdict(role)
    required_trigger = (
        role.omission_risks_incorrect_performance
        or role.omission_risks_improper_performance
    )
    print(json.dumps({
        "procedure": "local RoleInputs construction only",
        "pipeline_executed": False,
        "role_inputs": fields,
        "required_trigger": required_trigger,
        "supporting_trigger": role.materially_improves_understanding_or_validation,
        "preflight": "pass" if not required_trigger and role.materially_improves_understanding_or_validation else "fail",
    }, indent=2, sort_keys=True))
    if required_trigger or not role.materially_improves_understanding_or_validation:
        raise SystemExit("F6-D procedure preflight failed")


if __name__ == "__main__":
    main()
