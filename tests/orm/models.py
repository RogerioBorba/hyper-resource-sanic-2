from sqlalchemy import Column, Date, Integer,Double, String, Engine, Table, select, ForeignKey, Boolean
from geoalchemy2 import Geometry
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import func
from geoalchemy2.functions import _FUNCTIONS
from environs import Env
# Setup env
env = Env()
env.read_env()  # read .env file, if it exists
url_db_test: str = env.str("URL_DB_TEST", "")


class Base(DeclarativeBase):
    __abstract__ = True
    nome: Mapped[str] = mapped_column('nome', String, nullable=False)

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.name}"

class Lake(Base):
    __tablename__ = 'lake'
    id: Mapped[int] = mapped_column('id_lake', Integer, primary_key=True, nullable=False)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry('POLYGON'), nullable=True)


class LocalResidencia(Base):
    __tablename__ = 'local_residencia'

    id_local_residencia: Mapped[int] = mapped_column('id_local_residencia', Integer, primary_key=True, nullable=False)
    nome_estado: Mapped[str] = mapped_column('nome_estado', String, nullable=True)
    nome_municipio: Mapped[str] = mapped_column('nome_municipio', String, nullable=True)


class Pessoa(Base):
    __tablename__ = 'pessoa'

    data_nascimento: Mapped[Date] = mapped_column('data_nascimento', Date, nullable=True)
    id_pessoa: Mapped[int] = mapped_column('id_pessoa', Integer, primary_key=True, nullable=False)
    cpf: Mapped[str] = mapped_column('cpf', String, nullable=True)
    is_usuario: Mapped[bool] = mapped_column('is_usuario', Boolean, nullable=True)
    senha: Mapped[str] = mapped_column('senha', String, nullable=True)
    email: Mapped[str] = mapped_column('email', String, nullable=True)
    id_local_residencia: Mapped[int] = mapped_column('id_local_residencia', Integer, ForeignKey('local_residencia.id_local_residencia'), nullable=True)
    local_residencia: Mapped['LocalResidencia'] = relationship('LocalResidencia', foreign_keys=[id_local_residencia])


class Gasto(Base):
    __tablename__ = 'gasto'

    id_gasto: Mapped[int] = mapped_column('id_gasto', Integer, primary_key=True, nullable=False)
    valor: Mapped[float] = mapped_column('valor', Double, nullable=False)
    data: Mapped[Date] = mapped_column('data', Date, nullable=False)
    id_pessoa: Mapped[int] = mapped_column('id_pessoa', Integer, ForeignKey('pessoa.id_pessoa'), nullable=True)
    pessoa: Mapped['Pessoa'] = relationship('Pessoa', foreign_keys=[id_pessoa])
    id_tipo_gasto: Mapped[int] = mapped_column('id_tipo_gasto', Integer, ForeignKey('tipo_gasto.id_tipo_gasto'), nullable=False)
    tipo_gasto: Mapped['TipoGasto'] = relationship('TipoGasto', foreign_keys=[id_tipo_gasto])


class Grupo(Base):
    __tablename__ = 'grupo'

    id_grupo: Mapped[int] = mapped_column('id_grupo', Integer, primary_key=True, nullable=False)
    descricao: Mapped[str] = mapped_column('descricao', String, nullable=True)


class PessoaGrupo(Base):
    __tablename__ = 'pessoa_grupo'

    id_pessoa_grupo: Mapped[int] = mapped_column('id_pessoa_grupo', Integer, primary_key=True, nullable=False)
    id_grupo: Mapped[int] = mapped_column('id_grupo', Integer, ForeignKey('grupo.id_grupo'), nullable=False)
    grupo: Mapped['Grupo'] = relationship('Grupo', foreign_keys=[id_grupo])
    id_pessoa: Mapped[int] = mapped_column('id_pessoa', Integer, ForeignKey('pessoa.id_pessoa'), nullable=False)
    pessoa: Mapped['Pessoa'] = relationship('Pessoa', foreign_keys=[id_pessoa])
    data_entrada: Mapped[Date] = mapped_column('data_entrada', Date, nullable=True)


class TipoGasto(Base):
    __tablename__ = 'tipo_gasto'

    id_tipo_gasto: Mapped[int] = mapped_column('id_tipo_gasto', Integer, primary_key=True, nullable=False)
    descricao: Mapped[str] = mapped_column('descricao', String, nullable=False)
    id_tipo_gasto_pai: Mapped[int] = mapped_column('id_tipo_gasto_pai', Integer, ForeignKey('tipo_gasto.id_tipo_gasto'), nullable=True)
    tipo_gasto_pai: Mapped['TipoGasto'] = relationship('TipoGasto', foreign_keys=[id_tipo_gasto_pai])


class PalavraChave(Base):
    __tablename__ = 'palavra_chave'

    id: Mapped[int] = mapped_column('id_palavra_chave', Integer, primary_key=True, nullable=False)
    descricao: Mapped[str] = mapped_column('descricao', String, nullable=True)
    id_palavra_chave_superior: Mapped[int] = mapped_column('id_palavra_chave_superior', Integer, ForeignKey('palavra_chave.id_palavra_chave'), nullable=True)
    palavra_chave_superior: Mapped['PalavraChave'] = relationship('PalavraChave', foreign_keys=[id_palavra_chave_superior])
    identificador_recurso: Mapped[str] = mapped_column('identificador_recurso', String, nullable=True)


def new_engine() -> Engine:
    url_db: str = 'postgresql://postgres:desenv@127.0.0.1:5432/postgis'
    return create_engine(url_db_test, echo=True)


def drop_table_from(model: Base, engine) -> None:
    inspector = inspect(engine)
    if model.__table__.name in inspector.get_table_names():
        model.__table__.drop(engine)
        return
    print(f"Tabel {model.__table__.name} does not exist")


def drop_table_from(model: Base, engine) -> None:
    inspector = inspect(engine)
    if model.__table__.name not in inspector.get_table_names():
        print(f"Tabel {model.__table__.name} has already dropped before.")
        return
    model.__table__.drop(engine)


def create_table_from(model: Base, engine) -> None:
    inspector = inspect(engine)
    if model.__table__.name in inspector.get_table_names():
        print(f"Tabel {model.__table__.name} has already created before.")
        return
    model.__table__.create(engine)


def drop_tables(engine) -> None:
    drop_table_from(Lake, engine)
    drop_table_from(Gasto, engine)
    drop_table_from(TipoGasto, engine)
    drop_table_from(LocalResidencia, engine)
    drop_table_from(Pessoa, engine)
    drop_table_from( PessoaGrupo, engine )
    drop_table_from(Grupo, engine)
    drop_table_from(PalavraChave, engine)


def create_tables(engine) -> None:
    create_table_from(Lake, engine)
    create_table_from(TipoGasto, engine)
    create_table_from(LocalResidencia, engine)
    create_table_from(Pessoa, engine)
    create_table_from(Gasto, engine)
    create_table_from(Grupo, engine)
    create_table_from(PessoaGrupo, engine)
    create_table_from(PalavraChave, engine)


def create_lake_instances(engine) -> list[Base]:
    lake = Lake(name='Majeur', geom='POLYGON((0 0,1 0,1 1,0 1,0 0))')
    lista = [lake]
    lake = Lake(name='David', geom='POLYGON((0 0,1 0,1 1,0 1,0 0))')
    lista.append(lake)
    lake = Lake(name='Garde', geom='POLYGON((1 0,3 0,3 2,1 2,1 0))')
    lista.append(lake)
    lake = Lake(name='Orta', geom='POLYGON((3 0,6 0,6 3,3 3,3 0))')
    lista.append(lake)
    return lista


def create_tipo_gasto_instances(engine) -> list[Base]:
    tg = TipoGasto(descricao='Saúde')
    lista = [tg]
    tg1 = TipoGasto(descricao='Remédio')
    tg1.tipo_gasto_pai(tg)
    return lista

def create_instances(engine) -> list[Base]:
    lista: [Base] = []
    lista.extend(create_lake_instances(engine))
    lista.append(create_tipo_gasto_instances(engine))
    return lista

def persist_instances_in_db(instances: list[Base], engine: Engine) -> None:
    with Session(engine) as session:
        for a_model in instances:
            sel = select(a_model.__class__)
            model_instances = session.scalars(sel).all()
            if a_model.name not in [insta.name for insta in model_instances]:
                session.add(a_model)
                session.commit()


def query_in_lake(engine: Engine) -> None:
    with Session(engine) as session:
        #sel = select(Lake).where(func.ST_Contains(Lake.geom, 'POINT(4 1)'))
        print("Contains point(4 1)")
        sel = select(Lake).where(Lake.geom.ST_Contains('POINT(4 1)'))
        result = session.scalars(sel)
        for a_model in result:
            print(a_model)

        print("Intersects linestring(2 1, 4 1)")
        sel = select(Lake).where(Lake.geom.ST_Intersects('LINESTRING(2 1,4 1)'))
        result = session.scalars(sel)
        for a_model in result:
            print(a_model)

        print("Name and area from buffer equal 2")
        #sel = select(Lake.name, func.ST_Area(func.ST_Buffer(Lake.geom, 2)).label('bufferarea'))
        sel = select(Lake.name, Lake.geom.ST_Buffer(2).ST_Area().label('bufferarea'))
        result = session.execute(sel)
        for row in result:
            print(f"{row.name}, {row.bufferarea:.2f}")
        s = select(Lake)
        print(s)
def query_instances(engine: Engine):
    query_in_lake(engine)

def main():

    engine: Engine = new_engine()
    create_tables(engine)
    """instances = create_instances(engine)
    persist_instances_in_db(instances, engine)
    query_instances(engine)
"""

if __name__ == "__main__":
    main()
    l_ordenada = sorted(_FUNCTIONS, key=lambda x: x[0])
    for item in l_ordenada:
        print(item)