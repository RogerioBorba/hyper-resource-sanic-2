
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.unidade_federacao_a import UnidadeFederacaoA
from src.contexts.unidade_federacao_a import UnidadeFederacaoADetailContext, UnidadeFederacaoACollectionContext

class UnidadeFederacaoAResource(FeatureResource):
   model_class = UnidadeFederacaoA
   context_class = UnidadeFederacaoADetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return UnidadeFederacaoA
        
class UnidadeFederacaoACollectionResource(FeatureCollectionResource):
    model_class = UnidadeFederacaoA
    context_class = UnidadeFederacaoACollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return UnidadeFederacaoA
