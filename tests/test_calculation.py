"""
This module contains tests for the calculator operations and Calculation class.

The tests are designed to verify the correctness of basic arithmetic operations
(addition, subtraction, multiplication, division) implemented in the calculator.operations module,
as well as the functionality of the Calculation class that encapsulates these operations.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add,  divide, multiply, subtract, sin, cos, tan, sqrt

def test_calculation_operations(operation, expected, a, b):
    """
    Test calculation operations with various scenarios.
    
    This test ensures that the Calculation class correctly performs the arithmetic operation
    (specified by the 'operation' parameter) on two Decimal operands ('a' and 'b'),
    and that the result matches the expected outcome.
    
    Parameters:
        a (Decimal): The first operand in the calculation.
        b (Decimal): The second operand in the calculation.
        operation (function): The arithmetic operation to perform.
        expected (Decimal): The expected result of the operation.
    """
    calc = Calculation(operation,a, b)  # Create a Calculation instance with the provided operands and operation.
    assert calc.perform() == expected, f"Failed {operation} operation with {a} and {b}"  # Perform the operation and assert that the result matches the expected value.

def test_calculation_repr():
    """Test the string representation (__repr__) of the Calculation class."""
    calc = Calculation(add, Decimal('10'), Decimal('5'))  # Create a Calculation instance for testing.
    expected_repr = "Calculation(operation=add, a=10, b=5)"  # Expected string representation.
    assert repr(calc) == expected_repr, f"__repr__ output '{repr(calc)}' does not match expected '{expected_repr}'"
    assert repr(calc) == expected_repr, "The __repr__ method output does not match the expected string."  

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    
    This test checks that attempting to perform a division operation with a zero divisor
    correctly raises a ValueError, as dividing by zero is mathematically undefined and should be handled as an error.
    """
    calc = Calculation(divide, Decimal('10'), Decimal('0'))  # Create a Calculation instance with a zero divisor.
    with pytest.raises(ValueError, match = "Cannot divide by zero"):  
        calc.perform()
