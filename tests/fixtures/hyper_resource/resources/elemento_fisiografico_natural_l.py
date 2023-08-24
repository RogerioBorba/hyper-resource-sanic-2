
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.elemento_fisiografico_natural_l import ElementoFisiograficoNaturalL
from src.contexts.elemento_fisiografico_natural_l import ElementoFisiograficoNaturalLDetailContext, ElementoFisiograficoNaturalLCollectionContext

class ElementoFisiograficoNaturalLResource(FeatureResource):
   model_class = ElementoFisiograficoNaturalL
   context_class = ElementoFisiograficoNaturalLDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return ElementoFisiograficoNaturalL
        
class ElementoFisiograficoNaturalLCollectionResource(FeatureCollectionResource):
    model_class = ElementoFisiograficoNaturalL
    context_class = ElementoFisiograficoNaturalLCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return ElementoFisiograficoNaturalL
