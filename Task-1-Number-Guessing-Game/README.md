# Cognifyz Technologies – Software Development Internship
## Level 1 – Task 1: Number Guessing Game

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)
![Internship](https://img.shields.io/badge/Internship-Cognifyz%20Technologies-orange.svg)

---

## 📌 Project Overview
The **Number Guessing Game** is a text-based interactive Python application developed as part of **Level 1 – Task 1** for the Cognifyz Technologies Software Development Internship. 

The application generates a random integer between 1 and 100 and prompts the user to guess it within a set number of attempts determined by the chosen difficulty level. With each guess, the game delivers intuitive feedback ("Too High" or "Too Low"), handles invalid inputs safely without penalties, computes an efficiency-based score upon completion, and offers replayability.

---

## 🎯 Objectives
- Build a text-based game utilizing fundamental programming constructs in Python.
- Apply conditional logic (`if-elif-else`) to guide the user toward the secret number.
- Implement robust input validation and exception handling (`try-except`) for non-numeric or out-of-range entries.
- Design a modular, function-based codebase adhering to clean code and PEP 8 guidelines.
- Incorporate interactive features such as difficulty selection, score calculation, round counters, and replay options.

---

## ✨ Features
1. **Random Number Generation**: Employs Python's standard `random.randint` to pick a non-deterministic number between 1 and 100 in every round.
2. **Three Difficulty Levels**:
   - **Easy**: 15 attempts (for casual play and beginners).
   - **Medium**: 10 attempts (balanced challenge).
   - **Hard**: 5 attempts (demanding precision).
3. **Dynamic Feedback**: Real-time guidance informs the user whether their guess is *Too High* or *Too Low*, including remaining attempt counts.
4. **Input Sanitization & Exception Handling**:
   - Traps non-integer entries (letters, symbols, blanks) via `try...except ValueError`.
   - Rejects numbers outside the range `[1, 100]`.
   - Invalid entries do **not** consume attempts.
5. **Score & Performance Evaluation**:
   - Dynamically calculates the score based on efficiency:
     $$\text{Score} = \max\left(0, \text{round}\left(\frac{\text{max\_attempts} - \text{attempts\_taken} + 1}{\text{max\_attempts}} \times 100\right)\right)$$
6. **Replay & Session History**:
   - Allows users to start new rounds seamlessly.
   - Summarizes total rounds played, rounds won, total score, and average score upon exiting.
7. **Clean CLI Experience**: Formatted ASCII banners, borders, and clear user prompts.

---

## 🛠️ Technologies Used
- **Programming Language**: Python 3.8+ (tested on Python 3.14)
- **Standard Libraries**:
  - `random`: For generating pseudorandom target numbers.
  - `sys`: For system-level utilities.
  - `unittest`: For automated test coverage.
- **Operating Environment**: Cross-platform (Windows, macOS, Linux).

---

## 📁 Project Structure
```text
Task-1-Number-Guessing-Game/
│
├── game.py                 # Main game source code (modular and documented)
├── test_game.py            # Comprehensive unit and integration test suite (16 tests)
├── README.md               # Professional project documentation
└── screenshots/            # Directory reserved for internship submission screenshots
    └── README.md           # Guide on which screenshots to capture
```

---

## 🚀 Installation & Setup

### Prerequisites
Make sure Python 3 is installed on your computer. You can check your version by running:
```bash
python --version
# or on Windows:
py --version
```

### Clone or Download the Project
Navigate to the project root directory:
```bash
cd "Task-1-Number-Guessing-Game"
```

No external third-party libraries (e.g. `pip install`) are required, as the game utilizes only Python standard modules.

---

## 🎮 How to Run

### 1. Launch the Game
Run the game using the Python interpreter:
```bash
python game.py
# or
py game.py
```

### 2. Run Automated Unit Tests
To verify test coverage and validate all edge cases:
```bash
python -m unittest test_game.py -v
# or
py -m unittest test_game.py -v
```

---

## 💻 Sample Output

### Successful Game Session
```text
=================================================================
       WELCOME TO THE NUMBER GUESSING GAME - COGNIFYZ TECH       
=================================================================
Rules:
1. The computer picks a secret number between 1 and 100.
2. You will guess the number based on 'Too High' or 'Too Low' hints.
3. Try to guess the number within the allowed attempts!
4. Points are awarded based on how quickly you guess the number.
=================================================================

#################################################################
                       ROUND 1                        
#################################################################

Select Difficulty Level:
  [1] Easy   - 15 attempts
  [2] Medium - 10 attempts
  [3] Hard   -  5 attempts
Enter choice (1, 2, or 3): 2

>> Difficulty set to: Medium (10 attempts allowed)

[System] A secret number between 1 and 100 has been generated.
[System] You have 10 attempts. Good luck!

[Attempt 1/10] Enter your guess (1-100): 50
>> Too Low! Think higher. (9 attempts remaining)

[Attempt 2/10] Enter your guess (1-100): 75
>> Too High! Think lower. (8 attempts remaining)

[Attempt 3/10] Enter your guess (1-100): 64
-----------------------------------------------------------------
 [CONGRATULATIONS!] You guessed the correct number! 
 Secret Number    : 64
 Difficulty       : Medium
 Attempts Taken   : 3 / 10
 Final Score      : 80 / 100 pts
-----------------------------------------------------------------

Do you want to play again? (yes/no or y/n): n

=================================================================
                    GAME SESSION SUMMARY                         
=================================================================
 Total Rounds Played : 1
 Rounds Won          : 1
 Rounds Lost         : 0
 Cumulative Score    : 80 pts
 Average Score       : 80.0 pts
=================================================================
 Thank you for playing! Keep coding and have a great day!
=================================================================
```

### Input Validation & Error Handling
```text
[Attempt 1/5] Enter your guess (1-100): hello
[Error] Invalid input! Only whole numbers are allowed. Please try again.

[Attempt 1/5] Enter your guess (1-100): 150
[Warning] Out of range! Please enter a number between 1 and 100.
```

---

## 🧠 Key Concepts Learned & Demonstrated
- **Control Flow**: Proficient use of `while` loops, `for` constructs, `break`, `continue`, and nested conditional logic (`if`, `elif`, `else`).
- **Defensive Programming & Exception Handling**: Preventing runtime crashes using `try-except` blocks (`ValueError`), validating boundary constraints, and handling `KeyboardInterrupt` for graceful shutdowns.
- **Modularity & Clean Code**: Breaking down application logic into focused, single-responsibility functions (`display_banner`, `choose_difficulty`, `get_user_guess`, `calculate_score`, `play_round`, `ask_replay`).
- **Automated Testing**: Writing test cases with `unittest` and `unittest.mock` (`patch`) to simulate user inputs, edge cases, and deterministic random values.
- **UX in CLI**: Providing clear feedback, attempt countdowns, and detailed session statistics.

---

## 👤 Author
- **Intern Name**: Rajath Nayak
- **Internship**: Cognifyz Technologies Software Development Internship
- **Task**: Level 1 – Task 1 (Number Guessing Game)

