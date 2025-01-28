import os

from pathlib import Path

from meri.config.vector_config import VectorConfig


def test_vector_config():
    os.environ["VECTOR_DIMENSIONS"] = "1536"
    os.environ["VECTOR_DATABASE_FILE_PATH"] = "vector_database.bin"

    vector_config = VectorConfig()
    assert vector_config.vector_dimensions == 1536
    assert vector_config.vector_database_file_path == Path("vector_database.bin")
