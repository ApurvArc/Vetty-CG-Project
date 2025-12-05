from fastapi.testclient import TestClient
from app import app
from app.config import settings

client = TestClient(app)

# Test data
BTC_ID = "bitcoin"
NFT_CATEGORY = "non-fungible-tokens-nft"
# Use the INTERNAL_API_KEY provided by the user for token generation
INTERNAL_KEY = "Apurv12345" 

# Global variable to store the token for subsequent tests
ACCESS_TOKEN = None

# --- Helper function and Token Generation Test ---

def test_get_access_token():
    """Tests the /auth/token endpoint to get a JWT."""
    global ACCESS_TOKEN
    response = client.post(
        "/auth/token",
        headers={"x-api-key": INTERNAL_KEY}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    ACCESS_TOKEN = response.json()["access_token"]

def test_get_access_token_invalid_key():
    """Tests failure case for token generation."""
    response = client.post(
        "/auth/token",
        headers={"x-api-key": "wrong_key"}
    )
    assert response.status_code == 401
    assert "Invalid internal API Key" in response.json()["detail"]

def get_auth_headers():
    """Helper to ensure a token exists and return the Authorization header."""
    if not ACCESS_TOKEN:
        test_get_access_token()
    return {"Authorization": f"Bearer {ACCESS_TOKEN}"}

# --- Protected Endpoints Tests (Using JWT) ---

def test_list_coins():
    assert client.get("/coins", headers=get_auth_headers()).status_code == 200

def test_list_categories():
    assert client.get("/categories", headers=get_auth_headers()).status_code == 200

def test_get_coin_success():
    response = client.get(f"/coins/{BTC_ID}", headers=get_auth_headers())
    assert response.status_code == 200
    assert response.json()["id"] == BTC_ID
    
def test_get_coin_unauthorized():
    # Test without any token (401 expected)
    response = client.get(f"/coins/{BTC_ID}")
    assert response.status_code == 401
    
    # Test with a fake/expired token (401 expected)
    response = client.get(f"/coins/{BTC_ID}", headers={"Authorization": "Bearer fake.token.here"})
    assert response.status_code == 401

def test_filter_coins_by_category():
    response = client.get(
        "/coins/filter", 
        headers=get_auth_headers(), 
        params={
            "category": NFT_CATEGORY, 
            "vs_currencies": "cad" 
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0