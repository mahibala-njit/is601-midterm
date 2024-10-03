"""
This module contains unit tests for the calculator functionality.

It includes tests for various operations (addition, subtraction, multiplication, division)
and checks for proper error handling in cases such as division by zero and invalid inputs.
"""

import sys
import pytest
from main import calculate_and_print  # Ensure this import matches your project structure
from main import main


# Parameterize the test function to cover different operations and scenarios, including errors
@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),  # Adjusted for the actual error message
    ("9", "3", 'unknown', "Unknown operation: unknown"),  # Test for unknown operation
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),  # Testing invalid number input
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")  # Testing another invalid number input
])
def test_calculate_and_print(a_string, b_string, operation_string, expected_string, capsys):
    """
    Test the calculate_and_print function for various operations and error handling.

    Parameters:
        a_string (str): First number as a string.
        b_string (str): Second number as a string.
        operation_string (str): The operation to perform (add, subtract, etc.).
        expected_string (str): The expected output string.
        capsys (pytest fixture): Used to capture standard output.
    """
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string

def test_divide_by_zero(capsys):
    """
    Test the calculate_and_print function for division by zero.

    This should raise an appropriate error message.
    
    Parameters:
        capsys (pytest fixture): Used to capture standard output.
    """
    calculate_and_print("10", "0", "divide")  # Division by zero should raise an exception
    captured = capsys.readouterr()
    assert captured.out.strip() == "An error occurred: Cannot divide by zero"

def test_unexpected_error_handling(monkeypatch, capsys):
    """
    Test handling of unexpected errors in the calculate_and_print function.

    This simulates a faulty operation to ensure error messages are correctly handled.

    Parameters:
        monkeypatch (pytest fixture): Used to modify the Calculator's operation temporarily.
        capsys (pytest fixture): Used to capture standard output.
    """
    # Temporarily patch the operation_mappings to simulate an unexpected error
    def faulty_operation(a, b):
        raise ValueError("Unexpected error occurred")
    
    monkeypatch.setattr('calculator.Calculator.add', faulty_operation)
    
    calculate_and_print("5", "3", "add")  # This should now raise a ValueError
    captured = capsys.readouterr()
    assert captured.out.strip() == "An error occurred: Unexpected error occurred"

def test_main_correct_args(monkeypatch, capsys):
    """
    Test the main function with correct command-line arguments.

    This ensures that the expected output is produced when valid arguments are provided.

    Parameters:
        monkeypatch (pytest fixture): Used to simulate command-line arguments.
        capsys (pytest fixture): Used to capture standard output.
    """
    # Simulate passing correct arguments to the command line
    monkeypatch.setattr('sys.argv', ['calculator_main.py', '5', '3', 'add'])
    main()
    captured = capsys.readouterr()
    assert "The result of 5 add 3 is equal to 8" in captured.out.strip()

def test_invalid_operation_handling(capsys):
    """
    Test the calculate_and_print function for handling invalid operations.

    This verifies that an appropriate error message is returned for unknown operations.

    Parameters:
        capsys (pytest fixture): Used to capture standard output.
    """
    calculate_and_print("5", "3", "invalid_op")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Unknown operation: invalid_op"

def test_main_incorrect_args(monkeypatch, capsys):
    """
    Test the main function with incorrect command-line arguments.

    This checks that the script exits with an appropriate usage message when insufficient arguments are provided.

    Parameters:
        monkeypatch (pytest fixture): Used to simulate command-line arguments.
        capsys (pytest fixture): Used to capture standard output.
    """
    # Mock sys.argv with incorrect arguments (less than 4)
    monkeypatch.setattr(sys, 'argv', ['main.py', '5'])

    # Call the main function
    with pytest.raises(SystemExit):  # Expecting the script to exit with sys.exit(1)
        main()
    
    # Capture the output printed to the console
    captured = capsys.readouterr()
    
    # Assert that the correct usage message is printed when incorrect args are provided
    assert captured.out.strip() == "Usage: python calculator_main.py <number1> <number2> <operation>"

def test_divide_by_zero_in_main(monkeypatch, capsys):
    """
    Test the main function for division by zero.

    This ensures that the appropriate error message is displayed when attempting to divide by zero.

    Parameters:
        monkeypatch (pytest fixture): Used to simulate command-line arguments.
        capsys (pytest fixture): Used to capture standard output.
    """
    # Mock sys.argv for division by zero
    monkeypatch.setattr(sys, 'argv', ['main.py', '5', '0', 'divide'])
    main()  # Call main() without expecting SystemExit
    captured = capsys.readouterr()
    assert "Cannot divide by zero" in captured.out.strip()

def test_invalid_input_in_main(monkeypatch, capsys):
    """
    Test the main function for invalid string input.

    This checks that the appropriate error message is displayed when non-numeric input is provided.

    Parameters:
        monkeypatch (pytest fixture): Used to simulate command-line arguments.
        capsys (pytest fixture): Used to capture standard output.
    """
    # Mock sys.argv for invalid string input
    monkeypatch.setattr(sys, 'argv', ['main.py', 'abc', '5', 'add'])
    main()  # Call main() without expecting SystemExit
    captured = capsys.readouterr()
    assert "Invalid number input" in captured.out.strip()
