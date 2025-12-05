from pydantic import BaseModel

class Coin(BaseModel):
    id: str
    symbol: str
    name: str

class CoinCategory(BaseModel):
    category_id: str
    name: str

class CoinDetails(BaseModel):
    id: str
    usd: float
