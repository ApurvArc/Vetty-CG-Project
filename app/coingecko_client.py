# app/coingecko_client.py

import requests
from .config import settings

class CoinGeckoClient:
    BASE_URL = "https://api.coingecko.com/api/v3"

    # ... existing list_coins and list_categories methods ...

    def get_coin(self, coin_id: str):
        # REQUIRED CHANGE: vs_currencies must include usd, inr, and cad
        currencies = "usd,inr,cad" 
        url = f"{self.BASE_URL}/simple/price?ids={coin_id}&vs_currencies={currencies}&x_cg_demo_api_key={settings.coingecko_api_key}"
        return requests.get(url).json()

    # New method for Health Check (Extra Requirement)
    def ping(self):
        url = f"{self.BASE_URL}/ping?x_cg_demo_api_key={settings.coingecko_api_key}"
        return requests.get(url).json()