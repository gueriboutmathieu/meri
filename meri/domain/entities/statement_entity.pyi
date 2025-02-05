from _typeshed import Incomplete
from meri.config.vector_config import VectorConfig as VectorConfig
from pgvector.sqlalchemy import VECTOR
from python_utils.entity import Entity
from sqlalchemy.orm import Mapped as Mapped
from uuid import UUID as UUID

vector_config: Incomplete

class Statement(Entity):
    __tablename__: str
    __table_args__: Incomplete
    id: Mapped[UUID]
    content: Mapped[str]
    vector: Mapped[VECTOR]
