from typing import Protocol

from meri.domain.command_context import CommandContext
from python_utils.domain import CommandContextCreator, Domain as BaseDomain


class DomainCommandContext(CommandContext, Protocol):
    pass


class Domain(BaseDomain[CommandContext]):
    def __init__(
        self, command_context_creator: CommandContextCreator[DomainCommandContext]
    ) -> None:
        super().__init__(command_context_creator)
