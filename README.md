# Consolidating Cognitive Substrate (CCS)

**Programme-level umbrella for a research programme on multi-timescale continual
agents.** Theory, terminology, claim ledger, experiment dependency graph, and
evidence status.

> ## Status: no claim in this programme has empirical support.
>
> Reconciled 2026-09-02 against live GitHub state. **Four of five** sibling
> repositories now exist and three carry substantial development results — and
> **0 of 11 claims** have admissible evidence, because every result on file is a
> development calibration or an engineering pilot that its own track classifies
> as non-evidential. **0 of 4 synthesis-readiness tiers are cleared.**
>
> Repositories existing is not progress toward a claim. This repository exists to
> keep that distinction visible.

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

| Repository | Operator | Exists | Owns claims | Best result on file |
|---|---|---|---|---|
| [`in-c0/state-promotion`](https://github.com/in-c0/state-promotion) | COMMIT | ✅ | CCS-C2, C3, C10 | engineering pilot, null on the mechanism |
| [`in-c0/plasticity-routing`](https://github.com/in-c0/plasticity-routing) | ALLOCATE | ✅ | CCS-C4 | development calibration, `DEV_CALIBRATION` |
| [`in-c0/modular-consolidation`](https://github.com/in-c0/modular-consolidation) | slow-state structure | ✅ | CCS-C6, C11 | development simulator, synthetic |
| [`in-c0/lifetime-integrity`](https://github.com/in-c0/lifetime-integrity) | ACCUMULATE / long horizon | ✅ | CCS-C7 | single-seed pilot, non-evidential |
| `in-c0/adaptive-commitment` | COMMIT policy | ❌ planned | CCS-C5 | — |

Each existing track declares its own results non-evidential and declares that
they do not travel to other tracks. The umbrella honours those declarations: see
[the live reconciliation](docs/reconciliation/2026-09-02-live.md).

## Claim status

| Status | Count |
|---|---:|
| `theoretical-conjecture` | 3 |
| `unresolved` | 8 |
| `pilot-supported` | 0 |
| `confirmatory-supported` | **0** |
| `falsified` | 0 |

Six evidence entries are on file and **none is admissible**. Two of eleven claims
have no runnable test: CCS-C5 (`adaptive-commitment` does not exist) and CCS-C8
(no integration repository, deliberately). Full table:
[docs/CLAIM-LEDGER.md](docs/CLAIM-LEDGER.md).

Two claims are worth reading before the rest. **CCS-C6** carries two
against-direction development results and should be expected to end at
`falsified`; its live successor is **CCS-C11**, added rather than substituted so
the original is not quietly rewritten to follow the evidence.

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
