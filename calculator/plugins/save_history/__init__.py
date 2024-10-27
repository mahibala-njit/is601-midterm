from calculator.commands import Command  # Import Command base class
from calculator.history_facade.history_facade import HistoryFacade  # Use the strict facade
import logging

logger = logging.getLogger(__name__)

class SaveHistoryCommand(Command):
    def __init__(self):
        self.history_facade = HistoryFacade()  # Create an instance of HistoryFacade
        logger.info("Initialized SaveHistoryCommand.")

    def execute(self):
        """Executes the command to save calculation history."""
        try:
            # Use the facade instance to save history without needing a file path
            self.history_facade.save_history()  # Call the instance method
            logger.info("History saved successfully using the configured file path.")
            print("History saved successfully using the configured file path.")
        except Exception as e:
            logger.error("Failed to save history: %s", e)
            print("Error: Could not save history. Please check the logs for details.")
            raise  # Optionally re-raise the exception for further handling
