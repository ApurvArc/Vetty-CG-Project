from fastapi import FastAPI
from .main import router

def create_app():
    app = FastAPI(title="Crypto Market API", version="1.0")
    app.include_router(router)
    return app

app = create_app()
