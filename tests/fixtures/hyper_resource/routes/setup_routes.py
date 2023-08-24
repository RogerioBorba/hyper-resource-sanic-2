from src.hyper_resource.abstract_resource import AbstractResource
from src.routes.aglomerado_rural_isolado_p import aglomerado_rural_isolado_p_routes
from src.routes.aldeia_indigena_p import aldeia_indigena_p_routes
from src.routes.area_edificada_a import area_edificada_a_routes
from src.routes.banco_areia_a import banco_areia_a_routes
from src.routes.barragem_l import barragem_l_routes
from src.routes.barragem_p import barragem_p_routes
from src.routes.brejo_pantano_a import brejo_pantano_a_routes
from src.routes.capital_p import capital_p_routes
from src.routes.cidade_p import cidade_p_routes
from src.routes.corredeira_l import corredeira_l_routes
from src.routes.corredeira_p import corredeira_p_routes
from src.routes.curva_batimetrica_l import curva_batimetrica_l_routes
from src.routes.curva_nivel_l import curva_nivel_l_routes
from src.routes.duna_a import duna_a_routes
from src.routes.eclusa_l import eclusa_l_routes
from src.routes.edif_agropec_ext_vegetal_pesca_p import edif_agropec_ext_vegetal_pesca_p_routes
from src.routes.edif_const_aeroportuaria_p import edif_const_aeroportuaria_p_routes
from src.routes.edif_const_portuaria_p import edif_const_portuaria_p_routes
from src.routes.edif_metro_ferroviaria_p import edif_metro_ferroviaria_p_routes
from src.routes.edif_pub_militar_a import edif_pub_militar_a_routes
from src.routes.edif_pub_militar_p import edif_pub_militar_p_routes
from src.routes.elemento_fisiografico_natural_l import elemento_fisiografico_natural_l_routes
from src.routes.elemento_fisiografico_natural_p import elemento_fisiografico_natural_p_routes
from src.routes.est_gerad_energia_eletrica_p import est_gerad_energia_eletrica_p_routes
from src.routes.ext_mineral_a import ext_mineral_a_routes
from src.routes.ext_mineral_p import ext_mineral_p_routes
from src.routes.gasto import gasto_routes
from src.routes.grupo import grupo_routes
from src.routes.hidreletrica_p import hidreletrica_p_routes
from src.routes.ilha_a import ilha_a_routes
from src.routes.local_residencia import local_residencia_routes
from src.routes.mangue_a import mangue_a_routes
from src.routes.massa_dagua_a import massa_dagua_a_routes
from src.routes.municipio_a import municipio_a_routes
from src.routes.municipio_pib import municipio_pib_routes
from src.routes.outros_limites_oficiais_l import outros_limites_oficiais_l_routes
from src.routes.pais_a import pais_a_routes
from src.routes.pessoa import pessoa_routes
from src.routes.pessoa_grupo import pessoa_grupo_routes
from src.routes.pico_p import pico_p_routes
from src.routes.pista_ponto_pouso_p import pista_ponto_pouso_p_routes
from src.routes.ponte_l import ponte_l_routes
from src.routes.ponto_cotado_altimetrico_p import ponto_cotado_altimetrico_p_routes
from src.routes.ponto_cotado_batimetrico_p import ponto_cotado_batimetrico_p_routes
from src.routes.posto_fiscal_p import posto_fiscal_p_routes
from src.routes.queda_dagua_l import queda_dagua_l_routes
from src.routes.recife_a import recife_a_routes
from src.routes.rocha_em_agua_a import rocha_em_agua_a_routes
from src.routes.sinalizacao_p import sinalizacao_p_routes
from src.routes.sumidouro_vertedouro_p import sumidouro_vertedouro_p_routes
from src.routes.termeletrica_p import termeletrica_p_routes
from src.routes.terra_indigena_a import terra_indigena_a_routes
from src.routes.terra_indigena_p import terra_indigena_p_routes
from src.routes.terreno_sujeito_inundacao_a import terreno_sujeito_inundacao_a_routes
from src.routes.tipo_gasto import tipo_gasto_routes
from src.routes.travessia_l import travessia_l_routes
from src.routes.travessia_p import travessia_p_routes
from src.routes.trecho_drenagem_l import trecho_drenagem_l_routes
from src.routes.trecho_duto_l import trecho_duto_l_routes
from src.routes.trecho_ferroviario_l import trecho_ferroviario_l_routes
from src.routes.trecho_hidroviario_l import trecho_hidroviario_l_routes
from src.routes.trecho_massa_dagua_a import trecho_massa_dagua_a_routes
from src.routes.trecho_rodoviario_l import trecho_rodoviario_l_routes
from src.routes.tunel_l import tunel_l_routes
from src.routes.unidade_conservacao_nao_snuc_a import unidade_conservacao_nao_snuc_a_routes
from src.routes.unidade_federacao_a import unidade_federacao_a_routes
from src.routes.unidade_protecao_integral_a import unidade_protecao_integral_a_routes
from src.routes.unidade_uso_sustentavel_a import unidade_uso_sustentavel_a_routes
from src.routes.veg_restinga_a import veg_restinga_a_routes
from src.routes.vila_p import vila_p_routes
from src.resources.aglomerado_rural_isolado_p import AglomeradoRuralIsoladoPResource, AglomeradoRuralIsoladoPCollectionResource
from src.resources.aldeia_indigena_p import AldeiaIndigenaPResource, AldeiaIndigenaPCollectionResource
from src.resources.area_edificada_a import AreaEdificadaAResource, AreaEdificadaACollectionResource
from src.resources.banco_areia_a import BancoAreiaAResource, BancoAreiaACollectionResource
from src.resources.barragem_l import BarragemLResource, BarragemLCollectionResource
from src.resources.barragem_p import BarragemPResource, BarragemPCollectionResource
from src.resources.brejo_pantano_a import BrejoPantanoAResource, BrejoPantanoACollectionResource
from src.resources.capital_p import CapitalPResource, CapitalPCollectionResource
from src.resources.cidade_p import CidadePResource, CidadePCollectionResource
from src.resources.corredeira_l import CorredeiraLResource, CorredeiraLCollectionResource
from src.resources.corredeira_p import CorredeiraPResource, CorredeiraPCollectionResource
from src.resources.curva_batimetrica_l import CurvaBatimetricaLResource, CurvaBatimetricaLCollectionResource
from src.resources.curva_nivel_l import CurvaNivelLResource, CurvaNivelLCollectionResource
from src.resources.duna_a import DunaAResource, DunaACollectionResource
from src.resources.eclusa_l import EclusaLResource, EclusaLCollectionResource
from src.resources.edif_agropec_ext_vegetal_pesca_p import EdifAgropecExtVegetalPescaPResource, EdifAgropecExtVegetalPescaPCollectionResource
from src.resources.edif_const_aeroportuaria_p import EdifConstAeroportuariaPResource, EdifConstAeroportuariaPCollectionResource
from src.resources.edif_const_portuaria_p import EdifConstPortuariaPResource, EdifConstPortuariaPCollectionResource
from src.resources.edif_metro_ferroviaria_p import EdifMetroFerroviariaPResource, EdifMetroFerroviariaPCollectionResource
from src.resources.edif_pub_militar_a import EdifPubMilitarAResource, EdifPubMilitarACollectionResource
from src.resources.edif_pub_militar_p import EdifPubMilitarPResource, EdifPubMilitarPCollectionResource
from src.resources.elemento_fisiografico_natural_l import ElementoFisiograficoNaturalLResource, ElementoFisiograficoNaturalLCollectionResource
from src.resources.elemento_fisiografico_natural_p import ElementoFisiograficoNaturalPResource, ElementoFisiograficoNaturalPCollectionResource
from src.resources.est_gerad_energia_eletrica_p import EstGeradEnergiaEletricaPResource, EstGeradEnergiaEletricaPCollectionResource
from src.resources.ext_mineral_a import ExtMineralAResource, ExtMineralACollectionResource
from src.resources.ext_mineral_p import ExtMineralPResource, ExtMineralPCollectionResource
from src.resources.gasto import GastoResource, GastoCollectionResource
from src.resources.grupo import GrupoResource, GrupoCollectionResource
from src.resources.hidreletrica_p import HidreletricaPResource, HidreletricaPCollectionResource
from src.resources.ilha_a import IlhaAResource, IlhaACollectionResource
from src.resources.local_residencia import LocalResidenciaResource, LocalResidenciaCollectionResource
from src.resources.mangue_a import MangueAResource, MangueACollectionResource
from src.resources.massa_dagua_a import MassaDaguaAResource, MassaDaguaACollectionResource
from src.resources.municipio_a import MunicipioAResource, MunicipioACollectionResource
from src.resources.outros_limites_oficiais_l import OutrosLimitesOficiaisLResource, OutrosLimitesOficiaisLCollectionResource
from src.resources.pais_a import PaisAResource, PaisACollectionResource
from src.resources.pessoa import PessoaResource, PessoaCollectionResource
from src.resources.pessoa_grupo import PessoaGrupoResource, PessoaGrupoCollectionResource
from src.resources.pico_p import PicoPResource, PicoPCollectionResource
from src.resources.pista_ponto_pouso_p import PistaPontoPousoPResource, PistaPontoPousoPCollectionResource
from src.resources.ponte_l import PonteLResource, PonteLCollectionResource
from src.resources.ponto_cotado_altimetrico_p import PontoCotadoAltimetricoPResource, PontoCotadoAltimetricoPCollectionResource
from src.resources.ponto_cotado_batimetrico_p import PontoCotadoBatimetricoPResource, PontoCotadoBatimetricoPCollectionResource
from src.resources.posto_fiscal_p import PostoFiscalPResource, PostoFiscalPCollectionResource
from src.resources.queda_dagua_l import QuedaDaguaLResource, QuedaDaguaLCollectionResource
from src.resources.recife_a import RecifeAResource, RecifeACollectionResource
from src.resources.rocha_em_agua_a import RochaEmAguaAResource, RochaEmAguaACollectionResource
from src.resources.sinalizacao_p import SinalizacaoPResource, SinalizacaoPCollectionResource
from src.resources.sumidouro_vertedouro_p import SumidouroVertedouroPResource, SumidouroVertedouroPCollectionResource
from src.resources.termeletrica_p import TermeletricaPResource, TermeletricaPCollectionResource
from src.resources.terra_indigena_a import TerraIndigenaAResource, TerraIndigenaACollectionResource
from src.resources.terra_indigena_p import TerraIndigenaPResource, TerraIndigenaPCollectionResource
from src.resources.terreno_sujeito_inundacao_a import TerrenoSujeitoInundacaoAResource, TerrenoSujeitoInundacaoACollectionResource
from src.resources.tipo_gasto import TipoGastoResource, TipoGastoCollectionResource
from src.resources.travessia_l import TravessiaLResource, TravessiaLCollectionResource
from src.resources.travessia_p import TravessiaPResource, TravessiaPCollectionResource
from src.resources.trecho_drenagem_l import TrechoDrenagemLResource, TrechoDrenagemLCollectionResource
from src.resources.trecho_duto_l import TrechoDutoLResource, TrechoDutoLCollectionResource
from src.resources.trecho_ferroviario_l import TrechoFerroviarioLResource, TrechoFerroviarioLCollectionResource
from src.resources.trecho_hidroviario_l import TrechoHidroviarioLResource, TrechoHidroviarioLCollectionResource
from src.resources.trecho_massa_dagua_a import TrechoMassaDaguaAResource, TrechoMassaDaguaACollectionResource
from src.resources.trecho_rodoviario_l import TrechoRodoviarioLResource, TrechoRodoviarioLCollectionResource
from src.resources.tunel_l import TunelLResource, TunelLCollectionResource
from src.resources.unidade_conservacao_nao_snuc_a import UnidadeConservacaoNaoSnucAResource, UnidadeConservacaoNaoSnucACollectionResource
from src.resources.unidade_federacao_a import UnidadeFederacaoAResource, UnidadeFederacaoACollectionResource
from src.resources.unidade_protecao_integral_a import UnidadeProtecaoIntegralAResource, UnidadeProtecaoIntegralACollectionResource
from src.resources.unidade_uso_sustentavel_a import UnidadeUsoSustentavelAResource, UnidadeUsoSustentavelACollectionResource
from src.resources.veg_restinga_a import VegRestingaAResource, VegRestingaACollectionResource
from src.resources.vila_p import VilaPResource, VilaPCollectionResource
def setup_all_routes(app):
    aglomerado_rural_isolado_p_routes(app)
    aldeia_indigena_p_routes(app)
    area_edificada_a_routes(app)
    banco_areia_a_routes(app)
    barragem_l_routes(app)
    barragem_p_routes(app)
    brejo_pantano_a_routes(app)
    capital_p_routes(app)
    cidade_p_routes(app)
    corredeira_l_routes(app)
    corredeira_p_routes(app)
    curva_batimetrica_l_routes(app)
    curva_nivel_l_routes(app)
    duna_a_routes(app)
    eclusa_l_routes(app)
    edif_agropec_ext_vegetal_pesca_p_routes(app)
    edif_const_aeroportuaria_p_routes(app)
    edif_const_portuaria_p_routes(app)
    edif_metro_ferroviaria_p_routes(app)
    edif_pub_militar_a_routes(app)
    edif_pub_militar_p_routes(app)
    elemento_fisiografico_natural_l_routes(app)
    elemento_fisiografico_natural_p_routes(app)
    est_gerad_energia_eletrica_p_routes(app)
    ext_mineral_a_routes(app)
    ext_mineral_p_routes(app)
    gasto_routes(app)
    grupo_routes(app)
    hidreletrica_p_routes(app)
    ilha_a_routes(app)
    local_residencia_routes(app)
    mangue_a_routes(app)
    massa_dagua_a_routes(app)
    municipio_a_routes(app)
    municipio_pib_routes(app)
    outros_limites_oficiais_l_routes(app)
    pais_a_routes(app)
    pessoa_routes(app)
    pessoa_grupo_routes(app)
    pico_p_routes(app)
    pista_ponto_pouso_p_routes(app)
    ponte_l_routes(app)
    ponto_cotado_altimetrico_p_routes(app)
    ponto_cotado_batimetrico_p_routes(app)
    posto_fiscal_p_routes(app)
    queda_dagua_l_routes(app)
    recife_a_routes(app)
    rocha_em_agua_a_routes(app)
    sinalizacao_p_routes(app)
    sumidouro_vertedouro_p_routes(app)
    termeletrica_p_routes(app)
    terra_indigena_a_routes(app)
    terra_indigena_p_routes(app)
    terreno_sujeito_inundacao_a_routes(app)
    tipo_gasto_routes(app)
    travessia_l_routes(app)
    travessia_p_routes(app)
    trecho_drenagem_l_routes(app)
    trecho_duto_l_routes(app)
    trecho_ferroviario_l_routes(app)
    trecho_hidroviario_l_routes(app)
    trecho_massa_dagua_a_routes(app)
    trecho_rodoviario_l_routes(app)
    tunel_l_routes(app)
    unidade_conservacao_nao_snuc_a_routes(app)
    unidade_federacao_a_routes(app)
    unidade_protecao_integral_a_routes(app)
    unidade_uso_sustentavel_a_routes(app)
    veg_restinga_a_routes(app)
    vila_p_routes(app)
    
AbstractResource.MAP_MODEL_FOR_ROUTE = {
        AglomeradoRuralIsoladoPResource.model_class: aglomerado_rural_isolado_p_routes,
        AldeiaIndigenaPResource.model_class: aldeia_indigena_p_routes,
        AreaEdificadaAResource.model_class: area_edificada_a_routes,
        BancoAreiaAResource.model_class: banco_areia_a_routes,
        BarragemLResource.model_class: barragem_l_routes,
        BarragemPResource.model_class: barragem_p_routes,
        BrejoPantanoAResource.model_class: brejo_pantano_a_routes,
        CapitalPResource.model_class: capital_p_routes,
        CidadePResource.model_class: cidade_p_routes,
        CorredeiraLResource.model_class: corredeira_l_routes,
        CorredeiraPResource.model_class: corredeira_p_routes,
        CurvaBatimetricaLResource.model_class: curva_batimetrica_l_routes,
        CurvaNivelLResource.model_class: curva_nivel_l_routes,
        DunaAResource.model_class: duna_a_routes,
        EclusaLResource.model_class: eclusa_l_routes,
        EdifAgropecExtVegetalPescaPResource.model_class: edif_agropec_ext_vegetal_pesca_p_routes,
        EdifConstAeroportuariaPResource.model_class: edif_const_aeroportuaria_p_routes,
        EdifConstPortuariaPResource.model_class: edif_const_portuaria_p_routes,
        EdifMetroFerroviariaPResource.model_class: edif_metro_ferroviaria_p_routes,
        EdifPubMilitarAResource.model_class: edif_pub_militar_a_routes,
        EdifPubMilitarPResource.model_class: edif_pub_militar_p_routes,
        ElementoFisiograficoNaturalLResource.model_class: elemento_fisiografico_natural_l_routes,
        ElementoFisiograficoNaturalPResource.model_class: elemento_fisiografico_natural_p_routes,
        EstGeradEnergiaEletricaPResource.model_class: est_gerad_energia_eletrica_p_routes,
        ExtMineralAResource.model_class: ext_mineral_a_routes,
        ExtMineralPResource.model_class: ext_mineral_p_routes,
        GastoResource.model_class: gasto_routes,
        GrupoResource.model_class: grupo_routes,
        HidreletricaPResource.model_class: hidreletrica_p_routes,
        IlhaAResource.model_class: ilha_a_routes,
        LocalResidenciaResource.model_class: local_residencia_routes,
        MangueAResource.model_class: mangue_a_routes,
        MassaDaguaAResource.model_class: massa_dagua_a_routes,
        MunicipioAResource.model_class: municipio_a_routes,
        OutrosLimitesOficiaisLResource.model_class: outros_limites_oficiais_l_routes,
        PaisAResource.model_class: pais_a_routes,
        PessoaResource.model_class: pessoa_routes,
        PessoaGrupoResource.model_class: pessoa_grupo_routes,
        PicoPResource.model_class: pico_p_routes,
        PistaPontoPousoPResource.model_class: pista_ponto_pouso_p_routes,
        PonteLResource.model_class: ponte_l_routes,
        PontoCotadoAltimetricoPResource.model_class: ponto_cotado_altimetrico_p_routes,
        PontoCotadoBatimetricoPResource.model_class: ponto_cotado_batimetrico_p_routes,
        PostoFiscalPResource.model_class: posto_fiscal_p_routes,
        QuedaDaguaLResource.model_class: queda_dagua_l_routes,
        RecifeAResource.model_class: recife_a_routes,
        RochaEmAguaAResource.model_class: rocha_em_agua_a_routes,
        SinalizacaoPResource.model_class: sinalizacao_p_routes,
        SumidouroVertedouroPResource.model_class: sumidouro_vertedouro_p_routes,
        TermeletricaPResource.model_class: termeletrica_p_routes,
        TerraIndigenaAResource.model_class: terra_indigena_a_routes,
        TerraIndigenaPResource.model_class: terra_indigena_p_routes,
        TerrenoSujeitoInundacaoAResource.model_class: terreno_sujeito_inundacao_a_routes,
        TipoGastoResource.model_class: tipo_gasto_routes,
        TravessiaLResource.model_class: travessia_l_routes,
        TravessiaPResource.model_class: travessia_p_routes,
        TrechoDrenagemLResource.model_class: trecho_drenagem_l_routes,
        TrechoDutoLResource.model_class: trecho_duto_l_routes,
        TrechoFerroviarioLResource.model_class: trecho_ferroviario_l_routes,
        TrechoHidroviarioLResource.model_class: trecho_hidroviario_l_routes,
        TrechoMassaDaguaAResource.model_class: trecho_massa_dagua_a_routes,
        TrechoRodoviarioLResource.model_class: trecho_rodoviario_l_routes,
        TunelLResource.model_class: tunel_l_routes,
        UnidadeConservacaoNaoSnucAResource.model_class: unidade_conservacao_nao_snuc_a_routes,
        UnidadeFederacaoAResource.model_class: unidade_federacao_a_routes,
        UnidadeProtecaoIntegralAResource.model_class: unidade_protecao_integral_a_routes,
        UnidadeUsoSustentavelAResource.model_class: unidade_uso_sustentavel_a_routes,
        VegRestingaAResource.model_class: veg_restinga_a_routes,
        VilaPResource.model_class: vila_p_routes,
    }