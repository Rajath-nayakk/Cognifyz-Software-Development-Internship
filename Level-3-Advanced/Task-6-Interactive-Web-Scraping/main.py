"""
=============================================================================
Cognifyz Technologies - Software Development Internship
Level 3 (Advanced) - Task 6: Interactive Web Scraping (CLI Interface)
Author: Intern
Language: Python 3
Description:
    An interactive console application providing user-friendly web scraping
    capabilities. Extracts quotes, book catalogs, and custom webpage metadata.
    Supports JSON export and handles all network and HTML errors gracefully.
=============================================================================
"""

import json
import os
import sys
from scraper import WebScraper


def display_banner():
    """Prints the application banner."""
    print("=" * 70)
    print("       COGNIFYZ TECHNOLOGIES - INTERACTIVE WEB SCRAPER           ")
    print("=" * 70)
    print("Extract and visualize structured data from web pages safely & politely.")
    print("=" * 70)


def display_menu():
    """Displays the interactive menu."""
    print("\n" + "-" * 26 + " SCRAPER MENU " + "-" * 28)
    print("  [1] Scrape Famous Quotes       (quotes.toscrape.com)")
    print("  [2] Scrape Books Catalog       (books.toscrape.com)")
    print("  [3] Scrape Custom URL Metadata (Any public website)")
    print("  [4] Export Last Results to JSON File")
    print("  [5] Exit Application")
    print("-" * 70)


def display_quotes(quotes_result):
    """Prints quotes in formatted cards."""
    data = quotes_result.get("data", [])
    print("\n" + "=" * 70)
    print(f" SCRAPED {len(data)} QUOTES FROM: {quotes_result.get('url')}")
    print("=" * 70)
    for idx, item in enumerate(data, start=1):
        print(f"\n[{idx}] \"{item['quote']}\"")
        print(f"    — Author : {item['author']}")
        print(f"    — Tags   : {', '.join(item['tags']) if item['tags'] else 'None'}")
    print("\n" + "=" * 70)


def display_books(books_result):
    """Prints books in formatted cards."""
    data = books_result.get("data", [])
    print("\n" + "=" * 70)
    print(f" SCRAPED {len(data)} BOOKS FROM: {books_result.get('url')}")
    print("=" * 70)
    for idx, item in enumerate(data, start=1):
        print(f"[{idx:02d}] {item['title'][:40]:<40} | {item['price']:<8} | {item['rating']:<12} | {item['availability']}")
    print("=" * 70)


def display_custom_page(custom_result):
    """Prints structural metadata extracted from a custom URL."""
    meta = custom_result.get("data", {})
    print("\n" + "=" * 70)
    print(f" METADATA FOR: {custom_result.get('url')}")
    print("=" * 70)
    print(f" Title            : {meta.get('title')}")
    print(f" Meta Description : {meta.get('meta_description')}")
    print(f" Total Links Found: {meta.get('total_links_found')}")

    h1s = meta.get("h1_headings", [])
    print(f"\n Top H1 Headings ({len(h1s)}):")
    if h1s:
        for h in h1s:
            print(f"   • {h}")
    else:
        print("   (None found)")

    h2s = meta.get("h2_headings", [])
    print(f"\n Top H2 Headings ({len(h2s)}):")
    if h2s:
        for h in h2s:
            print(f"   • {h}")
    else:
        print("   (None found)")
    print("=" * 70)


def export_to_json(data_payload, default_filename="scraped_data.json", output_dir=None):
    """
    Exports scraped data payload to a formatted JSON file.

    Args:
        data_payload (dict): Scraped result dictionary.
        default_filename (str): Name of output JSON file.
        output_dir (str, optional): Target directory path.

    Returns:
        str: Path of generated file.
    """
    base_dir = output_dir if output_dir else os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(base_dir, default_filename)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data_payload, f, indent=4, ensure_ascii=False)
    return out_path


def main():
    """Main CLI orchestrator for Task 6."""
    display_banner()
    scraper = WebScraper()
    last_scraped_result = None

    try:
        while True:
            display_menu()
            choice = input("Enter choice (1-5): ").strip()

            if choice == "5":
                print("\n" + "=" * 70)
                print(" Thank you for using Interactive Web Scraper! Happy Coding! ")
                print("=" * 70 + "\n")
                break

            elif choice == "1":
                page_input = input("Enter page number to scrape (default 1): ").strip()
                page = int(page_input) if page_input.isdigit() and int(page_input) > 0 else 1
                print(f"\n[System] Connecting to quotes.toscrape.com (Page {page})...")
                res = scraper.scrape_quotes(page=page)

                if res["success"]:
                    last_scraped_result = res
                    display_quotes(res)
                else:
                    print(f"\n[Error] Scraping Failed: {res['error']}")

            elif choice == "2":
                print("\n[System] Connecting to books.toscrape.com...")
                res = scraper.scrape_books()

                if res["success"]:
                    last_scraped_result = res
                    display_books(res)
                else:
                    print(f"\n[Error] Scraping Failed: {res['error']}")

            elif choice == "3":
                custom_url = input("\nEnter full URL (e.g., https://example.com): ").strip()
                if not custom_url:
                    print("[Warning] URL cannot be blank.")
                    continue

                print(f"\n[System] Fetching metadata from '{custom_url}'...")
                res = scraper.scrape_custom_url(custom_url)

                if res["success"]:
                    last_scraped_result = res
                    display_custom_page(res)
                else:
                    print(f"\n[Error] Scraping Failed: {res['error']}")

            elif choice == "4":
                if not last_scraped_result or not last_scraped_result.get("data"):
                    print("\n[Info] No scraped data available in memory to export. Run a scrape first.")
                    continue

                saved_path = export_to_json(last_scraped_result)
                print(f"\n[Success] Scraped data successfully exported to:")
                print(f" -> {saved_path}")

            else:
                print("\n[Error] Invalid choice! Please select an option between 1 and 5.")

    except KeyboardInterrupt:
        print("\n\n[System] Application interrupted by user. Exiting gracefully...")
        sys.exit(0)


if __name__ == "__main__":
    main()
