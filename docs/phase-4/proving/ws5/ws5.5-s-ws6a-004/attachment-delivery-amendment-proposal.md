# Attachment-Delivery Amendment Proposal

**Status:** **PROPOSAL ONLY — NOT ADOPTED — NO SUCCESSOR CREATED — NO CONSUMER INTERACTION**

## Purpose and classification

This assessment addresses whether a text-attachment delivery route can replace
the frozen direct-text route for the existing package/control comparison.

**Classification: B — ATTACHMENT DELIVERY NOT VIABLE UNDER CURRENT
`WS5.5-S-WS6A-004` PROVING REQUIREMENTS.** This does not conclude that an
attachment-based experiment could never be governed; it concludes that it
cannot be introduced into the frozen successor-004 controls as a delivery
repair.

The completed disposable synthetic test established attachment conversion for
a long paste in the observed Firefox/Wayland configuration. It did not expose
the frozen package or either physical Consumer, and it did not establish
submission, platform-side byte fidelity, or identical Consumer processing.

## Existing frozen-control boundary

The successor-004 control requires one-message direct-text feasibility before
delivery and makes failed direct-text feasibility a mandatory stop condition.
Its exact delivery manifests prohibit attachment delivery, multipart delivery,
truncation, condensation, modified payloads, and unapproved framing. The
frozen package and control composites remain respectively:

| Arm | Frozen artifact | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| Package | `frozen-artifacts/package-delivery-payload.txt` | 61,592 | `8ebed11a11b4748fb844e82310475f7f223da9c12260b567b2f20887c54f3137` |
| Control | `frozen-artifacts/control-delivery-payload.txt` | 975 | `336812de6c3079b2ebf506265e09d7d6d015b9cbc799437b289f3c92a72c2786` |

The frozen D5 control payload also states: “No Context Engine package or
rendering, raw Source, repository path, link, **attachment**, tool, or
additional briefing is supplied.” Delivery of that exact payload as an
attachment would contradict its own ordinary-minimal-pointer statement.

Consequently, attachment delivery is not a factual erratum or a narrow
execution correction. It changes the input representation, the delivery
interaction, and the control condition.

## Supported-product evidence and its limits

Official OpenAI documentation states that ChatGPT supports attached TXT files,
subject to plan, account settings, client, model, and applicable limits. It
lists a 512 MB document limit and a 2-million-token cap for text/document
files. It also states that content processing can vary by file type and plan.
The 61,592-byte package is well below the published file-size cap, but that is
not evidence that the selected ChatGPT configuration will accept, extract,
retain, or reason over the exact file bytes equivalently to direct text.

Official documentation: [Uploading files and audio to ChatGPT](https://help.openai.com/en/articles/8555545-uploading-files-and-audio-to-chatgpt).

No reviewed official source establishes all of the following for this run:

- an attachment-bearing turn can be submitted with no extra message text;
- a TXT attachment is processed equivalently to a direct-text message;
- the platform exposes a cryptographic hash of uploaded bytes;
- package and control attachments have equivalent retrieval/extraction
  behavior despite their materially different sizes; or
- the selected Temporary Chat/model/configuration will accept the proposed
  interaction.

## Fairness assessment

| Candidate route | Exact source bytes retained locally | Delivery-mechanism fairness | Control integrity | Current result |
| --- | --- | --- | --- | --- |
| Package attachment; control direct text | Potentially | No — delivery mechanism becomes an arm-specific confound | Control text remains true | Prohibited / unfair |
| Both exact frozen payloads as attachments | Potentially | Better common mechanism, but retrieval/extraction may still vary with 61,592 vs. 975 bytes | No — frozen D5 text falsely says no attachment is supplied | Not viable as frozen |
| Both arms as approved attachment-compatible artifacts | Only after new artifact verification | Potentially, subject to evidence and Owner acceptance | Requires a newly approved control baseline | A different governed experiment |
| Multipart, condensation, rewrite, browser scripting, DOM injection, or hidden-editor manipulation | No or not governed | No | No | Prohibited |

Using a common attachment mechanism is the minimum plausible fairness control:
it avoids assigning different input modalities to the arms. It does not
eliminate the possibility that attachment retrieval/extraction behaves
differently for the large package than for the small baseline. That residual
confound must be expressly evaluated, not assumed away.

The frozen P1–P8 evaluator content need not be changed merely to assess an
attachment proposal. Its applicability and run-validity use, however, cannot
be presumed after this material delivery/intervention change; Project Owner
reaffirmation is required before it could evaluate an attachment-based run.

## Minimum proposed append-only path

Frozen successor-004 must remain historical and unchanged. The minimum
governance vehicle is a **proposed, not-created** append-only successor:
`WS5.5-S-WS6A-005` (or an equivalent separately identified successor required
by repository convention), not an in-place successor-004 amendment.

Before such a successor could be created, the Owner would need to decide:

1. Whether an attachment-based package/control comparison is an acceptable
   new experimental intervention.
2. Whether both arms must use the same governed TXT-attachment mechanism
   (recommended) and whether any accompanying user-message text is allowed;
   no extra text may be assumed.
3. An attachment-compatible control baseline, including removal or replacement
   of the frozen assertion that no attachment is supplied, and a fresh exact
   control artifact/hash.
4. Attachment artifact naming, proposed MIME `text/plain; charset=utf-8`,
   local SHA-256/byte verification, upload-selection evidence, and the limits
   of platform-side fidelity evidence. A neutral common filename (for example
   `input.txt`) is a proposal only, not a frozen decision.
5. A bounded non-proving validation plan that can establish the actual
   account/client/model attachment workflow without exposing frozen proving
   material; the current authorization does not authorize that test.
6. Whether the frozen evaluator's run-validity and fair-control comparison
   remain applicable to the new attachment intervention.
7. New execution controls, attachment-specific raw-input preservation,
   integrity/stop conditions, and all ordinary physical-disclosure and WS6A
   authorization gates.

Attachment evidence must at minimum preserve the local exact source file,
its SHA-256/byte count, selected filename and MIME type, observed upload state,
and the first raw response before evaluation. It cannot claim a platform-side
hash unless the platform supplies one.

## Consumer continuity and quarantine

Neither bound successor-004 Consumer has been exposed by this proposal, so the
current sessions remain quarantined. A future successor-005 does not inherit
their bindings automatically. Before any attachment delivery, each arm needs a
new Owner continuity attestation and separately approved carry-forward binding
to the new successor. WS5 reassessment is required if any continuity-breaking
event occurs; new reservations are then required only if that reassessment
finds the existing session ineligible.

No attachment, tool, connector, upload, or task/package/control exposure may
occur in either reserved Consumer until the distinct successor binding,
physical-disclosure, and WS6A authorities exist.

## Recommended next Owner decision

Decide whether to authorize **design of a separately identified successor-005
attachment-based experiment**. That decision must explicitly accept or reject
the material intervention change, require the same attachment mechanism for
both arms, and authorize preparation—not delivery—of a new attachment-compatible
control baseline and evaluator-fairness review. If the Owner declines that
change, successor-004 remains preserved and blocked on direct-text delivery.
