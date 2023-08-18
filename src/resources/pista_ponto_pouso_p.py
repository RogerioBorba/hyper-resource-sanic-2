
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.pista_ponto_pouso_p import PistaPontoPousoP
from src.contexts.pista_ponto_pouso_p import PistaPontoPousoPDetailContext, PistaPontoPousoPCollectionContext

class PistaPontoPousoPResource(FeatureResource):
   model_class = PistaPontoPousoP
   context_class = PistaPontoPousoPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return PistaPontoPousoP
        
class PistaPontoPousoPCollectionResource(FeatureCollectionResource):
    model_class = PistaPontoPousoP
    context_class = PistaPontoPousoPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return PistaPontoPousoP
