from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from datetime import timedelta
from .config import settings
from .jwt import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from .models import Token

auth_router = APIRouter(prefix="/auth", tags=["Authentication"])

# Define dependency to get the internal API Key from the custom header
api_key_header_auth = APIKeyHeader(name="x-api-key", auto_error=False)

@auth_router.post("/token", response_model=Token)
def login_for_access_token(x_api_key: str = Depends(api_key_header_auth)):
    """
    Exchanges the Internal API Key (in x-api-key header) for a JWT Access Token.
    
    The Internal API Key is only used once to obtain the JWT.
    """
    
    if not x_api_key or x_api_key != settings.internal_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid internal API Key for token generation",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create token using the Internal API Key as the subject identity
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": settings.internal_api_key},
        expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}