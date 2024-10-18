from abc import ABC, abstractmethod
import logging

# Set up logging for this module
logger = logging.getLogger(__name__)

class Command(ABC):
    """Abstract base class for all commands."""
    
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}
        logger.info("Initialized CommandHandler with an empty command registry.")

    def register_command(self, command_name: str, command_class):
        """Register a command to be executed by its name."""
        self.commands[command_name] = command_class  # Store class, not instance
        logger.info(f"Registered command: {command_name}")

    def execute_command(self, name, *args):
        if name not in self.commands:
            logger.error(f"Attempted to execute unknown command: {name}")
            raise KeyError(f"No such command: {name}")
        
        # Instantiate the command class with the provided arguments
        command_class = self.commands[name]
        command_instance = command_class(*args)  # Pass args to the command's constructor
        result = command_instance.execute()  # Execute the command and get the result
        logger.info(f"Executed command: {name} with arguments: {args}")
        return result
