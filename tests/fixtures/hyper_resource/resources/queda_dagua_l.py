
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.queda_dagua_l import QuedaDaguaL
from src.contexts.queda_dagua_l import QuedaDaguaLDetailContext, QuedaDaguaLCollectionContext

class QuedaDaguaLResource(FeatureResource):
   model_class = QuedaDaguaL
   context_class = QuedaDaguaLDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return QuedaDaguaL
        
class QuedaDaguaLCollectionResource(FeatureCollectionResource):
    model_class = QuedaDaguaL
    context_class = QuedaDaguaLCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return QuedaDaguaL
