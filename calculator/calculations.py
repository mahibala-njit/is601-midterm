import pandas as pd
import logging
from calculator.calculation import Calculation

logger = logging.getLogger(__name__)

class Calculations:
    """A class to manage both in-memory and persistent calculation history using a Pandas DataFrame."""

    # Initialize a DataFrame to store calculation history
    _history_df = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Adds a new calculation to the in-memory history and logs it."""
        # Perform the calculation to get the result
        result = calculation.perform()
        # Add the calculation to the DataFrame
        new_entry = {
            "operation": calculation.operation.__name__,
            "operand1": float(calculation.a),
            "operand2": float(calculation.b) if calculation.b is not None else None,
            "result": float(result)
        }
        # Create a DataFrame from the new entry
        new_entry_df = pd.DataFrame([new_entry])
        
        # Check if history_df is empty or not
        if cls._history_df.empty:
            cls._history_df = new_entry_df
        else:
            cls._history_df = pd.concat([cls._history_df, new_entry_df], ignore_index=True)

        #cls._history_df = pd.concat([cls._history_df, pd.DataFrame([new_entry])], ignore_index=True)
        logger.info("Added calculation to in-memory history: %s", new_entry)

    @classmethod
    def get_last_calculation(cls):
        """Retrieves the most recent calculation from the in-memory history."""
        if cls._history_df.empty:
            logger.warning("No calculations in history.")
            return None
        last_entry = cls._history_df.iloc[-1]
        logger.info("Retrieved last calculation: %s", last_entry.to_dict())
        return last_entry.to_dict()

    @classmethod
    def get_history(cls):
        """Retrieves the entire in-memory history as a DataFrame."""
        logger.debug("Retrieved complete in-memory history.")
        return cls._history_df

    @classmethod
    def clear_history(cls):
        """Clears the in-memory calculation history."""
        cls._history_df = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])
        logger.info("Cleared in-memory calculation history.")

    @classmethod
    def save_history(cls, file_path: str):
        """Saves the in-memory history to a CSV file."""
        cls._history_df.to_csv(file_path, index=False)
        logger.info("Saved calculation history to %s", file_path)

    @classmethod
    def load_history(cls, file_path: str):
        """Loads history from a CSV file into the in-memory DataFrame."""
        cls._history_df = pd.read_csv(file_path)
        logger.info("Loaded calculation history from %s", file_path)

    @classmethod
    def display_history(cls):
        """Displays the in-memory history."""
        if cls._history_df.empty:
            logger.info("No calculation history available to display.")
            # Instead of returning a string, return an empty DataFrame
            return pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])
        else:
            logger.info("Displaying calculation history.")
            return cls._history_df
