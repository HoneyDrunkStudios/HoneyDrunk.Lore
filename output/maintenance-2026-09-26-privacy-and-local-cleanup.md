# Lore privacy remediation and local cleanup

## Credential incident

GitHub secret-scanning alert 1 detected a Telegram bot credential in an imported
security-research article under `raw/2026-08-12-rss-tldr-infosec-the-permanent-threat-analyzing-aeternum-s-blockchain-base.md`.
The surrounding article labels it as third-party malware infrastructure, not a
HoneyDrunk configuration credential. GitHub reported it active; no attempt was
made to authenticate with it or control the associated bot.

The owner explicitly authorized an exception to raw-source immutability to
replace the credential with a redaction marker. Research provenance and the
other indicators remain intact. Shared Git history is not rewritten: old commits
still contain the exposure. Only the credential's owner/provider can revoke it;
redaction is not evidence of revocation or a false-positive finding.

The public RSS, browser, and Birdclaw capture paths now filter complete documents
before writing, including metadata. The common filter retains Birdclaw's existing
patterns and adds Telegram bot credentials, including URL and escaped-colon forms.
Run summaries also use filtered writes. This is best-effort defense in depth,
not a guarantee that all secret formats or encodings are detected. GitHub secret
scanning remains necessary. Manual/agent captures must follow the same privacy
rule before committing.

## Local changes reconciled

- Retain dated signal-review summaries and latest sourcing diagnostics as research
  and operational evidence. Their historical claims are not newly validated by
  this maintenance change.
- Retain feed author extraction and focused low-signal filters. Drop the broad
  "looking for a/an" filter, which would suppress legitimate technical questions.
- Normalize only percent-encoded unreserved URL characters; keep reserved
  delimiters encoded so distinct resources are not accidentally deduplicated.
- Discard the local Obsidian graph search text; it is session-specific UI state.

Offline regression tests use synthetic credentials and cover the capture writers,
redaction behavior, URL identity, feed authors, and filtering. No real credential
is included in the test fixtures or this report.
