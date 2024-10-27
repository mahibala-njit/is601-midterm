from decimal import Decimal
from calculator import Calculator
from calculator.commands import Command
import logging

# Set up logging
logger = logging.getLogger(__name__)

class CosCommand(Command):
    """Command to calculate the cosine of a given angle (in radians)."""

    def execute(self, operand: Decimal, *args) -> Decimal:
        """Executes the cosine operation on the given operand."""
        try:
            result = Calculator.cos(operand)
            logger.info("Calculated cos(%s) = %s", operand, result)
            print(f"Result: cos({operand}) = {result}")
            return result
        except Exception as e:
            logger.error("Error calculating cos(%s): %s", operand, e)
            print(f"Error: Could not calculate cos({operand}). {e}")
            raise
