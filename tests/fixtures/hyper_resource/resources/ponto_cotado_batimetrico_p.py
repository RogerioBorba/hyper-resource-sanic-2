
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.ponto_cotado_batimetrico_p import PontoCotadoBatimetricoP
from src.contexts.ponto_cotado_batimetrico_p import PontoCotadoBatimetricoPDetailContext, PontoCotadoBatimetricoPCollectionContext

class PontoCotadoBatimetricoPResource(FeatureResource):
   model_class = PontoCotadoBatimetricoP
   context_class = PontoCotadoBatimetricoPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return PontoCotadoBatimetricoP
        
class PontoCotadoBatimetricoPCollectionResource(FeatureCollectionResource):
    model_class = PontoCotadoBatimetricoP
    context_class = PontoCotadoBatimetricoPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return PontoCotadoBatimetricoP
