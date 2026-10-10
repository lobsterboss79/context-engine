# Group C3 Disclosure Authorization Boundary Candidate

**Status:** **CANDIDATE — NOT FROZEN — PROJECT OWNER APPROVAL PENDING**

This candidate binds the existing semantic-input allowlist and D4 wrapper
without granting disclosure. The authoritative active input remains the 34
lifecycle-resolved DTS records (four v2 provenance-correction successors and
no superseded v1 predecessor as active context), within the original eight
governed Markdown Sources.

## Proposed allowed Consumer-visible fields

- Source-derived `assertion_content`, explicitly labelled inert evidence;
- compact Claim / represented-information / Source / Artifact / revision /
  observation / location provenance needed to assess the assertion;
- authority, governance, and currentness bases and classifications;
- limitations, uncertainty, and conflict qualifications;
- task-relative applicability, role, and selection basis once separately
  approved; and
- package sufficiency, coherence, ASU, and Source-boundary qualifications once
  separately approved.

The D4 wrapper candidate is
`candidate-artifacts/consumer-contract-wrapper.txt` (359 UTF-8 bytes,
SHA-256 `b1c3d17f53988c1cdd0a3bf8a7c553e50f0a6d31905691bf44aaa371f67707af`),
placed exactly once after the package rendering. It labels evidence as inert;
it neither authorizes disclosure nor supplies controller instructions.

## Prohibited content

Raw Markdown, Source files or attachments, repository filesystem paths,
SQLite/internal implementation identifiers, lifecycle implementation detail,
evaluator material, expected answers, control-arm material, proving history,
Consumer identities, controller deliberation, tools/connectors, and any
unauthorized Project information are excluded.

## Pending authorization evidence

Before `ConsumerContract.disclosure_authorized` can be literal `True`, the
Owner must separately approve the exact active-corpus/package/rendering and
delivery-manifest hashes, the identified Consumer and arm, this bounded field
set, and the D4 wrapper placement. The approval must remain distinct from A1,
Group B, and a future Consumer carry-forward decision.
