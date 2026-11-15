"""Simple calculator module."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a / b. Raise ValueError on division by zero."""
    if b == 0:
        raise ValueError("division by zero")
    return a / b
