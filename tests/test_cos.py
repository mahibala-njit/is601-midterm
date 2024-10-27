"""
Test suite for the CosCommand functionality in the calculator.
"""

from decimal import Decimal
import logging
import pytest
from calculator import Calculator
from calculator.plugins.cos import CosCommand  # First-party import

# Set up logging for the tests
logger = logging.getLogger(__name__)

class MockCalculator:
    """A mock of the Calculator class to simulate behavior for testing."""

    @staticmethod
    def cos(operand):
        """Mocked cosine function that returns fixed values for specific inputs."""
        if operand == Decimal('0'):
            return Decimal('1')
        if operand == Decimal('1'):
            return Decimal('0.5403023058681398')  # cos(1) ~ 0.5403
        raise ValueError("Invalid input for cosine calculation.")

def test_cos_command_success():
    """Test that CosCommand executes successfully for valid input."""
    command = CosCommand()
    
    # Mock the Calculator to control the output
    Calculator.cos = MockCalculator.cos
    result = command.execute(Decimal('0'))
    
    assert result == Decimal('1')
    
    result = command.execute(Decimal('1'))
    assert result == Decimal('0.5403023058681398')

def test_cos_command_invalid_input():
    """Test that CosCommand raises an error for invalid input."""
    command = CosCommand()
    
    # Mock the Calculator to raise an error
    Calculator.cos = MockCalculator.cos
    
    with pytest.raises(ValueError):
        command.execute(Decimal('2'))  # Assuming cos(2) is not defined in MockCalculator

def test_cos_command_log_output(caplog):
    """Test logging output for CosCommand."""
    command = CosCommand()
    
    # Mock the Calculator for valid input
    Calculator.cos = MockCalculator.cos
    
    with caplog.at_level(logging.INFO):
        command.execute(Decimal('0'))
        
    assert "Calculated cos(0) = 1" in caplog.text

def test_cos_command_log_error(caplog):
    """Test logging output for CosCommand when an error occurs."""
    command = CosCommand()
    
    # Mock the Calculator to raise an error
    Calculator.cos = MockCalculator.cos
    
    with caplog.at_level(logging.ERROR):
        with pytest.raises(ValueError):
            command.execute(Decimal('2'))  # This should raise an error
            
    assert "Error calculating cos(2): Invalid input for cosine calculation." in caplog.text
