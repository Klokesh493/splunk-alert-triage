PYTHON ?= python3

.PHONY: verify
verify:
	$(PYTHON) triage.py example.csv
