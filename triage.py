"""Summarize exported Splunk alert rows without contacting a live system."""
import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


def summarize(rows):
    services = defaultdict(Counter)
    seen = {}
    for row in rows:
        event_id, service, severity = (
            (row.get(key) or "").strip() for key in ("event_id", "service", "severity")
        )
        if not event_id or not service or severity not in {"critical", "warning", "info"}:
            raise ValueError("each row needs an event ID, service and supported severity")
        signature = (service, severity)
        if event_id in seen:
            if seen[event_id] != signature:
                raise ValueError("conflicting rows share an event ID")
            continue
        seen[event_id] = signature
        services[service][severity] += 1
    return [
        {"service": service, "counts": dict(sorted(counts.items())),
         "queue": "page" if counts["critical"] else "review" if counts["warning"] else "observe"}
        for service, counts in sorted(services.items(), key=lambda item: (
            -item[1]["critical"], -item[1]["warning"], item[0]
        ))
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("export", type=Path)
    args = parser.parse_args()
    try:
        with args.export.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream, strict=True)
            if reader.fieldnames != ["event_id", "service", "severity"]:
                raise ValueError("expected CSV headers event_id,service,severity")
            print(json.dumps(summarize(reader), indent=2))
    except (OSError, ValueError, csv.Error) as exc:
        parser.exit(2, f"Input error: {exc}\n")


if __name__ == "__main__":
    main()
