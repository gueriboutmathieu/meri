import pytest
from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletion, Choice
from openai.types.chat.chat_completion_message import ChatCompletionMessage
from pytest_mock import MockerFixture
from meri.domain.entities.prompt_category_enum import PromptCategory

from meri.services.llm_service import LlmService


@pytest.fixture
def llm_service() -> LlmService:
    return LlmService("api_key", "model")


def test_llm_service_init(llm_service: LlmService):
    assert llm_service.api_key == "api_key"
    assert llm_service.model == "model"
    assert type(llm_service.client) is OpenAI


def test_embedding_service_categorize(llm_service: LlmService, mocker: MockerFixture):
    message = ChatCompletionMessage(content="statement", role="assistant")
    choice = Choice(finish_reason="stop", index=0, message=message)
    chat_completion = ChatCompletion(
        id="id",
        choices=[choice],
        created=0,
        model="model",
        object="chat.completion",
    )
    mocker.patch.object(llm_service.client.chat.completions, "create", return_value=chat_completion)
    assert llm_service.categorize("This is a statement") == PromptCategory.STATEMENT


def test_embedding_service_ask_about_statements(llm_service: LlmService, mocker: MockerFixture):
    statement =  "The opposite of a statement."
    message = ChatCompletionMessage(content=statement, role="assistant")
    choice = Choice(finish_reason="stop", index=0, message=message)
    chat_completion = ChatCompletion(
        id="id",
        choices=[choice],
        created=0,
        model="model",
        object="chat.completion",
    )
    mocker.patch.object(llm_service.client.chat.completions, "create", return_value=chat_completion)
    assert llm_service.ask_about_statements("What is a question ?", [statement]) == statement
