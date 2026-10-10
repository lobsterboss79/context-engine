# Candidate Delivery-Feasibility Test Procedure

**Status:** **COMPLETED SYNTHETIC COMPOSER-ONLY TEST — ATTACHMENT-ONLY OUTCOME — FROZEN-PAYLOAD DELIVERY FEASIBILITY INDETERMINATE**

## Purpose and governance boundary

This procedure tests only ChatGPT web-composer handling of a synthetic non-proving long direct-text payload. It is not a Consumer reservation, logical candidate Consumer, package-arm Consumer, control-arm Consumer, payload delivery, or WS6A action.

| Category | Identity / boundary | Permitted role in this procedure |
| --- | --- | --- |
| Logical candidate Consumer | `consumer:I10-DTS-CHATGPT-CANDIDATE-RENDERING-v1` | None; repository-side Stage 1 identity only |
| Package proving Consumer | `CE-P4-WS5-CONSUMER-002`, Firefox tab 2 | None; reserved, preflighted fresh, quarantined, and bound to successor-004 |
| Control proving Consumer | `CE-P4-WS5-CONTROL-001`, Firefox tab 3 | None; reserved, preflighted fresh, quarantined, and bound to successor-004 |
| Disposable UI-test session | New standalone Temporary Chat outside the Context Engine Project | Proposed future synthetic test only; never a proving Consumer |

The frozen package payload remains 61,592 UTF-8 bytes, SHA-256 `8ebed11a11b4748fb844e82310475f7f223da9c12260b567b2f20887c54f3137`. It must never enter the disposable session.

## Governance eligibility and required future authorization

The frozen proving controls prohibit interaction with the reserved Consumers, not a separately created non-proving session containing no proving material. The Project Owner's **PHASE 4 — SYNTHETIC DELIVERY-FEASIBILITY TEST** authorization permits one Owner-operated disposable Temporary Chat, this synthetic artifact, the listed composer-only observations, external evidence capture, and disposal. It does not authorize a message submission.

The completed authorization permitted deterministic synthetic-artifact materialization, integrity verification, one disposable composer-only paste/UI observation, external evidence capture, and disposal. It did not permit message submission, frozen proving-material exposure, reserved-Consumer interaction, or WS6A.

## Proposed synthetic payload specification

| Field | Proposed value |
| --- | --- |
| Identity | `I10-SYNTHETIC-DIRECT-TEXT-PROBE-v1` |
| Encoding | UTF-8 / ASCII subset |
| Construction | Repeat the single ASCII byte `0x58` (`X`) exactly 61,592 times |
| Exact byte count | 61,592 |
| Terminal newline | Absent |
| Content exclusions | No Context Engine, Day Trading System, task, package, evaluator, answer, proving procedure, control baseline, reserved Consumer identity, credential, or private data |
| Materialized path | `/home/lobsterboss79/temp/context-engine-synthetic-61592.txt` |
| SHA-256 | `ff734a0c25a0c754a7ad66142a749c4898ec159c83a9becb782c658f69b413b7` |

The method is deterministic and does not require semantic text. The materialized file was independently verified as exactly 61,592 UTF-8/ASCII bytes, all `0x58`, without a terminal newline. It has not been copied into a browser, clipboard, or Consumer session. The file is a temporary external test artifact, not a successor-004 artifact.

## Clipboard preparation for a future authorized test

No standalone clipboard utility (`wl-copy`, `xclip`, or `xsel`) is installed on LNX-01. The installed PyGObject/GDK 4 runtime can own an exact UTF-8 clipboard selection. After the Owner creates the authorized disposable test session, run the following command in a terminal and leave that terminal process running until the single paste has completed; end it with `Ctrl+C` afterward. It verifies the file before setting the selection and passes the file bytes directly without adding a newline.

```bash
python3 -c "import gi, hashlib; from pathlib import Path; gi.require_version('Gdk','4.0'); from gi.repository import Gdk, GLib; p=Path('/home/lobsterboss79/temp/context-engine-synthetic-61592.txt'); b=p.read_bytes(); assert len(b)==61592 and b==b'X'*61592 and hashlib.sha256(b).hexdigest()=='ff734a0c25a0c754a7ad66142a749c4898ec159c83a9becb782c658f69b413b7'; d=Gdk.Display.get_default(); assert d is not None; d.get_clipboard().set_content(Gdk.ContentProvider.new_for_bytes('text/plain;charset=utf-8', GLib.Bytes.new(b))); print('Synthetic clipboard selection is ready; paste once into the disposable composer, do not submit, then press Ctrl+C here.'); GLib.MainLoop().run()"
```

This command does not authorize submission; it is the byte-preserving copy mechanism for the approved composer-only procedure.

## Executed disposable-session procedure and factual observations

The Owner reports the following completed, factual sequence:

1. A disposable ChatGPT Temporary Chat outside the Context Engine Project was used on LNX-01 / Ubuntu / Wayland / Firefox.
2. The synthetic file integrity and its 61,592-byte size were verified; the Wayland clipboard byte count was also verified as 61,592.
3. The synthetic payload was pasted once into that disposable composer.
4. ChatGPT converted it automatically to a `Pasted text` attachment. The attachment viewer displayed content and exposed only `Pasted text.txt` and `File info`.
5. No **Show in text field** control was found in the viewer or attachment-card hover state.
6. No message was submitted. No frozen proving material was disclosed.
7. The disposable Temporary Chat was closed, the clipboard-owner process was stopped, and both reserved Consumers remained untouched.

The Owner did not report a platform-side hash calculation after paste. Attachment-viewer display is not evidence that ChatGPT retained every synthetic byte.

[Official OpenAI documentation](https://learn.chatgpt.com/docs/whats-new) says pastes longer than 10,000 characters become attachments and **Show in text field** moves the content back into the message. That documents a UI path, not exact-byte fidelity, successful submission, or behavior in a reserved proving session.

## Proposed classifications and limits

| Finding | PASS | FAIL | INDETERMINATE |
| --- | --- | --- | --- |
| Paste feasibility | Verified synthetic artifact can be pasted into disposable composer | Paste cannot be initiated or is rejected | UI state cannot be determined |
| Direct-text composer feasibility | After allowed conversion, one direct-text composer representation is observed | Attachment-only behavior persists | UI appearance cannot establish direct-text state |
| One-message submission feasibility | Only after separately authorized synthetic submission and preserved evidence | Submission requires multipart, modification, or attachment | No authorized submission or insufficient evidence |
| Exact-byte fidelity | Only if governed verification shows composed/submitted text equals synthetic artifact | Verified mismatch, truncation, or transformation | UI state alone cannot prove all bytes |
| Applicability to frozen package payload | Never PASS from synthetic evidence alone | N/A | Synthetic evidence informs risk only; exact frozen-payload delivery remains indeterminate until separately authorized exact-run validation |

## Completed-test classification

| Question | Classification | Evidence and limit |
| --- | --- | --- |
| Synthetic paste feasibility | **PASS** | The verified 61,592-byte synthetic payload was pasted into the disposable composer. |
| Attachment conversion | **OBSERVED** | The disposable composer automatically converted the paste to a `Pasted text` attachment. |
| Synthetic direct-text composer feasibility in the observed environment | **FAIL** | Attachment-only UI was observed and no **Show in text field** control was found. This is limited to the tested synthetic payload, Firefox/Wayland UI state, and observed controls. |
| Synthetic one-message submission feasibility | **INDETERMINATE** | Submission was prohibited and did not occur. |
| Platform-side exact-byte fidelity after paste | **INDETERMINATE** | File and clipboard size were verified; attachment-viewer display did not establish a platform-side byte hash or equivalence check. |
| Frozen 61,592-byte package-payload direct-text delivery | **INDETERMINATE** | The frozen bytes were not exposed, and a synthetic result cannot prove or disprove direct-text delivery of the frozen payload. |
| Frozen one-message delivery feasibility | **INDETERMINATE — BLOCKED UNDER CURRENT CONTROL** | Successor-004 requires direct-text one-message feasibility before delivery; its frozen controls prohibit attachment, multipart, truncation, condensation, and unapproved alternative delivery. |

## Mandatory stops

Stop and preserve evidence if proving material enters the disposable session; either reserved Consumer is activated or altered; synthetic bytes are altered, truncated, or cannot be integrity-verified; attachment-only behavior persists; target-session identity is uncertain; a message would be submitted without authorization; or any event conflicts with frozen controls. Do not propose multipart delivery, condensation, attachment delivery, or modification of the frozen package payload.

## Owner evidence-capture template

Record only observed facts; leave a field as `NOT OBSERVED` rather than infer it.

```text
Test identity: I10-SYNTHETIC-DIRECT-TEXT-PROBE-v1
Synthetic path: /home/lobsterboss79/temp/context-engine-synthetic-61592.txt
Synthetic byte count: 61592
Synthetic SHA-256: ff734a0c25a0c754a7ad66142a749c4898ec159c83a9becb782c658f69b413b7
Encoding / terminal newline: UTF-8 ASCII / absent
Disposable session boundary: <Owner-described new Temporary Chat; not either reserved Consumer>
Browser / displayed model or configuration: <observed>
Reserved Consumers untouched before and after: <attested>
Paste initiated: YES / NO
Automatic attachment conversion observed: YES / NO / NOT OBSERVED
"Show in text field" offered: YES / NO / NOT OBSERVED
"Show in text field" selected: YES / NO / NOT APPLICABLE
One direct-text composer representation observed: YES / NO / NOT OBSERVED
Displayed truncation, error, or unexpected state: <observed or NONE OBSERVED>
Message submitted: NO
Uploads or manually attached files: NO
Limitations: Composer appearance does not establish platform-side exact-byte fidelity or submission feasibility.
Classification: PASS / FAIL / INDETERMINATE, with factual basis
```

## Delivery-method boundary and recommended next Owner decision

The current successor permits only the exact direct-text, one-message payloads. Its package delivery manifest and successor control make attachment delivery, multipart delivery, truncation, condensation, modified payloads, and unapproved alternative delivery methods stop conditions. Therefore the completed disposable test does not authorize a frozen-payload submission.

| Possible next path | Frozen payload preserved | Governance effect | Consumer-reservation effect | Current status |
| --- | --- | --- | --- | --- |
| Establish an approved direct-text, one-message method for the exact frozen payload | Yes, if bytes, ordering, and one-message representation are independently verified | Requires a new, bounded delivery-feasibility authorization and evidence plan; no control change until a method is established | Does not itself require a new reservation; any later delivery still requires continuity, disclosure, and WS6A gates | Potentially compliant, but no method is currently established |
| Submit the frozen payload as the observed `Pasted text` attachment | Component bytes may be unchanged, but delivery representation changes | Requires a Project Owner delivery-method amendment and new append-only execution controls; it changes the package-arm intervention and requires a fresh control-arm fairness assessment | Existing successor-004 bindings cannot be used automatically; a governed carry-forward reassessment would be required and fresh reservations may be required if continuity is lost | Prohibited by current frozen controls |
| Split, condense, truncate, summarize, or otherwise rewrite the payload | No | Changes exact payload and experimental intervention; would require a material new governed design, not a delivery fix | Existing bindings cannot be used automatically | Prohibited by current frozen controls |
| Test or deliver through either reserved Consumer before a new authorization | N/A | Violates quarantine, disclosure, and WS6A boundaries | Could invalidate the affected Consumer | Prohibited |

**Recommended minimum Owner decision:** authorize a narrowly bounded **direct-text delivery-method investigation** outside the reserved Consumers. It must identify a candidate method that preserves the already frozen 61,592 bytes as one direct-text message and specify independent byte-fidelity evidence before any physical disclosure. It must not authorize attachment submission, multipart delivery, frozen-payload exposure, Consumer interaction, binding changes, or WS6A. If no such method can be established, the Owner must decide separately whether to pursue a material delivery-method/control amendment or preserve successor-004 without execution.
