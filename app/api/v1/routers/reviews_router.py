from sqlite3 import Connection
from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import AfterValidator

from app.core.db.connection import get_connection
from app.core.db.repositories.reviews_repository import ReviewsRepository
from app.core.services.reviews_service import ReviewsService
from app.entities import Sentiments, Review

reviews_router = APIRouter(prefix="/reviews")


def validate_sentiment(sentiment: str) -> Sentiments:
    return Sentiments(sentiment)


@reviews_router.get("/")
def get_reviews(
        sentiment: Annotated[str | Sentiments, AfterValidator(validate_sentiment)],
        connection: Annotated[Connection, Depends(get_connection)]
):
    reviews_service = ReviewsService()
    reviews_repository = ReviewsRepository(connection)
    reviews = reviews_service.get_reviews(sentiment, reviews_repository)
    return reviews


@reviews_router.post("/")
def post_review(review: Review, connection: Annotated[Connection, Depends(get_connection)]):
    reviews_service = ReviewsService()
    reviews_repository = ReviewsRepository(connection)
    processed_review = reviews_service.process_review(review, reviews_repository)
    return processed_review
