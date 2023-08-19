# -*- coding: latin-1 -*-
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Integer,String
from geoalchemy2.types import Geometry
from src.orm.geo_models import AlchemyGeoBase


class UnidadeUsoSustentavelA(AlchemyGeoBase): 
    __tablename__ = 'lim_unidade_uso_sustentavel_a'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    anocriacao: Mapped[int] = mapped_column('anocriacao', Integer, nullable=True)
    sigla: Mapped[str] = mapped_column('sigla', String, nullable=True)
    areaoficial: Mapped[str] = mapped_column('areaoficial', String, nullable=True)
    administracao: Mapped[str] = mapped_column('administracao', String, nullable=True)
    atolegal: Mapped[str] = mapped_column('atolegal', String, nullable=True)
    tipounidusosust: Mapped[str] = mapped_column('tipounidusosust', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry('MULTIPOLYGON'), nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)
