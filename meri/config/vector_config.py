from pathlib import Path

from python_utils.env_vars import EnvVar


class VectorConfig:
    def __init__(self) -> None:
        self.vector_dimensions = EnvVar[int]("VECTOR_DIMENSIONS", cast_fct=int).value
        self.vector_database_file_path = EnvVar[Path]("VECTOR_DATABASE_FILE_PATH", cast_fct=Path).value
