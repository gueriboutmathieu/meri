import pytest
from pytest_mock import MockerFixture
from sqlalchemy.orm import Session
from uuid6 import uuid7

from meri.domain.entities.statement_entity import Statement
from meri.domain.exceptions.statement_exceptions import StatementNotFoundException, StatementConstraintException
from meri.repositories.statement_repository import StatementRepository, StatementRepositoryException
from python_utils.loggers import get_logger


session = Session()
logger = get_logger(__name__)


@pytest.fixture
def statement_repository() -> StatementRepository:
    return StatementRepository(session=session, logger=logger)


def test_statement_repository_init(statement_repository: StatementRepository):
    assert statement_repository.session == session
    assert statement_repository.logger == logger
    assert statement_repository.entity_class == Statement
    assert statement_repository.default_exception == StatementRepositoryException
    assert statement_repository.not_found_exception == StatementNotFoundException
    assert statement_repository.constraint_exception == StatementConstraintException


def test_statement_repository_index_vectors(mocker: MockerFixture, statement_repository: StatementRepository):
    mocker.patch.object(statement_repository.session, "execute", return_value=None)
    assert statement_repository.index_vectors() is None


def test_statement_repository_search(mocker: MockerFixture, statement_repository: StatementRepository):
    vector = [1.0, 2.0, 3.0]
    mock_query = mocker.Mock()
    mocker.patch.object(statement_repository.session, "query", return_value=mock_query)
    mock_query.filter.return_value = mock_query  # pyright: ignore
    mock_query.order_by.return_value = mock_query  # pyright: ignore
    mock_query.limit.return_value = mock_query  # pyright: ignore
    expected_statements = [
        Statement(id=uuid7(), content="Statement 1", vector=vector)  # pyright: ignore
    ]
    mock_query.all.return_value = expected_statements  # pyright: ignore

    result = statement_repository.search(vector)
    assert result == expected_statements
