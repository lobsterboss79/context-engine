# VE-P4-3B-001 — INDETERMINATE Procedure/Evidence Investigation

**Status:** **INVESTIGATION COMPLETE — PROJECT OWNER SUCCESSOR-PROCEDURE
DISPOSITION REQUIRED**

## Authority, baseline, and immutable predecessor

This bounded investigation began from committed `HEAD`
`0c845c7fb00902dfd3333aa0902e0bc5093a9c4c` on
`phase4-ws3-trust-state-audit` (*Preserve Phase 4 trust state audit
indeterminate*). The original execution baseline was
`a06e4da5647df26db4ebe886f7bdfd0a95e00767`.

`VE-P4-3B-001` remains immutable **INDETERMINATE**. This investigation does
not rerun it, alter its frozen ER/runner/evidence, reconstruct the missing
streams, modify application source/tests/shared controls, make a Finding,
perform Item 3.9, or make a Gate/proving/readiness/TD-14 decision.

## Reconstruction of the executed sequence

The preserved exact invocation was:

```text
test ! -e docs/phase-4/validation-evidence/VE-P4-3B-001/raw && mkdir -p docs/phase-4/validation-evidence/VE-P4-3B-001/raw && PYTHONPATH=src python3 docs/phase-4/ws3-lane-b-trust-state-audit/control-runner.py docs/phase-4/validation-evidence/VE-P4-3B-001/raw > docs/phase-4/validation-evidence/VE-P4-3B-001/raw/stdout.txt 2> docs/phase-4/validation-evidence/VE-P4-3B-001/raw/stderr.txt
```

| Sequence | Established fact |
| --- | --- |
| 1 | `test` confirmed that `raw/` was absent; `mkdir -p` then created it. |
| 2 | Before the Python process began, the shell opened `raw/stdout.txt` and `raw/stderr.txt` for the command's standard output/error. Thus both paths were inside the directory supplied to the runner. |
| 3 | `control-runner.py` entered `main(output)`. Its lines 97–100 tested the now-existing `raw/` directory and executed `shutil.rmtree(output)`, followed by `output.mkdir(parents=True)`. |
| 4 | Recursive removal unlinked the two stream pathnames while their shell-open file descriptors remained inherited by the Python process. The runner recreated `raw/`, then created the retained SQLite/result artifacts there. |
| 5 | The runner reached its final `result.json` write and `print(...)`; the shell reported exit code 0. Existing open descriptors allow such writes after pathname unlinking, but the pathnames were absent when the descriptors later closed. |
| 6 | Post-run inspection established that `stdout.txt` and `stderr.txt` are absent. The committed raw directory contains only `source.sqlite`, `backup.sqlite`, `restored.sqlite`, and `result.json`. |

The missing streams cannot honestly be reconstructed. `result.json` is a
separate retained artifact, not the missing original stdout; an empty/missing
stderr cannot be inferred as a preserved stderr artifact.

## Cause and boundary assessment

**Classification: A — EXECUTION PROCEDURE / RUNNER DESIGN ERROR.**

The causal chain needs both elements of one procedure/runner interface error:
the execution procedure placed capture files inside the runner's output
directory, and the runner's frozen initialization contract recursively cleared
that directory. The first alone would preserve streams; the second alone would
not remove streams placed outside the output directory. They are not separate
product, shared-contract, or environment defects, so classification E is not
needed.

| Candidate boundary | Assessment |
| --- | --- |
| ER semantic expectation / fixture semantics | Not causal. B1–B4 expectations and synthetic semantic inputs were not changed by the pathname loss. |
| Executed runner implementation | Causal: `shutil.rmtree(output)` removes all preexisting children of its supplied output directory. |
| Shell invocation / evidence-capture procedure | Causal: redirection targets were pre-opened inside that same runner-cleared directory. The shell did not issue a delete command. |
| Shared WS3 evidence contract | Not defective. It correctly required stdout/stderr preservation; applying that requirement exposed the procedure defect. |
| Application/product behavior | Not causal. The only relevant adapter filesystem operations are a scoped restore-stage `os.replace(staging, self._database)` and failure cleanup of that staging file. They cannot target `stdout.txt` or `stderr.txt`; no application deletion of the stream paths is evidenced. |
| Environment/tooling | Not causal. The observed descriptor/pathname distinction is ordinary shell/POSIX file-descriptor behavior; no tool failure, error, or abnormal environment condition is evidenced. |

## Application assertion result versus validation evidence sufficiency

The retained `raw/result.json`, written after every frozen assertion and just
before the runner's final print, supports the bounded statement:

> The runner reached and recorded successful completion of its internal B1–B4
> assertions in the executed process.

It does **not** establish that raw stdout/stderr were preserved, that the
entire raw process transcript can be evaluated, or that Lane B attained PASS.
The shared contract and the frozen ER required those raw streams. Therefore
the immutable validation state remains **INDETERMINATE** even though the
application assertions reportedly completed successfully. The retained state
and result artifacts must not be promoted into a substitute stream capture.

## Finding and H3 assessment

**Recommendation: NO FINDING; H3 not triggered.**

The issue is a bounded validation-procedure/evidence-capture defect that was
detected, faithfully classified INDETERMINATE, and stopped before a false Lane
B PASS or product/security claim. No evidence shows an application,
authorization, Authority, Governance State, persistence, audit, or Provenance
semantic violation. The existing WS1 Finding types do not require creation of
a product Finding merely because one controlled validation record is
insufficient, and this bounded successor-procedure decision neither changes
approved semantics/architecture/security policy nor requires remediation.

This is a recommendation, not a governed disposition. If the Project Owner
determines the control/evidence process failure materially affects validation
validity beyond this preserved one-run lineage, a MATERIAL process/control
Finding and H3 assessment would require separate governance.

## Obligation and prior-evidence impact

| Scope | Impact |
| --- | --- |
| 3.4-A–D | **NOT YET VALIDATED.** No direct PASS is available from VE-P4-3B-001. |
| 3.5-A–C | **NOT YET VALIDATED.** No direct PASS is available from VE-P4-3B-001. |
| 3.6-A/B/D/E | **NOT YET VALIDATED.** No direct PASS is available from VE-P4-3B-001. |
| Existing Phase 3 / WS2 records | Unchanged supporting evidence only; no prior evidence is invalidated. |
| Surviving VE-P4-3B-001 artifacts | Usable only as evidence of the procedure investigation and the runner's recorded internal assertion completion; not usable direct obligation-validation evidence. |
| Lane A / Lane C | No demonstrated impact or invalidation. They are independent lanes and no evidence establishes that they used this runner/procedure. A similarly unsafe output-capture pattern, if independently proposed, would require its own preflight review; this investigation does not alter their controls. |

## Successor design options and recommendation

The semantic B1–B4 expectations have no evidenced defect. The versioning
boundary is therefore the **execution procedure/runner**, not a semantic
expected-result revision. `ER-P4-3B-001 v1` remains the immutable semantic ER
for its predecessor attempt and must not be edited or retrospectively passed.

| Option | Design | Assessment |
| --- | --- | --- |
| 1 — Versioned procedure/runner successor | Freeze a new lane-private execution-procedure control and runner version. The new runner receives a fresh, nonexisting `raw/state/` directory only; raw stdout/stderr are captured at `raw/stdout.txt` and `raw/stderr.txt`, outside `state/`. The runner must reject an existing state directory rather than delete it. Preserve procedure, streams, state artifacts, result, and manifest before result classification. | **Recommended minimum.** ER semantics remain unchanged; evidence identity is new. |
| 2 — ER v2 plus procedure/runner v2 | Create `ER-P4-3B-001 v2` solely to version the execution/control package while explicitly retaining identical B1–B4 semantic expectations, then use the same separated capture/state layout. | Permissible only if the Project Owner decides the local ER convention makes the runner/procedure part of the ER control identity. It must be a procedural supersession, not a changed semantic expected result. |
| 3 — Shared contract revision | Change shared requirements or treat `result.json` as stream substitute. | Not recommended and unsupported: the shared contract correctly required preserved streams. |

**Recommended successor lineage, subject to Project Owner authorization:**

```text
VE-P4-3B-001 / ER-P4-3B-001 v1 / runner v1
    -> immutable INDETERMINATE predecessor
    -> new frozen lane-private procedure control v2 + runner v2
    -> new evidence identity VE-P4-3B-002
```

The successor must be a new deliberate execution, with new pre-results hash
freeze and a fresh evidence directory. It must not overwrite or reuse the
predecessor's raw directory. It may reuse unchanged semantic B1–B4
expectations only after the Owner authorizes the successor procedure and
execution.

## Immutable artifacts and exact Owner decision

The following predecessor artifacts must remain unchanged: the committed
`0c845c7` history; `analysis-preparation.md`; `ER-P4-3B-001.md`; executed
`control-runner.py`; `VE-P4-3B-001/preflight.md`;
`VE-P4-3B-001/validation-evidence-record.md`; the preserved procedure text;
and every existing `VE-P4-3B-001/raw/` artifact, including the absence of the
two stream pathnames.

**Project Owner decision required:** approve or reject a new, lane-private,
non-semantic successor execution-procedure/runner control under Option 1
(recommended), or direct Option 2 if an ER-versioned procedural supersession
is required by the Owner. The decision must state whether a new execution is
authorized after that successor is frozen. It must retain VE-P4-3B-001 as
INDETERMINATE and create separate successor evidence; it does not authorize
application remediation, source/test/shared-file change, a Finding
disposition, Lane B completion, Item 3.9, TD-14 action, Gate 4B, proving, or
readiness.
