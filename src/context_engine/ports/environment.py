"""Port for observing non-governed process prerequisites."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class PrerequisiteCheck:
    """A safe, non-governed observation of one runtime prerequisite."""

    name: str
    available: bool
    detail: str


class PrerequisiteProbe(Protocol):
    """Abstract host observation boundary; no host mechanism enters the core."""

    def checks(self) -> tuple[PrerequisiteCheck, ...]:
        """Return deterministic prerequisite observations for this invocation."""
