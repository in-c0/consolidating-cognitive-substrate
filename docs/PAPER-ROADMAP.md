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

- **Host:** `plasticity-routing`
- **Requires:** Tier 1, plus a design that holds write budget fixed while varying
  placement — which that track has built
- **Status:** not writable. EXP-001 is preregistered and has not read out.
- **May claim:** that allocation is or is not a lever separable from commitment
- **Note:** a negative result here is disproportionately valuable, because it
  would collapse the programme's three-operator framing to two operators. That is
  a finding about the decomposition, and should be reported as one.
- **Live expectation:** that track sets a deliberately low prior on its learned
  router beating a calibrated fixed rule, and its development calibration already
  fired K1 against the method. A negative replication of Yoon (2026) is its
  preregistered publishable outcome. Note carefully that this would *not* falsify
  CCS-C4: allocation being a separable lever and the allocation policy being
  *learned* are different claims, and only the second is at stake in K1.

## P4 — Long-horizon integrity paper

- **Host:** `lifetime-integrity`
- **Requires:** Tier 1 + Tier 3
- **Status:** not writable. EXP-A001 and EXP-B001 are preregistered; the only run
  is a single-seed pilot marked NOT EVIDENCE.
- **May claim:** measured drift, staleness and re-grounding cost over long
  lifetimes, **for whatever substrate was scored** — that track is
  architecture-agnostic and forbids its results being read as validating a CCS
  latent architecture.
- **Note:** this paper is separable from the CCS programme and its track intends
  it to remain useful if the programme goes nowhere. Under P7 it is a component;
  on its own it is a benchmark paper.

## P5 — Modular consolidation: methods/attribution paper

- **Host:** `modular-consolidation`
- **Requires:** the control lattice applied to published methods; **not** a new
  policy and **not** Tier 1
- **Status:** not writable. EXP-100 is an explicit DRAFT, NOT FROZEN, and blocked
  until `plasticity-routing` freezes or exports the shared LM substrate.
- **May claim:** whether published modular continual-learning gains survive
  capacity- and compute-matched attribution
- **Note:** that track has made this its *primary* near-term output, ahead of any
  architecture paper, and its thesis is falsifiable in the useful direction — if
  published gains do survive the controls, the paper becomes a validation of the
  field's evaluation practice rather than a critique. It is the one paper on this
  roadmap that does not depend on the CCS conjecture being correct.

## P6 — External commitment paper

- **Host:** `adaptive-commitment` *(repository not created)*
- **Requires:** its own literature audit and preregistration first
- **Status:** not writable, not designed, no repository
- **May claim:** whether a policy over `WAIT` / `THINK` / `ASK` / `RESPOND` /
  `ACT` beats fixed or threshold-based release timing, under a stated exchange
  rate between accuracy, latency, intervention cost and consequence
- **Scope corrected 2026-09-03:** this paper was previously listed as being about
  adaptive *consolidation* thresholds. It is not. That idea survives as a
  `state-promotion` follow-on (CCS-C5) and must not be cited as this track's
  motivation.
- **Not gated on P1.** COMMIT_EXTERNAL was deliberately scoped as a separate
  domain, so unlike P3–P5 this paper does not wait on `state-promotion/EXP-001`.
  It is the one component paper that could, in principle, be written first.
- **The hard part is the objective, not the policy.** Trading a wrong answer
  against a slow one against an unnecessary question requires an exchange rate
  between quantities borne by different parties. That is open problem OP-1 in
  [RESOURCE-ENVELOPE.md](RESOURCE-ENVELOPE.md), and it is prior to any result.

## P6b — Unification paper *(conditional, hypothetical)*

- **Host:** none. `ccs/EXP-U1` has no repository and no design.
- **Requires:** admissible mechanisms in **both** commitment domains, plus a
  resolved exchange rate between their cost structures
- **Status:** not writable. CCS-C12 is a `theoretical-conjecture` with zero
  implementation — no track implements both domains, so no track can test it.
- **May claim:** that one learned mechanism governs both COMMIT_INTERNAL and
  COMMIT_EXTERNAL at least as well as two specialised ones
- **Note:** this paper exists on the roadmap only because the programme's old
  vocabulary asserted its conclusion for free. Making it a claim made it a paper
  that has to be earned. It may well be unwritable: if the two cost structures
  are incommensurable, the comparison cannot be posed at all.

## P7 — Synthesis paper

> *Consolidating Cognitive Substrate: Toward Multi-Timescale Coherent Continual Agents*

- **Host:** this repository (theory and synthesis only; the integration experiment
  needs its own repository)
- **Requires:** **all four tiers**, including a completed `ccs/EXP-I1`
- **Status:** **not writable, and not close.** Zero tiers cleared.
- **May claim:** only what the component papers established, plus a measured
  composition effect
- **May not claim:** that ACCUMULATE → ALLOCATE → COMMIT_INTERNAL is a discovered
  structure rather than an organising conjecture that survived testing; nor that
  the two commitment domains are unified, unless CCS-C12 was actually tested

**The title is recorded here as an intention. Its Results section does not exist,
will not be drafted speculatively, and is not a placeholder.** If the programme
reaches a point where P7 is tempting but Tier 4 is not cleared, the correct output
is the "minimum defensible paper" for the evidence actually available — see
[SYNTHESIS-READINESS.md](SYNTHESIS-READINESS.md#the-minimum-defensible-paper-at-each-stage).

## Ordering constraint

P1 gates everything. Until it reads out, no other paper on this list can be
designed against a tested premise, and drafting P7 in any form would be writing
conclusions before evidence.
