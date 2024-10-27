from calculator import Calculator
from decimal import Decimal
import pytest

def test_addition():
    """Test that the addition function works."""
    assert Calculator.add(Decimal(2), Decimal(2)) == Decimal(4)

def test_subtraction():
    """Test that the subtraction function works."""
    assert Calculator.subtract(Decimal(2), Decimal(2)) == Decimal(0)

def test_divide():
    """Test that the division function works."""
    assert Calculator.divide(Decimal(2), Decimal(2)) == Decimal(1)

def test_multiply():
    """Test that the multiplication function works."""
    assert Calculator.multiply(Decimal(2), Decimal(2)) == Decimal(4)

def test_sin():
    """Test that the sine function works."""
    assert Calculator.sin(Decimal(0)).quantize(Decimal('0.01')) == Decimal(0)  # sin(0) = 0

def test_cos():
    """Test that the cosine function works."""
    assert Calculator.cos(Decimal(0)).quantize(Decimal('0.01')) == Decimal(1)  # cos(0) = 1

def test_tan():
    """Test that the tangent function works."""
    assert Calculator.tan(Decimal(0)).quantize(Decimal('0.01')) == Decimal(0)  # tan(0) = 0

def test_sqrt():
    """Test that the square root function works."""
    assert Calculator.sqrt(Decimal(4)) == Decimal(2)  # sqrt(4) = 2
    assert Calculator.sqrt(Decimal(0)) == Decimal(0)  # sqrt(0) = 0

# Edge case tests
def test_addition_negative_numbers():
    """Test addition with negative numbers."""
    assert Calculator.add(Decimal(-2), Decimal(-3)) == Decimal(-5)

def test_subtraction_negative_numbers():
    """Test subtraction with negative numbers."""
    assert Calculator.subtract(Decimal(-2), Decimal(-3)) == Decimal(1)

def test_divide_by_zero():
    """Test division by zero handling."""
    with pytest.raises(ValueError):
        Calculator.divide(Decimal(2), Decimal(0))

def test_multiply_with_zero():
    """Test multiplication with zero."""
    assert Calculator.multiply(Decimal(0), Decimal(5)) == Decimal(0)

def test_sqrt_negative_number():
    """Test square root of a negative number."""
    with pytest.raises(ValueError):
        Calculator.sqrt(Decimal(-4))

# Run tests if this file is executed directly
if __name__ == "__main__":
    pytest.main()
