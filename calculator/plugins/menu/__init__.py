import logging
from calculator.commands import Command

# Set up logging for this module
logger = logging.getLogger(__name__)

class MenuCommand(Command):
    def execute(self):
        # Define the message for available commands with usage details
        message = (
            "\n==================================================\n"
            "        Available Commands\n"
            "==================================================\n"
            " Arithmetic Operations:\n"
            "   add(a, b)         - Adds two numbers (e.g., add(1, 2))\n"
            "   subtract(a, b)    - Subtracts second number from first (e.g., subtract(3, 1))\n"
            "   multiply(a, b)    - Multiplies two numbers (e.g., multiply(2, 3))\n"
            "   divide(a, b)      - Divides first number by second (e.g., divide(6, 2))\n"
            "   sqrt(a)           - Calculates the square root of x (e.g., sqrt(4))\n"
            "\n Trigonometric Functions:\n"
            "   sin(a)            - Calculates the sine of x (e.g., sin(1))\n"
            "   cos(a)            - Calculates the cosine of x (e.g., cos(1))\n"
            "   tan(a)            - Calculates the tangent of x (e.g., tan(1))\n"
            "\n Calculation History Commands:\n"
            "   display_history()  - Displays the calculation history\n"
            "   load_history()     - Loads calculation history from a file\n"
            "   save_history()     - Saves current calculation history to a file\n"
            "\n Utility Commands:\n"
            "   menu              - Displays this menu\n"
            "   exit              - Exits the calculator\n"
            "=================================================="
        )
        
        # Print the message to the console
        print(message)

        # Log the message for debug purposes
        logger.info("Displayed menu: %s", message)
        
        # Return the list of available commands
        return message  # Join the list into a single string