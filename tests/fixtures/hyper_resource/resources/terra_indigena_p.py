
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.terra_indigena_p import TerraIndigenaP
from src.contexts.terra_indigena_p import TerraIndigenaPDetailContext, TerraIndigenaPCollectionContext

class TerraIndigenaPResource(FeatureResource):
   model_class = TerraIndigenaP
   context_class = TerraIndigenaPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return TerraIndigenaP
        
class TerraIndigenaPCollectionResource(FeatureCollectionResource):
    model_class = TerraIndigenaP
    context_class = TerraIndigenaPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return TerraIndigenaP
