"""Test suite for the ClearHistoryCommand.
"""

import logging
from calculator.plugins.clear_history import ClearHistoryCommand

# Set up logging for the tests
logger = logging.getLogger(__name__)

def test_clear_history_command_success(caplog):
    """Test that ClearHistoryCommand executes successfully and logs the correct message."""
    command = ClearHistoryCommand()

    with caplog.at_level(logging.INFO):
        command.execute()  # Execute the command
        
    assert "Calculation history cleared successfully." in caplog.text
