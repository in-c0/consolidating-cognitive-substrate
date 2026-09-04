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

| Claim | Domain | Statement (abbreviated) | Status | Implementation | Tested by |
|---|---|---|---|---|---|
| **CCS-C1** Three-operator decomposition | cross-operator | Continual-agent competence over a lifetime decomposes usefully into ACCUMULATE (retain candidate… | `conjecture` | partial | `state-promotion/EXP-001`, `plasticity-routing/EXP-001`, `adaptive-commitment/EXP-A1` |
| **CCS-C2** Evidence-gated commitment beats scheduled commitment | COMMIT_INTERNAL | Under matched trainable-parameter capacity, replay budget, online-token budget and parameter-write… | `unresolved` | implemented | `state-promotion/EXP-001`, `state-promotion/EXP-002`, `state-promotion/EXP-003` |
| **CCS-C3** Persistent latent state carries context-dependent exceptions | COMMIT_INTERNAL | A bounded persistent latent state carried across stream items contributes specifically to handling… | `unresolved` | implemented | `state-promotion/EXP-001` |
| **CCS-C4** Allocation is a separable lever from commitment | ALLOCATE | Where an experience is routed within the substrate affects the stability-plasticity trade-off… | `unresolved` | implemented | `plasticity-routing/EXP-001`, `plasticity-routing/EXP-002` |
| **CCS-C5** Adaptive consolidation thresholds beat fixed thresholds | COMMIT_INTERNAL | For COMMIT_INTERNAL, a consolidation criterion that adapts to observed stream statistics outperforms a… | `conjecture` | none | `state-promotion/EXP-F1` |
| **CCS-C6** Modular slow state reduces interference | COMMIT_INTERNAL | In an unbounded-capacity regime, consolidating durable knowledge into separable modules produces less… | `unresolved` | implemented | `modular-consolidation/EXP-100` |
| **CCS-C7** Lifetime coherence is maintainable | ACCUMULATE | A multi-timescale substrate can be operated over lifetimes far longer than any single experiment stream… | `unresolved` | implemented | `lifetime-integrity/EXP-A001`, `lifetime-integrity/EXP-B001` |
| **CCS-C8** The components compose | cross-operator | A system combining accumulation, allocation and commitment outperforms the best single-component system… | `conjecture` | none | `ccs/EXP-I1` |
| **CCS-C9** Multiple timescales are necessary, not merely sufficient | cross-operator | A single-timescale controller given the same total capacity, write budget and compute cannot match a… | `unresolved` | partial | `state-promotion/EXP-001`, `plasticity-routing/EXP-001` |
| **CCS-C10** Gating overhead does not erase the gain | COMMIT_INTERNAL | The decision-time inference cost of evidence gating is small enough that the method retains its advantage… | `unresolved` | implemented | `state-promotion/EXP-001` |
| **CCS-C11** Under a binding capacity ceiling, pooling beats destroying | COMMIT_INTERNAL | Under a hard capacity ceiling below the number of distinct skills, and at identical live module count,… | `unresolved` | implemented | `modular-consolidation/EXP-003`, `modular-consolidation/EXP-100` |
| **CCS-C12** Internal and external commitment share one mechanism | COMMIT_INTERNAL + COMMIT_EXTERNAL | COMMIT_INTERNAL and COMMIT_EXTERNAL are instances of a single commitment principle: one learned mechanism,… | `conjecture` | none | `ccs/EXP-U1` |
| **CCS-C13** Useful consolidation needs pressure AND candidate diversity | COMMIT_INTERNAL | Consolidation improves the retention-plasticity frontier only when capacity pressure coincides with enough… | `unresolved` | implemented | `modular-consolidation/CANDIDATE-DIVERSITY`, `modular-consolidation/EXP-100` |

**13 claims. 0 with empirical support. 0 confirmatory.**

<!-- /GENERATED:claims -->

## Reading this table honestly

Reconciled 2026-09-02 against live GitHub state. **No claim in this programme has
empirical support.** Six evidence entries are on file and none is admissible:
every one is a development calibration or an engineering pilot that its own track
classifies as non-evidential.

Four claims moved from `theoretical-conjecture` to `unresolved` at this
reconciliation, and one claim was added. **None of that is an evidence
promotion** — both statuses assert zero empirical support. The moves record that
the claims are now implemented and under inconclusive test, which is what the
`implementation` column is for.

Updated 2026-09-03 for the COMMIT split. CCS-C5 was **re-scoped, not promoted**:
it had been attached to `adaptive-commitment` on the mistaken understanding that
that track was about consolidation thresholds. It is now a `state-promotion`
COMMIT_INTERNAL follow-on. CCS-C12 was **added** as the falsifiable home for a
unification the old vocabulary asserted for free. No status moved in either
direction, and CCS-C4, CCS-C6 and CCS-C11 are untouched.

Updated 2026-09-04. **The programme has its first admissible confirmatory
evidence** — `plasticity-routing/EXP-001`, recorded against CCS-C4 with scope
`partial`. CCS-C4 remains `unresolved` and carries a `held_back_reason`: the
experiment establishes that allocation *content* matters under matched budgets,
and contains no independently manipulable COMMIT_INTERNAL policy, so it cannot
settle the separability statement CCS-C4 actually makes. The claim was **not
narrowed post hoc** to match what arrived.

Five entries deserve attention before the rest:

- **CCS-C6** carries two against-direction development results. Its owning track
  records the equivalent track-local claim as falsified. It is held at
  `unresolved` here only because that finding is a synthetic simulator on a
  closed-form ridge learner and that track's own rules forbid its results
  travelling. Expect this one to end at `falsified`.
- **CCS-C11** was *added* rather than substituted for CCS-C6, so that narrowing
  the question to the regime where it survives cannot be mistaken for the
  original claim having held.
- **CCS-C10** now has the quantification it was waiting for, and it is
  unfavourable: `state-promotion`'s engineering pilot measured B5 decision compute
  at **72.4% of total algorithmic compute** — roughly 2.6× more spent deciding
  than adapting. That raises the bar the claim must clear rather than settling it.
- **CCS-C12** has a low prior and is the only claim whose falsifiers include a
  *measurement* failure: if the cost structures of internal and external
  commitment are incommensurable, unification fails even if a shared mechanism is
  buildable. See [RESOURCE-ENVELOPE.md](RESOURCE-ENVELOPE.md).
- **CCS-C7** now has a hard external gate: its owning track forbids any of its
  results being read as validating a CCS latent architecture until
  `state-promotion` establishes an admissible substrate. No quantity of
  long-horizon evidence lifts that on its own.

This is the expected state of a programme at this stage. It stops being expected
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
