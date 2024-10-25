"""Unit tests for the main calculator module and its REPL functionality."""

from decimal import Decimal, InvalidOperation
from unittest.mock import patch
import pytest
from calculator.commands import CommandHandler
from calculator.plugins.add import AddCommand
from calculator.plugins.subtract import SubtractCommand
from calculator.plugins.multiply import MultiplyCommand
from calculator.plugins.divide import DivideCommand
from calculator.plugins.menu import MenuCommand
from calculator.plugins.display_history import DisplayHistoryCommand
from calculator.plugins.save_history import SaveHistoryCommand
from calculator.plugins.load_history import LoadHistoryCommand

# Import main at the top level
from main import main

def setup_command_handler():
    """Set up the CommandHandler with available commands."""
    command_handler = CommandHandler()
    command_handler.register_command("add", AddCommand)
    command_handler.register_command("subtract", SubtractCommand)
    command_handler.register_command("multiply", MultiplyCommand)
    command_handler.register_command("divide", DivideCommand)
    command_handler.register_command("menu", MenuCommand)
    command_handler.register_command("display_history", DisplayHistoryCommand)
    command_handler.register_command("save_history", SaveHistoryCommand)
    command_handler.register_command("load_history", LoadHistoryCommand)
    return command_handler

def test_add_command():
    """Test the add command for correct output."""
    command_handler = setup_command_handler()
    result = command_handler.execute_command("add", Decimal('1.5'), Decimal('2.5'))
    assert result == Decimal('4.0')

def test_subtract_command():
    """Test the subtract command for correct output."""
    command_handler = setup_command_handler()
    result = command_handler.execute_command("subtract", Decimal('5.5'), Decimal('2.0'))
    assert result == Decimal('3.5')

def test_multiply_command():
    """Test the multiply command for correct output."""
    command_handler = setup_command_handler()
    result = command_handler.execute_command("multiply", Decimal('2.0'), Decimal('3.0'))
    assert result == Decimal('6.0')

def test_divide_command():
    """Test the divide command for correct output."""
    command_handler = setup_command_handler()
    result = command_handler.execute_command("divide", Decimal('10.0'), Decimal('2.0'))
    assert result == Decimal('5.0')

def test_divide_by_zero():
    """Test that dividing by zero raises an InvalidOperation."""
    command_handler = setup_command_handler()
    with pytest.raises(InvalidOperation):
        command_handler.execute_command("divide", Decimal('10.0'), Decimal('0.0'))

def test_invalid_command():
    """Test that an invalid command raises a KeyError."""
    command_handler = setup_command_handler()
    with pytest.raises(KeyError):
        command_handler.execute_command("invalid_command")

def test_menu_command():
    """Test that the menu command executes successfully."""
    command_handler = setup_command_handler()
    result = command_handler.execute_command("menu")
    assert result is not None  # Check the expected return value of the menu

@patch('builtins.input', side_effect=["add(1, 2)", "subtract(5, 3)", "menu", "exit"])
def test_main_repl(mock_input):
    """Test the main REPL for valid commands."""
    with patch('builtins.print') as mock_print:
        main()  # Call the main function directly here
        mock_print.assert_any_call("Welcome to the Calculator REPL!")
        mock_print.assert_any_call("Type commands like: add(1, 2), subtract(3, 1), etc.")
        mock_print.assert_any_call("Result: 2")  # Result of subtract(5, 3)
        mock_print.assert_any_call("Result: 3")  # Result of add(1, 2)
        mock_print.assert_any_call("Available commands: add, subtract, multiply, divide, display_history, load_history, save_history, menu, exit")

@patch('builtins.input', side_effect=[
    "add(1, 2)",
    "invalid_command",
    "menu",
    "subtract(5, 3)",
    "exit"
])
def test_main_repl_with_invalid_command(mock_input):
    """Test the main REPL with an invalid command."""
    with patch('builtins.print') as mock_print:
        main()  # Call the main function directly here
        
        # Check for valid command execution
        mock_print.assert_any_call("Result: 2")  # Result of subtract(5, 3)

        # Check for invalid command handling
        mock_print.assert_any_call("No such command: invalid_command. Type 'menu' for available commands.")
        
        # Check for valid menu command
        mock_print.assert_any_call("Available commands: add, subtract, multiply, divide, display_history, load_history, save_history, menu, exit")

@patch('builtins.input', side_effect=["menu", "exit"])
def test_main_repl_with_menu_command(mock_input):
    """Test the main REPL with the menu command."""
    with patch('builtins.print') as mock_print:
        main()  # Call the main function directly here

        # Check that the menu command was called
        mock_print.assert_any_call("Available commands: add, subtract, multiply, divide, display_history, load_history, save_history, menu, exit")
        
        # Check that exit was called
        mock_print.assert_any_call("Exiting the calculator.")

@patch('builtins.input', side_effect=["divide(1, 0)", "exit"])
def test_main_repl_with_divide_by_zero(mock_input):
    """Test the main REPL for handling division by zero."""
    with patch('builtins.print') as mock_print:
        main()  # Call the main function directly here

        # Check error handling for division by zero
        mock_print.assert_any_call("Invalid input. Please enter valid numbers.")
        mock_print.assert_any_call("Exiting the calculator.")

@patch('builtins.input', side_effect=["add(1, 2)", "exit"])
def test_main_repl_valid_commands(mock_input):
    """Test the main REPL with valid commands."""
    with patch('builtins.print') as mock_print:
        main()  # Call the main function directly here

        # Check that the add command was executed
        mock_print.assert_any_call("Result: 3")  # Result of add(1, 2)

        # Check that exit was called
        mock_print.assert_any_call("Exiting the calculator.")

@patch('builtins.input', side_effect=[
    "add(1, 2)",  # Valid command
    "invalid_command_format",  # Invalid command format
    "exit"
])
def test_main_repl_with_invalid_command_format(mock_input):
    """Test the main REPL with an invalid command format."""
    with patch('builtins.print') as mock_print:
        main()  # Call the main function directly here

        # Check that the add command was executed
        mock_print.assert_any_call("Welcome to the Calculator REPL!")
        mock_print.assert_any_call("Type commands like: add(1, 2), subtract(3, 1), etc.")
        mock_print.assert_any_call("Result: 3")  # Result of add(1, 2)

        # Check that exit was called
        mock_print.assert_any_call("Exiting the calculator.")

if __name__ == "__main__":
    pytest.main()
