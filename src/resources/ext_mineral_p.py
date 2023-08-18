
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.ext_mineral_p import ExtMineralP
from src.contexts.ext_mineral_p import ExtMineralPDetailContext, ExtMineralPCollectionContext

class ExtMineralPResource(FeatureResource):
   model_class = ExtMineralP
   context_class = ExtMineralPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return ExtMineralP
        
class ExtMineralPCollectionResource(FeatureCollectionResource):
    model_class = ExtMineralP
    context_class = ExtMineralPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return ExtMineralP
