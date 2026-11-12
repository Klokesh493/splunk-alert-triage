# Splunk Alert Triage architecture

Turn exported alert rows into a prioritized on-call review queue. Exact duplicates count once. Conflicting event IDs fail the run.

```mermaid
flowchart LR
    A["Exported Splunk alert CSV"]
    B["Validate rows, deduplicate IDs, and count severity per service"]
    C["Highest severity determines queue"]
    D["Page for critical"]
    E["Review for warning or observe for info"]
    A --> B --> C
    C --> D
    C --> E
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
