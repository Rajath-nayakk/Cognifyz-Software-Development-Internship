"""
=============================================================================
Automated Unit Test Suite for Task 6: Interactive Web Scraper
Author: Intern (Cognifyz Technologies)
Language: Python 3
Description:
    Tests scraping logic, data extraction, and error handling using mocked
    HTTP responses (via unittest.mock.patch) without making live network calls.
=============================================================================
"""

import unittest
from unittest.mock import patch, MagicMock
import os
import sys
import tempfile
import json
import requests

# Ensure local directory is in Python path for test execution from any directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from scraper import WebScraper
from main import export_to_json


# Sample HTML Fixtures for deterministic testing
QUOTES_HTML_FIXTURE = """
<!DOCTYPE html>
<html>
<body>
    <div class="quote">
        <span class="text">"The only way to do great work is to love what you do."</span>
        <span>by <small class="author">Steve Jobs</small></span>
        <div class="tags">
            <a class="tag">inspiration</a>
            <a class="tag">work</a>
        </div>
    </div>
    <div class="quote">
        <span class="text">"Life is what happens when you're busy making other plans."</span>
        <span>by <small class="author">John Lennon</small></span>
        <div class="tags">
            <a class="tag">life</a>
        </div>
    </div>
</body>
</html>
"""

BOOKS_HTML_FIXTURE = """
<!DOCTYPE html>
<html>
<body>
    <article class="product_pod">
        <h3><a href="#" title="A Light in the Attic">A Light in the ...</a></h3>
        <p class="star-rating Three"></p>
        <p class="price_color">£51.77</p>
        <p class="instock availability">In stock</p>
    </article>
    <article class="product_pod">
        <h3><a href="#" title="Tipping the Velvet">Tipping the ...</a></h3>
        <p class="star-rating One"></p>
        <p class="price_color">£53.74</p>
        <p class="instock availability">In stock</p>
    </article>
</body>
</html>
"""

CUSTOM_PAGE_FIXTURE = """
<!DOCTYPE html>
<html>
<head>
    <title>Mocked Test Organization</title>
    <meta name="description" content="This is an educational test page description.">
</head>
<body>
    <h1>Welcome to Testing</h1>
    <h2>Section 1: Architecture</h2>
    <h2>Section 2: Results</h2>
    <a href="/page1">Link 1</a>
    <a href="/page2">Link 2</a>
    <a href="/page3">Link 3</a>
</body>
</html>
"""


class TestWebScraperMocked(unittest.TestCase):
    """Tests the WebScraper engine with mocked HTTP calls."""

    def setUp(self):
        self.scraper = WebScraper(timeout=5)

    @patch('requests.get')
    def test_scrape_quotes_success(self, mock_get):
        """Tests parsing quotes, authors, and tags from HTML."""
        mock_resp = MagicMock()
        mock_resp.text = QUOTES_HTML_FIXTURE
        mock_resp.status_code = 200
        mock_resp.raise_for_status.return_value = None
        mock_get.return_value = mock_resp

        result = self.scraper.scrape_quotes(page=1)
        self.assertTrue(result["success"])
        self.assertEqual(result["count"], 2)

        first_quote = result["data"][0]
        self.assertIn("Steve Jobs", first_quote["author"])
        self.assertIn("inspiration", first_quote["tags"])
        self.assertIn("great work", first_quote["quote"])

    @patch('requests.get')
    def test_scrape_books_success(self, mock_get):
        """Tests extracting book title, price, rating, and stock from HTML."""
        mock_resp = MagicMock()
        mock_resp.text = BOOKS_HTML_FIXTURE
        mock_resp.status_code = 200
        mock_resp.raise_for_status.return_value = None
        mock_get.return_value = mock_resp

        result = self.scraper.scrape_books()
        self.assertTrue(result["success"])
        self.assertEqual(result["count"], 2)

        book1 = result["data"][0]
        self.assertEqual(book1["title"], "A Light in the Attic")
        self.assertEqual(book1["price"], "£51.77")
        self.assertEqual(book1["rating"], "Three Stars")
        self.assertEqual(book1["availability"], "In stock")

    @patch('requests.get')
    def test_scrape_custom_url_metadata(self, mock_get):
        """Tests extracting title, meta description, headers, and links count."""
        mock_resp = MagicMock()
        mock_resp.text = CUSTOM_PAGE_FIXTURE
        mock_resp.status_code = 200
        mock_resp.raise_for_status.return_value = None
        mock_get.return_value = mock_resp

        result = self.scraper.scrape_custom_url("https://example.org/test")
        self.assertTrue(result["success"])
        data = result["data"]
        self.assertEqual(data["title"], "Mocked Test Organization")
        self.assertEqual(data["meta_description"], "This is an educational test page description.")
        self.assertEqual(len(data["h1_headings"]), 1)
        self.assertEqual(len(data["h2_headings"]), 2)
        self.assertEqual(data["total_links_found"], 3)

    def test_invalid_url_format(self):
        """Invalid URLs without scheme should fail immediately with helpful error."""
        res = self.scraper.fetch_html("not-a-valid-url")
        self.assertFalse(res["success"])
        self.assertIn("Invalid URL format", res["error"])

    @patch('requests.get', side_effect=requests.exceptions.Timeout("Request timed out"))
    def test_timeout_handling(self, mock_get):
        """Timeouts should be caught and return a clean failure dict without crashing."""
        res = self.scraper.fetch_html("https://example.com/slow-endpoint")
        self.assertFalse(res["success"])
        self.assertIn("timed out", res["error"])

    @patch('requests.get', side_effect=requests.exceptions.ConnectionError("Name resolution failed"))
    def test_connection_error_handling(self, mock_get):
        """Connection errors should be intercepted gracefully."""
        res = self.scraper.fetch_html("https://nonexistent-domain-xyz.org")
        self.assertFalse(res["success"])
        self.assertIn("Failed to connect", res["error"])

    @patch('requests.get')
    def test_http_404_error_handling(self, mock_get):
        """HTTP 404 should be caught via raise_for_status."""
        mock_resp = MagicMock()
        mock_resp.status_code = 404
        mock_resp.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error: Not Found")
        mock_get.return_value = mock_resp

        res = self.scraper.fetch_html("https://example.com/notfound")
        self.assertFalse(res["success"])
        self.assertIn("HTTP Error 404", res["error"])

    @patch('requests.get')
    def test_missing_html_elements_handled_safely(self, mock_get):
        """Sparse HTML without title, meta, or headings should not raise AttributeError."""
        mock_resp = MagicMock()
        mock_resp.text = "<html><body><p>Bare text only</p></body></html>"
        mock_resp.status_code = 200
        mock_resp.raise_for_status.return_value = None
        mock_get.return_value = mock_resp

        res = self.scraper.scrape_custom_url("https://example.com/sparse")
        self.assertTrue(res["success"])
        self.assertEqual(res["data"]["title"], "No Title Found")
        self.assertEqual(res["data"]["h1_headings"], [])

    def test_export_to_json(self):
        """Tests exporting a scraped result payload to a JSON file."""
        sample_payload = {
            "success": True,
            "url": "https://test.com",
            "data": [{"item": "Alpha"}, {"item": "Beta"}]
        }
        with tempfile.TemporaryDirectory() as tmpdir:
            out = export_to_json(sample_payload, default_filename="test_export.json", output_dir=tmpdir)
            self.assertTrue(os.path.exists(out))
            with open(out, "r", encoding="utf-8") as f:
                loaded = json.load(f)
            self.assertEqual(loaded["data"][0]["item"], "Alpha")


if __name__ == '__main__':
    unittest.main()
