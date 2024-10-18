import sys
import logging
import logging.config
import re
from decimal import Decimal, InvalidOperation
from calculator.commands import CommandHandler
from calculator.plugins.add import AddCommand  # Ensure correct import paths
from calculator.plugins.subtract import SubtractCommand
from calculator.plugins.multiply import MultiplyCommand
from calculator.plugins.divide import DivideCommand
from calculator.plugins.menu import MenuCommand
from dotenv import load_dotenv
import os

def setup_logging():
    """Set up logging configuration based on environment."""
    environment = os.getenv('ENVIRONMENT', 'production')

    logger = logging.getLogger(__name__)

    if environment == 'development':
        # Log to a file in the 'logs' directory when in development mode
        log_file = os.path.join('logs', 'calculator.log')
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(sys.stdout)  # Also output to console
            ]
        )
        logger.info(f"Logging set to file: {log_file} and console (development).")
    else:
        # Use StreamHandler (console output) for other environments
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[logging.StreamHandler(sys.stdout)]
        )
        logger.info("Logging set to console (non-development).")

    return logger

def main():
    # Load environment variables from .env
    load_dotenv()

    # Setup logging and get the logger
    logger = setup_logging()
    logger.info("Starting the calculator application.")

    command_handler = CommandHandler()

    # Register commands in a loop for better maintainability
    command_classes = {
        "add": AddCommand,
        "subtract": SubtractCommand,
        "multiply": MultiplyCommand,
        "divide": DivideCommand,
        "menu": MenuCommand,
    }

    for command_name, command_class in command_classes.items():
        command_handler.register_command(command_name, command_class)

    logger.info("Registered all commands.")

    print("Welcome to the Calculator REPL!")
    print("Type commands like: add(1, 2), subtract(3, 1), etc.")
    print("Type 'menu' to list available commands.")
    print("Type 'exit' to exit.")

    while True:
        user_input = input(">>> ").strip()
        if user_input.lower() == 'exit':
            logger.info("Exiting the calculator.")
            print("Exiting the calculator.")
            break

        # Use regex to match the command and arguments, allowing for 'menu'
        match = re.match(r"(\w+)(?:\(([^)]*)\))?", user_input)

        if match:
            command_name = match.group(1)
            args = match.group(2)  # Get the arguments if present

            if args:
                args = args.split(",")  # Split arguments by comma
            else:
                args = []  # No arguments for menu command
            
            try:
                # Convert arguments to Decimal only if there are any
                decimal_args = list(map(Decimal, args)) if args else []
                command_handler.execute_command(command_name, *decimal_args)  # Pass as arguments
            except InvalidOperation:
                logger.error("Invalid input. Non-numeric values entered.")
                print("Invalid input. Please enter valid numbers.")
            except KeyError:
                logger.error(f"Unknown command: {command_name}")
                print(f"No such command: {command_name}. Type 'menu' for available commands.")
            except Exception as e:
                logger.exception(f"An error occurred: {e}")
                print(f"An error occurred: {e}")
        else:
            logger.warning(f"Invalid command format: {user_input}")
            print("Invalid command format")

if __name__ == '__main__':
    main()
