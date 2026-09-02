# Terminology

One term per concept across the programme. Sibling repositories should use these
words; where one already uses a different word, the mapping is recorded here
rather than imposed by editing that repository.

## Programme operators

| Term | Definition | Not to be confused with |
|---|---|---|
| **ACCUMULATE** | Retaining candidate experience without committing to it. | Replay (a mechanism inside accumulation), or memorisation (an outcome). |
| **ALLOCATE** | Deciding *where* capacity is assigned for an experience. | Routing in the MoE sense, which is per-token inference routing, not lifetime capacity assignment. |
| **COMMIT** | Deciding *whether and when* a change becomes durable. | Consolidation, which is the mechanism a commit decision invokes. |

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
| **Promotion gate** | The decision procedure that admits or declines a candidate. |
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

| Programme term | `state-promotion` term | Note |
|---|---|---|
| COMMIT operator | "promotion" / "state promotion" | The repository predates the operator vocabulary. Not a conflict. |
| Slow parametric state | "slow adapter bank" | Same thing. |
| Write unit | "write unit" | Identical; defined in EXP-001 Amendment A. |
| Decision-time compute | "decision-time inference compute" | Identical; defined in EXP-001 Amendment E. |

No terminology conflicts are outstanding as of 2026-09-02. New repositories
should adopt the programme terms directly.
