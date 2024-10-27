import sys
import logging
import logging.config
import re
import warnings
from decimal import Decimal, InvalidOperation
from calculator.commands import CommandHandler
from calculator.plugins.add import AddCommand
from calculator.plugins.subtract import SubtractCommand
from calculator.plugins.multiply import MultiplyCommand
from calculator.plugins.divide import DivideCommand
from calculator.plugins.menu import MenuCommand
from calculator.plugins.sin import SinCommand
from calculator.plugins.cos import CosCommand
from calculator.plugins.tan import TanCommand
from calculator.plugins.sqrt import SqrtCommand
from calculator.plugins.display_history import DisplayHistoryCommand
from calculator.plugins.save_history import SaveHistoryCommand
from calculator.plugins.load_history import LoadHistoryCommand
from calculator.plugins.clear_history import ClearHistoryCommand
from dotenv import load_dotenv
import os

def setup_logging():
    """Set up logging configuration based on environment."""
    environment = os.getenv('ENVIRONMENT', 'production')

    logger = logging.getLogger(__name__)

    if environment == 'development':
        log_file = os.path.join('logs', 'calculator.log')
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                #logging.StreamHandler(sys.stdout)
            ]
        )
        logger.info(f"Logging set to file: {log_file} and console (development).")
    else:
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

    # Suppress only FutureWarnings
    warnings.filterwarnings("ignore", category=FutureWarning)

    command_handler = CommandHandler()

    # Register commands in a loop for better maintainability
    command_classes = {
        "add": AddCommand,
        "subtract": SubtractCommand,
        "multiply": MultiplyCommand,
        "sin": SinCommand,
        "cos": CosCommand,
        "tan": TanCommand,
        "sqrt": SqrtCommand,
        "divide": DivideCommand,
        "menu": MenuCommand,
        "display_history": DisplayHistoryCommand,
        "save_history": SaveHistoryCommand,
        "load_history": LoadHistoryCommand,
        "clear_history": ClearHistoryCommand
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

        match = re.match(r"(\w+)(?:\(([^)]*)\))?", user_input)

        if match:
            command_name = match.group(1)
            args = match.group(2)

            if args:
                args = args.split(",")
            else:
                args = []
            
            try:
                # Handle specific commands that may require string arguments
                if command_name in ["save_history", "load_history"] and args:
                    command_handler.execute_command(command_name, *args)
                else:
                    decimal_args = list(map(Decimal, args)) if args else []
                    command_handler.execute_command(command_name, *decimal_args)
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
