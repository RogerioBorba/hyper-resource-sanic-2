
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.terreno_sujeito_inundacao_a import TerrenoSujeitoInundacaoA
from src.contexts.terreno_sujeito_inundacao_a import TerrenoSujeitoInundacaoADetailContext, TerrenoSujeitoInundacaoACollectionContext

class TerrenoSujeitoInundacaoAResource(FeatureResource):
   model_class = TerrenoSujeitoInundacaoA
   context_class = TerrenoSujeitoInundacaoADetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return TerrenoSujeitoInundacaoA
        
class TerrenoSujeitoInundacaoACollectionResource(FeatureCollectionResource):
    model_class = TerrenoSujeitoInundacaoA
    context_class = TerrenoSujeitoInundacaoACollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return TerrenoSujeitoInundacaoA
