import pytest


BASE_URL = "http://127.0.0.1:5000"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

# Reset in-memory datastore before every test
# @pytest.fixture(autouse=True)
# def reset_data():
#     datastore.restaurants.clear()
#     datastore.dishes.clear()
#     datastore.users.clear()
#     datastore.orders.clear()
#     datastore.ratings.clear()
#     datastore.feedbacks.clear()
#     yield

@pytest.fixture
def restaurant_payload():
    return {
        "name": "Food Hub",
        "category": "Indian",
        "location": "Hyderabad",
        "images": ["img1.jpg"],
        "contact": "9876543210"
    }