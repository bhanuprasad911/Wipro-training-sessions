import pytest
import requests
from jsonschema import validate

restaurant_schema = {
    "type": "array"
}
def test_add_restaurant(base_url,restaurant_payload):
    response = requests.post(f"{base_url}/api/v1/restaurants",json=restaurant_payload)
    assert response.status_code == 201
    assert isinstance(response.json(), list)
def test_add_restaurant_duplicate(base_url, restaurant_payload):
    # requests.post(f"{base_url}/api/v1/restaurants", json=restaurant_payload)
    response = requests.post(f"{base_url}/api/v1/restaurants",json=restaurant_payload)
    assert response.status_code == 409
def test_get_restaurant(base_url,restaurant_payload):
    response = requests.get(f"{base_url}/api/v1/restaurants/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Food Hub"
def test_disable_restaurant(base_url,restaurant_payload):
    response = requests.put(f"{base_url}/api/v1/restaurants/1/disable")
    assert response.status_code == 200
    assert response.json()["message"] == "Restaurant disabled"
@pytest.mark.parametrize("query", [
    "Hyderabad",
    "hyderabad",
    "HYD"
])
def test_search_by_location(base_url, restaurant_payload, query):
    requests.post(f"{base_url}/api/v1/restaurants", json=restaurant_payload)

    response = requests.get(
        f"{base_url}/api/v1/restaurants/search?location={query}"
    )

    assert response.status_code == 200
    assert len(response.json()) >= 1
