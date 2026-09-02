# Contributing

## Scope

This repository holds theory, terminology, claim status, and cross-repository
coordination. If a change involves a model, a training run, a metric
implementation, or an experimental protocol, it belongs in a sibling repository.

Pull requests that add experiment code here will be declined regardless of
quality. The umbrella must stay thin, or it becomes a place where architecture
gets described as working.

## Before you commit

```bash
make check
```

This validates the ledger invariants, confirms the rendered views match the JSON,
and scans prose for result language.

## Changing a claim's status

The only legitimate reason is a committed artefact in a sibling repository.

1. Add an `evidence` entry to `ledger/claims.json` with `repo`, `artefact`,
   `class` (`pilot`/`confirmatory`), `admissible`, and a factual `summary`.
2. Check the artefact against the admissibility rules in
   [EVIDENCE-MAP.md](docs/EVIDENCE-MAP.md#inherited-admissibility-rules).
3. Update `status`. Leave `implementation` alone unless the code changed — they
   are separate axes.
4. `make check`. The validator rejects a status asserting support without
   admissible evidence, and rejects evidence cited from a repository that does
   not exist.
5. Record the change in `docs/reconciliation/<date>.md`.

**Never raise a status because:** something was implemented; a result looks
promising; a pilot pointed the right way but was inadmissible; a paper deadline is
near; or the claim is needed by another claim.

**Never lower a `falsified` status to `unresolved`.** Falsified entries are
permanent, with their evidence attached.

## Adding a claim

Every claim needs a one-sentence falsifiable `statement`, at least one entry in
`falsified_by`, at least one DAG node in `supported_by`, and a `review_by`
trigger. The validator enforces all four.

If you cannot name what would kill a claim, it is not yet a claim.

## Adding a repository to the programme

1. Add it to `ledger/repos.json` with `existence`, `role`, owned components and
   owned claims.
2. Add its experiment nodes to `ledger/dag.json` with dependency edges.
3. Confirm no component is owned by two repositories.
4. Record the addition in a reconciliation report.

New repositories inherit the admissibility rules in EVIDENCE-MAP.md by default.
A departure must be declared in that repository's own preregistration and
recorded here.

## Writing

See [WRITING-RULES.md](WRITING-RULES.md).

## What this repository will not do to siblings

Reconciliation is read-only by construction (`tools/reconcile.py` refuses
non-read-only endpoints). We do not modify sibling protocols, amend
preregistrations, or open issues directing experimental design from here. The
strongest available action is raising a question in a reconciliation report.

## No CI

Deliberate. Gates run locally via `make check`. Run them before pushing.
