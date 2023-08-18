
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.barragem_l import BarragemL
from src.contexts.barragem_l import BarragemLDetailContext, BarragemLCollectionContext

class BarragemLResource(FeatureResource):
   model_class = BarragemL
   context_class = BarragemLDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return BarragemL
        
class BarragemLCollectionResource(FeatureCollectionResource):
    model_class = BarragemL
    context_class = BarragemLCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return BarragemL
