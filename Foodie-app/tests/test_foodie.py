import pytest
import requests

BASE_URL = "http://localhost:5000/api/v1"

@pytest.fixture
def sample_restaurant():
    payload = {"name": "Burger King", "category": "Fast Food", "location": "NYC"}
    response = requests.post(f"{BASE_URL}/restaurants", json=payload)
    return response.json()

def test_register_restaurant():
    payload = {"name": "Pizza Hut", "category": "Italian", "location": "Chicago"}
    response = requests.post(f"{BASE_URL}/restaurants", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Pizza Hut"

def test_get_restaurant_not_found():
    response = requests.get(f"{BASE_URL}/restaurants/999")
    assert response.status_code == 404

@pytest.mark.parametrize("name,email", [
    ("Alice", "alice@example.com"),
    ("Bob", "bob@example.com")
])
def test_user_registration(name, email):
    payload = {"name": name, "email": email, "password": "password123"}
    response = requests.post(f"{BASE_URL}/users/register", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == name