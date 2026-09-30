#!/usr/bin/env python3
"""Independent, lane-private WS4 4.2 evidence fixture."""
from __future__ import annotations
import argparse, hashlib, json, shutil, sqlite3
from pathlib import Path
from context_engine.adapters import sqlite_state
from context_engine.adapters.sqlite_state import CURRENT_SCHEMA_VERSION, PersistedEvidence, PersistedObservation, PersistedPackageConstruction, PersistedSourceRegistration, RestoreError, SQLiteStateStore

def sha(p: Path) -> str: return hashlib.sha256(p.read_bytes()).hexdigest()
def integrity(p: Path) -> str:
    with sqlite3.connect(f"file:{p}?mode=ro", uri=True) as c: return c.execute("PRAGMA integrity_check").fetchone()[0]
def version(p: Path) -> int:
    with sqlite3.connect(f"file:{p}?mode=ro", uri=True) as c: return c.execute("SELECT version FROM schema_version").fetchone()[0]
def populated(p: Path, project: str, claim: str) -> SQLiteStateStore:
    s=SQLiteStateStore(p); s.initialize(); s.save_evidence(PersistedEvidence(project,claim,f"historical {claim}"))
    if project == "project-a":
        s.save_source_registration(PersistedSourceRegistration(project,"source-a","markdown","docs","available","docs/a.md")); s.save_observation(PersistedObservation(project,"observation-a","source-a","2026-01-01T00:00:00+00:00","observed","local-only")); s.save_package_construction(PersistedPackageConstruction(project,"record-a","request-a","package-a","completed","sufficient","coherent","historic construction")); s.write_audit(project,"rendering-rendered","controlled render outcome")
    return s
def save(out: Path, result: dict) -> None:
    (out/"result.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8"); print(json.dumps(result,sort_keys=True))
def predecessor(out: Path) -> dict:
    source=populated(out/"source.sqlite","project-a","claim-a"); target=populated(out/"target.sqlite","project-b","claim-b"); backup=out/"valid.sqlite"; source.create_backup(backup,operator_authorized=True,purpose="ws4 independent interruption",retention_basis="lane-private evidence"); before=sha(out/"target.sqlite"); original=sqlite_state.os.replace; sqlite_state.os.replace=lambda _s,_t: (_ for _ in ()).throw(OSError("controlled replacement interruption")); caught=None
    try: target.restore_backup(backup,operator_authorized=True)
    except RestoreError as e: caught=str(e)
    finally: sqlite_state.os.replace=original
    return {"scenario_state":"APPLICATION-LEVEL FAILURE / RECOVERY REQUIRED","caught_restore_error":caught,"target_hash_before":before,"target_hash_after":sha(out/"target.sqlite"),"target_integrity":integrity(out/"target.sqlite"),"target_version":version(out/"target.sqlite"),"target_project_b_claim":target.restore_evidence("project-b","claim-b").historical_reference if target.restore_evidence("project-b","claim-b") else None,"target_project_a_claim":target.restore_evidence("project-a","claim-a"),"recovery_qualification":target.recovery_qualification() is not None,"staging_files":sorted(x.name for x in out.glob(".context-engine-restore-*.sqlite")),"backup_integrity":integrity(backup)}
def successor(out: Path, prior: Path) -> dict:
    shutil.copy2(prior/"target.sqlite",out/"target.sqlite"); shutil.copy2(prior/"valid.sqlite",out/"valid.sqlite"); predecessor_hash=sha(prior/"target.sqlite"); copied_hash=sha(out/"target.sqlite"); target=SQLiteStateStore(out/"target.sqlite"); q=target.restore_backup(out/"valid.sqlite",operator_authorized=True); restored=target.restore_evidence("project-a","claim-a")
    return {"scenario_state":"SUCCESSFUL PREDETERMINED RECOVERY SUCCESSOR","predecessor_target_hash":predecessor_hash,"copied_pre_recovery_target_hash":copied_hash,"target_integrity":integrity(out/"target.sqlite"),"target_version":version(out/"target.sqlite"),"target_project_a_claim":restored.historical_reference if restored else None,"target_project_b_claim":target.restore_evidence("project-b","claim-b") is not None,"source_registration":target.source_registrations_for_project("project-a")[0].source_identity,"observation":target.observations_for_project("project-a")[0].observation_identity,"construction":target.package_constructions_for_project("project-a")[0].record_identity,"audit":list(target.audit_for_project("project-a",authorized=True)),"qualification":q.qualification,"restored_currentness":restored.currentness if restored else None,"restored_authority_basis":restored.authority_basis if restored else "unexpected-none","staging_files":sorted(x.name for x in out.glob(".context-engine-restore-*.sqlite"))}
def migration(out: Path) -> dict:
    p=out/"version-one.sqlite"
    with sqlite3.connect(p) as c:
        c.execute("CREATE TABLE schema_version (version INTEGER NOT NULL)"); c.execute("INSERT INTO schema_version VALUES (1)"); c.execute("CREATE TABLE evidence (row_id INTEGER PRIMARY KEY, project_identity TEXT NOT NULL, semantic_identity TEXT NOT NULL, historical_reference TEXT NOT NULL, UNIQUE(project_identity, semantic_identity))"); c.execute("CREATE TABLE audit (row_id INTEGER PRIMARY KEY, project_identity TEXT NOT NULL, outcome TEXT NOT NULL, detail TEXT NOT NULL)"); c.execute("INSERT INTO evidence VALUES (1,'project-m','claim-m','v1 historical evidence')")
    s=SQLiteStateStore(p); s.initialize()
    with sqlite3.connect(f"file:{p}?mode=ro",uri=True) as c: table_names=sorted(x[0] for x in c.execute("SELECT name FROM sqlite_master WHERE type='table'"))
    r=s.restore_evidence("project-m","claim-m"); return {"scenario_state":"SUPPORTED MIGRATION COMPLETED","schema_version":version(p),"expected_schema_version":CURRENT_SCHEMA_VERSION,"integrity":integrity(p),"tables":table_names,"retained_v1_evidence":r.historical_reference if r else None}
def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument("scenario",choices=("predecessor","successor","migration")); ap.add_argument("--out",type=Path,required=True); ap.add_argument("--predecessor-state",type=Path); a=ap.parse_args()
    if a.out.exists(): raise SystemExit("output state directory must be new")
    a.out.mkdir(parents=True)
    result=predecessor(a.out) if a.scenario=="predecessor" else successor(a.out,a.predecessor_state) if a.scenario=="successor" and a.predecessor_state else migration(a.out)
    save(a.out,result)
if __name__ == "__main__": main()
