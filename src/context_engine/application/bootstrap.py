"""Explicit Bootstrap and Project-configuration application boundary."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import tomllib

class GovernanceEstablishmentError(ValueError):
    pass

@dataclass(frozen=True)
class Bootstrap:
    reference: Path
    project_identity: str
    scope: str
    governance_basis: str
    project_configuration_reference: Path

@dataclass(frozen=True)
class ProjectConfiguration:
    reference: Path
    project_identity: str
    governance_reference: str

def _load(reference: Path) -> dict[str, object]:
    try:
        with reference.open("rb") as source:
            return tomllib.load(source)
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise GovernanceEstablishmentError("Bootstrap/configuration is unavailable or malformed") from error

def establish_bootstrap(reference: Path | None, *, operator_authorized: bool) -> Bootstrap:
    if reference is None:
        raise GovernanceEstablishmentError("explicit Bootstrap reference is required")
    if not operator_authorized:
        raise GovernanceEstablishmentError("operator is not authorized to establish governance")
    data = _load(reference)
    section = data.get("bootstrap")
    if data.get("version") != 1 or not isinstance(section, dict):
        raise GovernanceEstablishmentError("unsupported Bootstrap version or structure")
    project, scope = section.get("project"), section.get("scope")
    basis, config = section.get("governance_basis"), section.get("project_configuration")
    if not all(isinstance(value, str) and value for value in (project, scope, basis, config)):
        raise GovernanceEstablishmentError("Bootstrap required fields are missing or inconsistent")
    config_reference = Path(config)
    if not config_reference.is_absolute():
        config_reference = reference.parent / config_reference
    return Bootstrap(reference, project, scope, basis, config_reference)

def load_project_configuration(bootstrap: Bootstrap, reference: Path) -> ProjectConfiguration:
    if reference != bootstrap.project_configuration_reference:
        raise GovernanceEstablishmentError("Project configuration is outside Bootstrap-established reference")
    data = _load(reference)
    section = data.get("project")
    if data.get("version") != 1 or not isinstance(section, dict):
        raise GovernanceEstablishmentError("unsupported Project configuration version or structure")
    project, governance = section.get("identity"), section.get("governance_reference")
    if project != bootstrap.project_identity or not isinstance(governance, str) or not governance:
        raise GovernanceEstablishmentError("Project configuration does not match established Bootstrap scope")
    return ProjectConfiguration(reference, project, governance)
