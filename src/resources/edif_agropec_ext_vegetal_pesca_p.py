
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.edif_agropec_ext_vegetal_pesca_p import EdifAgropecExtVegetalPescaP
from src.contexts.edif_agropec_ext_vegetal_pesca_p import EdifAgropecExtVegetalPescaPDetailContext, EdifAgropecExtVegetalPescaPCollectionContext

class EdifAgropecExtVegetalPescaPResource(FeatureResource):
   model_class = EdifAgropecExtVegetalPescaP
   context_class = EdifAgropecExtVegetalPescaPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return EdifAgropecExtVegetalPescaP
        
class EdifAgropecExtVegetalPescaPCollectionResource(FeatureCollectionResource):
    model_class = EdifAgropecExtVegetalPescaP
    context_class = EdifAgropecExtVegetalPescaPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return EdifAgropecExtVegetalPescaP
