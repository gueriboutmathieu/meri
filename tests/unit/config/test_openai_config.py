import os

from meri.config.openai_config import OpenaiConfig


def test_openai_config():
    os.environ["OPENAI_API_KEY"] = "openai_api_key"
    os.environ["OPENAI_LLM_MODEL"] = "openai_llm_model"
    os.environ["OPENAI_EMBEDDING_MODEL"] = "openai_embedding_model"

    openai_config = OpenaiConfig()
    assert openai_config.openai_api_key == "openai_api_key"
    assert openai_config.llm_model == "openai_llm_model"
    assert openai_config.embedding_model == "openai_embedding_model"
