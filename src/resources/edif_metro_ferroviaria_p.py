
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.edif_metro_ferroviaria_p import EdifMetroFerroviariaP
from src.contexts.edif_metro_ferroviaria_p import EdifMetroFerroviariaPDetailContext, EdifMetroFerroviariaPCollectionContext

class EdifMetroFerroviariaPResource(FeatureResource):
   model_class = EdifMetroFerroviariaP
   context_class = EdifMetroFerroviariaPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return EdifMetroFerroviariaP
        
class EdifMetroFerroviariaPCollectionResource(FeatureCollectionResource):
    model_class = EdifMetroFerroviariaP
    context_class = EdifMetroFerroviariaPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return EdifMetroFerroviariaP
