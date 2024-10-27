"""Test suite for the LoadHistoryCommand.
"""

import logging
import pytest
import pandas as pd
from calculator.plugins.load_history import LoadHistoryCommand

# Set up logging for the tests
logger = logging.getLogger(__name__)

@pytest.fixture(autouse=True)
def setup_history_file(tmp_path):
    """
    Fixture to set up a temporary history CSV file for testing.

    This fixture creates a sample history DataFrame containing basic operation
    results and saves it as 'history.csv' in a temporary directory. It ensures
    that the necessary file exists before running tests that depend on it. 

    The fixture automatically yields the path to the temporary file, allowing 
    tests to access it. After the tests are complete, the temporary file is 
    automatically cleaned up.
    """
    # Create a sample DataFrame for history
    sample_data = {'operation': ['add', 'subtract'], 'result': [3, 2]}
    sample_df = pd.DataFrame(sample_data)

    # Save the DataFrame to a CSV file in the temporary path
    history_file = tmp_path / 'history.csv'
    sample_df.to_csv(history_file, index=False)

    # Set the environment variable if needed (optional)
    # os.environ['HISTORY_FILE_PATH'] = str(history_file)

    yield  # This will run before the test

def test_load_history_command_success(caplog):
    """Test that LoadHistoryCommand executes successfully and logs the correct message."""
    command = LoadHistoryCommand()
    
    with caplog.at_level(logging.INFO):
        command.execute()  # Execute the command

    # Assertions
    assert "History loaded successfully using the configured file path." in caplog.text
