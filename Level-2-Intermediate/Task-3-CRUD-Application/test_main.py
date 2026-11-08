"""
=============================================================================
Automated Unit and Integration Test Suite for Task 3: Task CRUD Application
Author: Intern (Cognifyz Technologies)
Language: Python 3
=============================================================================
"""

import unittest
from unittest.mock import patch
import io
import sys
import os

# Ensure local directory is in Python path for test execution from any directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import Task and TaskManager from main.py
from main import (
    Task,
    TaskManager,
    get_integer_input,
    handle_add_task,
    handle_search_task,
    handle_update_task,
    handle_mark_completed,
    handle_delete_task,
    handle_view_statistics
)


class TestTaskModel(unittest.TestCase):
    """Tests the Task data model and string representations."""

    def test_task_initialization(self):
        task = Task(1, "Study Python", "Read chapters on classes", "Pending")
        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.title, "Study Python")
        self.assertEqual(task.description, "Read chapters on classes")
        self.assertEqual(task.status, "Pending")

    def test_task_status_transitions(self):
        task = Task(2, "Submit Code", "Upload to GitHub")
        self.assertEqual(task.status, "Pending")
        task.mark_completed()
        self.assertEqual(task.status, "Completed")
        task.mark_pending()
        self.assertEqual(task.status, "Pending")

    def test_task_str_representation(self):
        task = Task(3, "Test App", "Run unit tests", "Pending")
        task_str = str(task)
        self.assertIn("003", task_str)
        self.assertIn("[ ]", task_str)
        self.assertIn("Test App", task_str)


class TestTaskManagerCRUD(unittest.TestCase):
    """Tests in-memory list-based CRUD operations within TaskManager."""

    def setUp(self):
        """Create a fresh TaskManager instance before each test."""
        self.manager = TaskManager()

    # --- 1. CREATE ---
    def test_create_task_success(self):
        task = self.manager.create_task("Finish Report", "Draft internship documentation")
        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.title, "Finish Report")
        self.assertEqual(task.status, "Pending")
        self.assertEqual(len(self.manager.tasks), 1)

    def test_create_multiple_tasks_auto_increment_id(self):
        t1 = self.manager.create_task("Task 1", "Desc 1")
        t2 = self.manager.create_task("Task 2", "Desc 2")
        t3 = self.manager.create_task("Task 3", "Desc 3")
        self.assertEqual(t1.task_id, 1)
        self.assertEqual(t2.task_id, 2)
        self.assertEqual(t3.task_id, 3)
        self.assertEqual(len(self.manager.tasks), 3)

    def test_create_task_empty_title_raises_error(self):
        with self.assertRaises(ValueError):
            self.manager.create_task("", "No title provided")
        with self.assertRaises(ValueError):
            self.manager.create_task("   ", "Whitespace title")

    # --- 2. READ ---
    def test_read_all_tasks_empty(self):
        self.assertEqual(self.manager.get_all_tasks(), [])

    def test_read_all_tasks_populated(self):
        self.manager.create_task("T1", "D1")
        self.manager.create_task("T2", "D2")
        all_tasks = self.manager.get_all_tasks()
        self.assertEqual(len(all_tasks), 2)

    def test_find_task_by_id_exists(self):
        self.manager.create_task("Find Me", "Important task")
        found = self.manager.find_task_by_id(1)
        self.assertIsNotNone(found)
        self.assertEqual(found.title, "Find Me")

    def test_find_task_by_id_nonexistent(self):
        self.assertIsNone(self.manager.find_task_by_id(999))

    # --- 3. UPDATE ---
    def test_update_task_fields(self):
        self.manager.create_task("Original Title", "Original Desc")
        updated = self.manager.update_task(1, new_title="Updated Title", new_description="Updated Desc")
        self.assertTrue(updated)

        task = self.manager.find_task_by_id(1)
        self.assertEqual(task.title, "Updated Title")
        self.assertEqual(task.description, "Updated Desc")

    def test_update_task_nonexistent_id(self):
        updated = self.manager.update_task(404, new_title="Doesn't exist")
        self.assertFalse(updated)

    # --- 4. MARK COMPLETED ---
    def test_mark_completed(self):
        self.manager.create_task("Pending Task", "Should become completed")
        success = self.manager.mark_task_completed(1)
        self.assertTrue(success)
        task = self.manager.find_task_by_id(1)
        self.assertEqual(task.status, "Completed")

    def test_mark_completed_nonexistent(self):
        self.assertFalse(self.manager.mark_task_completed(888))

    # --- 5. DELETE ---
    def test_delete_task_success(self):
        self.manager.create_task("To Delete", "Remove this")
        self.assertEqual(len(self.manager.tasks), 1)

        deleted = self.manager.delete_task(1)
        self.assertTrue(deleted)
        self.assertEqual(len(self.manager.tasks), 0)
        self.assertIsNone(self.manager.find_task_by_id(1))

    def test_delete_task_nonexistent(self):
        deleted = self.manager.delete_task(555)
        self.assertFalse(deleted)

    # --- 6. STATISTICS ---
    def test_statistics_empty_list(self):
        stats = self.manager.get_statistics()
        self.assertEqual(stats["total"], 0)
        self.assertEqual(stats["completed"], 0)
        self.assertEqual(stats["pending"], 0)
        self.assertEqual(stats["completion_rate"], 0.0)

    def test_statistics_partial_completion(self):
        self.manager.create_task("T1", "D1")
        self.manager.create_task("T2", "D2")
        self.manager.create_task("T3", "D3")
        self.manager.create_task("T4", "D4")
        self.manager.mark_task_completed(1)
        self.manager.mark_task_completed(3)

        stats = self.manager.get_statistics()
        self.assertEqual(stats["total"], 4)
        self.assertEqual(stats["completed"], 2)
        self.assertEqual(stats["pending"], 2)
        self.assertEqual(stats["completion_rate"], 50.0)


class TestConsoleInputAndHandlers(unittest.TestCase):
    """Tests CLI input validation and menu action handlers with mocked input."""

    def setUp(self):
        self.manager = TaskManager()

    @patch('builtins.input', side_effect=['', 'abc', '42'])
    def test_get_integer_input_validation(self, mock_input):
        """Tests that blank lines and non-numeric inputs are discarded until 42 is entered."""
        val = get_integer_input("Enter ID: ")
        self.assertEqual(val, 42)

    @patch('builtins.input', side_effect=['', 'Write Tests', 'Write unit tests for Task 3'])
    def test_handle_add_task_cli(self, mock_input):
        handle_add_task(self.manager)
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].title, "Write Tests")

    @patch('builtins.input', side_effect=['1'])
    def test_handle_search_task_found(self, mock_input):
        self.manager.create_task("Demo Search", "Find me")
        # Should not raise exception
        handle_search_task(self.manager)

    @patch('builtins.input', side_effect=['1', 'New Title', 'New Desc'])
    def test_handle_update_task_cli(self, mock_input):
        self.manager.create_task("Old Title", "Old Desc")
        handle_update_task(self.manager)
        self.assertEqual(self.manager.tasks[0].title, "New Title")

    @patch('builtins.input', side_effect=['1'])
    def test_handle_mark_completed_cli(self, mock_input):
        self.manager.create_task("Action Task", "Desc")
        handle_mark_completed(self.manager)
        self.assertEqual(self.manager.tasks[0].status, "Completed")

    @patch('builtins.input', side_effect=['1', 'y'])
    def test_handle_delete_task_confirmed(self, mock_input):
        self.manager.create_task("Delete Me", "Desc")
        handle_delete_task(self.manager)
        self.assertEqual(len(self.manager.tasks), 0)

    @patch('builtins.input', side_effect=['1', 'n'])
    def test_handle_delete_task_cancelled(self, mock_input):
        self.manager.create_task("Keep Me", "Desc")
        handle_delete_task(self.manager)
        self.assertEqual(len(self.manager.tasks), 1)


if __name__ == '__main__':
    unittest.main()

