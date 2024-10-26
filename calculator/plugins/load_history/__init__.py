from calculator.commands import Command  # Import Command base class
from calculator.history_facade.history_facade import HistoryFacade  # Use the strict facade
import logging

logger = logging.getLogger(__name__)

class LoadHistoryCommand(Command):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.history_facade = HistoryFacade()  # Create an instance of HistoryFacade
        logger.info("Initialized LoadHistoryCommand with file path: %s", file_path)

    def execute(self):
        # Use the facade instance to load history
        self.history_facade.load_history(self.file_path)  # Call the instance method
        print(f"History loaded from {self.file_path}")
