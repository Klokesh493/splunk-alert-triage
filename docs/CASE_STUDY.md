# Splunk Alert Triage walkthrough

## Business problem

An exported alert stream can repeat events and bury the highest-severity service. Responders need a deduplicated queue for review.

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
