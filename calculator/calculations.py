from typing import List, Optional
from calculator.calculation import Calculation
import logging

# Set up logging for this module
logger = logging.getLogger(__name__)

class Calculations:
    """A class to manage an in-memory history of mathematical calculations."""
    
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Adds a new calculation to the in-memory history."""
        cls.history.append(calculation)
        logger.info("Added calculation to in-memory history: %s", calculation)

    @classmethod
    def get_last_calculation(cls) -> Optional[Calculation]:
        """Retrieves the latest calculation from in-memory history. Returns None if there's no history."""
        if cls.history:
            last_calculation = cls.history[-1]
            logger.info("Retrieved last calculation: %s", last_calculation)
            return last_calculation
        logger.warning("No calculations in history to retrieve.")
        return None

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Retrieves the entire in-memory history of calculations."""
        logger.debug("Retrieving in-memory calculation history: %s", cls.history)
        return cls.history

    @classmethod
    def clear_history(cls): 
        """Clears the in-memory calculation history."""
        cls.history.clear()
        logger.info("Cleared in-memory calculation history.")
