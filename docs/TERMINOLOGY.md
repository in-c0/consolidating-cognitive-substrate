# Terminology

One term per concept across the programme. Sibling repositories should use these
words; where one already uses a different word, the mapping is recorded here
rather than imposed by editing that repository.

## Programme operators

| Term | Definition | Not to be confused with |
|---|---|---|
| **ACCUMULATE** | Retaining candidate experience without committing to it. | Replay (a mechanism inside accumulation), or memorisation (an outcome). See the open ambiguity below. |
| **ALLOCATE** | Deciding *where* capacity is assigned for an experience. | Routing in the MoE sense, which is per-token inference routing, not lifetime capacity assignment. |
| **COMMIT_INTERNAL** | Deciding *whether and when* information or state becomes durable in the substrate — a memory or parameter write. | Consolidation, which is the mechanism a commit decision invokes. And **not** COMMIT_EXTERNAL. |
| **COMMIT_EXTERNAL** | Deciding *whether and when* cognition is released outward as a response or action — `WAIT`, `THINK`, `ASK`, `RESPOND`, `ACT`. | COMMIT_INTERNAL. Also not "inference", which is producing an output, not deciding to release one. |

### Why COMMIT was split — 2026-09-03

Until 2026-09-03 this programme used one word, **COMMIT**, for both. That was not
a shorthand; it was an unexamined assumption. Writing state durably and releasing
an utterance are different decisions with different costs, different
reversibility, and different parties bearing the consequence.

Using one word for both **presupposed** that a single mechanism governs them. That
is a research hypothesis with a low prior, and it now has an explicit, falsifiable
home as [CCS-C12](CLAIM-LEDGER.md) — including a falsifier the vocabulary was
hiding: the two cost structures may be genuinely incommensurable, in which case
unification fails on measurement grounds however elegant the mechanism.

`tools/validate_ledger.py` rejects bare `COMMIT` as a DAG operator, so the
distinction cannot erode back by habit.

**Domain ownership:** COMMIT_INTERNAL is `state-promotion`'s domain (with
`modular-consolidation` owning the structure of its target). COMMIT_EXTERNAL is
`adaptive-commitment`'s domain, and that repository does not exist yet.

### Open ambiguity — ACCUMULATE has the same problem, unresolved

This repository has read ACCUMULATE as *"retain candidate experience"* — a
statement about memory. `plasticity-routing` reads it as *"continue gathering /
thinking"* — a statement about behaviour, much closer to COMMIT_EXTERNAL's `WAIT`
and `THINK` than to state retention.

Those are not obviously the same operator, and the same internal/external split
may be latent here too. **ACCUMULATE has deliberately not been split**, because no
track has operationalised either reading and splitting it now would be inventing
structure ahead of evidence. It is recorded as a falsifier of
[CCS-C1](CLAIM-LEDGER.md): if the two readings turn out to be different operators,
the decomposition has been describing two pipelines under one set of names.

## State levels

| Term | Definition |
|---|---|
| **Ephemeral state** | Activations/context within a single step or session. |
| **Latent state** (`z_t`) | Bounded recurrent state persisting across items and sessions. Boundedness is definitional. |
| **Fast parametric state** (`F_t`) | Online plastic parameters updated from recent evidence. |
| **Slow parametric state** (`S`) | Durable parameters, written only through a commit decision. |
| **Foundation** | Frozen pretrained weights. Never modified in current experiments. |
| **Episodic memory** (`E`) | Bounded, attributable, inspectable store of examples and outcomes. Sits alongside the hierarchy, not inside it. |

## Decision machinery

| Term | Definition |
|---|---|
| **Candidate** | A proposed change to durable state that has not been committed. |
| **Promotion gate** | The decision procedure that admits or declines a candidate. COMMIT_INTERNAL. |
| **Release** | Emitting an outward response or action. The COMMIT_EXTERNAL analogue of a commit, and deliberately given a different word. |
| **Retention gate** | The check that rejects a candidate which regresses protected probes. |
| **Rollback** | Restoration of prior durable state after a rejected candidate. |
| **Write unit** | The number of parameter elements in the fast-state subset. The programme's unit of write-budget accounting. |
| **Decision-time compute** | Forward passes whose output can change a commit/rollback decision. Method overhead, never post-hoc evaluation. |

## Evidence vocabulary

| Term | Definition |
|---|---|
| **Pilot** | A run that is not admissible as paper evidence, by its own declaration. |
| **Confirmatory** | A run under a frozen protocol with disjoint confirmatory seeds. |
| **Admissible** | A readout that satisfies every rule in [EVIDENCE-MAP.md](EVIDENCE-MAP.md#inherited-admissibility-rules). |
| **Readout** | The moment results for an experiment are inspected. Before readout, protocol changes are amendments; after, they create a new protocol version. |
| **Falsifier** | A concrete outcome that would kill a claim. Every claim must have one. |

## Words used carefully

These are not banned, but they carry a burden of proof and the validator or a
reviewer should challenge them:

| Word | Why it is risky | Use instead, unless earned |
|---|---|---|
| "shows", "demonstrates", "proves" | Asserts a finding. | "is designed to test", "would indicate" |
| "outperforms" | Implies a measured comparison. | Name the comparison and its status. |
| "solves", "achieves" | Implies a completed outcome. | "targets", "is evaluated on" |
| "coherent", "cognitive", "substrate" | Programme branding that outruns evidence. | Say the mechanism. |
| "emergent" | Almost always unearned. | Describe what was measured. |
| "memory" (unqualified) | Ambiguous across five levels above. | Name the level. |
| "forgetting" | Sometimes desirable. | "catastrophic forgetting" vs "supersession". |

The last one is a real distinction, not pedantry: on a revision stream, retaining
a superseded answer is a failure, and counting it as retention would invert the
metric. `state-promotion` separates retention streams from revision streams for
this reason.

## Cross-repository mapping

| Programme term | Track term | Note |
|---|---|---|
| COMMIT_INTERNAL operator | `state-promotion`: "promotion" / "state promotion" | The repository predates the operator vocabulary. Not a conflict. |
| Slow parametric state | `state-promotion`: "slow adapter bank" | Same thing. |
| Write unit | `state-promotion`: "write unit" | Identical; defined in EXP-001 Amendment A. |
| Decision-time compute | `state-promotion`: "decision-time inference compute" | Identical; defined in EXP-001 Amendment E. |
| ALLOCATE operator | `plasticity-routing`: "allocation" / "routing" | Identical. |
| COMMIT_INTERNAL | `plasticity-routing`: the `SLOW` action | A durable internal write, reached by an allocation decision. |
| COMMIT_EXTERNAL | `plasticity-routing`: "commitment in the CCS sense" | That track explicitly models none of it. |
| Slow parametric state | `plasticity-routing`: `SLOW` action | One destination among four, not a level the track owns. |
| Slow-state structure | `modular-consolidation`: "module lifecycle" | Same thing. |
| Latent state | `lifetime-integrity`: "belief store" / "persistent state" | Deliberately substrate-neutral there; not a claim about a CCS latent architecture. |

## Resolved divergence — COMMIT

**Raised 2026-09-02, resolved 2026-09-03 by splitting the term.**

`plasticity-routing` read COMMIT as an *outward-facing* commitment and stated that
its durable `SLOW` write was therefore "not a commitment in the CCS sense". The
umbrella read COMMIT as the decision that a change becomes durable, which includes
an internal write.

Both were right about their own referent. The fault was the umbrella's: one word
covering two operators. Under the split, that track's `SLOW` write is a
**COMMIT_INTERNAL** action reached by an ALLOCATE decision, and the "commitment in
the CCS sense" it correctly declines to model is **COMMIT_EXTERNAL**. No sibling
needed to change anything, and none was asked to.

What this does *not* resolve: whether ALLOCATE and COMMIT_INTERNAL are cleanly
separable. That was the substantive question underneath the vocabulary clash, it
is untouched by renaming, and it remains [CCS-C4](CLAIM-LEDGER.md)'s to settle.

A second, smaller divergence stands unresolved: `plasticity-routing` describes
`state-promotion` as sitting at the ALLOCATE-to-COMMIT boundary, whereas this
registry assigns it COMMIT_INTERNAL. Recorded; no action.

New repositories should adopt the programme terms directly, and declare any
departure in their own documentation.
