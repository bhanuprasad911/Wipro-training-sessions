def validate_input(a, b):
    """Helper to ensure inputs are numeric."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numeric (int or float)")

def add(a, b):
    validate_input(a, b)
    return a + b

def subtract(a, b):
    validate_input(a, b)
    return a - b

def multiply(a, b):
    validate_input(a, b)
    return a * b

def divide(a, b):
    validate_input(a, b)
    if b == 0:
        # Requirement: Raise exception for division by zero
        raise ValueError("Division by zero is not allowed")
    return a / b