from logging import Logger
from meri.domain.entities.statement_entity import Statement as Statement
from meri.domain.exceptions.statement_exceptions import StatementConstraintException as StatementConstraintException, StatementNotFoundException as StatementNotFoundException
from python_utils.sqlalchemy_crud_repository import SQLAlchemyCRUDRepository
from sqlalchemy.orm import Session as Session

class StatementRepositoryException(Exception):
    def __init__(self, message: str = 'Statement repository exception') -> None: ...

class StatementRepository(SQLAlchemyCRUDRepository[Statement]):
    def __init__(self, session: Session, logger: Logger) -> None: ...
    def index_vectors(self) -> None: ...
    def search(self, question_vector: list[float]) -> list[Statement]: ...
