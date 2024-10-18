# calculator/commands/add/__init__.py

from decimal import Decimal
import logging
from calculator import Calculator
from calculator.commands import Command  

# Set up logging for this module
logger = logging.getLogger(__name__)

class AddCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        self.a = a
        self.b = b
        logger.info(f"Initialized AddCommand with a={a}, b={b}")

    def execute(self):
        result = Calculator.add(self.a, self.b)
        logger.info(f"Executed AddCommand: {self.a} + {self.b} = {result}")
        print(f"Result: {result}")
        return result

