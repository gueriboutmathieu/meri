from typing import Protocol


class CommandContext(Protocol):
    def rollback(self) -> None:
        ...

    def commit(self) -> None:
        ...


def make_context() -> CommandContext:
    class CC:
        def rollback(self) -> None:
            ...

        def commit(self) -> None:
            ...

    return CC()