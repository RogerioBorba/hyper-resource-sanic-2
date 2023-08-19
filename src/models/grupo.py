# -*- coding: latin-1 -*-
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Integer,String
from src.orm.models import AlchemyBase


class Grupo(AlchemyBase): 
    __tablename__ = 'grupo'
    __table_args__ = {'schema': 'pessoal'}

    id_grupo: Mapped[int] = mapped_column('id_grupo', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=False)
    descricao: Mapped[str] = mapped_column('descricao', String, nullable=True)
