# Integration criteria

When a component is allowed to be described as part of an integrated CCS system,
rather than as an independent experiment that happens to sit in the programme.

Integration is the step where a programme starts overstating itself, so the bar
is set before anything is ready to clear it.

## Gate I0 — the component exists and is honest

- [ ] The owning repository exists and is public.
- [ ] It has a preregistration committed before any confirmatory result was inspected.
- [ ] Its README states its own evidence status accurately.
- [ ] Its results are traceable to machine-readable run manifests.
- [ ] Negative and null results are published, not buried.

## Gate I1 — the component result is admissible

- [ ] Budgets matched: parameter capacity, replay bytes, unique online tokens,
      parameter-write ceiling.
- [ ] No held-out or task-identity signal in any decision path.
- [ ] Decision-time compute counted separately and reported.
- [ ] Non-ceiling benchmark; measurable interference demonstrated.
- [ ] Commit-count-matched control included where a routing or gating claim is made.
- [ ] ≥5 paired seeds, development seeds disjoint from confirmatory seeds.
- [ ] Effect sizes and confidence intervals reported, not only p-values.
- [ ] Result robust to task ordering.

A component failing any I1 box may be reported as a pilot. It may not enter an
integration argument.

## Gate I2 — the components are actually compatible

Two components can each be admissible and still not compose. Before an integrated
system is described:

- [ ] **Shared substrate.** Same state hierarchy and same definitions from
      [COMPONENTS.md](COMPONENTS.md), or documented differences.
- [ ] **Shared evaluation.** At least one benchmark on which both were measured
      under the same protocol version.
- [ ] **Shared budget accounting.** The same write-unit definition and the same
      decision-compute accounting. Two components using different write units
      cannot have their budgets added.
- [ ] **No overlapping ownership.** Two components must not both implement the
      same operator; see the ownership rule in COMPONENTS.md.
- [ ] **Interaction hazards named in advance.** Written down before the combined
      run, not after.

## Gate I3 — integration is measured, not assumed

This is the gate that matters, and no part of the programme has approached it.

- [ ] An integration experiment (`ccs/EXP-I1`) exists, in its own repository,
      with its own preregistration.
- [ ] The integrated system is compared against **each** component alone, under a
      matched *total* budget — not against a naive baseline.
- [ ] The combined effect exceeds the best single component's effect by more than
      the pooled confidence interval.
- [ ] An additivity analysis distinguishes genuine composition from the largest
      single contribution.
- [ ] Interference is reported: components that hurt each other are named.

**A combination that merely matches its best part is not an integrated system.**
It is one working component and some overhead, and the programme must say so.

## Current status

No component has cleared **I0**, because no component has a confirmatory result.
`state-promotion` is the only repository positioned to attempt I0 and I1.

Gates I2 and I3 are unreachable in principle until at least three component
experiments read out. `ccs/EXP-I1` has no repository and no design.
