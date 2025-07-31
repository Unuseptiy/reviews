import os
from dataclasses import dataclass
from pathlib import Path


# todo: хорошо бы pydantic.BaseSettings
@dataclass(frozen=True, slots=True)
class CommentsSettings:
    DB_NAME: str
    API_PREFIX: str

    @classmethod
    def load_from_env(cls):
        return cls(
            DB_NAME=os.getenv("DB_NAME", Path(__file__).parents[1] / "reviews.db"),
            API_PREFIX=os.getenv("API_PREFIX", "/api/v1"),
        )
