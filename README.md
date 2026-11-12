# Splunk Alert Triage

Turn exported alert rows into a prioritized on-call review queue. Exact duplicates count once. Conflicting event IDs fail the run.

## Quick start

With Python 3.10 or newer, run `python3 triage.py example.csv`. The synthetic sample places checkout in the page queue and catalog in observe.

## Input and limits

Export `event_id,service,severity` in that order. Normalize severity to `critical`, `warning`, or `info`. Critical services appear first, followed by warning count and service name. Queue names are recommendations. The CLI reads local files and makes no network calls. Live Splunk integration was outside the scope of this lab.

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI.

## Project walkthrough

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)
