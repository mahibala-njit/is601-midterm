from calculator.commands import Command
from calculator.history_facade.history_manager import HistoryManager
import logging

logger = logging.getLogger(__name__)

class DisplayHistoryCommand(Command):
    def __init__(self):
        self.history_manager = HistoryManager()
        logger.info("Initialized DisplayHistoryCommand.")

    def execute(self):
        history = self.history_manager.display_history()
        print("Calculation History:")
        print(history)
        return history
