
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.ilha_a import IlhaA
from src.contexts.ilha_a import IlhaADetailContext, IlhaACollectionContext

class IlhaAResource(FeatureResource):
   model_class = IlhaA
   context_class = IlhaADetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return IlhaA
        
class IlhaACollectionResource(FeatureCollectionResource):
    model_class = IlhaA
    context_class = IlhaACollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return IlhaA
