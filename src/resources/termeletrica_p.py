
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.termeletrica_p import TermeletricaP
from src.contexts.termeletrica_p import TermeletricaPDetailContext, TermeletricaPCollectionContext

class TermeletricaPResource(FeatureResource):
   model_class = TermeletricaP
   context_class = TermeletricaPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return TermeletricaP
        
class TermeletricaPCollectionResource(FeatureCollectionResource):
    model_class = TermeletricaP
    context_class = TermeletricaPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return TermeletricaP
