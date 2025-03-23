"""
Utility functions for the calculator.
"""

def is_number(value: str) -> bool:
    """
    Check if a string is a valid number.

    :param value: String input
    :return: True if value is a number, False otherwise
    """
    try:
        float(value)
        return True
    except ValueError:
        return False

