from fastapi import APIRouter, Depends, Query, HTTPException
from typing import List, Optional
# from .auth import verify_api_key # OLD: Removed
from .auth import verify_token # NEW: Imported for JWT verification
from .coingecko_client import CoinGeckoClient
from .models import Coin, CoinCategory, CoinDetails, MarketCoinDetails, TokenData # Import TokenData

router = APIRouter()
client = CoinGeckoClient()

@router.get("/coins", response_model=List[Coin])
def list_coins(token_data: TokenData = Depends(verify_token)): # Changed dependency
    return client.list_coins()

@router.get("/categories", response_model=List[CoinCategory])
def list_categories(token_data: TokenData = Depends(verify_token)): # Changed dependency
    return client.list_categories()

@router.get("/coins/{coin_id}", response_model=CoinDetails)
def get_coin(coin_id: str, token_data: TokenData = Depends(verify_token)): # Changed dependency
    return client.get_coin(coin_id, vs_currencies="usd,inr,cad")

@router.get("/coins/filter", response_model=List[MarketCoinDetails])
def filter_coins(
    token_data: TokenData = Depends(verify_token), # Changed dependency
    ids: Optional[str] = Query(None, description="Comma-separated list of coin IDs (e.g., 'bitcoin,ethereum')"),
    category: Optional[str] = Query(None, description="Filter by coin category ID (e.g., 'decentralized_finance')"),
    vs_currencies: str = Query("usd", description="Base currency for prices (e.g., 'usd' or 'inr' or 'cad')"),
    page_num: int = Query(1, ge=1, description="Page number for pagination"),
    per_page: int = Query(10, ge=1, le=250, description="Items per page (max 250)")
):
    
    if ids and category:
        raise HTTPException(
            status_code=400, 
            detail="Cannot filter by both 'ids' and 'category' simultaneously. Choose one."
        )

    supported_currencies = ["usd", "inr", "cad"]
    if vs_currencies.lower() not in supported_currencies:
        raise HTTPException(
            status_code=400, 
            detail=f"Unsupported currency: {vs_currencies}. Only {', '.join(supported_currencies).upper()} are supported."
        )

    return client.get_filtered_coins(
        ids=ids, 
        category=category, 
        vs_currencies=vs_currencies, 
        page=page_num, 
        per_page=per_page
    )