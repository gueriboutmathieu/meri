from meri.domain.commands.ask_llm_command import ask_llm_command
from meri.domain.command_context import CommandContext
from python_utils.domain import CommandContextCreator, Domain as BaseDomain



class Domain(BaseDomain[CommandContext]):
    def __init__(
        self, command_context_creator: CommandContextCreator[CommandContext]
    ) -> None:
        super().__init__(command_context_creator)

        self.ask_llm = self._bind_command(ask_llm_command)
