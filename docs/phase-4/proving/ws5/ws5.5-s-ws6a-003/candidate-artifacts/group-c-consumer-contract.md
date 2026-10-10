# Group C2 ConsumerContract Candidate

**Status:** **CANDIDATE — NOT FROZEN — PROJECT OWNER APPROVAL PENDING**

The production contract is:

```python
ConsumerContract(
    kind: ConsumerKind,
    consumer: Consumer,
    disclosure_authorized: bool | None,
    capacity_characters: int | None = None,
)
```

| Field | Candidate value | Contract status | Basis / limitation |
| --- | --- | --- | --- |
| `kind` | `ConsumerKind.CHATGPT` | Structurally valid | The intended package-arm Consumer is ChatGPT. |
| `consumer` | **UNRESOLVED** | Not instantiable | A successor-004 carry-forward decision has not been approved. WS5 evidence for `CE-P4-WS5-CONSUMER-002` does not itself create a successor-004 `Consumer` binding. |
| `disclosure_authorized` | **UNRESOLVED** | Not execution-valid | The renderer denies a value other than literal `True`; no separate Owner authorization for the exact Consumer-facing package disclosure exists. Do not set it to `True`. |
| `capacity_characters` | `None` proposed | Structurally valid | This means no Context Engine configured character limit. It does not assert unlimited ChatGPT or delivery capacity; C4 remains required. |

The dataclass accepts the field types, but a complete production contract cannot
be instantiated without a real `Consumer`; an unresolved string or placeholder
would not be an authorized substitute. The approved D4 inert-evidence wrapper
is a delivery-boundary artifact, not a `ConsumerContract` field and not a
disclosure grant.

No Consumer identity is placed in this candidate. No rendering is requested or
performed.
