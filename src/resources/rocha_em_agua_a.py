
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.rocha_em_agua_a import RochaEmAguaA
from src.contexts.rocha_em_agua_a import RochaEmAguaADetailContext, RochaEmAguaACollectionContext

class RochaEmAguaAResource(FeatureResource):
   model_class = RochaEmAguaA
   context_class = RochaEmAguaADetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return RochaEmAguaA
        
class RochaEmAguaACollectionResource(FeatureCollectionResource):
    model_class = RochaEmAguaA
    context_class = RochaEmAguaACollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return RochaEmAguaA
