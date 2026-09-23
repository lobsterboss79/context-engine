"""Narrow SQLite EB-03 adapter; rows never define semantic identity."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import sqlite3

class StateCompatibilityError(RuntimeError): pass
class SecretValueError(ValueError): pass
CURRENT_SCHEMA_VERSION = 1

@dataclass(frozen=True)
class PersistedEvidence:
    project_identity: str
    semantic_identity: str
    historical_reference: str
    currentness: str = "unknown"
    authority_basis: str | None = None

def _reject_secret(value: str) -> None:
    if any(marker in value.lower() for marker in ("secret=", "password=", "token=", "api_key=")):
        raise SecretValueError("secret values are excluded from durable state and audit")

class SQLiteStateStore:
    def __init__(self, database: Path) -> None: self._database = database
    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self._database)
        connection.execute("PRAGMA foreign_keys = ON")
        return connection
    def initialize(self) -> None:
        with self._connect() as connection:
            exists = connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='schema_version'").fetchone()
            if not exists:
                connection.execute("CREATE TABLE schema_version (version INTEGER NOT NULL)")
                connection.execute("INSERT INTO schema_version VALUES (1)")
                connection.execute("CREATE TABLE evidence (row_id INTEGER PRIMARY KEY, project_identity TEXT NOT NULL, semantic_identity TEXT NOT NULL, historical_reference TEXT NOT NULL, UNIQUE(project_identity, semantic_identity))")
                connection.execute("CREATE TABLE audit (row_id INTEGER PRIMARY KEY, project_identity TEXT NOT NULL, outcome TEXT NOT NULL, detail TEXT NOT NULL)")
            version = connection.execute("SELECT version FROM schema_version").fetchone()
            if version is None or version[0] != CURRENT_SCHEMA_VERSION:
                raise StateCompatibilityError("unsupported or malformed schema version")
    def save_evidence(self, evidence: PersistedEvidence) -> None:
        _reject_secret(evidence.historical_reference)
        with self._connect() as connection:
            connection.execute("INSERT INTO evidence(project_identity, semantic_identity, historical_reference) VALUES (?, ?, ?)", (evidence.project_identity, evidence.semantic_identity, evidence.historical_reference))
    def restore_evidence(self, project_identity: str, semantic_identity: str) -> PersistedEvidence | None:
        with self._connect() as connection:
            row = connection.execute("SELECT project_identity, semantic_identity, historical_reference FROM evidence WHERE project_identity=? AND semantic_identity=?", (project_identity, semantic_identity)).fetchone()
        return PersistedEvidence(*row) if row else None
    def write_audit(self, project_identity: str, outcome: str, detail: str) -> None:
        _reject_secret(detail)
        with self._connect() as connection:
            connection.execute("INSERT INTO audit(project_identity, outcome, detail) VALUES (?, ?, ?)", (project_identity, outcome, detail))
    def audit_for_project(self, project_identity: str, *, authorized: bool) -> tuple[tuple[str, str], ...]:
        if not authorized: raise PermissionError("audit access is authorization-bound")
        with self._connect() as connection:
            return tuple(connection.execute("SELECT outcome, detail FROM audit WHERE project_identity=?", (project_identity,)).fetchall())
