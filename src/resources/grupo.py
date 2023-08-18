
from src.hyper_resource.non_spatial_resource import NonSpatialResource
from src.hyper_resource.abstract_collection_resource import AbstractCollectionResource
from src.models.grupo import Grupo
from src.contexts.grupo import GrupoDetailContext, GrupoCollectionContext

class GrupoResource(NonSpatialResource):
   model_class = Grupo
   context_class = GrupoDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return Grupo
        
class GrupoCollectionResource(AbstractCollectionResource):
    model_class = Grupo
    context_class = GrupoCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return Grupo
