# -*- coding: latin-1 -*-
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Integer,String
from geoalchemy2.types import Geometry
from src.orm.geo_models import AlchemyGeoBase


class AglomeradoRuralIsoladoP(AlchemyGeoBase): 
    __tablename__ = 'loc_aglomerado_rural_isolado_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    tipoaglomrurisol: Mapped[str] = mapped_column('tipoaglomrurisol', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry('POINT'), nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)
