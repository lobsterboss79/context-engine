"""Narrow SQLite EB-03 adapter; rows never define semantic identity."""
from __future__ import annotations
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import UTC, datetime
import hashlib
import json
from pathlib import Path
import os
import sqlite3
import tempfile
import uuid

from context_engine.application.semantic_lifecycle import SemanticRecordLifecycleKind

class StateCompatibilityError(RuntimeError):
    """Raised when an application-owned schema cannot be safely used."""


class SecretValueError(ValueError):
    """Raised when a normal state/audit value resembles a secret."""


class BackupValidationError(RuntimeError):
    """Raised when a supplied backup is not a safe Context Engine backup."""


class RestoreError(RuntimeError):
    """Raised when controlled recovery cannot safely replace its target."""


CURRENT_SCHEMA_VERSION = 7

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
class PersistedSemanticRecord:
    project_identity: str
    record_identity: str
    version: str
    record_sha256: str
    claim_identity: str
    source_identity: str
    artifact_locator: str
    source_revision: str
    source_sha256: str
    observation_identity: str
    location_reference: str
    evidence: str


@dataclass(frozen=True)
class PersistedSemanticRecordSupersession:
    """One immutable, Project-scoped semantic-record lifecycle edge."""

    project_identity: str
    relation_identity: str
    version: str
    relation_sha256: str
    predecessor_record_identity: str
    predecessor_version: str
    predecessor_record_sha256: str
    successor_record_identity: str
    successor_version: str
    successor_record_sha256: str
    kind: str
    creation_basis: str
    evidence: str


def semantic_record_supersession_sha256(record: PersistedSemanticRecordSupersession) -> str:
    """Return the deterministic hash of immutable lifecycle relation content."""
    payload = {
        key: value for key, value in record.__dict__.items()
        if key != "relation_sha256"
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


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


@dataclass(frozen=True)
class BackupMetadata:
    """Non-governing evidence carried with one SQLite-consistent backup."""

    backup_identity: str
    created_at: str
    purpose: str
    retention_basis: str
    schema_version: int


@dataclass(frozen=True)
class RecoveryQualification:
    """Qualification applied to a database obtained through restore."""

    backup_identity: str
    restored_at: str
    qualification: str = "historical-only; currentness, Authority, Governance State, and present authorization require independent re-establishment"

def _reject_secret(value: str) -> None:
    if any(marker in value.lower() for marker in ("secret=", "password=", "token=", "api_key=")):
        raise SecretValueError("secret values are excluded from durable state and audit")


@contextmanager
def _managed_sqlite_connection(database: str | Path, *, uri: bool = False) -> Iterator[sqlite3.Connection]:
    """Commit or roll back one adapter-owned connection, then always release it."""
    connection = sqlite3.connect(database, uri=uri)
    try:
        with connection:
            yield connection
    finally:
        connection.close()


class SQLiteStateStore:
    def __init__(self, database: Path) -> None:
        self._database = database

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self._database)
        connection.execute("PRAGMA foreign_keys = ON")
        return connection

    @contextmanager
    def _connection(self) -> Iterator[sqlite3.Connection]:
        """Manage one operational connection without extending its native handle lifetime."""
        connection = self._connect()
        try:
            with connection:
                yield connection
        finally:
            connection.close()

    def initialize(self) -> None:
        """Initialize or deterministically advance the application-owned schema."""

        with self._connection() as connection:
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
                elif version == 4:
                    self._migrate_four_to_five(connection)
                    version = 5
                elif version == 5:
                    self._migrate_five_to_six(connection)
                    version = 6
                elif version == 6:
                    self._migrate_six_to_seven(connection)
                    version = 7
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

    @staticmethod
    def _migrate_four_to_five(connection: sqlite3.Connection) -> None:
        """Add only local recovery qualification state.

        A row is written only after a validated backup has been restored into a
        staged database.  It qualifies the restored deployment; it does not
        revise historic evidence or grant any present-tense semantic status.
        """
        connection.execute(
            "CREATE TABLE recovery_qualification (row_id INTEGER PRIMARY KEY, "
            "backup_identity TEXT NOT NULL, restored_at TEXT NOT NULL, qualification TEXT NOT NULL)"
        )
        connection.execute("UPDATE schema_version SET version = 5")

    @staticmethod
    def _migrate_five_to_six(connection: sqlite3.Connection) -> None:
        connection.execute(
            "CREATE TABLE semantic_record_evidence (row_id INTEGER PRIMARY KEY, "
            "project_identity TEXT NOT NULL, record_identity TEXT NOT NULL, version TEXT NOT NULL, "
            "record_sha256 TEXT NOT NULL, claim_identity TEXT NOT NULL, source_identity TEXT NOT NULL, "
            "artifact_locator TEXT NOT NULL, source_revision TEXT NOT NULL, source_sha256 TEXT NOT NULL, "
            "observation_identity TEXT NOT NULL, location_reference TEXT NOT NULL, evidence TEXT NOT NULL, "
            "UNIQUE(project_identity, record_identity, version, record_sha256))"
        )
        connection.execute("UPDATE schema_version SET version = 6")

    @staticmethod
    def _migrate_six_to_seven(connection: sqlite3.Connection) -> None:
        """Add immutable semantic-record predecessor/successor evidence only."""
        connection.execute(
            "CREATE TABLE semantic_record_supersession (row_id INTEGER PRIMARY KEY, "
            "project_identity TEXT NOT NULL, relation_identity TEXT NOT NULL, version TEXT NOT NULL, "
            "relation_sha256 TEXT NOT NULL, predecessor_record_identity TEXT NOT NULL, "
            "predecessor_version TEXT NOT NULL, predecessor_record_sha256 TEXT NOT NULL, "
            "successor_record_identity TEXT NOT NULL, successor_version TEXT NOT NULL, "
            "successor_record_sha256 TEXT NOT NULL, kind TEXT NOT NULL, creation_basis TEXT NOT NULL, "
            "evidence TEXT NOT NULL, "
            "UNIQUE(project_identity, relation_identity, version), "
            "UNIQUE(project_identity, relation_identity, version, relation_sha256), "
            "UNIQUE(project_identity, predecessor_record_identity, predecessor_version, predecessor_record_sha256), "
            "UNIQUE(project_identity, successor_record_identity, successor_version, successor_record_sha256), "
            "FOREIGN KEY(project_identity, predecessor_record_identity, predecessor_version, predecessor_record_sha256) "
            "REFERENCES semantic_record_evidence(project_identity, record_identity, version, record_sha256), "
            "FOREIGN KEY(project_identity, successor_record_identity, successor_version, successor_record_sha256) "
            "REFERENCES semantic_record_evidence(project_identity, record_identity, version, record_sha256))"
        )
        connection.execute("UPDATE schema_version SET version = 7")

    def save_evidence(self, evidence: PersistedEvidence) -> None:
        _reject_secret(evidence.historical_reference)
        with self._connection() as connection:
            connection.execute("INSERT INTO evidence(project_identity, semantic_identity, historical_reference) VALUES (?, ?, ?)", (evidence.project_identity, evidence.semantic_identity, evidence.historical_reference))
    def restore_evidence(self, project_identity: str, semantic_identity: str) -> PersistedEvidence | None:
        with self._connection() as connection:
            row = connection.execute("SELECT project_identity, semantic_identity, historical_reference FROM evidence WHERE project_identity=? AND semantic_identity=?", (project_identity, semantic_identity)).fetchone()
        return PersistedEvidence(*row) if row else None

    def save_source_registration(self, registration: PersistedSourceRegistration) -> None:
        """Persist Project-scoped lifecycle facts in one transaction.

        The caller-supplied semantic identity is stored as data; SQLite's row id
        is deliberately not exposed by this contract.
        """

        for value in (registration.source_identity, registration.scope, registration.locator or ""):
            _reject_secret(value)
        with self._connection() as connection:
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
        with self._connection() as connection:
            rows = connection.execute(
                "SELECT project_identity, source_identity, source_type, scope, availability, locator "
                "FROM source_registration WHERE project_identity=? ORDER BY source_identity",
                (project_identity,),
            ).fetchall()
        return tuple(PersistedSourceRegistration(*row) for row in rows)

    def write_audit(self, project_identity: str, outcome: str, detail: str) -> None:
        _reject_secret(detail)
        with self._connection() as connection:
            connection.execute("INSERT INTO audit(project_identity, outcome, detail) VALUES (?, ?, ?)", (project_identity, outcome, detail))
    def audit_for_project(self, project_identity: str, *, authorized: bool) -> tuple[tuple[str, str], ...]:
        if not authorized:
            raise PermissionError("audit access is authorization-bound")
        with self._connection() as connection:
            return tuple(
                connection.execute(
                    "SELECT outcome, detail FROM audit WHERE project_identity=?", (project_identity,)
                ).fetchall()
            )

    def save_observation(self, observation: PersistedObservation) -> None:
        self._reject_evidence_values(observation.project_identity, observation.observation_identity, observation.source_identity, observation.evidence)
        with self._connection() as connection:
            connection.execute(
                "INSERT INTO source_observation(project_identity, observation_identity, source_identity, observed_at, outcome, evidence) VALUES (?, ?, ?, ?, ?, ?)",
                (observation.project_identity, observation.observation_identity, observation.source_identity, observation.observed_at, observation.outcome, observation.evidence),
            )

    def save_artifact_evidence(self, artifact: PersistedArtifactEvidence) -> None:
        self._reject_evidence_values(artifact.project_identity, artifact.artifact_identity, artifact.artifact_version_identity, artifact.locator, artifact.original_content)
        with self._connection() as connection:
            connection.execute(
                "INSERT INTO artifact_evidence(project_identity, artifact_identity, artifact_version_identity, source_identity, locator, original_content, observation_identity) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (artifact.project_identity, artifact.artifact_identity, artifact.artifact_version_identity, artifact.source_identity, artifact.locator, artifact.original_content, artifact.observation_identity),
            )

    def save_transformation(self, transformation: PersistedTransformation) -> None:
        self._reject_evidence_values(transformation.project_identity, transformation.transformation_identity, transformation.evidence)
        with self._connection() as connection:
            connection.execute(
                "INSERT INTO transformation_evidence(project_identity, transformation_identity, artifact_version_identity, parser, configuration, outcome, evidence) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (transformation.project_identity, transformation.transformation_identity, transformation.artifact_version_identity, transformation.parser, transformation.configuration, transformation.outcome, transformation.evidence),
            )

    def save_representation(self, representation: PersistedRepresentation) -> None:
        self._reject_evidence_values(representation.project_identity, representation.representation_identity, representation.evidence)
        with self._connection() as connection:
            connection.execute(
                "INSERT INTO representation_evidence(project_identity, representation_identity, artifact_version_identity, provenance_identity, location_reference, evidence) VALUES (?, ?, ?, ?, ?, ?)",
                (representation.project_identity, representation.representation_identity, representation.artifact_version_identity, representation.provenance_identity, representation.location_reference, representation.evidence),
            )

    def save_package_construction(self, record: PersistedPackageConstruction) -> None:
        self._reject_evidence_values(record.project_identity, record.record_identity, record.request_identity, record.evidence)
        with self._connection() as connection:
            connection.execute(
                "INSERT INTO package_construction(project_identity, record_identity, request_identity, package_identity, status, sufficiency, coherence, evidence) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (record.project_identity, record.record_identity, record.request_identity, record.package_identity, record.status, record.sufficiency, record.coherence, record.evidence),
            )

    @staticmethod
    def _reject_evidence_values(*values: str) -> None:
        for value in values:
            _reject_secret(value)

    def observations_for_project(self, project_identity: str) -> tuple[PersistedObservation, ...]:
        with self._connection() as connection:
            rows = connection.execute("SELECT project_identity, observation_identity, source_identity, observed_at, outcome, evidence FROM source_observation WHERE project_identity=? ORDER BY observation_identity", (project_identity,)).fetchall()
        return tuple(PersistedObservation(*row) for row in rows)

    def artifact_evidence_for_project(self, project_identity: str) -> tuple[PersistedArtifactEvidence, ...]:
        with self._connection() as connection:
            rows = connection.execute("SELECT project_identity, artifact_identity, artifact_version_identity, source_identity, locator, original_content, observation_identity FROM artifact_evidence WHERE project_identity=? ORDER BY artifact_version_identity", (project_identity,)).fetchall()
        return tuple(PersistedArtifactEvidence(*row) for row in rows)

    def transformations_for_project(self, project_identity: str) -> tuple[PersistedTransformation, ...]:
        with self._connection() as connection:
            rows = connection.execute("SELECT project_identity, transformation_identity, artifact_version_identity, parser, configuration, outcome, evidence FROM transformation_evidence WHERE project_identity=? ORDER BY transformation_identity", (project_identity,)).fetchall()
        return tuple(PersistedTransformation(*row) for row in rows)

    def representations_for_project(self, project_identity: str) -> tuple[PersistedRepresentation, ...]:
        with self._connection() as connection:
            rows = connection.execute("SELECT project_identity, representation_identity, artifact_version_identity, provenance_identity, location_reference, evidence FROM representation_evidence WHERE project_identity=? ORDER BY representation_identity", (project_identity,)).fetchall()
        return tuple(PersistedRepresentation(*row) for row in rows)

    def save_semantic_record(self, record: PersistedSemanticRecord) -> None:
        self._validate_semantic_record(record)
        with self._connection() as connection:
            self._save_semantic_record(connection, record)

    @staticmethod
    def _is_sha256(value: str) -> bool:
        return len(value) == 64 and all(character in "0123456789abcdef" for character in value)

    def _validate_semantic_record(self, record: PersistedSemanticRecord) -> None:
        self._reject_evidence_values(
            record.project_identity, record.record_identity, record.version,
            record.claim_identity, record.evidence,
        )
        if not self._is_sha256(record.record_sha256) or not self._is_sha256(record.source_sha256):
            raise ValueError("semantic-record hashes must be lowercase SHA-256 values")

    def _save_semantic_record(self, connection: sqlite3.Connection, record: PersistedSemanticRecord) -> None:
        conflict = connection.execute(
            "SELECT record_sha256 FROM semantic_record_evidence "
            "WHERE project_identity=? AND record_identity=? AND version=?",
            (record.project_identity, record.record_identity, record.version),
        ).fetchone()
        if conflict is not None and conflict[0] != record.record_sha256:
            raise ValueError("semantic-record identity/version hash conflict")
        connection.execute(
            "INSERT OR IGNORE INTO semantic_record_evidence "
            "(project_identity, record_identity, version, record_sha256, claim_identity, source_identity, artifact_locator, source_revision, source_sha256, observation_identity, location_reference, evidence) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", tuple(record.__dict__.values())
        )

    def semantic_records_for_project(self, project_identity: str) -> tuple[PersistedSemanticRecord, ...]:
        with self._connection() as connection:
            rows = connection.execute(
                "SELECT project_identity, record_identity, version, record_sha256, claim_identity, source_identity, artifact_locator, source_revision, source_sha256, observation_identity, location_reference, evidence "
                "FROM semantic_record_evidence WHERE project_identity = ? ORDER BY record_identity, version, record_sha256", (project_identity,)
            ).fetchall()
        return tuple(PersistedSemanticRecord(*row) for row in rows)

    def save_semantic_record_successor(
        self, successor: PersistedSemanticRecord, relation: PersistedSemanticRecordSupersession
    ) -> None:
        """Atomically persist one validated successor and its immutable edge."""
        self._validate_semantic_record(successor)
        self._validate_semantic_record_supersession(relation)
        if (
            relation.project_identity != successor.project_identity
            or (relation.successor_record_identity, relation.successor_version, relation.successor_record_sha256)
            != (successor.record_identity, successor.version, successor.record_sha256)
        ):
            raise ValueError("semantic-record successor relation does not name supplied successor")
        with self._connection() as connection:
            predecessor = connection.execute(
                "SELECT project_identity, record_identity, version, record_sha256, claim_identity, source_identity, artifact_locator, source_revision, source_sha256, observation_identity, location_reference, evidence "
                "FROM semantic_record_evidence WHERE project_identity=? AND record_identity=? AND version=? AND record_sha256=?",
                (relation.project_identity, relation.predecessor_record_identity, relation.predecessor_version, relation.predecessor_record_sha256),
            ).fetchone()
            if predecessor is None:
                raise ValueError("semantic-record successor predecessor is missing")
            self._validate_persisted_successor(PersistedSemanticRecord(*predecessor), successor, relation.kind)
            existing = connection.execute(
                "SELECT relation_sha256 FROM semantic_record_supersession "
                "WHERE project_identity=? AND relation_identity=? AND version=?",
                (relation.project_identity, relation.relation_identity, relation.version),
            ).fetchone()
            if existing is not None:
                if existing[0] != relation.relation_sha256:
                    raise ValueError("semantic-record lifecycle relation identity/version hash conflict")
                return
            self._save_semantic_record(connection, successor)
            try:
                connection.execute(
                    "INSERT INTO semantic_record_supersession "
                    "(project_identity, relation_identity, version, relation_sha256, predecessor_record_identity, predecessor_version, predecessor_record_sha256, successor_record_identity, successor_version, successor_record_sha256, kind, creation_basis, evidence) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    tuple(relation.__dict__.values()),
                )
            except sqlite3.IntegrityError as error:
                raise ValueError("semantic-record lifecycle relation conflicts or has invalid endpoints") from error

    def _validate_semantic_record_supersession(self, relation: PersistedSemanticRecordSupersession) -> None:
        self._reject_evidence_values(relation.project_identity, relation.relation_identity, relation.version, relation.creation_basis, relation.evidence)
        if not self._is_sha256(relation.relation_sha256) or not self._is_sha256(relation.predecessor_record_sha256) or not self._is_sha256(relation.successor_record_sha256):
            raise ValueError("semantic-record lifecycle hashes must be lowercase SHA-256 values")
        if relation.relation_sha256 != semantic_record_supersession_sha256(relation):
            raise ValueError("semantic-record lifecycle relation hash mismatch")
        try:
            SemanticRecordLifecycleKind(relation.kind)
        except ValueError as error:
            raise ValueError("semantic-record lifecycle kind is invalid") from error
        if (
            relation.predecessor_record_identity,
            relation.predecessor_version,
            relation.predecessor_record_sha256,
        ) == (
            relation.successor_record_identity,
            relation.successor_version,
            relation.successor_record_sha256,
        ):
            raise ValueError("semantic-record lifecycle cannot self-supersede")

    @staticmethod
    def _validate_persisted_successor(
        predecessor: PersistedSemanticRecord, successor: PersistedSemanticRecord, kind: str
    ) -> None:
        lifecycle_kind = SemanticRecordLifecycleKind(kind)
        if lifecycle_kind is SemanticRecordLifecycleKind.PROVENANCE_CORRECTION:
            if predecessor.claim_identity != successor.claim_identity:
                raise ValueError("provenance correction Claim identity mismatch")
            if (
                predecessor.source_identity, predecessor.artifact_locator,
                predecessor.source_revision, predecessor.source_sha256,
            ) != (
                successor.source_identity, successor.artifact_locator,
                successor.source_revision, successor.source_sha256,
            ):
                raise ValueError("provenance correction Source binding mismatch")
        elif lifecycle_kind is SemanticRecordLifecycleKind.SEMANTIC_REVISION:
            if predecessor.claim_identity == successor.claim_identity:
                raise ValueError("semantic revision requires a new Claim identity")
        elif lifecycle_kind is SemanticRecordLifecycleKind.SOURCE_REVISION_TRANSITION:
            if (
                predecessor.source_identity, predecessor.source_revision, predecessor.source_sha256,
            ) == (
                successor.source_identity, successor.source_revision, successor.source_sha256,
            ):
                raise ValueError("source revision transition requires changed Source revision/hash")

    def semantic_record_supersessions_for_project(
        self, project_identity: str
    ) -> tuple[PersistedSemanticRecordSupersession, ...]:
        with self._connection() as connection:
            rows = connection.execute(
                "SELECT project_identity, relation_identity, version, relation_sha256, predecessor_record_identity, predecessor_version, predecessor_record_sha256, successor_record_identity, successor_version, successor_record_sha256, kind, creation_basis, evidence "
                "FROM semantic_record_supersession WHERE project_identity=? "
                "ORDER BY relation_identity, version, relation_sha256", (project_identity,)
            ).fetchall()
        return tuple(PersistedSemanticRecordSupersession(*row) for row in rows)

    def active_semantic_records_for_project(self, project_identity: str) -> tuple[PersistedSemanticRecord, ...]:
        """Return only unambiguous terminal records; malformed lineage fails closed."""
        records = self.semantic_records_for_project(project_identity)
        relations = self.semantic_record_supersessions_for_project(project_identity)
        by_instance = {(row.record_identity, row.version, row.record_sha256): row for row in records}
        if len(by_instance) != len(records):
            raise ValueError("semantic-record persistence contains duplicate instances")
        logical = {(row.record_identity, row.version) for row in records}
        if len(logical) != len(records):
            raise ValueError("semantic-record persistence contains identity/version ambiguity")
        successors: dict[tuple[str, str, str], tuple[str, str, str]] = {}
        predecessors: set[tuple[str, str, str]] = set()
        for relation in relations:
            self._validate_semantic_record_supersession(relation)
            predecessor_key = (relation.predecessor_record_identity, relation.predecessor_version, relation.predecessor_record_sha256)
            successor_key = (relation.successor_record_identity, relation.successor_version, relation.successor_record_sha256)
            if predecessor_key not in by_instance or successor_key not in by_instance:
                raise ValueError("semantic-record lifecycle has missing endpoint")
            self._validate_persisted_successor(by_instance[predecessor_key], by_instance[successor_key], relation.kind)
            if predecessor_key in successors or successor_key in predecessors:
                raise ValueError("semantic-record lifecycle is ambiguous")
            successors[predecessor_key] = successor_key
            predecessors.add(successor_key)
        for origin in successors:
            seen: set[tuple[str, str, str]] = set()
            current = origin
            while current in successors:
                if current in seen:
                    raise ValueError("semantic-record lifecycle contains a cycle")
                seen.add(current)
                current = successors[current]
        active = tuple(row for key, row in sorted(by_instance.items()) if key not in successors)
        if len({row.record_identity for row in active}) != len(active):
            raise ValueError("semantic-record lifecycle has ambiguous active versions")
        return active

    def package_constructions_for_project(self, project_identity: str) -> tuple[PersistedPackageConstruction, ...]:
        with self._connection() as connection:
            rows = connection.execute("SELECT project_identity, record_identity, request_identity, package_identity, status, sufficiency, coherence, evidence FROM package_construction WHERE project_identity=? ORDER BY record_identity", (project_identity,)).fetchall()
        return tuple(PersistedPackageConstruction(*row) for row in rows)

    def create_backup(
        self,
        destination: Path,
        *,
        operator_authorized: bool,
        purpose: str,
        retention_basis: str,
        backup_identity: str | None = None,
    ) -> BackupMetadata:
        """Create one consistent SQLite backup with bounded, non-secret metadata.

        The caller deliberately supplies the destination and the governance
        purpose/retention basis.  This adapter has no scheduler, storage
        service, or authority-creation behavior.  SQLite's backup API copies a
        consistent database image; metadata is then committed in that image so
        a later restore can validate what it is handling.
        """
        if not operator_authorized:
            raise PermissionError("backup requires established operator authorization")
        if not purpose or not retention_basis:
            raise ValueError("backup requires explicit purpose and retention basis")
        if self._database.resolve() == destination.resolve():
            raise ValueError("backup destination must differ from operational state")
        if destination.exists():
            raise FileExistsError("backup destination must be a new explicit path")
        self._reject_evidence_values(purpose, retention_basis)
        destination.parent.mkdir(parents=True, exist_ok=True)
        metadata = BackupMetadata(
            backup_identity or f"backup-{uuid.uuid4()}",
            datetime.now(UTC).isoformat(), purpose, retention_basis, CURRENT_SCHEMA_VERSION,
        )
        self._reject_evidence_values(metadata.backup_identity, metadata.created_at)
        # Schema/readiness is checked before any destination is created.
        self._validate_operational_database()
        try:
            with self._connection() as source, _managed_sqlite_connection(destination) as target:
                source.backup(target)
                target.execute(
                    "CREATE TABLE context_engine_backup_metadata (backup_identity TEXT NOT NULL, "
                    "created_at TEXT NOT NULL, purpose TEXT NOT NULL, retention_basis TEXT NOT NULL, "
                    "schema_version INTEGER NOT NULL)"
                )
                target.execute(
                    "INSERT INTO context_engine_backup_metadata VALUES (?, ?, ?, ?, ?)",
                    (metadata.backup_identity, metadata.created_at, metadata.purpose,
                     metadata.retention_basis, metadata.schema_version),
                )
        except sqlite3.Error as error:
            raise RestoreError("consistent backup was not completed") from error
        self.validate_backup(destination)
        return metadata

    @staticmethod
    def _schema_version(connection: sqlite3.Connection) -> int:
        row = connection.execute("SELECT version FROM schema_version").fetchone()
        if row is None or not isinstance(row[0], int):
            raise BackupValidationError("backup has malformed schema version")
        return row[0]

    def _validate_operational_database(self) -> None:
        try:
            with self._connection() as connection:
                if connection.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
                    raise StateCompatibilityError("operational database failed integrity check")
                if self._schema_version(connection) != CURRENT_SCHEMA_VERSION:
                    raise StateCompatibilityError("operational database is not at the supported schema version")
        except sqlite3.Error as error:
            raise StateCompatibilityError("operational database is unavailable or malformed") from error

    @classmethod
    def validate_backup(cls, backup: Path) -> BackupMetadata:
        """Validate format, integrity, compatibility, and secret-safe metadata."""
        if not backup.is_file():
            raise BackupValidationError("backup is unavailable")
        try:
            with _managed_sqlite_connection(f"file:{backup}?mode=ro", uri=True) as connection:
                integrity = connection.execute("PRAGMA integrity_check").fetchone()
                if integrity is None or integrity[0] != "ok":
                    raise BackupValidationError("backup integrity check failed")
                if cls._schema_version(connection) != CURRENT_SCHEMA_VERSION:
                    raise BackupValidationError("backup schema is incompatible")
                row = connection.execute(
                    "SELECT backup_identity, created_at, purpose, retention_basis, schema_version "
                    "FROM context_engine_backup_metadata"
                ).fetchone()
                count = connection.execute("SELECT COUNT(*) FROM context_engine_backup_metadata").fetchone()[0]
        except BackupValidationError:
            raise
        except sqlite3.Error as error:
            raise BackupValidationError("backup is malformed or incomplete") from error
        if row is None or count != 1:
            raise BackupValidationError("backup metadata is missing or ambiguous")
        metadata = BackupMetadata(*row)
        if metadata.schema_version != CURRENT_SCHEMA_VERSION:
            raise BackupValidationError("backup metadata schema is incompatible")
        try:
            _reject_secret(metadata.backup_identity)
            _reject_secret(metadata.created_at)
            _reject_secret(metadata.purpose)
            _reject_secret(metadata.retention_basis)
        except SecretValueError as error:
            raise BackupValidationError("backup metadata contains excluded secret-like content") from error
        return metadata

    def restore_backup(self, backup: Path, *, operator_authorized: bool) -> RecoveryQualification:
        """Validate then atomically replace state from a backup in the same directory.

        The valid target is untouched until the staged copy has passed SQLite
        validation and received its recovery qualification.  This intentionally
        restores history only: it is not a restart of present authorization,
        Authority, Governance State, or currentness.
        """
        if not operator_authorized:
            raise PermissionError("restore requires established operator authorization")
        metadata = self.validate_backup(backup)
        self._database.parent.mkdir(parents=True, exist_ok=True)
        descriptor, staging_name = tempfile.mkstemp(prefix=".context-engine-restore-", suffix=".sqlite", dir=self._database.parent)
        os.close(descriptor)
        staging = Path(staging_name)
        qualification = RecoveryQualification(metadata.backup_identity, datetime.now(UTC).isoformat())
        try:
            with _managed_sqlite_connection(f"file:{backup}?mode=ro", uri=True) as source, _managed_sqlite_connection(staging) as target:
                source.backup(target)
                target.execute(
                    "INSERT INTO recovery_qualification(backup_identity, restored_at, qualification) VALUES (?, ?, ?)",
                    (qualification.backup_identity, qualification.restored_at, qualification.qualification),
                )
            self.validate_backup(staging)
            with _managed_sqlite_connection(staging) as check:
                if check.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
                    raise BackupValidationError("staged restore integrity check failed")
            os.replace(staging, self._database)
        except (sqlite3.Error, OSError, BackupValidationError) as error:
            staging.unlink(missing_ok=True)
            raise RestoreError("restore failed before operational state was replaced") from error
        return qualification

    def recovery_qualification(self) -> RecoveryQualification | None:
        """Return the latest restore qualification without claiming currentness."""
        try:
            with self._connection() as connection:
                row = connection.execute(
                    "SELECT backup_identity, restored_at, qualification FROM recovery_qualification "
                    "ORDER BY row_id DESC LIMIT 1"
                ).fetchone()
        except sqlite3.OperationalError:
            return None
        return RecoveryQualification(*row) if row else None
