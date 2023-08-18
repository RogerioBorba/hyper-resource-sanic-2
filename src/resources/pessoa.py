
from src.hyper_resource.non_spatial_resource import NonSpatialResource
from src.hyper_resource.abstract_collection_resource import AbstractCollectionResource
from src.models.pessoa import Pessoa
from src.contexts.pessoa import PessoaDetailContext, PessoaCollectionContext

class PessoaResource(NonSpatialResource):
   model_class = Pessoa
   context_class = PessoaDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return Pessoa
        
class PessoaCollectionResource(AbstractCollectionResource):
    model_class = Pessoa
    context_class = PessoaCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return Pessoa
