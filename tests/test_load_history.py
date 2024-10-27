"""
Test suite for the LoadHistoryCommand.
"""

from calculator.plugins.load_history import LoadHistoryCommand
from calculator.history_facade.history_facade import HistoryFacade
from unittest.mock import patch
import pytest
import logging

# Set up logging for the tests
logger = logging.getLogger(__name__)

class MockHistoryFacade:
    """A mock of the HistoryFacade to simulate behavior for testing."""
    
    def load_history(self):
        """Mock the load_history method for successful case."""
        pass  # Simulate successful loading of history

def test_load_history_command_success(caplog):
    """Test that LoadHistoryCommand executes successfully and logs the correct message."""
    command = LoadHistoryCommand()
    
    # Mock the HistoryFacade to simulate successful execution
    with patch('calculator.plugins.load_history.HistoryFacade', new=MockHistoryFacade):
        with caplog.at_level(logging.INFO):
            command.execute()  # Execute the command
    
    # Assertions
    assert "History loaded successfully using the configured file path." in caplog.text

