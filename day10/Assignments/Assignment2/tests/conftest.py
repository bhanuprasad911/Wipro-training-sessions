import pytest

# Fixture with "module" scope: Runs once per test file
@pytest.fixture(scope="module")
def db_connection():
    print("\n[Setup] Opening Database Connection...")
    yield "DB_CONNECTED"
    print("\n[Teardown] Closing Database Connection...")

# Fixture with "function" scope: Runs before every single test
@pytest.fixture(scope="function")
def sample_data():
    print("\n[Setup] Preparing fresh test data...")
    return {"a": 20, "b": 10}