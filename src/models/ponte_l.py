# -*- coding: latin-1 -*-
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Integer,String,Double
from geoalchemy2.types import Geometry
from src.orm.geo_models import AlchemyGeoBase


class PonteL(AlchemyGeoBase): 
    __tablename__ = 'tra_ponte_l'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    tipoponte: Mapped[str] = mapped_column('tipoponte', String, nullable=True)
    modaluso: Mapped[str] = mapped_column('modaluso', String, nullable=True)
    situacaofisica: Mapped[str] = mapped_column('situacaofisica', String, nullable=True)
    operacional: Mapped[str] = mapped_column('operacional', String, nullable=True)
    matconstr: Mapped[str] = mapped_column('matconstr', String, nullable=True)
    vaolivrehoriz: Mapped[float] = mapped_column('vaolivrehoriz', Double, nullable=True)
    vaovertical: Mapped[float] = mapped_column('vaovertical', Double, nullable=True)
    cargasuportmaxima: Mapped[float] = mapped_column('cargasuportmaxima', Double, nullable=True)
    nrpistas: Mapped[int] = mapped_column('nrpistas', Integer, nullable=True)
    nrfaixas: Mapped[int] = mapped_column('nrfaixas', Integer, nullable=True)
    extensao: Mapped[float] = mapped_column('extensao', Double, nullable=True)
    largura: Mapped[float] = mapped_column('largura', Double, nullable=True)
    posicaopista: Mapped[str] = mapped_column('posicaopista', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry('LINESTRING'), nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)
