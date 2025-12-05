from fastapi import HTTPException, Depends, status
# FIX: Use the standard OAuth2PasswordBearer class, imported directly from fastapi.security
from fastapi.security import OAuth2PasswordBearer 
from .models import TokenData
from .jwt import decode_access_token

# Define dependency to extract token from Authorization: Bearer header
# This correctly integrates with the Swagger UI and extracts the token from the header.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

def verify_token(token: str = Depends(oauth2_scheme)) -> TokenData:
    """Verifies the JWT and returns the payload data."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # decode_access_token is defined in app/jwt.py
    payload = decode_access_token(token) 
    if payload is None:
        raise credentials_exception

    # Ensure the token has a subject identity
    token_data = TokenData(sub=payload.get("sub"))
    if token_data.sub is None:
        raise credentials_exception
        
    return token_data