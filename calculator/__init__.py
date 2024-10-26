from calculator.calculations import Calculations
from calculator.history_facade.history_facade import HistoryFacade
from calculator.operations import add, subtract, multiply, divide, cos, sin, tan, sqrt 
from calculator.calculation import Calculation 
from decimal import Decimal 
from typing import Callable 
import logging

# Set up logging for this module
logger = logging.getLogger(__name__)

class Calculator:
    """A simple calculator class providing static methods to perform basic arithmetic operations."""

    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and perform a calculation, then return the result."""
        logger.debug("Performing operation: %s with a: %s, b: %s", operation, a, b)
        
        calculation = Calculation.create(a, b, operation)
        logger.info("Created calculation: %s", calculation)

        # Use HistoryFacade to add the calculation
        HistoryFacade().add_calculation(calculation)  # Add calculation to HistoryFacade
        logger.info("Added calculation to history via HistoryFacade: %s", calculation)

        result = calculation.perform()
        logger.info("Performed operation: %s with result: %s", operation, result)
        return result

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """Add two Decimal numbers."""
        logger.debug("Adding: %s + %s", a, b)
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """Subtract the second Decimal number from the first."""
        logger.debug("Subtracting: %s - %s", a, b)
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """Multiply two Decimal numbers."""
        logger.debug("Multiplying: %s * %s", a, b)
        return Calculator._perform_operation(a, b, multiply)
    
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Divide the first Decimal number by the second."""
        logger.debug("Dividing: %s / %s", a, b)
        return Calculator._perform_operation(a, b, divide)

    @staticmethod
    def sin(a: Decimal) -> Decimal:
        logger.debug("Calculating sin(%s)", a)
        return Calculator._perform_operation(a, None, sin)

    @staticmethod
    def cos(a: Decimal) -> Decimal:
        logger.debug("Calculating cos(%s)", a)
        return Calculator._perform_operation(a, None, cos)

    @staticmethod
    def tan(a: Decimal) -> Decimal:
        logger.debug("Calculating tan(%s)", a)
        return Calculator._perform_operation(a, None, tan)

    @staticmethod
    def sqrt(a: Decimal) -> Decimal:
        logger.debug("Calculating sqrt(%s)", a)
        return Calculator._perform_operation(a, None, sqrt)
