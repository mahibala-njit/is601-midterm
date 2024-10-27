from calculator.commands import Command  # Import Command base class
from calculator.history_facade.history_facade import HistoryFacade  # Use the strict facade
import logging

logger = logging.getLogger(__name__)

class ClearHistoryCommand(Command):
    def __init__(self):
        self.history_facade = HistoryFacade()  # Create an instance of HistoryFacade
        logger.info("Initialized ClearHistoryCommand.")

    def execute(self):
        # Use the facade instance to clear history
        self.history_facade.clear_history()  # Call the instance method
        print("Calculation history cleared.")
