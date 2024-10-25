from decimal import Decimal
from calculator import Calculator
from calculator.commands import Command
import logging

# Set up logging
logger = logging.getLogger(__name__)

class SqrtCommand(Command):
    """Command to calculate the square root of a given operand."""

    def execute(self, operand: Decimal, *args) -> Decimal:
        """Executes the square root operation on the given operand."""
        try:
            if operand < 0:
                raise ValueError("Square root of a negative number is not defined for real numbers.")
            result = Calculator.sqrt(operand)
            logger.info("Calculated sqrt(%s) = %s", operand, result)
            print(f"Result: sqrt({operand}) = {result}")
            return result
        except Exception as e:
            logger.error("Error calculating sqrt(%s): %s", operand, e)
            print(f"Error: Could not calculate sqrt({operand}). {e}")
            raise
