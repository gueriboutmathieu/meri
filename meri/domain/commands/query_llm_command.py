from uuid6 import uuid7

from meri.domain.command_context import CommandContext
from meri.domain.entities.prompt_category_enum import PromptCategory
from meri.domain.entities.statement_entity import Statement


def query_llm_command(context: CommandContext, user_prompt: str) -> str:
    category = context.llm_service.categorize(user_prompt)

    match category:
        case PromptCategory.QUESTION:
            vector = context.embedding_service.embed(user_prompt)
            nearest_statements = context.statement_repository.search(vector)
            nearest_statements_contents = [statement.content for statement in nearest_statements]
            llm_response = context.llm_service.ask_about_statements(user_prompt, nearest_statements_contents)
        case PromptCategory.STATEMENT:
            vector = context.embedding_service.embed(user_prompt)
            statement = Statement(id=uuid7(), content=user_prompt, vector=vector)  # pyright: ignore
            context.statement_repository.create(statement)
            context.statement_repository.index_vectors()
            llm_response = "I will remember that."

    return llm_response
