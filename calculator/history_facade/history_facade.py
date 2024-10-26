from calculator.calculation import Calculation
from calculator.calculations import Calculations
import logging

logger = logging.getLogger(__name__)

class HistoryFacade:
    """A facade to manage calculation history, simplifying interaction with the Calculations class."""

    _instance = None  # Singleton instance of HistoryFacade

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(HistoryFacade, cls).__new__(cls)
            logger.info("Initialized singleton HistoryFacade instance.")
        return cls._instance

    def add_calculation(self, calculation: Calculation):
        """Adds a calculation to both in-memory and persistent history."""
        Calculations.add_calculation(calculation)
        logger.info("Added calculation to history via facade: %s", calculation)

    def get_last_calculation(self):
        """Retrieves the latest calculation from in-memory history."""
        return Calculations.get_last_calculation()

    def get_history(self):
        """Retrieves the entire in-memory history."""
        return Calculations.get_history()

    def clear_history(self):
        """Clears both in-memory history."""
        Calculations.clear_history()
        logger.info("Cleared in-memory history via facade.")

    def save_history(self, file_path: str):
        """Saves the in-memory history to a file."""
        Calculations.save_history(file_path)
        logger.info("Saved history to %s via facade", file_path)

    def load_history(self, file_path: str):
        """Loads calculation history from a file."""
        Calculations.load_history(file_path)
        logger.info("Loaded history from %s via facade", file_path)

    def display_history(self):
        """Displays the in-memory history."""
        return Calculations.display_history()
