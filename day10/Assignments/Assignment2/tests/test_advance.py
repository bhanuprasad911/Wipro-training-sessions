from src.calculator import divide

# Pytest automatically finds 'db_connection' in conftest.py
def test_division_with_resource(db_connection, sample_data):
    print(f"Using {db_connection} for audit logs")
    assert divide(sample_data["a"], sample_data["b"]) == 2