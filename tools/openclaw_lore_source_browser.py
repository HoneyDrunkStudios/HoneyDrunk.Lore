#!/usr/bin/env python3
"""Browser-backed producer for HoneyDrunk.Lore.

Uses the OpenClaw managed browser profile to snapshot login-walled sources
(X list + configured Discord announcement channels) and writes qualifying
snapshots into raw/ as markdown. This is intentionally conservative: Discord
channels must be explicit URLs in tools/browser-sources.json so we do not scrape
DMs/help/chat noise by accident.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import multiprocessing as mp
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(r"C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.Lore")
RAW = REPO / "raw"
OUTPUT = REPO / "output"
CONFIG = REPO / "tools" / "browser-sources.json"
OPENCLAW = shutil.which("openclaw.cmd") or shutil.which("openclaw") or "openclaw"

KEYWORDS = [
    "agent", "agents", "ai", "llm", "model", "mcp", "tool", "eval", "prompt",
    "dotnet", ".net", "aspire", "c#", "nuget", "azure", "foundry", "container",
    "github actions", "ci/cd", "workflow", "observability", "architecture",
    "unity", "blender", "game dev", "gamedev", "discord", "release", "announce",
]


def run(cmd: list[str], timeout: int = 90) -> str:
    """Run a command with a hard timeout.

    subprocess.run(timeout=...) can leave child node/openclaw processes alive on
    Windows when a browser call wedges. Use Popen + taskkill /T so each channel
    scrape is bounded and the scheduled job can continue.
    """
    env = dict(os.environ)
    env.setdefault("PYTHONIOENCODING", "utf-8")
    env.setdefault("NO_COLOR", "1")
    proc = subprocess.Popen(
        cmd,
        cwd=str(REPO),
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        env=env,
    )
    try:
        stdout, _ = proc.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        kill_process_tree(proc.pid)
        stdout, _ = proc.communicate(timeout=5)
        output = sanitize_output(stdout)
        raise TimeoutError(f"timed out after {timeout}s: {' '.join(cmd)}\n{output[-2000:]}")

    output = sanitize_output(stdout)
    if proc.returncode != 0:
        raise RuntimeError(output.strip() or f"command failed: {' '.join(cmd)}")
    return output


def kill_process_tree(pid: int) -> None:
    if os.name == "nt":
        subprocess.run(["taskkill", "/PID", str(pid), "/T", "/F"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        try:
            os.kill(pid, 9)
        except ProcessLookupError:
            pass


def sanitize_output(value: str | None) -> str:
    return (value or "").encode("ascii", "ignore").decode("ascii")


def browser(profile: str, *args: str, timeout: int = 90) -> str:
    return run([OPENCLAW, "browser", "--browser-profile", profile, *args], timeout=timeout)


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return (text[:80] or "browser-source").strip("-")


def yaml_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"').strip()


def score(text: str) -> int:
    hay = text.lower()
    return sum(1 for kw in KEYWORDS if kw in hay)


def clipped_snapshot(text: str, max_chars: int = 35000) -> str:
    # Keep snapshots useful but bounded. Prefer top of page; browser snapshots are already readable.
    text = re.sub(r"\n{4,}", "\n\n\n", text).strip()
    return text[:max_chars]


def write_raw(source: str, title: str, category: str, source_type: str, body: str, suffix: str) -> str:
    today = dt.date.today().isoformat()
    RAW.mkdir(parents=True, exist_ok=True)
    path = RAW / f"{today}-{source_type}-{slugify(suffix)}.md"
    n = 2
    while path.exists():
        path = RAW / f"{today}-{source_type}-{slugify(suffix)}-{n}.md"
        n += 1
    content = f'''---\nsource: "{yaml_escape(source)}"\ntitle: "{yaml_escape(title)}"\nauthor: "OpenClaw browser"\ndate_published: "unknown"\ndate_clipped: "{today}"\ncategory: "{yaml_escape(category)}"\nsource_type: "{source_type}"\n---\n\n# {title}\n\nSource: {source}\n\n{body}\n'''
    path.write_text(content, encoding="utf-8")
    return path.name


def source_x(profile: str, list_url: str, dry_run: bool) -> tuple[list[str], list[str]]:
    written: list[str] = []
    notes: list[str] = []
    # Assume the managed browser is already available; the scheduled wrapper starts it once.
    browser(profile, "open", list_url, "--label", "lore-x-list", timeout=120)
    snap = browser(profile, "snapshot", timeout=120)
    if "Log in" in snap and "Sign up" in snap:
        notes.append("X appears logged out; open the managed browser and log in again.")
        return written, notes
    s = score(snap)
    if s < 1:
        notes.append("X snapshot had no matching keywords; skipped.")
        return written, notes
    today = dt.date.today().isoformat()
    source = f"{list_url}#snapshot-{today}"
    title = f"X list snapshot — {today}"
    body = clipped_snapshot(snap)
    if dry_run:
        notes.append(f"DRY RUN: would write X list snapshot, score {s}.")
    else:
        written.append(write_raw(source, title, "AI / LLM Research & Tooling", "clipper", body, "x-list-snapshot"))
    return written, notes


def scrape_discord_channel_worker(profile: str, name: str, focus: str, url: str, dry_run: bool, label: str, queue: mp.Queue) -> None:
    notes: list[str] = []
    written: list[str] = []
    try:
        notes.append(f"Discord {name}: opening {url}")
        browser(profile, "open", url, "--label", label, timeout=45)
        browser(profile, "focus", label, timeout=30)
        notes.append(f"Discord {name}: snapshotting")
        snap = browser(profile, "snapshot", timeout=90)
        if "Welcome back" in snap and "Log In" in snap:
            notes.append("Discord appears logged out; open the managed browser and log in again.")
        else:
            s = score(snap)
            if s < 1:
                notes.append(f"Discord {name}: no matching keywords; skipped {url}.")
            else:
                today = dt.date.today().isoformat()
                source = f"{url}#snapshot-{today}"
                title = f"Discord {name} announcements snapshot — {today}"
                body = f"Configured focus: {focus}\n\n" + clipped_snapshot(snap)
                if dry_run:
                    notes.append(f"DRY RUN: would write Discord {name}, score {s}.")
                else:
                    written.append(write_raw(source, title, "Community / Announcements", "clipper", body, f"discord-{name}"))
    except Exception as e:
        notes.append(f"Discord {name}: failed {url}: {e}")
    finally:
        try:
            browser(profile, "close", label, timeout=15)
        except Exception:
            pass
        queue.put({"written": written, "notes": notes})


def append_progress(path: Path, message: str) -> None:
    with path.open("a", encoding="utf-8") as fh:
        fh.write(f"{dt.datetime.now().isoformat(timespec='seconds')} {message}\n")


def source_discord(profile: str, cfg: dict, dry_run: bool, limit: int = 0, channel_timeout: int = 180) -> tuple[list[str], list[str]]:
    written: list[str] = []
    notes: list[str] = []
    communities = cfg.get("communities") or []
    configured = 0
    processed = 0
    progress_path = OUTPUT / "openclaw-browser-sourcing-progress.log"
    OUTPUT.mkdir(parents=True, exist_ok=True)
    progress_path.write_text("", encoding="utf-8")

    for community in communities:
        name = community.get("name", "Discord")
        focus = community.get("focus", "announcements")
        urls = [u for u in community.get("channelUrls", []) if isinstance(u, str) and u.startswith("https://discord.com/channels/")]
        if not urls:
            notes.append(f"Discord setup needed: add announcement channel URL(s) for {name} in tools/browser-sources.json.")
            continue
        configured += len(urls)
        for idx, url in enumerate(urls, start=1):
            if limit and processed >= limit:
                notes.append(f"Discord limit reached after {processed} channel(s).")
                return written, notes
            processed += 1
            label = f"lore-discord-{slugify(name)}-{idx}-{int(dt.datetime.now().timestamp())}"
            append_progress(progress_path, f"Discord {name}: worker start {url}")
            queue: mp.Queue = mp.Queue()
            proc = mp.Process(target=scrape_discord_channel_worker, args=(profile, name, focus, url, dry_run, label, queue))
            proc.start()
            proc.join(channel_timeout)
            if proc.is_alive():
                kill_process_tree(proc.pid or 0)
                proc.join(10)
                msg = f"Discord {name}: timed out after {channel_timeout}s; skipped {url}."
                notes.append(msg)
                append_progress(progress_path, msg)
                continue
            if proc.exitcode not in (0, None):
                msg = f"Discord {name}: worker exited with code {proc.exitcode}; skipped {url}."
                notes.append(msg)
                append_progress(progress_path, msg)
                continue
            result = queue.get() if not queue.empty() else {"written": [], "notes": [f"Discord {name}: worker produced no result; skipped {url}."]}
            written.extend(result.get("written", []))
            for note in result.get("notes", []):
                notes.append(note)
                append_progress(progress_path, note)
    if configured == 0:
        notes.append("No Discord channel URLs configured yet; browser login is ready, but channel targeting still needs URLs.")
    return written, notes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--x-only", action="store_true")
    parser.add_argument("--discord-only", action="store_true")
    parser.add_argument("--discord-limit", type=int, default=0, help="Maximum Discord channel URLs to process; 0 means all.")
    parser.add_argument("--discord-channel-timeout", type=int, default=180, help="Hard timeout per Discord channel in seconds.")
    args = parser.parse_args()

    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    profile = cfg.get("browserProfile", "openclaw")
    written: list[str] = []
    notes: list[str] = []
    failures: list[str] = []

    try:
        browser(profile, "start", timeout=120)
    except Exception as e:
        failures.append(f"Browser start: {type(e).__name__}: {e}")

    try:
        if not failures and not args.discord_only and cfg.get("x", {}).get("enabled", True):
            w, n = source_x(profile, cfg["x"]["listUrl"], args.dry_run)
            written.extend(w); notes.extend(n)
    except Exception as e:
        failures.append(f"X: {type(e).__name__}: {e}")

    try:
        if not failures and not args.x_only and cfg.get("discord", {}).get("enabled", True):
            w, n = source_discord(profile, cfg["discord"], args.dry_run, args.discord_limit, args.discord_channel_timeout)
            written.extend(w); notes.extend(n)
    except Exception as e:
        failures.append(f"Discord: {type(e).__name__}: {e}")

    OUTPUT.mkdir(parents=True, exist_ok=True)
    summary = [
        "# OpenClaw Lore Browser Sourcing — Last Run",
        "",
        f"Timestamp: {dt.datetime.now().isoformat(timespec='seconds')}",
        f"Mode: {'dry-run' if args.dry_run else 'write'}",
        f"Browser profile: {profile}",
        f"Saved: {len(written)}",
        "",
        "## Files written",
    ]
    summary.extend((f"- raw/{name}" for name in written) if written else ["_None_"])
    summary.extend(["", "## Notes"])
    summary.extend((f"- {note}" for note in notes) if notes else ["_None_"])
    summary.extend(["", "## Failures"])
    summary.extend((f"- {failure}" for failure in failures) if failures else ["_None_"])
    if not args.dry_run:
        (OUTPUT / "openclaw-browser-sourcing-last-run.md").write_text("\n".join(summary) + "\n", encoding="utf-8")
    else:
        print("\n".join(summary))
    print(f"Browser sourced {len(written)} items; notes {len(notes)}; failures {len(failures)}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
