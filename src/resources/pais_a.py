
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.pais_a import PaisA
from src.contexts.pais_a import PaisADetailContext, PaisACollectionContext

class PaisAResource(FeatureResource):
   model_class = PaisA
   context_class = PaisADetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return PaisA
        
class PaisACollectionResource(FeatureCollectionResource):
    model_class = PaisA
    context_class = PaisACollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return PaisA
