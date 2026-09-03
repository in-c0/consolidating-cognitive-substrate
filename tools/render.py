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
        "| Claim | Domain | Statement (abbreviated) | Status | Implementation | Tested by |",
        "|---|---|---|---|---|---|",
    ]
    for c in claims["claims"]:
        stmt = c["statement"]
        stmt = stmt if len(stmt) <= 110 else stmt[:107].rsplit(" ", 1)[0] + "…"
        tests = ", ".join(f"`{s}`" for s in c["supported_by"]) or "—"
        rows.append(
            f"| **{c['id']}** {c['title']} | {c.get('domain', '—')} | {stmt} "
            f"| `{STATUS_MARK[c['status']]}` | {c['implementation']} | {tests} |"
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


def render_evidence(claims: dict, dag: dict, repos: dict) -> str:
    """Experiment -> claims, and the claims nothing can currently test."""
    exists = {r["id"] for r in repos["repos"] if r["existence"] == "exists"}
    by_claim: dict[str, list] = {}
    for n in dag["nodes"]:
        for cid in n["tests_claims"]:
            by_claim.setdefault(cid, []).append(n)

    lines = [
        "| Experiment | Repo exists | Stage | Can move | Admissible |",
        "|---|---|---|---|---|",
    ]
    for n in dag["nodes"]:
        ok = "yes" if (n["repo"] in exists or n["repo"] == "ccs") else "**no**"
        if n["repo"] == "ccs":
            ok = "**no repo**"
        adm = n.get("admissible_as_evidence")
        adm_s = {True: "yes", False: "**no**", None: "n/a"}[adm]
        claims_s = ", ".join(n["tests_claims"]) or "—"
        lines.append(
            f"| `{n['id']}` | {ok} | {n['stage']} | {claims_s} | {adm_s} |"
        )

    lines += ["", "### Claims with no runnable test", "",
              "| Claim | Blocked on |", "|---|---|"]
    blocked = 0
    for c in claims["claims"]:
        runnable = [
            n for n in by_claim.get(c["id"], [])
            if n["repo"] in exists and n["stage"] not in ("planned", "not-designed")
        ]
        if not runnable:
            reasons = []
            for n in by_claim.get(c["id"], []):
                if n["repo"] == "ccs":
                    reasons.append(
                        "no integration repository — deliberately undesigned"
                    )
                elif n["repo"] not in exists:
                    reasons.append(f"`{n['repo']}` does not exist")
                elif n["stage"] in ("planned", "not-designed"):
                    reasons.append(f"`{n['id']}` is {n['stage']}")
            uniq = sorted(set(reasons)) or ["no experiment mapped"]
            lines.append(f"| **{c['id']}** | {'; '.join(uniq)} |")
            blocked += 1
    lines += ["", f"**{blocked} of {len(claims['claims'])} claims have no runnable test.**"]

    # Evidence actually on file.
    lines += ["", "### Evidence on file", "",
              "| Claim | Artefact | Class | Admissible | Direction |", "|---|---|---|---|---|"]
    rows = 0
    for c in claims["claims"]:
        for e in c["evidence"]:
            lines.append(
                f"| {c['id']} | `{e['repo']}/{e['artefact']}` | {e['class']} "
                f"| {'yes' if e['admissible'] else '**no**'} | {e.get('direction', '—')} |"
            )
            rows += 1
    adm = sum(1 for c in claims["claims"] for e in c["evidence"] if e["admissible"])
    lines += ["", f"**{rows} evidence entries on file. {adm} admissible.**"]
    return "\n".join(lines)


def render_envelope(env: dict, repos: dict) -> str:
    """Coverage matrix for the common integration reporting envelope."""
    dims = env["dimensions"]
    tracks = [r["id"] for r in repos["repos"]]
    maps = env["track_mappings"]

    head = "| Dimension | Additive | " + " | ".join(
        t.replace("-", "&#8209;") for t in tracks
    ) + " |"
    lines = [head, "|---|---|" + "---|" * len(tracks)]
    for d in dims:
        cells = []
        for tr in tracks:
            m = maps.get(tr, {})
            if d["id"] in m.get("incommensurable", []):
                cells.append("**INCOMM**")
            elif d["id"] in m.get("mapped", {}):
                cells.append("mapped")
            elif "ALL" in m.get("unmapped", []):
                cells.append("—")
            elif d["id"] in m.get("unmapped", []):
                cells.append("—")
            else:
                cells.append("?")
        lines.append(
            f"| `{d['id']}` | {'yes' if d['additive'] else '**no**'} | "
            + " | ".join(cells) + " |"
        )

    total = len(dims) * len(tracks)
    mapped = sum(
        1 for d in dims for tr in tracks if d["id"] in maps.get(tr, {}).get("mapped", {})
    )
    incomm = sum(
        1 for d in dims for tr in tracks
        if d["id"] in maps.get(tr, {}).get("incommensurable", [])
    )
    lines += [
        "",
        "`mapped` = expressible in the common unit. `—` = the track has no such "
        "resource. `**INCOMM**` = the resource exists but has no non-arbitrary "
        "common unit, which **blocks integration**.",
        "",
        f"**{mapped} of {total} track/dimension cells mapped. "
        f"{incomm} incommensurable.**",
        "",
        "### Open problems",
        "",
        "| ID | Problem | Blocks |",
        "|---|---|---|",
    ]
    for op in env["open_problems"]:
        lines.append(
            f"| **{op['id']}** | {op['title']} | "
            + ", ".join(f"`{b}`" for b in op["blocks"]) + " |"
        )
    return "\n".join(lines)


def main() -> int:
    claims = json.loads((LEDGER / "claims.json").read_text())
    dag = json.loads((LEDGER / "dag.json").read_text())
    repos = json.loads((LEDGER / "repos.json").read_text())
    env = json.loads((LEDGER / "resource_envelope.json").read_text())
    splice(ROOT / "docs" / "CLAIM-LEDGER.md", "claims", render_claims(claims, dag))
    splice(ROOT / "docs" / "DEPENDENCY-DAG.md", "dag", render_dag(dag, repos))
    splice(
        ROOT / "docs" / "EVIDENCE-MAP.md",
        "evidence",
        render_evidence(claims, dag, repos),
    )
    splice(ROOT / "docs" / "RESOURCE-ENVELOPE.md", "envelope", render_envelope(env, repos))
    print(
        "rendered docs/CLAIM-LEDGER.md, docs/DEPENDENCY-DAG.md, "
        "docs/EVIDENCE-MAP.md, docs/RESOURCE-ENVELOPE.md"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
