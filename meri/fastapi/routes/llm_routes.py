from fastapi import FastAPI
from meri.domain.domain import Domain


def load_routes(fastapi_app: FastAPI, domain: Domain):
    @fastapi_app.post("/query")
    async def query_llm(prompt: str):  # pyright: ignore[reportUnusedFunction]
        return domain.query_llm(prompt)
