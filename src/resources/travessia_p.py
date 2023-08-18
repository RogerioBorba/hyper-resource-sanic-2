
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.travessia_p import TravessiaP
from src.contexts.travessia_p import TravessiaPDetailContext, TravessiaPCollectionContext

class TravessiaPResource(FeatureResource):
   model_class = TravessiaP
   context_class = TravessiaPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return TravessiaP
        
class TravessiaPCollectionResource(FeatureCollectionResource):
    model_class = TravessiaP
    context_class = TravessiaPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return TravessiaP
