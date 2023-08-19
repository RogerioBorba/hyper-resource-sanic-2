# -*- coding: latin-1 -*-
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Integer,Double,Date
from src.orm.models import AlchemyBase


class Gasto(AlchemyBase): 
    __tablename__ = 'gasto'
    __table_args__ = {'schema': 'pessoal'}

    id_gasto: Mapped[int] = mapped_column('id_gasto', Integer, primary_key=True, nullable=False)
    valor: Mapped[float] = mapped_column('valor', Double, nullable=False)
    data: Mapped[Date] = mapped_column('data', Date, nullable=False)
    id_pessoa: Mapped[int] = mapped_column('id_pessoa', Integer, ForeignKey('pessoal.pessoa.id_pessoa'), nullable=True)
    pessoa: Mapped['Pessoa'] = relationship('Pessoa', foreign_keys=[id_pessoa])
    id_tipo_gasto: Mapped[int] = mapped_column('id_tipo_gasto', Integer, ForeignKey('pessoal.tipo_gasto.id_tipo_gasto'), nullable=False)
    tipo_gasto: Mapped['TipoGasto'] = relationship('TipoGasto', foreign_keys=[id_tipo_gasto])
