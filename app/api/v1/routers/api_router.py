from fastapi import APIRouter

from app.settings import CommentsSettings
from .reviews_router import reviews_router


api_router = APIRouter(prefix=CommentsSettings.load_from_env().API_PREFIX)
api_router.include_router(reviews_router)
