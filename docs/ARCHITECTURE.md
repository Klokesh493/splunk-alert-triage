# Splunk Alert Triage architecture

Turn exported alert rows into a prioritized on-call review queue. Exact duplicates count once. Conflicting event IDs fail the run.

```mermaid
flowchart LR
    N0["example.csv"]
    N1["triage.py"]
    N2["Deduplicate event IDs and prioritize services by highest observed severity."]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
