
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.curva_batimetrica_l import CurvaBatimetricaL
from src.contexts.curva_batimetrica_l import CurvaBatimetricaLDetailContext, CurvaBatimetricaLCollectionContext

class CurvaBatimetricaLResource(FeatureResource):
   model_class = CurvaBatimetricaL
   context_class = CurvaBatimetricaLDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return CurvaBatimetricaL
        
class CurvaBatimetricaLCollectionResource(FeatureCollectionResource):
    model_class = CurvaBatimetricaL
    context_class = CurvaBatimetricaLCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return CurvaBatimetricaL
