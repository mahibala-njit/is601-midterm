"""Test suite for the DisplayHistoryCommand.
"""

import logging
from unittest.mock import patch
from calculator.plugins.display_history import DisplayHistoryCommand

# Set up logging for the tests
logger = logging.getLogger(__name__)

def test_display_history_command_success(caplog):
    """Test that DisplayHistoryCommand executes successfully and logs the correct message."""
    command = DisplayHistoryCommand()

    # Mock the HistoryFacade to simulate successful execution
    mock_history = "Sample calculation history"
    with patch('calculator.history_facade.history_facade.HistoryFacade') as MockHistoryFacade:
        instance = MockHistoryFacade.return_value
        instance.display_history.return_value = mock_history  # Mock the return value

        with caplog.at_level(logging.INFO):
            command.execute()  # Execute the command

    # Assertions
    assert "Successfully retrieved history" in caplog.text  # Check the log message
