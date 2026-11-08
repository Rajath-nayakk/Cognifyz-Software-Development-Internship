"""
=============================================================================
Automated Unit and Integration Test Suite for Task 5: Persistent Task Manager
Author: Intern (Cognifyz Technologies)
Language: Python 3
=============================================================================
"""

import unittest
from unittest.mock import patch
import os
import sys
import tempfile
import shutil

# Ensure local directory is in Python path for test execution from any directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import Task, PersistentTaskManager, FILE_DELIMITER


class TestTaskSerialization(unittest.TestCase):
    """Tests serialization and deserialization of Task entities."""

    def test_to_file_record_and_from_record(self):
        original = Task(1, "Test Title", "Test Description", "Pending")
        record_str = original.to_file_record()
        self.assertTrue(record_str.endswith("\n"))

        restored = Task.from_file_record(record_str)
        self.assertIsNotNone(restored)
        self.assertEqual(restored.task_id, 1)
        self.assertEqual(restored.title, "Test Title")
        self.assertEqual(restored.description, "Test Description")
        self.assertEqual(restored.status, "Pending")

    def test_pipe_sanitization(self):
        """Pipes in title or description should be sanitized to avoid delimiter collision."""
        task = Task(2, "Title|With|Pipe", "Desc|With|Pipe", "Completed")
        record = task.to_file_record()
        # Verify pipe delimiter count is exactly 3 (4 fields)
        parts = record.strip().split(FILE_DELIMITER)
        self.assertEqual(len(parts), 4)
        self.assertIn("Title/With/Pipe", parts[2])

    def test_from_file_record_malformed(self):
        """Malformed, comment, or blank lines should return None without error."""
        self.assertIsNone(Task.from_file_record(""))
        self.assertIsNone(Task.from_file_record("   "))
        self.assertIsNone(Task.from_file_record("# Comment line"))
        self.assertIsNone(Task.from_file_record("invalid|format"))
        self.assertIsNone(Task.from_file_record("abc|Pending|Title|Desc"))  # Non-integer ID


class TestFilePersistenceCRUD(unittest.TestCase):
    """Tests PersistentTaskManager CRUD operations and file synchronization."""

    def setUp(self):
        """Creates an isolated temporary directory for test storage files."""
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, "test_tasks.txt")
        self.manager = PersistentTaskManager(file_path=self.test_file)

    def tearDown(self):
        """Cleans up the temporary directory after tests."""
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_missing_file_creation(self):
        """Initializing with a nonexistent file path should create it automatically."""
        self.assertTrue(os.path.exists(self.test_file))
        self.assertEqual(self.manager.get_all_tasks(), [])

    def test_create_and_auto_save(self):
        """Creating a task should immediately write it to the disk file."""
        t1 = self.manager.create_task("Task 1", "Desc 1")
        self.assertEqual(t1.task_id, 1)

        # Inspect raw file content
        with open(self.test_file, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("Task 1", content)
        self.assertIn("Desc 1", content)

    def test_persistence_across_restarts(self):
        """Tasks created in one session must reload identically in a new manager instance."""
        self.manager.create_task("Session 1 Task", "Should persist")
        self.manager.create_task("Second Task", "Also persist")
        self.manager.mark_task_completed(1)

        # Simulate restarting the application by creating a brand-new manager instance
        new_manager = PersistentTaskManager(file_path=self.test_file)
        tasks = new_manager.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].task_id, 1)
        self.assertEqual(tasks[0].title, "Session 1 Task")
        self.assertEqual(tasks[0].status, "Completed")
        self.assertEqual(tasks[1].task_id, 2)
        self.assertEqual(tasks[1].title, "Second Task")
        self.assertEqual(tasks[1].status, "Pending")

        # Next created task should continue auto-incrementing ID properly
        t3 = new_manager.create_task("Third Task", "Desc 3")
        self.assertEqual(t3.task_id, 3)

    def test_update_and_auto_save(self):
        self.manager.create_task("Original Title", "Original Desc")
        self.manager.update_task(1, new_title="Updated Title", new_description="Updated Desc")

        # Verify reload from disk
        fresh_mgr = PersistentTaskManager(file_path=self.test_file)
        task = fresh_mgr.find_task_by_id(1)
        self.assertEqual(task.title, "Updated Title")
        self.assertEqual(task.description, "Updated Desc")

    def test_delete_and_auto_save(self):
        self.manager.create_task("Task to delete", "Will be removed")
        self.assertEqual(len(self.manager.get_all_tasks()), 1)

        self.manager.delete_task(1)
        self.assertEqual(len(self.manager.get_all_tasks()), 0)

        # Verify raw file shows no task records
        fresh_mgr = PersistentTaskManager(file_path=self.test_file)
        self.assertEqual(len(fresh_mgr.get_all_tasks()), 0)

    def test_malformed_records_skipped_gracefully(self):
        """Corrupt lines in file should be skipped while valid lines are loaded."""
        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write("# Header\n")
            f.write("1|Pending|Good Task 1|Desc 1\n")
            f.write("BROKEN_RECORD_WITHOUT_PIPES\n")
            f.write("bad_id|Pending|Broken ID|Desc\n")
            f.write("2|Completed|Good Task 2|Desc 2\n")

        fresh_mgr = PersistentTaskManager(file_path=self.test_file)
        tasks = fresh_mgr.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].task_id, 1)
        self.assertEqual(tasks[1].task_id, 2)

    def test_statistics_calculation(self):
        self.manager.create_task("T1", "D1")
        self.manager.create_task("T2", "D2")
        self.manager.mark_task_completed(1)
        stats = self.manager.get_statistics()
        self.assertEqual(stats["total"], 2)
        self.assertEqual(stats["completed"], 1)
        self.assertEqual(stats["pending"], 1)
        self.assertEqual(stats["completion_rate"], 50.0)


if __name__ == '__main__':
    unittest.main()

