
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.brejo_pantano_a import BrejoPantanoA
from src.contexts.brejo_pantano_a import BrejoPantanoADetailContext, BrejoPantanoACollectionContext

class BrejoPantanoAResource(FeatureResource):
   model_class = BrejoPantanoA
   context_class = BrejoPantanoADetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return BrejoPantanoA
        
class BrejoPantanoACollectionResource(FeatureCollectionResource):
    model_class = BrejoPantanoA
    context_class = BrejoPantanoACollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return BrejoPantanoA
