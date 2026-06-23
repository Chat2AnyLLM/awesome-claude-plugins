#!/usr/bin/env python3
from __future__ import annotations
import json, os
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

UA = "awesome-plugin-metadata/1.0"

def _jget(url: str, token: str | None) -> dict:
    headers = {"User-Agent": UA, "Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urlopen(Request(url, headers=headers), timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

def fetch_repos_from_sources(sources: list[dict]) -> list[dict]:
    token = os.environ.get("GITHUB_TOKEN")
    merged = {}
    for source in sources:
        data = _jget(source["url"], token)
        items = data.values() if isinstance(data, dict) else data
        for entry in items:
            owner = entry.get("repoOwner") or entry.get("owner") or ""
            name = entry.get("repoName") or entry.get("name") or ""
            if owner and name and entry.get("enabled", True):
                merged[f"{owner}/{name}"] = entry
    return list(merged.values())

def _fields(entry: dict) -> dict:
    owner = entry.get("repoOwner") or entry.get("owner") or ""
    name = entry.get("repoName") or entry.get("name") or ""
    return {
        "owner": owner,
        "name": name,
        "branch": entry.get("repoBranch") or entry.get("branch") or "main",
        "path": (entry.get("pluginPath") or ".claude-plugin").strip("/"),
        "display_name": entry.get("name") if entry.get("repoOwner") else f"{owner}/{name}",
    }

def _count_plugins(entry: dict, token: str | None) -> dict:
    f = _fields(entry)
    full = f"{f['owner']}/{f['name']}"
    candidates = []
    if f['path']:
        candidates.append(f"{f['path']}/marketplace.json")
    candidates.append('.claude-plugin/marketplace.json')
    last = 404
    for rel in candidates:
        try:
            data = _jget(f"https://raw.githubusercontent.com/{full}/{f['branch']}/{rel}", token)
            plugins = data.get('plugins') if isinstance(data, dict) else None
            if isinstance(plugins, list):
                return {"full": full, "count": len(plugins), "status": "ok", "note": "", "branch": f['branch'], "path": rel.rsplit('/',1)[0]}
        except HTTPError as e:
            last = e.code
            continue
        except (URLError, OSError, TimeoutError) as e:
            return {"full": full, "count": 0, "status": "error", "note": str(e)[:120], "branch": f['branch'], "path": f['path']}
    status = "missing" if last == 404 else "forbidden" if last == 403 else "error"
    return {"full": full, "count": 0, "status": status, "note": f"HTTP {last}; marketplace.json not found", "branch": f['branch'], "path": f['path']}

def count_plugins(entries: list[dict], max_workers: int = 8) -> dict[str, dict]:
    token = os.environ.get("GITHUB_TOKEN")
    out = {}
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        futs = {ex.submit(_count_plugins, e, token): e for e in entries}
        for fut in as_completed(futs):
            r = fut.result()
            out[r["full"]] = r
    return out

def render_readme(entries: list[dict], counts: dict[str, dict]) -> str:
    rows = []
    for e in entries:
        f = _fields(e)
        full = f"{f['owner']}/{f['name']}"
        rows.append({**f, **counts.get(full, {"count": 0, "status": "error", "note": "missing count"})})
    rows.sort(key=lambda r: (r["status"] != "ok", r["owner"].lower(), r["name"].lower()))
    total = sum(r["count"] for r in rows)
    ok = sum(1 for r in rows if r["status"] == "ok")
    bad = len(rows) - ok
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Awesome Claude Plugins",
        "",
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "",
        "Metadata catalog for Claude plugin marketplaces. This repo does **not** clone or mirror upstream content; it tracks marketplace repos from [awesome-repo-configs](https://github.com/Chat2AnyLLM/awesome-repo-configs) and counts entries in each `marketplace.json` via GitHub API.",
        "",
        f"- Enabled marketplaces: **{len(rows)}**",
        f"- Discoverable plugins: **{total:,}**",
        f"- Healthy repos: **{ok}** · Unavailable: **{bad}**",
        f"- Last updated: **{ts}**",
        "",
        "## Source Catalog",
        "",
        "| Repository | Plugins | Branch | Path | Status | Note |",
        "| --- | ---: | --- | --- | --- | --- |",
    ]
    for r in rows:
        repo = f"[{r['full']}](https://github.com/{r['full']})"
        path = f"`{r['path'] or '.'}`"
        status = {"ok": "✅ ok", "missing": "❌ missing", "forbidden": "⛔ forbidden", "error": "❌ error"}.get(r['status'], r['status'])
        note = (r.get("note") or "").replace("|", "\\|")
        lines.append(f"| {repo} | {r['count']:,} | `{r['branch']}` | {path} | {status} | {note} |")
    lines += ["", "## Contributing", "", "Add or disable source repositories in [awesome-repo-configs](https://github.com/Chat2AnyLLM/awesome-repo-configs). This repository is a metadata-only catalog."]
    return "\n".join(lines) + "\n"
