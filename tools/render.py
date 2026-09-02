#!/usr/bin/env python3
"""Render human-readable views from the machine-readable ledger.

The JSON files under ledger/ are the single source of truth. The Markdown
tables in docs/CLAIM-LEDGER.md and docs/DEPENDENCY-DAG.md are generated from
them so the two can never disagree. Edit the JSON, then re-run:

    python3 tools/render.py

Regions are replaced between GENERATED markers; surrounding prose is preserved.
"""

from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LEDGER = ROOT / "ledger"

BEGIN = "<!-- GENERATED:{key} -- do not edit by hand; run tools/render.py -->"
END = "<!-- /GENERATED:{key} -->"

STATUS_MARK = {
    "theoretical-conjecture": "conjecture",
    "implemented": "implemented (no evidence)",
    "pilot-supported": "pilot-supported",
    "confirmatory-supported": "CONFIRMATORY",
    "falsified": "FALSIFIED",
    "unresolved": "unresolved",
}


def splice(path: pathlib.Path, key: str, body: str) -> None:
    text = path.read_text()
    begin, end = BEGIN.format(key=key), END.format(key=key)
    pattern = re.compile(
        re.escape(begin) + r".*?" + re.escape(end), re.DOTALL
    )
    if not pattern.search(text):
        raise SystemExit(f"{path.name}: no GENERATED:{key} region found")
    path.write_text(pattern.sub(f"{begin}\n\n{body.strip()}\n\n{end}", text))


def render_claims(claims: dict, dag: dict) -> str:
    rows = [
        "| Claim | Statement (abbreviated) | Status | Implementation | Tested by |",
        "|---|---|---|---|---|",
    ]
    for c in claims["claims"]:
        stmt = c["statement"]
        stmt = stmt if len(stmt) <= 110 else stmt[:107].rsplit(" ", 1)[0] + "…"
        tests = ", ".join(f"`{s}`" for s in c["supported_by"]) or "—"
        rows.append(
            f"| **{c['id']}** {c['title']} | {stmt} | `{STATUS_MARK[c['status']]}` "
            f"| {c['implementation']} | {tests} |"
        )
    counts: dict[str, int] = {}
    for c in claims["claims"]:
        counts[c["status"]] = counts.get(c["status"], 0) + 1
    supported = counts.get("pilot-supported", 0) + counts.get("confirmatory-supported", 0)
    summary = (
        f"\n**{len(claims['claims'])} claims. "
        f"{supported} with empirical support. "
        f"{counts.get('confirmatory-supported', 0)} confirmatory.**\n"
    )
    return "\n".join(rows) + "\n" + summary


def render_dag(dag: dict, repos: dict) -> str:
    exists = {r["id"] for r in repos["repos"] if r["existence"] == "exists"}
    lines = ["```mermaid", "graph TD"]
    for n in dag["nodes"]:
        nid = n["id"]
        key = re.sub(r"[^A-Za-z0-9]", "_", nid)
        label = nid.replace("/", "<br/>")
        stage = n["stage"]
        if n["repo"] not in exists and n["repo"] != "ccs":
            shape = f'{key}["{label}<br/><i>repo not created</i>"]'
            cls = "planned"
        elif stage == "pilot-complete":
            shape = f'{key}["{label}<br/><i>pilot only</i>"]'
            cls = "pilot"
        elif stage == "pre-result-scaffold":
            shape = f'{key}["{label}<br/><i>pre-result</i>"]'
            cls = "active"
        elif stage == "not-designed":
            shape = f'{key}["{label}<br/><i>not designed</i>"]'
            cls = "undesigned"
        else:
            shape = f'{key}["{label}<br/><i>{stage}</i>"]'
            cls = "planned"
        lines.append(f"  {shape}")
        lines.append(f"  class {key} {cls};")
    lines.append("")
    for n in dag["nodes"]:
        tgt = re.sub(r"[^A-Za-z0-9]", "_", n["id"])
        for dep in n["depends_on"]:
            src = re.sub(r"[^A-Za-z0-9]", "_", dep)
            lines.append(f"  {src} --> {tgt}")
    lines += [
        "",
        "  classDef active fill:#1f6feb,stroke:#1f6feb,color:#fff;",
        "  classDef pilot fill:#8b5cf6,stroke:#8b5cf6,color:#fff;",
        "  classDef planned fill:#30363d,stroke:#6e7681,color:#c9d1d9,stroke-dasharray:4 3;",
        "  classDef undesigned fill:#3d1d1d,stroke:#f85149,color:#ffa198,stroke-dasharray:4 3;",
        "```",
        "",
        "Solid nodes exist in code. Dashed nodes have no repository. "
        "The red node has no design and no host repository.",
        "",
        "| Node | Operator | Stage | Tests | Depends on |",
        "|---|---|---|---|---|",
    ]
    for n in dag["nodes"]:
        deps = ", ".join(f"`{d}`" for d in n["depends_on"]) or "—"
        tests = ", ".join(n["tests_claims"]) or "—"
        lines.append(
            f"| `{n['id']}` | {n['operator']} | {n['stage']} | {tests} | {deps} |"
        )
    return "\n".join(lines)


def main() -> int:
    claims = json.loads((LEDGER / "claims.json").read_text())
    dag = json.loads((LEDGER / "dag.json").read_text())
    repos = json.loads((LEDGER / "repos.json").read_text())
    splice(ROOT / "docs" / "CLAIM-LEDGER.md", "claims", render_claims(claims, dag))
    splice(ROOT / "docs" / "DEPENDENCY-DAG.md", "dag", render_dag(dag, repos))
    print("rendered docs/CLAIM-LEDGER.md, docs/DEPENDENCY-DAG.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
