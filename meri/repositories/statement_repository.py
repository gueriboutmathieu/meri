from logging import Logger
from sqlalchemy import text
from sqlalchemy.orm import Session

from meri.domain.entities.statement import Statement
from meri.domain.exceptions.statement import StatementConstraintException, StatementNotFoundException
from python_utils.sqlalchemy_crud_repository import SQLAlchemyCRUDRepository


class StatementRepositoryException(Exception):
    def __init__(self, message: str = "Statement repository exception") -> None:
        super().__init__(message)


class StatementRepository(SQLAlchemyCRUDRepository[Statement]):
    def __init__(self, session: Session, logger: Logger) -> None:
        super().__init__(
            session=session,
            entity_class=Statement,
            logger=logger,
            default_exception=StatementRepositoryException,
            not_found_exception=StatementNotFoundException,
            constraint_exception=StatementConstraintException
        )

    def index_vectors(self) -> None:
        self.session.execute(text("REINDEX INDEX vector_idx;"))

    def search(self, question_vector: list[float]) -> list[Statement]:
        return self.session.query(
            Statement.id,
            Statement.content,
            Statement.vector.l2_distance(question_vector).label("distance")  # pyright: ignore
        ).order_by("distance").limit(5).all()
