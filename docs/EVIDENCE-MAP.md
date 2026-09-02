# Evidence map

The claim ledger says *what is believed*. This page says *what could change it*,
in the other direction: from each experiment to the claims it can move.

Maintaining this map in both directions is the point. A claim with no experiment
mapped to it is a claim nobody is testing, and the validator rejects it.

## Experiment → claims

| Experiment | Exists? | Can support | Can falsify |
|---|---|---|---|
| `state-promotion/EXP-000` | ✅ complete | — | — |
| `state-promotion/EXP-001` | ✅ scaffold, no results | CCS-C2, C3, C9, C10 | CCS-C2, C3, C9, C10, and by implication C1 |
| `state-promotion/EXP-002` | ❌ planned | CCS-C2 (external benchmarks) | CCS-C2 |
| `state-promotion/EXP-003` | ❌ planned | CCS-C2 (at scale) | CCS-C2 |
| `plasticity-routing/EXP-P1` | ❌ no repo | CCS-C4, C1, C9 | CCS-C4, and the three-operator framing in C1 |
| `adaptive-commitment/EXP-A1` | ❌ no repo | CCS-C5, C1 | CCS-C5 |
| `modular-consolidation/EXP-M1` | ❌ no repo | CCS-C6 | CCS-C6 |
| `lifetime-integrity/EXP-L1` | ❌ no repo | CCS-C7 | CCS-C7 |
| `ccs/EXP-I1` | ❌ no repo, no design | CCS-C8, C1 | CCS-C8 |

EXP-000 can neither support nor falsify anything. Its own repository classifies it
as engineering validation, its promotion arm tied with replay within variance, and
its fixed-consolidation control was algebraically identical to replay by
construction. It is listed so that it is never quietly upgraded.

## Claims nothing can currently test

| Claim | Blocked on |
|---|---|
| CCS-C4 (allocation separable) | `plasticity-routing` does not exist |
| CCS-C5 (adaptive thresholds) | `adaptive-commitment` does not exist |
| CCS-C6 (modular slow state) | `modular-consolidation` does not exist |
| CCS-C7 (lifetime coherence) | `lifetime-integrity` does not exist |
| CCS-C8 (composition) | No integration experiment is designed, and its five prerequisites have not read out |

Five of ten programme claims currently have **no runnable test anywhere**. That is
the single most important fact about the programme's evidence position, and it is
why no synthesis paper can be written now regardless of how EXP-001 turns out.

## Inherited admissibility rules

These come from `state-promotion`'s preregistration. The programme adopts them at
the umbrella level so that later repositories cannot quietly relax them. A readout
violating any of these is **not evidence for any CCS claim**:

1. **No held-out signal in a decision path.** Evaluation labels may not influence
   routing, promotion, rollback, optimizer selection, or replay construction.
2. **Budgets matched before architecture is interpreted.** Parameter capacity,
   replay bytes, unique online tokens, and the parameter-write ceiling.
3. **Decision-time compute counted separately and reported.** A gated method is
   never described as compute-matched without qualification.
4. **Ceiling effects invalidate.** If every adaptive arm exceeds 95% before the
   third segment, the configuration cannot adjudicate anything.
5. **Commit-count-matched controls required.** An advantage that vanishes against
   a random routing control matched on commit count was never a routing effect.
6. **Single task ordering is not a result.**
7. **Development and confirmatory seeds disjoint**, with thresholds frozen before
   confirmatory seeds are touched.

Any new sibling repository inherits these by default. A repository that needs to
depart from one must say so in its own preregistration, and the departure must be
recorded here at the next reconciliation.
