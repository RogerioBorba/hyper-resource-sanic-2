# -*- coding: latin-1 -*-
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Integer,String
from geoalchemy2.types import Geometry
from src.orm.geo_models import AlchemyGeoBase


class ExtMineralP(AlchemyGeoBase): 
    __tablename__ = 'eco_ext_mineral_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    tiposecaocnae: Mapped[str] = mapped_column('tiposecaocnae', String, nullable=True)
    operacional: Mapped[str] = mapped_column('operacional', String, nullable=True)
    situacaofisica: Mapped[str] = mapped_column('situacaofisica', String, nullable=True)
    tipoextmin: Mapped[str] = mapped_column('tipoextmin', String, nullable=True)
    tipoprodutoresiduo: Mapped[str] = mapped_column('tipoprodutoresiduo', String, nullable=True)
    tipopocomina: Mapped[str] = mapped_column('tipopocomina', String, nullable=True)
    procextracao: Mapped[str] = mapped_column('procextracao', String, nullable=True)
    formaextracao: Mapped[str] = mapped_column('formaextracao', String, nullable=True)
    atividade: Mapped[str] = mapped_column('atividade', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry('POINT'), nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)
