"""Unit tests for the HistoryFacade class.

This module contains tests for the HistoryFacade, ensuring that 
it correctly manages calculation history, including adding, 
saving, loading, and clearing history. It also tests for error 
handling and singleton behavior.
"""

import os
from unittest.mock import patch

import pandas as pd
import pytest

from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.history_facade.history_facade import HistoryFacade
from calculator.operations import add, subtract, divide  # Only importing what is used


@pytest.fixture
def set_env(monkeypatch):
    """Fixture to set the environment variable for the history file path."""
    monkeypatch.setenv("HISTORY_FILE_PATH", "test_history.csv")  # Path for the test


@pytest.fixture
def history_facade(set_env):
    """Fixture to initialize the HistoryFacade instance."""
    return HistoryFacade()


def test_add_and_get_last_calculation(history_facade):
    """
    Test that a calculation is added to the history and can be retrieved as the last calculation.
    """
    calculation = Calculation(add, 3, 4)  # Pass the actual callable, not the string

    # Add the calculation to the history
    history_facade.add_calculation(calculation)

    # Retrieve the last calculation and verify it
    last_calc = history_facade.get_last_calculation()

    # Check if last_calc is a dictionary
    if isinstance(last_calc, dict):
        assert last_calc["operation"] == "add"  # Check against the string "add"
        assert last_calc["operand1"] == 3
        assert last_calc["operand2"] == 4
        assert last_calc["result"] == 7
    else:
        assert last_calc.operation == add  # This should be the function
        assert last_calc.a == 3
        assert last_calc.b == 4
        assert last_calc.perform() == 7


def test_save_and_load_history(history_facade):
    """Test saving and loading history."""
    history_facade.clear_history()
    calc1 = Calculation(operation=add, a=3, b=4)  # Ensure 'add' is a callable function
    calc2 = Calculation(operation=subtract, a=10, b=5)  # Ensure 'subtract' is a callable function

    # Add calculations
    history_facade.add_calculation(calc1)
    history_facade.add_calculation(calc2)

    # Save history
    history_facade.save_history()

    # Clear history and load it back
    history_facade.clear_history()
    history_facade.load_history()

    # Verify loaded history contains the calculations
    loaded_history = history_facade.get_history()
    assert len(loaded_history) == 2
    assert loaded_history.iloc[0]['operation'] == 'add'
    assert loaded_history.iloc[1]['operation'] == 'subtract'


def test_clear_history(history_facade):
    """
    Test clearing the calculation history.
    """
    calculation = Calculation(add, 1, 2)  # Use the callable add function
    history_facade.add_calculation(calculation)

    # Clear the history
    history_facade.clear_history()

    # Verify that display_history returns an empty DataFrame
    history_display = history_facade.display_history()  # Call the display method
    assert isinstance(history_display, pd.DataFrame)  # Ensure it's a DataFrame
    assert history_display.empty  # Check if it's empty


def test_display_history(history_facade):
    """Test displaying history."""
    calc = Calculation(operation=divide, a=10, b=2)  # Ensure 'divide' is a callable function
    history_facade.add_calculation(calc)

    # Capture the display output
    displayed_history = history_facade.display_history()
    assert isinstance(displayed_history, pd.DataFrame)
    assert not displayed_history.empty  # Ensure there is something displayed


def test_load_history_file_not_found(history_facade):
    """Test loading history with a non-existent file."""
    # Set an invalid path for testing
    with patch.dict(os.environ, {"HISTORY_FILE_PATH": "invalid_path.csv"}):
        with pytest.raises(FileNotFoundError) as e:
            history_facade.load_history()
        assert "No such file or directory" in str(e.value)


def test_save_history_file_permission_denied(history_facade):
    """Test saving history with permission denied."""
    # Simulate permission error on save
    with patch('pandas.DataFrame.to_csv') as mock_to_csv:
        mock_to_csv.side_effect = PermissionError("Permission denied.")
        with pytest.raises(PermissionError, match="Permission denied."):
            history_facade.save_history()


def test_invalid_file_path_on_save(history_facade):
    """Test saving history with an invalid file path."""
    with patch('pandas.DataFrame.to_csv') as mock_to_csv:
        mock_to_csv.side_effect = FileNotFoundError("The file path does not exist.")
        with pytest.raises(FileNotFoundError):
            history_facade.save_history()


def test_clear_history_on_empty(history_facade):
    """Test clearing history when it is already empty."""
    # Clear history (should not raise any errors)
    history_facade.clear_history()

    # Verify display returns an empty DataFrame
    history_display = history_facade.display_history()
    assert isinstance(history_display, pd.DataFrame)
    assert history_display.empty  # Check if it's empty


def test_singleton_instance(history_facade):
    """Test that multiple calls return the same HistoryFacade instance."""
    instance1 = HistoryFacade()
    instance2 = HistoryFacade()
    assert instance1 is instance2  # Ensure they point to the same instance


def test_save_history_empty(history_facade):
    """Test saving empty history."""
    # Clear any existing history first
    history_facade.clear_history()

    # Save the empty history (should not raise any errors)
    history_facade.save_history()

    # Load the history back
    history_facade.load_history()

    # Ensure history is still empty
    loaded_history = history_facade.get_history()
    assert len(loaded_history) == 0


def test_clear_history_error_handling(history_facade):
    """Test handling error while clearing history."""
    with patch.object(Calculations, 'clear_history', side_effect=Exception("Clear history error")):
        with pytest.raises(Exception, match="Clear history error"):
            history_facade.clear_history()


def test_save_history_error_handling(history_facade):
    """Test handling error while saving history."""
    with patch('pandas.DataFrame.to_csv') as mock_to_csv:
        mock_to_csv.side_effect = Exception("Failed to save history.")
        with pytest.raises(Exception, match="Failed to save history."):
            history_facade.save_history()


def test_load_history_error_handling(history_facade):
    """Test handling error while loading history."""
    with patch('pandas.read_csv') as mock_read_csv:
        mock_read_csv.side_effect = Exception("Failed to load history.")
        with pytest.raises(Exception, match="Failed to load history."):
            history_facade.load_history()


def test_display_history_error_handling(history_facade):
    """Test handling error while displaying history."""
    with patch.object(Calculations, 'display_history', side_effect=Exception("Display history error")):
        with pytest.raises(Exception, match="Display history error"):
            history_facade.display_history()
