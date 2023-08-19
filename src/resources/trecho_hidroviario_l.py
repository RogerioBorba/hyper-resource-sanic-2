
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.trecho_hidroviario_l import TrechoHidroviarioL
from src.contexts.trecho_hidroviario_l import TrechoHidroviarioLDetailContext, TrechoHidroviarioLCollectionContext

class TrechoHidroviarioLResource(FeatureResource):
   model_class = TrechoHidroviarioL
   context_class = TrechoHidroviarioLDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return TrechoHidroviarioL
        
class TrechoHidroviarioLCollectionResource(FeatureCollectionResource):
    model_class = TrechoHidroviarioL
    context_class = TrechoHidroviarioLCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return TrechoHidroviarioL
