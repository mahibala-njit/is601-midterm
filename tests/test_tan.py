"""
Test suite for the TanCommand functionality in the calculator.
"""

from decimal import Decimal
import logging
import pytest
from calculator import Calculator
from calculator.plugins.tan import TanCommand  # First-party import

# Set up logging for the tests
logger = logging.getLogger(__name__)

class MockCalculator:
    """A mock of the Calculator class to simulate behavior for testing."""

    @staticmethod
    def tan(operand):
        """Mocked tangent function that returns fixed values for specific inputs."""
        if operand == Decimal('0'):
            return Decimal('0')
        if operand == Decimal('1'):
            return Decimal('1.5574077246549023')  # tan(1) ~ 1.5574
        raise ValueError("Invalid input for tangent calculation.")

def test_tan_command_success():
    """Test that TanCommand executes successfully for valid input."""
    command = TanCommand()
    
    # Mock the Calculator to control the output
    Calculator.tan = MockCalculator.tan
    result = command.execute(Decimal('0'))
    
    assert result == Decimal('0')
    
    result = command.execute(Decimal('1'))
    assert result == Decimal('1.5574077246549023')

def test_tan_command_invalid_input():
    """Test that TanCommand raises an error for invalid input."""
    command = TanCommand()
    
    # Mock the Calculator to raise an error
    Calculator.tan = MockCalculator.tan
    
    with pytest.raises(ValueError):
        command.execute(Decimal('2'))  # Assuming tan(2) is not defined in MockCalculator

def test_tan_command_log_output(caplog):
    """Test logging output for TanCommand."""
    command = TanCommand()
    
    # Mock the Calculator for valid input
    Calculator.tan = MockCalculator.tan
    
    with caplog.at_level(logging.INFO):
        command.execute(Decimal('0'))
        
    assert "Calculated tan(0) = 0" in caplog.text

def test_tan_command_log_error(caplog):
    """Test logging output for TanCommand when an error occurs."""
    command = TanCommand()
    
    # Mock the Calculator to raise an error
    Calculator.tan = MockCalculator.tan
    
    with caplog.at_level(logging.ERROR):
        with pytest.raises(ValueError):
            command.execute(Decimal('2'))  # This should raise an error
            
    assert "Error calculating tan(2): Invalid input for tangent calculation." in caplog.text
