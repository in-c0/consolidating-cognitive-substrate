.PHONY: check validate reconcile render clean help

VIEWS := docs/CLAIM-LEDGER.md docs/DEPENDENCY-DAG.md docs/EVIDENCE-MAP.md

help:
	@echo "make validate   - ledger invariants + prose tripwire"
	@echo "make reconcile  - read-only drift check against sibling repos"
	@echo "make render     - regenerate docs views from ledger/*.json"
	@echo "make check      - validate + confirm views match the ledger"

validate:
	python3 tools/validate_ledger.py

render:
	python3 tools/render.py

reconcile:
	python3 tools/reconcile.py

# `check` fails if a rendered view disagrees with the ledger JSON it comes from.
# It compares the working tree before and after rendering, NOT against git HEAD,
# so it behaves the same on a dirty tree as on a clean one.
check: validate
	@tmp=$$(mktemp -d); \
	for f in $(VIEWS); do cp "$$f" "$$tmp/$$(echo $$f | tr / _)"; done; \
	python3 tools/render.py >/dev/null; \
	rc=0; \
	for f in $(VIEWS); do \
		if ! diff -q "$$f" "$$tmp/$$(echo $$f | tr / _)" >/dev/null; then \
			echo "ERROR $$f was stale and has been regenerated; review and commit it."; \
			rc=1; \
		fi; \
	done; \
	rm -rf "$$tmp"; \
	if [ $$rc -eq 0 ]; then echo "OK    ledger valid, rendered views current"; fi; \
	exit $$rc
