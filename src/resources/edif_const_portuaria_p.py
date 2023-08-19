
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.edif_const_portuaria_p import EdifConstPortuariaP
from src.contexts.edif_const_portuaria_p import EdifConstPortuariaPDetailContext, EdifConstPortuariaPCollectionContext

class EdifConstPortuariaPResource(FeatureResource):
   model_class = EdifConstPortuariaP
   context_class = EdifConstPortuariaPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return EdifConstPortuariaP
        
class EdifConstPortuariaPCollectionResource(FeatureCollectionResource):
    model_class = EdifConstPortuariaP
    context_class = EdifConstPortuariaPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return EdifConstPortuariaP
