# -*- coding: latin-1 -*-
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Integer,String,Double
from geoalchemy2.types import Geometry
from src.orm.geo_models import AlchemyGeoBase


class TrechoDrenagemL(AlchemyGeoBase): 
    __tablename__ = 'hid_trecho_drenagem_l'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    dentrodepoligono: Mapped[str] = mapped_column('dentrodepoligono', String, nullable=True)
    compartilhado: Mapped[str] = mapped_column('compartilhado', String, nullable=True)
    eixoprincipal: Mapped[str] = mapped_column('eixoprincipal', String, nullable=True)
    caladomax: Mapped[float] = mapped_column('caladomax', Double, nullable=True)
    larguramedia: Mapped[float] = mapped_column('larguramedia', Double, nullable=True)
    velocidademedcorrente: Mapped[float] = mapped_column('velocidademedcorrente', Double, nullable=True)
    profundidademedia: Mapped[float] = mapped_column('profundidademedia', Double, nullable=True)
    coincidecomdentrode: Mapped[str] = mapped_column('coincidecomdentrode', String, nullable=True)
    navegabilidade: Mapped[str] = mapped_column('navegabilidade', String, nullable=True)
    regime: Mapped[str] = mapped_column('regime', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry('LINESTRING'), nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)
