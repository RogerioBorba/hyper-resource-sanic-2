
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.corredeira_l import CorredeiraL
from src.contexts.corredeira_l import CorredeiraLDetailContext, CorredeiraLCollectionContext

class CorredeiraLResource(FeatureResource):
   model_class = CorredeiraL
   context_class = CorredeiraLDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return CorredeiraL
        
class CorredeiraLCollectionResource(FeatureCollectionResource):
    model_class = CorredeiraL
    context_class = CorredeiraLCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return CorredeiraL
