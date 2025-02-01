from _typeshed import Incomplete
from meri.domain.command_context import CommandContext as CommandContext
from meri.domain.commands.query_command import query_command as query_command
from python_utils.domain import CommandContextCreator as CommandContextCreator, Domain as BaseDomain

class Domain(BaseDomain[CommandContext]):
    query_llm: Incomplete
    def __init__(self, command_context_creator: CommandContextCreator[CommandContext]) -> None: ...
