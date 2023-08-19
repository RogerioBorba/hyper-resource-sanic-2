
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.trecho_drenagem_l import TrechoDrenagemL
from src.contexts.trecho_drenagem_l import TrechoDrenagemLDetailContext, TrechoDrenagemLCollectionContext

class TrechoDrenagemLResource(FeatureResource):
   model_class = TrechoDrenagemL
   context_class = TrechoDrenagemLDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return TrechoDrenagemL
        
class TrechoDrenagemLCollectionResource(FeatureCollectionResource):
    model_class = TrechoDrenagemL
    context_class = TrechoDrenagemLCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return TrechoDrenagemL
