import uvicorn

from meri.config.postgres_config import PostgresConfig
from meri.domain.domain import Domain
from meri.fastapi.fastapi_app import FastapiApp
from python_utils.sqlalchemy_postgresql_engine_wrapper import SqlAlchemyPostgresqlEngineWrapper


postgres_config = PostgresConfig()
sqlalchemy_postgresql_engine_wrapper = SqlAlchemyPostgresqlEngineWrapper(
    sql_user=postgres_config.sql_user,
    sql_password=postgres_config.sql_password,
    sql_host=postgres_config.sql_host,
    sql_port=postgres_config.sql_port,
    sql_database=postgres_config.sql_database,
    pool_size=5,
)


class CommandContext:
    def __init__(self):
        self.sqlalchemy_session = sqlalchemy_postgresql_engine_wrapper.create_session()
    
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
