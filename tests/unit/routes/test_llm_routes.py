import pytest  # pyright: ignore  # noqa: F401
from fastapi.testclient import TestClient
from logging import Logger
from pytest_mock import MockerFixture
from sqlalchemy.orm import Session

from meri.domain.domain import Domain
from meri.routes.fastapi_app import FastapiApp
from meri.repositories.statement_repository import StatementRepository
from meri.services.embedding_service import EmbeddingService
from meri.services.llm_service import LlmService


class MockedCommandContext:
    def __init__(self) -> None:
        self._llm_service = LlmService("", "")
        self._embedding_service = EmbeddingService("", "", 0)
        self._statement_repository = StatementRepository(Session(), Logger(__name__))

    @property
    def llm_service(self):
        return self._llm_service

    @property
    def embedding_service(self):
        return self._embedding_service

    @property
    def statement_repository(self):
        return self._statement_repository

    def commit(self) -> None:
        pass

    def rollback(self) -> None:
        pass


domain = Domain(MockedCommandContext)


@pytest.fixture
def test_client():
    app = FastapiApp(domain)
    return TestClient(app.app)


def test_llm_routes_query_statement(mocker: MockerFixture, test_client: TestClient):
    mocker.patch.object(domain, "query_llm", return_value="C'est noté !")
    response = test_client.post("/query", params={"user_prompt": "I am a statement."})
    assert response.status_code == 200
    assert response.json() == "C'est noté !"


def test_llm_routes_query_question(mocker: MockerFixture, test_client: TestClient):
    mocker.patch.object(domain, "query_llm", return_value="A question is the opposite of a statement.")
    response = test_client.post("/query", params={"user_prompt": "What is a question ?"})
    assert response.status_code == 200
    assert response.json() == "A question is the opposite of a statement."
