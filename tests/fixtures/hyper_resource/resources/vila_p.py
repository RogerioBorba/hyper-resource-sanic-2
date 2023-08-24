
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.vila_p import VilaP
from src.contexts.vila_p import VilaPDetailContext, VilaPCollectionContext

class VilaPResource(FeatureResource):
   model_class = VilaP
   context_class = VilaPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return VilaP
        
class VilaPCollectionResource(FeatureCollectionResource):
    model_class = VilaP
    context_class = VilaPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return VilaP
