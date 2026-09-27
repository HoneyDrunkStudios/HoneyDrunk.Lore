"""Best-effort secret redaction for every Lore capture lane.

This is defense in depth, not a complete secret detector. Never validate captured
credentials against their providers. Tests use synthetic values only.
"""
from pathlib import Path
import re

SECRET_PATTERNS = [
    # Match standalone credentials and Bot API URL paths; support escaped colons.
    re.compile(r"(?<![0-9])[0-9]{5,16}(?::|%3[aA]|&#0*58;|&#x0*3[aA];)[A-Za-z0-9_-]{30,}(?![A-Za-z0-9_-])"),
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


def redact_secrets(text: str) -> tuple[str, int]:
    count = 0
    for pattern in SECRET_PATTERNS:
        text, changed = pattern.subn("[redacted-secret-like-value]", text)
        count += changed
    return text, count


def redact_text(text: str) -> str:
    return redact_secrets(text)[0]


def write_redacted_text(path: Path, text: str) -> None:
    """Filter the complete document, including frontmatter and source links."""
    path.write_text(redact_text(text), encoding="utf-8")
