from typing import List
from calculator.calculation import Calculation
from calculator.history_facade.history_manager import HistoryManager  # Import HistoryManager
import logging
import pandas as pd

# Set up logging for this module
logger = logging.getLogger(__name__)

class Calculations:
    """A class to manage a history of mathematical calculations."""
    
    history: List[Calculation] = []
    history_manager = HistoryManager()  # Create an instance of HistoryManager

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history."""
        cls.history.append(calculation)
        # Add the calculation to the HistoryManager
        cls.history_manager.add_to_history(
            operation=calculation.operation.__name__,
            a=calculation.a,
            b=calculation.b,
            result=calculation.perform()  # Ensure perform() is called
        )
        logger.info("Added calculation to history: %s", calculation)

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        """Get the latest calculation. Returns None if there's no history."""
        if cls.history:
            last_calculation = cls.history[-1]
            logger.info("Retrieved last calculation: %s", last_calculation)
            return last_calculation
        logger.warning("No calculations in history to retrieve.")
        return None

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Gets the entire history of calculations."""
        logger.debug("Retrieving calculation history: %s", cls.history)
        return cls.history

    @classmethod
    def clear_history(cls): 
        """Clears the calculation history."""
        cls.history.clear()
        cls.history_manager.history_df = pd.DataFrame(columns=["operation", "a", "b", "result"])  # Reset the DataFrame
        logger.info("Cleared calculation history.")
