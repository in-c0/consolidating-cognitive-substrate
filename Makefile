.PHONY: check validate reconcile render clean help

help:
	@echo "make validate   - ledger invariants + prose tripwire"
	@echo "make reconcile  - read-only drift check against sibling repos"
	@echo "make render     - regenerate docs views from ledger/*.json"
	@echo "make check      - validate + render + confirm views are current"

validate:
	python3 tools/validate_ledger.py

render:
	python3 tools/render.py

reconcile:
	python3 tools/reconcile.py

# `check` fails if the rendered views drift from the ledger JSON.
check: validate render
	@if ! git diff --quiet -- docs/CLAIM-LEDGER.md docs/DEPENDENCY-DAG.md; then \
		echo "ERROR rendered views were stale; they have been regenerated."; \
		echo "      review the diff and commit it."; \
		git --no-pager diff --stat -- docs/CLAIM-LEDGER.md docs/DEPENDENCY-DAG.md; \
		exit 1; \
	fi
	@echo "OK    ledger valid, rendered views current"
