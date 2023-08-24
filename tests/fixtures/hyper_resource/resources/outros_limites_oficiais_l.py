
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.outros_limites_oficiais_l import OutrosLimitesOficiaisL
from src.contexts.outros_limites_oficiais_l import OutrosLimitesOficiaisLDetailContext, OutrosLimitesOficiaisLCollectionContext

class OutrosLimitesOficiaisLResource(FeatureResource):
   model_class = OutrosLimitesOficiaisL
   context_class = OutrosLimitesOficiaisLDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return OutrosLimitesOficiaisL
        
class OutrosLimitesOficiaisLCollectionResource(FeatureCollectionResource):
    model_class = OutrosLimitesOficiaisL
    context_class = OutrosLimitesOficiaisLCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return OutrosLimitesOficiaisL
