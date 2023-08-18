
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.ext_mineral_a import ExtMineralA
from src.contexts.ext_mineral_a import ExtMineralADetailContext, ExtMineralACollectionContext

class ExtMineralAResource(FeatureResource):
   model_class = ExtMineralA
   context_class = ExtMineralADetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return ExtMineralA
        
class ExtMineralACollectionResource(FeatureCollectionResource):
    model_class = ExtMineralA
    context_class = ExtMineralACollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return ExtMineralA
