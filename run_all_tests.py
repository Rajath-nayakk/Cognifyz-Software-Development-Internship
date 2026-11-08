"""
=============================================================================
Cognifyz Technologies - Software Development Internship
Master Test Runner for All Six Tasks
Author: Intern (Rajath Nayak)
Language: Python 3
Description:
    Discovers and executes unit test suites across all six internship tasks
    in isolated subprocesses, providing a unified verification report.
=============================================================================
"""

import os
import sys
import subprocess
import time
import re


def main():
    start_time = time.time()
    workspace_root = os.path.dirname(os.path.abspath(__file__))

    # Test modules mapped to their respective task directories
    task_test_suites = [
        ("Level 1 - Task 1: Number Guessing Game", "Task-1-Number-Guessing-Game", "test_game.py"),
        ("Level 1 - Task 2: Number Pattern Generator", os.path.join("Level-1-Beginner", "Task-2-Number-Patterns"), "test_patterns.py"),
        ("Level 2 - Task 3: In-Memory Task CRUD App", os.path.join("Level-2-Intermediate", "Task-3-CRUD-Application"), "test_main.py"),
        ("Level 2 - Task 4: Temperature Converter", os.path.join("Level-2-Intermediate", "Task-4-Temperature-Converter"), "test_main.py"),
        ("Level 3 - Task 5: Persistent CRUD (File I/O)", os.path.join("Level-3-Advanced", "Task-5-CRUD-File-Persistence"), "test_main.py"),
        ("Level 3 - Task 6: Interactive Web Scraping", os.path.join("Level-3-Advanced", "Task-6-Interactive-Web-Scraping"), "test_main.py"),
    ]

    print("=" * 80)
    print("      COGNIFYZ TECHNOLOGIES INTERNSHIP - COMPLETE TEST SUITE VERIFICATION      ")
    print("=" * 80)

    total_tests = 0
    total_passed = 0
    total_failed = 0
    results_summary = []

    for task_name, rel_dir, test_file in task_test_suites:
        task_dir = os.path.join(workspace_root, rel_dir)
        test_path = os.path.join(task_dir, test_file)

        if not os.path.exists(test_path):
            results_summary.append((task_name, 0, 0, 1, "MISSING ✗"))
            total_failed += 1
            continue

        # Execute unittest in isolated subprocess
        cmd = [sys.executable, "-m", "unittest", test_file, "-v"]
        proc = subprocess.run(
            cmd,
            cwd=task_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        output = proc.stdout

        # Parse test count from output: e.g. "Ran 16 tests in 0.003s"
        match = re.search(r"Ran (\d+) tests? in", output)
        count = int(match.group(1)) if match else 0

        if proc.returncode == 0:
            passed = count
            failed = 0
            status = "PASSED ✓"
        else:
            failed_match = re.search(r"FAILED \((?:failures=(\d+))?(?:, )?(?:errors=(\d+))?\)", output)
            f_count = int(failed_match.group(1) or 0) if failed_match else 1
            e_count = int(failed_match.group(2) or 0) if failed_match else 0
            failed = f_count + e_count
            passed = count - failed
            status = "FAILED ✗"

        total_tests += count
        total_passed += passed
        total_failed += failed
        results_summary.append((task_name, count, passed, failed, status))

    elapsed = time.time() - start_time

    # Display Results Table
    print(f"\n{'Task Name':<48} | {'Tests':<6} | {'Passed':<6} | {'Failed':<6} | {'Status'}")
    print("-" * 80)
    for name, cnt, p, f, st in results_summary:
        print(f"{name:<48} | {cnt:<6} | {p:<6} | {f:<6} | {st}")
    print("=" * 80)

    print(f" TOTAL EXECUTED : {total_tests}")
    print(f" TOTAL PASSED   : {total_passed}")
    print(f" TOTAL FAILED   : {total_failed}")
    rate = (total_passed / total_tests * 100) if total_tests > 0 else 0.0
    print(f" SUCCESS RATE   : {rate:.1f}%")
    print(f" EXECUTION TIME : {elapsed:.3f} seconds")
    print("=" * 80)

    if total_failed == 0 and total_tests > 0:
        print(" >>> ALL 6 TASK TEST SUITES HAVE PASSED WITH 100% SUCCESS! <<<\n")
        return 0
    else:
        print(f" [FAILURES DETECTED] {total_failed} test(s) failed.\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
