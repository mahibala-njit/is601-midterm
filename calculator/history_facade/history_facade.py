from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.history_facade.history_manager import HistoryManager
import logging

logger = logging.getLogger(__name__)

class HistoryFacade:
    """A strict facade to manage both in-memory and persistent calculation histories."""
    
    _instance = None  # Class variable to hold the singleton instance

    def __new__(cls):
        if cls._instance is None:  # Check if instance already exists
            cls._instance = super(HistoryFacade, cls).__new__(cls)
            cls._instance.calculations = Calculations()  # Create instance of Calculations
            cls._instance.history_manager = HistoryManager()  # Create instance of HistoryManager
            logger.info("Initialized singleton HistoryFacade instance.")
        return cls._instance
    
    def add_calculation(self, calculation: Calculation):
        """Adds a calculation to both in-memory and persistent history."""
        # Add to in-memory history
        self.calculations.add_calculation(calculation)
        logger.info("Added calculation to in-memory history via facade: %s", calculation)
    
        # Add to persistent history using HistoryManager
        self.history_manager.add_to_history(
            operation=calculation.operation.__name__,
            a=float(calculation.a),
            b=float(calculation.b) if calculation.b is not None else None,
            result=float(calculation.perform())
        )
        logger.info("Added calculation to persistent history via HistoryManager: %s", calculation)


    def get_last_calculation(self):
        """Retrieves the latest calculation from in-memory history."""
        return self.calculations.get_last_calculation()

    def get_history(self):
        """Retrieves the entire in-memory history."""
        return self.calculations.get_history()

    def clear_history(self):
        """Clears both in-memory and persistent history."""
        self.calculations.clear_history()  # Clears in-memory history
        self.history_manager.clear_history()  # Clears persistent history
        logger.info("Cleared both in-memory and persistent history.")

    def save_history(self, file_path: str):
        """Saves the persistent history to a file."""
        self.history_manager.save_history(file_path)
        logger.info("Saved persistent history to %s", file_path)

    def load_history(self, file_path: str):
        """Loads calculation history from a file."""
        self.history_manager.load_history(file_path)
        logger.info("Loaded history from %s", file_path)

    def display_history(self):
        """Displays the persistent history."""
        return self.history_manager.display_history()
