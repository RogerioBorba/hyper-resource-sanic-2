
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.unidade_protecao_integral_a import UnidadeProtecaoIntegralA
from src.contexts.unidade_protecao_integral_a import UnidadeProtecaoIntegralADetailContext, UnidadeProtecaoIntegralACollectionContext

class UnidadeProtecaoIntegralAResource(FeatureResource):
   model_class = UnidadeProtecaoIntegralA
   context_class = UnidadeProtecaoIntegralADetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return UnidadeProtecaoIntegralA
        
class UnidadeProtecaoIntegralACollectionResource(FeatureCollectionResource):
    model_class = UnidadeProtecaoIntegralA
    context_class = UnidadeProtecaoIntegralACollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return UnidadeProtecaoIntegralA
