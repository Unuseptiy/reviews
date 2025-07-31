import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

from fastapi import FastAPI

from app.api.v1.routers.api_router import api_router
from app.entities import Sentiments


def validate_sentiment(sentiment: str) -> Sentiments:
    return Sentiments(sentiment)


def get_app() -> FastAPI:
    fastapi_app = FastAPI()
    fastapi_app.include_router(api_router)
    return fastapi_app


app = get_app()
