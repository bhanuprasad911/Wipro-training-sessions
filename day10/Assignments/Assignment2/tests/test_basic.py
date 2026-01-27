import pytest
from src.calculator import add

# xUnit-style: Module level
def setup_module(module):
    print("\n--- Starting Basic Operations Module ---")

def teardown_module(module):
    print("\n--- Finished Basic Operations Module ---")

# xUnit-style: Function level
def setup_function(function):
    print(f"\nSetting up for {function.__name__}")

# Using the fixture from conftest.py
def test_add_with_fixture(sample_data):
    result = add(sample_data["a"], sample_data["b"])
    assert result == 30

def test_add_simple():
    assert add(1, 2) == 3