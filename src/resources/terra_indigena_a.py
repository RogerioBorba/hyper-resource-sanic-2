
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.terra_indigena_a import TerraIndigenaA
from src.contexts.terra_indigena_a import TerraIndigenaADetailContext, TerraIndigenaACollectionContext

class TerraIndigenaAResource(FeatureResource):
   model_class = TerraIndigenaA
   context_class = TerraIndigenaADetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return TerraIndigenaA
        
class TerraIndigenaACollectionResource(FeatureCollectionResource):
    model_class = TerraIndigenaA
    context_class = TerraIndigenaACollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return TerraIndigenaA
