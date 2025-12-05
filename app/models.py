from pydantic import BaseModel
from typing import Optional

class Coin(BaseModel):
    id: str
    symbol: str
    name: str

class CoinCategory(BaseModel):
    category_id: str
    name: str

class CoinDetails(BaseModel):
    # Used for the simple /coins/{coin_id} endpoint
    id: str
    usd: Optional[float] = None
    inr: Optional[float] = None
    cad: Optional[float] = None

class MarketCoinDetails(BaseModel):
    # Used for the /coins/filter endpoint
    id: str
    symbol: str
    name: str
    current_price: float
    market_cap: Optional[float] = None
    total_volume: Optional[float] = None
    price_change_percentage_24h: Optional[float] = None
    # Note: These fields are dynamically named by CoinGecko's markets endpoint, 
    # but the pydantic model will automatically snake_case them.

class Token(BaseModel):
    """The model for the JWT response."""
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    """The model for the JWT payload."""
    sub: Optional[str] = None