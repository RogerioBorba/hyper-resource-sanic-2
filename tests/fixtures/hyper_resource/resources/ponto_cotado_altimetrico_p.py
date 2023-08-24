
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.ponto_cotado_altimetrico_p import PontoCotadoAltimetricoP
from src.contexts.ponto_cotado_altimetrico_p import PontoCotadoAltimetricoPDetailContext, PontoCotadoAltimetricoPCollectionContext

class PontoCotadoAltimetricoPResource(FeatureResource):
   model_class = PontoCotadoAltimetricoP
   context_class = PontoCotadoAltimetricoPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return PontoCotadoAltimetricoP
        
class PontoCotadoAltimetricoPCollectionResource(FeatureCollectionResource):
    model_class = PontoCotadoAltimetricoP
    context_class = PontoCotadoAltimetricoPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return PontoCotadoAltimetricoP
