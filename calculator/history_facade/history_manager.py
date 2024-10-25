import pandas as pd
import logging

logger = logging.getLogger(__name__)

class HistoryManager:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(HistoryManager, cls).__new__(cls)
            cls._instance.history_df = pd.DataFrame(columns=["operation", "a", "b", "result"])
            logger.info("Initialized HistoryManager with empty DataFrame.")
        return cls._instance

    def add_to_history(self, operation: str, a, b, result):
        new_entry = pd.DataFrame([{"operation": operation, "a": a, "b": b, "result": result}])
        self.history_df = pd.concat([self.history_df, new_entry], ignore_index=True)
        logger.info("Added to history: %s", new_entry)

    def save_history(self, file_path: str):
        self.history_df.to_csv(file_path, index=False)
        logger.info("Saved calculation history to %s", file_path)

    def load_history(self, file_path: str):
        self.history_df = pd.read_csv(file_path)
        logger.info("Loaded calculation history from %s", file_path)

    def display_history(self):
        if self.history_df.empty:
            logger.info("No calculation history available to display.")
            return "No history available."
        else:
            logger.info("Displaying calculation history.")
            return self.history_df
