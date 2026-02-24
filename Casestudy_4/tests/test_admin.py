from jsonschema import validate
import requests
import pytest

approve_schema = {
    "type": "object",
    "properties": {
        "message": {"type": "string"}
    },
    "required": ["message"]
}

orders_schema = {
    "type": "object",
    "properties": {
        "orders": {"type": "array"}
    },
    "required": ["orders"]
}

feedback_schema = {
    "type": "object",
    "properties": {
        "feedbacks": {"type": "array"}
    },
    "required": ["feedbacks"]
}
def test_admin_approve_restaurant(base_url,restaurant_payload):
    create = requests.post(
        f"{base_url}/api/v1/restaurants",
        json=restaurant_payload
    )
    assert create.status_code == 201
    response = requests.put(f"{base_url}/api/v1/admin/restaurants/1/approve")
    assert response.status_code == 200
    validate(response.json(), approve_schema)

@pytest.mark.parametrize("rid,expected", [
    (1, 200),
    (99, 404)
])
def test_admin_disable_restaurant(base_url, rid, expected,restaurant_payload):
    # create = requests.post(
    #     f"{base_url}/api/v1/restaurants",
    #     json=restaurant_payload
    # )
    # assert create.status_code == 201
    response = requests.put(f"{base_url}/api/v1/admin/restaurants/{rid}/disable")
    assert response.status_code == expected


def test_admin_get_orders(base_url):
    response = requests.get(f"{base_url}/api/v1/admin/orders")

    assert response.status_code == 200
    validate(response.json(), orders_schema)

def test_admin_get_feedback(base_url):
    response = requests.get(f"{base_url}/api/v1/admin/feedback")

    assert response.status_code == 200
    validate(response.json(), feedback_schema)
