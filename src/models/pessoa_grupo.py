# -*- coding: latin-1 -*-
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Integer,Date
from src.orm.models import AlchemyBase


class PessoaGrupo(AlchemyBase): 
    __tablename__ = 'pessoa_grupo'
    __table_args__ = {'schema': 'pessoal'}

    id_pessoa_grupo: Mapped[int] = mapped_column('id_pessoa_grupo', Integer, primary_key=True, nullable=False)
    id_grupo: Mapped[int] = mapped_column('id_grupo', Integer, ForeignKey('pessoal.grupo.id_grupo'), nullable=False)
    grupo: Mapped['Grupo'] = relationship('Grupo', foreign_keys=[id_grupo])
    id_pessoa: Mapped[int] = mapped_column('id_pessoa', Integer, ForeignKey('pessoal.pessoa.id_pessoa'), nullable=False)
    pessoa: Mapped['Pessoa'] = relationship('Pessoa', foreign_keys=[id_pessoa])
    data_entrada: Mapped[Date] = mapped_column('data_entrada', Date, nullable=True)
