from decimal import Decimal
from decimal import InvalidOperation  # Ensure this import is present
from calculator import Calculator
from calculator.commands import Command  # Ensure this import path is correct



class DivideCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            raise InvalidOperation("Cannot divide by zero")
        result = Calculator.divide(self.a, self.b)
        print(f"Result: {result}")
        return result
