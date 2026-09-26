"""Offline regressions: synthetic credentials only; no provider validation."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import lore_privacy as privacy
import lore_source_public as public
import lore_source_browser as browser
import lore_source_birdclaw as bird


def fake_token():
    return '123456789' + ':' + ('A' * 35)


class PrivacyTests(unittest.TestCase):
    def assert_metadata_redacted(self, text, opaque_value):
        self.assertNotIn(opaque_value, text)
        frontmatter = text.split('---', 2)[1]
        decoded = {}
        for line in frontmatter.splitlines():
            key, separator, value = line.partition(':')
            if separator and value.strip().startswith('"'):
                decoded[key] = json.loads(value.strip())
        self.assertTrue(decoded)
        self.assertTrue(any('[redacted-secret-like-value]' in value for value in decoded.values()))
        self.assertNotIn(opaque_value, repr(decoded))

    def test_browser_quoted_secret_metadata(self):
        opaque = 'abcdefghijklmnopqrstuvwx'
        value = 'password: "' + opaque + '"'
        with tempfile.TemporaryDirectory() as directory, patch.object(browser, 'RAW', Path(directory)):
            name = browser.write_raw('https://example.org/source', value, value, 'browser', value, value)
            self.assert_metadata_redacted((Path(directory) / name).read_text(), opaque)

    def test_public_quoted_secret_metadata(self):
        opaque = 'abcdefghijklmnopqrstuvwx'
        value = 'password: "' + opaque + '"'
        feed = f'<rss><channel><item><title>AI agent {value}</title><link>https://example.org/story</link><author>{value}</author><description>AI news</description></item></channel></rss>'
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch.multiple(public, RAW=root / 'raw', OUTPUT=root / 'output',
                                FEEDS=[('Test', 'https://example.org/feed', 'security')],
                                JSON_SOURCES=[], WEB_INDEX_SOURCES=[]), \
                 patch.object(public, 'known_urls', return_value=set()), \
                 patch.object(public, 'fetch', return_value=feed), \
                 patch.object(public, 'article_body', return_value='Research notes ' * 40), \
                 patch('sys.argv', ['lore_source_public.py']), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(public.main(), 0)
            captures = list((root / 'raw').glob('*.md'))
            self.assertEqual(len(captures), 1)
            self.assert_metadata_redacted(captures[0].read_text(), opaque)

    def test_birdclaw_quoted_secret_metadata(self):
        opaque = 'abcdefghijklmnopqrstuvwx'
        value = 'password: "' + opaque + '"'
        item = {'id': '12345', 'text': 'AI news', 'author': 'Researcher',
                'url': 'https://x.com/example/status/12345'}
        _, _, _, _, markdown = bird.item_to_markdown(item, value, '2026-09-26')
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'capture.md'
            privacy.write_redacted_text(path, markdown)
            self.assert_metadata_redacted(path.read_text(), opaque)

    def test_telegram_forms(self):
        token = fake_token()
        for value in [token, 'https://api.telegram.org/bot' + token + '/getMe',
                      token.replace(':', '%3A'), token.replace(':', '&#58;'),
                      token.replace(':', '&#x3a;')]:
            with self.subTest(form=value[:15]):
                cleaned, count = privacy.redact_secrets(value)
                self.assertEqual(count, 1)
                self.assertNotIn('A' * 35, cleaned)

    def test_benign_text_and_idempotence(self):
        text = 'Article 123456789: notes, SHA256 abc123, https://example.org/a%2Fb'
        self.assertEqual(privacy.redact_text(text), text)
        clean = privacy.redact_text(fake_token())
        self.assertEqual(privacy.redact_text(clean), clean)

    def test_existing_patterns_retained(self):
        for token in ['ghp_' + 'a' * 36, 'Bearer ' + 'b' * 30, 'AKIA' + 'A' * 16]:
            self.assertNotEqual(privacy.redact_text(token), token)

    def test_browser_metadata_body_and_filename(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(browser, 'RAW', Path(directory)):
            name = browser.write_raw('https://example.org/' + fake_token(), fake_token(),
                                     'security', 'browser', fake_token(), fake_token())
            self.assertNotIn('A' * 35, name)
            self.assertNotIn('A' * 35, (Path(directory) / name).read_text())

    def test_public_feed_end_to_end_without_network(self):
        token = fake_token()
        feed = f'<rss><channel><item><title>AI agent {token}</title><link>https://example.org/story</link><author>Researcher</author><description>AI news</description></item></channel></rss>'
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch.multiple(public, RAW=root / 'raw', OUTPUT=root / 'output',
                                FEEDS=[('Test', 'https://example.org/feed', 'security')],
                                JSON_SOURCES=[], WEB_INDEX_SOURCES=[]), \
                 patch.object(public, 'known_urls', return_value=set()), \
                 patch.object(public, 'fetch', return_value=feed), \
                 patch.object(public, 'article_body', return_value='Research notes ' * 40 + token), \
                 patch('sys.argv', ['lore_source_public.py']), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(public.main(), 0)
            captures = list((root / 'raw').glob('*.md'))
            self.assertEqual(len(captures), 1)
            self.assertIn('author: "Researcher"', captures[0].read_text())
            for path in root.rglob('*.md'):
                self.assertNotIn('A' * 35, path.name)
                self.assertNotIn('A' * 35, path.read_text())

    def test_birdclaw_complete_document(self):
        item = {'id': '12345', 'text': 'AI news ' + fake_token(),
                'author': fake_token(), 'url': 'https://x.com/example/status/12345'}
        title, _, _, _, markdown = bird.item_to_markdown(item, 'security', '2026-09-26')
        self.assertNotIn('A' * 35, title)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'capture.md'
            privacy.write_redacted_text(path, markdown)
            self.assertNotIn('A' * 35, path.read_text())

    def test_url_identity(self):
        self.assertEqual(public.canonical_url('https://EXAMPLE.org/%7estory/?utm_source=x'), 'https://example.org/~story')
        self.assertEqual(public.canonical_url('https://example.org/a%2fb%3fc%23d'), 'https://example.org/a%2Fb%3Fc%23d')
        self.assertNotEqual(public.canonical_url('https://example.org/a%2Fb'), public.canonical_url('https://example.org/a/b'))

    def test_rss_dc_author(self):
        feed = '<rss xmlns:dc="http://purl.org/dc/elements/1.1/"><channel><item><title>News</title><link>https://example.org</link><dc:creator>Writer</dc:creator></item></channel></rss>'
        self.assertEqual(public.parse_feed(feed, 'Feed', 'news')[0]['author'], 'Writer')

    def test_atom_author(self):
        feed = '<feed xmlns="http://www.w3.org/2005/Atom"><entry><title>News</title><link href="https://example.org"/><author><name>Writer</name></author></entry></feed>'
        self.assertEqual(public.parse_feed(feed, 'Feed', 'news')[0]['author'], 'Writer')

    def test_filter_keeps_technical_questions(self):
        self.assertFalse(public.is_low_signal_item({'title': 'Looking for an agent evaluation framework'}))
        self.assertTrue(public.is_low_signal_item({'title': 'Unpaid/portfolio opportunity'}))


if __name__ == '__main__':
    unittest.main()
