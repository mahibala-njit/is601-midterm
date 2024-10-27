from calculator.commands import Command  # Import Command base class
from calculator.history_facade.history_facade import HistoryFacade  # Use the strict facade
import logging

logger = logging.getLogger(__name__)

class DisplayHistoryCommand(Command):
    def __init__(self):
        self.history_facade = HistoryFacade()  # Create an instance of HistoryFacade
        logger.info("Initialized DisplayHistoryCommand.")

    def execute(self):
        # Use the facade instance to access the display history function
        history = self.history_facade.display_history()  # Call the instance method
        print("Calculation History:")
        print(history)
        return history
