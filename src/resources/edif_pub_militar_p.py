
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.edif_pub_militar_p import EdifPubMilitarP
from src.contexts.edif_pub_militar_p import EdifPubMilitarPDetailContext, EdifPubMilitarPCollectionContext

class EdifPubMilitarPResource(FeatureResource):
   model_class = EdifPubMilitarP
   context_class = EdifPubMilitarPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return EdifPubMilitarP
        
class EdifPubMilitarPCollectionResource(FeatureCollectionResource):
    model_class = EdifPubMilitarP
    context_class = EdifPubMilitarPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return EdifPubMilitarP
