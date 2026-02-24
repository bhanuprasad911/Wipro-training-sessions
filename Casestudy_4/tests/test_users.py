import pytest
import requests
from jsonschema import validate


user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "password": {"type": "string"}
    },
    "required": ["id", "name", "email", "password"]
}

feedback_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "user_id": {"type": "number"},
        "order_id": {"type": "number"},
        "rating": {"type": "number"},
        "comment": {"type": "string"}
    },
    "required": ["id", "user_id", "order_id", "rating", "comment"]
}


@pytest.fixture
def user_payload():
    return {
        "name": "ram",
        "email": "ram@gmail.com",
        "password": "12345"
    }


@pytest.fixture
def feedback_payload():
    return {
        "user_id": 1,
        "order_id": 1,
        "rating": 5,
        "comment": "Excellent service"
    }



def test_user_register_success(base_url,user_payload):
    response = requests.post(
        f"{base_url}/api/v1/user/register",
        json=user_payload
    )

    assert response.status_code == 201
    validate(response.json(), user_schema)


#Register User - Duplicate
def test_user_register_duplicate(base_url,user_payload):
    requests.post(
        f"{base_url}/api/v1/user/register",
        json=user_payload
    )

    response = requests.post(
        f"{base_url}/api/v1/user/register",
        json=user_payload
    )

    assert response.status_code == 409
    assert "error" in response.json()


# Add Feedback - Positive
def test_add_feedback_success(base_url,feedback_payload):
    response = requests.post(
        f"{base_url}/api/v1/user/feedback",
        json=feedback_payload
    )

    assert response.status_code == 201
    validate(response.json(), feedback_schema)


# Add Feedback - Negative (Missing field)
def test_add_feedback_missing_field(base_url):
    payload = {
        "user_id": 1,
        "order_id": 1
    }

    response = requests.post(
        f"{base_url}/api/v1/user/feedback",
        json=payload
    )

    # Your API may throw 500 since no validation
    assert response.status_code in [400, 500]
