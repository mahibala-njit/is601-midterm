# test_history_facade.py

import pytest
import os
from calculator.calculation import Calculation
from calculator.history_facade.history_facade import HistoryFacade
from calculator.calculations import Calculations

def add(x, y): return x + y  # Named function for consistent operation naming

@pytest.fixture(scope="function")
def history_facade():
    """Fixture to initialize HistoryFacade and clear history before each test."""
    facade = HistoryFacade()
    Calculations.clear_history()  # Clears in-memory history to ensure test isolation
    return facade

def test_add_and_get_last_calculation(history_facade):
    calculation = Calculation(add, 3, 4)
    history_facade.add_calculation(calculation)
    last_calculation = history_facade.get_last_calculation()
    assert last_calculation["operation"] == "add"  # Adjusted to match named function
    assert last_calculation["a"] == 3.0
    assert last_calculation["b"] == 4.0
    assert last_calculation["result"] == 7.0

# Repeat similar changes for other tests with consistent operation names
