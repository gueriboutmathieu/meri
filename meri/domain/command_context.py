from typing import Protocol

from meri.services.llm import Llm


class CommandContext(Protocol):
    @property
    def llm(self) -> Llm:
        ...

    def rollback(self) -> None:
        ...

    def commit(self) -> None:
        ...


def make_context(llm: Llm) -> CommandContext:
    class CC:
        def __init__(self) -> None:
            self.llm = llm

        def rollback(self) -> None:
            ...

        def commit(self) -> None:
            ...

    return CC()
