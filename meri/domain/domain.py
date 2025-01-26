from meri.domain.commands.query_llm_command import query_llm_command
from meri.domain.command_context import CommandContext
from python_utils.domain import CommandContextCreator, Domain as BaseDomain



class Domain(BaseDomain[CommandContext]):
    def __init__(
        self, command_context_creator: CommandContextCreator[CommandContext]
    ) -> None:
        super().__init__(command_context_creator)

        self.query_llm = self._bind_command(query_llm_command)
