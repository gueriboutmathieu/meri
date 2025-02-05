from _typeshed import Incomplete
from meri.domain.entities.prompt_category_enum import PromptCategory as PromptCategory

class LlmService:
    api_key: Incomplete
    model: Incomplete
    client: Incomplete
    def __init__(self, api_key: str, model: str) -> None: ...
    def categorize(self, user_prompt: str) -> PromptCategory: ...
    def ask_about_statements(self, question: str, statements: list[str]) -> str: ...
