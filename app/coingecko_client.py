import requests
from .config import settings

class CoinGeckoClient:
    BASE_URL = "https://api.coingecko.com/api/v3"

    def list_coins(self):
        url = f"{self.BASE_URL}/coins/list?x_cg_demo_api_key={settings.coingecko_api_key}"
        return requests.get(url).json()

    def list_categories(self):
        url = f"{self.BASE_URL}/coins/categories?x_cg_demo_api_key={settings.coingecko_api_key}"
        return requests.get(url).json()

    def get_coin(self, coin_id: str):
        url = f"{self.BASE_URL}/simple/price?ids={coin_id}&vs_currencies=usd&x_cg_demo_api_key={settings.coingecko_api_key}"
        return requests.get(url).json()
