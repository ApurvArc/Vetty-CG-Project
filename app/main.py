from fastapi import APIRouter, Depends
from .auth import verify_api_key
from .coingecko_client import CoinGeckoClient

router = APIRouter()
client = CoinGeckoClient()

@router.get("/coins")
def list_coins(api_key: str = Depends(verify_api_key)):
    return client.list_coins()

@router.get("/categories")
def list_categories(api_key: str = Depends(verify_api_key)):
    return client.list_categories()

@router.get("/coins/{coin_id}")
def get_coin(coin_id: str, api_key: str = Depends(verify_api_key)):
    return client.get_coin(coin_id)
