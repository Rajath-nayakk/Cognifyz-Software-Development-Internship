# Cognifyz Technologies – Software Development Internship
## Level 3 (Advanced) – Task 5: Persistent Task Manager Using File I/O

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)
![Internship](https://img.shields.io/badge/Internship-Cognifyz%20Technologies-orange.svg)

---

## 📌 Project Overview
The **Persistent Task Manager** is an enterprise-grade command-line application developed as part of **Level 3 – Task 5** for the Cognifyz Technologies Software Development Internship.

This project directly enhances the in-memory CRUD architecture from **Task 3** by introducing a robust **File I/O persistence layer**. It serializes tasks to a structured, pipe-delimited text file (`data/tasks.txt`) without utilizing any external databases. Changes made during task creation, updating, completion, or deletion are automatically synchronized to disk in real time, ensuring zero data loss across application restarts.

---

## 🎯 Objectives
- Reuse and enhance the Object-Oriented `Task` class and CRUD service concepts from Task 3.
- Implement reliable text file persistence using Python's standard `open()`, `read()`, and `write()` File I/O interfaces.
- Design an automatic write-through caching strategy (auto-saving on every mutating operation).
- Preserve unique task IDs, status states, titles, and descriptions between runtime sessions.
- Handle edge conditions defensively:
  - Missing file or directory $\rightarrow$ creates it cleanly.
  - Empty file $\rightarrow$ initializes safely without crashing.
  - Corrupt or malformed lines $\rightarrow$ logged and skipped without corrupting valid data.
  - File system errors (`PermissionError`, `OSError`) $\rightarrow$ captured and reported gracefully.
- Provide comprehensive automated tests utilizing isolated temporary directories.

---

## ✨ Features
1. **Persistent Data Storage**:
   - Stores records in `data/tasks.txt` in a clean pipe-delimited format:
     `task_id|status|title|description`
2. **Auto-Save Mechanism**:
   - Creation, field updates, status changes, and deletions instantly flush to disk.
3. **ID Continuity & Collision Prevention**:
   - Dynamically inspects existing records on startup and calculates the next unique ID (`max(task_id) + 1`).
4. **Resilient Deserializer**:
   - Ignores comments (`# ...`) and empty lines.
   - Skips malformed rows with fewer than 4 columns or non-integer IDs.
   - Sanitizes pipe characters within text to prevent delimiter collision.
5. **Full CRUD + Statistics**:
   - Create, Read (table & search by ID), Update, Mark Completed, Delete, Statistics, and Manual Reload from disk.

---

## 🛠️ Technologies Used
- **Programming Language**: Python 3.8+ (tested on Python 3.14)
- **Standard Modules**: `os`, `sys`, `tempfile`, `shutil`, `unittest`, `unittest.mock`
- **Database Dependency**: **None** (strict standard library File I/O compliance)

---

## 📁 Project Structure
```text
Task-5-CRUD-File-Persistence/
│
├── main.py                 # Core application with PersistentTaskManager & Task class
├── test_main.py            # Automated test suite with tempfile testing (10 tests)
├── README.md               # Detailed project documentation
├── screenshots/            # Submission screenshot directory
│   └── README.md           # Screenshot guide
└── data/                   # Storage directory for runtime tasks
    ├── .gitkeep            # Directory placeholder for Git
    └── tasks.txt           # Auto-generated pipe-delimited storage file
```

---

## 🚀 Installation & How to Run

### 1. Navigate to Task 5 Directory
```bash
cd "Level-3-Advanced/Task-5-CRUD-File-Persistence"
```

### 2. Run the Application
```bash
py main.py
```

### 3. Run Automated Unit Tests
```bash
py -m unittest test_main.py -v
```

---

## 💻 Sample Outputs

### 1. Application Startup & Auto-Loading
```text
========================================================================
       COGNIFYZ TECHNOLOGIES - PERSISTENT TASK MANAGER (FILE I/O) 
========================================================================
 Storage File: tasks.txt (Auto-saving enabled)
========================================================================

------------------------------ MENU ------------------------------------
  [1] Add New Task (Create & Auto-save)
  [2] View All Tasks (Read)
  [3] Search Task by ID
  [4] Update Task Details (Update & Auto-save)
  [5] Mark Task as Completed (Auto-save)
  [6] Delete Task (Delete & Auto-save)
  [7] View Task Statistics
  [8] Reload Data from Disk
  [9] Exit Application
------------------------------------------------------------------------
```

### 2. Inspection of Raw `data/tasks.txt` File
```text
# Cognifyz Task Persistence File | Format: task_id|status|title|description
1|Completed|Complete Internship Level 1|Finish Task 1 and Task 2 and document results
2|Pending|Implement Task 5 File I/O|Persist tasks to text file using safe serialization
```

### 3. Creating & Auto-Saving a Task
```text
Enter your choice (1-9): 1

--- Add New Task ---
Enter task title: Test Persistence
Enter task description (optional): Verify records survive restart
[Success] Task #3 ('Test Persistence') created and saved to disk!
```

---

## 🧠 Key Concepts Learned & Demonstrated
- **Serialization & Deserialization**: Transforming in-memory Python objects into persistent text formats and parsing them back accurately.
- **Context Management**: Using `with open(...) as f:` to guarantee proper file handle acquisition and closure even during exceptions.
- **Defensive File Handling**: Protecting applications against missing files, bad line structures, and permission errors.
- **State Preservation**: Maintaining sequential, unique identification and application state across separate execution sessions.

---

## 👤 Author
- **Developer**: Rajath Nayak
- **Internship**: Cognifyz Technologies Software Development Internship
- **Track**: Level 3 (Advanced) – Task 5
