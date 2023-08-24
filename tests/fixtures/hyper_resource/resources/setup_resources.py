from src.hyper_resource.abstract_resource import AbstractResource
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

def setup_all_resources():
    AbstractResource.MAP_MODEL_FOR_CONTEXT = {
        AglomeradoRuralIsoladoPResource.model_class: AglomeradoRuralIsoladoPResource.context_class,
        AldeiaIndigenaPResource.model_class: AldeiaIndigenaPResource.context_class,
        AreaEdificadaAResource.model_class: AreaEdificadaAResource.context_class,
        BancoAreiaAResource.model_class: BancoAreiaAResource.context_class,
        BarragemLResource.model_class: BarragemLResource.context_class,
        BarragemPResource.model_class: BarragemPResource.context_class,
        BrejoPantanoAResource.model_class: BrejoPantanoAResource.context_class,
        CapitalPResource.model_class: CapitalPResource.context_class,
        CidadePResource.model_class: CidadePResource.context_class,
        CorredeiraLResource.model_class: CorredeiraLResource.context_class,
        CorredeiraPResource.model_class: CorredeiraPResource.context_class,
        CurvaBatimetricaLResource.model_class: CurvaBatimetricaLResource.context_class,
        CurvaNivelLResource.model_class: CurvaNivelLResource.context_class,
        DunaAResource.model_class: DunaAResource.context_class,
        EclusaLResource.model_class: EclusaLResource.context_class,
        EdifAgropecExtVegetalPescaPResource.model_class: EdifAgropecExtVegetalPescaPResource.context_class,
        EdifConstAeroportuariaPResource.model_class: EdifConstAeroportuariaPResource.context_class,
        EdifConstPortuariaPResource.model_class: EdifConstPortuariaPResource.context_class,
        EdifMetroFerroviariaPResource.model_class: EdifMetroFerroviariaPResource.context_class,
        EdifPubMilitarAResource.model_class: EdifPubMilitarAResource.context_class,
        EdifPubMilitarPResource.model_class: EdifPubMilitarPResource.context_class,
        ElementoFisiograficoNaturalLResource.model_class: ElementoFisiograficoNaturalLResource.context_class,
        ElementoFisiograficoNaturalPResource.model_class: ElementoFisiograficoNaturalPResource.context_class,
        EstGeradEnergiaEletricaPResource.model_class: EstGeradEnergiaEletricaPResource.context_class,
        ExtMineralAResource.model_class: ExtMineralAResource.context_class,
        ExtMineralPResource.model_class: ExtMineralPResource.context_class,
        GastoResource.model_class: GastoResource.context_class,
        GrupoResource.model_class: GrupoResource.context_class,
        HidreletricaPResource.model_class: HidreletricaPResource.context_class,
        IlhaAResource.model_class: IlhaAResource.context_class,
        LocalResidenciaResource.model_class: LocalResidenciaResource.context_class,
        MangueAResource.model_class: MangueAResource.context_class,
        MassaDaguaAResource.model_class: MassaDaguaAResource.context_class,
        MunicipioAResource.model_class: MunicipioAResource.context_class,
        OutrosLimitesOficiaisLResource.model_class: OutrosLimitesOficiaisLResource.context_class,
        PaisAResource.model_class: PaisAResource.context_class,
        PessoaResource.model_class: PessoaResource.context_class,
        PessoaGrupoResource.model_class: PessoaGrupoResource.context_class,
        PicoPResource.model_class: PicoPResource.context_class,
        PistaPontoPousoPResource.model_class: PistaPontoPousoPResource.context_class,
        PonteLResource.model_class: PonteLResource.context_class,
        PontoCotadoAltimetricoPResource.model_class: PontoCotadoAltimetricoPResource.context_class,
        PontoCotadoBatimetricoPResource.model_class: PontoCotadoBatimetricoPResource.context_class,
        PostoFiscalPResource.model_class: PostoFiscalPResource.context_class,
        QuedaDaguaLResource.model_class: QuedaDaguaLResource.context_class,
        RecifeAResource.model_class: RecifeAResource.context_class,
        RochaEmAguaAResource.model_class: RochaEmAguaAResource.context_class,
        SinalizacaoPResource.model_class: SinalizacaoPResource.context_class,
        SumidouroVertedouroPResource.model_class: SumidouroVertedouroPResource.context_class,
        TermeletricaPResource.model_class: TermeletricaPResource.context_class,
        TerraIndigenaAResource.model_class: TerraIndigenaAResource.context_class,
        TerraIndigenaPResource.model_class: TerraIndigenaPResource.context_class,
        TerrenoSujeitoInundacaoAResource.model_class: TerrenoSujeitoInundacaoAResource.context_class,
        TipoGastoResource.model_class: TipoGastoResource.context_class,
        TravessiaLResource.model_class: TravessiaLResource.context_class,
        TravessiaPResource.model_class: TravessiaPResource.context_class,
        TrechoDrenagemLResource.model_class: TrechoDrenagemLResource.context_class,
        TrechoDutoLResource.model_class: TrechoDutoLResource.context_class,
        TrechoFerroviarioLResource.model_class: TrechoFerroviarioLResource.context_class,
        TrechoHidroviarioLResource.model_class: TrechoHidroviarioLResource.context_class,
        TrechoMassaDaguaAResource.model_class: TrechoMassaDaguaAResource.context_class,
        TrechoRodoviarioLResource.model_class: TrechoRodoviarioLResource.context_class,
        TunelLResource.model_class: TunelLResource.context_class,
        UnidadeConservacaoNaoSnucAResource.model_class: UnidadeConservacaoNaoSnucAResource.context_class,
        UnidadeFederacaoAResource.model_class: UnidadeFederacaoAResource.context_class,
        UnidadeProtecaoIntegralAResource.model_class: UnidadeProtecaoIntegralAResource.context_class,
        UnidadeUsoSustentavelAResource.model_class: UnidadeUsoSustentavelAResource.context_class,
        VegRestingaAResource.model_class: VegRestingaAResource.context_class,
        VilaPResource.model_class: VilaPResource.context_class,
    }