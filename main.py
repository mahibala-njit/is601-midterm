import sys
import logging
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

def setup_logging(environment):
    """Set up logging configuration based on environment."""
    logger = logging.getLogger(__name__)

    # Retrieve the log level and log file from the environment variable
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()  # Ensure it’s uppercase
    log_file = os.getenv('LOG_FILE', f'logs/{environment}_calculator.log')

    # Set the log level based on the environment variable
    level = getattr(logging, log_level, logging.INFO)  # Default to INFO if invalid level

    if environment == 'development':
        logging.basicConfig(
            level=level,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                #logging.StreamHandler(sys.stdout)
            ]
        )
        logger.info(f"Logging set to file: {log_file} and console (development).")
    else:
        logging.basicConfig(
            level=level,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[logging.StreamHandler(sys.stdout)]
        )
        logger.info("Logging set to console (non-development).")

    logger.info(f"Logging level set to : {log_level}")   

    return logger

def main():
    # Load environment variables from .env file
    environment = os.getenv('ENVIRONMENT', 'development')
    env_file = f'.env.{environment}'
    load_dotenv(env_file)

    # Setup logging and get the logger
    logger = setup_logging(environment)
    logger.info("Starting the calculator application.")

    # Suppress only FutureWarnings
    warnings.filterwarnings("ignore", category=FutureWarning)

    # Instantiate command handler and register commands
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
    logger.info("Registered all commands successfully.")

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

            # Process args if they exist, otherwise create an empty list
            args = args.split(",") if args else []

            try:
                # Handle string-based arguments specifically for history commands
                if command_name in ["save_history", "load_history"] and args:
                    command_handler.execute_command(command_name, *args)
                else:
                    # Convert to Decimal for numeric commands, catching invalid input
                    decimal_args = list(map(Decimal, args)) if args else []
                    command_handler.execute_command(command_name, *decimal_args)
                logger.info(f"Command '{command_name}' executed successfully with arguments: {args}")

            except InvalidOperation:
                logger.error("Invalid input. Non-numeric values entered.")
                print("Invalid input. Please enter valid numbers.")
            except KeyError:
                logger.error(f"Unknown command: {command_name}")
                print(f"No such command: {command_name}. Type 'menu' for available commands.")
            except Exception as e:
                logger.exception(f"An error occurred while processing the command '{command_name}': {e}")
                print(f"An error occurred: {e}")

        else:
            logger.warning(f"Invalid command format entered: {user_input}")
            print("Invalid command format. Type 'menu' to see available commands.")

if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        logging.critical("Critical error encountered during application execution: %s", str(ex))
        print("A critical error occurred. The application will now exit.")
