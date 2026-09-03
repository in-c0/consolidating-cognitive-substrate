# Common integration reporting envelope

**A precondition for [`ccs/EXP-I1`](DEPENDENCY-DAG.md) and `ccs/EXP-U1`, not a
detail of them.**

Four tracks account for resources in four incompatible ways. Each is correct for
its own purposes. None of them add up.

| Track | Native accounting |
|---|---|
| `state-promotion` | write units — elements in the fast-state parameter subset |
| `plasticity-routing` | a unified cost table with one hard write ceiling per arm |
| `modular-consolidation` | capacity: `param_total`, `param_active`, `param_peak`, storage, total algorithmic FLOPs |
| `lifetime-integrity` | evidence reads against a capped log |
| `adaptive-commitment` | undefined — repository does not exist |

Until these can be expressed in one envelope, the phrase **"matched total
budget"** — which appears in the primary comparison of both CCS-C8 and CCS-C12 —
has no referent. The integration experiment cannot be *stated*, let alone run.

## What this is and is not

**Native units stay authoritative.** This is a reporting layer, not a
replacement. No track is asked to change its internal accounting, and the
umbrella has no standing to ask.

**Unmapped is usually fine.** A dash below normally means the track has no such
resource — `lifetime-integrity` is architecture-agnostic, so parameter-denominated
dimensions may stay permanently unmapped, and that is a property of the benchmark
rather than a defect.

**Incommensurable is the serious case.** The resource exists but cannot be
expressed in a common unit without an arbitrary exchange rate. That blocks
integration, and `tools/validate_ledger.py` enforces the block: while any
incommensurable dimension is open, `ccs/EXP-I1` and `ccs/EXP-U1` may not leave
`not-designed`.

## Coverage

**Source of truth is [`ledger/resource_envelope.json`](../ledger/resource_envelope.json).**

<!-- GENERATED:envelope -- do not edit by hand; run tools/render.py -->

| Dimension | Additive | state&#8209;promotion | adaptive&#8209;commitment | plasticity&#8209;routing | modular&#8209;consolidation | lifetime&#8209;integrity |
|---|---|---|---|---|---|---|
| `param_capacity_stored` | yes | — | — | — | mapped | — |
| `param_capacity_active` | **no** | mapped | — | — | mapped | — |
| `write_ops` | yes | mapped | — | mapped | — | — |
| `compute_training` | yes | mapped | — | — | — | — |
| `compute_inference` | yes | — | — | — | — | — |
| `compute_decision` | yes | mapped | — | mapped | mapped | — |
| `compute_consolidation` | yes | — | — | — | mapped | mapped |
| `store_bytes` | yes | mapped | — | mapped | mapped | mapped |
| `store_reads` | yes | — | — | mapped | — | mapped |
| `wall_runtime` | **no** | mapped | — | — | — | — |
| `latency_to_response` | **no** | — | **INCOMM** | — | — | — |
| `intervention_cost` | **no** | — | **INCOMM** | — | — | — |

`mapped` = expressible in the common unit. `—` = the track has no such resource. `**INCOMM**` = the resource exists but has no non-arbitrary common unit, which **blocks integration**.

**18 of 60 track/dimension cells mapped. 2 incommensurable.**

### Open problems

| ID | Problem | Blocks |
|---|---|---|
| **OP-1** | No shared exchange rate between internal and external commitment costs | `ccs/EXP-U1`, `ccs/EXP-I1` |
| **OP-2** | param_capacity_active is not additive across tracks | `ccs/EXP-I1` |
| **OP-3** | Nobody owns the envelope | `ccs/EXP-I1`, `ccs/EXP-U1` |

<!-- /GENERATED:envelope -->

## The problem the split created

Separating COMMIT_INTERNAL from COMMIT_EXTERNAL made a measurement problem
visible that the old vocabulary had concealed.

An internal commitment costs parameters, writes, and interference. An external
commitment costs latency, an interlocutor's patience, and — for irreversible
actions — consequence. These are not the same kind of quantity. Asking whether one
mechanism governs both "at matched total budget" presupposes an exchange rate
between a parameter write and a second of someone's waiting.

That may not exist non-arbitrarily. It is recorded as the fourth falsifier of
CCS-C12: **if the cost structures are genuinely incommensurable, the unification
claim fails on measurement grounds even if a shared mechanism turns out to be
buildable.** That is a real way for the claim to be false, not a caveat about
tooling.

`plasticity-routing` has solved a version of this problem inside one track — its
objective folds storage, write and compute into a single scalar via `λ` weights.
Those weights are a candidate starting point, but they were calibrated for SDW-1
and are not automatically transferable, least of all to a domain with a human on
the other end.

## Ownership

**Unowned as of 2026-09-03.** Populating and maintaining the mapping is umbrella
work. Reconciling a genuine disagreement about what a dimension *means* would
require agreement across tracks, which the umbrella cannot direct — see
[RECONCILIATION-POLICY.md](RECONCILIATION-POLICY.md).

This is recorded as open problem OP-3 rather than assigned, because assigning it
from here would be exactly the kind of cross-track direction this repository is
built not to do.
