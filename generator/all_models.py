from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import Integer,Double,String,Float
from geoalchemy2.types import Geometry
from src.orm.geo_models import AlchemyGeoBase


class ExtMineralA(AlchemyGeoBase): 
    __tablename__ = 'eco_ext_mineral_a'
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
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class EdifPubMilitarA(AlchemyGeoBase): 
    __tablename__ = 'adm_edif_pub_militar_a'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    tipoedifmil: Mapped[str] = mapped_column('tipoedifmil', String, nullable=True)
    tipousoedif: Mapped[str] = mapped_column('tipousoedif', String, nullable=True)
    situacaofisica: Mapped[str] = mapped_column('situacaofisica', String, nullable=True)
    operacional: Mapped[str] = mapped_column('operacional', String, nullable=True)
    matconstr: Mapped[str] = mapped_column('matconstr', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class EdifPubMilitarP(AlchemyGeoBase): 
    __tablename__ = 'adm_edif_pub_militar_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    tipoedifmil: Mapped[str] = mapped_column('tipoedifmil', String, nullable=True)
    tipousoedif: Mapped[str] = mapped_column('tipousoedif', String, nullable=True)
    situacaofisica: Mapped[str] = mapped_column('situacaofisica', String, nullable=True)
    operacional: Mapped[str] = mapped_column('operacional', String, nullable=True)
    matconstr: Mapped[str] = mapped_column('matconstr', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class PostoFiscalP(AlchemyGeoBase): 
    __tablename__ = 'adm_posto_fiscal_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    operacional: Mapped[str] = mapped_column('operacional', String, nullable=True)
    situacaofisica: Mapped[str] = mapped_column('situacaofisica', String, nullable=True)
    tipopostofisc: Mapped[str] = mapped_column('tipopostofisc', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class EdifAgropecExtVegetalPescaP(AlchemyGeoBase): 
    __tablename__ = 'eco_edif_agropec_ext_vegetal_pesca_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    operacional: Mapped[str] = mapped_column('operacional', String, nullable=True)
    situacaofisica: Mapped[str] = mapped_column('situacaofisica', String, nullable=True)
    tipoedifagropec: Mapped[str] = mapped_column('tipoedifagropec', String, nullable=True)
    matconstr: Mapped[str] = mapped_column('matconstr', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


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
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class EstGeradEnergiaEletricaP(AlchemyGeoBase): 
    __tablename__ = 'enc_est_gerad_energia_eletrica_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    codigoestacao: Mapped[str] = mapped_column('codigoestacao', String, nullable=True)
    potenciaoutorgada: Mapped[int] = mapped_column('potenciaoutorgada', Integer, nullable=True)
    potenciafiscalizada: Mapped[int] = mapped_column('potenciafiscalizada', Integer, nullable=True)
    operacional: Mapped[str] = mapped_column('operacional', String, nullable=True)
    situacaofisica: Mapped[str] = mapped_column('situacaofisica', String, nullable=True)
    tipoestgerad: Mapped[str] = mapped_column('tipoestgerad', String, nullable=True)
    destenergelet: Mapped[str] = mapped_column('destenergelet', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class TermeletricaP(AlchemyGeoBase): 
    __tablename__ = 'enc_termeletrica_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    potenciaoutorgada: Mapped[int] = mapped_column('potenciaoutorgada', Integer, nullable=True)
    potenciafiscalizada: Mapped[int] = mapped_column('potenciafiscalizada', Integer, nullable=True)
    combrenovavel: Mapped[str] = mapped_column('combrenovavel', String, nullable=True)
    tipomaqtermica: Mapped[str] = mapped_column('tipomaqtermica', String, nullable=True)
    geracao: Mapped[str] = mapped_column('geracao', String, nullable=True)
    tipocombustivel: Mapped[str] = mapped_column('tipocombustivel', String, nullable=True)
    operacional: Mapped[str] = mapped_column('operacional', String, nullable=True)
    situacaofisica: Mapped[str] = mapped_column('situacaofisica', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class HidreletricaP(AlchemyGeoBase): 
    __tablename__ = 'enc_hidreletrica_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    potenciaoutorgada: Mapped[int] = mapped_column('potenciaoutorgada', Integer, nullable=True)
    potenciafiscalizada: Mapped[int] = mapped_column('potenciafiscalizada', Integer, nullable=True)
    codigohidreletrica: Mapped[str] = mapped_column('codigohidreletrica', String, nullable=True)
    operacional: Mapped[str] = mapped_column('operacional', String, nullable=True)
    situacaofisica: Mapped[str] = mapped_column('situacaofisica', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class BarragemL(AlchemyGeoBase): 
    __tablename__ = 'hid_barragem_l'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    matconstr: Mapped[str] = mapped_column('matconstr', String, nullable=True)
    usoprincipal: Mapped[str] = mapped_column('usoprincipal', String, nullable=True)
    operacional: Mapped[str] = mapped_column('operacional', String, nullable=True)
    situacaofisica: Mapped[str] = mapped_column('situacaofisica', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class BancoAreiaA(AlchemyGeoBase): 
    __tablename__ = 'hid_banco_areia_a'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    tipobanco: Mapped[str] = mapped_column('tipobanco', String, nullable=True)
    situacaoemagua: Mapped[str] = mapped_column('situacaoemagua', String, nullable=True)
    materialpredominante: Mapped[str] = mapped_column('materialpredominante', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class BarragemP(AlchemyGeoBase): 
    __tablename__ = 'hid_barragem_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    matconstr: Mapped[str] = mapped_column('matconstr', String, nullable=True)
    usoprincipal: Mapped[str] = mapped_column('usoprincipal', String, nullable=True)
    operacional: Mapped[str] = mapped_column('operacional', String, nullable=True)
    situacaofisica: Mapped[str] = mapped_column('situacaofisica', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class CorredeiraL(AlchemyGeoBase): 
    __tablename__ = 'hid_corredeira_l'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class CorredeiraP(AlchemyGeoBase): 
    __tablename__ = 'hid_corredeira_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class IlhaA(AlchemyGeoBase): 
    __tablename__ = 'hid_ilha_a'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    tipoilha: Mapped[str] = mapped_column('tipoilha', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class MassaDaguaA(AlchemyGeoBase): 
    __tablename__ = 'hid_massa_dagua_a'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    tipomassadagua: Mapped[str] = mapped_column('tipomassadagua', String, nullable=True)
    salinidade: Mapped[str] = mapped_column('salinidade', String, nullable=True)
    regime: Mapped[str] = mapped_column('regime', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class QuedaDaguaL(AlchemyGeoBase): 
    __tablename__ = 'hid_queda_dagua_l'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    altura: Mapped[float] = mapped_column('altura', Double, nullable=True)
    tipoqueda: Mapped[str] = mapped_column('tipoqueda', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class RecifeA(AlchemyGeoBase): 
    __tablename__ = 'hid_recife_a'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    tiporecife: Mapped[str] = mapped_column('tiporecife', String, nullable=True)
    situamare: Mapped[str] = mapped_column('situamare', String, nullable=True)
    situacaocosta: Mapped[str] = mapped_column('situacaocosta', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class RochaEmAguaA(AlchemyGeoBase): 
    __tablename__ = 'hid_rocha_em_agua_a'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    alturalamina: Mapped[float] = mapped_column('alturalamina', Double, nullable=True)
    situacaoemagua: Mapped[str] = mapped_column('situacaoemagua', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class SumidouroVertedouroP(AlchemyGeoBase): 
    __tablename__ = 'hid_sumidouro_vertedouro_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    causa: Mapped[str] = mapped_column('causa', String, nullable=True)
    tiposumvert: Mapped[str] = mapped_column('tiposumvert', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class TerrenoSujeitoInundacaoA(AlchemyGeoBase): 
    __tablename__ = 'hid_terreno_sujeito_inundacao_a'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    periodicidadeinunda: Mapped[str] = mapped_column('periodicidadeinunda', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


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
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class TrechoMassaDaguaA(AlchemyGeoBase): 
    __tablename__ = 'hid_trecho_massa_dagua_a'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    tipotrechomassa: Mapped[str] = mapped_column('tipotrechomassa', String, nullable=True)
    salinidade: Mapped[str] = mapped_column('salinidade', String, nullable=True)
    regime: Mapped[str] = mapped_column('regime', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class OutrosLimitesOficiaisL(AlchemyGeoBase): 
    __tablename__ = 'lim_outros_limites_oficiais_l'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    coincidecomdentrode: Mapped[str] = mapped_column('coincidecomdentrode', String, nullable=True)
    extensao: Mapped[float] = mapped_column('extensao', Double, nullable=True)
    obssituacao: Mapped[str] = mapped_column('obssituacao', String, nullable=True)
    tipooutlimofic: Mapped[str] = mapped_column('tipooutlimofic', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class MunicipioA(AlchemyGeoBase): 
    __tablename__ = 'lim_municipio_a'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    geocodigo: Mapped[str] = mapped_column('geocodigo', String, nullable=True)
    anodereferencia: Mapped[int] = mapped_column('anodereferencia', Integer, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class PaisA(AlchemyGeoBase): 
    __tablename__ = 'lim_pais_a'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    sigla: Mapped[str] = mapped_column('sigla', String, nullable=True)
    codiso3166: Mapped[str] = mapped_column('codiso3166', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


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
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    codigofunai: Mapped[int] = mapped_column('codigofunai', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class TerraIndigenaP(AlchemyGeoBase): 
    __tablename__ = 'lim_terra_indigena_p'
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
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    codigofunai: Mapped[int] = mapped_column('codigofunai', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class AldeiaIndigenaP(AlchemyGeoBase): 
    __tablename__ = 'loc_aldeia_indigena_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    codigofunai: Mapped[str] = mapped_column('codigofunai', String, nullable=True)
    terraindigena: Mapped[str] = mapped_column('terraindigena', String, nullable=True)
    etnia: Mapped[str] = mapped_column('etnia', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class UnidadeConservacaoNaoSnucA(AlchemyGeoBase): 
    __tablename__ = 'lim_unidade_conservacao_nao_snuc_a'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    anocriacao: Mapped[int] = mapped_column('anocriacao', Integer, nullable=True)
    sigla: Mapped[str] = mapped_column('sigla', String, nullable=True)
    areaoficial: Mapped[str] = mapped_column('areaoficial', String, nullable=True)
    administracao: Mapped[str] = mapped_column('administracao', String, nullable=True)
    classificacao: Mapped[str] = mapped_column('classificacao', String, nullable=True)
    atolegal: Mapped[str] = mapped_column('atolegal', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class UnidadeFederacaoA(AlchemyGeoBase): 
    __tablename__ = 'lim_unidade_federacao_a'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    sigla: Mapped[str] = mapped_column('sigla', String, nullable=True)
    geocodigo: Mapped[str] = mapped_column('geocodigo', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)
    iri_metadata: Mapped[str] = mapped_column('iri_metadata', String, nullable=True)
    iri_style: Mapped[str] = mapped_column('iri_style', String, nullable=True)


class UnidadeProtecaoIntegralA(AlchemyGeoBase): 
    __tablename__ = 'lim_unidade_protecao_integral_a'
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
    tipounidprotinteg: Mapped[str] = mapped_column('tipounidprotinteg', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


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
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class AglomeradoRuralIsoladoP(AlchemyGeoBase): 
    __tablename__ = 'loc_aglomerado_rural_isolado_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    tipoaglomrurisol: Mapped[str] = mapped_column('tipoaglomrurisol', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class CidadeP(AlchemyGeoBase): 
    __tablename__ = 'loc_cidade_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class AreaEdificadaA(AlchemyGeoBase): 
    __tablename__ = 'loc_area_edificada_a'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    geocodigo: Mapped[str] = mapped_column('geocodigo', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class CapitalP(AlchemyGeoBase): 
    __tablename__ = 'loc_capital_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    tipocapital: Mapped[str] = mapped_column('tipocapital', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class VilaP(AlchemyGeoBase): 
    __tablename__ = 'loc_vila_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class CurvaBatimetricaL(AlchemyGeoBase): 
    __tablename__ = 'rel_curva_batimetrica_l'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    profundidade: Mapped[int] = mapped_column('profundidade', Integer, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class CurvaNivelL(AlchemyGeoBase): 
    __tablename__ = 'rel_curva_nivel_l'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    cota: Mapped[int] = mapped_column('cota', Integer, nullable=True)
    depressao: Mapped[str] = mapped_column('depressao', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    indice: Mapped[str] = mapped_column('indice', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class DunaA(AlchemyGeoBase): 
    __tablename__ = 'rel_duna_a'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    fixa: Mapped[str] = mapped_column('fixa', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class ElementoFisiograficoNaturalL(AlchemyGeoBase): 
    __tablename__ = 'rel_elemento_fisiografico_natural_l'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    tipoelemnat: Mapped[str] = mapped_column('tipoelemnat', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class ElementoFisiograficoNaturalP(AlchemyGeoBase): 
    __tablename__ = 'rel_elemento_fisiografico_natural_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    tipoelemnat: Mapped[str] = mapped_column('tipoelemnat', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class PicoP(AlchemyGeoBase): 
    __tablename__ = 'rel_pico_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class PontoCotadoAltimetricoP(AlchemyGeoBase): 
    __tablename__ = 'rel_ponto_cotado_altimetrico_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    cota: Mapped[float] = mapped_column('cota', Double, nullable=True)
    cotacomprovada: Mapped[str] = mapped_column('cotacomprovada', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class PontoCotadoBatimetricoP(AlchemyGeoBase): 
    __tablename__ = 'rel_ponto_cotado_batimetrico_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    profundidade: Mapped[float] = mapped_column('profundidade', Double, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class EclusaL(AlchemyGeoBase): 
    __tablename__ = 'tra_eclusa_l'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    desnivel: Mapped[float] = mapped_column('desnivel', Double, nullable=True)
    largura: Mapped[float] = mapped_column('largura', Double, nullable=True)
    extensao: Mapped[float] = mapped_column('extensao', Double, nullable=True)
    calado: Mapped[float] = mapped_column('calado', Double, nullable=True)
    matconstr: Mapped[str] = mapped_column('matconstr', String, nullable=True)
    operacional: Mapped[str] = mapped_column('operacional', String, nullable=True)
    situacaofisica: Mapped[str] = mapped_column('situacaofisica', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class EdifConstAeroportuariaP(AlchemyGeoBase): 
    __tablename__ = 'tra_edif_const_aeroportuaria_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    operacional: Mapped[str] = mapped_column('operacional', String, nullable=True)
    situacaofisica: Mapped[str] = mapped_column('situacaofisica', String, nullable=True)
    administracao: Mapped[str] = mapped_column('administracao', String, nullable=True)
    matconstr: Mapped[str] = mapped_column('matconstr', String, nullable=True)
    tipoedifaero: Mapped[str] = mapped_column('tipoedifaero', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class EdifConstPortuariaP(AlchemyGeoBase): 
    __tablename__ = 'tra_edif_const_portuaria_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    tipoedifport: Mapped[str] = mapped_column('tipoedifport', String, nullable=True)
    administracao: Mapped[str] = mapped_column('administracao', String, nullable=True)
    matconstr: Mapped[str] = mapped_column('matconstr', String, nullable=True)
    operacional: Mapped[str] = mapped_column('operacional', String, nullable=True)
    situacaofisica: Mapped[str] = mapped_column('situacaofisica', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


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
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class EdifMetroFerroviariaP(AlchemyGeoBase): 
    __tablename__ = 'tra_edif_metro_ferroviaria_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    multimodal: Mapped[str] = mapped_column('multimodal', String, nullable=True)
    funcaoedifmetroferrov: Mapped[str] = mapped_column('funcaoedifmetroferrov', String, nullable=True)
    operacional: Mapped[str] = mapped_column('operacional', String, nullable=True)
    situacaofisica: Mapped[str] = mapped_column('situacaofisica', String, nullable=True)
    administracao: Mapped[str] = mapped_column('administracao', String, nullable=True)
    matconstr: Mapped[str] = mapped_column('matconstr', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class PistaPontoPousoP(AlchemyGeoBase): 
    __tablename__ = 'tra_pista_ponto_pouso_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    largura: Mapped[float] = mapped_column('largura', Double, nullable=True)
    extensao: Mapped[float] = mapped_column('extensao', Double, nullable=True)
    operacional: Mapped[str] = mapped_column('operacional', String, nullable=True)
    situacaofisica: Mapped[str] = mapped_column('situacaofisica', String, nullable=True)
    homologacao: Mapped[str] = mapped_column('homologacao', String, nullable=True)
    tipopista: Mapped[str] = mapped_column('tipopista', String, nullable=True)
    usopista: Mapped[str] = mapped_column('usopista', String, nullable=True)
    revestimento: Mapped[str] = mapped_column('revestimento', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class SinalizacaoP(AlchemyGeoBase): 
    __tablename__ = 'tra_sinalizacao_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    operacional: Mapped[str] = mapped_column('operacional', String, nullable=True)
    situacaofisica: Mapped[str] = mapped_column('situacaofisica', String, nullable=True)
    tiposinal: Mapped[str] = mapped_column('tiposinal', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class TravessiaL(AlchemyGeoBase): 
    __tablename__ = 'tra_travessia_l'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    tipotravessia: Mapped[str] = mapped_column('tipotravessia', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class TravessiaP(AlchemyGeoBase): 
    __tablename__ = 'tra_travessia_p'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    tipotravessia: Mapped[str] = mapped_column('tipotravessia', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class TrechoDutoL(AlchemyGeoBase): 
    __tablename__ = 'tra_trecho_duto_l'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    nrdutos: Mapped[int] = mapped_column('nrdutos', Integer, nullable=True)
    tipotrechoduto: Mapped[str] = mapped_column('tipotrechoduto', String, nullable=True)
    mattransp: Mapped[str] = mapped_column('mattransp', String, nullable=True)
    setor: Mapped[str] = mapped_column('setor', String, nullable=True)
    posicaorelativa: Mapped[str] = mapped_column('posicaorelativa', String, nullable=True)
    matconstr: Mapped[str] = mapped_column('matconstr', String, nullable=True)
    situacaoespacial: Mapped[str] = mapped_column('situacaoespacial', String, nullable=True)
    operacional: Mapped[str] = mapped_column('operacional', String, nullable=True)
    situacaofisica: Mapped[str] = mapped_column('situacaofisica', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class TrechoFerroviarioL(AlchemyGeoBase): 
    __tablename__ = 'tra_trecho_ferroviario_l'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    codtrechoferrov: Mapped[str] = mapped_column('codtrechoferrov', String, nullable=True)
    posicaorelativa: Mapped[str] = mapped_column('posicaorelativa', String, nullable=True)
    tipotrechoferrov: Mapped[str] = mapped_column('tipotrechoferrov', String, nullable=True)
    bitola: Mapped[str] = mapped_column('bitola', String, nullable=True)
    eletrificada: Mapped[str] = mapped_column('eletrificada', String, nullable=True)
    nrlinhas: Mapped[str] = mapped_column('nrlinhas', String, nullable=True)
    emarruamento: Mapped[str] = mapped_column('emarruamento', String, nullable=True)
    jurisdicao: Mapped[str] = mapped_column('jurisdicao', String, nullable=True)
    administracao: Mapped[str] = mapped_column('administracao', String, nullable=True)
    concessionaria: Mapped[str] = mapped_column('concessionaria', String, nullable=True)
    operacional: Mapped[str] = mapped_column('operacional', String, nullable=True)
    cargasuportmaxima: Mapped[float] = mapped_column('cargasuportmaxima', Double, nullable=True)
    situacaofisica: Mapped[str] = mapped_column('situacaofisica', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class TrechoHidroviarioL(AlchemyGeoBase): 
    __tablename__ = 'tra_trecho_hidroviario_l'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    extensaotrecho: Mapped[float] = mapped_column('extensaotrecho', Double, nullable=True)
    caladomaxseca: Mapped[float] = mapped_column('caladomaxseca', Double, nullable=True)
    operacional: Mapped[str] = mapped_column('operacional', String, nullable=True)
    situacaofisica: Mapped[str] = mapped_column('situacaofisica', String, nullable=True)
    regime: Mapped[str] = mapped_column('regime', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


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
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    canteirodivisorio: Mapped[str] = mapped_column('canteirodivisorio', String, nullable=True)


class TunelL(AlchemyGeoBase): 
    __tablename__ = 'tra_tunel_l'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    modaluso: Mapped[str] = mapped_column('modaluso', String, nullable=True)
    nrpistas: Mapped[int] = mapped_column('nrpistas', Integer, nullable=True)
    nrfaixas: Mapped[int] = mapped_column('nrfaixas', Integer, nullable=True)
    extensao: Mapped[float] = mapped_column('extensao', Double, nullable=True)
    altura: Mapped[float] = mapped_column('altura', Double, nullable=True)
    largura: Mapped[float] = mapped_column('largura', Double, nullable=True)
    posicaopista: Mapped[str] = mapped_column('posicaopista', String, nullable=True)
    situacaofisica: Mapped[str] = mapped_column('situacaofisica', String, nullable=True)
    operacional: Mapped[str] = mapped_column('operacional', String, nullable=True)
    matconstr: Mapped[str] = mapped_column('matconstr', String, nullable=True)
    tipotunel: Mapped[str] = mapped_column('tipotunel', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class BrejoPantanoA(AlchemyGeoBase): 
    __tablename__ = 'veg_brejo_pantano_a'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    alturamediaindividuos: Mapped[float] = mapped_column('alturamediaindividuos', Double, nullable=True)
    classificacaoporte: Mapped[str] = mapped_column('classificacaoporte', String, nullable=True)
    tipobrejopantano: Mapped[str] = mapped_column('tipobrejopantano', String, nullable=True)
    denso: Mapped[str] = mapped_column('denso', String, nullable=True)
    antropizada: Mapped[str] = mapped_column('antropizada', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class MangueA(AlchemyGeoBase): 
    __tablename__ = 'veg_mangue_a'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    alturamediaindividuos: Mapped[float] = mapped_column('alturamediaindividuos', Double, nullable=True)
    classificacaoporte: Mapped[str] = mapped_column('classificacaoporte', String, nullable=True)
    denso: Mapped[str] = mapped_column('denso', String, nullable=True)
    antropizada: Mapped[str] = mapped_column('antropizada', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)


class VegRestingaA(AlchemyGeoBase): 
    __tablename__ = 'veg_veg_restinga_a'
    __table_args__ = {'schema': 'bcim'}

    id_objeto: Mapped[int] = mapped_column('id_objeto', Integer, primary_key=True, nullable=False)
    nome: Mapped[str] = mapped_column('nome', String, nullable=True)
    nomeabrev: Mapped[str] = mapped_column('nomeabrev', String, nullable=True)
    geometriaaproximada: Mapped[str] = mapped_column('geometriaaproximada', String, nullable=True)
    alturamediaindividuos: Mapped[float] = mapped_column('alturamediaindividuos', Double, nullable=True)
    classificacaoporte: Mapped[str] = mapped_column('classificacaoporte', String, nullable=True)
    denso: Mapped[str] = mapped_column('denso', String, nullable=True)
    antropizada: Mapped[str] = mapped_column('antropizada', String, nullable=True)
    geom: Mapped[Geometry] = mapped_column('geom', Geometry, nullable=True)
    id_produtor: Mapped[int] = mapped_column('id_produtor', Integer, nullable=True)
    id_elementoprodutor: Mapped[int] = mapped_column('id_elementoprodutor', Integer, nullable=True)
    cd_insumo_orgao: Mapped[int] = mapped_column('cd_insumo_orgao', Integer, nullable=True)
    nr_insumo_mes: Mapped[int] = mapped_column('nr_insumo_mes', Integer, nullable=True)
    nr_insumo_ano: Mapped[int] = mapped_column('nr_insumo_ano', Integer, nullable=True)
    tx_insumo_documento: Mapped[str] = mapped_column('tx_insumo_documento', String, nullable=True)
