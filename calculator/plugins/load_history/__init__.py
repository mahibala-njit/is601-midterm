from calculator.commands import Command  # Import Command base class
from calculator.history_facade.history_facade import HistoryFacade  # Use the strict facade
import logging

logger = logging.getLogger(__name__)

class LoadHistoryCommand(Command):
    def __init__(self):
        self.history_facade = HistoryFacade()  # Create an instance of HistoryFacade
        logger.info("Initialized LoadHistoryCommand.")

    def execute(self):
        # Use the facade instance to load history without needing a file path
        self.history_facade.load_history()  # Call the instance method
        logger.info("History loaded using the configured file path.")
        print("History loaded using the configured file path.")
