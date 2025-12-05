# app/auth.py

from fastapi import Header, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from .config import settings
from .security import decode_access_token # Import the decoding function

# Use OAuth2PasswordBearer for token extraction (defaults to 'Bearer <token>')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Remove the old verify_api_key function

def get_current_user(token: str = Depends(oauth2_scheme)):
    """Decodes the JWT and validates its contents."""
    
    payload = decode_access_token(token)
    
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired authentication token")

    # In a real app, you would fetch user data from a DB here using payload['sub']
    # For this exercise, we just verify the payload exists.
    
    # This return value can be used as the dependency result
    return payload