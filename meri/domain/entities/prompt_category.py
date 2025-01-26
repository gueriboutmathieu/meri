from enum import Enum


class PromptCategory(str, Enum):
    QUESTION = "question"
    STATEMENT = "statement"
