"""
This module contains unit tests for the calculator operations.

It includes tests for various arithmetic operations using the Calculation class,
as well as specific tests for edge cases such as division by zero.

Tests:
- Various arithmetic operations (addition, subtraction, multiplication, division).
- Handling of division by zero scenarios.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import divide


def test_operation( operation, expected, a, b):
    '''Testing various operations'''
    calculation = Calculation.create( a, b, operation)
    assert calculation.perform() == expected, f"{operation} operation failed"

# Keeping the divide by zero test as is since it tests a specific case
def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(divide,Decimal('10'), Decimal('0') )
        calculation.perform()
