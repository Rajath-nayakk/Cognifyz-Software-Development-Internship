"""
=============================================================================
Cognifyz Technologies - Software Development Internship
Level 2 (Intermediate) - Task 3: Console CRUD Application for Tasks
Author: Intern
Language: Python 3
Description:
    A modular, object-oriented console application implementing in-memory
    CRUD (Create, Read, Update, Delete) operations on a list of Task objects.
    Features unique ID auto-generation, task search, status toggling,
    comprehensive statistics, input validation, and error handling.
=============================================================================
"""

import sys


# ---------------------------------------------------------------------------
# Task Model Class
# ---------------------------------------------------------------------------
class Task:
    """
    Represents an individual Task entity with an ID, title, description,
    and completion status.
    """

    def __init__(self, task_id, title, description, status="Pending"):
        """
        Initializes a new Task instance.

        Args:
            task_id (int): Unique identifier for the task.
            title (str): Brief title or summary of the task.
            description (str): Detailed description of what needs to be done.
            status (str): Current status ('Pending' or 'Completed').
        """
        self.task_id = task_id
        self.title = title.strip()
        self.description = description.strip()
        self.status = status

    def mark_completed(self):
        """Marks the task status as 'Completed'."""
        self.status = "Completed"

    def mark_pending(self):
        """Marks the task status as 'Pending'."""
        self.status = "Pending"

    def __str__(self):
        """String representation of a task."""
        status_icon = "[x]" if self.status == "Completed" else "[ ]"
        return f"ID {self.task_id:03d} | {status_icon} {self.status:<9} | {self.title} - {self.description}"


# ---------------------------------------------------------------------------
# Task Manager Service Class (In-Memory CRUD Operations)
# ---------------------------------------------------------------------------
class TaskManager:
    """
    Manages in-memory CRUD operations over a Python list of Task objects.
    Ensures sequential and unique auto-incrementing task IDs.
    """

    def __init__(self):
        """Initializes an empty task list and sets starting ID counter."""
        self.tasks = []
        self._next_id = 1

    def create_task(self, title, description):
        """
        Creates a new Task and appends it to the in-memory list.

        Args:
            title (str): Title of the task.
            description (str): Description of the task.

        Returns:
            Task: The newly created Task instance.

        Raises:
            ValueError: If the title is empty or blank.
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
        return new_task

    def get_all_tasks(self):
        """
        Returns all tasks currently stored.

        Returns:
            list of Task: Complete list of tasks.
        """
        return self.tasks

    def find_task_by_id(self, task_id):
        """
        Searches for a task by its unique ID.

        Args:
            task_id (int): Unique task identifier.

        Returns:
            Task or None: The matching Task object, or None if not found.
        """
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def update_task(self, task_id, new_title=None, new_description=None, new_status=None):
        """
        Updates fields of an existing task.

        Args:
            task_id (int): Unique task identifier.
            new_title (str, optional): New title to assign.
            new_description (str, optional): New description to assign.
            new_status (str, optional): New status ('Pending' or 'Completed').

        Returns:
            bool: True if task was found and updated, False otherwise.
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

        return True

    def mark_task_completed(self, task_id):
        """
        Marks a specific task as 'Completed'.

        Args:
            task_id (int): Unique task identifier.

        Returns:
            bool: True if task was found and marked, False otherwise.
        """
        task = self.find_task_by_id(task_id)
        if task:
            task.mark_completed()
            return True
        return False

    def delete_task(self, task_id):
        """
        Removes a task from the list by its ID.

        Args:
            task_id (int): Unique task identifier.

        Returns:
            bool: True if task was found and removed, False otherwise.
        """
        task = self.find_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def get_statistics(self):
        """
        Calculates and returns summary statistics of stored tasks.

        Returns:
            dict: Summary statistics dictionary containing counts and rates.
        """
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
# UI & Formatting Helpers
# ---------------------------------------------------------------------------
def display_banner():
    """Prints the application banner."""
    print("=" * 70)
    print("       COGNIFYZ TECHNOLOGIES - TASK TRACKER (CRUD SYSTEM)        ")
    print("=" * 70)
    print("Manage your in-memory tasks efficiently using list-based CRUD operations.")
    print("=" * 70)


def display_menu():
    """Prints the main interactive menu."""
    print("\n" + "-" * 35 + " MENU " + "-" * 29)
    print("  [1] Add New Task (Create)")
    print("  [2] View All Tasks (Read)")
    print("  [3] Search Task by ID")
    print("  [4] Update Task Details (Update)")
    print("  [5] Mark Task as Completed")
    print("  [6] Delete Task (Delete)")
    print("  [7] View Task Statistics")
    print("  [8] Exit Application")
    print("-" * 70)


def print_tasks_table(tasks):
    """
    Renders tasks in a clean tabular view.

    Args:
        tasks (list of Task): Tasks to display.
    """
    if not tasks:
        print("\n[Info] No tasks available. Your task list is currently empty.")
        return

    print("\n" + "=" * 70)
    print(f"{'ID':<6} | {'Status':<11} | {'Title':<20} | {'Description'}")
    print("-" * 70)
    for task in tasks:
        status_label = f"✓ {task.status}" if task.status == "Completed" else f"○ {task.status}"
        title_snippet = task.title if len(task.title) <= 20 else task.title[:17] + "..."
        desc_snippet = task.description if len(task.description) <= 25 else task.description[:22] + "..."
        print(f"{task.task_id:<6} | {status_label:<11} | {title_snippet:<20} | {desc_snippet}")
    print("=" * 70)


def get_integer_input(prompt):
    """
    Safely prompts the user for an integer, retrying on invalid input.

    Args:
        prompt (str): Text prompt to display.

    Returns:
        int: Validated integer.
    """
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
# Menu Action Handlers
# ---------------------------------------------------------------------------
def handle_add_task(manager):
    """Handles creating and adding a new task."""
    print("\n--- Add New Task ---")
    while True:
        title = input("Enter task title: ").strip()
        if not title:
            print("[Error] Task title cannot be empty. Please provide a title.")
            continue
        break

    description = input("Enter task description (optional): ").strip()
    task = manager.create_task(title, description)
    print(f"\n[Success] Task #{task.task_id} ('{task.title}') created successfully!")


def handle_view_tasks(manager):
    """Handles displaying all tasks."""
    tasks = manager.get_all_tasks()
    print_tasks_table(tasks)


def handle_search_task(manager):
    """Handles searching for a task by ID."""
    print("\n--- Search Task by ID ---")
    if not manager.get_all_tasks():
        print("[Info] Task list is empty. Add a task first.")
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
    """Handles updating an existing task's title or description."""
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
        print(f"\n[Success] Task #{task_id} updated successfully!")


def handle_mark_completed(manager):
    """Handles marking a task as Completed."""
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
        print(f"\n[Success] Task #{task_id} ('{task.title}') marked as Completed! ✓")


def handle_delete_task(manager):
    """Handles deleting a task from the list."""
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
        print(f"\n[Success] Task #{task_id} was deleted successfully.")
    else:
        print("\n[Cancelled] Task deletion cancelled.")


def handle_view_statistics(manager):
    """Handles displaying summary statistics."""
    stats = manager.get_statistics()
    print("\n" + "=" * 50)
    print("               TASK STATISTICS SUMMARY            ")
    print("=" * 50)
    print(f" Total Tasks Stored  : {stats['total']}")
    print(f" Completed Tasks     : {stats['completed']}")
    print(f" Pending Tasks       : {stats['pending']}")
    print(f" Completion Rate     : {stats['completion_rate']}%")
    print("=" * 50)


# ---------------------------------------------------------------------------
# Main Controller Loop
# ---------------------------------------------------------------------------
def main():
    """
    Main driver function: initializes TaskManager, displays menu,
    dispatches user selections, and manages application lifecycle.
    """
    display_banner()
    manager = TaskManager()

    # Pre-populate with 2 initial sample tasks for immediate user convenience
    manager.create_task("Complete Internship Level 1", "Finish Task 1 and Task 2 and document results")
    manager.create_task("Review CRUD Operations", "Practice list methods: append, remove, iteration")
    manager.mark_task_completed(1)

    menu_actions = {
        "1": handle_add_task,
        "2": handle_view_tasks,
        "3": handle_search_task,
        "4": handle_update_task,
        "5": handle_mark_completed,
        "6": handle_delete_task,
        "7": handle_view_statistics
    }

    try:
        while True:
            display_menu()
            choice = input("Enter your choice (1-8): ").strip()

            if choice == "8":
                print("\n" + "=" * 70)
                print(" Thank you for using Task Tracker! Best wishes on your internship! ")
                print("=" * 70 + "\n")
                break

            if choice in menu_actions:
                menu_actions[choice](manager)
            else:
                print("\n[Error] Invalid choice! Please select an option between 1 and 8.")

    except KeyboardInterrupt:
        print("\n\n[System] Application interrupted by user. Exiting gracefully...")
        sys.exit(0)


if __name__ == "__main__":
    main()

