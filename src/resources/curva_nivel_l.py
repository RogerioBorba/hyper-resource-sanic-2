
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.curva_nivel_l import CurvaNivelL
from src.contexts.curva_nivel_l import CurvaNivelLDetailContext, CurvaNivelLCollectionContext

class CurvaNivelLResource(FeatureResource):
   model_class = CurvaNivelL
   context_class = CurvaNivelLDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return CurvaNivelL
        
class CurvaNivelLCollectionResource(FeatureCollectionResource):
    model_class = CurvaNivelL
    context_class = CurvaNivelLCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return CurvaNivelL
