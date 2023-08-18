
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.massa_dagua_a import MassaDaguaA
from src.contexts.massa_dagua_a import MassaDaguaADetailContext, MassaDaguaACollectionContext

class MassaDaguaAResource(FeatureResource):
   model_class = MassaDaguaA
   context_class = MassaDaguaADetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return MassaDaguaA
        
class MassaDaguaACollectionResource(FeatureCollectionResource):
    model_class = MassaDaguaA
    context_class = MassaDaguaACollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return MassaDaguaA
