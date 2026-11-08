# Cognifyz Technologies – Software Development Internship
## Level 2 (Intermediate) – Task 4: Temperature Converter

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)
![Internship](https://img.shields.io/badge/Internship-Cognifyz%20Technologies-orange.svg)

---

## 📌 Project Overview
The **Temperature Converter** is a modular Python command-line utility developed as part of **Level 2 – Task 4** for the Cognifyz Technologies Software Development Internship.

The tool provides bidirectional conversion between the major thermal scales—**Celsius**, **Fahrenheit**, and **Kelvin**. Built with mathematical precision and physical validity in mind, it implements exact conversion formulas, validates negative numbers against Absolute Zero thresholds, formats outputs cleanly to two decimal places, and operates in a continuous interactive menu loop.

---

## 🎯 Objectives
- Build a console-based temperature conversion tool using clean, functional programming principles.
- Implement the official mathematical conversion formulas:
  $$F = \left(C \times \frac{9}{5}\right) + 32$$
  $$C = (F - 32) \times \frac{5}{9}$$
- Expand support to Kelvin ($K = C + 273.15$, $C = K - 273.15$).
- Implement defensive input validation for floating-point values and menu choices.
- Accurately process negative temperatures and physically impossible inputs ($< \text{Absolute Zero}$).
- Write comprehensive automated unit tests covering mathematical edge points and validation recovery.

---

## ✨ Features
1. **Six-Way Conversion Spectrum**:
   - Celsius to Fahrenheit (°C $\rightarrow$ °F)
   - Fahrenheit to Celsius (°F $\rightarrow$ °C)
   - Celsius to Kelvin (°C $\rightarrow$ K)
   - Kelvin to Celsius (K $\rightarrow$ °C)
   - Fahrenheit to Kelvin (°F $\rightarrow$ K)
   - Kelvin to Fahrenheit (K $\rightarrow$ °F)
2. **Physical Boundary Checks**:
   - Enforces Absolute Zero limits ($-273.15^\circ\text{C}$, $-459.67^\circ\text{F}$, $0\text{ K}$) to prevent physically meaningless calculations.
3. **Robust Input Sanitization**:
   - Handles floats, negative values, and zero.
   - Catches `ValueError` when non-numeric characters are entered without terminating.
   - Prevents blank inputs.
4. **Transparent Mathematical Output**:
   - Formatted to 2 decimal places with scale abbreviations.
   - Displays the exact mathematical formula utilized in the calculation.
5. **Continuous Execution**: Stays active until user specifically chooses the exit option.

---

## 🛠️ Technologies Used
- **Programming Language**: Python 3.8+ (tested on Python 3.14)
- **Standard Modules**: `sys`, `unittest`, `unittest.mock`
- **Dependencies**: None (pure standard library)

---

## 📁 Project Structure
```text
Task-4-Temperature-Converter/
│
├── main.py                 # Core application with conversion functions and menu loop
├── test_main.py            # Automated test suite (18 unit tests)
├── README.md               # Detailed project documentation
└── screenshots/            # Directory reserved for submission evidence
    └── README.md           # Screenshot capture guide
```

---

## 🚀 Installation & How to Run

### 1. Prerequisites
Verify Python 3 is installed:
```bash
py --version
```

### 2. Navigate to Task 4 Directory
```bash
cd "Level-2-Intermediate/Task-4-Temperature-Converter"
```

### 3. Run the Application
```bash
py main.py
```

### 4. Run Automated Unit Tests
```bash
py -m unittest test_main.py -v
```

---

## 💻 Sample Outputs

### 1. Celsius to Fahrenheit (Boiling Point & Normal Body Temperature)
```text
----------------------- CONVERSION MENU -----------------------
  [1] Celsius to Fahrenheit (°C -> °F)
  [2] Fahrenheit to Celsius (°F -> °C)
  [3] Celsius to Kelvin     (°C -> K)
  [4] Kelvin to Celsius     (K -> °C)
  [5] Fahrenheit to Kelvin  (°F -> K)
  [6] Kelvin to Fahrenheit  (K -> °F)
  [7] Exit Program
-----------------------------------------------------------------
Select an option (1-7): 1
Enter temperature in Celsius (°C): 100

=======================================================
                 CONVERSION RESULT                       
=======================================================
 Input Temperature  : 100.00 °C
 Converted Result   : 212.00 °F
 Applied Formula    : F = (C × 9/5) + 32
=======================================================
```

### 2. Negative Temperature Equal Point ($-40^\circ$)
```text
Select an option (1-7): 2
Enter temperature in Fahrenheit (°F): -40

=======================================================
                 CONVERSION RESULT                       
=======================================================
 Input Temperature  : -40.00 °F
 Converted Result   : -40.00 °C
 Applied Formula    : C = (F - 32) × 5/9
=======================================================
```

### 3. Absolute Zero Violation Warning
```text
Select an option (1-7): 1
Enter temperature in Celsius (°C): -300
[Warning] Physical Limit Exceeded: Temperature cannot be lower than Absolute Zero (-273.15 Celsius). Please re-enter.
Enter temperature in Celsius (°C): 25
```

---

## 🧠 Key Concepts Learned & Demonstrated
- **Mathematical Modeling**: Translating scientific algebraic equations into precise Python functions.
- **Floating-Point Handling**: Accurately working with `float` types and precision formatting (`{val:,.2f}`).
- **Defensive Input Loops**: Designing user-friendly validation loops using `try-except` blocks.
- **Unit Testing Mathematical Edge Cases**: Validating freezing points, boiling points, negative values, and the $-40^\circ$ equivalence point using `assertAlmostEqual`.

---

## 👤 Author
- **Developer**: Rajath Nayak
- **Internship**: Cognifyz Technologies Software Development Internship
- **Track**: Level 2 (Intermediate) – Task 4
