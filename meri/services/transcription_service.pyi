from _typeshed import Incomplete

class TranscriptionService:
    api_key: Incomplete
    model: Incomplete
    client: Incomplete
    def __init__(self, api_key: str, model: str) -> None: ...
    def transcribe(self, audio_bytes: bytes) -> str: ...
