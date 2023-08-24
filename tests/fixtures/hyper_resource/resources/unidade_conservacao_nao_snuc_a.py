
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.unidade_conservacao_nao_snuc_a import UnidadeConservacaoNaoSnucA
from src.contexts.unidade_conservacao_nao_snuc_a import UnidadeConservacaoNaoSnucADetailContext, UnidadeConservacaoNaoSnucACollectionContext

class UnidadeConservacaoNaoSnucAResource(FeatureResource):
   model_class = UnidadeConservacaoNaoSnucA
   context_class = UnidadeConservacaoNaoSnucADetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return UnidadeConservacaoNaoSnucA
        
class UnidadeConservacaoNaoSnucACollectionResource(FeatureCollectionResource):
    model_class = UnidadeConservacaoNaoSnucA
    context_class = UnidadeConservacaoNaoSnucACollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return UnidadeConservacaoNaoSnucA
