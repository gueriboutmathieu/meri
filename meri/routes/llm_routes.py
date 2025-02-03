from fastapi import FastAPI  # pyright: ignore[reportUnknownVariableType]

from meri.domain.domain import Domain


def load_routes(fastapi_app: FastAPI, domain: Domain):
    @fastapi_app.post("/query")
    async def query(user_prompt: str):  # pyright: ignore[reportUnusedFunction]
        return domain.query_llm(user_prompt)
