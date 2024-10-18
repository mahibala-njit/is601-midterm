from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract, multiply, divide
import logging

# Set up logging for this module
logger = logging.getLogger(__name__)

class Calculation:
    """A class to represent a mathematical calculation that encapsulates two operands 
    and an operation (such as addition, subtraction, etc.)"""

    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Initializes a Calculation object with two operands and an operation"""
        self.a = a
        self.b = b
        self.operation = operation
        logger.debug("Initialized Calculation: a=%s, b=%s, operation=%s", a, b, operation.__name__)

    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Static method to create a new Calculation instance"""
        calculation = Calculation(a, b, operation)
        logger.info("Created Calculation: %s", calculation)
        return calculation

    def perform(self) -> Decimal:
        """Executes the operation stored in this Calculation object on the two operands"""
        logger.debug("Performing Calculation: %s", self)
        result = self.operation(self.a, self.b)
        logger.info("Performed %s: %s = %s", self.operation.__name__, self, result)
        return result

    def __repr__(self):
        """Returns a string representation of the Calculation object"""
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
