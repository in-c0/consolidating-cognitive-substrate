# Consolidating Cognitive Substrate (CCS)

**Programme-level umbrella for a research programme on multi-timescale continual
agents.** Theory, terminology, claim ledger, experiment dependency graph, and
evidence status.

> ## Status: no claim in this programme has empirical support.
>
> Reconciled 2026-09-04. **The programme has its first admissible confirmatory
> result**: `plasticity-routing/EXP-001` passed every preregistered gate on five
> held-out seeds. It supports CCS-C4 **partially** — allocation *content* matters
> under matched budgets — and does not establish CCS-C4's separability statement,
> because the experiment contains no independently manipulable COMMIT_INTERNAL
> policy to hold fixed.
>
> **CCS-C4 stays `unresolved`, and was not narrowed to fit the result.** No claim
> has empirical support. **0 of 4 synthesis-readiness tiers are cleared.**
>
> A component result is not evidence that the decomposition composes. This
> repository exists to keep that distinction visible.

## What this repository is

A thin coordination layer. It maintains:

- the [architecture hypothesis](docs/ARCHITECTURE-HYPOTHESIS.md) — explicitly a conjecture
- [component definitions](docs/COMPONENTS.md) and [terminology](docs/TERMINOLOGY.md)
- the [claim ledger](docs/CLAIM-LEDGER.md) — every claim, its evidence status, its falsifier
- the [resource envelope](docs/RESOURCE-ENVELOPE.md) — the common accounting the integration experiment needs before it can be stated
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
ACCUMULATE  ──▶  ALLOCATE  ──▶  COMMIT_INTERNAL
 retain          decide          decide whether and when
 candidate       where           a change to durable
 experience      capacity        state is made
                 is assigned

        ————— a separate commitment domain —————

                 COMMIT_EXTERNAL
                 decide whether and when cognition is
                 released outward: WAIT / THINK / ASK
                 / RESPOND / ACT
```

…with state maintained at multiple timescales: ephemeral, latent, fast
parametric, slow parametric, over a frozen foundation.

**This is an organising conjecture, not a finding.** It is written down so it can
be attacked. Four specific ways it may be wrong — including the live possibility
that ALLOCATE is not separable from COMMIT_INTERNAL — are in
[ARCHITECTURE-HYPOTHESIS.md](docs/ARCHITECTURE-HYPOTHESIS.md).

**COMMIT was split on 2026-09-03.** One word had been covering two decisions —
making state durable, and releasing an utterance — which presupposed that a single
mechanism governs both. That is now an explicit claim with four falsifiers
([CCS-C12](docs/CLAIM-LEDGER.md)), not a naming convention. Whether
COMMIT_EXTERNAL belongs in the pipeline above is unresolved.

## Programme repositories

| Repository | Operator | Exists | Owns claims | Best result on file |
|---|---|---|---|---|
| [`in-c0/state-promotion`](https://github.com/in-c0/state-promotion) | COMMIT_INTERNAL | ✅ | CCS-C2, C3, C5, C10 | engineering pilot, null on the mechanism |
| [`in-c0/plasticity-routing`](https://github.com/in-c0/plasticity-routing) | ALLOCATE | ✅ | CCS-C4 | **confirmatory complete, H1 supported** — partial support only |
| [`in-c0/modular-consolidation`](https://github.com/in-c0/modular-consolidation) | COMMIT_INTERNAL target structure | ✅ | CCS-C6, C11 | preregistered frozen grid, development seeds |
| [`in-c0/lifetime-integrity`](https://github.com/in-c0/lifetime-integrity) | ACCUMULATE / long horizon | ✅ | CCS-C7 | single-seed pilot, non-evidential |
| `in-c0/adaptive-commitment` | COMMIT_EXTERNAL | ❌ planned | *(none yet)* | — |

Each existing track declares its own results non-evidential and declares that
they do not travel to other tracks. The umbrella honours those declarations: see
[the live reconciliation](docs/reconciliation/2026-09-02-live.md).

## Claim status

| Status | Count |
|---|---:|
| `theoretical-conjecture` | 4 |
| `unresolved` | 9 |
| `pilot-supported` | 0 |
| `confirmatory-supported` | **0** |
| `falsified` | 0 |

Ten evidence entries are on file; **one is admissible, and it is partial-scope**.
Three of thirteen claims have no runnable test: CCS-C5, CCS-C8 and CCS-C12 — the
last two because their experiments have no host repository, deliberately.

The ledger distinguishes **full** from **partial** evidence scope. A partial entry
records what it establishes *and* what it leaves open, so an admissible component
result can be logged without narrowing the claim to fit it. The validator refuses
a full-scope supporting admissible entry on an unpromoted claim, and requires a
`held_back_reason` whenever admissible evidence does not promote. Full table:
[docs/CLAIM-LEDGER.md](docs/CLAIM-LEDGER.md).

Two claims are worth reading before the rest. **CCS-C6** carries two
against-direction development results and should be expected to end at
`falsified`; its live successor is **CCS-C11**, added rather than substituted so
the original is not quietly rewritten to follow the evidence.

**CCS-C11 is now itself under pressure.** A preregistered frozen-grid run found
that pooling beats refusing-to-admit only above a threshold in *absolute skill
count*, and that its advantage grows as the ceiling **loosens** — the opposite of
the claim's motivating intuition, which pointed at high pressure. The claim has
not been rewritten; the tension is recorded on it, and the successor mechanism
was **added** as **CCS-C13** (consolidation needs pressure *and* candidate
diversity) rather than substituted.

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
- [`resource_envelope.json`](ledger/resource_envelope.json) — cross-track resource accounting

Markdown tables in `docs/` are generated from these. Edit the JSON, then
`make render`.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [WRITING-RULES.md](WRITING-RULES.md).
The short version: a claim's status may only rise when a committed artefact in a
sibling repository supports it, and never because something was implemented,
looks promising, or is needed for a deadline.

## License

Apache-2.0, matching the sibling repositories.
