
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.aldeia_indigena_p import AldeiaIndigenaP
from src.contexts.aldeia_indigena_p import AldeiaIndigenaPDetailContext, AldeiaIndigenaPCollectionContext

class AldeiaIndigenaPResource(FeatureResource):
   model_class = AldeiaIndigenaP
   context_class = AldeiaIndigenaPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return AldeiaIndigenaP
        
class AldeiaIndigenaPCollectionResource(FeatureCollectionResource):
    model_class = AldeiaIndigenaP
    context_class = AldeiaIndigenaPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return AldeiaIndigenaP
