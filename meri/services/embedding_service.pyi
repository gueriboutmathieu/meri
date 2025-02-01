from _typeshed import Incomplete

class EmbeddingService:
    api_key: Incomplete
    model: Incomplete
    vector_dimensions: Incomplete
    client: Incomplete
    def __init__(self, api_key: str, model: str, vector_dimensions: int) -> None: ...
    def embed(self, statement: str) -> list[float]: ...
