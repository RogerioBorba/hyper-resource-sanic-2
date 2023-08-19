
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.aglomerado_rural_isolado_p import AglomeradoRuralIsoladoP
from src.contexts.aglomerado_rural_isolado_p import AglomeradoRuralIsoladoPDetailContext, AglomeradoRuralIsoladoPCollectionContext

class AglomeradoRuralIsoladoPResource(FeatureResource):
   model_class = AglomeradoRuralIsoladoP
   context_class = AglomeradoRuralIsoladoPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return AglomeradoRuralIsoladoP
        
class AglomeradoRuralIsoladoPCollectionResource(FeatureCollectionResource):
    model_class = AglomeradoRuralIsoladoP
    context_class = AglomeradoRuralIsoladoPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return AglomeradoRuralIsoladoP
