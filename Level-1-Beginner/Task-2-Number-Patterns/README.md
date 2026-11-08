# Cognifyz Technologies – Software Development Internship
## Level 1 – Task 2: Number Pattern Generator

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)
![Internship](https://img.shields.io/badge/Internship-Cognifyz%20Technologies-orange.svg)

---

## 📌 Project Overview
The **Number Pattern Generator** is a text-based Python console application developed as part of **Level 1 – Task 2** for the Cognifyz Technologies Software Development Internship.

The tool provides an interactive menu allowing users to generate five distinct geometric number patterns using nested loops. It includes defensive input validation for menu choices and row counts, allows multiple consecutive pattern generations without restarting, and terminates cleanly upon user request.

---

## 🎯 Objectives
- Apply nested loop structures (`for` and `while`) to construct complex geometric arrangements of numbers.
- Implement modular functions with single-responsibility design following PEP 8 conventions.
- Provide input sanitization and boundary checking to prevent crashes and misformatting.
- Enable smooth CLI interaction through a menu loop with seamless re-runs and exit options.
- Establish comprehensive automated testing with 100% test pass rates using Python's standard `unittest` framework.

---

## ✨ Features

### Supported Patterns
1. **Right-Angle Number Triangle**:
   A right-angled triangle where row $i$ contains numbers from $1$ up to $i$.
2. **Inverted Number Triangle**:
   An inverted triangle starting with $N$ numbers on the first row and decreasing down to $1$.
3. **Centered Number Pyramid**:
   A visually centered pyramid using symmetrical leading whitespace padding with numbers separated by spaces.
4. **Floyd's Triangle**:
   A right-angled triangle filled with continuous, sequential natural numbers ($1, 2, 3, \dots, \frac{N(N+1)}{2}$).
5. **Diamond Number Pattern**:
   A symmetrical diamond composed of an upper pyramid of $N$ rows and an inverted lower pyramid of $N - 1$ rows.

### Additional Features
- **Dynamic Row Configuration**: Users can customize the height of each pattern ($1 \le \text{rows} \le 20$).
- **Robust Input Validation**:
  - Traps non-integer entries (strings, symbols, empty inputs) with `try...except ValueError`.
  - Enforces minimum ($1$) and maximum ($20$) boundary limits.
  - Validates menu selections ($1$ to $6$).
- **Continuous Multi-Pattern Workflow**: Generates multiple patterns consecutively without having to relaunch the application.
- **Graceful Termination**: Supports menu exit option and catches `KeyboardInterrupt` (`Ctrl+C`).

---

## 🛠️ Technologies Used
- **Programming Language**: Python 3.8+ (tested on Python 3.14)
- **Standard Libraries**:
  - `sys`: For system exit and stream handling.
  - `unittest`: For automated test suite and regression coverage.
  - `unittest.mock`: For patching inputs in automated testing.
- **Dependencies**: None (100% standard library; zero third-party packages required).

---

## 📁 Project Structure
```text
cognifyz/
├── Task-1-Number-Guessing-Game/
│   ├── game.py
│   ├── test_game.py
│   └── README.md
│
└── Level-1-Beginner/
    └── Task-2-Number-Patterns/
        ├── patterns.py             # Main application source code
        ├── test_patterns.py        # Automated test suite (17 unit & integration tests)
        ├── README.md               # Complete task documentation
        └── screenshots/            # Directory for internship submission evidence
            └── README.md           # Screenshot instructions
```

---

## 🚀 Installation & How to Run

### 1. Prerequisites
Ensure Python 3 is installed:
```bash
python --version
# or on Windows
py --version
```

### 2. Navigate to Task 2 Directory
```bash
cd "Level-1-Beginner/Task-2-Number-Patterns"
```

### 3. Run the Application
```bash
python patterns.py
# or on Windows
py patterns.py
```

### 4. Run Automated Unit Tests
To execute all 17 unit tests verifying pattern structure, edge cases, and validation:
```bash
python -m unittest test_patterns.py -v
# or
py -m unittest test_patterns.py -v
```

---

## 💻 Sample Outputs

### 1. Right-Angle Number Triangle (rows = 4)
```text
---------------------------------------------
  OUTPUT: Right-Angle Number Triangle
---------------------------------------------
1
1 2
1 2 3
1 2 3 4
---------------------------------------------
```

### 2. Inverted Number Triangle (rows = 4)
```text
---------------------------------------------
  OUTPUT: Inverted Number Triangle
---------------------------------------------
1 2 3 4
1 2 3
1 2
1
---------------------------------------------
```

### 3. Centered Number Pyramid (rows = 4)
```text
---------------------------------------------
  OUTPUT: Centered Number Pyramid
---------------------------------------------
   1
  1 2
 1 2 3
1 2 3 4
---------------------------------------------
```

### 4. Floyd's Triangle (rows = 4)
```text
---------------------------------------------
  OUTPUT: Floyd's Triangle
---------------------------------------------
1
2 3
4 5 6
7 8 9 10
---------------------------------------------
```

### 5. Diamond Number Pattern (rows = 3)
```text
---------------------------------------------
  OUTPUT: Diamond Number Pattern
---------------------------------------------
  1
 1 2
1 2 3
 1 2
  1
---------------------------------------------
```

### 6. Input Validation Handling
```text
Enter your choice (1-6): 9
[Error] Invalid selection! Please enter a number between 1 and 6.

Enter your choice (1-6): 1
Enter number of rows (1-20): abc
[Error] Invalid input! Only positive integers are allowed.

Enter number of rows (1-20): 0
[Warning] Rows must be at least 1. Please try again.

Enter number of rows (1-20): 50
[Warning] Maximum supported rows is 20 for optimal display.
```

---

## 🧠 Key Concepts Learned & Demonstrated

### 1. Nested Loop Mechanics
- **Outer Loop**: Controls vertical movement (iterating over row indices $1$ to $N$).
- **Inner Loops**: Control horizontal elements on each line:
  - Loop for generating space indentations (e.g., `rows - row`).
  - Loop for printing or collecting row numerical sequences (e.g., $1$ to `row`).

### 2. Single Responsibility Principle (SRP)
Each pattern generator is written as an independent pure function taking `rows: int` and returning a `list[str]`. This separates algorithmic pattern calculation from console I/O, enabling deterministic testing.

### 3. Defensive Programming
- Using `try...except ValueError` to catch non-numeric text.
- Enforcing valid boundary conditions to prevent formatting anomalies.
- Graceful shutdown handling on `Ctrl+C` via `KeyboardInterrupt`.

---

## 👤 Author
- **Intern**: Rajath Nayak
- **Internship**: Cognifyz Technologies Software Development Internship
- **Track**: Level 1 (Beginner) – Task 2

