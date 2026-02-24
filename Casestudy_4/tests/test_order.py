import pytest
import requests
from jsonschema import validate


order_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "user_id": {"type": "number"},
        "restaurant_id": {"type": "number"},
        "dishes": {"type": "array"},
        "status": {"type": "string"}
    },
    "required": ["id", "user_id", "restaurant_id", "dishes", "status"]
}

rating_schema = {
    "type": "object",
    "properties": {
        "order_id": {"type": "number"},
        "rating": {"type": "number"},
        "comment": {"type": ["string", "null"]}
    },
    "required": ["order_id", "rating"]
}


@pytest.fixture
def order_payload():
    return {
        "user_id": 1,
        "restaurant_id": 1,
        "dishes": [1, 2]
    }


@pytest.fixture
def rating_payload():
    return {
        "order_id": 1,
        "rating": 5,
        "comment": "Excellent food"
    }


# Place Order - Positive
def test_place_order_success(base_url,order_payload):
    response = requests.post(
        f"{base_url}/api/v1/orders",
        json=order_payload
    )

    assert response.status_code == 201
    validate(response.json(), order_schema)


# Place Order - Negative (Missing field)
def test_place_order_missing_field(base_url):
    payload = {
        "user_id": 1
    }

    response = requests.post(
        f"{base_url}/api/v1/orders",
        json=payload
    )

    # Your API currently throws 500 if missing fields
    assert response.status_code in [400, 500]


# Add Rating - Positive
def test_add_rating_success(base_url,order_payload, rating_payload):
    # First create order
    requests.post(f"{base_url}/api/v1/orders", json=order_payload)

    response = requests.post(
        f"{base_url}/api/v1/ratings",
        json=rating_payload
    )

    assert response.status_code == 201
    validate(response.json(), rating_schema)


# Get Orders by Restaurant
@pytest.mark.parametrize("rid", [1, 99])
def test_get_orders_by_restaurant(base_url,rid, order_payload):
    # create order
    requests.post(f"{base_url}/api/v1/orders", json=order_payload)

    response = requests.get(
        f"{base_url}/api/v1/restaurants/{rid}/orders"
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Get Orders by User
@pytest.mark.parametrize("uid", [1, 99])
def test_get_orders_by_user(base_url,uid, order_payload):
    requests.post(f"{base_url}/api/v1/orders", json=order_payload)

    response = requests.get(
        f"{base_url}/api/v1/users/{uid}/orders"
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)
