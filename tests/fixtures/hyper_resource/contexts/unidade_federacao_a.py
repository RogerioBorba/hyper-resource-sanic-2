
from src.hyper_resource.context.geocontext import GeoDetailContext
from src.hyper_resource.context.geocontext import GeoCollectionContext

class UnidadeFederacaoACollectionContext(GeoCollectionContext):
    @staticmethod
    def get_type_by_model_class():
        return GeoCollectionContext.get_type_by_model_class()

class UnidadeFederacaoADetailContext(GeoDetailContext):
    @staticmethod
    def get_type_by_model_class():
        return GeoDetailContext.get_type_by_model_class()
