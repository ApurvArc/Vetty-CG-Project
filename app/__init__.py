from fastapi import FastAPI
from .main import router
from .auth_router import auth_router # Import new router

def create_app():
    app = FastAPI(title="Crypto Market API", version="1.0")
    app.include_router(auth_router) # Include the new auth router
    app.include_router(router)
    return app

app = create_app()