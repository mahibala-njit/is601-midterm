from calculator.calculation import Calculation
from calculator.calculations import Calculations
import logging
import os
from dotenv import load_dotenv
import pandas as pd

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
        try:
            Calculations.add_calculation(calculation)
            logger.info("Added calculation to history via facade: %s", calculation)
        except Exception as e:
            logger.error("Failed to add calculation: %s", e)
            raise

    def get_last_calculation(self):
        """Retrieves the latest calculation from in-memory history."""
        try:
            return Calculations.get_last_calculation()
        except Exception as e:
            logger.error("Failed to retrieve the last calculation: %s", e)
            raise

    def get_history(self):
        """Retrieves the entire in-memory history."""
        try:
            return Calculations.get_history()
        except Exception as e:
            logger.error("Failed to retrieve history: %s", e)
            raise

    def clear_history(self):
        """Clears both in-memory history."""
        try:
            Calculations.clear_history()
            logger.info("Cleared in-memory history via facade.")
        except Exception as e:
            logger.error("Failed to clear history: %s", e)
            raise

    def save_history(self):
        """Saves the in-memory history to a file using the path from .env."""
        file_path = os.getenv('HISTORY_FILE_PATH', 'history.csv')  # Default to history.csv if not set
        if not file_path or not isinstance(file_path, str):  # LBYL approach
            logger.warning("Invalid file path provided. Defaulting to 'history.csv'.")
            file_path = 'history.csv'
        
        try:
            Calculations.save_history(file_path)
            logger.info("Saved history to %s via facade", file_path)
        except FileNotFoundError:
            logger.error("The file path does not exist: %s", file_path)
            raise
        except Exception as e:
            logger.error("Failed to save history: %s", e)
            raise

    def load_history(self):
        """Loads calculation history from a file using the path from .env."""
        file_path = os.getenv('HISTORY_FILE_PATH', 'history.csv')  # Default to history.csv if not set
        if not file_path or not isinstance(file_path, str):  # LBYL approach
            logger.warning("Invalid file path provided. Defaulting to 'history.csv'.")
            file_path = 'history.csv'

        try:
            Calculations.load_history(file_path)
            logger.info("Loaded history from %s via facade", file_path)
        except FileNotFoundError:
            logger.error("The file path does not exist: %s", file_path)
            raise
        except Exception as e:
            logger.error("Failed to load history: %s", e)
            raise

    def display_history(self):
        """Displays the in-memory history."""
        try:
            return Calculations.display_history()
        except Exception as e:
            logger.error("Failed to display history: %s", e)
            raise
