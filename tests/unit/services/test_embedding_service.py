import pytest
from openai import OpenAI
from openai.types.create_embedding_response import CreateEmbeddingResponse, Usage
from openai.types.embedding import Embedding
from pytest_mock import MockerFixture

from meri.services.embedding_service import EmbeddingService


@pytest.fixture
def embedding_service() -> EmbeddingService:
    return EmbeddingService("api_key", "model", 1)


def test_embedding_service_init(embedding_service: EmbeddingService):
    assert embedding_service.api_key == "api_key"
    assert embedding_service.model == "model"
    assert embedding_service.vector_dimensions == 1
    assert type(embedding_service.client) is OpenAI


def test_embedding_service_embed(embedding_service: EmbeddingService, mocker: MockerFixture):
    vector = [1.0, 2.0, 3.0]
    embedding_response = CreateEmbeddingResponse(
        data=[Embedding(embedding=vector, index=0, object="embedding")],
        model="model",
        object="list",
        usage=Usage(prompt_tokens=100, total_tokens=100)
    )
    mocker.patch.object(embedding_service.client.embeddings, "create", return_value=embedding_response)
    assert embedding_service.embed("Statement") == vector
