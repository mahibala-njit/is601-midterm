"""Test suite for the LoadHistoryCommand.
"""

import logging
from calculator.plugins.load_history import LoadHistoryCommand

# Set up logging for the tests
logger = logging.getLogger(__name__)

def test_load_history_command_success(caplog):
    """Test that LoadHistoryCommand executes successfully and logs the correct message."""
    command = LoadHistoryCommand()

    with caplog.at_level(logging.INFO):
        command.execute()  # Execute the command

    # Assertions
    assert "History loaded successfully using the configured file path." in caplog.text
