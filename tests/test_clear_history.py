"""
Test suite for the ClearHistoryCommand.
"""

from calculator.plugins.clear_history import ClearHistoryCommand
from calculator.history_facade.history_facade import HistoryFacade
from unittest.mock import patch
import pytest
import logging

# Set up logging for the tests
logger = logging.getLogger(__name__)

class MockHistoryFacade:
    """A mock of the HistoryFacade to simulate behavior for testing."""
    
    def clear_history(self):
        """Mock the clear_history method for successful case."""
        pass  # Simulate successful clearing of history

def test_clear_history_command_success(caplog):
    """Test that ClearHistoryCommand executes successfully and logs the correct message."""
    command = ClearHistoryCommand()
    
    # Mock the HistoryFacade to simulate successful execution
    with patch('calculator.plugins.clear_history.HistoryFacade', new=MockHistoryFacade):
        with caplog.at_level(logging.INFO):
            command.execute()
        
    assert "Calculation history cleared successfully." in caplog.text
