# Skills and verification

## What this repository demonstrates

An offline triage CLI for exported Splunk alerts. It validates event ID, service, and severity, counts exact duplicates once, rejects conflicting duplicate IDs, and groups remaining events into page, review, or observe queues.

## Reproduce the result

Checkout goes to page with one critical and one warning. Catalog goes to observe with one info event. Reproduce the primary fixture with `python3 triage.py example.csv`.

Run `make verify` locally. Ruff and Bandit medium/high checks passed for the checked Python code.

## Scope

Use the CSV header event_id,service,severity in that order. Queue labels are recommendations. The tool does not connect to Splunk or send pages.

A conflicting duplicate event ID signals an export integrity issue. Review it upstream before trusting the service queue.

[triage.py](../triage.py) · [examples/Demo 1.stdout.txt](../examples/Demo%201.stdout.txt) · [Architecture](../docs/ARCHITECTURE.md) · [Case study](../docs/CASE_STUDY.md) · [Runbook](../docs/RUNBOOK.md) · [CI template](../docs/github-actions/ci.yml)
