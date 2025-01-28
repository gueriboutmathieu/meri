import os

from meri.config.postgresql_config import PostgresqlConfig


def test_postgresql_config():  # pyright: ignore  # noqa: F811
    os.environ["SQL_USER"] = "user"
    os.environ["SQL_PASSWORD"] = "password"
    os.environ["SQL_HOST"] = "localhost"
    os.environ["SQL_PORT"] = "5432"
    os.environ["SQL_DATABASE"] = "meri"


    postgresql_config = PostgresqlConfig()
    assert postgresql_config.sql_user == "user"
    assert postgresql_config.sql_password == "password"
    assert postgresql_config.sql_host == "localhost"
    assert postgresql_config.sql_port == 5432
    assert postgresql_config.sql_database == "meri"
