# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 triage.py example.csv
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
````
