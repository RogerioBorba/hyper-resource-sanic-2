
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.trecho_ferroviario_l import TrechoFerroviarioL
from src.contexts.trecho_ferroviario_l import TrechoFerroviarioLDetailContext, TrechoFerroviarioLCollectionContext

class TrechoFerroviarioLResource(FeatureResource):
   model_class = TrechoFerroviarioL
   context_class = TrechoFerroviarioLDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return TrechoFerroviarioL
        
class TrechoFerroviarioLCollectionResource(FeatureCollectionResource):
    model_class = TrechoFerroviarioL
    context_class = TrechoFerroviarioLCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return TrechoFerroviarioL
