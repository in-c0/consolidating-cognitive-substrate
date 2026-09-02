# Synthesis readiness

What evidence must exist before a synthesis paper is scientifically defensible.

The eventual paper might be titled something like *Consolidating Cognitive
Substrate: Toward Multi-Timescale Coherent Continual Agents*. **This repository
will not contain its Results section, its abstract, or its claims until the gates
below are cleared.** The title is recorded as an intention, not as a placeholder
to be filled in.

## Readiness checklist

### Tier 1 — the central mechanism (required, none cleared)

- [ ] `state-promotion/EXP-001` reaches confirmatory status under a frozen protocol
- [ ] Development/confirmatory seed boundary frozen before confirmatory seeds are touched
- [ ] Code commit SHA, weight/tokenizer revisions, and environment lock recorded
- [ ] ≥5 paired seeds, effect sizes and CIs reported
- [ ] H1 result — **in either direction** — published
- [ ] The B4 commit-count-matched control included and reported
- [ ] Decision-time compute reported alongside adaptation compute (Amendment E)
- [ ] PALS shown non-ceiling with measurable interference

### Tier 2 — external validity (required, none cleared)

- [ ] `state-promotion/EXP-002` on CITB/TRACE with documented preprocessing
- [ ] Effect direction consistent, or the inconsistency reported as a limit
- [ ] Robustness to task ordering demonstrated

### Tier 3 — the decomposition is real (required, none cleared)

- [ ] At least one experiment establishing ALLOCATE as separable from COMMIT
      (`plasticity-routing/EXP-001` — preregistered, not read out)
- [ ] At least one long-horizon result on lifetime coherence
      (`lifetime-integrity/EXP-A001` — preregistered, not read out)
- [ ] An admissible substrate established by `state-promotion`, without which
      `lifetime-integrity` results cannot license a CCS architecture claim at all
- [ ] Each component's contribution isolated by ablation

### Tier 4 — composition (required for a *synthesis* claim, none cleared)

- [ ] `ccs/EXP-I1` exists in its own repository with its own preregistration
- [ ] Integrated system beaten against **each** component alone at matched total budget
- [ ] Combined effect exceeds best single component by more than the pooled CI
- [ ] Additivity analysis separating composition from the largest single contribution
- [ ] Interference between components reported

## The minimum defensible paper at each stage

Being unready for synthesis does not mean being unready to publish. What is
honestly publishable, as each tier clears:

| Evidence available | Defensible paper |
|---|---|
| **Today** | None. A methods/preregistration note at most. |
| Tier 1 only | A single-mechanism paper about evidence-gated consolidation on a synthetic stream. Not a substrate paper. |
| Tier 1 + 2 | A continual-learning method paper with external benchmark support. Still not a substrate paper. |
| Tier 1 + 2 + 3 | A multi-component paper reporting each component separately, with an explicitly conjectural framing section. |
| Tier 1 + 2 + 3 + 4 | The synthesis paper. |

The gap between row 4 and row 5 is the entire difference between "we built several
things" and "these things constitute a substrate". Only Tier 4 evidence closes it.

## Where the programme actually stands — reconciled 2026-09-02

**Zero of four tiers cleared. Zero checkboxes cleared.**

The programme grew substantially between the first survey and this
reconciliation, and cleared nothing:

- Four repositories of five now exist; `adaptive-commitment` is the last gap.
- **Six evidence entries are on file and none is admissible.** Every one is a
  development calibration or an engineering pilot that its own track classifies
  as non-evidential.
- `state-promotion` main is unchanged with an empty `results/`. An off-main
  small-LM pilot exists; a sibling records it as mechanically valid but
  scientifically uninterpretable, with a LoRA representation repair predeclared.
- `plasticity-routing`'s development calibration fired K1 **against** learned
  routing.
- `modular-consolidation` records the unbounded-regime consolidation claim as
  falsified in its own track-local ledger.
- The integration experiment still has no design and no host repository, by
  decision rather than oversight.

The correct description of this programme today is: **four well-controlled
scaffolds, several preregistrations, and no admissible evidence.** That is a
respectable place to be after one day of parallel work. It is not a substrate,
and it is not a paper.

### The specific trap this page exists to block

Four repositories now contain real code, real controls, real confidence
intervals, and numbers that look like results. None of it is admissible, every
track says so about its own output, and each has declared that its results do not
travel to other tracks. The temptation to assemble a synthesis narrative from six
inadmissible development readouts is precisely the failure mode
[FAILURE-CRITERIA.md](FAILURE-CRITERIA.md) calls F2, arriving earlier than
expected and looking more like progress than F1 would.

## The rule this page exists to enforce

> No Results section, no abstract, no broad claim, and no architecture-as-finding
> prose is written in this repository until the gates above are cleared and the
> ledger records confirmatory support.

If the programme wants a paper sooner, the route is the "minimum defensible paper"
table above — narrow the claim to fit the evidence. It is never to widen the
evidence to fit the claim.
