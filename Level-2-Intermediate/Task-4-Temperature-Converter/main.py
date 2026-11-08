"""
=============================================================================
Cognifyz Technologies - Software Development Internship
Level 2 (Intermediate) - Task 4: Temperature Converter
Author: Intern
Language: Python 3
Description:
    A modular, user-friendly console application that converts temperatures
    across Celsius, Fahrenheit, and Kelvin scales. Includes input validation,
    physical boundary checks (Absolute Zero), formatted mathematical outputs,
    and a continuous interactive menu.
=============================================================================
"""

import sys

# ---------------------------------------------------------------------------
# Physical Constants (Absolute Zero Boundaries)
# ---------------------------------------------------------------------------
ABSOLUTE_ZERO_C = -273.15
ABSOLUTE_ZERO_F = -459.67
ABSOLUTE_ZERO_K = 0.0


# ---------------------------------------------------------------------------
# Conversion Functions (Pure Mathematical Logic)
# ---------------------------------------------------------------------------
def celsius_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit.
    Formula: F = (C * 9/5) + 32

    Args:
        celsius (float): Temperature in degrees Celsius.

    Returns:
        float: Temperature in degrees Fahrenheit.
    """
    return (celsius * (9.0 / 5.0)) + 32.0


def fahrenheit_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius.
    Formula: C = (F - 32) * 5/9

    Args:
        fahrenheit (float): Temperature in degrees Fahrenheit.

    Returns:
        float: Temperature in degrees Celsius.
    """
    return (fahrenheit - 32.0) * (5.0 / 9.0)


def celsius_to_kelvin(celsius):
    """
    Converts Celsius to Kelvin.
    Formula: K = C + 273.15
    """
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    """
    Converts Kelvin to Celsius.
    Formula: C = K - 273.15
    """
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    """
    Converts Fahrenheit to Kelvin via Celsius.
    """
    c = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(c)


def kelvin_to_fahrenheit(kelvin):
    """
    Converts Kelvin to Fahrenheit via Celsius.
    """
    c = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(c)


# ---------------------------------------------------------------------------
# UI & Input Validation Helpers
# ---------------------------------------------------------------------------
def display_banner():
    """Prints the application welcome header."""
    print("=" * 65)
    print("       COGNIFYZ TECHNOLOGIES - TEMPERATURE CONVERTER             ")
    print("=" * 65)
    print("Convert temperatures between Celsius, Fahrenheit, and Kelvin.")
    print("=" * 65)


def display_menu():
    """Displays the conversion selection menu."""
    print("\n" + "-" * 23 + " CONVERSION MENU " + "-" * 23)
    print("  [1] Celsius to Fahrenheit (°C -> °F)")
    print("  [2] Fahrenheit to Celsius (°F -> °C)")
    print("  [3] Celsius to Kelvin     (°C -> K)")
    print("  [4] Kelvin to Celsius     (K -> °C)")
    print("  [5] Fahrenheit to Kelvin  (°F -> K)")
    print("  [6] Kelvin to Fahrenheit  (K -> °F)")
    print("  [7] Exit Program")
    print("-" * 65)


def get_menu_choice():
    """
    Prompts the user for a menu selection and validates it (1 to 7).

    Returns:
        str: Validated menu option ('1' through '7').
    """
    while True:
        choice = input("Select an option (1-7): ").strip()
        if choice in ("1", "2", "3", "4", "5", "6", "7"):
            return choice
        print("[Error] Invalid choice! Please select an option between 1 and 7.")


def get_temperature_input(unit_name, min_limit=None):
    """
    Prompts the user for a temperature value and ensures:
    1. Input is non-empty.
    2. Input is a valid floating-point number.
    3. Input does not violate physical lower bounds (Absolute Zero).

    Args:
        unit_name (str): Name or symbol of the temperature scale.
        min_limit (float, optional): Theoretical minimum temperature.

    Returns:
        float: Validated temperature value.
    """
    prompt = f"Enter temperature in {unit_name}: "
    while True:
        raw_val = input(prompt).strip()

        if not raw_val:
            print("[Warning] Input cannot be blank. Please enter a valid number.")
            continue

        try:
            val = float(raw_val)
        except ValueError:
            print("[Error] Invalid entry! Please enter a valid numerical value (e.g., 25, -10.5).")
            continue

        if min_limit is not None and val < min_limit:
            print(f"[Warning] Physical Limit Exceeded: Temperature cannot be lower than "
                  f"Absolute Zero ({min_limit} {unit_name}). Please re-enter.")
            continue

        return val


def display_result(from_val, from_unit, to_val, to_unit, formula_str):
    """
    Displays the formatted conversion result and mathematical formula.

    Args:
        from_val (float): Original temperature value.
        from_unit (str): Original unit name.
        to_val (float): Converted temperature value.
        to_unit (str): Converted unit name.
        formula_str (str): Mathematical representation of the applied formula.
    """
    print("\n" + "=" * 55)
    print("                 CONVERSION RESULT                       ")
    print("=" * 55)
    print(f" Input Temperature  : {from_val:,.2f} {from_unit}")
    print(f" Converted Result   : {to_val:,.2f} {to_unit}")
    print(f" Applied Formula    : {formula_str}")
    print("=" * 55)


# ---------------------------------------------------------------------------
# Main Controller Loop
# ---------------------------------------------------------------------------
def main():
    """
    Main driver function: coordinates the menu loop, dispatches conversion
    functions, handles user inputs, and displays results until exit.
    """
    display_banner()

    try:
        while True:
            display_menu()
            choice = get_menu_choice()

            if choice == "7":
                print("\n" + "=" * 65)
                print(" Thank you for using Temperature Converter! Keep learning! ")
                print("=" * 65 + "\n")
                break

            if choice == "1":
                # Celsius to Fahrenheit: F = (C * 9/5) + 32
                c = get_temperature_input("Celsius (°C)", min_limit=ABSOLUTE_ZERO_C)
                f = celsius_to_fahrenheit(c)
                display_result(c, "°C", f, "°F", "F = (C × 9/5) + 32")

            elif choice == "2":
                # Fahrenheit to Celsius: C = (F - 32) * 5/9
                f = get_temperature_input("Fahrenheit (°F)", min_limit=ABSOLUTE_ZERO_F)
                c = fahrenheit_to_celsius(f)
                display_result(f, "°F", c, "°C", "C = (F - 32) × 5/9")

            elif choice == "3":
                # Celsius to Kelvin: K = C + 273.15
                c = get_temperature_input("Celsius (°C)", min_limit=ABSOLUTE_ZERO_C)
                k = celsius_to_kelvin(c)
                display_result(c, "°C", k, "K", "K = C + 273.15")

            elif choice == "4":
                # Kelvin to Celsius: C = K - 273.15
                k = get_temperature_input("Kelvin (K)", min_limit=ABSOLUTE_ZERO_K)
                c = kelvin_to_celsius(k)
                display_result(k, "K", c, "°C", "C = K - 273.15")

            elif choice == "5":
                # Fahrenheit to Kelvin
                f = get_temperature_input("Fahrenheit (°F)", min_limit=ABSOLUTE_ZERO_F)
                k = fahrenheit_to_kelvin(f)
                display_result(f, "°F", k, "K", "K = ((F - 32) × 5/9) + 273.15")

            elif choice == "6":
                # Kelvin to Fahrenheit
                k = get_temperature_input("Kelvin (K)", min_limit=ABSOLUTE_ZERO_K)
                f = kelvin_to_fahrenheit(k)
                display_result(k, "K", f, "°F", "F = ((K - 273.15) × 9/5) + 32")

    except KeyboardInterrupt:
        print("\n\n[System] Program interrupted by user. Exiting gracefully...")
        sys.exit(0)


if __name__ == "__main__":
    main()
