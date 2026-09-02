# Claim ledger

Every programme-level claim, its evidence status, and what would kill it.

**Source of truth is [`ledger/claims.json`](../ledger/claims.json).** The table
below is generated from it by `tools/render.py`. Do not edit the table by hand.

## Status vocabulary

| Status | Means | Requires |
|---|---|---|
| `theoretical-conjecture` | Proposed. Not tested. | A named falsifier. |
| `implemented` | Mechanism exists in code. | Nothing empirical. **Code is not evidence.** |
| `pilot-supported` | A pilot points this way. | ≥1 pilot artefact, explicitly labelled non-confirmatory. |
| `confirmatory-supported` | Survived a preregistered confirmatory test. | ≥1 admissible confirmatory readout under valid conditions. |
| `falsified` | A valid test came out against it. | ≥1 admissible readout. **Recorded, never deleted.** |
| `unresolved` | Actively open: tested inconclusively, or the only pilot was null/degenerate. | — |

Two things this vocabulary deliberately refuses to allow:

- **Implementation is a separate axis from evidence.** A claim can be
  `implemented` and still `theoretical-conjecture`. The `implementation` column
  exists so that building something is never mistaken for learning something.
- **A conjecture is not "supported by absence of refutation."** Six claims below
  are unfalsified only because nothing capable of falsifying them has been run.

## Current state

<!-- GENERATED:claims -- do not edit by hand; run tools/render.py -->

| Claim | Statement (abbreviated) | Status | Implementation | Tested by |
|---|---|---|---|---|
| **CCS-C1** Three-operator decomposition | Continual-agent competence over a lifetime decomposes usefully into ACCUMULATE (retain candidate… | `conjecture` | partial | `state-promotion/EXP-001`, `plasticity-routing/EXP-P1`, `adaptive-commitment/EXP-A1` |
| **CCS-C2** Evidence-gated commitment beats scheduled commitment | Under matched trainable-parameter capacity, replay budget, online-token budget and parameter-write… | `unresolved` | implemented | `state-promotion/EXP-001`, `state-promotion/EXP-002`, `state-promotion/EXP-003` |
| **CCS-C3** Persistent latent state carries context-dependent exceptions | A bounded persistent latent state carried across stream items contributes specifically to handling… | `unresolved` | implemented | `state-promotion/EXP-001` |
| **CCS-C4** Allocation is a separable lever from commitment | Where an experience is routed within the substrate affects the stability-plasticity trade-off… | `conjecture` | none | `plasticity-routing/EXP-P1` |
| **CCS-C5** Adaptive commitment thresholds beat fixed thresholds | A commitment criterion that adapts to observed stream statistics outperforms a well-tuned constant… | `conjecture` | none | `adaptive-commitment/EXP-A1` |
| **CCS-C6** Modular slow state reduces interference | Consolidating durable knowledge into separable modules produces less cross-task interference than… | `conjecture` | none | `modular-consolidation/EXP-M1` |
| **CCS-C7** Lifetime coherence is maintainable | A multi-timescale substrate can be operated over lifetimes far longer than any single experiment stream… | `conjecture` | none | `lifetime-integrity/EXP-L1` |
| **CCS-C8** The components compose | A system combining accumulation, allocation and commitment outperforms the best single-component system… | `conjecture` | none | `ccs/EXP-I1` |
| **CCS-C9** Multiple timescales are necessary, not merely sufficient | A single-timescale controller given the same total capacity, write budget and compute cannot match a… | `unresolved` | partial | `state-promotion/EXP-001`, `plasticity-routing/EXP-P1` |
| **CCS-C10** Gating overhead does not erase the gain | The decision-time inference cost of evidence gating is small enough that the method retains its advantage… | `unresolved` | implemented | `state-promotion/EXP-001` |

**10 claims. 0 with empirical support. 0 confirmatory.**

<!-- /GENERATED:claims -->

## Reading this table honestly

As of 2026-09-02, **no claim in this programme has empirical support.** The single
pilot that has run ([EXP-000](https://github.com/in-c0/state-promotion/blob/main/experiments/EXP-000-RESULT.md))
returned a null result on the central mechanism, and its own repository classifies
it as engineering validation that is not paper evidence.

That is the expected state of a programme at this stage. It stops being expected
if it is still true after `state-promotion/EXP-001` reads out.

## Per-claim detail

Full statements, evidence entries, falsifiers and review triggers are in
[`ledger/claims.json`](../ledger/claims.json). Each claim carries:

- `statement` — the claim in one falsifiable sentence
- `status` / `implementation` — the two axes above
- `evidence[]` — artefact, class (`pilot`/`confirmatory`), admissibility, direction
- `supported_by[]` — DAG nodes able to test it
- `falsified_by[]` — concrete outcomes that would kill it
- `review_by` — the event that forces a status re-review

## Changing a status

1. Point at a committed artefact in a sibling repository. A conversation, a
   plan, or a passing test suite is not an artefact.
2. Add an `evidence` entry recording its class and admissibility.
3. Run `python3 tools/validate_ledger.py`. It refuses statuses that assert
   support without admissible evidence, and refuses evidence cited from
   repositories that do not exist.
4. Run `python3 tools/render.py` to regenerate this page.
5. Record the change in [`reconciliation/`](reconciliation/) with the date and the
   artefact.

A status may never be raised because a mechanism was implemented, because a
result "looks promising", or because a deadline is near.
