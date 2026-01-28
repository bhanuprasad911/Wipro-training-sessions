import pytest
import time

@pytest.mark.functional
class TestProductWorkflow:
    
    @pytest.mark.parametrize("product_id", [101, 102, 103, 104])
    def test_get_product_details(self, api_client, product_id):
        # Simulated delay to show parallel execution benefit
        time.sleep(1) 
        assert api_client["status"] == "ready"
        print(f"Verified product {product_id}")

    def test_system_version(self, api_client):
        time.sleep(1)
        assert "version" in api_client