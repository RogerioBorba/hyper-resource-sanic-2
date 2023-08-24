
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.trecho_massa_dagua_a import TrechoMassaDaguaA
from src.contexts.trecho_massa_dagua_a import TrechoMassaDaguaADetailContext, TrechoMassaDaguaACollectionContext

class TrechoMassaDaguaAResource(FeatureResource):
   model_class = TrechoMassaDaguaA
   context_class = TrechoMassaDaguaADetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return TrechoMassaDaguaA
        
class TrechoMassaDaguaACollectionResource(FeatureCollectionResource):
    model_class = TrechoMassaDaguaA
    context_class = TrechoMassaDaguaACollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return TrechoMassaDaguaA
