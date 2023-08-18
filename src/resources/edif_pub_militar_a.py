
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.edif_pub_militar_a import EdifPubMilitarA
from src.contexts.edif_pub_militar_a import EdifPubMilitarADetailContext, EdifPubMilitarACollectionContext

class EdifPubMilitarAResource(FeatureResource):
   model_class = EdifPubMilitarA
   context_class = EdifPubMilitarADetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return EdifPubMilitarA
        
class EdifPubMilitarACollectionResource(FeatureCollectionResource):
    model_class = EdifPubMilitarA
    context_class = EdifPubMilitarACollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return EdifPubMilitarA
