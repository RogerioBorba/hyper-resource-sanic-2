
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.pico_p import PicoP
from src.contexts.pico_p import PicoPDetailContext, PicoPCollectionContext

class PicoPResource(FeatureResource):
   model_class = PicoP
   context_class = PicoPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return PicoP
        
class PicoPCollectionResource(FeatureCollectionResource):
    model_class = PicoP
    context_class = PicoPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return PicoP
