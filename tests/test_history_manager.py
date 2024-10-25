import os
import pytest
import pandas as pd
from calculator.history_facade.history_manager import HistoryManager

@pytest.fixture
def history_manager():
    manager = HistoryManager()
    manager.history_df = pd.DataFrame(columns=["operation", "a", "b", "result"])  # reset history for tests
    return manager

def test_add_to_history(history_manager):
    history_manager.add_to_history("add", 5, 3, 8)
    assert len(history_manager.history_df) == 1
    assert history_manager.history_df.iloc[0].to_dict() == {"operation": "add", "a": 5, "b": 3, "result": 8}

def test_display_history_empty(history_manager):
    result = history_manager.display_history()
    assert result == "No history available."

def test_display_history_with_entries(history_manager):
    history_manager.add_to_history("subtract", 10, 4, 6)
    result_df = history_manager.display_history()
    assert result_df.shape[0] == 1  # one row added
    assert result_df.iloc[0].to_dict() == {"operation": "subtract", "a": 10, "b": 4, "result": 6}

def test_save_history(history_manager, tmp_path):
    history_manager.add_to_history("multiply", 3, 7, 21)
    file_path = tmp_path / "history.csv"
    history_manager.save_history(file_path)
    saved_df = pd.read_csv(file_path)
    assert saved_df.shape[0] == 1
    assert saved_df.iloc[0].to_dict() == {"operation": "multiply", "a": 3, "b": 7, "result": 21}

def test_load_history(history_manager, tmp_path):
    file_path = tmp_path / "history.csv"
    data = pd.DataFrame([{"operation": "divide", "a": 20, "b": 5, "result": 4}])
    data.to_csv(file_path, index=False)
    history_manager.load_history(file_path)
    assert len(history_manager.history_df) == 1
    assert history_manager.history_df.iloc[0].to_dict() == {"operation": "divide", "a": 20, "b": 5, "result": 4}

def test_add_multiple_entries(history_manager):
    history_manager.add_to_history("add", 5, 3, 8)
    history_manager.add_to_history("subtract", 10.5, 4.3, 6.2)
    assert len(history_manager.history_df) == 2
    assert history_manager.history_df.iloc[1].to_dict() == {"operation": "subtract", "a": 10.5, "b": 4.3, "result": 6.2}

def test_save_history_invalid_path(history_manager):
    history_manager.add_to_history("multiply", 3, 7, 21)
    with pytest.raises(Exception):
        # Attempt to save in an invalid directory
        history_manager.save_history("/invalid_path/history.csv")


def test_load_empty_file(history_manager, tmp_path):
    # Create an empty CSV file
    file_path = tmp_path / "empty.csv"
    file_path.write_text("")

    # Expect ValueError for an empty file
    with pytest.raises(ValueError, match="Invalid CSV file format or empty file"):
        history_manager.load_history(file_path)

def test_display_history_with_entries(history_manager):
    history_manager.add_to_history("divide", 20, 5, 4)
    result_df = history_manager.display_history()
    assert not result_df.empty
    assert result_df.iloc[0].to_dict() == {"operation": "divide", "a": 20, "b": 5, "result": 4}
