
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.elemento_fisiografico_natural_p import ElementoFisiograficoNaturalP
from src.contexts.elemento_fisiografico_natural_p import ElementoFisiograficoNaturalPDetailContext, ElementoFisiograficoNaturalPCollectionContext

class ElementoFisiograficoNaturalPResource(FeatureResource):
   model_class = ElementoFisiograficoNaturalP
   context_class = ElementoFisiograficoNaturalPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return ElementoFisiograficoNaturalP
        
class ElementoFisiograficoNaturalPCollectionResource(FeatureCollectionResource):
    model_class = ElementoFisiograficoNaturalP
    context_class = ElementoFisiograficoNaturalPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return ElementoFisiograficoNaturalP
