import uvicorn

from meri.config.openai_config import OpenaiConfig
from meri.config.postgresql_config import PostgresqlConfig
from meri.config.vector_config import VectorConfig
from meri.domain.domain import Domain
from meri.repositories.statement_repository import StatementRepository
from meri.services.embedding_service import EmbeddingService
from meri.services.llm_service import LlmService
from meri.fastapi.fastapi_app import FastapiApp
from python_utils.loggers import get_logger
from python_utils.sqlalchemy_postgresql_engine_wrapper import SqlAlchemyPostgresqlEngineWrapper


# Logger
logger = get_logger(__name__)


# Configs
openai_config = OpenaiConfig()
postgresql_config = PostgresqlConfig()
vector_config = VectorConfig()


# Services
embedding_service = EmbeddingService(
    api_key=openai_config.openai_api_key,
    model=openai_config.embedding_model,
    vector_dimensions=vector_config.vector_dimensions
)
llm_service = LlmService(api_key=openai_config.openai_api_key, model=openai_config.llm_model)


# SQLAlchemyEngineWrapper
sqlalchemy_postgresql_engine_wrapper = SqlAlchemyPostgresqlEngineWrapper(
    sql_user=postgresql_config.sql_user,
    sql_password=postgresql_config.sql_password,
    sql_host=postgresql_config.sql_host,
    sql_port=postgresql_config.sql_port,
    sql_database=postgresql_config.sql_database,
    pool_size=5
)
sqlalchemy_session = sqlalchemy_postgresql_engine_wrapper.create_session()


# Repositories
statement_repository = StatementRepository(session=sqlalchemy_session, logger=logger)


class CommandContext:
    def __init__(self):
        self.sqlalchemy_session = sqlalchemy_session
        self.statement_repository = statement_repository
        self.llm_service = llm_service
        self.embedding_service = embedding_service

    def commit(self):
        self.sqlalchemy_session.commit()

    def rollback(self):
        self.sqlalchemy_session.rollback()



bound_domain = Domain(CommandContext)
fastapi_app = FastapiApp(bound_domain)


def run_server():
    uvicorn.run(fastapi_app.app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    run_server()
