# Reconciliation policy

How the umbrella repository stays in sync with the sibling repositories, and the
strict limits on what it may do to them.

## The boundary

**This repository observes. It does not steer.**

Specifically, from here we do **not**:

- modify any experimental protocol in a sibling repository
- edit, amend or reinterpret a preregistration
- change thresholds, budgets, seeds, baselines or metrics
- open pull requests or issues that direct experimental design
- push to any sibling repository

`tools/reconcile.py` issues HTTP GET requests only and refuses any endpoint
outside `repos/`. This is enforced in code, not by convention.

The reason is not politeness. A programme-level document that can rewrite an
experiment's protocol can rewrite it *toward the programme's thesis*, and the
preregistrations become worthless. The separation is what makes the sibling
prereg claims meaningful.

## What reconciliation may do

- record observed remote state (head, push time, visibility, results presence)
- detect drift between the registry and reality
- flag terminology divergence
- flag when a sibling's stated evidence status disagrees with the ledger
- **raise a question** in a reconciliation report

Raising a question is the strongest available action. If a sibling repository
appears to have a methodological problem, the reconciliation report says so; the
fix happens in that repository, by its own process.

## Cadence

Reconcile when any of these occur:

- a sibling repository is created, renamed, archived, or made public/private
- a sibling's `results/` becomes populated — **a possible readout**
- a preregistration is committed or amended
- a paper draft begins
- any claim status is proposed for change
- otherwise, periodically; the last date is recorded in `ledger/repos.json`

## Procedure

```bash
python3 tools/reconcile.py          # report drift, non-zero exit if drift found
python3 tools/reconcile.py --write  # refresh observed blocks after review
python3 tools/validate_ledger.py    # re-check invariants
python3 tools/render.py             # regenerate the human-readable views
```

Then write a dated report in [`reconciliation/`](reconciliation/) recording what
changed, what was decided, and what remains open.

## Readout handling

When a sibling's `results/` becomes populated, reconciliation must **not**
immediately update claim statuses. The order is:

1. Confirm the run was confirmatory, not a pilot.
2. Check it against the admissibility rules in
   [EVIDENCE-MAP.md](EVIDENCE-MAP.md#inherited-admissibility-rules).
3. Confirm the protocol was frozen before confirmatory seeds were touched.
4. Only then add an `evidence` entry and propose a status change.
5. Re-run the validator, which will reject a status asserting support without
   admissible evidence.

A populated `results/` directory is a signal to look, not permission to claim.

## Divergence that must be recorded, not fixed

If a sibling repository:

- uses different terminology → record the mapping in [TERMINOLOGY.md](TERMINOLOGY.md)
- departs from an inherited admissibility rule → record it in EVIDENCE-MAP.md and
  mark affected claims `unresolved`
- implements a component owned by another repository → record as programme drift
  and flag the ownership conflict
- states an evidence status stronger than the ledger supports → record the
  disagreement in the reconciliation report

In every case the umbrella records the divergence. The sibling decides what to do
about it.
