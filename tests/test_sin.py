"""
Test suite for the SinCommand functionality in the calculator.
"""

from decimal import Decimal
import logging
import pytest
from calculator import Calculator
from calculator.plugins.sin import SinCommand  # First-party import

# Set up logging for the tests
logger = logging.getLogger(__name__)

class MockCalculator:
    """A mock of the Calculator class to simulate behavior for testing."""

    @staticmethod
    def sin(operand):
        """Mocked sine function that returns fixed values for specific inputs."""
        if operand == Decimal('0'):
            return Decimal('0')
        if operand == Decimal('1'):
            return Decimal('0.8414709848078965')  # sin(1) ~ 0.8415
        raise ValueError("Invalid input for sine calculation.")

def test_sin_command_success():
    """Test that SinCommand executes successfully for valid input."""
    command = SinCommand()
    
    # Mock the Calculator to control the output
    Calculator.sin = MockCalculator.sin
    result = command.execute(Decimal('0'))
    
    assert result == Decimal('0')
    
    result = command.execute(Decimal('1'))
    assert result == Decimal('0.8414709848078965')

def test_sin_command_invalid_input():
    """Test that SinCommand raises an error for invalid input."""
    command = SinCommand()
    
    # Mock the Calculator to raise an error
    Calculator.sin = MockCalculator.sin
    
    with pytest.raises(ValueError):
        command.execute(Decimal('2'))  # Assuming sin(2) is not defined in MockCalculator

def test_sin_command_log_output(caplog):
    """Test logging output for SinCommand."""
    command = SinCommand()
    
    # Mock the Calculator for valid input
    Calculator.sin = MockCalculator.sin
    
    with caplog.at_level(logging.INFO):
        command.execute(Decimal('0'))
        
    assert "Calculated sin(0) = 0" in caplog.text

def test_sin_command_log_error(caplog):
    """Test logging output for SinCommand when an error occurs."""
    command = SinCommand()
    
    # Mock the Calculator to raise an error
    Calculator.sin = MockCalculator.sin
    
    with caplog.at_level(logging.ERROR):
        with pytest.raises(ValueError):
            command.execute(Decimal('2'))  # This should raise an error
            
    assert "Error calculating sin(2): Invalid input for sine calculation." in caplog.text
