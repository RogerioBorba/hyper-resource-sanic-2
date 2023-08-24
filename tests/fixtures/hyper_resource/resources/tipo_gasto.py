
from src.hyper_resource.non_spatial_resource import NonSpatialResource
from src.hyper_resource.abstract_collection_resource import AbstractCollectionResource
from src.models.tipo_gasto import TipoGasto
from src.contexts.tipo_gasto import TipoGastoDetailContext, TipoGastoCollectionContext

class TipoGastoResource(NonSpatialResource):
   model_class = TipoGasto
   context_class = TipoGastoDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return TipoGasto
        
class TipoGastoCollectionResource(AbstractCollectionResource):
    model_class = TipoGasto
    context_class = TipoGastoCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return TipoGasto
