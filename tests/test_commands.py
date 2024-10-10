"""Unit tests for the Command and CommandHandler classes."""

from calculator.commands import Command
from calculator.commands import CommandHandler

class TestCommand(Command):
    """A concrete subclass that implements the abstract method."""

    def execute(self):
        # You can leave this empty, or raise NotImplementedError
        return None  # or any default value you'd like to return


def test_command_handler_with_test_command():
    """Test the CommandHandler with a test command."""
    command_handler = CommandHandler()
    command_handler.register_command("test", TestCommand)

    result = command_handler.execute_command("test")
    
    # This checks that the command was executed; adjust based on what you expect.
    assert result is None  # This should pass, depending on your TestCommand logic.
