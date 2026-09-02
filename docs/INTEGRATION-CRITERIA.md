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

## Current status — reconciled 2026-09-02

**No component has cleared I0**, because no component has a confirmatory result.
Four repositories now satisfy most of I0's *process* boxes — preregistrations
committed before results, accurate self-declared status, machine-readable
manifests, negative results published rather than buried — and none satisfies the
box that matters, which is having an admissible result at all.

Gate **I2** has acquired a concrete obstacle that did not exist at the first
survey. Two of the four tracks do not currently share a budget-accounting scheme:

- `state-promotion` accounts in **write units** (parameter elements in the fast
  subset) with decision-time inference compute reported separately.
- `plasticity-routing` accounts in a **unified cost table** over storage, write
  and compute, with one hard write ceiling shared across arms.
- `modular-consolidation` accounts in **capacity terms** — `param_total`,
  `param_active`, `param_peak`, storage including cold storage, and total
  algorithmic FLOPs.
- `lifetime-integrity` accounts in **evidence reads** against a capped log.

These are not interchangeable, and I2 requires that budgets be addable before any
integrated total is meaningful. Reconciling them is a real piece of work that
nobody currently owns, and it is a prerequisite for EXP-I1 rather than a detail of
it.

Gate **I3** remains unreachable. `ccs/EXP-I1` has no repository and no design, and
per the 2026-09-02 reconciliation instruction none is to be created yet.
