"""Execution-only procedure for frozen FX-F6-J v1 / ER-F6-J v1."""
from __future__ import annotations

from dataclasses import asdict, is_dataclass
from datetime import UTC, datetime
from enum import Enum
import json
from pathlib import Path
import platform
import sys

import markdown_it

from context_engine.adapters.git_source import LocalGitSourceAdapter
from context_engine.adapters.sqlite_state import SQLiteStateStore
from context_engine.application.lifecycle import ApplicableSourceUniverse, Availability, BoundaryAdequacy, RegisteredSource
from context_engine.application.orchestration import GovernedRenderInputs, run_governed_render
from context_engine.application.package_construction import CoherenceInputs
from context_engine.application.rendering import ConsumerContract, ConsumerKind, render_package
from context_engine.application.representation import observe_markdown_artifact
from context_engine.application.sufficiency import RequiredDeficiency
from context_engine.core.model import Consumer, ConsumerId, ContextRequest, EpistemicState, Requester, RequesterId, SemanticIdentity, TaskIntent, TaskScope, Uncertainty


ROOT = Path.cwd()
FIXTURE = ROOT / "docs/phase-4/ws2-item-2.6-fixtures/F6-J"
OUT = ROOT / "docs/phase-4/validation-evidence/VE-F6-J-001/raw"


def ident(kind: str, value: str) -> SemanticIdentity:
    return SemanticIdentity(kind, value)


def normalize(value):
    if isinstance(value, Enum): return value.value
    if isinstance(value, Path): return str(value)
    if is_dataclass(value): return {key: normalize(item) for key, item in asdict(value).items()}
    if isinstance(value, tuple): return [normalize(item) for item in value]
    if isinstance(value, list): return [normalize(item) for item in value]
    if isinstance(value, dict): return {str(key): normalize(item) for key, item in value.items()}
    return value


def main() -> None:
    request = ContextRequest(ident("request", "REQ-F6J-LANTERN-REVIEW-STATUS"), ident("project", "fixture-lantern-f6j"), Requester(RequesterId(ident("requester", "fixture-requester"))), Consumer(ConsumerId(ident("consumer", "fixture-human"))), TaskIntent("Prepare the particular synthetic Lantern review-status statement that exists only inside the governed Required PDF Artifact."), TaskScope("lantern/governed-review/current"))
    source = RegisteredSource("SRC-F6J-LANTERN-REVIEW-REPOSITORY", "fixture-lantern-f6j", "git", "lantern/governed-review/current", Availability.AVAILABLE, str(ROOT))
    basis = "For REQ-F6J-LANTERN-REVIEW-STATUS, the complete governed applicable Source universe is exactly SRC-F6J-LANTERN-REVIEW-REPOSITORY. That local Source and its Artifact ART-F6J-LANTERN-REVIEW-STATUS-PDF are registered, governed in scope, available, accessible, and requester-authorized. The governed boundary is adequate as a Source universe; the Required Artifact's PDF capability limitation is separately preserved and does not establish another Source or ASU gap."
    universe = ApplicableSourceUniverse(request.identity.value, (source,), BoundaryAdequacy.ADEQUATE, basis)
    git_observation = LocalGitSourceAdapter().observe(source, inspection_authorized=True)
    if git_observation.outcome not in {"observed", "partial"}:
        raise RuntimeError("registered Source observation did not establish local Source availability")
    artifact_observation = observe_markdown_artifact(FIXTURE, "sources/lantern-review-status.pdf")
    if artifact_observation.outcome != "failed" or not artifact_observation.limitations or "unsupported-artifact-type" not in artifact_observation.limitations[0].detail:
        raise RuntimeError("existing v0.1 Artifact capability check did not produce its unsupported PDF outcome")
    if artifact_observation.original_markdown is not None:
        raise RuntimeError("unsupported Artifact content was unexpectedly observed")
    limitation = Uncertainty(EpistemicState.UNKNOWN, evidence_boundary=basis, detail="DEF-F6J-REQUIRED-PDF-CAPABILITY: Required information need remains unmet. ART-F6J-LANTERN-REVIEW-STATUS-PDF belongs to available, accessible, requester-authorized, supported, governed-in-scope Source SRC-F6J-LANTERN-REVIEW-REPOSITORY; Artifact format=pdf is unsupported by the approved v0.1 Artifact capability. Zero Artifact-derived represented information and zero Artifact-derived Candidate Context exist. This is not Source unavailability, inaccessibility, unauthorized status, absence, or unsupported Source state.")
    deficiency = RequiredDeficiency(ident("deficiency", "DEF-F6J-REQUIRED-PDF-CAPABILITY"), "The task materially depends on the Required PDF Artifact content; no Supporting substitute or separately safe bounded task exists.", can_proceed_bounded_without=False, limitation=limitation)
    store = SQLiteStateStore(OUT / "f6-j-state.sqlite")
    store.initialize()
    inputs = GovernedRenderInputs(FIXTURE / "bootstrap.toml", FIXTURE / "project.toml", True, request, universe, (), (), (), (), "No Candidate Context was formed because the sole Required PDF Artifact failed the existing capability check before content observation.", (deficiency,), False, False, False, ident("package", "PKG-F6J-LANTERN-REVIEW-STATUS"), ident("record", "PCR-F6J-LANTERN-REVIEW-STATUS"), "Source registration, availability, accessibility, and requester authorization were established. The Required PDF Artifact reached unsupported-artifact-type before content parsing; no Artifact content was observed, transformed, represented, or used to form a Candidate. Required deficiency remains; no bounded substitute exists.", ConsumerContract(ConsumerKind.HUMAN, request.consumer, True), coherence_inputs=CoherenceInputs(understood_qualified_state=True, basis="The adequate ASU and Source state, unsupported Required Artifact capability, explicit Required deficiency, zero Artifact-derived representation/Candidates, Insufficient sufficiency, and retained limitation are internally consistent."), construction_qualifications=(limitation,))
    outcome = run_governed_render(inputs, store=store)
    package = outcome.construction.package
    if package is None:
        raise RuntimeError("logical package construction was denied unexpectedly")
    renderings = {"human": outcome.rendering}
    for kind, name in ((ConsumerKind.CHATGPT, "fixture-chatgpt"), (ConsumerKind.CODEX, "fixture-codex")):
        renderings[kind.value] = render_package(package, ConsumerContract(kind, Consumer(ConsumerId(ident("consumer", name))), True))
    for kind, rendering in renderings.items():
        (OUT / f"rendering-{kind}.md").write_text(rendering.content or "", encoding="utf-8")
    result = {"evidence_id": "VE-F6-J-001", "fixture": "FX-F6-J v1", "expected_result": "ER-F6-J v1", "execution_utc": datetime.now(UTC).isoformat(), "environment": {"python": sys.version, "platform": platform.platform(), "markdown_it": markdown_it.__version__}, "source_state": {"identity": source.identity, "availability": source.availability, "accessible": True, "requester_authorized": True, "supported": True, "governed_in_scope": True, "git_observation": git_observation}, "artifact": {"identity": "ART-F6J-LANTERN-REVIEW-STATUS-PDF", "source": source.identity, "locator": "sources/lantern-review-status.pdf", "format": "pdf", "role": "required", "relevant_to_task": True, "contains_required_material": True, "capability_observation": artifact_observation}, "asu": {"identity": "ASU-F6J-LANTERN-REVIEW-STATUS", "adequacy": universe.adequacy, "basis": universe.basis}, "represented_information": [], "candidates": [], "required_information_need": "The particular synthetic Lantern review-status statement exists only inside the governed Required PDF Artifact.", "required_deficiency": deficiency, "construction": outcome.construction, "renderings": {kind: {"status": value.status, "reason_codes": value.reason_codes, "reference": value.rendering.representation_reference if value.rendering else None} for kind, value in renderings.items()}, "audit": store.audit_for_project("fixture-lantern-f6j", authorized=True)}
    (OUT / "raw-result.json").write_text(json.dumps(normalize(result), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(normalize({"evidence_id": "VE-F6-J-001", "source_availability": source.availability, "artifact_outcome": artifact_observation.outcome, "artifact_limitation": artifact_observation.limitations[0].detail, "represented_information": 0, "candidates": 0, "sufficiency": package.sufficiency, "coherence": package.coherence.outcome, "rendering_statuses": {key: value.status for key, value in renderings.items()}}), sort_keys=True))


if __name__ == "__main__":
    main()
