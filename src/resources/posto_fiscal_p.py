
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.posto_fiscal_p import PostoFiscalP
from src.contexts.posto_fiscal_p import PostoFiscalPDetailContext, PostoFiscalPCollectionContext

class PostoFiscalPResource(FeatureResource):
   model_class = PostoFiscalP
   context_class = PostoFiscalPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return PostoFiscalP
        
class PostoFiscalPCollectionResource(FeatureCollectionResource):
    model_class = PostoFiscalP
    context_class = PostoFiscalPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return PostoFiscalP
