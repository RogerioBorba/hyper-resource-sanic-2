
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.sinalizacao_p import SinalizacaoP
from src.contexts.sinalizacao_p import SinalizacaoPDetailContext, SinalizacaoPCollectionContext

class SinalizacaoPResource(FeatureResource):
   model_class = SinalizacaoP
   context_class = SinalizacaoPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return SinalizacaoP
        
class SinalizacaoPCollectionResource(FeatureCollectionResource):
    model_class = SinalizacaoP
    context_class = SinalizacaoPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return SinalizacaoP
