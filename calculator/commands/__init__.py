# calculator/commands/__init__.py

from abc import ABC, abstractmethod

class Command(ABC):
    """Abstract base class for all commands."""
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command_class):
        """Register a command to be executed by its name."""
        self.commands[command_name] = command_class  # Store class, not instance

    def execute_command(self, name, *args):
        if name not in self.commands:
            raise KeyError(f"No such command: {name}")
        command = self.commands[name](*args)
        return command.execute()  # Return the result from the command
