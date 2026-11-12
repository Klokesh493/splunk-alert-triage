# Splunk Alert Triage walkthrough

## Business problem

Turn exported alert rows into a prioritized on-call review queue. Exact duplicates count once. Conflicting event IDs fail the run.

## Reproduce the workflow

Run `python3 triage.py example.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
[
  {
    "service": "checkout",
    "counts": {
      "critical": 1,
      "warning": 1
    },
    "queue": "page"
  },
  {
    "service": "catalog",
    "counts": {
      "info": 1
    },
    "queue": "observe"
  }
]
```

The sample supplies these fields. `event_id`, `service`, `severity`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
