from decimal import Decimal
from calculator.plugins.sqrt import SqrtCommand
import pytest
import logging
from calculator import Calculator

# Set up logging for the tests
logger = logging.getLogger(__name__)

class MockCalculator:
    """A mock of the Calculator class to simulate behavior for testing."""

    @staticmethod
    def sqrt(operand):
        if operand == Decimal('0'):
            return Decimal('0')
        elif operand == Decimal('4'):
            return Decimal('2')
        elif operand == Decimal('9'):
            return Decimal('3')
        raise ValueError("Invalid input for square root calculation.")

def test_sqrt_command_success():
    """Test that SqrtCommand executes successfully for valid input."""
    command = SqrtCommand()
    
    # Mock the Calculator to control the output
    Calculator.sqrt = MockCalculator.sqrt
    
    result = command.execute(Decimal('0'))
    assert result == Decimal('0')
    
    result = command.execute(Decimal('4'))
    assert result == Decimal('2')
    
    result = command.execute(Decimal('9'))
    assert result == Decimal('3')

def test_sqrt_command_invalid_input():
    """Test that SqrtCommand raises an error for invalid input (negative number)."""
    command = SqrtCommand()
    
    with pytest.raises(ValueError):
        command.execute(Decimal('-1'))  # Square root of negative number should raise an error

def test_sqrt_command_log_output(caplog):
    """Test logging output for SqrtCommand."""
    command = SqrtCommand()
    
    # Mock the Calculator for valid input
    Calculator.sqrt = MockCalculator.sqrt
    
    with caplog.at_level(logging.INFO):
        command.execute(Decimal('4'))
        
    assert "Calculated sqrt(4) = 2" in caplog.text

def test_sqrt_command_log_error(caplog):
    """Test logging output for SqrtCommand when an error occurs."""
    command = SqrtCommand()
    
    with caplog.at_level(logging.ERROR):
        with pytest.raises(ValueError):
            command.execute(Decimal('-1'))  # This should raise an error
            
    assert "Error calculating sqrt(-1): Square root of a negative number is not defined for real numbers." in caplog.text
