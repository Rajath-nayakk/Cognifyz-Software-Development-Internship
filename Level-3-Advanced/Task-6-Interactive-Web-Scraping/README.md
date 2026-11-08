# Cognifyz Technologies – Software Development Internship
## Level 3 (Advanced) – Task 6: Interactive Web Scraping

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)
![Internship](https://img.shields.io/badge/Internship-Cognifyz%20Technologies-orange.svg)

---

## 📌 Project Overview
The **Interactive Web Scraper** is a command-line application developed as part of **Level 3 – Task 6** for the Cognifyz Technologies Software Development Internship.

The tool provides an ethical, polite, and user-friendly interface for extracting structured data from publicly accessible educational sandbox websites (`quotes.toscrape.com`, `books.toscrape.com`) as well as user-specified custom URLs. Built with `requests` and `beautifulsoup4`, it includes request timeouts, polite User-Agent headers, automated HTML sanitization, JSON export capabilities, and defensive error trapping across network and HTTP failure modes.

---

## 🎯 Objectives
- Build an interactive, menu-driven Python web scraper utilizing `requests` and `beautifulsoup4`.
- Extract targeted, structured information:
  - **Famous Quotes**: Text, author names, and categorical tags.
  - **Books Catalog**: Book titles, prices in British Pounds (£), star ratings, and stock availability.
  - **Custom URLs**: Page title, meta descriptions, hierarchical headings (`<h1>`, `<h2>`), and total hyperlink counts.
- Implement ethical scraping practices:
  - Custom User-Agent header identifying the request.
  - Respectful request timeouts (`10s`).
  - No scraping of restricted, authenticated, or anti-bot-protected sites.
- Implement defensive error handling for:
  - Invalid / malformed URLs.
  - Server connection failures.
  - HTTP errors (404 Not Found, 500 Server Error).
  - Missing or sparse HTML elements.
- Develop unit tests utilizing **mocked HTTP responses** so tests execute reliably without live internet dependencies.

---

## ✨ Features
1. **Multi-Target Scraping Modes**:
   - Mode 1: Quotes Scraper (`quotes.toscrape.com`) with pagination support.
   - Mode 2: Book Catalog Scraper (`books.toscrape.com`) with price, rating, and stock parsing.
   - Mode 3: Custom Webpage Metadata Inspector for any standard public URL.
2. **Polite Request Handling**:
   - Sets custom User-Agent identifying the client as `CognifyzInternshipBot/1.0`.
   - Includes 10-second timeout to avoid hanging processes.
3. **Data Export Utility**:
   - Option to export the latest scraped payload into a clean, formatted JSON file (`scraped_data.json`).
4. **Resilient Parser**:
   - Safe parsing using `.find()` and fallback values (`N/A`, `Unknown Title`) preventing `AttributeError` crashes on missing HTML nodes.

---

## 🛠️ Technologies Used
- **Programming Language**: Python 3.8+ (tested on Python 3.14)
- **Libraries**:
  - `requests`: HTTP networking library for fetching remote web pages.
  - `beautifulsoup4`: HTML parsing and DOM tree traversal.
  - `json`: Data serialization for JSON export.
  - `unittest` & `unittest.mock`: Test suite with mock HTTP responses.

---

## 📁 Project Structure
```text
Task-6-Interactive-Web-Scraping/
│
├── scraper.py              # WebScraper service engine (HTTP requests and HTML parsing)
├── main.py                 # Interactive console CLI and JSON exporter
├── test_main.py            # Automated test suite using mocked HTTP calls (9 tests)
├── README.md               # Detailed project documentation
└── screenshots/            # Submission screenshot directory
    └── README.md           # Screenshot capture instructions
```

---

## 🚀 Installation & How to Run

### 1. Prerequisites & Dependencies
Ensure Python 3 is installed and install the required scraping libraries:
```bash
pip install requests beautifulsoup4
```

### 2. Navigate to Project Directory
```bash
cd "Level-3-Advanced/Task-6-Interactive-Web-Scraping"
```

### 3. Run the Application
```bash
py main.py
```

### 4. Run Automated Unit Tests (Offline / Mocked)
```bash
py -m unittest test_main.py -v
```

---

## 💻 Sample Outputs

### 1. Scraping Quotes
```text
-------------------------- SCRAPER MENU ----------------------------
  [1] Scrape Famous Quotes       (quotes.toscrape.com)
  [2] Scrape Books Catalog       (books.toscrape.com)
  [3] Scrape Custom URL Metadata (Any public website)
  [4] Export Last Results to JSON File
  [5] Exit Application
----------------------------------------------------------------------
Enter choice (1-5): 1
Enter page number to scrape (default 1): 1

[System] Connecting to quotes.toscrape.com (Page 1)...

======================================================================
 SCRAPED 10 QUOTES FROM: https://quotes.toscrape.com/page/1/
======================================================================

[1] "“The world as we have created it is a process of our thinking...”"
    — Author : Albert Einstein
    — Tags   : change, deep-thoughts, thinking, world

[2] "“It is our choices, Harry, that show what we truly are...”"
    — Author : J.K. Rowling
    — Tags   : abilities, choices
======================================================================
```

### 2. Scraping Books Catalog
```text
Enter choice (1-5): 2

[System] Connecting to books.toscrape.com...

======================================================================
 SCRAPED 20 BOOKS FROM: https://books.toscrape.com/
======================================================================
[01] A Light in the Attic                     | £51.77   | Three Stars  | In stock
[02] Tipping the Velvet                       | £53.74   | One Stars    | In stock
[03] Soumission                               | £50.10   | One Stars    | In stock
======================================================================
```

### 3. Export to JSON
```text
Enter choice (1-5): 4

[Success] Scraped data successfully exported to:
 -> C:\Users\Rajath Nayak\OneDrive\Desktop\cognifyz\Level-3-Advanced\Task-6-Interactive-Web-Scraping\scraped_data.json
```

---

## 🧠 Key Concepts Learned & Demonstrated
- **DOM Traversal**: Using CSS selectors, `.find()`, and `.find_all()` to extract nested attributes (`href`, `title`, classes).
- **HTTP Lifecycle**: Understanding HTTP headers, status codes (`200`, `404`, `500`), timeouts, and connection errors.
- **Ethical Web Scraping**: Adhering to robots.txt, using polite User-Agent headers, avoiding excessive request rates, and targeting sanctioned sandbox sites.
- **Mock Testing in QA**: Simulating network responses using `unittest.mock.patch('requests.get')` to guarantee 100% deterministic test execution independent of external internet connectivity.

---

## 👤 Author
- **Developer**: Rajath Nayak
- **Internship**: Cognifyz Technologies Software Development Internship
- **Track**: Level 3 (Advanced) – Task 6

