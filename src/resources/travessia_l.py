
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.travessia_l import TravessiaL
from src.contexts.travessia_l import TravessiaLDetailContext, TravessiaLCollectionContext

class TravessiaLResource(FeatureResource):
   model_class = TravessiaL
   context_class = TravessiaLDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return TravessiaL
        
class TravessiaLCollectionResource(FeatureCollectionResource):
    model_class = TravessiaL
    context_class = TravessiaLCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return TravessiaL
