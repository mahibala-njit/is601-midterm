from calculator.commands import Command  # Import Command base class
from calculator.history_facade.history_facade import HistoryFacade  # Use the strict facade
import logging

logger = logging.getLogger(__name__)

class SaveHistoryCommand(Command):
    def __init__(self):
        self.history_facade = HistoryFacade()  # Create an instance of HistoryFacade
        logger.info("Initialized SaveHistoryCommand.")

    def execute(self):
        # Use the facade instance to save history without needing a file path
        self.history_facade.save_history()
        logger.info("History saved using the configured file path.")
        print("History saved using the configured file path.")