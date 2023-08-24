
from src.hyper_resource.non_spatial_resource import NonSpatialResource
from src.hyper_resource.abstract_collection_resource import AbstractCollectionResource
from src.models.pessoa_grupo import PessoaGrupo
from src.contexts.pessoa_grupo import PessoaGrupoDetailContext, PessoaGrupoCollectionContext

class PessoaGrupoResource(NonSpatialResource):
   model_class = PessoaGrupo
   context_class = PessoaGrupoDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return PessoaGrupo
        
class PessoaGrupoCollectionResource(AbstractCollectionResource):
    model_class = PessoaGrupo
    context_class = PessoaGrupoCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return PessoaGrupo
