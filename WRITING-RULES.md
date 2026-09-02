# Writing rules

This repository describes a programme whose central claims are untested. The
failure mode it must avoid is prose that drifts, sentence by sentence, from
"we propose" to "the substrate does".

These rules apply to every Markdown file here.

## 1. Separate proposal from finding, in every sentence

| Write | Not |
|---|---|
| "The programme conjectures that…" | "The substrate accumulates…" |
| "EXP-001 is designed to test whether…" | "Evidence gating improves…" |
| "If confirmed, this would indicate…" | "This shows…" |

## 2. Never describe a mechanism's purpose as its effect

"The retention gate rejects candidates that regress protected probes" is a
description of code. "The retention gate prevents forgetting" is a claim about
outcomes, and requires an admissible readout.

## 3. State epistemic status at the top of any conceptual document

[ARCHITECTURE-HYPOTHESIS.md](docs/ARCHITECTURE-HYPOTHESIS.md) opens with a status
block. Any new conceptual document must do the same.

## 4. Absence of refutation is not support

Six claims in the ledger are unfalsified only because nothing capable of
falsifying them has run. Say that, rather than letting silence read as agreement.

## 5. Name the benchmark, always

A result on PALS is a result on a synthetic nonce-symbol stream. A result at 0.5B
is a result at 0.5B. Claims inherit the scope of their evidence and never exceed
it.

## 6. Link claims to their ledger entry

Any mention of a programme claim links to [CLAIM-LEDGER.md](docs/CLAIM-LEDGER.md),
so a reader can see its status without trusting the surrounding prose.

## 7. Keep failure visible

Falsified claims stay in the ledger with their evidence. Null results are cited by
name — EXP-000's null result appears in the README, the ledger, the architecture
document, and the reconciliation report, because it is the most informative
empirical fact the programme currently has.

## Enforced mechanically

`tools/validate_ledger.py` scans committed prose for result language:

| Pattern | Why |
|---|---|
| "we show / demonstrate / prove / find that" | asserts a finding |
| "our results show / demonstrate / confirm" | asserts results |
| "significantly outperform", "substantially better than" | asserts a comparison |
| "state-of-the-art" | unearned |
| "achieves N%", "achieves superior" | asserts a measured outcome |

This file is exempt from the scan, since it must quote the banned phrases.

The scan is a coarse tripwire, not a proof. It catches the obvious drift so
review attention can go to the subtle kind: a mechanism described so confidently
that a reader concludes it works.
