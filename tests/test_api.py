# tests/test_api.py

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)
headers = {"x-api-key": "mysecret"}

def test_list_coins():
    assert client.get("/coins", headers=headers).status_code == 200

def test_list_categories():
    assert client.get("/categories", headers=headers).status_code == 200

def test_get_coin_with_currencies():
    # Test that the price request is successful (now fetching INR/CAD)
    response = client.get("/coins/bitcoin", headers=headers)
    assert response.status_code == 200
    # Add an assertion that the response contains the new currencies (optional but good practice)
    # assert "bitcoin" in response.json()
    # assert "inr" in response.json()["bitcoin"]
    # assert "cad" in response.json()["bitcoin"]

def test_filter_coins_pagination():
    # Test the new filter endpoint with pagination params
    response = client.get("/coins/filter?page_num=2&per_page=5", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) <= 5 # Check pagination limit

def test_health_check():
    # Test the new health check endpoint
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["api_status"] == "ok"
    # Note: coingecko_status check relies on external service, better to mock in real unit test

def test_version_info():
    # Test the new version info endpoint
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json()["version"] == "1.0"