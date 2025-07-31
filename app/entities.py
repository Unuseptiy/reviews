from enum import StrEnum
from pydantic import BaseModel


class Sentiments(StrEnum):
    positive: str = "positive"
    negative: str = "negative"
    neutral: str = "neutral"


class Review(BaseModel):
    text: str


class ProcessedReview(Review):
    id: int | None = None
    sentiment: Sentiments
    created_at: str

    @classmethod
    def create_from_entity(cls, entity: list):
        return cls(
            id=entity[0],
            text=entity[1],
            sentiment=entity[2],
            created_at=entity[3],
        )

    # def __conform__(self, protocol):
    #     if protocol is sqlite3.PrepareProtocol:
    #         return f"{self.text};{self.sentiment};{self.created_at}"
