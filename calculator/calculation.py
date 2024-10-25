from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract, multiply, divide
import logging

# Set up logging for this module
logger = logging.getLogger(__name__)

class Calculation:
    """A class to represent a mathematical calculation that encapsulates two operands 
    and an operation (such as addition, subtraction, etc.)"""

    def __init__(self, operation: Callable, a: Decimal, b: Decimal = None):
        self.operation = operation
        self.a = a
        self.b = b  # optional for unary operations
        logger.debug("Initialized Calculation: a=%s, b=%s, operation=%s", a, b, operation)

    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable) -> 'Calculation':
        """Static method to create a new Calculation instance"""
        # Adjust the operation to ensure it is callable and not a Decimal
        calculation = Calculation(operation, a, b)
        logger.info("Created Calculation: %s", calculation)
        return calculation

    def perform(self) -> Decimal:
        if self.b is None:
            result = self.operation(self.a)  # Unary
        else:
            result = self.operation(self.a, self.b)  # Binary
        logger.info("Performed %s: %s = %s", self.operation.__name__, self, result)
        return result

    def __repr__(self):
        """Returns a string representation of the Calculation object"""
        return f"Calculation({self.a}, {self.b}, {self.operation})"
