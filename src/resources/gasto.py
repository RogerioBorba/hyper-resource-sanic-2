
from src.hyper_resource.non_spatial_resource import NonSpatialResource
from src.hyper_resource.abstract_collection_resource import AbstractCollectionResource
from src.models.gasto import Gasto
from src.contexts.gasto import GastoDetailContext, GastoCollectionContext

class GastoResource(NonSpatialResource):
   model_class = Gasto
   context_class = GastoDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return Gasto
        
class GastoCollectionResource(AbstractCollectionResource):
    model_class = Gasto
    context_class = GastoCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return Gasto
