from openai import OpenAI


class EmbeddingService:
    def __init__(self, api_key: str, model: str, vector_dimensions: int) -> None:
        self.api_key = api_key
        self.model = model
        self.vector_dimensions = vector_dimensions
        self.client = OpenAI(api_key=api_key)

    def embed(self, statement: str) -> list[float]:
        response = self.client.embeddings.create(
            model=self.model,
            input=[statement],
            dimensions=self.vector_dimensions,
        )
        return response.data[0].embedding
