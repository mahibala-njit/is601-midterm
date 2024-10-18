import logging
from calculator.commands import Command 

# Set up logging for this module
logger = logging.getLogger(__name__)

class MenuCommand(Command):
    def execute(self):
        logger.info("Executing MenuCommand.")
        available_commands = ["add", "subtract", "multiply", "divide", "menu", "exit"]
        print("Available commands:", ", ".join(available_commands))
        logger.debug("Available commands: %s", ", ".join(available_commands))
        return available_commands  # Return list of commands
