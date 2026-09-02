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
Decides whether fast-state learning is committed to slow parameters, using only
already-observed training and replay evidence. Never held-out labels: this is
enforced in `state-promotion` by a machine-checkable
`heldout_gate_example_count` that must be zero.

Owns programme claims **CCS-C2** and **CCS-C10**.

### Retention gate and rollback
Rejects a consolidation candidate if protected replay-derived probes regress
beyond a preregistered tolerance, and restores the prior slow state. This is the
mechanism that makes "candidate ≠ committed" real rather than rhetorical.

## Components with no implementation anywhere

These are named so the DAG can reference them. Naming a component is not
designing it.

### Allocator — `plasticity-routing` *(repository not created)*
Would decide *where* an incoming experience is assigned, holding the commit
policy fixed. Owns **CCS-C4**.

The definitional hazard: an allocator that changes how often commitment happens
is not testing allocation, it is testing commitment frequency under another name.
Any design must hold commit count fixed while varying placement, or it cannot
support the claim.

### Commit policy — `adaptive-commitment` *(repository not created)*
Would make the commit threshold a function of observed stream statistics rather
than a frozen constant. Owns **CCS-C5**.

Constraint inherited from programme methodology: the policy may not consume
held-out or task-identity signal. An adaptive threshold that peeks is not a
weaker result, it is an inadmissible one.

### Slow-state structure — `modular-consolidation` *(repository not created)*
Would make slow parametric state separable into modules. Owns **CCS-C6**.

Constraint: modules must be compared at *equal total capacity*. More modules
meaning more parameters would make any observed advantage a budget artefact.

### Integrity monitor — `lifetime-integrity` *(repository not created)*
Would measure whether the substrate stays coherent over lifetimes much longer
than a single experiment stream: drift, staleness, accumulated commitment error.
Owns **CCS-C7**.

Constraint: this is the one component whose claim cannot be supported by any
short-stream experiment, however well controlled. No quantity of EXP-001 evidence
substitutes for a long run.

## Ownership rule

A component is defined here and implemented in exactly one sibling repository. If
two repositories implement the same component, that is programme drift and the
next reconciliation must record it. The umbrella repository implements nothing.
