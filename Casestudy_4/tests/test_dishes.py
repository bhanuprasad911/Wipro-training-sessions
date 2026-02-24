import pytest
import requests
from jsonschema import validate


dish_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "type": {"type": "string"},
        "price": {"type": "number"},
        "available_time": {"type": "string"},
        "image": {"type": ["string", "null"]},
        "enabled": {"type": "boolean"}
    },
    "required": ["id", "name", "type", "price", "available_time", "enabled"]
}

message_schema = {
    "type": "object",
    "properties": {
        "message": {"type": "string"}
    },
    "required": ["message"]
}
@pytest.fixture
def dish_payload():
    return {
        "name": "Paneer Butter Masala",
        "type": "Veg",
        "price": 250,
        "available_time": "10AM-10PM",
        "image": "paneer.jpg"
    }


# -----------------------
#  Add Dish (Positive)
def test_add_dish(base_url,dish_payload):
    response = requests.post(
        f"{base_url}/api/v1/restaurants/1/dishes",
        json=dish_payload
    )

    assert response.status_code == 201
    validate(response.json(), dish_schema)


# Update Dish (Positive + Negative)
@pytest.mark.parametrize("dish_id,expected", [
    (1, 200),
    (999, 404)
])
def test_update_dish(base_url,dish_id, expected):
    payload = {"price": 300}
    response = requests.put(
        f"{base_url}/api/v1/dishes/{dish_id}",
        json=payload
    )
    assert response.status_code == expected


# Update Dish Status
@pytest.mark.parametrize("dish_id,expected", [
    (1, 200),
    (999, 404)
])
def test_update_dish_status(base_url,dish_id, expected):
    payload = {"enabled": False}
    response = requests.put(
        f"{base_url}/api/v1/dishes/{dish_id}/status",
        json=payload
    )
    assert response.status_code == expected


#Delete Dish
@pytest.mark.parametrize("dish_id,expected", [
    (1, 200),
    (999, 404)
])
def test_delete_dish(base_url,dish_id, expected):
    response = requests.delete(
        f"{base_url}/api/v1/dishes/{dish_id}"
    )
    assert response.status_code == expected
