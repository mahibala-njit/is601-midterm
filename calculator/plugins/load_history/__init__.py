from calculator.commands import Command
from calculator.history_facade.history_manager import HistoryManager
import logging

logger = logging.getLogger(__name__)

class LoadHistoryCommand(Command):
    def __init__(self, file_path: str):
        self.history_manager = HistoryManager()
        self.file_path = file_path
        logger.info("Initialized LoadHistoryCommand with file path: %s", file_path)

    def execute(self):
        self.history_manager.load_history(self.file_path)
        print(f"History loaded from {self.file_path}")
