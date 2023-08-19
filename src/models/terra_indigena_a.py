# -*- coding: latin-1 -*-
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Integer,String,Double
from geoalchemy2.types import Geometry
from src.orm.geo_models import AlchemyGeoBase


class TerraIndigenaA(AlchemyGeoBase): 
    __tablename__ = 'lim_terra_indigena_a'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    perimetrooficial: Mapped[float] = mapped_column('perimetrooficial', Double, nullable=True)
    areaoficialha: Mapped[float] = mapped_column('areaoficialha', Double, nullable=True)
    grupoetnico: Mapped[str] = mapped_column('grupoetnico', String, nullable=True)
    datasituacaojuridica: Mapped[str] = mapped_column('datasituacaojuridica', String, nullable=True)
    situacaojuridica: Mapped[str] = mapped_column('situacaojuridica', String, nullable=True)
    nometi: Mapped[str] = mapped_column('nometi', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry('MULTIPOLYGON'), nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    codigofunai: Mapped[int] = mapped_column('codigofunai', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)
