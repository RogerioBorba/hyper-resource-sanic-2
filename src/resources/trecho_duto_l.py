
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.trecho_duto_l import TrechoDutoL
from src.contexts.trecho_duto_l import TrechoDutoLDetailContext, TrechoDutoLCollectionContext

class TrechoDutoLResource(FeatureResource):
   model_class = TrechoDutoL
   context_class = TrechoDutoLDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return TrechoDutoL
        
class TrechoDutoLCollectionResource(FeatureCollectionResource):
    model_class = TrechoDutoL
    context_class = TrechoDutoLCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return TrechoDutoL
