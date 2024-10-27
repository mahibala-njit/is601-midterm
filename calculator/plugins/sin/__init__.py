from decimal import Decimal
from calculator import Calculator
from calculator.commands import Command
import logging

# Set up logging
logger = logging.getLogger(__name__)

class SinCommand(Command):
    """Command to calculate the sine of a given angle (in radians)."""

    def execute(self, operand: Decimal, *args) -> Decimal:
        """Executes the sine operation on the given operand."""
        try:
            result = Calculator.sin(operand)
            logger.info("Calculated sin(%s) = %s", operand, result)
            print(f"Result: sin({operand}) = {result}")
            return result
        except Exception as e:
            logger.error("Error calculating sin(%s): %s", operand, e)
            print(f"Error: Could not calculate sin({operand}). {e}")
            raise
