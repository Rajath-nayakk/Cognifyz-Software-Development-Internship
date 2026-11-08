"""
=============================================================================
Cognifyz Technologies - Software Development Internship
Level 3 (Advanced) - Task 6: Interactive Web Scraping (Scraper Engine)
Author: Intern
Language: Python 3
Description:
    Core web scraping engine using requests and BeautifulSoup4.
    Includes polite User-Agent headers, timeouts, robust HTTP error handling,
    and safe HTML parsing for missing or irregular tags.
=============================================================================
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Default polite configuration
DEFAULT_TIMEOUT = 10  # seconds
USER_AGENT = "Mozilla/5.0 (compatible; CognifyzInternshipBot/1.0; +https://cognifyz.com)"
HEADERS = {"User-Agent": USER_AGENT}


class WebScraper:
    """
    Handles HTTP fetching, HTML parsing, error trapping, and data extraction
    from public sandbox sites and generic URLs.
    """

    def __init__(self, timeout=DEFAULT_TIMEOUT):
        self.timeout = timeout
        self.headers = HEADERS

    def fetch_html(self, url):
        """
        Safely performs an HTTP GET request to fetch webpage content.

        Args:
            url (str): Target webpage URL.

        Returns:
            dict: {"success": bool, "html": str, "status_code": int, "error": str}
        """
        # Validate URL schema
        parsed = urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            return {
                "success": False,
                "html": "",
                "status_code": 0,
                "error": f"Invalid URL format: '{url}'. Please include 'http://' or 'https://'."
            }

        try:
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            return {
                "success": True,
                "html": response.text,
                "status_code": response.status_code,
                "error": ""
            }
        except requests.exceptions.Timeout:
            return {
                "success": False,
                "html": "",
                "status_code": 0,
                "error": f"Request timed out after {self.timeout} seconds while accessing {url}."
            }
        except requests.exceptions.ConnectionError:
            return {
                "success": False,
                "html": "",
                "status_code": 0,
                "error": f"Failed to connect to server. Check your network or verify domain: {url}."
            }
        except requests.exceptions.HTTPError as e:
            code = response.status_code if 'response' in locals() else 0
            return {
                "success": False,
                "html": "",
                "status_code": code,
                "error": f"HTTP Error {code}: {e}"
            }
        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "html": "",
                "status_code": 0,
                "error": f"An unexpected request error occurred: {e}"
            }

    def scrape_quotes(self, page=1):
        """
        Scrapes quotes, authors, and associated tags from quotes.toscrape.com.

        Args:
            page (int): Target page number.

        Returns:
            dict: Response payload containing parsed list of quotes.
        """
        url = f"https://quotes.toscrape.com/page/{page}/"
        fetch_result = self.fetch_html(url)
        if not fetch_result["success"]:
            return fetch_result

        soup = BeautifulSoup(fetch_result["html"], "html.parser")
        quote_elements = soup.find_all("div", class_="quote")
        quotes_data = []

        for elem in quote_elements:
            text_elem = elem.find("span", class_="text")
            author_elem = elem.find("small", class_="author")
            tag_elems = elem.find_all("a", class_="tag")

            text = text_elem.get_text(strip=True) if text_elem else "N/A"
            author = author_elem.get_text(strip=True) if author_elem else "Unknown"
            tags = [t.get_text(strip=True) for t in tag_elems]

            quotes_data.append({
                "quote": text,
                "author": author,
                "tags": tags
            })

        return {
            "success": True,
            "url": url,
            "count": len(quotes_data),
            "data": quotes_data,
            "error": ""
        }

    def scrape_books(self):
        """
        Scrapes top books from books.toscrape.com (sandbox catalog).

        Returns:
            dict: Response payload containing book titles, prices, ratings, and availability.
        """
        url = "https://books.toscrape.com/"
        fetch_result = self.fetch_html(url)
        if not fetch_result["success"]:
            return fetch_result

        soup = BeautifulSoup(fetch_result["html"], "html.parser")
        product_pods = soup.find_all("article", class_="product_pod")
        books_data = []

        for pod in product_pods:
            # Title
            h3 = pod.find("h3")
            title_tag = h3.find("a") if h3 else None
            title = title_tag.get("title", title_tag.get_text(strip=True)) if title_tag else "Unknown Title"

            # Price
            price_elem = pod.find("p", class_="price_color")
            price = price_elem.get_text(strip=True) if price_elem else "N/A"

            # Availability
            avail_elem = pod.find("p", class_="instock availability")
            availability = avail_elem.get_text(strip=True) if avail_elem else "N/A"

            # Star Rating (class star-rating One/Two/Three/Four/Five)
            rating_elem = pod.find("p", class_="star-rating")
            rating_classes = rating_elem.get("class", []) if rating_elem else []
            rating = [c for c in rating_classes if c != "star-rating"]
            rating_str = rating[0] if rating else "Unrated"

            books_data.append({
                "title": title,
                "price": price,
                "availability": availability,
                "rating": f"{rating_str} Stars"
            })

        return {
            "success": True,
            "url": url,
            "count": len(books_data),
            "data": books_data,
            "error": ""
        }

    def scrape_custom_url(self, url):
        """
        Scrapes general structural metadata from any user-provided URL:
        Title, Meta Description, H1/H2 Headings, and Hyperlink summary.

        Args:
            url (str): Target webpage URL.

        Returns:
            dict: Extracted structural page summary.
        """
        fetch_result = self.fetch_html(url)
        if not fetch_result["success"]:
            return fetch_result

        soup = BeautifulSoup(fetch_result["html"], "html.parser")

        # 1. Page Title
        title_tag = soup.find("title")
        page_title = title_tag.get_text(strip=True) if title_tag else "No Title Found"

        # 2. Meta Description
        meta_desc = "No meta description found."
        meta_tag = soup.find("meta", attrs={"name": "description"}) or soup.find("meta", attrs={"property": "og:description"})
        if meta_tag and meta_tag.get("content"):
            meta_desc = meta_tag.get("content").strip()

        # 3. Headings (H1 and H2)
        h1_tags = [h.get_text(strip=True) for h in soup.find_all("h1") if h.get_text(strip=True)]
        h2_tags = [h.get_text(strip=True) for h in soup.find_all("h2") if h.get_text(strip=True)]

        # 4. Links count
        links = soup.find_all("a", href=True)

        return {
            "success": True,
            "url": url,
            "data": {
                "title": page_title,
                "meta_description": meta_desc,
                "h1_headings": h1_tags[:5],
                "h2_headings": h2_tags[:5],
                "total_links_found": len(links)
            },
            "error": ""
        }

