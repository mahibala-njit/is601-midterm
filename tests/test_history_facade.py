# test_history_facade.py

import pytest
import os
from calculator.calculation import Calculation
from calculator.history_facade.history_facade import HistoryFacade
import pandas as pd
from unittest.mock import patch


@pytest.fixture
def set_env(monkeypatch):
    """Fixture to set the environment variable for the history file path."""
    monkeypatch.setenv("HISTORY_FILE_PATH", "test_history.csv")  # Path for the test

@pytest.fixture
def history_facade(set_env):
    """Fixture to initialize the HistoryFacade instance."""
    return HistoryFacade()

def test_add_and_get_last_calculation(history_facade):
    """Test adding and retrieving the last calculation."""
    calc = Calculation(operation='add', a=1, b=2)  # Avoid using 'calculation' to prevent confusion
    history_facade.add_calculation(calc)

    # Retrieve the last calculation and assert its properties
    last_calc = history_facade.get_last_calculation()
    assert last_calc.operation == 'add'
    assert last_calc.a == 1
    assert last_calc.b == 2

def test_save_and_load_history(history_facade):
    """Test saving and loading history."""
    calc1 = Calculation(operation='add', a=3, b=4)
    calc2 = Calculation(operation='subtract', a=10, b=5)
    
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
    """Test clearing history."""
    calc = Calculation(operation='multiply', a=2, b=3)
    history_facade.add_calculation(calc)

    # Ensure history is not empty before clearing
    assert len(history_facade.get_history()) == 1

    # Clear history
    history_facade.clear_history()

    # Verify history is empty
    assert len(history_facade.get_history()) == 0

def test_display_history(history_facade):
    """Test displaying history."""
    calc = Calculation(operation='divide', a=10, b=2)
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
        assert str(e.value) == "The history file was not found."

def test_save_history_file_permission_denied(history_facade):
    """Test saving history with permission denied."""
    # Simulate permission error on save
    with patch('pandas.DataFrame.to_csv') as mock_to_csv:
        mock_to_csv.side_effect = PermissionError("Permission denied.")
        with pytest.raises(PermissionError, match="Permission denied."):
            history_facade.save_history()

# Run tests if this file is executed directly
if __name__ == "__main__":
    pytest.main()
