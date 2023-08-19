
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.mangue_a import MangueA
from src.contexts.mangue_a import MangueADetailContext, MangueACollectionContext

class MangueAResource(FeatureResource):
   model_class = MangueA
   context_class = MangueADetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return MangueA
        
class MangueACollectionResource(FeatureCollectionResource):
    model_class = MangueA
    context_class = MangueACollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return MangueA
