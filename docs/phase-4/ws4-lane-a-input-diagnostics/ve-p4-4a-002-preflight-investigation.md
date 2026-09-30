# VE-P4-4A-002 Preflight Investigation

**Status:** **INVESTIGATION COMPLETE — PROJECT OWNER PREFLIGHT-SUCCESSOR DISPOSITION REQUIRED**

## Baseline, lineage, and scope

This bounded read-only investigation began on committed baseline `85d0adf`
(`Preserve Phase 4 input diagnostics preflight indeterminate`). `VE-P4-4A-001`
is the immutable first predecessor: INDETERMINATE because CTL-P4-4A-001
constructed `SemanticIdentity` with one instead of two fields. Its approved
investigation is committed at `f55d254`. `VE-P4-4A-002` remains permanently
**INDETERMINATE — PREFLIGHT PROCEDURE DEFICIENCY; CONTROL NOT EXECUTED**.
Neither classification is changed by this investigation.

## Exact failed mechanism

The 002 preflight attempted these command forms under Windows PowerShell:

```powershell
git cat-file -e 1fdef6e^{commit}
git cat-file -e f55d254^{commit}
```

The intended Git revision form was `<rev>^{commit}` (peel and require a commit).
PowerShell did not pass that expression as one Git argument. Its parser tokenizes
the first form as `Generic: 1fdef6e^`, `LCurly: {`, `Identifier: commit`, and
`RCurly: }`. Git consequently rejected the invocation (`unknown switch 'n'` in
the preserved attempt), and the shell procedure recorded both committed-lineage
flags false. The failure was command construction before semantic control
execution, not a Git repository state failure.

Read-only commands without peel-expression characters establish the actual
state:

```powershell
git rev-parse --verify --quiet 1fdef6e
git show -s --format=%H 1fdef6e
git merge-base --is-ancestor 1fdef6e HEAD
git rev-parse --verify --quiet f55d254
git show -s --format=%H f55d254
git merge-base --is-ancestor f55d254 HEAD
```

Each command succeeded. The resolved predecessor is
`1fdef6ee07c5a6f5e6663f34b85b6e339845bd03`; the investigation is
`f55d2541b7c650e28cdfa70dc0ff3648ff11fa51`; both are ancestors of `HEAD`.
Therefore the precondition was **TRUE**, while its 002 check implementation
was **FALSE**.

The portable replacement to freeze in a later authorized preflight is the
paired `rev-parse --verify --quiet <literal-sha>` plus
`merge-base --is-ancestor <literal-sha> HEAD` form above. It validates identity
and reachability without using `^{commit}`, braces, or other shell-sensitive
revision syntax. It is not implemented by this record.

## Classification and semantic status

**Root-cause classification: A — WINDOWS-SPECIFIC PREFLIGHT COMMAND / SHELL
DESIGN ERROR.** The mandatory use of an unquoted Git peel expression is
incompatible with the actual PowerShell tokenization. This does not indicate a
generic Git/repository defect, missing lineage, semantic-control defect, or
H3 ambiguity.

All other preserved preflight criteria passed: correct branch and `636afcf`
ancestry; v1 immutability; source/test/shared WS4 and Lane B/C integrity;
fresh 002 namespace; Windows environment; frozen successor hashes; and static
verification that the 002 runner has one direct `SemanticIdentity(kind, value)`
call with two fields. The semantic ER, v1 fixtures, corrected runner, and
expected-state model remain valid and untouched. The 002 runner was never
invoked: no CLI case, Source case, diagnostic check, assertion, distinction
matrix, regression, or application semantic execution occurred.

## Immutability and supersession boundary

Immutable 002 artifacts are its ER, procedure, runner/control, referenced v1
fixtures, preflight raw facts/hashes, preflight record, and validation-evidence
record. `VE-P4-4A-002` must remain the permanent INDETERMINATE preflight
attempt even though its intended repository precondition is now shown true.

Existing WS1/WS4 preservation rules require a later result to be separately
identified; they do not permit editing 002's preflight or converting it to
PASS. Because no semantic runner execution occurred and the frozen 002 ER,
fixtures, and runner remain valid, **Option 1** is the minimum
governance-correct boundary: a separately versioned, portable successor
preflight/procedure may reference unchanged `CTL-P4-4A-002`, its ER, and its
fixtures, while preserving fresh, independently identified evidence. A new
evidence identity would be required for that later result; it is not created
or authorized here. Option 2 (entirely new semantic CTL/ER/fixture) is not
supported because no defect in those artifacts is evidenced.

## Finding, impact, and required decision

**NO FINDING; H3 NOT TRIGGERED.** The defect is confined to preflight command
construction and demonstrates no product or material validation-governance
defect. All Lane A obligations remain **NOT YET VALIDATED**: 4.1-A, 4.1-B,
4.1-C, 4.1-D, and 4.6-B. Lane B/C are unaffected. **NO 4.7 INTERACTION:**
this ordinary validation-procedure portability defect evidences none of Item
4.7's enumerated operational/infrastructure needs.

**Exact Project Owner decision required:** authorize or decline preparation of
a separately identified portable preflight/procedure successor and fresh
evidence record that reuses the unchanged frozen 002 semantic control/ER/
fixture basis; if prepared, separately authorize its preflight and only then
its semantic control execution. No edit, rerun, remediation, or 003 artifact
is authorized by this investigation.
