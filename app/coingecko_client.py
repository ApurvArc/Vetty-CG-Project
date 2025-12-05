# app/coingecko_client.py

import requests
from fastapi import HTTPException
from typing import List, Dict, Any, Optional
from .config import settings

class CoinGeckoClient:
    BASE_URL = "https://api.coingecko.com/api/v3"

    def _make_request(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """Internal helper for making requests with error handling and key management."""
        url = f"{self.BASE_URL}/{endpoint}"
        
        if params is None:
            params = {}
        # Add API key to query parameters for free tier
        params['x_cg_demo_api_key'] = settings.coingecko_api_key

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return response.json()
        except requests.exceptions.HTTPError as e:
            # Re-raise as a proper FastAPI HTTPException
            status_code = response.status_code if 'response' in locals() else 500
            detail = f"CoinGecko API Error ({status_code}): {e.response.text if 'response' in locals() else 'Unknown error'}"
            raise HTTPException(status_code=status_code, detail=detail)
        except requests.exceptions.RequestException as e:
            # Handle connection errors (e.g., DNS, timeout)
            raise HTTPException(status_code=503, detail=f"External API Service Unavailable: {e}")

    def list_coins(self) -> List[Dict[str, Any]]:
        return self._make_request("coins/list")

    def list_categories(self) -> List[Dict[str, Any]]:
        return self._make_request("coins/categories")

    def get_coin(self, coin_id: str) -> Dict[str, float]:
        """Gets a single coin's price, processing the response to be flat."""
        # vs_currencies must include usd, inr, and cad
        data = self._make_request(
            "simple/price", 
            params={"ids": coin_id, "vs_currencies": "usd,inr,cad"}
        )
        
        # Process the nested response: {"bitcoin": {"usd": 68000}} -> {"id": "bitcoin", "usd": 68000}
        if coin_id in data:
            price_data = data[coin_id]
            price_data["id"] = coin_id
            return price_data
        
        raise HTTPException(status_code=404, detail=f"Coin ID '{coin_id}' not found.")

    def get_filtered_coins(self, ids: Optional[str] = None, category: Optional[str] = None, 
                           vs_currencies: str = "usd", page: int = 1, per_page: int = 10) -> List[Dict[str, Any]]:
        
        params = {
            "vs_currency": vs_currencies.split(',')[0].strip(),
            "order": "market_cap_desc",
            "per_page": per_page,
            "page": page,
            "sparkline": "false",
            "price_change_percentage": "24h"
        }
        
        if ids:
            params["ids"] = ids
        elif category:
            params["category"] = category
        
        return self._make_request("coins/markets", params=params)

    # Added Health Check method
    def ping(self):
        return self._make_request("ping")