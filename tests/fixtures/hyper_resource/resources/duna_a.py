
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.duna_a import DunaA
from src.contexts.duna_a import DunaADetailContext, DunaACollectionContext

class DunaAResource(FeatureResource):
   model_class = DunaA
   context_class = DunaADetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return DunaA
        
class DunaACollectionResource(FeatureCollectionResource):
    model_class = DunaA
    context_class = DunaACollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return DunaA
