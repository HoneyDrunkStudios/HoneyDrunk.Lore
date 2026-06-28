#!/usr/bin/env python3
"""Run Birdclaw recent X sourcing for HoneyDrunk.Lore.

This wrapper keeps the Lore integration honest:
- it attempts a live Birdclaw refresh before converting anything;
- it refuses to write from local-only cache unless explicitly allowed;
- it records a run summary for the daily signal review.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(r"C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.Lore")
OUTPUT = REPO / "output"
CONVERTER = REPO / "tools" / "lore_source_birdclaw.py"
BIRDCLAW = shutil.which("birdclaw.cmd") or shutil.which("birdclaw.exe") or shutil.which("birdclaw")


def run(command: list[str], *, input_text: str | None = None, timeout: int = 120) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        input=input_text,
        cwd=str(REPO),
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
    )


def birdclaw_command(*args: str) -> list[str]:
    if not BIRDCLAW:
        raise FileNotFoundError("birdclaw command not found on PATH")
    return [BIRDCLAW, *args]


def short_output(value: str, limit: int = 6000) -> str:
    value = value.strip()
    if len(value) <= limit:
        return value
    return value[:limit] + "\n...[truncated]"


def json_or_none(text: str) -> object | None:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Refresh Birdclaw and convert recent X signals into Lore raw files.")
    parser.add_argument("--resource", choices=("home", "mentions", "authored"), default="home")
    parser.add_argument("--query", default="", help="Optional local search query.")
    parser.add_argument("--since", default="", help="Include tweets created at or after this date. Defaults to yesterday.")
    parser.add_argument("--limit", type=int, default=25)
    parser.add_argument("--min-likes", type=int, default=50)
    parser.add_argument("--max-pages", type=int, default=1)
    parser.add_argument("--account", default="", help="Optional Birdclaw account id.")
    parser.add_argument("--category", default="AI / LLM Research & Tooling")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-live-sync", action="store_true")
    parser.add_argument("--allow-local-cache", action="store_true", help="Allow conversion even when live refresh fails.")
    args = parser.parse_args()

    OUTPUT.mkdir(parents=True, exist_ok=True)
    since = args.since or (dt.date.today() - dt.timedelta(days=1)).isoformat()
    timestamp = dt.datetime.now().isoformat(timespec="seconds")

    auth = run(birdclaw_command("auth", "status", "--json"), timeout=30)
    auth_json = json_or_none(auth.stdout)

    sync_attempted = not args.no_live_sync
    sync_ok = False
    sync_output = ""
    if sync_attempted:
        sync_command = [
            *birdclaw_command("sync", "timeline"),
            "--mode",
            "auto",
            "--limit",
            str(max(5, min(args.limit, 100))),
            "--max-pages",
            str(max(1, args.max_pages)),
            "--refresh",
        ]
        if args.account:
            sync_command.extend(["--account", args.account])
        sync = run(sync_command, timeout=120)
        sync_ok = sync.returncode == 0
        sync_output = sync.stdout
    else:
        sync_output = "Live sync skipped by --no-live-sync."

    search_command = [
        *birdclaw_command("search", "tweets"),
        "--resource",
        args.resource,
        "--hide-low-quality",
        "--min-likes",
        str(args.min_likes),
        "--since",
        since,
        "--limit",
        str(args.limit),
        "--json",
    ]
    if args.query:
        search_command.append(args.query)

    conversion_output = ""
    search_output = ""
    wrote_from_cache = False
    converter_returncode = 0
    items_count = 0

    can_convert = sync_ok or args.no_live_sync or args.allow_local_cache
    if can_convert:
        search = run(search_command, timeout=60)
        search_output = search.stdout
        if search.returncode != 0:
            converter_returncode = search.returncode
            conversion_output = "Birdclaw search failed; converter was not run."
        else:
            parsed = json_or_none(search.stdout)
            if isinstance(parsed, list):
                items_count = len(parsed)
            converter_command = [
                sys.executable,
                str(CONVERTER),
                "-",
                "--max-items",
                str(args.limit),
                "--category",
                args.category,
            ]
            if args.dry_run:
                converter_command.append("--dry-run")
            converter = run(converter_command, input_text=search.stdout, timeout=60)
            converter_returncode = converter.returncode
            conversion_output = converter.stdout
            wrote_from_cache = not sync_ok
    else:
        conversion_output = "Skipped conversion because live Birdclaw refresh failed and --allow-local-cache was not set."

    blocker = ""
    if sync_attempted and not sync_ok:
        blocker = "Live Birdclaw refresh failed; check xurl auth or bird command configuration."
    if converter_returncode != 0:
        blocker = (blocker + " " if blocker else "") + "Birdclaw conversion failed."

    lines = [
        "# Lore Birdclaw Sourcing - Last Run",
        "",
        f"Timestamp: {timestamp}",
        f"Mode: {'dry-run' if args.dry_run else 'write'}",
        f"Resource: {args.resource}",
        f"Since: {since}",
        f"Limit: {args.limit}",
        f"Live sync attempted: {'yes' if sync_attempted else 'no'}",
        f"Live sync succeeded: {'yes' if sync_ok else 'no'}",
        f"Converted from local cache: {'yes' if wrote_from_cache else 'no'}",
        f"Items exported for conversion: {items_count}",
        "",
        "## Auth status",
        "",
        "```json",
        json.dumps(auth_json, indent=2) if auth_json is not None else short_output(auth.stdout),
        "```",
        "",
        "## Sync output",
        "",
        "```text",
        short_output(sync_output) or "_None_",
        "```",
        "",
        "## Conversion output",
        "",
        "```text",
        short_output(conversion_output) or "_None_",
        "```",
        "",
        "## Blockers",
        "",
        f"- {blocker}" if blocker else "_None_",
        "",
    ]
    summary = "\n".join(lines)
    (OUTPUT / "lore-birdclaw-sourcing-last-run.md").write_text(summary, encoding="utf-8")
    print(summary)
    return 0 if converter_returncode == 0 else converter_returncode


if __name__ == "__main__":
    raise SystemExit(main())
