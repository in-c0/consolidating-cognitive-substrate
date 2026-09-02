# Novelty boundaries

What this programme does **not** claim to have invented. Written before results so
it cannot be quietly narrowed later to fit whatever survives.

## Not claimed as novel

The programme claims novelty for **none** of the following, individually or in
familiar combinations:

- multi-timescale or fast/slow weight systems
- external, episodic or retrieval-based memory
- experience replay in any form
- frozen backbones with adapter-based adaptation
- modular or mixture-of-experts parameter structure
- consolidation, distillation, or rehearsal-based retention
- test-time training or test-time memorisation
- the observation that catastrophic forgetting exists, or that stability and
  plasticity trade off
- the general idea that some experiences matter more than others

## Prior work that constrains the claim

Inherited from `state-promotion` and maintained at programme level. Any CCS claim
must be positioned against these, and a claim that collapses into one of them is
not a contribution.

- Behrouz et al., **Titans: Learning to Memorize at Test Time** (2025), arXiv:2501.00663
- Behrouz et al., **Nested Learning / Hope** (NeurIPS 2025)
- Pattichis & Dovrolis, **Continual Knowledge Updating in LLM Systems: Learning Through Multi-Timescale Memory Dynamics** (2026), arXiv:2605.05097
- Ding et al., **State commitment learning: training language models to distinguish computation from memory** (2026), arXiv:2606.05201
- Lee et al., **SCALE: Upscaled Continual Learning of Large Language Models** (ACL Findings 2026), arXiv:2511.03270
- Kang et al., **Harness Continual Learning: Continual Adaptation Beyond Model Parameters** (2026), arXiv:2608.19013
- RightNow-AI, **Memoir** (2026), arXiv:2607.20792

**Memoir deserves specific attention.** Its preregistered fast-write coupling test
produced a *negative* result and exposed write-volume and ceiling confounds. It is
the closest published precedent for both this programme's method and its most
likely failure mode. Any CCS result that resembles a Memoir-style gain must
explicitly rule out the confounds Memoir identified before it is reported.

## What is actually at stake

The programme's candidate contribution is narrow and entirely conditional on
evidence that does not yet exist:

> Whether **evidence-gated promotion across ephemeral, latent, fast and slow
> state, with guarded commitment and explicit write-budget matching**, improves
> continual adaptation — established under controls strict enough that the result
> cannot be attributed to unequal writes, leaked task identity, ceiling effects,
> or unaccounted decision-time compute.

The contribution, if any, is **the controlled comparison**, not the architecture.
The architecture is an arrangement of known parts.

## Novelty claims this repository will not host

1. Any claim that multi-timescale state is itself new.
2. Any claim of a general "continual learning solution".
3. Any claim about agents, cognition, or lifelong learning that outruns the
   benchmarks actually run. PALS is a synthetic nonce-symbol stream; a result on
   it is a result on it.
4. Any claim of scale generality from a 0.5B model, or of small-model generality
   from a 7B replication.
5. Any framing that presents ACCUMULATE → ALLOCATE → COMMIT as a discovered
   structure rather than an organising conjecture.

## Boundary review

Reviewed at every reconciliation. If a component experiment reads out and its
result is best explained by something on the "not claimed as novel" list, that
must be recorded in the ledger notes rather than reframed as a CCS contribution.
