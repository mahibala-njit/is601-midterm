# Homework 4 - Generate tests using Faker

# Calculator Project

This project is a simple calculator implemented in Python that performs basic arithmetic operations: addition, subtraction, multiplication, and division. The calculator is designed using object-oriented principles and showcases various design patterns, including class methods, static methods, and a calculation history feature.

## Features

- Perform basic arithmetic operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division (with error handling for division by zero)
- Store a history of calculations
- Retrieve the last calculation
- Clear the calculation history
- Uses `Decimal` for high-precision arithmetic

## Addtional Features

- Added the "faker" libary
- Added a new command to pytest to generate  N number of records "tests/conftest.py"
- Added a main.py file to serve as the entry point

## Install Instructions

1. Clone
2. Install the requirements
```bash
pip3 install -r requirments.txt
```

## Testing 
This project includes extensive unit tests for each feature and operation. Testing is done using the pytest framework, and code linting is handled by pylint to ensure code quality.

The project has been fully tested.

```bash
pytest --num_records=100
pytest --pylint --cov
pytest --pylint --cov --cov-report=xml --cov-report=term-missing
```
pytest results:
![image](https://github.com/user-attachments/assets/d3b61e03-b8ca-4c4e-a289-6c5c3a1b1975)


