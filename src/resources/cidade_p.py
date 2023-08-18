
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.cidade_p import CidadeP
from src.contexts.cidade_p import CidadePDetailContext, CidadePCollectionContext

class CidadePResource(FeatureResource):
   model_class = CidadeP
   context_class = CidadePDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return CidadeP
        
class CidadePCollectionResource(FeatureCollectionResource):
    model_class = CidadeP
    context_class = CidadePCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return CidadeP
