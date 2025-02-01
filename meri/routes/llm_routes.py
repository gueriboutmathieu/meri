from fastapi import FastAPI, File, UploadFile  # pyright: ignore[reportUnknownVariableType]

from meri.domain.domain import Domain


def load_routes(fastapi_app: FastAPI, domain: Domain):
    @fastapi_app.post("/query")
    async def query(file: UploadFile = File(...)):  # pyright: ignore[reportUnusedFunction]
        audio_bytes = await file.read()
        return domain.query_llm(audio_bytes)
