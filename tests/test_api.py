from fastapi.testclient import TestClient
from app import app

client = TestClient(app)
headers = {"x-api-key": "mysecret"}

def test_list_coins():
    assert client.get("/coins", headers=headers).status_code == 200

def test_list_categories():
    assert client.get("/categories", headers=headers).status_code == 200

def test_get_coin():
    assert client.get("/coins/bitcoin", headers=headers).status_code == 200
