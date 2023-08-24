
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.eclusa_l import EclusaL
from src.contexts.eclusa_l import EclusaLDetailContext, EclusaLCollectionContext

class EclusaLResource(FeatureResource):
   model_class = EclusaL
   context_class = EclusaLDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return EclusaL
        
class EclusaLCollectionResource(FeatureCollectionResource):
    model_class = EclusaL
    context_class = EclusaLCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return EclusaL
