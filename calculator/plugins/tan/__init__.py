from decimal import Decimal
from calculator import Calculator
from calculator.commands import Command
import logging

# Set up logging
logger = logging.getLogger(__name__)

class TanCommand(Command):
    """Command to calculate the tangent of a given angle (in radians)."""

    def execute(self, operand: Decimal, *args) -> Decimal:
        """Executes the tangent operation on the given operand."""
        try:
            result = Calculator.tan(operand)
            logger.info("Calculated tan(%s) = %s", operand, result)
            print(f"Result: tan({operand}) = {result}")
            return result
        except Exception as e:
            logger.error("Error calculating tan(%s): %s", operand, e)
            print(f"Error: Could not calculate tan({operand}). {e}")
            raise
