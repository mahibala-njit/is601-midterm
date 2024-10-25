from abc import ABC, abstractmethod
import logging
from decimal import Decimal

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

    def execute_command(self, command_name: str, *args: Decimal):
        command_class = self.commands.get(command_name)
        if not command_class:
            raise ValueError(f"Unknown command: {command_name}")

        # Check if command requires arguments (like AddCommand) or not (like CosCommand)
        if len(args) == 1 and command_name in ["cos", "sin", "tan", "sqrt"]:
            command_instance = command_class()  # Instantiate unary command without arguments
            result = command_instance.execute(args[0])  # Pass single argument to execute
        else:
            command_instance = command_class(*args)  # Instantiate binary command with arguments
            result = command_instance.execute()

        logger.info("Executed command: %s with arguments: %s", command_name, args)
        return result
