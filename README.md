# code-reviewer
# Intelligent Code Reviewer & Explainer

## Overview

This project is a simple AI-powered Code Reviewer and Explainer developed as part of the DecodeLabs Generative AI Internship.

The application analyzes a code snippet, identifies potential bugs, explains the code in plain language, and provides an optimized version of the code.

## Features

* Detects common coding issues
* Generates bug reports
* Explains code functionality
* Suggests optimized code
* Displays structured output

## Technologies Used

* Python
* VS Code

## Project Structure

```
Project4_Code_Reviewer/
│
├── code_reviewer.py
├── README.md
└── screenshots/
```

## How to Run

1. Install Python.
2. Open terminal in the project folder.
3. Run:

```bash
python code_reviewer.py
```

## Sample Output

### Bug Report

Potential Division By Zero Error Detected

### Explanation

The function divides one number by another. Calling the function with zero as the divisor causes a runtime error.

### Optimized Code

```python
def divide(a,b):
    if b == 0:
        return "Cannot divide by zero"
    return a/b

print(divide(10,2))
```

## Learning Outcomes

* Code analysis pipelines
* Structured output generation
* Bug detection and reporting
* Python programming

## Author

Generative AI Internship Project – DecodeLabs
