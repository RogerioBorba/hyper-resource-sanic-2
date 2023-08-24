
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.edif_const_aeroportuaria_p import EdifConstAeroportuariaP
from src.contexts.edif_const_aeroportuaria_p import EdifConstAeroportuariaPDetailContext, EdifConstAeroportuariaPCollectionContext

class EdifConstAeroportuariaPResource(FeatureResource):
   model_class = EdifConstAeroportuariaP
   context_class = EdifConstAeroportuariaPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return EdifConstAeroportuariaP
        
class EdifConstAeroportuariaPCollectionResource(FeatureCollectionResource):
    model_class = EdifConstAeroportuariaP
    context_class = EdifConstAeroportuariaPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return EdifConstAeroportuariaP
