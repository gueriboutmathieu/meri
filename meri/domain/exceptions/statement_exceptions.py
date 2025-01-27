class StatementNotFoundException(Exception):
    def __init__(self, message: str = "Statement not found") -> None:
        super().__init__(message)


class StatementConstraintException(Exception):
    def __init__(self, message: str = "Statement constraint exception") -> None:
        super().__init__(message)
