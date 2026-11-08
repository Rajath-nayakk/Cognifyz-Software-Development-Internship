"""
=============================================================================
Unit Test Suite for Level 1 - Task 2: Number Pattern Generator
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

# Import functions from patterns.py
from patterns import (
    generate_right_angle_triangle,
    generate_inverted_triangle,
    generate_pyramid,
    generate_floyds_triangle,
    generate_diamond,
    get_menu_choice,
    get_row_count,
    MIN_ROWS,
    MAX_ROWS
)


class TestPatternGeneration(unittest.TestCase):
    """Tests the exact outputs of each of the five pattern generators."""

    # 1. Right-Angle Number Triangle
    def test_right_angle_triangle_single_row(self):
        result = generate_right_angle_triangle(1)
        self.assertEqual(result, ["1"])

    def test_right_angle_triangle_four_rows(self):
        result = generate_right_angle_triangle(4)
        expected = [
            "1",
            "1 2",
            "1 2 3",
            "1 2 3 4"
        ]
        self.assertEqual(result, expected)

    # 2. Inverted Number Triangle
    def test_inverted_triangle_single_row(self):
        result = generate_inverted_triangle(1)
        self.assertEqual(result, ["1"])

    def test_inverted_triangle_four_rows(self):
        result = generate_inverted_triangle(4)
        expected = [
            "1 2 3 4",
            "1 2 3",
            "1 2",
            "1"
        ]
        self.assertEqual(result, expected)

    # 3. Centered Number Pyramid
    def test_centered_pyramid_single_row(self):
        result = generate_pyramid(1)
        self.assertEqual(result, ["1"])

    def test_centered_pyramid_four_rows(self):
        result = generate_pyramid(4)
        expected = [
            "   1",
            "  1 2",
            " 1 2 3",
            "1 2 3 4"
        ]
        self.assertEqual(result, expected)

    # 4. Floyd's Triangle
    def test_floyds_triangle_single_row(self):
        result = generate_floyds_triangle(1)
        self.assertEqual(result, ["1"])

    def test_floyds_triangle_four_rows(self):
        result = generate_floyds_triangle(4)
        expected = [
            "1",
            "2 3",
            "4 5 6",
            "7 8 9 10"
        ]
        self.assertEqual(result, expected)

    # 5. Diamond Number Pattern
    def test_diamond_pattern_single_row(self):
        result = generate_diamond(1)
        # rows = 1: upper 1 row, lower 0 rows -> ["1"]
        self.assertEqual(result, ["1"])

    def test_diamond_pattern_three_rows(self):
        result = generate_diamond(3)
        expected = [
            "  1",
            " 1 2",
            "1 2 3",
            " 1 2",
            "  1"
        ]
        self.assertEqual(result, expected)
        self.assertEqual(len(result), 5)  # 2 * rows - 1 = 5


class TestInputValidation(unittest.TestCase):
    """Tests menu choices and row count input validation."""

    # Menu Choice Tests
    @patch('builtins.input', side_effect=['1'])
    def test_menu_choice_valid_1(self, mock_input):
        self.assertEqual(get_menu_choice(), '1')

    @patch('builtins.input', side_effect=['6'])
    def test_menu_choice_valid_6(self, mock_input):
        self.assertEqual(get_menu_choice(), '6')

    @patch('builtins.input', side_effect=['0', '7', 'abc', '', '3'])
    def test_menu_choice_invalid_recovery(self, mock_input):
        """Tests that invalid inputs are discarded until a valid selection ('3') is made."""
        self.assertEqual(get_menu_choice(), '3')

    # Row Count Tests
    @patch('builtins.input', side_effect=['5'])
    def test_row_count_valid(self, mock_input):
        self.assertEqual(get_row_count(), 5)

    @patch('builtins.input', side_effect=['', 'abc', '0', '-5', '99', '4'])
    def test_row_count_invalid_recovery(self, mock_input):
        """Tests that empty lines, strings, non-positive, and out-of-range rows loop until valid '4'."""
        self.assertEqual(get_row_count(), 4)

    @patch('builtins.input', side_effect=[str(MIN_ROWS)])
    def test_row_count_boundary_min(self, mock_input):
        self.assertEqual(get_row_count(), MIN_ROWS)

    @patch('builtins.input', side_effect=[str(MAX_ROWS)])
    def test_row_count_boundary_max(self, mock_input):
        self.assertEqual(get_row_count(), MAX_ROWS)


if __name__ == '__main__':
    unittest.main()

