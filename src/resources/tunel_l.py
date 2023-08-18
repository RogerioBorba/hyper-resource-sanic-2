
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.tunel_l import TunelL
from src.contexts.tunel_l import TunelLDetailContext, TunelLCollectionContext

class TunelLResource(FeatureResource):
   model_class = TunelL
   context_class = TunelLDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return TunelL
        
class TunelLCollectionResource(FeatureCollectionResource):
    model_class = TunelL
    context_class = TunelLCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return TunelL
