# Cognifyz Technologies – Software Development Internship
## Level 2 (Intermediate) – Task 3: Task CRUD Console Application

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)
![Internship](https://img.shields.io/badge/Internship-Cognifyz%20Technologies-orange.svg)

---

## 📌 Project Overview
The **Task CRUD Application** is an interactive, menu-driven Python console system developed as part of **Level 2 – Task 3** for the Cognifyz Technologies Software Development Internship.

The application allows users to perform full in-memory **CRUD** (Create, Read, Update, Delete) operations on tasks represented by an object-oriented `Task` model. It features auto-incrementing unique IDs, status tracking (`Pending` / `Completed`), search capabilities, deletion safeguards, aggregate statistics, and defensive input validation.

---

## 🎯 Objectives
- Implement an Object-Oriented `Task` class containing `task_id`, `title`, `description`, and `status`.
- Store and manage task instances dynamically inside an in-memory Python `list`.
- Implement full CRUD operations:
  - **Create**: Add new tasks with unique IDs.
  - **Read**: View all tasks in a formatted table or search an individual task by ID.
  - **Update**: Modify titles and descriptions with optional field retention.
  - **Delete**: Safely remove tasks by ID with confirmation prompt.
- Provide task completion toggling (`mark_completed`) and metric calculations (`completion_rate`).
- Build an interactive, resilient console interface validating menu choices, IDs, and non-empty titles.

---

## ✨ Features
1. **Object-Oriented Design**:
   - `Task` model encapsulating state and string formatting.
   - `TaskManager` service encapsulating all list manipulation logic.
2. **Auto-Incrementing Unique IDs**: Sequential ID generation ($1, 2, 3, \dots$) prevents collision and manual tracking errors.
3. **Formatted Tabular Display**: Clean ASCII tables with status icons (`✓ Completed`, `○ Pending`) and text truncation for long strings.
4. **Flexible Updates**: Users can press `[Enter]` to retain existing values when modifying a task.
5. **Real-Time Task Analytics**:
   - Total tasks count
   - Completed tasks count
   - Pending tasks count
   - Dynamic completion rate percentage
6. **Defensive Validation & Exception Handling**:
   - Rejects blank/whitespace-only titles.
   - Traps non-numeric inputs using `try...except ValueError`.
   - Handles nonexistent task IDs gracefully with user-friendly notices.
   - Graceful exit on `Ctrl+C` (`KeyboardInterrupt`).

---

## 🛠️ Technologies Used
- **Programming Language**: Python 3.8+ (tested on Python 3.14)
- **Standard Modules**:
  - `sys`: For system-level utilities and exit calls.
  - `unittest`: For automated unit and integration tests.
  - `unittest.mock`: For patching CLI input streams during test runs.
- **Persistence**: Pure in-memory Python `list` (per Task 3 requirements; file/DB persistence reserved for later tasks).

---

## 📁 Project Structure
```text
cognifyz/
├── Task-1-Number-Guessing-Game/
├── Level-1-Beginner/
│   └── Task-2-Number-Patterns/
│
└── Level-2-Intermediate/
    └── Task-3-CRUD-Application/
        ├── main.py                 # Core application with Task and TaskManager classes
        ├── test_main.py            # Comprehensive unit test suite (25 tests)
        ├── README.md               # Complete project documentation
        └── screenshots/            # Submission screenshot directory
            └── README.md           # Guide on required screenshots
```

---

## 🚀 Installation & How to Run

### 1. Prerequisites
Verify Python 3 is installed:
```bash
python --version
# or on Windows
py --version
```

### 2. Navigate to Project Directory
```bash
cd "Level-2-Intermediate/Task-3-CRUD-Application"
```

### 3. Run the Application
```bash
python main.py
# or on Windows
py main.py
```

### 4. Run Automated Test Suite
To run all 25 unit and integration tests:
```bash
python -m unittest test_main.py -v
# or
py -m unittest test_main.py -v
```

---

## 💻 Sample Output

### Main Menu & Reading Tasks
```text
======================================================================
       COGNIFYZ TECHNOLOGIES - TASK TRACKER (CRUD SYSTEM)        
======================================================================
Manage your in-memory tasks efficiently using list-based CRUD operations.
======================================================================

----------------------------------- MENU -----------------------------
  [1] Add New Task (Create)
  [2] View All Tasks (Read)
  [3] Search Task by ID
  [4] Update Task Details (Update)
  [5] Mark Task as Completed
  [6] Delete Task (Delete)
  [7] View Task Statistics
  [8] Exit Application
----------------------------------------------------------------------
Enter your choice (1-8): 2

======================================================================
ID     | Status      | Title                | Description
----------------------------------------------------------------------
1      | ✓ Completed | Complete Internsh... | Finish Task 1 and Task...
2      | ○ Pending   | Review CRUD Opera... | Practice list methods:...
======================================================================
```

### Searching & Marking Completed
```text
Enter your choice (1-8): 3

--- Search Task by ID ---
Enter Task ID to search: 2

==================================================
 Task ID     : 2
 Title       : Review CRUD Operations
 Description : Practice list methods: append, remove, iteration
 Status      : Pending
==================================================

Enter your choice (1-8): 5

--- Mark Task as Completed ---
Enter Task ID to mark as completed: 2

[Success] Task #2 ('Review CRUD Operations') marked as Completed! ✓
```

### Statistics Summary
```text
Enter your choice (1-8): 7

==================================================
               TASK STATISTICS SUMMARY            
==================================================
 Total Tasks Stored  : 2
 Completed Tasks     : 2
 Pending Tasks       : 0
 Completion Rate     : 100.0%
==================================================
```

---

## 🧠 Key Concepts Learned & Demonstrated

### 1. Object-Oriented Programming (OOP)
- **Encapsulation**: State (`task_id`, `title`, `description`, `status`) and behaviors (`mark_completed`, `__str__`) are cleanly encapsulated inside the `Task` class.
- **Separation of Concerns**: The `TaskManager` class acts as the data service layer, completely decoupled from console print/input logic.

### 2. List Operations in Python
- Appending new items: `self.tasks.append(new_task)`
- Iterating & searching: `for task in self.tasks: if task.task_id == task_id: ...`
- Deleting items: `self.tasks.remove(task)`
- Comprehensions for metrics: `sum(1 for t in self.tasks if t.status == 'Completed')`

### 3. Defensive Programming
- Intercepting `ValueError` on integer inputs.
- Guarding against invalid IDs with clear feedback.
- Confirming destructive actions (deletion) before executing.

---

## 👤 Author
- **Developer**: Rajath Nayak
- **Internship**: Cognifyz Technologies Software Development Internship
- **Track**: Level 2 (Intermediate) – Task 3

