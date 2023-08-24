from sqlalchemy import Engine, create_engine
from environs import Env
# Setup env
env = Env()
env.read_env()  # read .env file, if it exists


def new_engine() -> Engine:
    url_db_test: str = env.str("URL_DB_TEST")
    return create_engine(url_db_test, echo=True)

