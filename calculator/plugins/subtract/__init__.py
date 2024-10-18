import logging
from decimal import Decimal
from calculator import Calculator
from calculator.commands import Command  

# Set up logging for this module
logger = logging.getLogger(__name__)

class SubtractCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        self.a = a
        self.b = b

    def execute(self):
        logger.info("Executing SubtractCommand with arguments: a=%s, b=%s", self.a, self.b)
        result = Calculator.subtract(self.a, self.b)
        logger.debug("Subtraction result: %s", result)
        print(f"Result: {result}")
        return result
