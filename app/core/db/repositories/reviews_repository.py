from sqlite3 import Connection

from app.entities import Sentiments, ProcessedReview


class ReviewsRepository:
    __CREATE_SQL = """
        INSERT INTO reviews (text, sentiment, created_at) 
        VALUES (?, ?, ?)
    """

    __GET_SQL = """
        SELECT * FROM reviews WHERE sentiment=?
    """

    def __init__(self, connection: Connection):
        self._connection = connection

    def add(self, review: ProcessedReview) -> ProcessedReview:
        cursor = self._connection.cursor()
        cursor.execute(self.__CREATE_SQL, (review.text, review.sentiment, review.created_at))
        self._connection.commit()
        review.id = cursor.lastrowid
        return review

    def get(self, sentiment: Sentiments) -> list[list]:
        cursor = self._connection.cursor()
        cursor.execute(self.__GET_SQL, (sentiment,))
        return cursor.fetchall()
