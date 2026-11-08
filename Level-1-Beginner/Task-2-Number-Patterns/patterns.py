"""
=============================================================================
Cognifyz Technologies - Software Development Internship
Level 1 - Task 2: Number Pattern Generator
Author: Intern
Language: Python 3
Description:
    A modular, interactive Python application that generates various
    geometric number patterns using nested loops. Includes input validation,
    menu-driven navigation, multiple pattern selections, and defensive programming.
=============================================================================
"""

import sys

# ---------------------------------------------------------------------------
# Global Constants
# ---------------------------------------------------------------------------
MIN_ROWS = 1
MAX_ROWS = 20  # Recommended maximum to prevent terminal line wrapping


# ---------------------------------------------------------------------------
# Pattern Generation Functions (Using Nested Loops)
# ---------------------------------------------------------------------------
def generate_right_angle_triangle(rows):
    """
    Generates a right-angle number triangle where each row `i`
    contains numbers from 1 to `i`.

    Example (rows = 4):
    1
    1 2
    1 2 3
    1 2 3 4

    Args:
        rows (int): Number of rows to generate.

    Returns:
        list of str: List containing each line of the pattern.
    """
    pattern_lines = []
    # Outer loop controls the row number (1 to rows)
    for row in range(1, rows + 1):
        row_numbers = []
        # Inner loop generates numbers from 1 up to the current row number
        for col in range(1, row + 1):
            row_numbers.append(str(col))
        pattern_lines.append(" ".join(row_numbers))
    return pattern_lines


def generate_inverted_triangle(rows):
    """
    Generates an inverted number triangle starting with `rows` numbers
    and decreasing down to 1 number.

    Example (rows = 4):
    1 2 3 4
    1 2 3
    1 2
    1

    Args:
        rows (int): Number of rows to generate.

    Returns:
        list of str: List containing each line of the pattern.
    """
    pattern_lines = []
    # Outer loop counts downwards from rows down to 1
    for row in range(rows, 0, -1):
        row_numbers = []
        # Inner loop generates numbers from 1 up to the current row count
        for col in range(1, row + 1):
            row_numbers.append(str(col))
        pattern_lines.append(" ".join(row_numbers))
    return pattern_lines


def generate_pyramid(rows):
    """
    Generates a centered number pyramid with symmetrical indentation.

    Example (rows = 4):
       1
      1 2
     1 2 3
    1 2 3 4

    Args:
        rows (int): Number of rows to generate.

    Returns:
        list of str: List containing each line of the pattern.
    """
    pattern_lines = []
    # Outer loop controls the row index (1 to rows)
    for row in range(1, rows + 1):
        # Leading spaces to center-align the pyramid: (rows - row)
        leading_spaces = " " * (rows - row)

        row_numbers = []
        # Inner loop generates numbers from 1 to the current row
        for col in range(1, row + 1):
            row_numbers.append(str(col))

        numbers_str = " ".join(row_numbers)
        pattern_lines.append(leading_spaces + numbers_str)
    return pattern_lines


def generate_floyds_triangle(rows):
    """
    Generates Floyd's Triangle: consecutive natural integers starting from 1
    arranged in a right-angled triangle.

    Example (rows = 4):
    1
    2 3
    4 5 6
    7 8 9 10

    Args:
        rows (int): Number of rows to generate.

    Returns:
        list of str: List containing each line of the pattern.
    """
    pattern_lines = []
    current_number = 1  # Continuous counter for consecutive numbers

    # Outer loop determines the number of rows
    for row in range(1, rows + 1):
        row_numbers = []
        # Inner loop places `row` count of consecutive numbers
        for _ in range(1, row + 1):
            row_numbers.append(str(current_number))
            current_number += 1
        pattern_lines.append(" ".join(row_numbers))
    return pattern_lines


def generate_diamond(rows):
    """
    Generates a symmetrical diamond number pattern.
    The upper section consists of `rows` lines, and the lower
    section consists of `rows - 1` lines.

    Example (rows = 3):
      1
     1 2
    1 2 3
     1 2
      1

    Args:
        rows (int): Number of rows in the upper half of the diamond.

    Returns:
        list of str: List containing each line of the pattern.
    """
    pattern_lines = []

    # --- Part 1: Upper Pyramid (including the center widest row) ---
    for row in range(1, rows + 1):
        leading_spaces = " " * (rows - row)
        row_numbers = []
        for col in range(1, row + 1):
            row_numbers.append(str(col))
        pattern_lines.append(leading_spaces + " ".join(row_numbers))

    # --- Part 2: Lower Inverted Pyramid ---
    for row in range(rows - 1, 0, -1):
        leading_spaces = " " * (rows - row)
        row_numbers = []
        for col in range(1, row + 1):
            row_numbers.append(str(col))
        pattern_lines.append(leading_spaces + " ".join(row_numbers))

    return pattern_lines


# ---------------------------------------------------------------------------
# Display & UI Helpers
# ---------------------------------------------------------------------------
def display_banner():
    """Displays the welcome header for the application."""
    print("=" * 65)
    print("       COGNIFYZ TECHNOLOGIES - NUMBER PATTERN GENERATOR          ")
    print("=" * 65)
    print("Generate and visualize geometric number patterns using loops.")
    print("=" * 65)


def display_menu():
    """Prints the pattern selection menu options."""
    print("\nPattern Selection Menu:")
    print("  [1] Right-Angle Number Triangle")
    print("  [2] Inverted Number Triangle")
    print("  [3] Centered Number Pyramid")
    print("  [4] Floyd's Triangle")
    print("  [5] Diamond Number Pattern")
    print("  [6] Exit Application")


def print_pattern(title, lines):
    """
    Prints the generated pattern cleanly with labeled borders.

    Args:
        title (str): Title/Name of the pattern.
        lines (list of str): Lines of the pattern to output.
    """
    border_len = max(len(title) + 12, 45)
    print("\n" + "-" * border_len)
    print(f"  OUTPUT: {title}")
    print("-" * border_len)
    for line in lines:
        print(line)
    print("-" * border_len + "\n")


# ---------------------------------------------------------------------------
# Input Validation Handlers
# ---------------------------------------------------------------------------
def get_menu_choice():
    """
    Prompts the user for a menu choice and validates that it is between 1 and 6.

    Returns:
        str: Validated menu option ('1' through '6').
    """
    while True:
        choice = input("Enter your choice (1-6): ").strip()
        if choice in ("1", "2", "3", "4", "5", "6"):
            return choice
        print("[Error] Invalid selection! Please enter a number between 1 and 6.")


def get_row_count():
    """
    Prompts the user for the number of rows and validates:
    1. Input is non-empty.
    2. Input is a valid positive integer.
    3. Input is within [MIN_ROWS, MAX_ROWS].

    Returns:
        int: Validated number of rows.
    """
    prompt = f"Enter number of rows ({MIN_ROWS}-{MAX_ROWS}): "
    while True:
        raw_input = input(prompt).strip()

        # Check for empty string
        if not raw_input:
            print("[Warning] Input cannot be blank. Please enter a whole number.")
            continue

        # Check for numeric integer
        try:
            rows = int(raw_input)
        except ValueError:
            print("[Error] Invalid input! Only positive integers are allowed.")
            continue

        # Check range boundaries
        if rows < MIN_ROWS:
            print(f"[Warning] Rows must be at least {MIN_ROWS}. Please try again.")
            continue
        if rows > MAX_ROWS:
            print(f"[Warning] Maximum supported rows is {MAX_ROWS} for optimal display.")
            continue

        return rows


# ---------------------------------------------------------------------------
# Main Controller & Application Loop
# ---------------------------------------------------------------------------
def main():
    """
    Main driver function: orchestrates user interactions, routes menu
    choices to corresponding pattern generators, and handles program lifecycle.
    """
    display_banner()

    # Pattern routing map linking choice to (Title, Generator Function)
    pattern_dispatch = {
        "1": ("Right-Angle Number Triangle", generate_right_angle_triangle),
        "2": ("Inverted Number Triangle", generate_inverted_triangle),
        "3": ("Centered Number Pyramid", generate_pyramid),
        "4": ("Floyd's Triangle", generate_floyds_triangle),
        "5": ("Diamond Number Pattern", generate_diamond)
    }

    try:
        while True:
            display_menu()
            choice = get_menu_choice()

            # Exit condition
            if choice == "6":
                print("\n" + "=" * 65)
                print(" Thank you for using Number Pattern Generator! Happy Coding! ")
                print("=" * 65 + "\n")
                break

            # Prompt for rows
            rows = get_row_count()

            # Retrieve and execute pattern generator
            title, generator_func = pattern_dispatch[choice]
            pattern_lines = generator_func(rows)

            # Display the result
            print_pattern(title, pattern_lines)

    except KeyboardInterrupt:
        print("\n\n[System] Program interrupted by user. Exiting gracefully...")
        sys.exit(0)


# ---------------------------------------------------------------------------
# Script Entry Point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()

