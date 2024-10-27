import math
from decimal import Decimal

def add(a: Decimal, b: Decimal) -> Decimal:
    """ Adds two Decimal numbers """
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """ Subtracts the second Decimal number from the first """
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """ Multiplies two Decimal numbers """
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    """  Divides the first Decimal number by the second. Raises a ZeroDivisionError
    if the second number is zero"""
    
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def sin(a: Decimal) -> Decimal:
    """Calculates the sine of a Decimal number."""
    return Decimal(math.sin(float(a)))

def cos(a: Decimal) -> Decimal:
    """Calculates the cosine of a Decimal number."""
    return Decimal(math.cos(float(a)))

def tan(a: Decimal) -> Decimal:
    """Calculates the tangent of a Decimal number."""
    return Decimal(math.tan(float(a)))

def sqrt(a: Decimal) -> Decimal:
    """Calculates the square root of a Decimal number. Raises ValueError for negative inputs."""
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return Decimal(math.sqrt(float(a)))