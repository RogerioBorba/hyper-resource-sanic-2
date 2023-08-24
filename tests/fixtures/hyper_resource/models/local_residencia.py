# -*- coding: latin-1 -*-
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Integer,String
from src.orm.models import AlchemyBase


class LocalResidencia(AlchemyBase): 
    __tablename__ = 'local_residencia'
    __table_args__ = {'schema': 'pessoal'}

    id_local_residencia: Mapped[int] = mapped_column('id_local_residencia', Integer, primary_key=True, nullable=False)
    nome_estado: Mapped[str] = mapped_column('nome_estado', String, nullable=True)
    nome_municipio: Mapped[str] = mapped_column('nome_municipio', String, nullable=True)
