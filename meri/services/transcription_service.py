from uuid6 import uuid7
from pathlib import Path
from openai import OpenAI


class TranscriptionService:
    def __init__(self, api_key: str, model: str) -> None:
        self.api_key = api_key
        self.model = model
        self.client = OpenAI(api_key=api_key)

    def transcribe(self, audio_bytes: bytes) -> str:
        temporary_audio_file = Path(f"/tmp/{uuid7()}.mp3")
        temporary_audio_file.write_bytes(audio_bytes)
        response = self.client.audio.transcriptions.create(
            file=temporary_audio_file,
            model=self.model,
            response_format="text",
            language="fr",
            timeout=60
        )
        temporary_audio_file.unlink()
        return response
