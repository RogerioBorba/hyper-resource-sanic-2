
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.hidreletrica_p import HidreletricaP
from src.contexts.hidreletrica_p import HidreletricaPDetailContext, HidreletricaPCollectionContext

class HidreletricaPResource(FeatureResource):
   model_class = HidreletricaP
   context_class = HidreletricaPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return HidreletricaP
        
class HidreletricaPCollectionResource(FeatureCollectionResource):
    model_class = HidreletricaP
    context_class = HidreletricaPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return HidreletricaP
