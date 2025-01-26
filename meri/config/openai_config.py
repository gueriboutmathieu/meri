from python_utils.env_vars import EnvVar


class OpenaiConfig:
    def __init__(self) -> None:
        self.openai_api_key = EnvVar[str]("OPENAI_API_KEY", cast_fct=str).value
        self.model = EnvVar[str]("OPENAI_MODEL", cast_fct=str).value
