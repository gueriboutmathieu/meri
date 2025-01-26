from pgvector.sqlalchemy import VECTOR  # pyright: ignore
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID

from meri.config.vector_config import VectorConfig
from python_utils.entity import Entity


vector_config = VectorConfig()


class Statement(Entity):
    __tablename__ = "statements"

    id: Mapped[UUID] = mapped_column(init=True, primary_key=True)
    content: Mapped[str] = mapped_column(init=True)
    vector: Mapped[VECTOR] = mapped_column(VECTOR(dim=vector_config.vector_dimensions), init=True)  # pyright: ignore
