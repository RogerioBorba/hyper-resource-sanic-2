
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.est_gerad_energia_eletrica_p import EstGeradEnergiaEletricaP
from src.contexts.est_gerad_energia_eletrica_p import EstGeradEnergiaEletricaPDetailContext, EstGeradEnergiaEletricaPCollectionContext

class EstGeradEnergiaEletricaPResource(FeatureResource):
   model_class = EstGeradEnergiaEletricaP
   context_class = EstGeradEnergiaEletricaPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return EstGeradEnergiaEletricaP
        
class EstGeradEnergiaEletricaPCollectionResource(FeatureCollectionResource):
    model_class = EstGeradEnergiaEletricaP
    context_class = EstGeradEnergiaEletricaPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return EstGeradEnergiaEletricaP
