# Cognifyz Technologies – Software Development Internship

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Internship](https://img.shields.io/badge/Cognifyz%20Technologies-Software%20Development%20Internship-orange.svg)
![Build Status](https://img.shields.io/badge/Tests-95%2F95%20Passing-brightgreen.svg)
![Coverage](https://img.shields.io/badge/Coverage-100%25-success.svg)
![License](https://img.shields.io/badge/License-MIT-purple.svg)

This repository contains the complete, production-grade solutions, documentation, and test suites for all **six official tasks** across all **three proficiency levels** of the **Cognifyz Technologies Software Development Internship**.

---

## 📌 Executive Summary

The project is structured according to the official Cognifyz curriculum, emphasizing **Clean Code (PEP 8)**, **Object-Oriented Design (OOP)**, **Defensive Programming**, **File I/O Persistence**, and **Ethical Web Scraping**.

- **All 6 tasks implemented and verified.**
- **95 automated unit and integration tests passing with 100% success rate.**
- **Zero unnecessary external dependencies** (standard library utilized wherever possible; `requests` and `beautifulsoup4` exclusively for Task 6).
- **Independent execution** supported for every application module.

---

## 📂 Repository Structure & Task Matrix

```text
cognifyz/
├── .gitignore                                       # Python, OS, & runtime data exclusion rules
├── requirements.txt                                 # Optional dependencies (requests, bs4 for Task 6)
├── run_all_tests.py                                 # Master test runner (runs all 95 tests)
├── README.md                                        # Master repository documentation
│
├── Task-1-Number-Guessing-Game/                     # LEVEL 1 - TASK 1
│   ├── game.py                                      # Number guessing game CLI
│   ├── test_game.py                                 # 16 unit tests
│   ├── README.md                                    # Task 1 documentation
│   └── screenshots/README.md                        # Screenshot guide
│
├── Level-1-Beginner/
│   └── Task-2-Number-Patterns/                      # LEVEL 1 - TASK 2
│       ├── patterns.py                              # 5 geometric pattern generators
│       ├── test_patterns.py                         # 17 unit tests
│       ├── README.md                                # Task 2 documentation
│       └── screenshots/README.md                    # Screenshot guide
│
├── Level-2-Intermediate/
│   ├── Task-3-CRUD-Application/                     # LEVEL 2 - TASK 3
│   │   ├── main.py                                  # In-memory Task CRUD system
│   │   ├── test_main.py                             # 25 unit tests
│   │   ├── README.md                                # Task 3 documentation
│   │   └── screenshots/README.md                    # Screenshot guide
│   │
│   └── Task-4-Temperature-Converter/                # LEVEL 2 - TASK 4
│       ├── main.py                                  # C, F, K bidirectional converter
│       ├── test_main.py                             # 18 unit tests
│       ├── README.md                                # Task 4 documentation
│       └── screenshots/README.md                    # Screenshot guide
│
└── Level-3-Advanced/
    ├── Task-5-CRUD-File-Persistence/                # LEVEL 3 - TASK 5
    │   ├── main.py                                  # Persistent Task CRUD with File I/O
    │   ├── test_main.py                             # 10 unit tests with tempfile isolation
    │   ├── README.md                                # Task 5 documentation
    │   ├── screenshots/README.md                    # Screenshot guide
    │   └── data/                                    # Persistent text storage
    │       └── .gitkeep                             # Git directory placeholder
    │
    └── Task-6-Interactive-Web-Scraping/             # LEVEL 3 - TASK 6
        ├── scraper.py                               # WebScraper engine (requests + BS4)
        ├── main.py                                  # Interactive CLI & JSON exporter
        ├── test_main.py                             # 9 unit tests with mocked HTTP
        ├── README.md                                # Task 6 documentation
        └── screenshots/README.md                    # Screenshot guide
```

---

## 🎯 Task Breakdown & Highlights

### Level 1: Beginner

#### Task 1: Number Guessing Game
* **Directory**: [`Task-1-Number-Guessing-Game/`](Task-1-Number-Guessing-Game/)
* **Description**: Text-based number guessing game generating random numbers between 1 and 100.
* **Features**: Three difficulty tiers (Easy: 15, Medium: 10, Hard: 5 attempts), directional hints ("Too High" / "Too Low"), performance scoring, replay capability, and session summary metrics.
* **Automated Tests**: 16 tests passing.

#### Task 2: Number Pattern Generator
* **Directory**: [`Level-1-Beginner/Task-2-Number-Patterns/`](Level-1-Beginner/Task-2-Number-Patterns/)
* **Description**: Interactive pattern generator constructing geometric shapes using nested loops.
* **Patterns**: Right-Angle Triangle, Inverted Triangle, Centered Pyramid, Floyd's Triangle, and Symmetrical Diamond.
* **Features**: Dynamic row configurations ($1 \le N \le 20$), input validation, multi-run continuous menu.
* **Automated Tests**: 17 tests passing.

---

### Level 2: Intermediate

#### Task 3: In-Memory Task CRUD Application
* **Directory**: [`Level-2-Intermediate/Task-3-CRUD-Application/`](Level-2-Intermediate/Task-3-CRUD-Application/)
* **Description**: Modular console application managing a list of `Task` objects entirely in memory.
* **Features**: Auto-incrementing unique IDs, Create, Read (table & search by ID), Update (title/description), Delete with confirmation, status toggle (`Pending` / `Completed`), and live completion metrics.
* **Automated Tests**: 25 tests passing.

#### Task 4: Temperature Converter
* **Directory**: [`Level-2-Intermediate/Task-4-Temperature-Converter/`](Level-2-Intermediate/Task-4-Temperature-Converter/)
* **Description**: Precision thermal conversion engine supporting Celsius, Fahrenheit, and Kelvin scales.
* **Formulas**:
  $$F = \left(C \times \frac{9}{5}\right) + 32 \quad | \quad C = (F - 32) \times \frac{5}{9} \quad | \quad K = C + 273.15$$
* **Features**: Physical boundary checks against Absolute Zero ($-273.15^\circ\text{C}$, $-459.67^\circ\text{F}$, $0\text{ K}$), decimal precision formatting, formula disclosure, and negative temperature validation.
* **Automated Tests**: 18 tests passing.

---

### Level 3: Advanced

#### Task 5: Persistent Task Manager Using File I/O
* **Directory**: [`Level-3-Advanced/Task-5-CRUD-File-Persistence/`](Level-3-Advanced/Task-5-CRUD-File-Persistence/)
* **Description**: Direct architectural enhancement of Task 3 that persists tasks to a delimited text file (`data/tasks.txt`) using standard Python File I/O without any external databases.
* **Features**: Auto-saving write-through caching, ID preservation across restarts, resilient deserialization skipping malformed lines, and defensive exception handling (`FileNotFoundError`, `PermissionError`).
* **Automated Tests**: 10 tests passing (isolated via `tempfile`).

#### Task 6: Interactive Web Scraping
* **Directory**: [`Level-3-Advanced/Task-6-Interactive-Web-Scraping/`](Level-3-Advanced/Task-6-Interactive-Web-Scraping/)
* **Description**: Polite, ethical web scraper using `requests` and `beautifulsoup4` for structured extraction.
* **Targets**: Famous Quotes (`quotes.toscrape.com`), Books Catalog (`books.toscrape.com`), and Custom URL structural metadata.
* **Features**: Custom User-Agent identification, 10s request timeouts, missing DOM tag fallbacks, network error recovery, and one-click JSON export.
* **Automated Tests**: 9 tests passing (100% mocked offline requests via `unittest.mock.patch`).

---

## 🚀 Installation & Setup

### Prerequisites
Make sure Python 3.8 or higher is installed:
```bash
python --version
# or on Windows
py --version
```

### Clone the Repository
```bash
git clone https://github.com/Rajath-nayakk/Cognifyz-Software-Development-Internship.git
cd Cognifyz-Software-Development-Internship
```

### Install Dependencies (Required for Task 6 only)
```bash
pip install -r requirements.txt
```
*(Tasks 1 through 5 run strictly on standard Python with zero dependencies!)*

---

## 🧪 Verification & Automated Testing

To run the complete test suite across all six tasks in one command:
```bash
py run_all_tests.py
# or
python run_all_tests.py
```

### Test Results Summary
```text
================================================================================
      COGNIFYZ TECHNOLOGIES INTERNSHIP - COMPLETE TEST SUITE VERIFICATION      
================================================================================

Task Name                                        | Tests  | Passed | Failed | Status
--------------------------------------------------------------------------------
Level 1 - Task 1: Number Guessing Game           | 16     | 16     | 0      | PASSED ✓
Level 1 - Task 2: Number Pattern Generator       | 17     | 17     | 0      | PASSED ✓
Level 2 - Task 3: In-Memory Task CRUD App        | 25     | 25     | 0      | PASSED ✓
Level 2 - Task 4: Temperature Converter          | 18     | 18     | 0      | PASSED ✓
Level 3 - Task 5: Persistent CRUD (File I/O)     | 10     | 10     | 0      | PASSED ✓
Level 3 - Task 6: Interactive Web Scraping       | 9      | 9      | 0      | PASSED ✓
================================================================================
 TOTAL EXECUTED : 95
 TOTAL PASSED   : 95
 TOTAL FAILED   : 0
 SUCCESS RATE   : 100.0%
 EXECUTION TIME : 1.333 seconds
================================================================================
 >>> ALL 6 TASK TEST SUITES HAVE PASSED WITH 100% SUCCESS! <<<
```

---

## 🎮 How to Execute Individual Tasks

```bash
# Level 1 - Task 1: Number Guessing Game
cd "Task-1-Number-Guessing-Game" && py game.py

# Level 1 - Task 2: Number Pattern Generator
cd "Level-1-Beginner/Task-2-Number-Patterns" && py patterns.py

# Level 2 - Task 3: In-Memory Task CRUD Application
cd "Level-2-Intermediate/Task-3-CRUD-Application" && py main.py

# Level 2 - Task 4: Temperature Converter
cd "Level-2-Intermediate/Task-4-Temperature-Converter" && py main.py

# Level 3 - Task 5: Persistent CRUD Application
cd "Level-3-Advanced/Task-5-CRUD-File-Persistence" && py main.py

# Level 3 - Task 6: Interactive Web Scraper
cd "Level-3-Advanced/Task-6-Interactive-Web-Scraping" && py main.py
```

---

## ✅ Internship Completion Checklist

- [x] **Level 1 – Task 1**: Number Guessing Game (Completed & Documented)
- [x] **Level 1 – Task 2**: Number Pattern Generator (Completed & Documented)
- [x] **Level 2 – Task 3**: In-Memory Task CRUD Application (Completed & Documented)
- [x] **Level 2 – Task 4**: Temperature Converter (Completed & Documented)
- [x] **Level 3 – Task 5**: Persistent File I/O CRUD Application (Completed & Documented)
- [x] **Level 3 – Task 6**: Interactive Web Scraper (Completed & Documented)
- [x] **Complete Automated Test Suite**: 95 / 95 unit tests passing
- [x] **Screenshots Guidance**: Dedicated folders & READMEs prepared for every task
- [x] **GitHub Synchronization**: Full codebase committed and synchronized with remote repository

---

## 👤 Author & Acknowledgments

- **Intern**: Rajath Nayak
- **Internship**: Cognifyz Technologies – Software Development Internship
- **GitHub**: [@Rajath-nayakk](https://github.com/Rajath-nayakk)
- **Repository**: [Cognifyz-Software-Development-Internship](https://github.com/Rajath-nayakk/Cognifyz-Software-Development-Internship)
