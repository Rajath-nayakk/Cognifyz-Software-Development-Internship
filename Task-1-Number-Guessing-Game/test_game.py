"""
Unit and Integration Test Suite for Task 1: Number Guessing Game
Author: Intern (Cognifyz Technologies)
Language: Python 3
"""

import unittest
from unittest.mock import patch
import io
import sys
import random

# Import functions from game.py
from game import (
    calculate_score,
    choose_difficulty,
    get_user_guess,
    ask_replay,
    play_round,
    LOWER_BOUND,
    UPPER_BOUND
)


class TestScoreCalculation(unittest.TestCase):
    """Tests the score calculation formula under different circumstances."""

    def test_first_attempt_win(self):
        """Winning on the 1st attempt should yield 100 points."""
        score_easy = calculate_score(attempts_used=1, max_attempts=15)
        score_med = calculate_score(attempts_used=1, max_attempts=10)
        score_hard = calculate_score(attempts_used=1, max_attempts=5)
        self.assertEqual(score_easy, 100)
        self.assertEqual(score_med, 100)
        self.assertEqual(score_hard, 100)

    def test_last_attempt_win(self):
        """Winning on the very last attempt should yield minimal positive points."""
        # For Easy: ((15 - 15 + 1) / 15) * 100 = 1/15 * 100 = ~7 points
        score_easy = calculate_score(attempts_used=15, max_attempts=15)
        self.assertEqual(score_easy, 7)

        # For Medium: 1/10 * 100 = 10 points
        score_med = calculate_score(attempts_used=10, max_attempts=10)
        self.assertEqual(score_med, 10)

        # For Hard: 1/5 * 100 = 20 points
        score_hard = calculate_score(attempts_used=5, max_attempts=5)
        self.assertEqual(score_hard, 20)

    def test_zero_or_exceeded_attempts(self):
        """Attempts used <= 0 or > max_attempts should return 0."""
        self.assertEqual(calculate_score(attempts_used=16, max_attempts=15), 0)
        self.assertEqual(calculate_score(attempts_used=0, max_attempts=10), 0)


class TestDifficultySelection(unittest.TestCase):
    """Tests difficulty selection with valid and invalid inputs."""

    @patch('builtins.input', side_effect=['1'])
    def test_easy_selection(self, mock_input):
        diff_name, max_attempts = choose_difficulty()
        self.assertEqual(diff_name, "Easy")
        self.assertEqual(max_attempts, 15)

    @patch('builtins.input', side_effect=['2'])
    def test_medium_selection(self, mock_input):
        diff_name, max_attempts = choose_difficulty()
        self.assertEqual(diff_name, "Medium")
        self.assertEqual(max_attempts, 10)

    @patch('builtins.input', side_effect=['3'])
    def test_hard_selection(self, mock_input):
        diff_name, max_attempts = choose_difficulty()
        self.assertEqual(diff_name, "Hard")
        self.assertEqual(max_attempts, 5)

    @patch('builtins.input', side_effect=['9', 'abc', '', '2'])
    def test_invalid_then_valid_selection(self, mock_input):
        """Should prompt repeatedly until valid input (2) is provided."""
        diff_name, max_attempts = choose_difficulty()
        self.assertEqual(diff_name, "Medium")
        self.assertEqual(max_attempts, 10)


class TestUserInputValidation(unittest.TestCase):
    """Tests the guess input validator with valid, invalid, out-of-range, and empty inputs."""

    @patch('builtins.input', side_effect=['50'])
    def test_valid_guess(self, mock_input):
        guess = get_user_guess(1, 10)
        self.assertEqual(guess, 50)

    @patch('builtins.input', side_effect=['invalid', '', '0', '101', '75'])
    def test_recover_from_invalid_inputs(self, mock_input):
        """Tests that text, empty lines, and out-of-bounds numbers are rejected until 75 is entered."""
        guess = get_user_guess(1, 10)
        self.assertEqual(guess, 75)


class TestReplayPrompt(unittest.TestCase):
    """Tests the replay query with yes/no and retry logic."""

    @patch('builtins.input', side_effect=['y'])
    def test_replay_yes_single(self, mock_input):
        self.assertTrue(ask_replay())

    @patch('builtins.input', side_effect=['yes'])
    def test_replay_yes_full(self, mock_input):
        self.assertTrue(ask_replay())

    @patch('builtins.input', side_effect=['n'])
    def test_replay_no_single(self, mock_input):
        self.assertFalse(ask_replay())

    @patch('builtins.input', side_effect=['invalid', 'no'])
    def test_replay_invalid_then_no(self, mock_input):
        self.assertFalse(ask_replay())


class TestGameplayFlow(unittest.TestCase):
    """Tests full simulated rounds for winning and losing scenarios."""

    @patch('random.randint', return_value=42)
    @patch('builtins.input', side_effect=['3', '42'])  # Hard mode (3), Guess 42
    def test_win_on_first_guess(self, mock_input, mock_random):
        result = play_round(round_number=1)
        self.assertTrue(result['won'])
        self.assertEqual(result['attempts_used'], 1)
        self.assertEqual(result['score'], 100)
        self.assertEqual(result['secret_number'], 42)

    @patch('random.randint', return_value=70)
    @patch('builtins.input', side_effect=['3', '50', '80', '70'])  # Hard mode, 50(low), 80(high), 70(win)
    def test_win_with_hints(self, mock_input, mock_random):
        result = play_round(round_number=1)
        self.assertTrue(result['won'])
        self.assertEqual(result['attempts_used'], 3)
        self.assertEqual(result['secret_number'], 70)
        # Score on Hard (max 5) with 3 used: ((5 - 3 + 1)/5)*100 = 60
        self.assertEqual(result['score'], 60)

    @patch('random.randint', return_value=99)
    @patch('builtins.input', side_effect=['3', '10', '20', '30', '40', '50'])  # Hard mode (5 attempts), all wrong
    def test_loss_exhaust_attempts(self, mock_input, mock_random):
        result = play_round(round_number=1)
        self.assertFalse(result['won'])
        self.assertEqual(result['attempts_used'], 5)
        self.assertEqual(result['score'], 0)
        self.assertEqual(result['secret_number'], 99)


if __name__ == '__main__':
    unittest.main()

