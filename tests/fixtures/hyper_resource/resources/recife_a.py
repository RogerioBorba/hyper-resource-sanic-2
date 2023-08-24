
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.recife_a import RecifeA
from src.contexts.recife_a import RecifeADetailContext, RecifeACollectionContext

class RecifeAResource(FeatureResource):
   model_class = RecifeA
   context_class = RecifeADetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return RecifeA
        
class RecifeACollectionResource(FeatureCollectionResource):
    model_class = RecifeA
    context_class = RecifeACollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return RecifeA
