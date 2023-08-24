# -*- coding: latin-1 -*-
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Integer,String,Float
from geoalchemy2.types import Geometry
from src.orm.geo_models import AlchemyGeoBase


class TrechoRodoviarioL(AlchemyGeoBase): 
    __tablename__ = 'tra_trecho_rodoviario_l'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    codtrechorodov: Mapped[str] = mapped_column('codtrechorodov', String, nullable=True)
    tipotrechorod: Mapped[str] = mapped_column('tipotrechorod', String, nullable=True)
    jurisdicao: Mapped[str] = mapped_column('jurisdicao', String, nullable=True)
    administracao: Mapped[str] = mapped_column('administracao', String, nullable=True)
    concessionaria: Mapped[str] = mapped_column('concessionaria', String, nullable=True)
    revestimento: Mapped[str] = mapped_column('revestimento', String, nullable=True)
    operacional: Mapped[str] = mapped_column('operacional', String, nullable=True)
    situacaofisica: Mapped[str] = mapped_column('situacaofisica', String, nullable=True)
    nrpistas: Mapped[int] = mapped_column('nrpistas', Integer, nullable=True)
    nrfaixas: Mapped[int] = mapped_column('nrfaixas', Integer, nullable=True)
    trafego: Mapped[str] = mapped_column('trafego', String, nullable=True)
    capaccarga: Mapped[float] = mapped_column('capaccarga', Float, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry('LINESTRING'), nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    canteirodivisorio: Mapped[str] = mapped_column('canteirodivisorio', String, nullable=True)
