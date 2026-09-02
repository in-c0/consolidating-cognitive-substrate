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
consolidation. The COMMIT operator is the programme's most developed idea. If it
fails cleanly, the rest is unmotivated in this framing.

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
ALLOCATE cannot be varied independently of COMMIT, or allocation effects reduce
entirely to commit frequency. The three-operator framing collapses to two, and
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
| Central COMMIT claim falsified (F1) | Programme framing abandoned or fundamentally revised |
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

## Publication obligation on failure

Inherited from `state-promotion`: negative results are published. If H1 is
falsified under valid conditions, the negative result is written up and the
programme proceeds only with a revised hypothesis that is clearly marked
post-hoc.

A programme that publishes only its successes has not been running experiments.
