# Paper roadmap

What could be written, when, and what each paper may and may not claim.

Ordering is by evidence, not by ambition. Every paper here is conditional; none is
in progress.

## P1 — Component paper: evidence-gated consolidation

- **Host:** `state-promotion`
- **Requires:** Synthesis-readiness Tier 1
- **Status:** not writable — no confirmatory results exist
- **May claim:** that evidence-gated commitment does or does not improve the
  stability–plasticity trade-off on a synthetic continual stream, under stated
  budget controls, at 0.5B scale
- **May not claim:** anything about substrates, agents, cognition, allocation, or
  lifetime coherence
- **Publishable if H1 fails:** yes, and it should be. A clean negative result on a
  well-controlled preregistered comparison is the more useful paper, given that
  Memoir's related negative result is already in the literature.

## P2 — External validity extension

- **Host:** `state-promotion`
- **Requires:** Tier 1 + Tier 2 (EXP-002 on CITB/TRACE, EXP-003 at ~7B)
- **Status:** not writable
- **May claim:** that the P1 effect transfers, or does not, to established
  benchmarks and larger scale
- **May not claim:** general continual-learning capability. Scale results are
  replication evidence and do not substitute for small-model ablations.

## P3 — Allocation paper

- **Host:** `plasticity-routing` *(repository not created)*
- **Requires:** Tier 1, plus a design that holds commit count fixed while varying
  placement
- **Status:** not writable, not designed, no repository
- **May claim:** that allocation is or is not a lever separable from commitment
- **Note:** a negative result here is disproportionately valuable, because it
  would collapse the programme's three-operator framing to two operators. That is
  a finding about the decomposition, and should be reported as one.

## P4 — Long-horizon integrity paper

- **Host:** `lifetime-integrity` *(repository not created)*
- **Requires:** Tier 1 + Tier 3, and stream lengths no current experiment reaches
- **Status:** not writable, not designed, no repository
- **May claim:** measured drift, staleness and commitment-error behaviour over
  long lifetimes
- **Note:** the claim this paper would test (CCS-C7) is the one most likely to be
  assumed rather than measured elsewhere in the programme.

## P5 — Modular consolidation paper

- **Host:** `modular-consolidation` *(repository not created)*
- **Requires:** Tier 1, plus equal-total-capacity controls
- **Status:** not writable, not designed, no repository

## P6 — Adaptive commitment paper

- **Host:** `adaptive-commitment` *(repository not created)*
- **Requires:** Tier 1, and only worth running if CCS-C2 survives
- **Status:** not writable, not designed, no repository

## P7 — Synthesis paper

> *Consolidating Cognitive Substrate: Toward Multi-Timescale Coherent Continual Agents*

- **Host:** this repository (theory and synthesis only; the integration experiment
  needs its own repository)
- **Requires:** **all four tiers**, including a completed `ccs/EXP-I1`
- **Status:** **not writable, and not close.** Zero tiers cleared.
- **May claim:** only what the component papers established, plus a measured
  composition effect
- **May not claim:** that ACCUMULATE → ALLOCATE → COMMIT is a discovered structure
  rather than an organising conjecture that survived testing

**The title is recorded here as an intention. Its Results section does not exist,
will not be drafted speculatively, and is not a placeholder.** If the programme
reaches a point where P7 is tempting but Tier 4 is not cleared, the correct output
is the "minimum defensible paper" for the evidence actually available — see
[SYNTHESIS-READINESS.md](SYNTHESIS-READINESS.md#the-minimum-defensible-paper-at-each-stage).

## Ordering constraint

P1 gates everything. Until it reads out, no other paper on this list can be
designed against a tested premise, and drafting P7 in any form would be writing
conclusions before evidence.
