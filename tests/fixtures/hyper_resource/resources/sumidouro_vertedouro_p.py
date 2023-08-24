
from src.hyper_resource.feature_resource import FeatureResource
from src.hyper_resource.feature_collection_resource import FeatureCollectionResource
from src.models.sumidouro_vertedouro_p import SumidouroVertedouroP
from src.contexts.sumidouro_vertedouro_p import SumidouroVertedouroPDetailContext, SumidouroVertedouroPCollectionContext

class SumidouroVertedouroPResource(FeatureResource):
   model_class = SumidouroVertedouroP
   context_class = SumidouroVertedouroPDetailContext
   def __init__(self, request):
        super().__init__(request)
    
   def entity_class(self):
       return SumidouroVertedouroP
        
class SumidouroVertedouroPCollectionResource(FeatureCollectionResource):
    model_class = SumidouroVertedouroP
    context_class = SumidouroVertedouroPCollectionContext    
    
    def __init__(self, request):
        super().__init__(request)
    
    def entity_class(self):
        return SumidouroVertedouroP
