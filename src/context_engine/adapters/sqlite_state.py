"""Narrow SQLite EB-03 adapter; rows never define semantic identity."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import sqlite3

class StateCompatibilityError(RuntimeError):
    """Raised when an application-owned schema cannot be safely used."""


class SecretValueError(ValueError):
    """Raised when a normal state/audit value resembles a secret."""


CURRENT_SCHEMA_VERSION = 2

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
                "FROM source_registration WHERE project_identity=? ORDER BY row_id",
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
