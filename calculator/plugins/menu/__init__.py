import logging
from calculator.commands import Command

# Set up logging for this module
logger = logging.getLogger(__name__)

class MenuCommand(Command):
    def execute(self):
        # Define the message for available commands
        message = "Available commands: add, subtract, multiply, divide, display_history, load_history, save_history, menu, exit"
        
        # Print the message to the console
        print(message)
        
        # Log the message for debug purposes
        logger.info(message)
        
        # Return the list of available commands
        return ["add", "subtract", "multiply", "divide", "menu", "exit"]
