from _typeshed import Incomplete
from meri.config.openai_config import OpenaiConfig as OpenaiConfig
from meri.config.postgresql_config import PostgresqlConfig as PostgresqlConfig
from meri.config.vector_config import VectorConfig as VectorConfig
from meri.domain.domain import Domain as Domain
from meri.repositories.statement_repository import StatementRepository as StatementRepository
from meri.routes.fastapi_app import FastapiApp as FastapiApp
from meri.services.embedding_service import EmbeddingService as EmbeddingService
from meri.services.llm_service import LlmService as LlmService

logger: Incomplete
openai_config: Incomplete
postgresql_config: Incomplete
vector_config: Incomplete
embedding_service: Incomplete
llm_service: Incomplete
sqlalchemy_postgresql_engine_wrapper: Incomplete
sqlalchemy_session: Incomplete
statement_repository: Incomplete

class CommandContext:
    sqlalchemy_session: Incomplete
    statement_repository: Incomplete
    llm_service: Incomplete
    embedding_service: Incomplete
    def __init__(self) -> None: ...
    def commit(self) -> None: ...
    def rollback(self) -> None: ...

bound_domain: Incomplete
fastapi_app: Incomplete

def run_server() -> None: ...
