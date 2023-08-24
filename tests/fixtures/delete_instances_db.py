from sqlalchemy import Engine, select, Select
from sqlalchemy.orm import Session
from engine import new_engine
from tests.fixtures.hyper_resource.models.gasto import Gasto
from tests.fixtures.hyper_resource.models.tipo_gasto import TipoGasto
from tests.fixtures.hyper_resource.models.pessoa import Pessoa
from environs import Env
# Setup env
env = Env()
env.read_env()  # read .env file, if it exists


def delete_tipo_gasto_instances(session: Session) -> None:
    stmt: Select = select(TipoGasto).where(TipoGasto.tipo_gasto_pai is not None)
    for obj in session.scalars(stmt):
        session.delete(obj)
        session.commit()
    stmt: Select = select(TipoGasto)
    for obj in session.scalars(stmt):
        session.delete(obj)
        session.commit()


def delete_pessoa_instances(session) -> list[Pessoa]:
    stmt: Select = select(Pessoa)
    for obj in session.scalars(stmt):
        session.delete(obj)
        session.commit()


def delete_gasto_instances(session: Session) -> None:
    stmt: Select = select(Gasto)
    for obj in session.scalars(stmt):
        session.delete(obj)
        session.commit()


def delete_instances(session: Session) -> None:
    delete_gasto_instances(session)
    delete_tipo_gasto_instances(session)
    delete_pessoa_instances(session)


def main():
    engine: Engine = new_engine()
    with Session(engine) as session:
        delete_instances(session)


if __name__ == "__main__":
    main()
