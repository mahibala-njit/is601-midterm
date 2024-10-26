# test_calculations.py

import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations

# Helper function to add two numbers (for testing the add operation)
def add(x: float, y: float) -> float:
    """Function to perform addition."""
    return x + y

def test_add_calculation() -> None:
    """
    Test that a calculation is added to the in-memory history.
    Verifies that the calculation is correctly stored in the Calculations history.
    """
    # Create a calculation object using the add function
    calculation = Calculation(add, 1, 2)
    
    # Add the calculation to the history
    Calculations.add_calculation(calculation)
    
    # Retrieve the entire history DataFrame
    history = Calculations.get_history()
    
    # Assert that the history is not empty after adding a calculation
    assert not history.empty, "History should not be empty after adding a calculation"
    
    # Convert the first row to a dictionary and verify it matches the expected values
    expected = {"operation": "add", "a": 1.0, "b": 2.0, "result": 3.0}
    assert history.iloc[0].to_dict() == expected, f"Expected {expected}, but got {history.iloc[0].to_dict()}"

def test_get_history() -> None:
    """
    Test that the get_history method retrieves the correct calculation history.
    Ensures that the last added calculation matches the expected operation and values.
    """
    # Clear any existing history to ensure a clean slate
    Calculations.clear_history()
    
    # Add a calculation to history for testing retrieval
    calculation = Calculation(add, 1, 2)
    Calculations.add_calculation(calculation)
    
    # Retrieve the entire history
    history = Calculations.get_history()
    
    # Assert that the history is not empty
    assert not history.empty, "History should not be empty after adding a calculation"
    
    # Verify that the operation in the first record is 'add'
    assert history.iloc[0]["operation"] == "add", "Expected operation 'add' in history"

def test_clear_history() -> None:
    """
    Test that the clear_history method empties the in-memory history.
    Verifies that the history DataFrame is empty after clearing.
    """
    # Add a calculation to ensure history is not empty initially
    calculation = Calculation(add, 1, 2)
    Calculations.add_calculation(calculation)
    
    # Clear the history
    Calculations.clear_history()
    
    # Assert that the history is now empty
    assert Calculations.get_history().empty, "History should be empty after clearing"
