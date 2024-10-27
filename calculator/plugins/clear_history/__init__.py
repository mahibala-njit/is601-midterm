from calculator.commands import Command  # Import Command base class
from calculator.history_facade.history_facade import HistoryFacade  # Use the strict facade
import logging

logger = logging.getLogger(__name__)

class ClearHistoryCommand(Command):
    def __init__(self):
        self.history_facade = HistoryFacade()  # Create an instance of HistoryFacade
        logger.info("Initialized ClearHistoryCommand.")

    def execute(self):
        """Executes the command to clear calculation history."""
        try:
            # Use the facade instance to clear history
            self.history_facade.clear_history()  # Call the instance method
            logger.info("Calculation history cleared successfully.")
            print("Calculation history cleared successfully.")
        except Exception as e:
            logger.error("Failed to clear calculation history: %s", e)
            print("Error: Could not clear calculation history. Please check the logs for details.")
            raise  # Optionally re-raise the exception for further handling
