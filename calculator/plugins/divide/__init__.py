from decimal import Decimal
from decimal import InvalidOperation  
import logging
from calculator import Calculator
from calculator.commands import Command 

# Set up logging for this module
logger = logging.getLogger(__name__)

class DivideCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        self.a = a
        self.b = b
        logger.info(f"Initialized DivideCommand with a={a}, b={b}")

    def execute(self):
        try:
            if self.b == 0:
                logger.error("Attempted to divide by zero.")
                raise InvalidOperation("Cannot divide by zero")
            result = Calculator.divide(self.a, self.b)
            logger.info(f"Executed DivideCommand: {self.a} / {self.b} = {result}")
            print(f"Result: {result}")
            return result
        except InvalidOperation as e:
            logger.exception("Invalid operation: %s", e)
            raise  # Re-raise the exception after logging it
