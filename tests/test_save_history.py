"""Test suite for the SaveHistoryCommand.
"""

import logging
from calculator.plugins.save_history import SaveHistoryCommand

# Set up logging for the tests
logger = logging.getLogger(__name__)

def test_save_history_command_success(caplog):
    """Test that SaveHistoryCommand executes successfully and logs the correct message."""
    command = SaveHistoryCommand()

    with caplog.at_level(logging.INFO):
        command.execute()  # Execute the command

    # Assertions
    assert "History saved successfully using the configured file path." in caplog.text
