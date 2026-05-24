#!/usr/bin/env python3
"""Public-source producer for HoneyDrunk.Lore.

Fetches a small, high-signal set of public RSS/Atom feeds from sourcing-playbook.md,
filters for HoneyDrunk relevance, dedupes against raw/ + wiki/indexes/sources.md,
and writes qualifying markdown files into raw/.

This is intentionally a producer only. It does not compile raw/ into wiki/.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
import textwrap
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(r"C:\Users\tatte\source\repos\HoneyDrunkStudios\HoneyDrunk.Lore")
RAW = REPO / "raw"
OUTPUT = REPO / "output"
SOURCES_INDEX = REPO / "wiki" / "indexes" / "sources.md"

FEEDS = [
    (".NET Blog", "https://devblogs.microsoft.com/dotnet/feed/", ".NET Ecosystem"),
    ("Azure Blog", "https://devblogs.microsoft.com/azure-sdk/feed/", "Azure & Cloud"),
    ("GitHub Changelog Actions", "https://github.blog/changelog/label/actions/feed/", "DevOps & CI/CD"),
    ("OpenTelemetry Blog", "https://opentelemetry.io/blog/index.xml", "DevOps & CI/CD"),
    ("Docker Blog", "https://www.docker.com/blog/feed/", "DevOps & CI/CD"),
    ("Martin Fowler", "https://martinfowler.com/feed.atom", "Software Architecture"),
    ("High Scalability", "https://highscalability.com/feed/", "Software Architecture"),
    ("Architecture Notes", "https://architecturenotes.co/feed/", "Software Architecture"),
    ("System Design Newsletter", "https://newsletter.systemdesign.one/feed", "Software Architecture"),
    ("The New Stack", "https://thenewstack.io/feed/", "Emerging Technology"),
    ("Thoughtworks Insights", "https://www.thoughtworks.com/rss/insights.xml", "Software Architecture"),
    ("Simon Willison", "https://simonwillison.net/atom/everything/", "AI / LLM Research & Tooling"),
    ("Hugging Face Blog", "https://huggingface.co/blog/feed.xml", "AI / LLM Research & Tooling"),
    ("Google Developers Blog", "https://developers.googleblog.com/feeds/posts/default", "AI / LLM Research & Tooling"),
    ("Google AI Blog", "https://blog.google/technology/ai/rss/", "AI / LLM Research & Tooling"),
    ("Google Gemini Blog", "https://blog.google/products/gemini/rss/", "AI / LLM Research & Tooling"),
    ("TLDR Tech", "https://tldr.tech/api/rss/tech", "Emerging Technology"),
    ("TLDR AI", "https://tldr.tech/api/rss/ai", "AI / LLM Research & Tooling"),
    ("TLDR Web Dev", "https://tldr.tech/api/rss/webdev", "Developer Tooling & AI Coding"),
    ("TLDR DevOps", "https://tldr.tech/api/rss/devops", "DevOps & CI/CD"),
    ("TLDR InfoSec", "https://tldr.tech/api/rss/infosec", "Security & Ethical Hacking"),
    ("AINews / smol.ai", "https://news.smol.ai/rss.xml", "AI / LLM Research & Tooling"),
    ("n8n Blog", "https://blog.n8n.io/rss/", "Workflow Automation"),
    ("Unity Blog", "https://unity.com/blog/rss", "Game Development / Unity"),
    ("Game Developer", "https://www.gamedeveloper.com/rss.xml", "Game Development / Unity"),
    ("80 Level", "https://80.lv/feed", "Game Development / Unity"),
    ("DEV.to Gamedev", "https://dev.to/feed/tag/gamedev", "Game Development / Unity"),
    ("DEV.to Unity", "https://dev.to/feed/tag/unity3d", "Game Development / Unity"),
    ("Blender News", "https://www.blender.org/category/news/feed/", "Technical Art & Creator Tools"),
    ("Blender Releases", "https://www.blender.org/feed/", "Technical Art & Creator Tools"),
    ("RealtimeVFX", "https://realtimevfx.com/latest.rss", "Technical Art & Creator Tools"),
    ("Tech-Artists.org", "https://www.tech-artists.org/latest.rss", "Technical Art & Creator Tools"),
    ("Polycount", "https://polycount.com/discussions/feed.rss", "Technical Art & Creator Tools"),
]

JSON_SOURCES = [
    ("Adobe Developer Blog", "https://blog.developer.adobe.com/en/query-index.json", "Technical Art & Creator Tools"),
]

WEB_INDEX_SOURCES = [
    ("Anthropic News", "https://www.anthropic.com/news", "AI / LLM Research & Tooling", r"/(?:news|engineering)/[a-z0-9-]+"),
    ("The Rundown AI", "https://www.therundown.ai", "AI / LLM Research & Tooling", r"/p/[a-z0-9-]+"),
]

# Podcasts, YouTube, X, and Discord are intentionally excluded from scheduled sourcing.
# Prefer canonical written websites/docs/changelogs/support pages instead.

KEYWORDS = [
    "agent", "agents", "ai", "llm", "model", "prompt", "eval", "mcp", "tool",
    "anthropic", "claude", "openai", "codex", "gemini", "karpathy", "cursor",
    "dotnet", ".net", "asp.net", "c#", "nuget", "azure", "container app", "key vault",
    "github", "github actions", "breach", "source code", "ci/cd", "workflow", "opentelemetry", "observability", "distributed",
    "architecture", "event", "outbox", "saga", "ddd", "api", "contract", "saas",
    "pricing", "solo", "indie", "automation", "webhook", "developer tool",
    "unity", "godot", "unreal", "game dev", "gamedev", "rendering", "simulation",
    "procedural", "blender", "webdev", "frontend", "security", "oauth", "oidc",
    "photoshop", "adobe", "creative cloud", "uxp", "firefly", "illustrator",
    "substance", "premiere", "after effects", "shader", "shaders", "vfx",
    "technical art", "tech art", "art pipeline", "asset", "assets", "material",
    "texture", "textures", "rigging", "animation", "compositing",
]

ADOBE_CREATOR_TERMS = [
    "photoshop", "creative cloud", "uxp", "firefly", "illustrator", "substance",
    "premiere", "after effects", "plugin", "image", "3d", "graphics",
]

HIGH_SIGNAL_TERMS = [
    "codex", "claude code", "karpathy", "anthropic", "openai", "github breach",
    "github breached", "internal repos", "exfiltration", "source code breach",
    "mcp", "agent governance", "supply chain", "rampart",
]

SOURCE_PRIORITY = {
    ".NET Blog": 90,
    "Azure Blog": 88,
    "GitHub Changelog Actions": 86,
    "TLDR AI": 82,
    "TLDR Tech": 80,
    "TLDR Web Dev": 78,
    "TLDR DevOps": 78,
    "TLDR InfoSec": 78,
    "The Rundown AI": 74,
    "AINews / smol.ai": 72,
    "Anthropic News": 68,
    "Google Developers Blog": 55,
    "Google AI Blog": 55,
    "Google Gemini Blog": 55,
    "Unity Blog": 55,
    "Game Developer": 35,
    "80 Level": 30,
    "OpenTelemetry Blog": 50,
    "Simon Willison": 50,
    "Hugging Face Blog": 50,
}

FOCUS_CATEGORIES = [
    "AI / LLM Research & Tooling",
    ".NET Ecosystem",
    "Azure & Cloud",
    "DevOps & CI/CD",
    "Security & Ethical Hacking",
    "Game Development / Unity",
    "Software Architecture",
    "Technical Art & Creator Tools",
]

MIN_PER_FOCUS_CATEGORY = 2

USER_AGENT = "Honeyclaw-Lore-Sourcing/0.1 (+https://honeydrunkstudios.com)"


def source_priority(item: dict) -> int:
    return SOURCE_PRIORITY.get(item.get("feed", ""), 10)


def sort_key(item: dict) -> tuple:
    return (source_priority(item), item.get("score", 0), item.get("published", ""))


def fetch(url: str, timeout: int = 25) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/atom+xml,application/rss+xml,*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read(15_000_000)
        charset = resp.headers.get_content_charset() or "utf-8"
        return raw.decode(charset, errors="replace")


def strip_html(value: str) -> str:
    value = re.sub(r"(?is)<(script|style).*?</\\1>", " ", value)
    value = re.sub(r"(?is)<br\s*/?>", "\n", value)
    value = re.sub(r"(?is)</p\s*>", "\n\n", value)
    value = re.sub(r"(?is)<[^>]+>", " ", value)
    value = html.unescape(value)
    value = re.sub(r"[ \t]+", " ", value)
    value = re.sub(r"\n\s+", "\n", value)
    value = re.sub(r"\n{3,}", "\n\n", value)
    return value.strip()


def parse_feed(xml_text: str, feed_name: str, category: str) -> list[dict]:
    root = ET.fromstring(xml_text)
    items = []
    if root.tag.lower().endswith("rss") or root.find("channel") is not None:
        for item in root.findall(".//item"):
            title = text_of(item, "title")
            link = text_of(item, "link") or text_of(item, "guid")
            summary = text_of(item, "description")
            published = text_of(item, "pubDate")
            items.append({"feed": feed_name, "title": title, "url": link, "summary": strip_html(summary), "published": published, "category": category})
    else:
        ns = {"a": "http://www.w3.org/2005/Atom"}
        for entry in root.findall(".//a:entry", ns) or root.findall(".//entry"):
            title = text_of(entry, "{http://www.w3.org/2005/Atom}title") or text_of(entry, "title")
            link = ""
            for lnk in entry.findall("{http://www.w3.org/2005/Atom}link") + entry.findall("link"):
                if lnk.attrib.get("href") and lnk.attrib.get("rel", "alternate") == "alternate":
                    link = lnk.attrib["href"]
                    break
            summary = (
                text_of(entry, "{http://www.w3.org/2005/Atom}summary")
                or text_of(entry, "{http://www.w3.org/2005/Atom}content")
                or text_of(entry, "{http://search.yahoo.com/mrss/}group/{http://search.yahoo.com/mrss/}description")
                or text_of(entry, "summary")
            )
            published = text_of(entry, "{http://www.w3.org/2005/Atom}published") or text_of(entry, "{http://www.w3.org/2005/Atom}updated")
            items.append({"feed": feed_name, "title": title, "url": link, "summary": strip_html(summary), "published": published, "category": category})
    return [i for i in items if i.get("title") and i.get("url")]


SPONSOR_RE = re.compile(r"\(\s*sponsor\s*\)|\bsponsored\b", re.I)
TLDR_STORY_RE = re.compile(
    r'<a class="font-bold" href="([^"#]+)"[^>]*><h3>(.*?)</h3></a><div class="newsletter-html">(.*?)</div>',
    re.S,
)


def canonical_url(url: str) -> str:
    url = html.unescape(html.unescape(url)).strip()
    parsed = urllib.parse.urlsplit(url)
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    query = [(k, v) for k, v in query if not k.lower().startswith("utm_")]
    return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, urllib.parse.urlencode(query), ""))


def parse_tldr_issue(issue_html: str, feed_name: str, category: str, published: str, issue_url: str) -> list[dict]:
    items: list[dict] = []
    for href, title_html, body_html in TLDR_STORY_RE.findall(issue_html):
        title = strip_html(title_html)
        if SPONSOR_RE.search(title):
            continue
        summary = strip_html(body_html)
        if not title or not summary:
            continue
        items.append({
            "feed": feed_name,
            "title": title,
            "url": canonical_url(href),
            "summary": summary,
            "published": published,
            "category": category,
            "source_type": "rss",
            "discovered_via": issue_url,
            "source_role": "primary-via-tldr",
        })
    return items


def parse_tldr_feed(xml_text: str, feed_name: str, category: str, issue_limit: int = 2, story_limit: int = 8) -> list[dict]:
    issues = parse_feed(xml_text, feed_name, category)[:issue_limit]
    items: list[dict] = []
    for issue in issues:
        try:
            stories = parse_tldr_issue(fetch(issue["url"]), feed_name, category, issue.get("published", "unknown"), issue["url"])
        except Exception:
            issue["source_type"] = "rss"
            items.append(issue)
            continue
        items.extend(stories[:story_limit])
    return items


def text_of(node: ET.Element, name: str) -> str:
    child = node.find(name)
    if child is None or child.text is None:
        return ""
    return child.text.strip()


def parse_json_source(text: str, source_name: str, source_url: str, category: str) -> list[dict]:
    if source_name == "Adobe Developer Blog":
        return parse_adobe_developer_index(text, source_name, source_url, category)
    return []


def parse_web_index(text: str, source_name: str, source_url: str, category: str, href_pattern: str) -> list[dict]:
    urls = []
    for href in re.findall(r"href=[\"']([^\"']+)", text):
        if not re.fullmatch(href_pattern, href):
            continue
        url = urllib.parse.urljoin(source_url, href)
        if url not in urls:
            urls.append(url)

    items = []
    for url in urls[:3]:
        try:
            page = fetch(url)
        except Exception:
            continue
        title = meta_value(page, "og:title") or html_title(page) or url.rsplit("/", 1)[-1].replace("-", " ").title()
        summary = meta_value(page, "description") or meta_value(page, "og:description") or strip_html(page)[:1000]
        published = json_ld_value(page, "datePublished") or json_ld_value(page, "dateModified") or "unknown"
        items.append({"feed": source_name, "title": title, "url": url, "summary": summary, "published": published, "category": category, "source_type": "web"})
    return items


def meta_value(page: str, name: str) -> str:
    pattern = rf"<meta[^>]+(?:name|property)=[\"']{re.escape(name)}[\"'][^>]+content=[\"']([^\"']+)[\"']"
    m = re.search(pattern, page, re.I)
    return html.unescape(m.group(1)).strip() if m else ""


def html_title(page: str) -> str:
    m = re.search(r"(?is)<title[^>]*>(.*?)</title>", page)
    return strip_html(m.group(1)) if m else ""


def json_ld_value(page: str, key: str) -> str:
    m = re.search(rf"[\"']{re.escape(key)}[\"']\s*:\s*[\"']([^\"']+)", page)
    return html.unescape(m.group(1)).strip() if m else ""


def parse_adobe_developer_index(text: str, source_name: str, source_url: str, category: str) -> list[dict]:
    data = json.loads(text)
    rows = data.get("data") or []
    items = []
    for row in rows:
        title = (row.get("title") or "").strip()
        path = (row.get("path") or "").strip()
        description = strip_html(row.get("description") or "")
        tags = row.get("tags") or ""
        hay = f"{title} {description} {tags}".lower()
        if not title or not path or not any(term in hay for term in ADOBE_CREATOR_TERMS):
            continue
        url = urllib.parse.urljoin("https://blog.developer.adobe.com", path)
        items.append({
            "feed": source_name,
            "title": title,
            "url": url,
            "summary": description,
            "published": row.get("date") or "unknown",
            "category": category,
        })
    return items


def score(item: dict) -> int:
    hay = f"{item.get('feed','')} {item.get('title','')} {item.get('summary','')}".lower()
    base = sum(1 for kw in KEYWORDS if kw in hay)
    boost = 3 * sum(1 for term in HIGH_SIGNAL_TERMS if term in hay)
    return base + boost


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text[:70] or "untitled"


def known_urls() -> set[str]:
    urls = set()
    if SOURCES_INDEX.exists():
        urls.update(re.findall(r"https?://[^)\s]+", SOURCES_INDEX.read_text(encoding="utf-8", errors="ignore")))
    for md in RAW.glob("*.md"):
        text = md.read_text(encoding="utf-8", errors="ignore")[:2000]
        m = re.search(r"^source:\s*[\"']?([^\"'\n]+)", text, re.M)
        if m:
            urls.add(m.group(1).strip())
    return urls


def article_body(url: str, fallback: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    if parsed.netloc.lower() in {"x.com", "twitter.com", "www.x.com", "www.twitter.com"}:
        return fallback.strip()
    try:
        page = fetch(url)
    except Exception:
        return fallback.strip()
    # crude readable extraction: prefer article/main, otherwise body text
    m = re.search(r"(?is)<article[^>]*>(.*?)</article>", page) or re.search(r"(?is)<main[^>]*>(.*?)</main>", page)
    body = strip_html(m.group(1) if m else page)
    noisy_markers = ["stylesheet-group", "window.__appglobals__", "cloudflare_turnstile", "html,body{height"]
    if any(marker in body.lower() for marker in noisy_markers):
        return fallback.strip()
    # Drop very short/noisy pages back to feed summary.
    if len(body) < max(500, len(fallback)):
        return fallback.strip()
    return body[:50000]



def yaml_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"').strip()


def select_diverse(items: list[dict], max_items: int) -> list[dict]:
    """Prefer priority sources while guaranteeing breadth across focus categories when possible."""
    selected = []
    selected_urls = set()

    for category in FOCUS_CATEGORIES:
        if len(selected) >= max_items:
            break
        category_items = [item for item in items if item.get("category") == category and item["url"] not in selected_urls]
        category_items.sort(key=sort_key, reverse=True)
        for item in category_items[:MIN_PER_FOCUS_CATEGORY]:
            if len(selected) >= max_items:
                break
            selected.append(item)
            selected_urls.add(item["url"])

    for item in items:
        if len(selected) >= max_items:
            break
        if item["url"] in selected_urls:
            continue
        selected.append(item)
        selected_urls.add(item["url"])

    return selected


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-items", type=int, default=15)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    today = dt.date.today().isoformat()
    known = known_urls()
    candidates = []
    failures = []

    for name, url, category in FEEDS:
        try:
            if name.startswith("TLDR "):
                items = parse_tldr_feed(fetch(url), name, category)
            else:
                items = parse_feed(fetch(url), name, category)[:3]
                for item in items:
                    item["source_type"] = "rss"
            candidates.extend(items)
        except Exception as e:
            failures.append(f"{name}: {type(e).__name__}: {e}")

    for name, url, category in JSON_SOURCES:
        try:
            items = parse_json_source(fetch(url), name, url, category)[:3]
            for item in items:
                item["source_type"] = "rss"
            candidates.extend(items)
        except Exception as e:
            failures.append(f"{name}: {type(e).__name__}: {e}")

    for name, url, category, href_pattern in WEB_INDEX_SOURCES:
        try:
            candidates.extend(parse_web_index(fetch(url), name, url, category, href_pattern)[:3])
        except Exception as e:
            failures.append(f"{name}: {type(e).__name__}: {e}")


    seen = set()
    fresh = []
    skipped_dupes = 0
    for item in candidates:
        url = item["url"].strip()
        if url in known or url in seen:
            skipped_dupes += 1
            continue
        seen.add(url)
        item["score"] = score(item)
        if item["score"] >= 1:
            fresh.append(item)

    fresh.sort(key=sort_key, reverse=True)
    selected = select_diverse(fresh, args.max_items)

    written = []
    if not args.dry_run:
        RAW.mkdir(parents=True, exist_ok=True)
        OUTPUT.mkdir(parents=True, exist_ok=True)
        for item in selected:
            source_type = item.get("source_type", "rss")
            body = article_body(item["url"], item.get("summary", ""))
            min_len = 300
            if len(body) < min_len:
                failures.append(f"{item['feed']}: skipped short content: {item['url']}")
                continue
            fname = f"{today}-{source_type}-{slugify(item['feed'] + '-' + item['title'])}.md"
            path = RAW / fname
            n = 2
            while path.exists():
                path = RAW / f"{today}-{source_type}-{slugify(item['feed'] + '-' + item['title'])}-{n}.md"
                n += 1
            published = item.get("published") or "unknown"
            extra_meta = ""
            if item.get("discovered_via"):
                extra_meta += f'discovered_via: "{yaml_escape(item["discovered_via"])}"\n'
            if item.get("source_role"):
                extra_meta += f'source_role: "{yaml_escape(item["source_role"])}"\n'
            content = f'''---\nsource: "{yaml_escape(item['url'])}"\ntitle: "{yaml_escape(item['title'])}"\nauthor: "{yaml_escape(item['feed'])}"\ndate_published: "{yaml_escape(published)}"\ndate_clipped: "{today}"\ncategory: "{yaml_escape(item['category'])}"\nsource_type: "{source_type}"\n{extra_meta}---\n\n# {item['title']}\n\nSource: {item['url']}\n\n{body}\n'''
            path.write_text(content, encoding="utf-8")
            written.append(path.name)

    summary = [
        "# OpenClaw Lore Sourcing — Last Run",
        "",
        f"Timestamp: {dt.datetime.now().isoformat(timespec='seconds')}",
        f"Mode: {'dry-run' if args.dry_run else 'write'}",
        f"Candidates scanned: {len(candidates)}",
        f"Skipped duplicates: {skipped_dupes}",
        f"Selected: {len(selected)}",
        f"Saved: {len(written)}",
        "",
        "## Selected candidates",
    ]
    summary.extend((f"- [{item.get('category')}] {item.get('feed')}: {item.get('title')}" for item in selected) if selected else ["_None_"])
    summary.extend(["", "## Files written"])
    summary.extend((f"- raw/{name}" for name in written) if written else ["_None_"])
    summary.extend(["", "## Failures / skips"])
    summary.extend((f"- {failure}" for failure in failures) if failures else ["_None_"])
    if not args.dry_run:
        (OUTPUT / "openclaw-sourcing-last-run.md").write_text("\n".join(summary) + "\n", encoding="utf-8")
    else:
        print("\n".join(summary))

    print(f"Sourced {len(written)} items; skipped {skipped_dupes} duplicates; failures {len(failures)}")
    for name in written:
        print(f"raw/{name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
