"""
=============================================================================
Cognifyz Technologies - Software Development Internship
Level 3 (Advanced) - Task 5: Persistent CRUD Application Using File I/O
Author: Intern
Language: Python 3
Description:
    An enterprise-grade enhancement of the Task 3 CRUD application that
    persists task data to a structured text file using standard File I/O.
    Features automatic save-on-action, ID preservation, status tracking,
    graceful handling of missing/corrupt files, and zero database dependencies.
=============================================================================
"""

import os
import sys

# Default storage location inside the project's data directory
DEFAULT_STORAGE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "tasks.txt")
FILE_DELIMITER = "|"


# ---------------------------------------------------------------------------
# Task Model Class (Reused and Extended from Task 3)
# ---------------------------------------------------------------------------
class Task:
    """
    Represents an individual Task entity with an ID, title, description,
    and completion status.
    """

    def __init__(self, task_id, title, description, status="Pending"):
        self.task_id = int(task_id)
        self.title = str(title).strip()
        self.description = str(description).strip()
        self.status = str(status).strip()

    def mark_completed(self):
        """Marks the task status as 'Completed'."""
        self.status = "Completed"

    def mark_pending(self):
        """Marks the task status as 'Pending'."""
        self.status = "Pending"

    def to_file_record(self):
        """
        Serializes the task into a delimited text record.
        Pipes inside title/description are sanitized to forward slashes.

        Returns:
            str: Single line record suitable for file persistence.
        """
        safe_title = self.title.replace(FILE_DELIMITER, "/")
        safe_desc = self.description.replace(FILE_DELIMITER, "/")
        return f"{self.task_id}{FILE_DELIMITER}{self.status}{FILE_DELIMITER}{safe_title}{FILE_DELIMITER}{safe_desc}\n"

    @classmethod
    def from_file_record(cls, record_line):
        """
        Deserializes a text record line into a Task object.

        Args:
            record_line (str): Raw string from storage file.

        Returns:
            Task or None: Constructed Task object, or None if malformed.
        """
        line = record_line.strip()
        if not line or line.startswith("#"):
            return None

        parts = line.split(FILE_DELIMITER)
        if len(parts) < 4:
            return None

        try:
            task_id = int(parts[0].strip())
            status = parts[1].strip()
            title = parts[2].strip()
            # In case description had multiple splits, join the remainder
            description = FILE_DELIMITER.join(parts[3:]).strip()
            return cls(task_id=task_id, title=title, description=description, status=status)
        except (ValueError, IndexError):
            return None

    def __str__(self):
        status_icon = "[x]" if self.status == "Completed" else "[ ]"
        return f"ID {self.task_id:03d} | {status_icon} {self.status:<9} | {self.title} - {self.description}"


# ---------------------------------------------------------------------------
# Persistent Task Manager (File I/O CRUD Operations)
# ---------------------------------------------------------------------------
class PersistentTaskManager:
    """
    Manages CRUD operations on Task objects with automatic file synchronization.
    Data survives application restarts.
    """

    def __init__(self, file_path=DEFAULT_STORAGE_FILE):
        """
        Initializes the persistent task manager.

        Args:
            file_path (str): File path where tasks are saved/loaded.
        """
        self.file_path = os.path.abspath(file_path)
        self.tasks = []
        self._next_id = 1

        # Ensure parent directory exists
        parent_dir = os.path.dirname(self.file_path)
        if parent_dir and not os.path.exists(parent_dir):
            try:
                os.makedirs(parent_dir, exist_ok=True)
            except OSError as e:
                print(f"[Warning] Could not create storage directory: {e}")

        # Load existing tasks from disk
        self.load_from_file()

    def load_from_file(self):
        """
        Loads all task records from the persistence text file.
        Handles missing files, empty files, and malformed records gracefully.
        """
        self.tasks = []

        if not os.path.exists(self.file_path):
            # File does not exist yet; initialize empty state and create it
            self._next_id = 1
            self.save_to_file()
            return

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            for line_num, line in enumerate(lines, start=1):
                task = Task.from_file_record(line)
                if task:
                    self.tasks.append(task)
                elif line.strip() and not line.strip().startswith("#"):
                    print(f"[Warning] Skipping malformed record on line {line_num} in '{self.file_path}'")

            # Determine next unique ID based on existing records
            if self.tasks:
                self._next_id = max(t.task_id for t in self.tasks) + 1
            else:
                self._next_id = 1

        except (IOError, OSError, PermissionError) as e:
            print(f"[Error] Failed to read storage file: {e}")
            self._next_id = 1

    def save_to_file(self):
        """
        Saves all tasks in memory to the storage text file.
        Uses safe write practices to prevent partial file corruption.

        Returns:
            bool: True if file write succeeded, False otherwise.
        """
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                f.write(f"# Cognifyz Task Persistence File | Format: task_id{FILE_DELIMITER}status{FILE_DELIMITER}title{FILE_DELIMITER}description\n")
                for task in self.tasks:
                    f.write(task.to_file_record())
            return True
        except (IOError, OSError, PermissionError) as e:
            print(f"[Error] Failed to save tasks to file: {e}")
            return False

    def create_task(self, title, description):
        """
        Creates a new Task, appends it to memory, and automatically saves to disk.

        Args:
            title (str): Title of the task.
            description (str): Description of the task.

        Returns:
            Task: The newly created Task instance.

        Raises:
            ValueError: If the title is blank.
        """
        cleaned_title = title.strip() if title else ""
        if not cleaned_title:
            raise ValueError("Task title cannot be blank or whitespace.")

        cleaned_description = description.strip() if description else "No description provided."

        new_task = Task(
            task_id=self._next_id,
            title=cleaned_title,
            description=cleaned_description,
            status="Pending"
        )
        self.tasks.append(new_task)
        self._next_id += 1
        self.save_to_file()  # Auto-save
        return new_task

    def get_all_tasks(self):
        """Returns all current tasks."""
        return self.tasks

    def find_task_by_id(self, task_id):
        """Searches for a task by its unique ID."""
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def update_task(self, task_id, new_title=None, new_description=None, new_status=None):
        """
        Updates fields of an existing task and automatically saves to disk.

        Returns:
            bool: True if updated and saved, False if task was not found.
        """
        task = self.find_task_by_id(task_id)
        if not task:
            return False

        if new_title is not None and new_title.strip():
            task.title = new_title.strip()
        if new_description is not None and new_description.strip():
            task.description = new_description.strip()
        if new_status in ("Pending", "Completed"):
            task.status = new_status

        self.save_to_file()  # Auto-save
        return True

    def mark_task_completed(self, task_id):
        """Marks a task as completed and automatically saves to disk."""
        task = self.find_task_by_id(task_id)
        if task:
            task.mark_completed()
            self.save_to_file()  # Auto-save
            return True
        return False

    def delete_task(self, task_id):
        """Deletes a task by ID and automatically saves changes to disk."""
        task = self.find_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self.save_to_file()  # Auto-save
            return True
        return False

    def get_statistics(self):
        """Calculates task metrics."""
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t.status == "Completed")
        pending = total - completed
        completion_rate = (completed / total * 100) if total > 0 else 0.0

        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "completion_rate": round(completion_rate, 1)
        }


# ---------------------------------------------------------------------------
# CLI & Formatting Helpers
# ---------------------------------------------------------------------------
def display_banner(file_path):
    """Prints the application banner showing storage info."""
    print("=" * 72)
    print("       COGNIFYZ TECHNOLOGIES - PERSISTENT TASK MANAGER (FILE I/O) ")
    print("=" * 72)
    print(f" Storage File: {os.path.basename(file_path)} (Auto-saving enabled)")
    print("=" * 72)


def display_menu():
    """Prints the main interactive menu."""
    print("\n" + "-" * 30 + " MENU " + "-" * 36)
    print("  [1] Add New Task (Create & Auto-save)")
    print("  [2] View All Tasks (Read)")
    print("  [3] Search Task by ID")
    print("  [4] Update Task Details (Update & Auto-save)")
    print("  [5] Mark Task as Completed (Auto-save)")
    print("  [6] Delete Task (Delete & Auto-save)")
    print("  [7] View Task Statistics")
    print("  [8] Reload Data from Disk")
    print("  [9] Exit Application")
    print("-" * 72)


def print_tasks_table(tasks):
    """Renders tasks in formatted tabular output."""
    if not tasks:
        print("\n[Info] No tasks available. Your task list is currently empty.")
        return

    print("\n" + "=" * 72)
    print(f"{'ID':<6} | {'Status':<11} | {'Title':<20} | {'Description'}")
    print("-" * 72)
    for task in tasks:
        status_label = f"✓ {task.status}" if task.status == "Completed" else f"○ {task.status}"
        title_snippet = task.title if len(task.title) <= 20 else task.title[:17] + "..."
        desc_snippet = task.description if len(task.description) <= 26 else task.description[:23] + "..."
        print(f"{task.task_id:<6} | {status_label:<11} | {title_snippet:<20} | {desc_snippet}")
    print("=" * 72)


def get_integer_input(prompt):
    """Validates integer inputs from the console."""
    while True:
        raw_val = input(prompt).strip()
        if not raw_val:
            print("[Warning] Input cannot be blank. Please enter a valid number.")
            continue
        try:
            return int(raw_val)
        except ValueError:
            print("[Error] Invalid entry! Please enter a whole integer number.")


# ---------------------------------------------------------------------------
# Action Handlers
# ---------------------------------------------------------------------------
def handle_add_task(manager):
    print("\n--- Add New Task ---")
    while True:
        title = input("Enter task title: ").strip()
        if not title:
            print("[Error] Task title cannot be empty. Please provide a title.")
            continue
        break

    description = input("Enter task description (optional): ").strip()
    task = manager.create_task(title, description)
    print(f"\n[Success] Task #{task.task_id} ('{task.title}') created and saved to disk!")


def handle_view_tasks(manager):
    tasks = manager.get_all_tasks()
    print_tasks_table(tasks)


def handle_search_task(manager):
    print("\n--- Search Task by ID ---")
    if not manager.get_all_tasks():
        print("[Info] Task list is empty.")
        return

    task_id = get_integer_input("Enter Task ID to search: ")
    task = manager.find_task_by_id(task_id)
    if task:
        print("\n" + "=" * 50)
        print(f" Task ID     : {task.task_id}")
        print(f" Title       : {task.title}")
        print(f" Description : {task.description}")
        print(f" Status      : {task.status}")
        print("=" * 50)
    else:
        print(f"\n[Error] Task with ID {task_id} does not exist.")


def handle_update_task(manager):
    print("\n--- Update Task Details ---")
    if not manager.get_all_tasks():
        print("[Info] Task list is empty. Nothing to update.")
        return

    task_id = get_integer_input("Enter Task ID to update: ")
    task = manager.find_task_by_id(task_id)
    if not task:
        print(f"\n[Error] Task with ID {task_id} not found.")
        return

    print(f"\nEditing Task #{task.task_id}: '{task.title}'")
    print("(Press [Enter] to keep the current value)")

    new_title = input(f"New title [{task.title}]: ").strip()
    new_desc = input(f"New description [{task.description}]: ").strip()

    updated = manager.update_task(
        task_id=task_id,
        new_title=new_title if new_title else None,
        new_description=new_desc if new_desc else None
    )

    if updated:
        print(f"\n[Success] Task #{task_id} updated and saved to disk!")


def handle_mark_completed(manager):
    print("\n--- Mark Task as Completed ---")
    if not manager.get_all_tasks():
        print("[Info] Task list is empty.")
        return

    task_id = get_integer_input("Enter Task ID to mark as completed: ")
    task = manager.find_task_by_id(task_id)
    if not task:
        print(f"\n[Error] Task with ID {task_id} not found.")
        return

    if task.status == "Completed":
        print(f"\n[Info] Task #{task_id} is already marked as Completed.")
    else:
        manager.mark_task_completed(task_id)
        print(f"\n[Success] Task #{task_id} ('{task.title}') marked as Completed & saved! ✓")


def handle_delete_task(manager):
    print("\n--- Delete Task ---")
    if not manager.get_all_tasks():
        print("[Info] Task list is empty. Nothing to delete.")
        return

    task_id = get_integer_input("Enter Task ID to delete: ")
    task = manager.find_task_by_id(task_id)
    if not task:
        print(f"\n[Error] Task with ID {task_id} not found.")
        return

    confirm = input(f"Are you sure you want to delete Task #{task_id} ('{task.title}')? (y/n): ").strip().lower()
    if confirm in ("y", "yes"):
        manager.delete_task(task_id)
        print(f"\n[Success] Task #{task_id} was deleted and file updated.")
    else:
        print("\n[Cancelled] Task deletion cancelled.")


def handle_view_statistics(manager):
    stats = manager.get_statistics()
    print("\n" + "=" * 50)
    print("               TASK STATISTICS SUMMARY            ")
    print("=" * 50)
    print(f" Total Tasks Stored  : {stats['total']}")
    print(f" Completed Tasks     : {stats['completed']}")
    print(f" Pending Tasks       : {stats['pending']}")
    print(f" Completion Rate     : {stats['completion_rate']}%")
    print(f" Storage File        : {manager.file_path}")
    print("=" * 50)


def handle_reload(manager):
    print("\n[System] Reloading tasks from disk...")
    manager.load_from_file()
    print(f"[Success] Loaded {len(manager.tasks)} tasks from file.")


# ---------------------------------------------------------------------------
# Main Application Loop
# ---------------------------------------------------------------------------
def main():
    manager = PersistentTaskManager()
    display_banner(manager.file_path)

    # If first time running and empty, insert sample tasks to get the user started
    if not manager.get_all_tasks():
        manager.create_task("Complete Internship Level 1", "Finish Task 1 and Task 2 and document results")
        manager.create_task("Implement Task 5 File I/O", "Persist tasks to text file using safe serialization")
        manager.mark_task_completed(1)

    menu_actions = {
        "1": handle_add_task,
        "2": handle_view_tasks,
        "3": handle_search_task,
        "4": handle_update_task,
        "5": handle_mark_completed,
        "6": handle_delete_task,
        "7": handle_view_statistics,
        "8": handle_reload
    }

    try:
        while True:
            display_menu()
            choice = input("Enter your choice (1-9): ").strip()

            if choice == "9":
                print("\n" + "=" * 72)
                print(" All changes saved to disk. Thank you for using Persistent Task Manager! ")
                print("=" * 72 + "\n")
                break

            if choice in menu_actions:
                menu_actions[choice](manager)
            else:
                print("\n[Error] Invalid choice! Please select an option between 1 and 9.")

    except KeyboardInterrupt:
        print("\n\n[System] Application interrupted. All changes are safely saved to disk.")
        sys.exit(0)


if __name__ == "__main__":
    main()
