
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.trecho_rodoviario_l import TrechoRodoviarioL
from src.contexts.trecho_rodoviario_l import TrechoRodoviarioLDetailContext, TrechoRodoviarioLCollectionContext

class TrechoRodoviarioLResource(FeatureResource):
   model_class = TrechoRodoviarioL
   context_class = TrechoRodoviarioLDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return TrechoRodoviarioL
        
class TrechoRodoviarioLCollectionResource(FeatureCollectionResource):
    model_class = TrechoRodoviarioL
    context_class = TrechoRodoviarioLCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return TrechoRodoviarioL
