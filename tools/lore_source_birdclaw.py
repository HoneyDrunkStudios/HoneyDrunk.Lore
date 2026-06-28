#!/usr/bin/env python3
"""Birdclaw-to-raw converter for HoneyDrunk.Lore.

This is an optional, operator-invoked sourcing lane for targeted X/Twitter
captures. It converts stable Birdclaw JSON exports into normal Lore raw
markdown files; it does not crawl X, authenticate to X, or compile raw files
into the wiki.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import urllib.parse
from pathlib import Path
from typing import Any

REPO = Path(r"C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.Lore")
RAW = REPO / "raw"
SOURCES_INDEX = REPO / "wiki" / "indexes" / "sources.md"

ITEM_LIST_KEYS = ("items", "tweets", "posts", "results", "data", "records")
TEXT_KEYS = ("text", "full_text", "plainText", "plain_text", "content", "body", "markdown", "summary")
URL_KEYS = ("url", "source", "source_url", "permalink", "tweet_url", "tweetUrl", "canonicalUrl", "canonical_url", "link")
ID_KEYS = ("id", "source_id", "tweet_id", "conversation_id", "status_id")
DATE_KEYS = ("created_at", "createdAt", "date", "published_at", "date_published", "timestamp")
AUTHOR_KEYS = ("author", "username", "userName", "handle", "user", "screen_name", "display_name", "name")
ENGAGEMENT_KEYS = {
    "like_count": ("likeCount", "like_count", "favorite_count", "favorites"),
    "repost_count": ("retweetCount", "repostCount", "retweet_count", "repost_count"),
    "reply_count": ("replyCount", "reply_count"),
    "quote_count": ("quoteCount", "quote_count"),
    "view_count": ("viewCount", "view_count", "impression_count"),
    "bookmark_count": ("bookmarkCount", "bookmark_count"),
}

SECRET_PATTERNS = [
    re.compile(r"discord(app)?\.com/api/webhooks/[0-9]+/[A-Za-z0-9._-]+"),
    re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]{20,}"),
    re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bASIA[0-9A-Z]{16}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    re.compile(r"(?i)(api[_-]?key|secret|token|password|cookie)\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{16,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
]


def read_json(path: str) -> Any:
    if path == "-":
        text = sys.stdin.read()
    else:
        text = Path(path).read_text(encoding="utf-8")
    return json.loads(text)


def iter_items(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, list):
        return [item for entry in value for item in iter_items(entry)]
    if not isinstance(value, dict):
        return []
    if has_item_shape(value):
        return [value]
    if isinstance(value.get("data"), list):
        return enrich_xurl_items(value)
    for key in ITEM_LIST_KEYS:
        nested = value.get(key)
        if isinstance(nested, (list, dict)):
            return iter_items(nested)
    return []


def enrich_xurl_items(envelope: dict[str, Any]) -> list[dict[str, Any]]:
    users_by_id: dict[str, dict[str, Any]] = {}
    includes = envelope.get("includes")
    if isinstance(includes, dict):
        users = includes.get("users")
        if isinstance(users, list):
            for user in users:
                if isinstance(user, dict) and user.get("id") is not None:
                    users_by_id[str(user["id"])] = user

    enriched: list[dict[str, Any]] = []
    for item in envelope.get("data") or []:
        if not isinstance(item, dict):
            continue
        normalized = dict(item)
        author_id = normalized.get("author_id") or normalized.get("authorId")
        if author_id is not None and str(author_id) in users_by_id:
            user = users_by_id[str(author_id)]
            normalized.setdefault("author", user.get("username") or user.get("name") or str(author_id))
            normalized.setdefault("author_name", user.get("name") or "")
        enriched.extend(iter_items(normalized))
    return enriched


def has_item_shape(value: dict[str, Any]) -> bool:
    return any(key in value for key in TEXT_KEYS) and (
        any(key in value for key in URL_KEYS) or any(key in value for key in ID_KEYS)
    )


def first_text(value: dict[str, Any], keys: tuple[str, ...]) -> str:
    for key in keys:
        candidate = value.get(key)
        if isinstance(candidate, str) and candidate.strip():
            return candidate.strip()
        if isinstance(candidate, int):
            return str(candidate)
        if isinstance(candidate, dict):
            nested = first_text(candidate, AUTHOR_KEYS + URL_KEYS + ID_KEYS + DATE_KEYS)
            if nested:
                return nested
    return ""


def author_text(item: dict[str, Any]) -> str:
    raw = first_text(item, AUTHOR_KEYS)
    if not raw:
        user = item.get("user")
        if isinstance(user, dict):
            raw = first_text(user, AUTHOR_KEYS)
    raw = raw.strip()
    if raw and not raw.startswith("@") and re.fullmatch(r"[A-Za-z0-9_]{1,32}", raw):
        return "@" + raw
    return raw or "unknown"


def source_url(item: dict[str, Any]) -> str:
    url = first_text(item, URL_KEYS)
    if url:
        return canonical_url(url)
    source_id = source_id_text(item)
    if source_id:
        return f"https://x.com/i/web/status/{source_id}"
    return ""


def source_id_text(item: dict[str, Any]) -> str:
    for key in ID_KEYS:
        candidate = item.get(key)
        if isinstance(candidate, (str, int)) and str(candidate).strip():
            return str(candidate).strip()
    return ""


def first_int(value: dict[str, Any], keys: tuple[str, ...]) -> int | None:
    for key in keys:
        candidate = value.get(key)
        if isinstance(candidate, bool):
            continue
        if isinstance(candidate, int):
            return candidate
        if isinstance(candidate, float) and candidate.is_integer():
            return int(candidate)
        if isinstance(candidate, str):
            text = candidate.replace(",", "").strip()
            if re.fullmatch(r"\d+", text):
                return int(text)
    return None


def engagement_counts(item: dict[str, Any]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for label, keys in ENGAGEMENT_KEYS.items():
        value = first_int(item, keys)
        if value is not None:
            counts[label] = value
    return counts


def engagement_summary(counts: dict[str, int]) -> str:
    labels = (
        ("like_count", "likes"),
        ("repost_count", "reposts"),
        ("reply_count", "replies"),
        ("quote_count", "quotes"),
        ("view_count", "views"),
        ("bookmark_count", "bookmarks"),
    )
    return ", ".join(f"{counts[key]} {label}" for key, label in labels if key in counts)


def canonical_url(url: str) -> str:
    url = url.strip()
    parsed = urllib.parse.urlsplit(url)
    path = parsed.path.rstrip("/") if parsed.path != "/" else parsed.path
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    query = [
        (key, value)
        for key, value in query
        if not key.lower().startswith("utm_")
        and key.lower() not in {"token", "auth", "authorization", "code", "sig", "signature", "api_key", "apikey"}
    ]
    return urllib.parse.urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), path, urllib.parse.urlencode(query), ""))


def normalize_date(value: str) -> str:
    value = value.strip()
    if not value:
        return "unknown"
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return value
    try:
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).date().isoformat()
    except ValueError:
        pass
    for fmt in ("%a %b %d %H:%M:%S %z %Y", "%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S%z"):
        try:
            return dt.datetime.strptime(value, fmt).date().isoformat()
        except ValueError:
            continue
    return value


def clip_title(author: str, text: str) -> str:
    clean = re.sub(r"\s+", " ", text).strip()
    clean = clean[:90].rstrip()
    return f"X signal: {author} - {clean}" if clean else f"X signal: {author}"


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return (text[:80] or "x-signal").strip("-")


def yaml_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"').strip()


def redact_secrets(text: str) -> tuple[str, int]:
    redactions = 0
    for pattern in SECRET_PATTERNS:
        text, count = pattern.subn("[redacted-secret-like-value]", text)
        redactions += count
    return text, redactions


def sanitize_url_secrets(text: str) -> tuple[str, int]:
    redactions = 0

    def replace_url(match: re.Match[str]) -> str:
        nonlocal redactions
        original = match.group(0)
        cleaned = canonical_url(original)
        if cleaned != original:
            redactions += 1
        return cleaned

    return re.sub(r"https?://[^\s)>\]]+", replace_url, text), redactions


def known_sources(raw_dir: Path, sources_index: Path) -> tuple[set[str], set[str]]:
    urls: set[str] = set()
    ids: set[str] = set()
    if sources_index.exists():
        urls.update(canonical_url(match) for match in re.findall(r"https?://[^)\s]+", sources_index.read_text(encoding="utf-8", errors="ignore")))
    for md in raw_dir.glob("*.md"):
        text = md.read_text(encoding="utf-8", errors="ignore")[:2500]
        for key in ("source", "canonical_source"):
            match = re.search(rf"^{key}:\s*[\"']?([^\"'\n]+)", text, re.M)
            if match:
                urls.add(canonical_url(match.group(1).strip()))
        for key in ("source_id", "birdclaw_id"):
            match = re.search(rf"^{key}:\s*[\"']?([^\"'\n]+)", text, re.M)
            if match:
                ids.add(match.group(1).strip())
    return urls, ids


def item_to_markdown(item: dict[str, Any], category: str, clipped_date: str) -> tuple[str, str, str, int, str]:
    text = first_text(item, TEXT_KEYS)
    text, url_redactions = sanitize_url_secrets(text)
    text, redactions = redact_secrets(text)
    redactions += url_redactions
    author = author_text(item)
    url = source_url(item)
    source_id = source_id_text(item)
    published = normalize_date(first_text(item, DATE_KEYS))
    title = clip_title(author, text)
    related_links = related_link_lines(item)
    counts = engagement_counts(item)
    engagement = engagement_summary(counts)

    body = [
        f"# {title}",
        "",
        f"Source: {url}",
        f"Author: {author}",
        f"Published: {published}",
    ]
    if engagement:
        body.append(f"Engagement: {engagement}")
    body.extend(["", "## Captured X Signal", "", text])
    if related_links:
        body.extend(["", "## Related Links", "", *related_links])
    if redactions:
        body.extend(["", "Privacy filter: redacted secret-like values from the captured text."])

    frontmatter = [
        "---",
        f'source: "{yaml_escape(url)}"',
        f'title: "{yaml_escape(title)}"',
        f'author: "{yaml_escape(author)}"',
        f'date_published: "{yaml_escape(published)}"',
        f'date_clipped: "{clipped_date}"',
        f'category: "{yaml_escape(category)}"',
        'source_type: "birdclaw-x"',
        'source_role: "early-signal"',
    ]
    if source_id:
        frontmatter.append(f'source_id: "{yaml_escape(source_id)}"')
        frontmatter.append(f'birdclaw_id: "{yaml_escape(source_id)}"')
    for key in sorted(counts):
        frontmatter.append(f"{key}: {counts[key]}")
    frontmatter.append("---")

    return title, url, source_id, redactions, "\n".join(frontmatter + [""] + body) + "\n"


def related_link_lines(item: dict[str, Any]) -> list[str]:
    links: list[str] = []
    def collect(value: Any) -> None:
        if isinstance(value, str):
            for match in re.findall(r"https?://[^\s)>\]]+", value):
                url = canonical_url(match)
                if "x.com/" not in url and "twitter.com/" not in url and url not in links:
                    links.append(url)
        elif isinstance(value, list):
            for entry in value:
                collect(entry)
        elif isinstance(value, dict):
            for key in ("expanded_url", "expandedUrl", "unwound_url", "unwoundUrl", "url", "href"):
                candidate = value.get(key)
                if isinstance(candidate, str) and candidate.startswith("http"):
                    url = canonical_url(candidate)
                    if "x.com/" not in url and "twitter.com/" not in url and url not in links:
                        links.append(url)
            for nested in value.values():
                if isinstance(nested, (dict, list)):
                    collect(nested)

    for value in item.values():
        collect(value)
    return [f"- {url}" for url in links[:8]]


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Convert Birdclaw JSON exports into HoneyDrunk.Lore raw markdown files.")
    parser.add_argument("input", nargs="?", default="-", help="Birdclaw JSON file, or '-' for stdin.")
    parser.add_argument("--raw-dir", default=str(RAW), help="Output raw directory.")
    parser.add_argument("--sources-index", default=str(SOURCES_INDEX), help="Lore sources index for dedupe.")
    parser.add_argument("--category", default="AI / LLM Research & Tooling", help="Lore category for generated raw files.")
    parser.add_argument("--max-items", type=int, default=50, help="Maximum items to convert from this export.")
    parser.add_argument("--dry-run", action="store_true", help="Print summary without writing files.")
    args = parser.parse_args()

    raw_dir = Path(args.raw_dir)
    sources_index = Path(args.sources_index)
    clipped_date = dt.date.today().isoformat()
    urls, ids = known_sources(raw_dir, sources_index)

    items = iter_items(read_json(args.input))
    written: list[str] = []
    skipped: list[str] = []
    failed: list[str] = []
    redactions = 0

    if not args.dry_run:
        raw_dir.mkdir(parents=True, exist_ok=True)

    for item in items[: args.max_items]:
        try:
            title, url, source_id, item_redactions, markdown = item_to_markdown(item, args.category, clipped_date)
            redactions += item_redactions
            if not url:
                skipped.append("missing source URL/id")
                continue
            if url in urls or (source_id and source_id in ids):
                skipped.append(f"duplicate: {url}")
                continue
            filename = f"{clipped_date}-birdclaw-x-{slugify(title)}.md"
            path = raw_dir / filename
            suffix = 2
            while path.exists():
                path = raw_dir / f"{clipped_date}-birdclaw-x-{slugify(title)}-{suffix}.md"
                suffix += 1
            if not args.dry_run:
                path.write_text(markdown, encoding="utf-8")
            written.append(path.name)
            urls.add(url)
            if source_id:
                ids.add(source_id)
        except Exception as exc:
            failed.append(f"{type(exc).__name__}: {exc}")

    print("# Birdclaw Lore X Sourcing Summary")
    print()
    print(f"Mode: {'dry-run' if args.dry_run else 'write'}")
    print(f"Items scanned: {len(items)}")
    print(f"Written: {len(written)}")
    print(f"Skipped duplicates/invalid: {len(skipped)}")
    print(f"Failed: {len(failed)}")
    print(f"Privacy redactions: {redactions}")
    print()
    print("## Files written")
    print("\n".join(f"- raw/{name}" for name in written) if written else "_None_")
    print()
    print("## Skipped")
    print("\n".join(f"- {item}" for item in skipped[:20]) if skipped else "_None_")
    print()
    print("## Failed")
    print("\n".join(f"- {item}" for item in failed) if failed else "_None_")
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
