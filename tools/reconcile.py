#!/usr/bin/env python3
"""Reconcile the umbrella registry against the real state of the sibling repos.

READ-ONLY BY CONSTRUCTION. This tool issues GET requests only. It never pushes,
never opens issues or pull requests, and never edits a sibling repository. The
umbrella repository observes the programme; it does not steer experimental
protocols from here. See docs/RECONCILIATION-POLICY.md.

Usage:
    python3 tools/reconcile.py            # report drift, exit 1 if drift found
    python3 tools/reconcile.py --write    # additionally refresh 'observed' blocks
"""

from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REPOS = ROOT / "ledger" / "repos.json"

# Every command this tool is permitted to run. Anything mutating is absent.
READ_ONLY_ENDPOINTS = ("repos/",)


def gh_api(path: str) -> tuple[bool, object]:
    """GET a GitHub API path via the gh CLI. Refuses non-read-only paths."""
    if not path.startswith(READ_ONLY_ENDPOINTS):
        raise SystemExit(f"refusing non-read-only endpoint: {path}")
    proc = subprocess.run(
        ["gh", "api", "-X", "GET", path],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        return False, proc.stderr.strip()
    try:
        return True, json.loads(proc.stdout)
    except json.JSONDecodeError:
        return False, "unparseable response"


def observe(slug: str) -> dict | None:
    ok, data = gh_api(f"repos/{slug}")
    if not ok:
        return None
    assert isinstance(data, dict)
    obs: dict = {
        "default_branch": data.get("default_branch"),
        "visibility": "private" if data.get("private") else "public",
        "pushed_at": data.get("pushed_at"),
    }
    ok, commits = gh_api(f"repos/{slug}/commits?per_page=1")
    if ok and isinstance(commits, list) and commits:
        obs["head"] = commits[0]["sha"][:7]
    ok, contents = gh_api(f"repos/{slug}/contents/results")
    if ok and isinstance(contents, list):
        real = [c for c in contents if c["name"] not in (".gitkeep", ".gitignore")]
        obs["results_dir_populated"] = bool(real)
    return obs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="refresh observed blocks")
    args = ap.parse_args()

    doc = json.loads(REPOS.read_text())
    drift: list[str] = []
    notes: list[str] = []

    for repo in doc["repos"]:
        slug = repo["slug"]
        declared = repo["existence"]
        live = observe(slug)

        if live is None:
            if declared == "exists":
                drift.append(
                    f"{slug}: registry says 'exists' but the repository was not "
                    f"found. Either it was deleted/renamed, or it is private and "
                    f"outside this token's scope."
                )
            else:
                notes.append(f"{slug}: still planned, not created.")
            continue

        if declared == "planned":
            drift.append(
                f"{slug}: registry says 'planned' but the repository now EXISTS. "
                f"Create its DAG node design and reclassify before citing it."
            )
            if args.write:
                repo["existence"] = "exists"
                repo.pop("existence_note", None)
                repo["observed"] = live
            continue

        prev = repo.get("observed") or {}
        for field in ("head", "pushed_at", "default_branch", "visibility"):
            if prev.get(field) and live.get(field) and prev[field] != live[field]:
                drift.append(
                    f"{slug}: {field} changed {prev[field]!r} -> {live[field]!r}"
                )

        if live.get("results_dir_populated") and not prev.get("results_dir_populated"):
            drift.append(
                f"{slug}: results/ is now POPULATED. A readout may exist. Review "
                f"the run manifests and update ledger/claims.json evidence before "
                f"any claim status is changed."
            )

        if args.write:
            merged = dict(prev)
            merged.update(live)
            repo["observed"] = merged

    if args.write:
        import datetime

        doc["last_reconciled"] = datetime.date.today().isoformat()
        REPOS.write_text(json.dumps(doc, indent=2) + "\n")
        print(f"wrote {REPOS.relative_to(ROOT)}")

    for n in notes:
        print(f"note   {n}")
    for d in drift:
        print(f"DRIFT  {d}")
    if not drift:
        print("OK     registry matches observed remote state")
    return 1 if drift and not args.write else 0


if __name__ == "__main__":
    sys.exit(main())
