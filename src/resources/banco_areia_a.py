
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.banco_areia_a import BancoAreiaA
from src.contexts.banco_areia_a import BancoAreiaADetailContext, BancoAreiaACollectionContext

class BancoAreiaAResource(FeatureResource):
   model_class = BancoAreiaA
   context_class = BancoAreiaADetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return BancoAreiaA
        
class BancoAreiaACollectionResource(FeatureCollectionResource):
    model_class = BancoAreiaA
    context_class = BancoAreiaACollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return BancoAreiaA
