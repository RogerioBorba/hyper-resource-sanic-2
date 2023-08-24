
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.area_edificada_a import AreaEdificadaA
from src.contexts.area_edificada_a import AreaEdificadaADetailContext, AreaEdificadaACollectionContext

class AreaEdificadaAResource(FeatureResource):
   model_class = AreaEdificadaA
   context_class = AreaEdificadaADetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return AreaEdificadaA
        
class AreaEdificadaACollectionResource(FeatureCollectionResource):
    model_class = AreaEdificadaA
    context_class = AreaEdificadaACollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return AreaEdificadaA
