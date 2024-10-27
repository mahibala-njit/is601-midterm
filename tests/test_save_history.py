"""
Test suite for the SaveHistoryCommand.
"""

from calculator.plugins.save_history import SaveHistoryCommand
from calculator.history_facade.history_facade import HistoryFacade
from unittest.mock import patch
import pytest
import logging

# Set up logging for the tests
logger = logging.getLogger(__name__)

class MockHistoryFacade:
    """A mock of the HistoryFacade to simulate behavior for testing."""
    
    def save_history(self):
        """Mock the save_history method for successful case."""
        pass  # Simulate successful saving of history

class MockHistoryFacadeWithError:
    """A mock of the HistoryFacade to simulate an error during saving history."""
    
    def save_history(self):
        """Raise an exception to simulate an error."""
        raise Exception("Failed to save history.")

def test_save_history_command_success(caplog):
    """Test that SaveHistoryCommand executes successfully and logs the correct message."""
    command = SaveHistoryCommand()
    
    # Mock the HistoryFacade to simulate successful execution
    with patch('calculator.plugins.save_history.HistoryFacade', new=MockHistoryFacade):
        with caplog.at_level(logging.INFO):
            command.execute()  # Execute the command
    
    # Assertions
    assert "History saved successfully using the configured file path." in caplog.text
