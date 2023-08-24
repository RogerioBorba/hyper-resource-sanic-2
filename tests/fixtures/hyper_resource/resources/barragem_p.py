
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.barragem_p import BarragemP
from src.contexts.barragem_p import BarragemPDetailContext, BarragemPCollectionContext

class BarragemPResource(FeatureResource):
   model_class = BarragemP
   context_class = BarragemPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return BarragemP
        
class BarragemPCollectionResource(FeatureCollectionResource):
    model_class = BarragemP
    context_class = BarragemPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return BarragemP
