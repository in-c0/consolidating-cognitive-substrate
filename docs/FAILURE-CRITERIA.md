# Failure criteria

What would make this programme wrong, and what should happen then.

Written now, while nothing has read out, so that a later result cannot be
reinterpreted into a success. A programme that cannot describe its own failure in
advance is not testing anything.

## Programme-level failure

The CCS framing should be **abandoned or fundamentally revised** if:

**F1 — The central mechanism does not work.**
`state-promotion/EXP-001` H1 is falsified under valid, budget-matched conditions:
evidence-gated promotion fails to beat sequential adaptation and fixed-schedule
consolidation. COMMIT_INTERNAL is the programme's most developed idea. If it
fails cleanly, the rest is unmotivated in this framing — with one exception:
`adaptive-commitment` (COMMIT_EXTERNAL) is a separate domain and would survive
F1 intact.

**F2 — Gains are artefacts.**
Any apparent advantage is explained by unequal parameter writes, leaked task
identity, ceiling effects, a single task ordering, or unaccounted decision-time
compute. This is a worse outcome than F1, because it means the programme's
controls failed rather than its hypothesis.

**F3 — The advantage is routing-count, not routing-policy.**
The promotion arm's advantage disappears against the B4 random-routing control
matched on commit count. This falsifies the *specific* claim that evidence-gating
matters, while leaving multi-timescale structure intact — a partial failure that
would demand a narrower programme, not a broader one.

**F4 — The decomposition does not decompose.**
ALLOCATE cannot be varied independently of COMMIT_INTERNAL, or allocation effects
reduce entirely to commit frequency. The three-operator framing collapses to two, and
[ARCHITECTURE-HYPOTHESIS.md](ARCHITECTURE-HYPOTHESIS.md) must be rewritten rather
than annotated.

**F5 — The overhead eats the gain.**
Decision-time gating compute is large enough that a compute-augmented baseline
given the same total budget matches the gated method. The mechanism would then be
real but not worth its cost, which is a negative result about the *system*, and
must be reported as one.

**F6 — Nothing survives contact with real benchmarks.**
Effects hold on PALS but vanish on CITB/TRACE. The programme would have a result
about a synthetic stream, and must say only that.

**F7 — Long horizons defeat it.**
Coherence degrades without bound as lifetime grows, or is maintainable only by
periodic full resets. A substrate that must be reset does not accumulate, and the
programme's name would be wrong.

## Component-level failure does not equal programme failure

A single component failing is normal and publishable. The distinction:

| Outcome | Programme response |
|---|---|
| One component falsified, others hold | Record `falsified` in the ledger, publish it, narrow the synthesis scope |
| Central COMMIT_INTERNAL claim falsified (F1) | State-pipeline framing abandoned or fundamentally revised; COMMIT_EXTERNAL unaffected |
| Controls failed (F2) | Halt readouts, fix controls, re-run. **Do not report.** |
| Component works but does not compose (I3) | Report components separately. No synthesis paper. |

## What must not happen

These are the failure modes of the *programme*, not of the science:

1. **Reclassifying a falsified claim as "unresolved"** to keep it alive. Falsified
   entries stay in the ledger permanently, with their evidence.
2. **Moving the goalposts after a readout.** Any post-lock change to a hypothesis
   creates a new protocol version, and prior runs are not evidence for it.
3. **Substituting a working component for a failed one** and describing the
   programme as on track.
4. **Writing the synthesis paper anyway** with hedged language. See
   [SYNTHESIS-READINESS.md](SYNTHESIS-READINESS.md).
5. **Letting this repository accumulate architectural description** that outpaces
   evidence. `tools/validate_ledger.py` scans committed prose for result language
   as a coarse tripwire against exactly this.
6. **Quietly dropping a falsifier** from `ledger/claims.json`. The validator
   rejects any claim with no falsifier.

## Live failure watch — 2026-09-02

Two criteria have development-level signals pointing at them. Neither has fired,
because neither has admissible evidence behind it, and recording them here is not
the same as conceding them.

**F4 (the decomposition does not decompose)** — the vocabulary half of this was
resolved on 2026-09-03 by splitting COMMIT_INTERNAL from COMMIT_EXTERNAL:
`plasticity-routing`'s `SLOW` write is a COMMIT_INTERNAL action reached by an
ALLOCATE decision, and the "commitment in the CCS sense" it declines to model is
COMMIT_EXTERNAL. See [TERMINOLOGY.md](TERMINOLOGY.md#resolved-divergence--commit).

The substantive half is untouched. Renaming does not make ALLOCATE and
COMMIT_INTERNAL separable, and CCS-C4 still has to settle it. A second instance of
the same hazard is now visible and unresolved: ACCUMULATE is read as "retain
candidate experience" here and as "continue gathering / thinking" by
`plasticity-routing`, which are plausibly different operators. It has not been
split, because no track has operationalised either reading.

**F8 — the operators cannot be compared at all.** New as of 2026-09-03, and
distinct from F1–F7 because it is a measurement failure rather than a hypothesis
failure. If internal and external commitment costs have no non-arbitrary exchange
rate, then CCS-C12 and CCS-C8 cannot be *posed*, regardless of how well any
individual mechanism works. A programme can fail by being wrong; it can also fail
by asking a question that has no measurable form. Tracked as OP-1 in
[RESOURCE-ENVELOPE.md](RESOURCE-ENVELOPE.md) and machine-enforced: while any
incommensurable dimension is open, both `ccs` nodes are pinned at
`not-designed`.

**An unanticipated failure mode — consolidation may have nothing to fix.**
`modular-consolidation`'s development simulator finds retention versus capacity
monotone non-decreasing under competent routing, which would make consolidation a
compression mechanism rather than a forgetting mechanism in the unbounded regime.
The original failure criteria did not anticipate this: F1 through F7 all assume
the mechanisms matter and ask whether they *work*. This asks whether one of them
has a job. It is now tracked as CCS-C6 against CCS-C11, and if it holds for real
models the programme's name overstates what the programme does.

**F9 — a preregistered criterion turns out to be unsatisfiable.** New as of
2026-09-03, observed in `modular-consolidation`'s EXP-003, where the strict
reading of the predeclared Pareto rule required dominating an arm that maximises
plasticity by construction. This is a failure of the *protocol*, not of the
hypothesis, and it is the most dangerous kind for a programme that leans on
preregistration: it is invisible until results arrive, and at that point every
available response looks like moving the goalposts.

The programme's answer is prevention, not adjudication — see admissibility rule
13 in [EVIDENCE-MAP.md](EVIDENCE-MAP.md#added-2026-09-03). When it does happen,
the honest handling is what that track did: report both readings, compute both
over the complete grid, decline to choose unilaterally, and escalate the choice
to the owner. The umbrella records the open decision and does not resolve it.

## Publication obligation on failure

Inherited from `state-promotion`: negative results are published. If H1 is
falsified under valid conditions, the negative result is written up and the
programme proceeds only with a revised hypothesis that is clearly marked
post-hoc.

A programme that publishes only its successes has not been running experiments.
