import pytest
from src.Calculator import add, subtract, multiply, divide

# Discovery: Pytest will find this because of the 'test_' prefix
def test_addition():
    assert add(10, 5) == 15  # Assert statement

def test_subtraction():
    assert subtract(10, 5) == 5

def test_multiplication():
    assert multiply(2, 3) == 6

def test_division():
    assert divide(10, 2) == 5

# Requirement 4: Validate exception is raised
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        divide(10, 0)