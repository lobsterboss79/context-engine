"""Narrow SQLite EB-03 adapter; rows never define semantic identity."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import sqlite3

class StateCompatibilityError(RuntimeError):
    """Raised when an application-owned schema cannot be safely used."""


class SecretValueError(ValueError):
    """Raised when a normal state/audit value resembles a secret."""


CURRENT_SCHEMA_VERSION = 4

@dataclass(frozen=True)
class PersistedEvidence:
    project_identity: str
    semantic_identity: str
    historical_reference: str
    currentness: str = "unknown"
    authority_basis: str | None = None


@dataclass(frozen=True)
class PersistedSourceRegistration:
    """Durable lifecycle facts, excluding semantic elevation fields by design."""

    project_identity: str
    source_identity: str
    source_type: str
    scope: str
    availability: str
    locator: str | None = None


@dataclass(frozen=True)
class PersistedObservation:
    project_identity: str
    observation_identity: str
    source_identity: str
    observed_at: str
    outcome: str
    evidence: str


@dataclass(frozen=True)
class PersistedArtifactEvidence:
    project_identity: str
    artifact_identity: str
    artifact_version_identity: str
    source_identity: str
    locator: str
    original_content: str
    observation_identity: str


@dataclass(frozen=True)
class PersistedTransformation:
    project_identity: str
    transformation_identity: str
    artifact_version_identity: str
    parser: str
    configuration: str
    outcome: str
    evidence: str


@dataclass(frozen=True)
class PersistedRepresentation:
    project_identity: str
    representation_identity: str
    artifact_version_identity: str
    provenance_identity: str
    location_reference: str
    evidence: str


@dataclass(frozen=True)
class PersistedPackageConstruction:
    project_identity: str
    record_identity: str
    request_identity: str
    package_identity: str | None
    status: str
    sufficiency: str | None
    coherence: str | None
    evidence: str

def _reject_secret(value: str) -> None:
    if any(marker in value.lower() for marker in ("secret=", "password=", "token=", "api_key=")):
        raise SecretValueError("secret values are excluded from durable state and audit")

class SQLiteStateStore:
    def __init__(self, database: Path) -> None:
        self._database = database

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self._database)
        connection.execute("PRAGMA foreign_keys = ON")
        return connection
    def initialize(self) -> None:
        """Initialize or deterministically advance the application-owned schema."""

        with self._connect() as connection:
            exists = connection.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='schema_version'"
            ).fetchone()
            if not exists:
                self._create_version_one(connection)
            version_row = connection.execute("SELECT version FROM schema_version").fetchone()
            if version_row is None or not isinstance(version_row[0], int):
                raise StateCompatibilityError("unsupported or malformed schema version")
            version = version_row[0]
            if version > CURRENT_SCHEMA_VERSION or version < 1:
                raise StateCompatibilityError("unsupported or malformed schema version")
            while version < CURRENT_SCHEMA_VERSION:
                if version == 1:
                    self._migrate_one_to_two(connection)
                    version = 2
                elif version == 2:
                    self._migrate_two_to_three(connection)
                    version = 3
                elif version == 3:
                    self._migrate_three_to_four(connection)
                    version = 4
                else:
                    raise StateCompatibilityError("unsupported or malformed schema version")

    @staticmethod
    def _create_version_one(connection: sqlite3.Connection) -> None:
        connection.execute("CREATE TABLE schema_version (version INTEGER NOT NULL)")
        connection.execute("INSERT INTO schema_version VALUES (1)")
        connection.execute(
            "CREATE TABLE evidence (row_id INTEGER PRIMARY KEY, project_identity TEXT NOT NULL, "
            "semantic_identity TEXT NOT NULL, historical_reference TEXT NOT NULL, "
            "UNIQUE(project_identity, semantic_identity))"
        )
        connection.execute(
            "CREATE TABLE audit (row_id INTEGER PRIMARY KEY, project_identity TEXT NOT NULL, "
            "outcome TEXT NOT NULL, detail TEXT NOT NULL)"
        )

    @staticmethod
    def _migrate_one_to_two(connection: sqlite3.Connection) -> None:
        connection.execute(
            "CREATE TABLE source_registration (row_id INTEGER PRIMARY KEY, "
            "project_identity TEXT NOT NULL, source_identity TEXT NOT NULL, "
            "source_type TEXT NOT NULL, scope TEXT NOT NULL, availability TEXT NOT NULL, "
            "locator TEXT, UNIQUE(project_identity, source_identity))"
        )
        connection.execute("UPDATE schema_version SET version = 2")

    @staticmethod
    def _migrate_two_to_three(connection: sqlite3.Connection) -> None:
        """Add append-only Workstream 5 evidence tables.

        SQLite row IDs remain private implementation details.  Caller supplied
        semantic identities and explicit Project association form every public
        lookup key; reload never asserts currentness or Authority.
        """
        connection.execute(
            "CREATE TABLE source_observation (row_id INTEGER PRIMARY KEY, "
            "project_identity TEXT NOT NULL, observation_identity TEXT NOT NULL, "
            "source_identity TEXT NOT NULL, observed_at TEXT NOT NULL, outcome TEXT NOT NULL, "
            "evidence TEXT NOT NULL, UNIQUE(project_identity, observation_identity))"
        )
        connection.execute(
            "CREATE TABLE artifact_evidence (row_id INTEGER PRIMARY KEY, "
            "project_identity TEXT NOT NULL, artifact_identity TEXT NOT NULL, "
            "artifact_version_identity TEXT NOT NULL, source_identity TEXT NOT NULL, "
            "locator TEXT NOT NULL, original_content TEXT NOT NULL, observation_identity TEXT NOT NULL, "
            "UNIQUE(project_identity, artifact_version_identity))"
        )
        connection.execute(
            "CREATE TABLE transformation_evidence (row_id INTEGER PRIMARY KEY, "
            "project_identity TEXT NOT NULL, transformation_identity TEXT NOT NULL, "
            "artifact_version_identity TEXT NOT NULL, parser TEXT NOT NULL, configuration TEXT NOT NULL, "
            "outcome TEXT NOT NULL, evidence TEXT NOT NULL, "
            "UNIQUE(project_identity, transformation_identity))"
        )
        connection.execute(
            "CREATE TABLE representation_evidence (row_id INTEGER PRIMARY KEY, "
            "project_identity TEXT NOT NULL, representation_identity TEXT NOT NULL, "
            "artifact_version_identity TEXT NOT NULL, provenance_identity TEXT NOT NULL, "
            "location_reference TEXT NOT NULL, evidence TEXT NOT NULL, "
            "UNIQUE(project_identity, representation_identity))"
        )
        connection.execute("UPDATE schema_version SET version = 3")

    @staticmethod
    def _migrate_three_to_four(connection: sqlite3.Connection) -> None:
        """Add Project-scoped historical package-construction evidence.

        This table records a construction attempt, not Consumer rendering,
        delivery, receipt, use, Authority, or currentness.
        """
        connection.execute(
            "CREATE TABLE package_construction (row_id INTEGER PRIMARY KEY, "
            "project_identity TEXT NOT NULL, record_identity TEXT NOT NULL, request_identity TEXT NOT NULL, "
            "package_identity TEXT, status TEXT NOT NULL, sufficiency TEXT, coherence TEXT, evidence TEXT NOT NULL, "
            "UNIQUE(project_identity, record_identity))"
        )
        connection.execute("UPDATE schema_version SET version = 4")

    def save_evidence(self, evidence: PersistedEvidence) -> None:
        _reject_secret(evidence.historical_reference)
        with self._connect() as connection:
            connection.execute("INSERT INTO evidence(project_identity, semantic_identity, historical_reference) VALUES (?, ?, ?)", (evidence.project_identity, evidence.semantic_identity, evidence.historical_reference))
    def restore_evidence(self, project_identity: str, semantic_identity: str) -> PersistedEvidence | None:
        with self._connect() as connection:
            row = connection.execute("SELECT project_identity, semantic_identity, historical_reference FROM evidence WHERE project_identity=? AND semantic_identity=?", (project_identity, semantic_identity)).fetchone()
        return PersistedEvidence(*row) if row else None

    def save_source_registration(self, registration: PersistedSourceRegistration) -> None:
        """Persist Project-scoped lifecycle facts in one transaction.

        The caller-supplied semantic identity is stored as data; SQLite's row id
        is deliberately not exposed by this contract.
        """

        for value in (registration.source_identity, registration.scope, registration.locator or ""):
            _reject_secret(value)
        with self._connect() as connection:
            connection.execute(
                "INSERT INTO source_registration(project_identity, source_identity, source_type, "
                "scope, availability, locator) VALUES (?, ?, ?, ?, ?, ?)",
                (
                    registration.project_identity,
                    registration.source_identity,
                    registration.source_type,
                    registration.scope,
                    registration.availability,
                    registration.locator,
                ),
            )

    def source_registrations_for_project(
        self, project_identity: str
    ) -> tuple[PersistedSourceRegistration, ...]:
        with self._connect() as connection:
            rows = connection.execute(
                "SELECT project_identity, source_identity, source_type, scope, availability, locator "
                "FROM source_registration WHERE project_identity=? ORDER BY source_identity",
                (project_identity,),
            ).fetchall()
        return tuple(PersistedSourceRegistration(*row) for row in rows)

    def write_audit(self, project_identity: str, outcome: str, detail: str) -> None:
        _reject_secret(detail)
        with self._connect() as connection:
            connection.execute("INSERT INTO audit(project_identity, outcome, detail) VALUES (?, ?, ?)", (project_identity, outcome, detail))
    def audit_for_project(self, project_identity: str, *, authorized: bool) -> tuple[tuple[str, str], ...]:
        if not authorized:
            raise PermissionError("audit access is authorization-bound")
        with self._connect() as connection:
            return tuple(
                connection.execute(
                    "SELECT outcome, detail FROM audit WHERE project_identity=?", (project_identity,)
                ).fetchall()
            )

    def save_observation(self, observation: PersistedObservation) -> None:
        self._reject_evidence_values(observation.project_identity, observation.observation_identity, observation.source_identity, observation.evidence)
        with self._connect() as connection:
            connection.execute(
                "INSERT INTO source_observation(project_identity, observation_identity, source_identity, observed_at, outcome, evidence) VALUES (?, ?, ?, ?, ?, ?)",
                (observation.project_identity, observation.observation_identity, observation.source_identity, observation.observed_at, observation.outcome, observation.evidence),
            )

    def save_artifact_evidence(self, artifact: PersistedArtifactEvidence) -> None:
        self._reject_evidence_values(artifact.project_identity, artifact.artifact_identity, artifact.artifact_version_identity, artifact.locator, artifact.original_content)
        with self._connect() as connection:
            connection.execute(
                "INSERT INTO artifact_evidence(project_identity, artifact_identity, artifact_version_identity, source_identity, locator, original_content, observation_identity) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (artifact.project_identity, artifact.artifact_identity, artifact.artifact_version_identity, artifact.source_identity, artifact.locator, artifact.original_content, artifact.observation_identity),
            )

    def save_transformation(self, transformation: PersistedTransformation) -> None:
        self._reject_evidence_values(transformation.project_identity, transformation.transformation_identity, transformation.evidence)
        with self._connect() as connection:
            connection.execute(
                "INSERT INTO transformation_evidence(project_identity, transformation_identity, artifact_version_identity, parser, configuration, outcome, evidence) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (transformation.project_identity, transformation.transformation_identity, transformation.artifact_version_identity, transformation.parser, transformation.configuration, transformation.outcome, transformation.evidence),
            )

    def save_representation(self, representation: PersistedRepresentation) -> None:
        self._reject_evidence_values(representation.project_identity, representation.representation_identity, representation.evidence)
        with self._connect() as connection:
            connection.execute(
                "INSERT INTO representation_evidence(project_identity, representation_identity, artifact_version_identity, provenance_identity, location_reference, evidence) VALUES (?, ?, ?, ?, ?, ?)",
                (representation.project_identity, representation.representation_identity, representation.artifact_version_identity, representation.provenance_identity, representation.location_reference, representation.evidence),
            )

    def save_package_construction(self, record: PersistedPackageConstruction) -> None:
        self._reject_evidence_values(record.project_identity, record.record_identity, record.request_identity, record.evidence)
        with self._connect() as connection:
            connection.execute(
                "INSERT INTO package_construction(project_identity, record_identity, request_identity, package_identity, status, sufficiency, coherence, evidence) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (record.project_identity, record.record_identity, record.request_identity, record.package_identity, record.status, record.sufficiency, record.coherence, record.evidence),
            )

    @staticmethod
    def _reject_evidence_values(*values: str) -> None:
        for value in values:
            _reject_secret(value)

    def observations_for_project(self, project_identity: str) -> tuple[PersistedObservation, ...]:
        with self._connect() as connection:
            rows = connection.execute("SELECT project_identity, observation_identity, source_identity, observed_at, outcome, evidence FROM source_observation WHERE project_identity=? ORDER BY observation_identity", (project_identity,)).fetchall()
        return tuple(PersistedObservation(*row) for row in rows)

    def artifact_evidence_for_project(self, project_identity: str) -> tuple[PersistedArtifactEvidence, ...]:
        with self._connect() as connection:
            rows = connection.execute("SELECT project_identity, artifact_identity, artifact_version_identity, source_identity, locator, original_content, observation_identity FROM artifact_evidence WHERE project_identity=? ORDER BY artifact_version_identity", (project_identity,)).fetchall()
        return tuple(PersistedArtifactEvidence(*row) for row in rows)

    def transformations_for_project(self, project_identity: str) -> tuple[PersistedTransformation, ...]:
        with self._connect() as connection:
            rows = connection.execute("SELECT project_identity, transformation_identity, artifact_version_identity, parser, configuration, outcome, evidence FROM transformation_evidence WHERE project_identity=? ORDER BY transformation_identity", (project_identity,)).fetchall()
        return tuple(PersistedTransformation(*row) for row in rows)

    def representations_for_project(self, project_identity: str) -> tuple[PersistedRepresentation, ...]:
        with self._connect() as connection:
            rows = connection.execute("SELECT project_identity, representation_identity, artifact_version_identity, provenance_identity, location_reference, evidence FROM representation_evidence WHERE project_identity=? ORDER BY representation_identity", (project_identity,)).fetchall()
        return tuple(PersistedRepresentation(*row) for row in rows)

    def package_constructions_for_project(self, project_identity: str) -> tuple[PersistedPackageConstruction, ...]:
        with self._connect() as connection:
            rows = connection.execute("SELECT project_identity, record_identity, request_identity, package_identity, status, sufficiency, coherence, evidence FROM package_construction WHERE project_identity=? ORDER BY record_identity", (project_identity,)).fetchall()
        return tuple(PersistedPackageConstruction(*row) for row in rows)
