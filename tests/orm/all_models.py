# -*- coding: latin-1 -*-
from sqlalchemy import CHAR, Column, Double, Float, Boolean, Integer, Numeric, SmallInteger, String, Text, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql.sqltypes import NullType

from geoalchemy2 import Geometry

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    __abstract__ = True

class AlchemyBase(Base):
    __abstract__ = True

class GeoAlchemyBase(AlchemyBase):
    __abstract__ = True


class LocalResidencia(AlchemyBase):
    __tablename__ = 'local_residencia'

    id_local_residencia: Mapped[int] = mapped_column('id_local_residencia', Integer, primary_key=True, nullable=False)
    nome_estado: Mapped[str] = mapped_column('nome_estado', String, nullable=True)
    nome_municipio: Mapped[str] = mapped_column('nome_municipio', String, nullable=True)


class Pessoa(AlchemyBase):
    __tablename__ = 'pessoa'

    nome: Mapped[str] = mapped_column('nome', String, nullable=False)
    data_nascimento: Mapped[Date] = mapped_column('data_nascimento', Date, nullable=True)
    id_pessoa: Mapped[int] = mapped_column('id_pessoa', Integer, primary_key=True, nullable=False)
    cpf: Mapped[str] = mapped_column('cpf', String, nullable=True)
    is_usuario: Mapped[bool] = mapped_column('is_usuario', Boolean, nullable=True)
    senha: Mapped[str] = mapped_column('senha', String, nullable=True)
    email: Mapped[str] = mapped_column('email', String, nullable=True)
    id_local_residencia: Mapped[int] = mapped_column('id_local_residencia', Integer, ForeignKey('local_residencia.id_local_residencia'), nullable=True)
    local_residencia: Mapped['LocalResidencia'] = relationship('LocalResidencia', foreign_keys=[id_local_residencia])


class TipoGasto(AlchemyBase):
    __tablename__ = 'tipo_gasto'

    id_tipo_gasto: Mapped[int] = mapped_column('id_tipo_gasto', Integer, primary_key=True, nullable=False)
    descricao: Mapped[str] = mapped_column('descricao', String, nullable=False)
    id_tipo_gasto_pai: Mapped[int] = mapped_column('id_tipo_gasto_pai', Integer, ForeignKey('tipo_gasto.id_tipo_gasto_pai'), nullable=True)
    tipo_gasto_pai: Mapped['TipoGasto'] = relationship('TipoGasto', foreign_keys=[id_tipo_gasto_pai])


class Gasto(AlchemyBase):
    __tablename__ = 'gasto'

    id_gasto: Mapped[int] = mapped_column('id_gasto', Integer, primary_key=True, nullable=False)
    valor: Mapped[float] = mapped_column('valor', Double, nullable=False)
    data: Mapped[Date] = mapped_column('data', Date, nullable=False)
    id_pessoa: Mapped[int] = mapped_column('id_pessoa', Integer, ForeignKey('pessoa.id_pessoa'), nullable=True)
    pessoa: Mapped['Pessoa'] = relationship('Pessoa', foreign_keys=[id_pessoa])
    id_tipo_gasto: Mapped[int] = mapped_column('id_tipo_gasto', Integer, ForeignKey('tipo_gasto.id_tipo_gasto'), nullable=False)
    tipo_gasto: Mapped['TipoGasto'] = relationship('TipoGasto', foreign_keys=[id_tipo_gasto])


class Grupo(AlchemyBase):
    __tablename__ = 'grupo'

    id_grupo: Mapped[int] = mapped_column('id_grupo', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=False)
    descricao: Mapped[str] = mapped_column('descricao', String, nullable=True)


class PessoaGrupo(AlchemyBase):
    __tablename__ = 'pessoa_grupo'

    id_pessoa_grupo: Mapped[int] = mapped_column('id_pessoa_grupo', Integer, primary_key=True, nullable=False)
    id_grupo: Mapped[int] = mapped_column('id_grupo', Integer, ForeignKey('grupo.id_grupo'), nullable=False)
    grupo: Mapped['Grupo'] = relationship('Grupo', foreign_keys=[id_grupo])
    id_pessoa: Mapped[int] = mapped_column('id_pessoa', Integer, ForeignKey('pessoa.id_pessoa'), nullable=False)
    pessoa: Mapped['Pessoa'] = relationship('Pessoa', foreign_keys=[id_pessoa])
    data_entrada: Mapped[Date] = mapped_column('data_entrada', Date, nullable=True)


class AldeiaIndigenaP(GeoAlchemyBase):
    __tablename__ = 'aldeia_indigena_p'

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    codigofunai: Mapped[str] = mapped_column('codigofunai', String, nullable=True)
    terraindigena: Mapped[str] = mapped_column('terraindigena', String, nullable=True)
    etnia: Mapped[str] = mapped_column('etnia', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)


