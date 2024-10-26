from calculator.commands import Command  # Import Command base class
from calculator.history_facade.history_facade import HistoryFacade  # Use the strict facade
import logging

logger = logging.getLogger(__name__)

class SaveHistoryCommand(Command):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.history_facade = HistoryFacade()  # Create an instance of HistoryFacade
        logger.info("Initialized SaveHistoryCommand with file path: %s", file_path)

    def execute(self):
        # Use the facade instance to save history
        self.history_facade.save_history(self.file_path)
        print(f"History saved to {self.file_path}")
