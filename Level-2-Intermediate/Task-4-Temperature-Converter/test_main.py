"""
=============================================================================
Automated Unit Test Suite for Level 2 - Task 4: Temperature Converter
Author: Intern (Cognifyz Technologies)
Language: Python 3
=============================================================================
"""

import unittest
from unittest.mock import patch
import os
import sys

# Ensure local directory is in Python path for test execution from any directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_fahrenheit,
    get_menu_choice,
    get_temperature_input,
    ABSOLUTE_ZERO_C,
    ABSOLUTE_ZERO_F,
    ABSOLUTE_ZERO_K
)


class TestTemperatureFormulas(unittest.TestCase):
    """Tests the mathematical accuracy of each temperature conversion formula."""

    # --- Celsius to Fahrenheit: F = (C * 9/5) + 32 ---
    def test_celsius_to_fahrenheit_freezing_point(self):
        """0°C should convert exactly to 32°F."""
        self.assertAlmostEqual(celsius_to_fahrenheit(0.0), 32.0, places=4)

    def test_celsius_to_fahrenheit_boiling_point(self):
        """100°C should convert exactly to 212°F."""
        self.assertAlmostEqual(celsius_to_fahrenheit(100.0), 212.0, places=4)

    def test_celsius_to_fahrenheit_equal_point(self):
        """-40°C should equal -40°F."""
        self.assertAlmostEqual(celsius_to_fahrenheit(-40.0), -40.0, places=4)

    def test_celsius_to_fahrenheit_body_temp(self):
        """37°C should convert to 98.6°F."""
        self.assertAlmostEqual(celsius_to_fahrenheit(37.0), 98.6, places=2)

    # --- Fahrenheit to Celsius: C = (F - 32) * 5/9 ---
    def test_fahrenheit_to_celsius_freezing_point(self):
        """32°F should convert exactly to 0°C."""
        self.assertAlmostEqual(fahrenheit_to_celsius(32.0), 0.0, places=4)

    def test_fahrenheit_to_celsius_boiling_point(self):
        """212°F should convert exactly to 100°C."""
        self.assertAlmostEqual(fahrenheit_to_celsius(212.0), 100.0, places=4)

    def test_fahrenheit_to_celsius_equal_point(self):
        """-40°F should equal -40°C."""
        self.assertAlmostEqual(fahrenheit_to_celsius(-40.0), -40.0, places=4)

    def test_fahrenheit_to_celsius_negative_range(self):
        """-10°F should convert to -23.3333°C."""
        self.assertAlmostEqual(fahrenheit_to_celsius(-10.0), -23.3333, places=3)

    # --- Kelvin Conversions ---
    def test_celsius_to_kelvin_zero(self):
        """0°C should equal 273.15 K."""
        self.assertAlmostEqual(celsius_to_kelvin(0.0), 273.15, places=2)

    def test_kelvin_to_celsius_zero_k(self):
        """0 K should equal -273.15°C."""
        self.assertAlmostEqual(kelvin_to_celsius(0.0), -273.15, places=2)

    def test_fahrenheit_to_kelvin(self):
        """32°F should equal 273.15 K."""
        self.assertAlmostEqual(fahrenheit_to_kelvin(32.0), 273.15, places=2)

    def test_kelvin_to_fahrenheit(self):
        """0 K should convert to -459.67°F."""
        self.assertAlmostEqual(kelvin_to_fahrenheit(0.0), -459.67, places=2)


class TestInputValidation(unittest.TestCase):
    """Tests menu selection and temperature numeric input validation."""

    @patch('builtins.input', side_effect=['1'])
    def test_menu_choice_valid(self, mock_input):
        self.assertEqual(get_menu_choice(), '1')

    @patch('builtins.input', side_effect=['0', '9', 'abc', '', '7'])
    def test_menu_choice_invalid_recovery(self, mock_input):
        """Tests that invalid menu options loop until a valid choice ('7') is made."""
        self.assertEqual(get_menu_choice(), '7')

    @patch('builtins.input', side_effect=['25.5'])
    def test_temperature_input_valid_positive_float(self, mock_input):
        val = get_temperature_input("Celsius")
        self.assertEqual(val, 25.5)

    @patch('builtins.input', side_effect=['-15.0'])
    def test_temperature_input_valid_negative_float(self, mock_input):
        val = get_temperature_input("Celsius")
        self.assertEqual(val, -15.0)

    @patch('builtins.input', side_effect=['', 'invalid_str', '100'])
    def test_temperature_input_recover_from_non_numeric(self, mock_input):
        """Tests that empty lines and text loop until '100' is provided."""
        val = get_temperature_input("Celsius")
        self.assertEqual(val, 100.0)

    @patch('builtins.input', side_effect=['-300', '20'])
    def test_temperature_input_absolute_zero_boundary(self, mock_input):
        """Tests that temperatures below absolute zero (-273.15°C) are rejected until valid (20)."""
        val = get_temperature_input("Celsius", min_limit=ABSOLUTE_ZERO_C)
        self.assertEqual(val, 20.0)


if __name__ == '__main__':
    unittest.main()

