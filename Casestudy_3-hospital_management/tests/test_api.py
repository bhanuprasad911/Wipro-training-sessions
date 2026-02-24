import pytest
import requests

@pytest.mark.parametrize("name, age, disease", [
    ("John Doe", 30, "Flu"),
    ("Jane Smith", 25, "Cold")
])
def test_add_patient(base_url, name, age, disease):
    payload = {
        "name": name,
        "age": age,
        "disease": disease,
        "contact": "1234567890",
        "doctor_assigned": "Dr. House"
    }
    response = requests.post(f"{base_url}/patients", json=payload)
    assert response.status_code == 201
    assert response.json()["message"] == "Patient added successfully"

def test_get_nonexistent_patient(base_url):
    response = requests.get(f"{base_url}/patients/9999")
    assert response.status_code == 404