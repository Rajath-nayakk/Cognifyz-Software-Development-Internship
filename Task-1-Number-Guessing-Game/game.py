"""
=============================================================================
Cognifyz Technologies - Software Development Internship
Level 1 - Task 1: Number Guessing Game
Author: Intern
Language: Python 3
Description:
    A text-based number guessing game developed using modular functions,
    conditional statements, loops, exception handling, and input validation.
    The game generates a random secret number between 1 and 100, offers
    three difficulty levels, tracks attempts and scores, and supports replay.
=============================================================================
"""

import random
import sys

# ---------------------------------------------------------------------------
# Global Constants
# ---------------------------------------------------------------------------
LOWER_BOUND = 1
UPPER_BOUND = 100

# Mapping difficulty choices to (Display Name, Max Attempts)
DIFFICULTY_LEVELS = {
    "1": ("Easy", 15),
    "2": ("Medium", 10),
    "3": ("Hard", 5)
}


# ---------------------------------------------------------------------------
# Display Functions
# ---------------------------------------------------------------------------
def display_banner():
    """Prints the welcome banner and rules of the game."""
    print("=" * 65)
    print("       WELCOME TO THE NUMBER GUESSING GAME - COGNIFYZ TECH       ")
    print("=" * 65)
    print("Rules:")
    print(f"1. The computer picks a secret number between {LOWER_BOUND} and {UPPER_BOUND}.")
    print("2. You will guess the number based on 'Too High' or 'Too Low' hints.")
    print("3. Try to guess the number within the allowed attempts!")
    print("4. Points are awarded based on how quickly you guess the number.")
    print("=" * 65)


def display_difficulty_menu():
    """Displays the difficulty options available to the user."""
    print("\nSelect Difficulty Level:")
    print("  [1] Easy   - 15 attempts")
    print("  [2] Medium - 10 attempts")
    print("  [3] Hard   -  5 attempts")


# ---------------------------------------------------------------------------
# Input Validation & Helper Functions
# ---------------------------------------------------------------------------
def choose_difficulty():
    """
    Prompts the user to select a difficulty level and validates the input.

    Returns:
        tuple: (difficulty_name: str, max_attempts: int)
    """
    display_difficulty_menu()
    while True:
        choice = input("Enter choice (1, 2, or 3): ").strip()
        if choice in DIFFICULTY_LEVELS:
            diff_name, max_attempts = DIFFICULTY_LEVELS[choice]
            print(f"\n>> Difficulty set to: {diff_name} ({max_attempts} attempts allowed)")
            return diff_name, max_attempts
        print("[Error] Invalid selection. Please enter 1, 2, or 3.")


def get_user_guess(attempt_number, max_attempts):
    """
    Prompts the user for a numeric guess and validates that:
    1. The input is a valid integer (handles ValueError).
    2. The input falls within [LOWER_BOUND, UPPER_BOUND].

    Args:
        attempt_number (int): Current attempt index (1-based).
        max_attempts (int): Maximum attempts allowed for the round.

    Returns:
        int: Validated integer guess.
    """
    prompt = f"[Attempt {attempt_number}/{max_attempts}] Enter your guess ({LOWER_BOUND}-{UPPER_BOUND}): "
    while True:
        raw_input = input(prompt).strip()

        # Check for empty input
        if not raw_input:
            print("[Warning] Input cannot be empty. Please enter a valid number.")
            continue

        # Try parsing input as integer
        try:
            guess = int(raw_input)
        except ValueError:
            print("[Error] Invalid input! Only whole numbers are allowed. Please try again.")
            continue

        # Check range boundaries
        if guess < LOWER_BOUND or guess > UPPER_BOUND:
            print(f"[Warning] Out of range! Please enter a number between {LOWER_BOUND} and {UPPER_BOUND}.")
            continue

        return guess


def calculate_score(attempts_used, max_attempts):
    """
    Calculates the player's score based on attempts used versus allowed.
    Formula: ((max_attempts - attempts_used + 1) / max_attempts) * 100

    Args:
        attempts_used (int): Number of attempts the user took to win.
        max_attempts (int): Total attempts allowed for the chosen difficulty.

    Returns:
        int: Calculated score percentage (0-100).
    """
    if attempts_used > max_attempts or attempts_used <= 0:
        return 0
    score = ((max_attempts - attempts_used + 1) / max_attempts) * 100
    return max(0, min(100, round(score)))


def ask_replay():
    """
    Asks the player whether they want to play another round.

    Returns:
        bool: True if user wants to replay, False otherwise.
    """
    while True:
        choice = input("\nDo you want to play again? (yes/no or y/n): ").strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("[Error] Invalid input. Please enter 'y'/'yes' to continue or 'n'/'no' to exit.")


# ---------------------------------------------------------------------------
# Core Game Logic
# ---------------------------------------------------------------------------
def play_round(round_number=1):
    """
    Executes a single complete round of the Number Guessing Game.

    Args:
        round_number (int): The current round counter.

    Returns:
        dict: Summary of the round results containing:
              - 'won': bool
              - 'attempts_used': int
              - 'max_attempts': int
              - 'score': int
              - 'secret_number': int
              - 'difficulty': str
    """
    print("\n" + "#" * 65)
    print(f"                       ROUND {round_number}                        ")
    print("#" * 65)

    # 1. Select difficulty
    difficulty_name, max_attempts = choose_difficulty()

    # 2. Generate random secret number
    secret_number = random.randint(LOWER_BOUND, UPPER_BOUND)

    print(f"\n[System] A secret number between {LOWER_BOUND} and {UPPER_BOUND} has been generated.")
    print(f"[System] You have {max_attempts} attempts. Good luck!\n")

    attempts_used = 0
    won = False

    # 3. Main guess loop
    while attempts_used < max_attempts:
        attempts_used += 1
        guess = get_user_guess(attempts_used, max_attempts)

        # 4. Conditional checks for game feedback
        if guess == secret_number:
            won = True
            break
        elif guess < secret_number:
            remaining = max_attempts - attempts_used
            print(f">> Too Low! Think higher. ({remaining} attempts remaining)\n")
        else:
            remaining = max_attempts - attempts_used
            print(f">> Too High! Think lower. ({remaining} attempts remaining)\n")

    # 5. Round conclusion & Score evaluation
    print("-" * 65)
    if won:
        round_score = calculate_score(attempts_used, max_attempts)
        print(" [CONGRATULATIONS!] You guessed the correct number! ")
        print(f" Secret Number    : {secret_number}")
        print(f" Difficulty       : {difficulty_name}")
        print(f" Attempts Taken   : {attempts_used} / {max_attempts}")
        print(f" Final Score      : {round_score} / 100 pts")
    else:
        round_score = 0
        print(" [GAME OVER] You've exhausted all your attempts! ")
        print(f" The secret number was : {secret_number}")
        print(f" Difficulty            : {difficulty_name}")
        print(f" Attempts Used         : {max_attempts} / {max_attempts}")
        print(f" Final Score           : 0 / 100 pts")
        print(" Better luck next time!")
    print("-" * 65)

    return {
        "won": won,
        "attempts_used": attempts_used if won else max_attempts,
        "max_attempts": max_attempts,
        "score": round_score,
        "secret_number": secret_number,
        "difficulty": difficulty_name
    }


def main():
    """
    Main driver function: handles the overall game lifecycle, tracks
    cumulative statistics across rounds, and greets the user.
    """
    display_banner()

    rounds_played = 0
    rounds_won = 0
    total_score = 0
    round_history = []

    try:
        while True:
            rounds_played += 1
            result = play_round(round_number=rounds_played)

            if result["won"]:
                rounds_won += 1
            total_score += result["score"]
            round_history.append(result)

            # Check if user wants to play again
            if not ask_replay():
                break

    except KeyboardInterrupt:
        # Graceful exit if the user presses Ctrl+C
        print("\n\n[System] Game interrupted by player. Exiting gracefully...")

    # Final Session Summary
    print("\n" + "=" * 65)
    print("                    GAME SESSION SUMMARY                         ")
    print("=" * 65)
    print(f" Total Rounds Played : {rounds_played}")
    print(f" Rounds Won          : {rounds_won}")
    print(f" Rounds Lost         : {rounds_played - rounds_won}")
    avg_score = (total_score / rounds_played) if rounds_played > 0 else 0
    print(f" Cumulative Score    : {total_score} pts")
    print(f" Average Score       : {avg_score:.1f} pts")
    print("=" * 65)
    print(" Thank you for playing! Keep coding and have a great day!")
    print("=" * 65 + "\n")


# ---------------------------------------------------------------------------
# Program Entry Point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()

