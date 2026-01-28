import pytest

@pytest.fixture
def api_client():
    """Fixture for functional E2E tests."""
    print("\n[Setup] Initializing API Client...")
    # Mocking a functional connection
    client = {"status": "ready", "version": "2.1.0"}
    yield client
    print("\n[Teardown] Closing API Client connection...")