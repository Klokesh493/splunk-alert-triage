# Replay evidence

Captured stdout is compared with a checked-in baseline.

## Demo 1

Result: **PASS**

````text
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

## Last sample record in isolation

Result: **PASS**

````text
[
  {
    "service": "checkout",
    "counts": {
      "critical": 1
    },
    "queue": "page"
  }
]
````
