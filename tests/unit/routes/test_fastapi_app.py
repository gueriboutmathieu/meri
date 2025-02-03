import importlib.metadata
import pytest  # pyright: ignore  # noqa: F401
from logging import Logger
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



def test_fastapi_app():
    app = FastapiApp(Domain(MockedCommandContext))
    assert app.app.version == importlib.metadata.version("meri")
    expected_routes = ["/", "/health", "/force_exception", "/query"]
    assert set(expected_routes) <= set([route.path for route in app.app.routes])  # pyright: ignore
