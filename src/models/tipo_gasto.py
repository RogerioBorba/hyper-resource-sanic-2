# -*- coding: latin-1 -*-
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Integer,String
from src.orm.models import AlchemyBase


class TipoGasto(AlchemyBase): 
    __tablename__ = 'tipo_gasto'
    __table_args__ = {'schema': 'pessoal'}

    id_tipo_gasto: Mapped[int] = mapped_column('id_tipo_gasto', Integer, primary_key=True, nullable=False)
    descricao: Mapped[str] = mapped_column('descricao', String, nullable=False)
    id_tipo_gasto_pai: Mapped[int] = mapped_column('id_tipo_gasto_pai', Integer, ForeignKey('pessoal.tipo_gasto.id_tipo_gasto'), nullable=True)
    tipo_gasto_pai: Mapped['TipoGasto'] = relationship('TipoGasto', foreign_keys=[id_tipo_gasto_pai])
