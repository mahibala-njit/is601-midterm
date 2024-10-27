from calculator.commands import Command  # Import Command base class
from calculator.history_facade.history_facade import HistoryFacade  # Use the strict facade
import logging

logger = logging.getLogger(__name__)

class LoadHistoryCommand(Command):
    def __init__(self):
        self.history_facade = HistoryFacade()  # Create an instance of HistoryFacade
        logger.info("Initialized LoadHistoryCommand.")

    def execute(self):
        """Executes the command to load calculation history."""
        try:
            # Use the facade instance to load history without needing a file path
            self.history_facade.load_history()  # Call the instance method
            logger.info("History loaded successfully using the configured file path.")
            print("History loaded successfully using the configured file path.")
        except Exception as e:
            logger.error("Failed to load history: %s", e)
            print("Error: Could not load history. Please check the logs for details.")
            raise  # Optionally re-raise the exception for further handling
