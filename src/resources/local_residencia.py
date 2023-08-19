
from src.hyper_resource.non_spatial_resource import NonSpatialResource
from src.hyper_resource.abstract_collection_resource import AbstractCollectionResource
from src.models.local_residencia import LocalResidencia
from src.contexts.local_residencia import LocalResidenciaDetailContext, LocalResidenciaCollectionContext

class LocalResidenciaResource(NonSpatialResource):
   model_class = LocalResidencia
   context_class = LocalResidenciaDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return LocalResidencia
        
class LocalResidenciaCollectionResource(AbstractCollectionResource):
    model_class = LocalResidencia
    context_class = LocalResidenciaCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return LocalResidencia
