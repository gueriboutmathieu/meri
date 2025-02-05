from meri.domain.command_context import CommandContext as CommandContext
from meri.domain.entities.prompt_category_enum import PromptCategory as PromptCategory
from meri.domain.entities.statement_entity import Statement as Statement

def query_command(context: CommandContext, user_prompt: str) -> str: ...
