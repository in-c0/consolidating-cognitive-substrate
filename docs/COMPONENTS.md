# Component definitions

Each component has exactly one owning repository. The umbrella repository defines
what a component *is* so that sibling repositories can disagree with the
definition explicitly rather than by accident.

"Implemented" below means code exists. It does not mean the component has been
shown to do anything. See [CLAIM-LEDGER.md](CLAIM-LEDGER.md).

## Implemented components

All of these live in [`in-c0/state-promotion`](https://github.com/in-c0/state-promotion).

### Ephemeral computation
Activations and context for a single reasoning step. No persistence mechanism of
its own. Present in any transformer; listed for completeness of the hierarchy.

### Persistent latent state `z_t`
A bounded-size recurrent state carried across stream items and sessions. Bounded
size is the definitional constraint: an unbounded latent state is a cache, and
the programme's questions about it become trivial.

Owns programme claim **CCS-C3**.

### Fast parametric state `F_t`
Online plastic parameters updated on recent evidence. The store that absorbs new
behaviour quickly and is expected to be unreliable.

### Slow parametric state `S`
Durable parameterised knowledge. Written to only through a commit decision, never
directly from an online gradient. Currently a single adapter bank; whether it
should be modular is **CCS-C6**, owned by a repository that does not exist.

### Episodic replay `E`
A bounded reservoir of attributable training examples and outcomes. Deliberately
kept inspectable. The programme does not treat replay as a memory *level* — it is
evidence storage that other components consult.

### Promotion gate
**COMMIT_INTERNAL.** Decides whether fast-state learning is committed to slow
parameters, using only already-observed training and replay evidence. Never held-out labels: this is
enforced in `state-promotion` by a machine-checkable
`heldout_gate_example_count` that must be zero.

Owns programme claims **CCS-C2** and **CCS-C10**.

### Retention gate and rollback
Rejects a consolidation candidate if protected replay-derived probes regress
beyond a preregistered tolerance, and restores the prior slow state. This is the
mechanism that makes "candidate ≠ committed" real rather than rhetorical.

## Implemented components — `plasticity-routing`

### Allocator
Decides *where* an incoming experience is assigned. Implemented over four
actions — `IGNORE`, `EPISODIC`, `FAST`, `SLOW` — chosen so that write *depth*
stays a real axis, with `IGNORE` making "write nowhere" an explicit option the
umbrella's state hierarchy does not otherwise name. Owns **CCS-C4**.

The definitional hazard is handled rather than assumed away: the track runs a
budget-matched random allocator with nearly the same action mix, so an advantage
that is really about write volume cannot be read as an advantage about placement.
It also excludes `UPDATE_EXISTING_MODULE` and `SPAWN_NEW_MODULE` precisely
because they add capacity, which is the primary confound.

Whether four actions are *justified* is tested rather than asserted: the
benchmark is admissible only if the empirically optimal class-to-action mapping
is a bijection.

## Implemented components — `modular-consolidation`

### Slow-state structure
Module allocation, specialisation, merging, retirement with reinstatement, and
reuse, with capacity, cold storage for retired modules, and routing decision
compute all metered. Owns **CCS-C6** and **CCS-C11**.

Constraint the track enforces and the umbrella has adopted programme-wide: a
dynamic method must be compared against a fixed configuration of *its own final
size* at equal compute. Without that control, "dynamic allocation helps" is
indistinguishable from "N modules is the right size".

## Implemented components — `lifetime-integrity`

### Integrity monitor
Nine re-grounding mechanisms scored behind a metered, capped evidence log, with
integrity scored separately from accuracy: answering a correct value nobody ever
supplied counts as a failure, not a success. Owns **CCS-C7**.

Architecture-agnostic by construction — anything implementing
`observe / on_gap / on_context_shift / answer / state_bytes` can be scored. That
track states this is a hard dependency rather than a stylistic choice, and that
no result from it may be used to claim a CCS latent architecture is validated
without an admissible substrate from `state-promotion`.

## Components with no implementation anywhere

These are named so the DAG can reference them. Naming a component is not
designing it.

### External commitment policy — `adaptive-commitment` *(the only uncreated sibling)*

**Role corrected 2026-09-03.** This component was previously described here as an
adaptive *consolidation threshold* — a refinement of `state-promotion`. That was
wrong, and it was the umbrella's error rather than the track's: it followed from
using one word, COMMIT, for two operators.

Would own **COMMIT_EXTERNAL**: deciding when cognition is released outward under
streaming evidence — `WAIT`, `THINK`, `ASK`, `RESPOND`, `ACT` — trading accuracy
against latency, compute, intervention cost, uncertainty, and
consequence/reversibility.

**Owns no CCS claim yet, by owner decision.** A programme claim for behavioural
commitment timing is to be written only after that track's own literature audit
and preregistration define its exact falsifiable form. Writing one now would be
inventing a hypothesis on its behalf, which is the same error in the opposite
direction.

Two constraints it will inherit and one it will not:

- Inherited: no held-out or task-identity signal in a decision path.
- Inherited: decision-time compute counted separately — the cost of deciding
  whether to speak is part of the method, not overhead to be hidden.
- **Not** inherited: this track is *not* blocked on `state-promotion/EXP-001`. It
  was deliberately scoped as a separate domain, and the previous dependency edge
  has been removed.

Its two native costs — latency borne by an interlocutor, and the consequence of an
irreversible action — have no counterpart in any other track. See
[RESOURCE-ENVELOPE.md](RESOURCE-ENVELOPE.md).

## Commitment domains

Two components in this file make commitment decisions, and they are **not
assumed to share a mechanism**:

| Component | Domain | Track | Decides |
|---|---|---|---|
| Promotion gate | COMMIT_INTERNAL | `state-promotion` | whether state becomes durable |
| External commitment policy | COMMIT_EXTERNAL | `adaptive-commitment` | whether cognition is released outward |

Whether one learned mechanism can govern both is
[CCS-C12](CLAIM-LEDGER.md) — a claim with a low prior and four falsifiers, not a
naming convention.

## Ownership rule

A component is defined here and implemented in exactly one sibling repository. If
two repositories implement the same component, that is programme drift and the
next reconciliation must record it. The umbrella repository implements nothing.

### Overlap under watch

`plasticity-routing` and `modular-consolidation` both touch slow parametric
state. They are not currently in conflict: the former treats `SLOW` as one
destination among four and deliberately excludes the module-spawning actions,
while the latter owns the internal structure of that destination. The boundary
holds only as long as `plasticity-routing` keeps excluding
`UPDATE_EXISTING_MODULE` and `SPAWN_NEW_MODULE`. If that exclusion is ever
relaxed, the two tracks would be varying the same factor and the next
reconciliation must record an ownership conflict.
