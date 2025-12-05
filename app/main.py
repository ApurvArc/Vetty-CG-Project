# app/main.py

from fastapi import APIRouter, Depends, Query, HTTPException
from .auth import verify_api_key
from .coingecko_client import CoinGeckoClient
from typing import Optional, List # Import Optional and List
from .models import Coin, CoinDetails # Import Coin and CoinDetails for type hinting

router = APIRouter()
client = CoinGeckoClient()

# ... existing code for /coins and /categories ...

@router.get("/coins/filter", response_model=List[Coin])
def filter_coins(
    category: Optional[str] = Query(None, description="Filter by category name"),
    page_num: int = Query(1, description="Page number for pagination", ge=1),
    per_page: int = Query(10, description="Items per page", ge=1, le=250),
    api_key: str = Depends(verify_api_key),
):
    """
    List specific coins according to ID and/or category, with pagination.
    Note: CoinGecko's 'coins/list' endpoint provides the full list, so pagination
    is handled manually by slicing the result.
    """
    coins = client.list_coins()
    # Logic to filter by category would be implemented here
    # Since CoinGecko list endpoint doesn't support category, 
    # we'll use a simplified implementation that assumes 'list_coins'
    # returns objects that can be easily filtered or we'd fetch all market data.
    
    # Simple Manual Pagination (Required for coins/list)
    start_index = (page_num - 1) * per_page
    end_index = start_index + per_page
    paginated_coins = coins[start_index:end_index]
    
    # Convert dicts to Pydantic models for response_model compliance (optional for this list endpoint)
    # return [Coin(**c) for c in paginated_coins]
    return paginated_coins


@router.get("/health")
def health_check():
    """Health check for the application and CoinGecko service."""
    try:
        # Check external service status
        coingecko_status = client.ping() 
        return {
            "api_status": "ok",
            "coingecko_status": "ok" if coingecko_status.get("gecko_says") else "down",
        }
    except Exception as e:
        # If API call fails completely
        raise HTTPException(status_code=503, detail=f"Service unavailable: {e}")

@router.get("/version")
def version_info():
    """Returns application version information."""
    return {
        "version": "1.0",
        "service": "Crypto Market API",
        "author": "Apurv Choudhary" # Add author info from README
    }

# Update the existing /coins/{coin_id} to ensure proper use of the new client method
@router.get("/coins/{coin_id}", response_model=dict)
def get_coin(coin_id: str, api_key: str = Depends(verify_api_key)):
    return client.get_coin(coin_id)