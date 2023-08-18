
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.unidade_uso_sustentavel_a import UnidadeUsoSustentavelA
from src.contexts.unidade_uso_sustentavel_a import UnidadeUsoSustentavelADetailContext, UnidadeUsoSustentavelACollectionContext

class UnidadeUsoSustentavelAResource(FeatureResource):
   model_class = UnidadeUsoSustentavelA
   context_class = UnidadeUsoSustentavelADetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return UnidadeUsoSustentavelA
        
class UnidadeUsoSustentavelACollectionResource(FeatureCollectionResource):
    model_class = UnidadeUsoSustentavelA
    context_class = UnidadeUsoSustentavelACollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return UnidadeUsoSustentavelA
