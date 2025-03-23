"""
Core calculator operations.
"""

def add(a: float, b: float) -> float:
    """
    Add two numbers.

    :param a: First number
    :param b: Second number
    :return: Sum of a and b
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Subtract b from a.

    :param a: First number
    :param b: Second number
    :return: Result of a - b
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.

    :param a: First number
    :param b: Second number
    :return: Product of a and b
    """
    return a * b

def divide(a: float, b: float) -> float:
    """
    Divide a by b.

    :param a: Numerator
    :param b: Denominator
    :return: Quotient of a / b
    :raises ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
