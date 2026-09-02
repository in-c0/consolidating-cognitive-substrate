# Consolidating Cognitive Substrate (CCS)

**Programme-level umbrella for a research programme on multi-timescale continual
agents.** Theory, terminology, claim ledger, experiment dependency graph, and
evidence status.

> ## Status: no claim in this programme has empirical support.
>
> As of 2026-09-02: one of five sibling repositories exists, it has no
> confirmatory results, and its only pilot returned a null result on the central
> mechanism. **0 of 4 synthesis-readiness tiers are cleared.**
>
> This repository exists to keep that fact visible.

## What this repository is

A thin coordination layer. It maintains:

- the [architecture hypothesis](docs/ARCHITECTURE-HYPOTHESIS.md) — explicitly a conjecture
- [component definitions](docs/COMPONENTS.md) and [terminology](docs/TERMINOLOGY.md)
- the [claim ledger](docs/CLAIM-LEDGER.md) — every claim, its evidence status, its falsifier
- the [evidence map](docs/EVIDENCE-MAP.md) — claim ↔ experiment, in both directions
- the [experiment dependency DAG](docs/DEPENDENCY-DAG.md)
- the [paper roadmap](docs/PAPER-ROADMAP.md), [novelty boundaries](docs/NOVELTY-BOUNDARIES.md),
  [integration criteria](docs/INTEGRATION-CRITERIA.md), [failure criteria](docs/FAILURE-CRITERIA.md)
- [synthesis readiness](docs/SYNTHESIS-READINESS.md) — what must be true before a synthesis paper is defensible

## What this repository is NOT

- **Not an experiment implementation repository.** No models, no training code, no
  runs. Experiments live in sibling repositories and stay there.
- **Not a place where untested architecture is described as results.** The
  decomposition below is a conjecture. `tools/validate_ledger.py` scans committed
  prose for result language as a tripwire.
- **Not a controller of sibling protocols.** Reconciliation is read-only by
  construction. See [RECONCILIATION-POLICY.md](docs/RECONCILIATION-POLICY.md).

## The conjecture under investigation

```text
ACCUMULATE  ──▶  ALLOCATE  ──▶  COMMIT
 retain          decide          decide whether
 candidate       where           and when a change
 experience      capacity        becomes durable
                 is assigned
```

…with state maintained at multiple timescales: ephemeral, latent, fast
parametric, slow parametric, over a frozen foundation.

**This is an organising conjecture, not a finding.** It is written down so it can
be attacked. Three specific ways it may be wrong — including the live possibility
that ALLOCATE is not separable from COMMIT — are in
[ARCHITECTURE-HYPOTHESIS.md](docs/ARCHITECTURE-HYPOTHESIS.md).

## Programme repositories

| Repository | Operator | Exists | Owns claims |
|---|---|---|---|
| [`in-c0/state-promotion`](https://github.com/in-c0/state-promotion) | COMMIT | ✅ | CCS-C2, C3, C10 |
| `in-c0/adaptive-commitment` | COMMIT policy | ❌ planned | CCS-C5 |
| `in-c0/plasticity-routing` | ALLOCATE | ❌ planned | CCS-C4 |
| `in-c0/modular-consolidation` | slow-state structure | ❌ planned | CCS-C6 |
| `in-c0/lifetime-integrity` | ACCUMULATE / long horizon | ❌ planned | CCS-C7 |

`modular-consolidation` and `lifetime-integrity` were reported as existing on
2026-09-02 but were not found; see
[the reconciliation report](docs/reconciliation/2026-09-02.md).

## Claim status

| Status | Count |
|---|---:|
| `theoretical-conjecture` | 6 |
| `unresolved` | 4 |
| `pilot-supported` | 0 |
| `confirmatory-supported` | **0** |
| `falsified` | 0 |

Five of ten claims have **no runnable test anywhere**, because their repositories
do not exist. Full table: [docs/CLAIM-LEDGER.md](docs/CLAIM-LEDGER.md).

## The eventual synthesis paper

The programme's endpoint might be titled something like *Consolidating Cognitive
Substrate: Toward Multi-Timescale Coherent Continual Agents*.

**Its Results section will not be written until the evidence exists**, and this
repository will not host speculative drafts of it. The gates are in
[SYNTHESIS-READINESS.md](docs/SYNTHESIS-READINESS.md); none are cleared. What is
honestly publishable at each stage short of synthesis is tabulated there too.

## Local gates

No CI. No GitHub Actions. Run locally:

```bash
make check
```

| Command | Does |
|---|---|
| `make validate` | Ledger invariants: falsifiers present, evidence backs every supported status, DAG acyclic, no result language in prose |
| `make reconcile` | Read-only drift check against sibling repositories |
| `make render` | Regenerate the ledger and DAG views from JSON |
| `make check` | validate + render + confirm the rendered views are current |

Python 3 standard library only, by design.

## Source of truth

Machine-readable, under [`ledger/`](ledger/):

- [`claims.json`](ledger/claims.json) — the claim ledger
- [`repos.json`](ledger/repos.json) — sibling registry and observed state
- [`dag.json`](ledger/dag.json) — experiment dependency graph

Markdown tables in `docs/` are generated from these. Edit the JSON, then
`make render`.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [WRITING-RULES.md](WRITING-RULES.md).
The short version: a claim's status may only rise when a committed artefact in a
sibling repository supports it, and never because something was implemented,
looks promising, or is needed for a deadline.

## License

Apache-2.0, matching the sibling repositories.
