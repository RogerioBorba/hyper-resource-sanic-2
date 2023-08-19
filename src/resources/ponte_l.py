
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.ponte_l import PonteL
from src.contexts.ponte_l import PonteLDetailContext, PonteLCollectionContext

class PonteLResource(FeatureResource):
   model_class = PonteL
   context_class = PonteLDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return PonteL
        
class PonteLCollectionResource(FeatureCollectionResource):
    model_class = PonteL
    context_class = PonteLCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return PonteL
