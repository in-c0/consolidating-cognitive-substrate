# CCS architecture hypothesis

> **Epistemic status: conjecture.** Nothing on this page has been tested. It is a
> decomposition proposed to organise a research programme, not a description of a
> system that works. It is written down so that it can be attacked.

## The conjecture

A continual agent that stays coherent over a long lifetime must solve three
problems that are usually collapsed into one. The conjecture is that they are
*separable*, and that separating them is what makes the system analysable:

```text
                       ACCUMULATE
              retain candidate experience
        without committing to it prematurely
                            |
                            v
                        ALLOCATE
          decide WHERE capacity is assigned
              (which store, which module)
                            |
                            v
                         COMMIT
        decide WHETHER and WHEN a change becomes
           durable, and be able to undo it
```

Each operator runs at its own characteristic timescale, and state persists at
several timescales simultaneously.

## Why the arrow diagram is misleading

The diagram above is drawn as a pipeline because pipelines are easy to read. The
programme does not assume the pipeline is real. Three specific ways it may be
wrong, each of which a component experiment is meant to expose:

1. **ALLOCATE may not be separable from COMMIT.** If every allocation policy can
   be reduced to "commit more often" or "commit less often", the decomposition is
   two operators wearing three hats. This is [CCS-C4](CLAIM-LEDGER.md)'s falsifier,
   and it is the failure mode the programme should expect to find first.
2. **The order may not be fixed.** Commitment decisions plausibly feed back into
   what is worth accumulating. If the loop is essential, a feed-forward
   decomposition is the wrong shape.
3. **ACCUMULATE may be doing no work.** If a bounded replay reservoir is enough,
   then "accumulation" is a rebranding of replay, and the operator should be
   dropped rather than defended.

## State timescales

The timescale table below is inherited from `state-promotion`, which is the only
repository that has implemented any of it. It is reproduced here as programme
terminology, not as an independent result.

| Level | Lifetime | Update mechanism | Implemented in |
|---|---|---|---|
| Ephemeral | one step / session | ordinary activations and context | `state-promotion` |
| Latent | sessions to days | bounded recurrent state | `state-promotion` |
| Fast parametric | examples to hours | online adapter updates | `state-promotion` |
| Slow parametric | weeks and longer | gated consolidation | `state-promotion` |
| Foundation | frozen | never modified in current experiments | `state-promotion` |

External episodic memory sits alongside this hierarchy rather than inside it: it
stays attributable and inspectable, and the programme does not treat it as
equivalent to latent or parametric state.

## The one structural commitment

If the programme has a single load-bearing idea, it is not multi-timescale
learning, which is prior art (see [NOVELTY-BOUNDARIES.md](NOVELTY-BOUNDARIES.md)).
It is this distinction, taken from `state-promotion`:

> **candidate ≠ committed state**

A gradient being available is a mechanical fact. Whether the system *should*
learn from it is a separate question, and the programme's bet is that making that
question explicit — with a gate, a retention test, and a rollback path — is worth
its cost.

That bet is currently unsupported. The only pilot that has run
([EXP-000](https://github.com/in-c0/state-promotion/blob/main/experiments/EXP-000-RESULT.md))
returned a null result for the gate, and its fixed-schedule control was
algebraically degenerate, so it could not have adjudicated the question either
way.

## What would make this page a description rather than a conjecture

See [SYNTHESIS-READINESS.md](SYNTHESIS-READINESS.md). In short: at minimum a
confirmatory readout on `state-promotion/EXP-001` under valid budget-matched
conditions, plus at least one experiment establishing that ALLOCATE is a real and
separate lever. Neither exists.
