import pytest
from src.calculator import add

def test_addition_positive_numbers():
    # Arrange
    a, b = 10, 20
    # Act
    result = add(a, b)
    # Assert
    assert result == 30

def test_addition_string_fail():
    # Validates that adding a string to an int raises a TypeError
    with pytest.raises(TypeError):
        add(5, "five")
