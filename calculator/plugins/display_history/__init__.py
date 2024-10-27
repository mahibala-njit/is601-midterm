from calculator.commands import Command  # Import Command base class
from calculator.history_facade.history_facade import HistoryFacade  # Use the strict facade
import logging

logger = logging.getLogger(__name__)

class DisplayHistoryCommand(Command):
    def __init__(self):
        self.history_facade = HistoryFacade()  # Create an instance of HistoryFacade
        logger.info("Initialized DisplayHistoryCommand.")

    def execute(self):
        """Executes the command to display calculation history."""
        try:
            # Use the facade instance to access the display history function
            history = self.history_facade.display_history()  # Call the instance method
            
            logger.info("Successfully retrieved history: \n%s", history)  # Log the history
            
            print("Calculation History:")
            print(history)  # Print the history
            return history
        except Exception as e:
            logger.error("Failed to retrieve calculation history: %s", e)
            print("Error: Could not display calculation history. Please check the logs for details.")
            raise  # Optionally re-raise the exception for further handling
