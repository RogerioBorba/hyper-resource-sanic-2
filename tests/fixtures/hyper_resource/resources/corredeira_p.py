
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.corredeira_p import CorredeiraP
from src.contexts.corredeira_p import CorredeiraPDetailContext, CorredeiraPCollectionContext

class CorredeiraPResource(FeatureResource):
   model_class = CorredeiraP
   context_class = CorredeiraPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return CorredeiraP
        
class CorredeiraPCollectionResource(FeatureCollectionResource):
    model_class = CorredeiraP
    context_class = CorredeiraPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return CorredeiraP
