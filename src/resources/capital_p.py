
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.capital_p import CapitalP
from src.contexts.capital_p import CapitalPDetailContext, CapitalPCollectionContext

class CapitalPResource(FeatureResource):
   model_class = CapitalP
   context_class = CapitalPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return CapitalP
        
class CapitalPCollectionResource(FeatureCollectionResource):
    model_class = CapitalP
    context_class = CapitalPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return CapitalP
