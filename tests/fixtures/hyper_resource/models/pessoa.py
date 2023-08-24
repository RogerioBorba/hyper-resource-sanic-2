# -*- coding: latin-1 -*-
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String,Date,Integer,Boolean
from src.orm.models import AlchemyBase


class Pessoa(AlchemyBase): 
    __tablename__ = 'pessoa'
    __table_args__ = {'schema': 'pessoal'}

    nome: Mapped[str] = mapped_column('nome', String, nullable=False)
    data_nascimento: Mapped[Date] = mapped_column('data_nascimento', Date, nullable=True)
    id_pessoa: Mapped[int] = mapped_column('id_pessoa', Integer, primary_key=True, nullable=False)
    cpf: Mapped[str] = mapped_column('cpf', String, nullable=True)
    is_usuario: Mapped[bool] = mapped_column('is_usuario', Boolean, nullable=True)
    senha: Mapped[str] = mapped_column('senha', String, nullable=True)
    email: Mapped[str] = mapped_column('email', String, nullable=True)
    #id_local_residencia: Mapped[int] = mapped_column('id_local_residencia', Integer, ForeignKey('pessoal.local_residencia.id_local_residencia'), nullable=True)
    #local_residencia: Mapped['tests.fixtures.hyper_resource.models.LocalResidencia'] = relationship('LocalResidencia', foreign_keys=[id_local_residencia])
