# app/models.py

from pydantic import BaseModel

class Coin(BaseModel):
    id: str
    symbol: str
    name: str

class CoinCategory(BaseModel):
    category_id: str
    name: str

# REQUIRED CHANGE: Add inr and cad fields
class CoinDetails(BaseModel):
    id: str
    usd: float
    inr: float
    cad: float