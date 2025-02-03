from typing import Protocol

from meri.repositories.statement_repository import StatementRepository
from meri.services.embedding_service import EmbeddingService
from meri.services.llm_service import LlmService


class CommandContext(Protocol):
    @property
    def embedding_service(self) -> EmbeddingService:
        ...

    @property
    def llm_service(self) -> LlmService:
        ...

    @property
    def statement_repository(self) -> StatementRepository:
        ...

    def commit(self) -> None:
        ...

    def rollback(self) -> None:
        ...


def make_context(
    embedding_service: EmbeddingService,
    llm_service: LlmService,
    statement_repository: StatementRepository,
) -> CommandContext:
    class CC:
        def __init__(self) -> None:
            self.llm_service = llm_service
            self.embedding_service = embedding_service
            self.statement_repository = statement_repository

        def commit(self) -> None:
            ...

        def rollback(self) -> None:
            ...

    return CC()
