#!/usr/bin/env python3
"""Validate the CCS claim ledger, repo registry and experiment DAG.

Stdlib only, by design: this gate must run on any machine without a setup step.

The point of this validator is not schema tidiness. It is to make it mechanically
hard for the umbrella repository to drift into describing untested architectural
ideas as results. The invariants below are the programme's epistemic rules
expressed as code.
"""

from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LEDGER = ROOT / "ledger"

STATUSES = [
    "theoretical-conjecture",
    "implemented",
    "pilot-supported",
    "confirmatory-supported",
    "falsified",
    "unresolved",
]
# Statuses that assert empirical support and therefore require evidence.
EVIDENCE_BEARING = {"pilot-supported", "confirmatory-supported", "falsified"}
IMPLEMENTATION_LEVELS = {"none", "partial", "implemented"}
EVIDENCE_CLASSES = {"pilot", "confirmatory"}
STAGES = {
    "not-designed",
    "planned",
    "pre-result-scaffold",
    "pilot-complete",
    "confirmatory-complete",
}
EXISTENCE = {"exists", "planned", "archived"}

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def load(name: str) -> dict:
    path = LEDGER / name
    if not path.exists():
        err(f"missing ledger file: {path}")
        return {}
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        err(f"{name}: invalid JSON: {exc}")
        return {}


def check_claims(claims_doc: dict, dag_doc: dict, repos_doc: dict) -> None:
    claims = claims_doc.get("claims", [])
    if not claims:
        err("claims.json: no claims defined")
        return

    node_ids = {n["id"] for n in dag_doc.get("nodes", [])}
    repo_ids = {r["id"] for r in repos_doc.get("repos", [])}
    existing_repos = {
        r["id"] for r in repos_doc.get("repos", []) if r.get("existence") == "exists"
    }
    seen: set[str] = set()

    for c in claims:
        cid = c.get("id", "<no id>")
        if cid in seen:
            err(f"{cid}: duplicate claim id")
        seen.add(cid)

        if not re.fullmatch(r"CCS-C\d+", cid):
            err(f"{cid}: id must match CCS-C<n>")

        status = c.get("status")
        if status not in STATUSES:
            err(f"{cid}: status {status!r} not in the ledger vocabulary")

        impl = c.get("implementation")
        if impl not in IMPLEMENTATION_LEVELS:
            err(f"{cid}: implementation {impl!r} not in {sorted(IMPLEMENTATION_LEVELS)}")

        for field in ("title", "statement", "notes", "review_by"):
            if not c.get(field):
                err(f"{cid}: missing required field {field!r}")

        evidence = c.get("evidence", [])

        # INVARIANT 1 -- a status that asserts empirical support needs evidence.
        if status in EVIDENCE_BEARING and not evidence:
            err(
                f"{cid}: status {status!r} asserts empirical support but the "
                f"evidence list is empty"
            )

        # INVARIANT 2 -- every claim must be falsifiable by something concrete.
        if not c.get("falsified_by"):
            err(f"{cid}: no falsifier recorded; every CCS claim must be falsifiable")

        # INVARIANT 3 -- implementation is not evidence.
        if impl == "implemented" and status in {"pilot-supported", "confirmatory-supported"}:
            if not any(e.get("admissible") for e in evidence):
                err(
                    f"{cid}: claims empirical support but no admissible evidence "
                    f"entry exists; code existing is not evidence"
                )

        # INVARIANT 4 -- claimed supporting experiments must exist in the DAG.
        for node in c.get("supported_by", []):
            if node not in node_ids:
                err(f"{cid}: supported_by references unknown DAG node {node!r}")

        # INVARIANT 5 -- every claim needs at least one experiment able to test it.
        if not c.get("supported_by"):
            err(f"{cid}: no experiment is mapped to this claim")

        # INVARIANT 6 -- evidence must point at a real repository and be classified.
        for e in evidence:
            repo = e.get("repo")
            if repo not in repo_ids:
                err(f"{cid}: evidence references unknown repo {repo!r}")
            elif repo not in existing_repos:
                err(
                    f"{cid}: evidence cites {repo!r}, which does not exist; "
                    f"evidence cannot come from an uncreated repository"
                )
            if e.get("class") not in EVIDENCE_CLASSES:
                err(f"{cid}: evidence class {e.get('class')!r} invalid")
            if not e.get("artefact"):
                err(f"{cid}: evidence entry has no artefact path")
            if "admissible" not in e:
                err(f"{cid}: evidence entry must state admissibility explicitly")

        # INVARIANT 7 -- a conjecture must not carry admissible evidence unnoticed.
        if status == "theoretical-conjecture" and any(
            e.get("admissible") for e in evidence
        ):
            warn(
                f"{cid}: status is theoretical-conjecture but admissible evidence "
                f"is attached; the status may be stale"
            )


def check_dag(dag_doc: dict, repos_doc: dict) -> None:
    nodes = dag_doc.get("nodes", [])
    ids = {n["id"] for n in nodes}
    repo_ids = {r["id"] for r in repos_doc.get("repos", [])} | {"ccs"}
    existing = {
        r["id"] for r in repos_doc.get("repos", []) if r.get("existence") == "exists"
    }

    for n in nodes:
        nid = n.get("id", "<no id>")
        if n.get("stage") not in STAGES:
            err(f"{nid}: stage {n.get('stage')!r} not in {sorted(STAGES)}")
        if n.get("repo") not in repo_ids:
            err(f"{nid}: unknown repo {n.get('repo')!r}")
        if not n.get("question"):
            err(f"{nid}: no research question recorded")
        for dep in n.get("depends_on", []):
            if dep not in ids:
                err(f"{nid}: depends_on unknown node {dep!r}")

        # A node in a repository that does not exist cannot have a readout.
        if n.get("repo") not in existing and n.get("readout"):
            err(f"{nid}: has a readout but its repository does not exist")

        # A node with a readout must say whether that readout is admissible.
        if n.get("readout") and n.get("admissible_as_evidence") is None:
            err(f"{nid}: has a readout but admissibility is unstated")

    # Cycle detection.
    colour: dict[str, int] = {}

    def visit(nid: str, path: list[str]) -> None:
        if colour.get(nid) == 2:
            return
        if colour.get(nid) == 1:
            err(f"dependency cycle: {' -> '.join(path + [nid])}")
            return
        colour[nid] = 1
        node = next((x for x in nodes if x["id"] == nid), None)
        if node:
            for dep in node.get("depends_on", []):
                visit(dep, path + [nid])
        colour[nid] = 2

    for n in nodes:
        visit(n["id"], [])


def check_repos(repos_doc: dict) -> None:
    for r in repos_doc.get("repos", []):
        rid = r.get("id", "<no id>")
        if r.get("existence") not in EXISTENCE:
            err(f"{rid}: existence {r.get('existence')!r} not in {sorted(EXISTENCE)}")
        if r.get("existence") == "planned" and r.get("observed"):
            err(f"{rid}: marked planned but carries observed remote state")
        if r.get("existence") == "exists" and not r.get("observed"):
            warn(f"{rid}: exists but has never been reconciled")
        if not r.get("role"):
            err(f"{rid}: no role recorded")


RESULT_LANGUAGE = [
    # Phrases that would indicate the umbrella repo has started reporting results.
    (r"\bwe (?:show|demonstrate|prove|find that)\b", "asserts a finding"),
    (r"\bour (?:results|experiments) (?:show|demonstrate|confirm)\b", "asserts results"),
    (r"\b(?:significantly|substantially) (?:outperform|better than)\b", "asserts a comparison"),
    (r"\bstate[- ]of[- ]the[- ]art\b", "SOTA claim"),
    (r"\bachieves? (?:\d+(?:\.\d+)?%|superior)\b", "asserts a measured outcome"),
]


def check_prose() -> None:
    """Scan committed prose for language that reports results.

    The umbrella repository maintains theory and evidence status. It is not a
    place where an untested architecture is described as working. This check is
    a coarse tripwire, not a proof; it is meant to fail loudly during review.
    """
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(errors="ignore")
        # Allow quoted negative examples in the style guide itself.
        if path.name == "WRITING-RULES.md":
            continue
        for pattern, why in RESULT_LANGUAGE:
            for m in re.finditer(pattern, text, flags=re.IGNORECASE):
                line = text[: m.start()].count("\n") + 1
                err(
                    f"{path.relative_to(ROOT)}:{line}: result language "
                    f"({why}): {m.group(0)!r}"
                )


def main() -> int:
    claims_doc = load("claims.json")
    repos_doc = load("repos.json")
    dag_doc = load("dag.json")

    if not errors:
        check_repos(repos_doc)
        check_dag(dag_doc, repos_doc)
        check_claims(claims_doc, dag_doc, repos_doc)
        check_prose()

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")

    claims = claims_doc.get("claims", [])
    if not errors:
        counts: dict[str, int] = {}
        for c in claims:
            counts[c["status"]] = counts.get(c["status"], 0) + 1
        print(f"OK    {len(claims)} claims, {len(dag_doc.get('nodes', []))} DAG nodes")
        for s in STATUSES:
            if counts.get(s):
                print(f"      {s}: {counts[s]}")
        supported = sum(
            counts.get(s, 0) for s in ("pilot-supported", "confirmatory-supported")
        )
        print(
            f"      claims with empirical support: {supported}"
            + ("" if supported else "  <- nothing in this programme is established yet")
        )
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
