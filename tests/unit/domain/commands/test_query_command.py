import pytest  # pyright: ignore  # noqa: F401
from logging import Logger
from pytest_mock import MockerFixture
from sqlalchemy.orm import Session
from uuid6 import uuid7

from meri.domain.commands.query_command import query_command
from meri.domain.command_context import CommandContext
from meri.domain.entities.statement_entity import Statement
from meri.repositories.statement_repository import StatementRepository
from meri.services.embedding_service import EmbeddingService
from meri.services.llm_service import LlmService
from meri.services.transcription_service import TranscriptionService


class MockedCommandContext(CommandContext):
    def __init__(self) -> None:
        self._llm_service = LlmService("", "")
        self._embedding_service = EmbeddingService("", "", 0)
        self._statement_repository = StatementRepository(Session(), Logger(__name__))
        self._transcription_service = TranscriptionService("", "")

    @property
    def llm_service(self):
        return self._llm_service

    @property
    def embedding_service(self):
        return self._embedding_service

    @property
    def statement_repository(self):
        return self._statement_repository

    @property
    def transcription_service(self):
        return self._transcription_service

    def commit(self) -> None:
        pass

    def rollback(self) -> None:
        pass


def test_query_llm_command_statement(mocker: MockerFixture):
    context = MockedCommandContext()
    mocker.patch.object(context.transcription_service, "transcribe", return_value="What is a question ?")
    mocker.patch.object(context.llm_service, "categorize", return_value="statement")
    mocker.patch.object(context.embedding_service, "embed", return_value=[0.0])
    mocker.patch.object(context.statement_repository, "create")
    mocker.patch.object(context.statement_repository, "index_vectors")
    user_prompt = b"I am a statement."
    llm_response = query_command(context, user_prompt)
    assert llm_response == "C'est noté !"


def test_query_llm_command_question(mocker: MockerFixture):
    context = MockedCommandContext()
    mocker.patch.object(context.transcription_service, "transcribe", return_value="What is a question ?")
    mocker.patch.object(context.llm_service, "categorize", return_value="question")
    statement = Statement(id=uuid7(), content="A question is the opposite of a statement.", vector=[0.0])
    mocker.patch.object(context.embedding_service, "embed", return_value=[0.0])
    mocker.patch.object(context.statement_repository, "search", return_value=[statement])
    mocker.patch.object(context.llm_service, "ask_about_statements", return_value="A question is the opposite of a statement.")
    user_prompt = b"What is a question ?"
    llm_response = query_command(context, user_prompt)
    assert llm_response == "A question is the opposite of a statement."
