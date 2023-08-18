
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.veg_restinga_a import VegRestingaA
from src.contexts.veg_restinga_a import VegRestingaADetailContext, VegRestingaACollectionContext

class VegRestingaAResource(FeatureResource):
   model_class = VegRestingaA
   context_class = VegRestingaADetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return VegRestingaA
        
class VegRestingaACollectionResource(FeatureCollectionResource):
    model_class = VegRestingaA
    context_class = VegRestingaACollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return VegRestingaA
