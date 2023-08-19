
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.municipio_a import MunicipioA
from src.contexts.municipio_a import MunicipioADetailContext, MunicipioACollectionContext

class MunicipioAResource(FeatureResource):
   model_class = MunicipioA
   context_class = MunicipioADetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return MunicipioA
        
class MunicipioACollectionResource(FeatureCollectionResource):
    model_class = MunicipioA
    context_class = MunicipioACollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return MunicipioA
