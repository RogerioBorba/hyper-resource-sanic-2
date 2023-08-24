from sqlalchemy import Engine, select
from engine import new_engine
from sqlalchemy.orm import Session

from tests.fixtures.hyper_resource.models.gasto import Gasto
from tests.fixtures.hyper_resource.models.tipo_gasto import TipoGasto
from tests.fixtures.hyper_resource.models.pessoa import Pessoa
from environs import Env
# Setup env
env = Env()
env.read_env()  # read .env file, if it exists


def tipo_gasto_instances(session: Session) -> list:
    saude = TipoGasto(descricao='Saúde')
    session.add(saude)
    lista = [saude]
    remedio = TipoGasto(descricao='Remédio', tipo_gasto_pai=saude)
    session.add(remedio)
    lista.append(remedio)
    session.commit()
    nyteb = TipoGasto(descricao='Nyteb', tipo_gasto_pai=remedio)
    session.add(nyteb)
    lista.append(nyteb)
    session.commit()
    educacao = TipoGasto(descricao='Educação')
    session.add(educacao)
    lista.append(educacao)
    habitacao = TipoGasto(descricao='Habitação')
    session.add(habitacao)
    lista.append(habitacao)
    condominio = TipoGasto(descricao='Condomínio', tipo_gasto_pai=habitacao)
    session.add(condominio)
    lista.append(condominio)
    transporte = TipoGasto(descricao='Transporte')
    session.add(transporte)
    lista.append(transporte)
    alimentacao = TipoGasto(descricao='Alimentação')
    session.add(alimentacao)
    lista.append(alimentacao)
    session.commit()
    supermercado = TipoGasto(descricao='Supermercado', tipo_gasto_pai=alimentacao)
    session.add(supermercado)
    lista.append(supermercado)
    session.commit()
    lazer = TipoGasto(descricao='Lazer')
    session.add(lazer)
    lista.append(lazer)
    session.commit()
    cinema = TipoGasto(descricao='Cinema', tipo_gasto_pai=lazer)
    session.add(cinema)
    lista.append(cinema)
    session.commit()
    return lista


def pessoa_instances(session: Session) -> list[Pessoa]:
    lista = [Pessoa(nome='João Borges', data_nascimento='2000-01-01', email='jm123@gmail.com'),
             Pessoa(nome='Maria Clara Borges', data_nascimento='2001-01-01', email='mcb123@gmail.com'),
             Pessoa(nome='Lara Borges', data_nascimento='2011-01-01', email='lb123@gmail.com'),
             Pessoa(nome='Luiz Borges', data_nascimento='2011-01-01', email='lb123456@gmail.com')]
    session.add_all(lista)
    session.commit()
    return lista


def gasto_instances(session: Session) -> list:
    lista = []
    stmt = select(TipoGasto).where(TipoGasto.descricao == 'Nyteb')
    tipo_gasto_nytb = session.scalar(stmt)
    stmt2 = select(Pessoa).where(Pessoa.nome == 'João Borges')
    pessoa_jb = session.scalar(stmt2)
    print(tipo_gasto_nytb)
    gasto = Gasto(data="2023-07-23", valor=53.40, tipo_gasto=tipo_gasto_nytb, pessoa=pessoa_jb)
    session.add(gasto)
    lista.append(gasto)
    stmt3 = select(TipoGasto).where(TipoGasto.descricao == 'Supermercado')
    tipo_gasto_super = session.scalar(stmt3)
    gasto1 = Gasto(data="2023-07-23", valor=1570.00, tipo_gasto=tipo_gasto_super, pessoa=pessoa_jb)
    session.add(gasto1)
    lista.append(gasto1)
    session.commit()
    stmt4 = select(Pessoa).where(Pessoa.nome == 'Maria Clara Borges')
    pessoa_mcb = session.scalar(stmt4)
    stmt5 = select(TipoGasto).where(TipoGasto.descricao == 'Cinema')
    tipo_gasto_cinema = session.scalar(stmt5)
    gasto2 = Gasto(data="2023-08-20", valor=190.00, tipo_gasto=tipo_gasto_cinema, pessoa=pessoa_mcb)
    session.add(gasto2)
    lista.append(gasto2)
    session.commit()
    return lista


def create_instances(session: Session) -> list:
    lista = []
    lista.extend(pessoa_instances(session))
    lista.extend(tipo_gasto_instances(session))
    lista.extend(gasto_instances(session))

    return lista


def main():
    engine: Engine = new_engine()
    with Session(engine) as session:
        create_instances(session)


if __name__ == "__main__":
    main()
