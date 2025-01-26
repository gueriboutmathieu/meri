from fastapi import FastAPI
from meri.domain.domain import Domain


def load_routes(fastapi_app: FastAPI, domain: Domain):
    @fastapi_app.post("/llm/ask")
    async def ask_llm(user_prompt: str):  # pyright: ignore[reportUnusedFunction]
        return domain.ask_llm(user_prompt)
