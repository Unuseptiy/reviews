from datetime import datetime

from ..db.repositories.reviews_repository import ReviewsRepository
from ...entities import Sentiments, Review, ProcessedReview


class ReviewsService:
    def process_review(self, review: Review, reviews_repository: ReviewsRepository) -> ProcessedReview:
        review_entity = ProcessedReview(
            text=review.text,
            sentiment=self._get_sentiment(review.text),
            created_at=datetime.utcnow().isoformat(),
        )
        return reviews_repository.add(review_entity)

    def get_reviews(self, sentiment: Sentiments, reviews_repository: ReviewsRepository) -> list[ProcessedReview]:
        reviews_entities = reviews_repository.get(sentiment)
        return [ProcessedReview.create_from_entity(review_entity) for review_entity in reviews_entities]

    @staticmethod
    def _get_sentiment(text: str):
        if "хорош" in text or "люблю" in text:
            return Sentiments.positive
        elif "плохо" in text or "ненавиж" in text:
            return Sentiments.negative
        else:
            return Sentiments.neutral
